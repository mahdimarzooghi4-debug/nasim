"""PostgreSQL and HTTP tests for the bounded human Case Journey read workspace."""

import base64
import json
import os
from datetime import UTC, datetime
from uuid import UUID, uuid4

import httpx
import pytest
from pydantic import PostgresDsn
from sqlalchemy import func, select

from nasim.api.app import create_app, get_actor
from nasim.application.care_journey import CareJourneyWorkspace
from nasim.domain.contracts import CreateCase, ReassignCaregiver, RecordObservation
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType
from nasim.infrastructure.config import Settings
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent
from nasim.referral.contracts import CreateReferral, RecordReferralFollowUp
from nasim.referral.follow_up import ReferralFollowUps
from nasim.referral.service import Referrals

pytestmark = pytest.mark.integration

READ_GROUPS = (
    "case.read.assigned",
    "referral.read.assigned",
    "referral.follow_up.read.assigned",
)


@pytest.fixture
async def journey(service, manager, caregiver):
    actor = caregiver.model_copy(
        update={
            "capabilities": caregiver.capabilities
            | {
                "referral.create.assigned",
                "referral.read.assigned",
                "referral.follow_up.record.assigned",
                "referral.follow_up.read.assigned",
            }
        }
    )
    case = await service.mutate(
        "create",
        CreateCase(
            upstream_enrollment_ref="pre-existing-upstream-enrollment",
            elder_reference="opaque-elder",
            initial_caregiver_actor_id=actor.actor_id,
        ),
        manager,
        "journey-create",
    )
    case_id = UUID(case["case"]["id"])
    assignment_id = UUID(case["current_assignment"]["id"])
    referrals = Referrals(service.sessions)
    follow_ups = ReferralFollowUps(service.sessions)
    referral_ids = []
    for n in (1, 2):
        observation = await service.mutate(
            "observation_add",
            RecordObservation(
                expected_current_assignment_id=assignment_id,
                record_type="NEED_CAPTURE",
                occurred_at=datetime.now(UTC),
                content=f"Human need capture {n}",
            ),
            actor,
            f"journey-need-{n}",
            case_id,
        )
        referral = await referrals.create(
            case_id,
            CreateReferral(
                source_need_observation_id=UUID(observation["id"]),
                expected_current_assignment_id=assignment_id,
                reason=f"Human referral record {n}",
            ),
            actor,
            f"journey-referral-{n}",
        )
        referral_ids.append(UUID(referral["id"]))
    for n in (1, 2):
        await follow_ups.record(
            referral_ids[0],
            RecordReferralFollowUp(
                expected_current_assignment_id=assignment_id,
                note=f"Sensitive follow-up {n}",
                reason="Descriptive human note only",
            ),
            actor,
            f"journey-follow-up-{n}",
        )
    return (
        CareJourneyWorkspace(service, referrals, follow_ups),
        case_id,
        assignment_id,
        referral_ids,
        actor,
    )


async def effects(admin_engine) -> tuple[int, int, int]:
    async with admin_engine.connect() as conn:
        return (
            await conn.scalar(select(func.count()).select_from(AuditEntry)),
            await conn.scalar(select(func.count()).select_from(OutboxEvent)),
            await conn.scalar(select(func.count()).select_from(IdempotencyRecord)),
        )


async def test_case_journey_independent_pages_and_referral_scoped_follow_ups(journey, admin_engine):
    reader, case_id, _, referral_ids, actor = journey
    before = await effects(admin_engine)
    page = await reader.read(case_id, actor, referral_id=referral_ids[0], limit=1)
    assert page.case.case.id == case_id
    assert page.case.current_assignment.caregiver_actor_id == actor.actor_id
    assert len(page.observations.items) == len(page.referrals.items) == 1
    assert page.selected_referral is not None
    assert page.selected_referral.id == referral_ids[0]
    assert page.follow_ups is not None and len(page.follow_ups.items) == 1
    assert page.observations.next_cursor
    assert page.referrals.next_cursor
    assert page.follow_ups.next_cursor

    advanced_observations = await reader.read(
        case_id,
        actor,
        referral_id=referral_ids[0],
        observation_cursor=page.observations.next_cursor,
        limit=1,
    )
    assert advanced_observations.observations.items[0].id != page.observations.items[0].id
    assert advanced_observations.referrals.items[0].id == page.referrals.items[0].id
    assert advanced_observations.follow_ups is not None
    assert advanced_observations.follow_ups.items[0].id == page.follow_ups.items[0].id

    advanced_referrals = await reader.read(
        case_id, actor, referral_cursor=page.referrals.next_cursor, limit=1
    )
    assert advanced_referrals.referrals.items[0].id != page.referrals.items[0].id
    assert advanced_referrals.follow_ups is None
    assert advanced_referrals.selected_referral is None

    advanced_followups = await reader.read(
        case_id,
        actor,
        referral_id=referral_ids[0],
        follow_up_cursor=page.follow_ups.next_cursor,
        limit=1,
    )
    assert advanced_followups.follow_ups is not None
    assert advanced_followups.follow_ups.items[0].id != page.follow_ups.items[0].id
    assert advanced_followups.follow_ups.next_cursor is None

    other = await reader.read(case_id, actor, referral_id=referral_ids[1], limit=1)
    assert other.follow_ups is not None and other.follow_ups.items == []
    assert await effects(admin_engine) == before
    assert set(page.model_dump(mode="json")) == {
        "case",
        "observations",
        "referrals",
        "selected_referral",
        "follow_ups",
    }
    assert not any(key in page.model_dump() for key in ("outcome", "completed", "provider"))


