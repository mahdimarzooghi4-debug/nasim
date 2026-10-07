from uuid import uuid4

import httpx
import pytest
from pydantic import PostgresDsn

from nasim.api.app import create_app
from nasim.infrastructure.config import Settings


def app_without_db():
    return create_app(Settings(database_url=PostgresDsn("postgresql://unused@127.0.0.1:1/unused")))


EXPECTED = {
    "/api/v1/authorization/self": {"get"},
    "/health": {"get"},
    "/api/v1/provider-candidates": {"get", "post"},
    "/api/v1/provider-candidates/{candidate_id}": {"get"},
    "/api/v1/provider-candidates/{candidate_id}/qualification-evidence": {"get", "post"},
    "/api/v1/provider-qualification-evidence/{evidence_id}": {"get"},
    "/api/v1/cases/{case_id}/referrals": {"get", "post"},
    "/api/v1/referrals/{referral_id}": {"get"},
    "/api/v1/cases": {"post"},
    "/api/v1/cases/{case_id}": {"get"},
    "/api/v1/cases/{case_id}/workspace": {"get"},
    "/api/v1/cases/{case_id}/profile/corrections": {"post"},
    "/api/v1/cases/{case_id}/reassignments": {"post"},
    "/api/v1/cases/{case_id}/assignments": {"get"},
    "/api/v1/cases/{case_id}/contacts": {"get", "post"},
    "/api/v1/cases/{case_id}/contacts/{logical_contact_id}/corrections": {"post"},
    "/api/v1/cases/{case_id}/interactions": {"get", "post"},
    "/api/v1/cases/{case_id}/interactions/{interaction_id}/corrections": {"post"},
    "/api/v1/cases/{case_id}/observations": {"get", "post"},
    "/api/v1/cases/{case_id}/observations/{observation_id}/corrections": {"post"},
    "/api/v1/cases/{case_id}/timeline": {"get"},
}


def test_exact_openapi_route_surface():
    paths = app_without_db().openapi()["paths"]
    assert {path: set(methods) for path, methods in paths.items()} == EXPECTED
    for _path, methods in paths.items():
        for method, operation in methods.items():
            assert (
                "schema"
                in operation["responses"]["200" if method == "get" else "201"]["content"][
                    "application/json"
                ]
            )
            if method == "post":
                header = next(p for p in operation["parameters"] if p["name"] == "Idempotency-Key")
                assert header["required"]
                assert "requestBody" in operation
                for code in [
                    "CASE_ASSIGNMENT_CHANGED",
                    "STALE_RECORD_REVISION",
                    "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD",
                ]:
                    assert code in operation["responses"]["409"]["description"]


def test_schema_snapshot():
    schemas = app_without_db().openapi()["components"]["schemas"]
    assert set(schemas["CreateCase"]["required"]) == {
        "upstream_enrollment_ref",
        "elder_reference",
        "initial_caregiver_actor_id",
    }
    assert set(schemas["RecordObservation"]["properties"]) == {
        "expected_current_assignment_id",
        "record_type",
        "occurred_at",
        "content",
    }
    assert schemas["RecordObservation"]["additionalProperties"] is False
    assert schemas["RecordInteraction"]["properties"]["interaction_type"]["enum"] == [
        "CONTACT",
        "MONITORING",
    ]
    assert schemas["RecordObservation"]["properties"]["record_type"]["enum"] == [
        "OBSERVATION",
        "NEED_CAPTURE",
    ]
    for name in [
        "CorrectCaseProfile",
        "CorrectContactPoint",
        "CorrectInteraction",
        "CorrectObservation",
    ]:
        assert "correction_reason" in schemas[name]["required"]
        assert "expected_current_assignment_id" in schemas[name]["required"]
    assert schemas["CaseView"]["properties"].keys() == {
        "id",
        "upstream_enrollment_ref",
        "created_at",
        "created_by_actor_id",
        "created_by_actor_type",
    }
    assert set(schemas["RegisterProviderCandidate"]["required"]) == {
        "display_name",
        "reason",
    }
    assert set(schemas["RegisterProviderCandidate"]["properties"]) == {
        "display_name",
        "reason",
    }
    assert schemas["RegisterProviderCandidate"]["additionalProperties"] is False
    assert set(schemas["RecordProviderQualificationEvidence"]["required"]) == {
        "evidence_label",
        "evidence_reference",
        "reason",
    }
    assert set(schemas["RecordProviderQualificationEvidence"]["properties"]) == {
        "evidence_label",
        "evidence_reference",
        "reason",
    }
    assert schemas["RecordProviderQualificationEvidence"]["additionalProperties"] is False


@pytest.mark.parametrize(
    "path", [p for p in EXPECTED if p.startswith("/api") and "get" in EXPECTED[p]]
)
async def test_every_read_fails_closed_without_context(path):
    app = app_without_db()
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get(
            path.replace("{case_id}", str(uuid4()))
            .replace("{referral_id}", str(uuid4()))
            .replace("{candidate_id}", str(uuid4()))
            .replace("{evidence_id}", str(uuid4())),
            headers={
                "X-Actor-Id": "caregiver-a",
                "X-Capabilities": "case.read.oversight",
                "Authorization": "Bearer invented",
            },
        )
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "ACTOR_CONTEXT_REQUIRED"
    await app.state.engine.dispose()


async def test_create_fails_closed_without_context():
    app = app_without_db()
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.post(
            "/api/v1/cases",
            json={
                "upstream_enrollment_ref": "enrolled",
                "elder_reference": "elder",
                "initial_caregiver_actor_id": "caregiver",
            },
            headers={"Idempotency-Key": "key"},
        )
    assert response.status_code == 401
    await app.state.engine.dispose()
