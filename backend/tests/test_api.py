import base64
import json
import os
from collections.abc import AsyncIterator
from datetime import UTC, datetime
from uuid import uuid4

import httpx
import pytest
from pydantic import PostgresDsn

from nasim.api.app import create_app, get_actor
from nasim.identity_context.contracts import ActorContext
from nasim.infrastructure.config import Settings

pytestmark = pytest.mark.integration


@pytest.fixture
async def api(admin_engine) -> AsyncIterator:
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    yield app
    await app.state.engine.dispose()


def as_actor(app, actor: ActorContext):
    # Test-only injection; no identity headers, development flag or bypass in production.
    app.dependency_overrides[get_actor] = lambda: actor


async def test_full_rest_case_journey(api, manager, caregiver):
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=api), base_url="http://test"
    ) as client:
        assert (await client.get("/health")).json() == {"status": "ok"}
        as_actor(api, manager)
        creation = {
            "upstream_enrollment_ref": "enrolled",
            "elder_reference": "elder",
            "initial_caregiver_actor_id": caregiver.actor_id,
        }
        response = await client.post(
            "/api/v1/cases", json=creation, headers={"Idempotency-Key": "create"}
        )
        assert response.status_code == 201, response.text
        original = response.json()
        case_id = original["case"]["id"]
        assignment_id = original["current_assignment"]["id"]
        base = f"/api/v1/cases/{case_id}"
        retry = await client.post(
            "/api/v1/cases", json=creation, headers={"Idempotency-Key": "create"}
        )
        assert retry.json() == original
        profile = await client.post(
            f"{base}/profile/corrections",
            json={
                "expected_current_assignment_id": assignment_id,
                "expected_current_revision_id": original["profile"]["id"],
                "elder_reference": "corrected-ref",
                "correction_reason": "transcription error",
            },
            headers={"Idempotency-Key": "profile"},
        )
        assert profile.status_code == 201, profile.text
        as_actor(api, caregiver)
        contact = await client.post(
            f"{base}/contacts",
            json={
                "expected_current_assignment_id": assignment_id,
                "contact_kind": "phone",
                "contact_value": "original-contact",
            },
            headers={"Idempotency-Key": "contact"},
        )
        assert contact.status_code == 201
        logical_id = contact.json()["logical_contact_id"]
        corrected = await client.post(
            f"{base}/contacts/{logical_id}/corrections",
            json={
                "expected_current_assignment_id": assignment_id,
                "expected_current_revision_id": contact.json()["id"],
                "contact_kind": "phone",
                "contact_value": "correct-contact",
                "correction_reason": "wrong number",
            },
            headers={"Idempotency-Key": "contact-correct"},
        )
        assert corrected.status_code == 201, corrected.text
        for kind, type_field, value in [
            ("interactions", "interaction_type", "MONITORING"),
            ("observations", "record_type", "NEED_CAPTURE"),
        ]:
            body = {
                "expected_current_assignment_id": assignment_id,
                type_field: value,
                "occurred_at": datetime.now(UTC).isoformat(),
                "content": "original note",
            }
            added = await client.post(
                f"{base}/{kind}", json=body, headers={"Idempotency-Key": kind}
            )
            assert added.status_code == 201, added.text
            corrected = await client.post(
                f"{base}/{kind}/{added.json()['id']}/corrections",
                json={
                    **body,
                    "content": "corrected note",
                    "expected_current_record_id": added.json()["id"],
                    "correction_reason": "clarification",
                },
                headers={"Idempotency-Key": f"{kind}-correct"},
            )
            assert corrected.status_code == 201, corrected.text
        for suffix in [
            "",
            "/workspace",
            "/contacts",
            "/assignments",
            "/interactions",
            "/observations",
            "/timeline",
        ]:
            response = await client.get(base + suffix)
            assert response.status_code == 200, response.text
        workspace = (await client.get(f"{base}/workspace")).json()
        assert workspace["profile"]["elder_reference"] == "corrected-ref"
        assert len(workspace["profile_history"]) == 2
        assert workspace["contacts"][0]["contact_value"] == "correct-contact"
        assert len(workspace["interactions"]) == len(workspace["observations"]) == 1
        bad_cursor = await client.get(f"{base}/timeline?cursor=invalid")
        assert bad_cursor.status_code == 422
        assert bad_cursor.json()["error"]["code"] == "INVALID_CURSOR"
        as_actor(api, manager)
        reassignment = await client.post(
            f"{base}/reassignments",
            json={
                "expected_current_assignment_id": assignment_id,
                "caregiver_actor_id": "next",
                "reason": "handoff",
            },
            headers={"Idempotency-Key": "reassign"},
        )
        assert reassignment.status_code == 201, reassignment.text
        stale = await client.post(
            f"{base}/reassignments",
            json={
                "expected_current_assignment_id": assignment_id,
                "caregiver_actor_id": "other",
                "reason": "handoff",
            },
            headers={"Idempotency-Key": "stale"},
        )
        assert stale.status_code == 409
        assert stale.json()["error"]["code"] == "CASE_ASSIGNMENT_CHANGED"
        as_actor(api, caregiver)
        denied = await client.get(base)
        assert denied.status_code == 403
        assert denied.json()["error"]["code"] == "ASSIGNED_CAREGIVER_REQUIRED"


