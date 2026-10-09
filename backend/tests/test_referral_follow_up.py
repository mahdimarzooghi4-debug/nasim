"""Real PostgreSQL follow-up foundation: no inferred Referral/Provider outcome."""

import asyncio
import base64
import json
import os
from datetime import UTC, datetime
from uuid import UUID, uuid4

import httpx
import pytest
from pydantic import PostgresDsn, ValidationError
from sqlalchemy import func, select, text
from sqlalchemy.exc import DBAPIError

from nasim.api.app import create_app, get_actor
from nasim.domain.contracts import CreateCase, ReassignCaregiver, RecordObservation
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorType
from nasim.infrastructure.config import Settings
from nasim.infrastructure.database import make_sessions
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent
from nasim.referral.contracts import (
    REFERRAL_FOLLOW_UP_PERMISSIONS,
    CreateReferral,
    RecordReferralFollowUp,
)
from nasim.referral.follow_up import ReferralFollowUps
from nasim.referral.models import ReferralFollowUpRecord
from nasim.referral.service import Referrals

pytestmark = pytest.mark.integration


@pytest.fixture
async def env(service, manager, caregiver):
    creator = await service.mutate(
        "create",
        CreateCase(
            upstream_enrollment_ref="synthetic-enrolled",
            elder_reference="synthetic-elder",
            initial_caregiver_actor_id=caregiver.actor_id,
        ),
        manager,
        "follow-up-create",
    )
    case_id = UUID(creator["case"]["id"])
    assignment_id = UUID(creator["current_assignment"]["id"])
    need = await service.mutate(
        "observation_add",
        RecordObservation(
            expected_current_assignment_id=assignment_id,
            record_type="NEED_CAPTURE",
            occurred_at=datetime.now(UTC),
            content="Human observed Need (not a verified medical diagnosis)",
        ),
        caregiver,
        "follow-up-need",
        case_id,
    )
    actor = caregiver.model_copy(
        update={
            "capabilities": caregiver.capabilities
            | {"referral.create.assigned", "referral.read.assigned"}
            | frozenset(REFERRAL_FOLLOW_UP_PERMISSIONS)
        }
    )
    referrals = Referrals(service.sessions)
    created = await referrals.create(
        case_id,
        CreateReferral(
            source_need_observation_id=UUID(need["id"]),
            expected_current_assignment_id=assignment_id,
            reason="Recorded need for later follow-up",
        ),
        actor,
        "follow-up-referral",
    )
    return (
        ReferralFollowUps(service.sessions),
        referrals,
        case_id,
        assignment_id,
        UUID(created["id"]),
        actor,
    )


def command(env, note: str = "Caregiver recorded an attempted follow-up"):
    return RecordReferralFollowUp(
        expected_current_assignment_id=env[3],
        note=note,
        reason="Document human contact attempt only",
    )


async def counts(admin_engine):
    async with admin_engine.connect() as conn:
        return (
            await conn.scalar(select(func.count()).select_from(ReferralFollowUpRecord)),
            await conn.scalar(
                select(func.count()).select_from(AuditEntry).where(
                    AuditEntry.action == "referral.follow_up_recorded.v1"
                )
            ),
            await conn.scalar(
                select(func.count()).select_from(OutboxEvent).where(
                    OutboxEvent.event_type == "referral.follow_up_recorded.v1"
                )
            ),
            await conn.scalar(
                select(func.count()).select_from(IdempotencyRecord).where(
                    IdempotencyRecord.operation.like("referral.follow_up.record.%")
                )
            ),
        )


async def test_follow_up_append_only_effects_no_outcome_leak(env, admin_engine, service):
    followups, _, case_id, _, referral_id, actor = env
    created = await followups.record(referral_id, command(env), actor, "first-note")
    assert created["referral_id"] == str(referral_id)
    assert created["recorded_by_actor_type"] == "HUMAN"
    assert set(created) == {
        "id", "referral_id", "recorded_at", "recorded_by_actor_id",
        "recorded_by_actor_type", "note", "reason", "correlation_id",
    }
    assert await counts(admin_engine) == (1, 1, 1, 1)
    async with admin_engine.connect() as conn:
        event = await conn.scalar(
            select(OutboxEvent.payload).where(
                OutboxEvent.event_type == "referral.follow_up_recorded.v1"
            )
        )
        assert set(event) == {
            "follow_up_record_id", "referral_id", "case_id", "actor_id",
            "actor_type", "recorded_at", "correlation_id",
        }
        assert event["case_id"] == str(case_id)
        assert "Caregiver recorded" not in str(event)
    # TS-03 timeline must never expose Referral notes via the shared audit table.
    case_timeline = await service.read("timeline", case_id, actor)
    assert all(item.action.startswith("case.") for item in case_timeline.items)


