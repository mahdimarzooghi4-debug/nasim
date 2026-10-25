"""End-to-end read-only composition of the existing Provider foundation records."""

import base64
import json
import os
from uuid import UUID, uuid4

import httpx
import pytest
from pydantic import PostgresDsn
from sqlalchemy import func, select

from nasim.api.app import create_app, get_actor
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType
from nasim.infrastructure.config import Settings
from nasim.infrastructure.database import make_engine, make_sessions
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent
from nasim.provider_registry.contracts import (
    RecordProviderQualificationEvidence,
    RegisterProviderCandidate,
    RequestProviderQualificationReview,
)
from nasim.provider_registry.models import (
    ProviderCandidateRecord,
    ProviderQualificationEvidenceRecord,
    ProviderQualificationReviewRequestRecord,
)
from nasim.provider_registry.service import (
    ProviderCandidates,
    ProviderQualificationEvidence,
    ProviderQualificationReviewRequests,
    ProviderQualificationReviewWorkspace,
)

ALL_READ = frozenset(
    {
        "provider_candidate.read",
        "provider_qualification_evidence.read",
        "provider_qualification_review.read",
    }
)


@pytest.fixture
def reader() -> ActorContext:
    return ActorContext(
        actor_id="workspace-reviewer",
        actor_type=ActorType.HUMAN,
        capabilities=ALL_READ
        | {
            "provider_candidate.register",
            "provider_qualification_evidence.record",
            "provider_qualification_review.request",
        },
        correlation_id="workspace-test",
    )


@pytest.fixture
async def provider_services(admin_engine):
    url = os.environ.get("NASIM_TEST_APP_DATABASE_URL") or os.environ["NASIM_TEST_DATABASE_URL"]
    engine = make_engine(Settings(database_url=PostgresDsn(url)))
    sessions = make_sessions(engine)
    try:
        yield (
            ProviderCandidates(sessions),
            ProviderQualificationEvidence(sessions),
            ProviderQualificationReviewRequests(sessions),
            ProviderQualificationReviewWorkspace(sessions),
        )
    finally:
        await engine.dispose()


async def seed_candidate(services, reader: ActorContext, name: str) -> UUID:
    candidate = await services[0].register(
        RegisterProviderCandidate(display_name=name, reason="Read-only workspace setup"),
        reader,
        f"candidate-{uuid4()}",
    )
    return UUID(candidate["id"])


async def effect_counts(admin_engine) -> tuple[int, int, int, int, int, int]:
    async with admin_engine.connect() as connection:
        return (
            await connection.scalar(select(func.count()).select_from(ProviderCandidateRecord)),
            await connection.scalar(
                select(func.count()).select_from(ProviderQualificationEvidenceRecord)
            ),
            await connection.scalar(
                select(func.count()).select_from(ProviderQualificationReviewRequestRecord)
            ),
            await connection.scalar(select(func.count()).select_from(AuditEntry)),
            await connection.scalar(select(func.count()).select_from(OutboxEvent)),
            await connection.scalar(select(func.count()).select_from(IdempotencyRecord)),
        )


async def test_workspace_independent_pages_and_no_cross_candidate_data(
    provider_services, reader, admin_engine
):
    services = provider_services
    first = await seed_candidate(services, reader, "First candidate")
    second = await seed_candidate(services, reader, "Second candidate")
    for candidate in (first, second):
        for n in (1, 2):
            await services[1].record(
                candidate,
                RecordProviderQualificationEvidence(
                    evidence_label=f"Evidence {n}",
                    evidence_reference=f"opaque-{candidate}-{n}",
                    reason="descriptive only",
                ),
                reader,
                f"evidence-{candidate}-{n}",
            )
            await services[2].request(
                candidate,
                RequestProviderQualificationReview(reason=f"Review request {n}"),
                reader,
                f"request-{candidate}-{n}",
            )
    before = await effect_counts(admin_engine)
    page_one = await services[3].read(first, reader, limit=1)
    assert page_one.candidate.id == first
    assert page_one.evidence.next_cursor is not None
    assert page_one.review_requests.next_cursor is not None
    assert len(page_one.evidence.items) == len(page_one.review_requests.items) == 1
    assert page_one.evidence.items[0].provider_candidate_id == first
    assert page_one.review_requests.items[0].provider_candidate_id == first

    # Both cursors are separate; advancing evidence must not advance requests.
    evidence_two = await services[3].read(
        first, reader, evidence_cursor=page_one.evidence.next_cursor, limit=1
    )
    assert evidence_two.evidence.items[0].id != page_one.evidence.items[0].id
    assert evidence_two.review_requests.items[0].id == page_one.review_requests.items[0].id
    assert evidence_two.evidence.next_cursor is None

    requests_two = await services[3].read(
        first, reader, request_cursor=page_one.review_requests.next_cursor, limit=1
    )
    assert requests_two.review_requests.items[0].id != page_one.review_requests.items[0].id
    assert requests_two.evidence.items[0].id == page_one.evidence.items[0].id
    assert requests_two.review_requests.next_cursor is None

    other = await services[3].read(second, reader)
    assert all(x.provider_candidate_id == second for x in other.evidence.items)
    assert all(x.provider_candidate_id == second for x in other.review_requests.items)
    assert len(other.evidence.items) == len(other.review_requests.items) == 2
    assert await effect_counts(admin_engine) == before

    # No decision, status or implied activation field appears on the read model.
    payload = page_one.model_dump(mode="json")
    assert set(payload) == {"candidate", "evidence", "review_requests"}
    assert not any(key in payload for key in ("decision", "qualified", "approved", "active"))