@pytest.mark.parametrize(
    "suffix",
    [
        "profile/corrections",
        "reassignments",
        "contacts",
        "contacts/{id}/corrections",
        "interactions",
        "interactions/{id}/corrections",
        "observations",
        "observations/{id}/corrections",
    ],
)
async def test_all_existing_case_mutations_deny_missing_actor(api, suffix):
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=api), base_url="http://test"
    ) as client:
        response = await client.post(
            f"/api/v1/cases/{uuid4()}/{suffix.replace('{id}', str(uuid4()))}",
            json={},
            headers={"Idempotency-Key": "key"},
        )
    assert response.status_code == 401
    assert response.json()["error"]["code"] == "ACTOR_CONTEXT_REQUIRED"


async def test_rest_validation_no_leak_and_scope_denial(api, manager):
    as_actor(api, manager)
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=api), base_url="http://test"
    ) as client:
        body = {
            "upstream_enrollment_ref": "enrolled",
            "elder_reference": "private-elder",
            "initial_caregiver_actor_id": "caregiver",
        }
        missing_key = await client.post("/api/v1/cases", json=body)
        assert missing_key.status_code == 422
        assert missing_key.json()["error"]["code"] == "VALIDATION_ERROR"
        assert "private-elder" not in missing_key.text
        unsupported = await client.post(
            "/api/v1/cases", json={**body, "eligibility": True}, headers={"Idempotency-Key": "key"}
        )
        assert unsupported.status_code == 422
        for path in ["enrollments", "referrals", "providers", "outcomes", "emergencies", "ai"]:
            assert (await client.post(f"/api/v1/{path}", json={})).status_code == 404
        assert (await client.delete(f"/api/v1/cases/{uuid4()}")).status_code == 405
        assert (await client.patch(f"/api/v1/cases/{uuid4()}", json={})).status_code == 405


@pytest.mark.parametrize("read_kind", ["case", "referral", "provider"])
@pytest.mark.parametrize(
    "payload",
    [
        ["2026-10-08T12:00:00+00:00", 123],
        [123, "123e4567-e89b-12d3-a456-426614174000"],
    ],
)
async def test_malformed_cursor_http_contract_across_existing_reads(
    api, manager, read_kind, payload
):
    """Shared cursor parser must return 422 through all approved HTTP read contexts."""
    token = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()
    as_actor(api, manager)
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=api), base_url="http://test"
    ) as client:
        created = await client.post(
            "/api/v1/cases",
            json={
                "upstream_enrollment_ref": "enrolled-test",
                "elder_reference": "synthetic-test-ref",
                "initial_caregiver_actor_id": "caregiver-test",
            },
            headers={"Idempotency-Key": "create-for-cursor-regression"},
        )
        assert created.status_code == 201, created.text
        case_id = created.json()["case"]["id"]
        if read_kind == "case":
            path = f"/api/v1/cases/{case_id}/timeline"
        elif read_kind == "referral":
            path = f"/api/v1/cases/{case_id}/referrals"
            as_actor(
                api,
                manager.model_copy(
                    update={"capabilities": manager.capabilities | {"referral.read.oversight"}}
                ),
            )
        else:
            path = "/api/v1/provider-candidates"
            as_actor(
                api,
                manager.model_copy(
                    update={"capabilities": manager.capabilities | {"provider_candidate.read"}}
                ),
            )
        response = await client.get(path, params={"cursor": token})
        assert response.status_code == 422, response.text
        assert response.json()["error"]["code"] == "INVALID_CURSOR"
        assert "synthetic-test-ref" not in response.text