@pytest.mark.parametrize(
    "field", ["status", "closed", "complete", "outcome", "provider_id", "rating"]
)
def test_follow_up_contract_forbids_unapproved_fields(env, field):
    with pytest.raises(ValidationError):
        RecordReferralFollowUp(**command(env).model_dump(), **{field: "invented"})


@pytest.mark.parametrize("value", ["", " ", "\n"])
def test_follow_up_note_and_reason_required(env, value):
    for field in ("note", "reason"):
        payload = command(env).model_dump()
        payload[field] = value
        with pytest.raises(ValidationError):
            RecordReferralFollowUp(**payload)


async def test_idempotent_race_conflict_and_retries(env, admin_engine):
    followups, _, _, _, ref_id, actor = env
    results = await asyncio.gather(
        followups.record(ref_id, command(env), actor, "race"),
        followups.record(ref_id, command(env), actor, "race"),
    )
    assert results[0] == results[1]
    assert await counts(admin_engine) == (1, 1, 1, 1)
    with pytest.raises(DomainError) as error:
        await followups.record(ref_id, command(env, "different note"), actor, "race")
    assert error.value.code == "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"
    assert await counts(admin_engine) == (1, 1, 1, 1)


async def test_multiple_notes_and_paginated_read_isolation(env, admin_engine):
    followups, referrals, case_id, aid, ref_id, actor = env
    first = await followups.record(ref_id, command(env, "First"), actor, "one")
    second = await followups.record(ref_id, command(env, "Second"), actor, "two")
    first_page = await followups.list(ref_id, actor, limit=1)
    next_page = await followups.list(ref_id, actor, cursor=first_page.next_cursor, limit=1)
    assert first_page.next_cursor
    assert not next_page.next_cursor
    assert {str(first_page.items[0].id), str(next_page.items[0].id)} == {
        first["id"], second["id"],
    }
    assert (await followups.get(UUID(first["id"]), actor)).note == "First"
    second_referral = await referrals.create(
        case_id,
        CreateReferral(
            source_need_observation_id=(
                await referrals.get(ref_id, actor)
            ).source_need_observation_id,
            expected_current_assignment_id=aid,
            reason="Another referral recording for the same Need",
        ),
        actor,
        "another-referral",
    )
    assert (await followups.list(UUID(second_referral["id"]), actor)).items == []
    assert await counts(admin_engine) == (2, 2, 2, 2)


async def test_read_deny_missing_capability_actor_and_ai(env):
    followups, _, _, _, ref_id, actor = env
    recorded = await followups.record(ref_id, command(env), actor, "record")
    for rejected in (
        actor.model_copy(update={"capabilities": frozenset({"referral.read.assigned"})}),
        actor.model_copy(update={"actor_id": "other"}),
        actor.model_copy(update={"actor_type": ActorType.AI}),
    ):
        with pytest.raises(DomainError) as error:
            await followups.list(ref_id, rejected)
        assert error.value.status == 403
        with pytest.raises(DomainError):
            await followups.get(UUID(recorded["id"]), rejected)

    oversight = actor.model_copy(
        update={
            "actor_id": "explicit-oversight",
            "capabilities": frozenset({"referral.follow_up.read.oversight"}),
        }
    )
    assert (await followups.list(ref_id, oversight)).items[0].note == command(env).note


async def test_record_deny_ai_automation_wrong_assignment_and_missing_referral(env, admin_engine):
    followups, _, _, _, ref_id, actor = env
    for other_type in (ActorType.AI, ActorType.SYSTEM, ActorType.AUTOMATION):
        with pytest.raises(DomainError):
            await followups.record(
                ref_id, command(env), actor.model_copy(update={"actor_type": other_type}),
                f"actor-{other_type.value}",
            )
    with pytest.raises(DomainError) as err:
        await followups.record(
            ref_id, command(env), actor.model_copy(update={"actor_id": "other"}), "other"
        )
    assert err.value.code == "ASSIGNED_CAREGIVER_REQUIRED"
    with pytest.raises(DomainError) as err:
        await followups.record(
            ref_id,
            RecordReferralFollowUp(
                expected_current_assignment_id=uuid4(),
                note="stale",
                reason="stale",
            ),
            actor,
            "stale",
        )
    assert err.value.code == "CASE_ASSIGNMENT_CHANGED"
    with pytest.raises(DomainError) as err:
        await followups.record(uuid4(), command(env), actor, "missing")
    assert err.value.code == "REFERRAL_NOT_FOUND"
    assert await counts(admin_engine) == (0, 0, 0, 0)