@pytest.mark.parametrize("missing", READ_GROUPS)
async def test_journey_requires_all_independent_read_capabilities(journey, missing):
    reader, case_id, _, _, actor = journey
    denied = actor.model_copy(update={"capabilities": actor.capabilities - {missing}})
    with pytest.raises(DomainError) as error:
        await reader.read(case_id, denied)
    assert error.value.code == "CAPABILITY_REQUIRED"
    assert error.value.status == 403


async def test_journey_denies_ai_and_wrong_human_and_allows_explicit_oversight(journey):
    reader, case_id, _, _, actor = journey
    for denied in (
        actor.model_copy(update={"actor_type": ActorType.AI}),
        actor.model_copy(update={"actor_id": "unassigned-caregiver"}),
    ):
        with pytest.raises(DomainError) as error:
            await reader.read(case_id, denied)
        assert error.value.status == 403
    oversight = ActorContext(
        actor_id="explicit-human-oversight",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset(
            {
                "case.read.oversight",
                "referral.read.oversight",
                "referral.follow_up.read.oversight",
            }
        ),
        correlation_id="oversight-test",
    )
    result = await reader.read(case_id, oversight)
    assert len(result.referrals.items) == 2


async def test_journey_rejects_wrong_referral_selection_and_cursor_without_context(journey):
    reader, case_id, _, _, actor = journey
    with pytest.raises(DomainError) as error:
        await reader.read(case_id, actor, referral_id=uuid4())
    assert error.value.code == "REFERRAL_NOT_FOUND"
    with pytest.raises(DomainError) as error:
        await reader.read(case_id, actor, follow_up_cursor="opaque")
    assert error.value.code == "INVALID_CURSOR"
    for limit in (0, 101):
        with pytest.raises(DomainError) as error:
            await reader.read(case_id, actor, limit=limit)
        assert error.value.code == "INVALID_PAGE_LIMIT"
    invalid = base64.urlsafe_b64encode(
        json.dumps(["2026-10-09T00:00:00+00:00", {"not": "uuid"}]).encode()
    ).decode()
    with pytest.raises(DomainError) as error:
        await reader.read(case_id, actor, observation_cursor=invalid)
    assert error.value.code == "INVALID_CURSOR"


async def test_journey_revokes_old_caregiver_after_human_reassignment(
    journey, service, manager, admin_engine
):
    reader, case_id, assignment_id, referral_ids, actor = journey
    await reader.read(case_id, actor, referral_id=referral_ids[0])
    await service.mutate(
        "reassign",
        ReassignCaregiver(
            expected_current_assignment_id=assignment_id,
            caregiver_actor_id="successor-caregiver",
            reason="Explicit replacement of caregiver",
        ),
        manager,
        "journey-handover",
        case_id,
    )
    before = await effects(admin_engine)
    with pytest.raises(DomainError) as error:
        await reader.read(case_id, actor, referral_id=referral_ids[0])
    assert error.value.status == 403
    assert await effects(admin_engine) == before


async def test_journey_http_shape_anonymous_and_no_mutation(journey):
    _, case_id, _, referral_ids, actor = journey
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    route = f"/api/v1/cases/{case_id}/journey-workspace"
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            assert (await client.get(route)).status_code == 401
            app.dependency_overrides[get_actor] = lambda: actor
            good = await client.get(route, params={"referral_id": str(referral_ids[0]), "limit": 1})
            assert good.status_code == 200, good.text
            payload = good.json()
            assert payload["case"]["case"]["id"] == str(case_id)
            assert payload["follow_ups"]["items"][0]["referral_id"] == str(referral_ids[0])
            assert payload["referrals"]["next_cursor"] is not None
            assert (await client.get(route, params={"limit": 0})).status_code == 422
            assert (await client.get(route, params={"follow_up_cursor": "bad"})).status_code == 422
            assert (await client.post(route, json={})).status_code == 405
            spec = (await client.get("/openapi.json")).json()
            path = "/api/v1/cases/{case_id}/journey-workspace"
            assert list(spec["paths"][path]) == ["get"]
            response_schema = spec["paths"][path]["get"]["responses"]["200"]["content"][
                "application/json"
            ]["schema"]
            assert "CareJourneyWorkspaceView" in str(response_schema)

            app.dependency_overrides[get_actor] = lambda: actor.model_copy(
                update={"capabilities": frozenset({"case.read.assigned"})}
            )
            assert (await client.get(route)).status_code == 403
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()
