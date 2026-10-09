"""Real PostgreSQL/HTTP coverage for assignment-scoped Case index."""

import base64
import json
import os
from uuid import UUID

import httpx
import pytest
from pydantic import PostgresDsn
from sqlalchemy import func, select

from nasim.api.app import create_app, get_actor
from nasim.application.case_index import AssignedCaseIndex
from nasim.domain.contracts import CorrectCaseProfile, CreateCase, ReassignCaregiver
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorType
from nasim.infrastructure.config import Settings
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent

pytestmark = pytest.mark.integration


@pytest.fixture
async def indexed_cases(service, manager, caregiver):
    """Two currently assigned to caregiver-a; one to a different human."""
    records = []
    owners = (caregiver.actor_id, "unassigned-human", caregiver.actor_id)
    for n, owner in enumerate(owners):
        result = await service.mutate(
            "create",
            CreateCase(
                upstream_enrollment_ref=f"preexisting-enrollment-{n}",
                elder_reference=f"opaque-elder-{n}",
                initial_caregiver_actor_id=owner,
            ),
            manager,
            f"index-case-{n}",
        )
        records.append(result)
    return AssignedCaseIndex(service.sessions), records


async def effect_counts(admin_engine):
    async with admin_engine.connect() as conn:
        return (
            await conn.scalar(select(func.count()).select_from(AuditEntry)),
            await conn.scalar(select(func.count()).select_from(OutboxEvent)),
            await conn.scalar(select(func.count()).select_from(IdempotencyRecord)),
        )


async def test_assigned_index_is_bounded_and_uses_latest_profile(
    indexed_cases, service, manager, caregiver, admin_engine
):
    index, created = indexed_cases
    first = created[0]
    case_id = UUID(first["case"]["id"])
    await service.mutate(
        "profile_correct",
        CorrectCaseProfile(
            expected_current_assignment_id=UUID(first["current_assignment"]["id"]),
            expected_current_revision_id=UUID(first["profile"]["id"]),
            elder_reference="corrected-opaque-profile",
            correction_reason="Human corrected transcription",
        ),
        manager,
        "index-correct",
        case_id,
    )
    before = await effect_counts(admin_engine)
    page = await index.list(caregiver, limit=1)
    assert len(page.items) == 1 and page.next_cursor
    last = await index.list(caregiver, cursor=page.next_cursor, limit=1)
    assert len(last.items) == 1 and last.next_cursor is None
    combined = page.items + last.items
    ids = {row.case.id for row in combined}
    assert ids == {UUID(created[0]["case"]["id"]), UUID(created[2]["case"]["id"])}
    assert UUID(created[1]["case"]["id"]) not in ids
    assert all(row.current_assignment.caregiver_actor_id == caregiver.actor_id for row in combined)
    assert [str(row.case.id) for row in combined] == [
        str(row.case.id)
        for row in sorted(combined, key=lambda row: (row.case.created_at, row.case.id))
    ]
    assert next(row.profile.elder_reference for row in combined if row.case.id == case_id) == (
        "corrected-opaque-profile"
    )
    assert await effect_counts(admin_engine) == before


async def test_oversight_requires_explicit_read_capability(indexed_cases, manager, caregiver):
    index, created = indexed_cases
    # Managing assignments is not permission to view a Case index.
    only_manager = manager.model_copy(
        update={"capabilities": frozenset({"case.assignment.manage"})}
    )
    with pytest.raises(DomainError) as error:
        await index.list(only_manager)
    assert error.value.code == "CAPABILITY_REQUIRED"
    oversight = await index.list(manager, limit=100)
    assert {row.case.id for row in oversight.items} == {UUID(x["case"]["id"]) for x in created}
    no_read = caregiver.model_copy(update={"capabilities": frozenset({"case.monitor.assigned"})})
    with pytest.raises(DomainError) as error:
        await index.list(no_read)
    assert error.value.status == 403
    ai = manager.model_copy(update={"actor_type": ActorType.AI})
    with pytest.raises(DomainError) as error:
        await index.list(ai)
    assert error.value.status == 403


async def test_assignment_revoke_immediately_removes_case_from_index(
    indexed_cases, service, manager, caregiver, admin_engine
):
    index, created = indexed_cases
    case_id = UUID(created[0]["case"]["id"])
    assert case_id in {row.case.id for row in (await index.list(caregiver)).items}
    await service.mutate(
        "reassign",
        ReassignCaregiver(
            expected_current_assignment_id=UUID(created[0]["current_assignment"]["id"]),
            caregiver_actor_id="new-owner",
            reason="Explicit human reassignment",
        ),
        manager,
        "index-reassignment",
        case_id,
    )
    before = await effect_counts(admin_engine)
    assert case_id not in {row.case.id for row in (await index.list(caregiver)).items}
    replacement = caregiver.model_copy(update={"actor_id": "new-owner"})
    assert {row.case.id for row in (await index.list(replacement)).items} == {case_id}
    assert await effect_counts(admin_engine) == before


async def test_pagination_fail_closed_and_empty_case_list(indexed_cases, caregiver):
    index, _ = indexed_cases
    for bad in (0, 101, -1):
        with pytest.raises(DomainError) as error:
            await index.list(caregiver, limit=bad)
        assert error.value.code == "INVALID_PAGE_LIMIT"

    malformed = base64.urlsafe_b64encode(
        json.dumps(["2026-10-09T00:00:00+00:00", {"not": "uuid"}]).encode()
    ).decode()
    for token in (malformed, "bad", "a" * 500):
        with pytest.raises(DomainError) as error:
            await index.list(caregiver, cursor=token)
        assert error.value.code == "INVALID_CURSOR"
    outsider = caregiver.model_copy(update={"actor_id": "no-current-assignments"})
    empty = await index.list(outsider)
    assert empty.items == [] and empty.next_cursor is None


async def test_http_index_auth_query_and_exact_response(indexed_cases, manager, caregiver):
    _, created = indexed_cases
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            anonymous = await client.get("/api/v1/cases")
            assert anonymous.status_code == 401
            app.dependency_overrides[get_actor] = lambda: caregiver
            response = await client.get("/api/v1/cases", params={"limit": 1})
            assert response.status_code == 200, response.text
            assert set(response.json()) == {"items", "next_cursor"}
            assert set(response.json()["items"][0]) == {"case", "profile", "current_assignment"}
            assert response.json()["next_cursor"]
            assert (await client.get("/api/v1/cases", params={"limit": 0})).status_code == 422
            app.dependency_overrides[get_actor] = lambda: manager
            result = await client.get("/api/v1/cases")
            assert result.status_code == 200
            assert {x["case"]["id"] for x in result.json()["items"]} == {
                x["case"]["id"] for x in created
            }
            spec = (await client.get("/openapi.json")).json()
            assert set(spec["paths"]["/api/v1/cases"]) == {"get", "post"}
            assert "Page_CaseProfileView_" in str(
                spec["paths"]["/api/v1/cases"]["get"]["responses"]["200"]
            )
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()