async def test_cached_retry_after_caregiver_reassignment_denied(
    env, service, manager, admin_engine
):
    followups, _, case_id, aid, ref_id, actor = env
    await followups.record(ref_id, command(env), actor, "repeat")
    await service.mutate(
        "reassign",
        ReassignCaregiver(
            expected_current_assignment_id=aid,
            caregiver_actor_id="new-caregiver",
            reason="Explicit human reassignment",
        ),
        manager,
        "follow-up-reassign",
        case_id,
    )
    with pytest.raises(DomainError) as error:
        await followups.record(ref_id, command(env), actor, "repeat")
    assert error.value.code == "ASSIGNED_CAREGIVER_REQUIRED"
    assert await counts(admin_engine) == (1, 1, 1, 1)


async def test_effect_flush_failure_rolls_back_and_db_guards(env, admin_engine, monkeypatch):
    followups, _, _, _, ref_id, actor = env
    original = followups.effects.append

    async def fail_after(*args, **kwargs):
        await original(*args, **kwargs)
        raise RuntimeError("rollback test")

    monkeypatch.setattr(followups.effects, "append", fail_after)
    with pytest.raises(RuntimeError):
        await followups.record(ref_id, command(env), actor, "rollback")
    assert await counts(admin_engine) == (0, 0, 0, 0)
    monkeypatch.setattr(followups.effects, "append", original)
    record = await followups.record(ref_id, command(env), actor, "rollback")
    assert await counts(admin_engine) == (1, 1, 1, 1)

    for statement in (
        "UPDATE referral_follow_up_record SET note='tampered' WHERE id=:id",
        "DELETE FROM referral_follow_up_record WHERE id=:id",
    ):
        async with admin_engine.begin() as conn:
            with pytest.raises(DBAPIError):
                await conn.execute(text(statement), {"id": UUID(record["id"])})


async def test_direct_sql_without_atomic_effects_is_rejected(env, admin_engine):
    _, _, _, _, ref_id, actor = env
    row = ReferralFollowUpRecord(
        id=uuid4(),
        referral_id=ref_id,
        recorded_at=datetime.now(UTC),
        recorded_by_actor_id=actor.actor_id,
        recorded_by_actor_type="HUMAN",
        note="Direct insertion",
        reason="No effects",
        correlation_id=actor.correlation_id,
    )
    async with make_sessions(admin_engine)() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                session.add(row)
                await session.flush()
    assert await counts(admin_engine) == (0, 0, 0, 0)


async def test_http_read_write_with_trusted_actor(env, admin_engine):
    _, _, _, _, ref_id, actor = env
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    url = f"/api/v1/referrals/{ref_id}/follow-up-records"
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            assert (await client.get(url)).status_code == 401
            assert (await client.post(
                url, json=command(env).model_dump(mode="json"),
                headers={"Idempotency-Key": "http"}
            )).status_code == 401
            app.dependency_overrides[get_actor] = lambda: actor
            created = await client.post(
                url, json=command(env).model_dump(mode="json"),
                headers={"Idempotency-Key": "http"}
            )
            assert created.status_code == 201, created.text
            assert (await client.get(url)).json()["items"][0]["id"] == created.json()["id"]
            assert (await client.get(
                f"/api/v1/referral-follow-up-records/{created.json()['id']}"
            )).status_code == 200
            assert (await client.get(url, params={"limit": 0})).status_code == 422
            assert (await client.patch(
                f"/api/v1/referral-follow-up-records/{created.json()['id']}",
                json={"note": "tamper"}
            )).status_code == 405
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()
    assert await counts(admin_engine) == (1, 1, 1, 1)


@pytest.mark.parametrize("slot", ["cursor", "limit"])
async def test_malformed_pagination_is_bounded(env, slot):
    followups, _, _, _, ref_id, actor = env
    if slot == "limit":
        with pytest.raises(DomainError) as error:
            await followups.list(ref_id, actor, limit=101)
    else:
        token = base64.urlsafe_b64encode(
            json.dumps(["2026-10-08T00:00:00+00:00", {"uuid": "wrong type"}]).encode()
        ).decode()
        with pytest.raises(DomainError) as error:
            await followups.list(ref_id, actor, cursor=token)
    assert error.value.status == 422
    assert error.value.code == (
        "INVALID_PAGE_LIMIT" if slot == "limit" else "INVALID_CURSOR"
    )