@pytest.mark.parametrize("missing", sorted(ALL_READ))
async def test_workspace_requires_intersection_of_all_existing_read_capabilities(
    provider_services, reader, missing
):
    candidate = await seed_candidate(provider_services, reader, "Unauthorized")
    partial = reader.model_copy(update={"capabilities": reader.capabilities - {missing}})
    with pytest.raises(DomainError) as error:
        await provider_services[3].read(candidate, partial)
    assert error.value.code == "CAPABILITY_REQUIRED"
    assert error.value.status == 403


async def test_workspace_ai_is_denied_even_with_all_read_grants(provider_services, reader):
    candidate = await seed_candidate(provider_services, reader, "AI denied")
    with pytest.raises(DomainError) as error:
        await provider_services[3].read(
            candidate, reader.model_copy(update={"actor_type": ActorType.AI})
        )
    assert error.value.code == "CAPABILITY_REQUIRED"


async def test_workspace_missing_candidate_and_invalid_limits(provider_services, reader):
    with pytest.raises(DomainError) as error:
        await provider_services[3].read(uuid4(), reader)
    assert error.value.code == "PROVIDER_CANDIDATE_NOT_FOUND"

    candidate = await seed_candidate(provider_services, reader, "Limits")
    for limit in (0, 101, -1):
        with pytest.raises(DomainError) as error:
            await provider_services[3].read(candidate, reader, limit=limit)
        assert error.value.code == "INVALID_PAGE_LIMIT"
        assert error.value.status == 422
    for limit in (1, 100):
        result = await provider_services[3].read(candidate, reader, limit=limit)
        assert result.evidence.items == [] and result.review_requests.items == []


@pytest.mark.parametrize("slot", ["evidence", "request"])
async def test_workspace_malformed_cursor_fails_existing_contract(provider_services, reader, slot):
    candidate = await seed_candidate(provider_services, reader, "Invalid cursor")
    malformed = base64.urlsafe_b64encode(
        json.dumps(["2026-10-08T00:00:00+00:00", {"bad": "uuid"}]).encode()
    ).decode()
    kwargs = {"evidence_cursor": malformed} if slot == "evidence" else {"request_cursor": malformed}
    with pytest.raises(DomainError) as error:
        await provider_services[3].read(candidate, reader, **kwargs)
    assert error.value.code == "INVALID_CURSOR"
    assert error.value.status == 422


async def test_workspace_http_auth_and_openapi(provider_services, reader):
    candidate = await seed_candidate(provider_services, reader, "HTTP workspace")
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    route = f"/api/v1/provider-candidates/{candidate}/qualification-review-workspace"
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            anonymous = await client.get(route)
            assert anonymous.status_code == 401

            app.dependency_overrides[get_actor] = lambda: reader
            page = await client.get(route, params={"limit": 1})
            assert page.status_code == 200, page.text
            assert page.json()["candidate"]["id"] == str(candidate)
            assert set(page.json()) == {"candidate", "evidence", "review_requests"}
            assert (await client.get(route, params={"limit": 0})).status_code == 422
            spec = (await client.get("/openapi.json")).json()
            path = "/api/v1/provider-candidates/{candidate_id}/qualification-review-workspace"
            assert list(spec["paths"][path]) == ["get"]
            schema = spec["paths"][path]["get"]["responses"]["200"]["content"]["application/json"][
                "schema"
            ]
            assert "ProviderQualificationReviewWorkspaceView" in str(schema)
            for method in ("post", "patch", "put", "delete"):
                assert method not in spec["paths"][path]

            app.dependency_overrides[get_actor] = lambda: reader.model_copy(
                update={"capabilities": frozenset({"provider_candidate.read"})}
            )
            assert (await client.get(route)).status_code == 403
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()
