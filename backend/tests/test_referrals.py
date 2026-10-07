"""Real PostgreSQL Referral foundation contracts, authorization, races and atomicity."""

import asyncio
import os
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal
from uuid import UUID, uuid4

import httpx
import pytest
from pydantic import PostgresDsn
from sqlalchemy import func, select, text
from sqlalchemy.exc import DBAPIError

from nasim.api.app import create_app, get_actor
from nasim.authorization.contracts import TrustedPrincipal, Window
from nasim.authorization.models import PermissionDefinition, RoleDefinition
from nasim.authorization.service import AuthorizationResolver, Provisioning
from nasim.domain.contracts import (
    CorrectObservation,
    CreateCase,
    ReassignCaregiver,
    RecordObservation,
)
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorType
from nasim.infrastructure.config import Settings
from nasim.infrastructure.database import make_sessions
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent
from nasim.referral.contracts import REFERRAL_PERMISSIONS, CreateReferral
from nasim.referral.models import ReferralRecord
from nasim.referral.service import Referrals

pytestmark = pytest.mark.integration


async def seed_need(
    service,
    manager,
    caregiver,
    kind: Literal["NEED_CAPTURE", "OBSERVATION"] = "NEED_CAPTURE",
    key="create",
):
    created = await service.mutate(
        "create",
        CreateCase(
            upstream_enrollment_ref="enrolled",
            elder_reference="elder",
            initial_caregiver_actor_id=caregiver.actor_id,
        ),
        manager,
        key,
    )
    case_id = UUID(created["case"]["id"])
    assignment_id = UUID(created["current_assignment"]["id"])
    need = await service.mutate(
        "observation_add",
        RecordObservation(
            expected_current_assignment_id=assignment_id,
            record_type=kind,
            occurred_at=datetime.now(UTC),
            content="Sensitive Need free text",
        ),
        caregiver,
        "need",
        case_id,
    )
    return case_id, assignment_id, UUID(need["id"])


@pytest.fixture
async def referral_env(service, manager, caregiver):
    case_id, assignment_id, need_id = await seed_need(service, manager, caregiver)
    actor = caregiver.model_copy(
        update={"capabilities": caregiver.capabilities | frozenset(REFERRAL_PERMISSIONS)}
    )
    return Referrals(service.sessions), case_id, assignment_id, need_id, actor


def command(env, **changes):
    return CreateReferral(
        **(
            {
                "source_need_observation_id": env[3],
                "expected_current_assignment_id": env[2],
                "reason": "Record Need for referral process",
            }
            | changes
        )
    )


async def counts(engine):
    async with engine.connect() as conn:
        queries = [
            select(func.count()).select_from(ReferralRecord),
            select(func.count())
            .select_from(AuditEntry)
            .where(AuditEntry.action == "referral.recorded.v1"),
            select(func.count())
            .select_from(OutboxEvent)
            .where(OutboxEvent.event_type == "referral.recorded.v1"),
            select(func.count())
            .select_from(IdempotencyRecord)
            .where(IdempotencyRecord.operation.like("referral.record.%")),
        ]
        return tuple([await conn.scalar(q) for q in queries])


async def test_valid_need_atomic_effects_and_minimal_event(referral_env, admin_engine):
    ref, cid, _, nid, actor = referral_env
    result = await ref.create(cid, command(referral_env), actor, "record")
    assert result["source_need_observation_id"] == str(nid)
    assert result["case_id"] == str(cid)
    assert await counts(admin_engine) == (1, 1, 1, 1)
    async with admin_engine.connect() as conn:
        payload = await conn.scalar(
            select(OutboxEvent.payload).where(OutboxEvent.event_type == "referral.recorded.v1")
        )
        assert set(payload) == {
            "referral_id",
            "case_id",
            "source_need_observation_id",
            "actor_id",
            "actor_type",
            "recorded_at",
            "correlation_id",
        }
        assert "Sensitive Need" not in str(payload)
        audit = (
            await conn.execute(
                select(AuditEntry).where(AuditEntry.action == "referral.recorded.v1")
            )
        ).one()
        assert audit.before_reference == nid
        assert audit.after_reference == UUID(result["id"])
        assert audit.reason == result["reason"] and audit.correlation_id == actor.correlation_id


async def test_no_invented_one_referral_per_need(referral_env, admin_engine):
    ref, cid, _, _, actor = referral_env
    first = await ref.create(cid, command(referral_env), actor, "first")
    second = await ref.create(cid, command(referral_env), actor, "second")
    assert first["id"] != second["id"]
    assert await counts(admin_engine) == (2, 2, 2, 2)


@pytest.mark.parametrize("invalid", ["missing", "cross_case", "ordinary", "superseded"])
async def test_source_fail_closed(referral_env, service, manager, caregiver, admin_engine, invalid):
    ref, cid, aid, nid, actor = referral_env
    source = nid
    if invalid == "missing":
        source = uuid4()
    if invalid == "cross_case":
        _, _, source = await seed_need(service, manager, caregiver, key="other-case")
    if invalid == "ordinary":
        _, _, other = await seed_need(service, manager, caregiver, kind="OBSERVATION", key="other")
        # Use ordinary Observation in the original Case to isolate the type condition.
        row = await service.mutate(
            "observation_add",
            RecordObservation(
                expected_current_assignment_id=aid,
                record_type="OBSERVATION",
                occurred_at=datetime.now(UTC),
                content="ordinary",
            ),
            caregiver,
            "ordinary",
            cid,
        )
        source = UUID(row["id"])
    if invalid == "superseded":
        await service.mutate(
            "observation_correct",
            CorrectObservation(
                expected_current_assignment_id=aid,
                expected_current_record_id=nid,
                record_type="NEED_CAPTURE",
                occurred_at=datetime.now(UTC),
                content="corrected",
                correction_reason="correction",
            ),
            caregiver,
            "correct",
            cid,
            nid,
        )
    with pytest.raises(DomainError) as error:
        await ref.create(
            cid, command(referral_env, source_need_observation_id=source), actor, "record"
        )
    assert (
        error.value.code
        == {
            "missing": "RECORD_NOT_FOUND",
            "cross_case": "RECORD_NOT_FOUND",
            "ordinary": "NEED_CAPTURE_REQUIRED",
            "superseded": "STALE_RECORD_REVISION",
        }[invalid]
    )
    assert await counts(admin_engine) == (0, 0, 0, 0)


@pytest.mark.parametrize(
    "invalid", ["missing_capability", "not_assigned", "stale", "AI", "title_only"]
)
async def test_create_authorization_fail_closed(referral_env, admin_engine, invalid):
    ref, cid, _, _, actor = referral_env
    body = command(referral_env)
    if invalid in {"missing_capability", "title_only"}:
        actor = actor.model_copy(
            update={
                "capabilities": frozenset({"caregiver"}) if invalid == "title_only" else frozenset()
            }
        )
    if invalid == "not_assigned":
        actor = actor.model_copy(update={"actor_id": "other"})
    if invalid == "AI":
        actor = actor.model_copy(update={"actor_type": ActorType.AI})
    if invalid == "stale":
        body = command(referral_env, expected_current_assignment_id=uuid4())
    with pytest.raises(DomainError) as error:
        await ref.create(cid, body, actor, "record")
    assert error.value.code == {
        "not_assigned": "ASSIGNED_CAREGIVER_REQUIRED",
        "stale": "CASE_ASSIGNMENT_CHANGED",
    }.get(invalid, "CAPABILITY_REQUIRED")
    assert await counts(admin_engine) == (0, 0, 0, 0)


@pytest.mark.parametrize("kind", [ActorType.HUMAN, ActorType.SYSTEM, ActorType.AUTOMATION])
async def test_explicit_authorized_actor_provenance(referral_env, admin_engine, kind):
    ref, cid, _, _, actor = referral_env
    actor = actor.model_copy(update={"actor_type": kind})
    result = await ref.create(cid, command(referral_env), actor, "record")
    assert result["created_by_actor_type"] == kind.value
    async with admin_engine.connect() as conn:
        assert (
            await conn.scalar(
                select(AuditEntry.actor_type).where(AuditEntry.action == "referral.recorded.v1")
            )
            == kind.value
        )
        payload = await conn.scalar(
            select(OutboxEvent.payload).where(OutboxEvent.event_type == "referral.recorded.v1")
        )
        assert payload["actor_type"] == kind.value


async def test_idempotent_retry(referral_env, admin_engine):
    ref, cid, _, _, actor = referral_env
    first = await ref.create(cid, command(referral_env), actor, "record")
    assert await ref.create(cid, command(referral_env), actor, "record") == first
    assert await counts(admin_engine) == (1, 1, 1, 1)


async def test_key_payload_conflict(referral_env, admin_engine):
    ref, cid, _, _, actor = referral_env
    await ref.create(cid, command(referral_env), actor, "record")
    with pytest.raises(DomainError) as error:
        await ref.create(cid, command(referral_env, reason="Different payload"), actor, "record")
    assert error.value.code == "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"
    assert await counts(admin_engine) == (1, 1, 1, 1)


@pytest.mark.parametrize("key", ["", " ", "x" * 201])
async def test_invalid_idempotency_key(referral_env, key):
    with pytest.raises(DomainError) as error:
        await referral_env[0].create(referral_env[1], command(referral_env), referral_env[4], key)
    assert error.value.code == "INVALID_IDEMPOTENCY_KEY"


@pytest.mark.parametrize("different", [False, True])
async def test_real_idempotency_race(referral_env, admin_engine, different):
    ref, cid, _, _, actor = referral_env
    results = await asyncio.gather(
        ref.create(cid, command(referral_env), actor, "race"),
        ref.create(
            cid,
            command(referral_env, reason="Changed" if different else command(referral_env).reason),
            actor,
            "race",
        ),
        return_exceptions=True,
    )
    if different:
        assert (
            sum(
                isinstance(r, DomainError)
                and r.code == "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"
                for r in results
            )
            == 1
        )
    else:
        assert results[0] == results[1] and not isinstance(results[0], Exception)
    assert await counts(admin_engine) == (1, 1, 1, 1)


async def test_real_distinct_key_race_allows_same_need(referral_env, admin_engine):
    ref, cid, _, _, actor = referral_env
    results = await asyncio.gather(
        *[ref.create(cid, command(referral_env), actor, f"key-{i}") for i in range(2)]
    )
    assert results[0]["id"] != results[1]["id"]
    assert await counts(admin_engine) == (2, 2, 2, 2)


async def test_rollback_after_all_effects_flush(referral_env, admin_engine, monkeypatch):
    ref, cid, _, _, actor = referral_env
    original = ref.effects.append

    async def fail_after_flush(*args, **kwargs):
        await original(*args, **kwargs)
        raise RuntimeError("injected failure after all effects")

    monkeypatch.setattr(ref.effects, "append", fail_after_flush)
    with pytest.raises(RuntimeError):
        await ref.create(cid, command(referral_env), actor, "record")
    assert await counts(admin_engine) == (0, 0, 0, 0)
    monkeypatch.setattr(ref.effects, "append", original)
    await ref.create(cid, command(referral_env), actor, "record")
    assert await counts(admin_engine) == (1, 1, 1, 1)


@pytest.mark.parametrize("operation", ["UPDATE", "DELETE"])
async def test_referral_db_history_immutable(referral_env, admin_engine, operation):
    ref, cid, _, _, actor = referral_env
    await ref.create(cid, command(referral_env), actor, "record")
    async with admin_engine.begin() as conn:
        with pytest.raises(DBAPIError):
            await conn.execute(
                text(
                    "UPDATE referral_record SET reason='tampered'"
                    if operation == "UPDATE"
                    else "DELETE FROM referral_record"
                )
            )


async def test_direct_insert_without_effects_rolls_back(referral_env, admin_engine):
    _, cid, _, nid, actor = referral_env
    async with make_sessions(admin_engine)() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                session.add(
                    ReferralRecord(
                        id=uuid4(),
                        case_id=cid,
                        source_need_observation_id=nid,
                        created_at=datetime.now(UTC),
                        created_by_actor_id=actor.actor_id,
                        created_by_actor_type=actor.actor_type.value,
                        reason="unlogged",
                        correlation_id="test",
                    )
                )
    assert await counts(admin_engine) == (0, 0, 0, 0)


async def test_reads_permission_assignment_oversight_and_pagination(referral_env):
    ref, cid, _, _, actor = referral_env
    first = await ref.create(cid, command(referral_env), actor, "first")
    await ref.create(cid, command(referral_env), actor, "second")
    assigned = actor.model_copy(update={"capabilities": frozenset({"referral.read.assigned"})})
    page = await ref.list(cid, assigned, limit=1)
    assert len(page.items) == 1 and page.next_cursor
    second = await ref.list(cid, assigned, cursor=page.next_cursor, limit=1)
    assert len(second.items) == 1 and second.items[0].id != page.items[0].id
    assert (await ref.get(UUID(first["id"]), assigned)).id == UUID(first["id"])
    oversight = actor.model_copy(
        update={"actor_id": "observer", "capabilities": frozenset({"referral.read.oversight"})}
    )
    assert len((await ref.list(cid, oversight)).items) == 2
    assert await ref.get(UUID(first["id"]), oversight)
    for rejected in [
        assigned.model_copy(update={"actor_id": "other"}),
        assigned.model_copy(update={"capabilities": frozenset({"case.read.oversight"})}),
        oversight.model_copy(update={"actor_type": ActorType.AI}),
    ]:
        with pytest.raises(DomainError):
            await ref.list(cid, rejected)
        with pytest.raises(DomainError):
            await ref.get(UUID(first["id"]), rejected)


async def test_cached_retry_after_reassignment_fails_closed(referral_env, service, manager):
    ref, cid, aid, _, actor = referral_env
    await ref.create(cid, command(referral_env), actor, "record")
    await service.mutate(
        "reassign",
        ReassignCaregiver(
            expected_current_assignment_id=aid, caregiver_actor_id="new-caregiver", reason="handoff"
        ),
        manager,
        "reassign",
        cid,
    )
    with pytest.raises(DomainError) as error:
        await ref.create(cid, command(referral_env), actor, "record")
    assert error.value.code == "ASSIGNED_CAREGIVER_REQUIRED"


async def test_cached_retry_after_source_correction_fails_closed(referral_env, service, caregiver):
    ref, cid, aid, nid, actor = referral_env
    await ref.create(cid, command(referral_env), actor, "record")
    await service.mutate(
        "observation_correct",
        CorrectObservation(
            expected_current_assignment_id=aid,
            expected_current_record_id=nid,
            record_type="NEED_CAPTURE",
            occurred_at=datetime.now(UTC),
            content="updated",
            correction_reason="correction",
        ),
        caregiver,
        "correct",
        cid,
        nid,
    )
    with pytest.raises(DomainError) as error:
        await ref.create(cid, command(referral_env), actor, "record")
    assert error.value.code == "STALE_RECORD_REVISION"
    # Historical evidence retains the original source; no invented invalidation workflow.
    assert (await ref.list(cid, actor)).items[0].source_need_observation_id == nid


async def test_resolved_ts05_capabilities_and_anonymous_http(referral_env, admin_engine):
    ref, cid, _, _, actor = referral_env
    async with admin_engine.begin() as conn:
        await conn.execute(
            text("TRUNCATE actor_role_assignment,role_permission_grant,authorization_audit")
        )
    sessions = make_sessions(admin_engine)
    provision = Provisioning(sessions)
    identity = TrustedPrincipal(
        actor_id=actor.actor_id, actor_type=ActorType.HUMAN, correlation_id="trusted-test"
    )
    window = Window(
        starts_at=datetime.now(UTC), reason="Explicit isolated test grant, not Business mapping"
    )
    async with sessions() as session:
        role = await session.scalar(
            select(RoleDefinition.id).where(
                RoleDefinition.code == "caregiver", RoleDefinition.revision_no == 1
            )
        )
        definitions = {
            p.code: p.id
            for p in await session.scalars(
                select(PermissionDefinition).where(
                    PermissionDefinition.code.in_(REFERRAL_PERMISSIONS)
                )
            )
        }
    assert role
    try:
        await provision.assign(identity, role, window, actor)
        resolver = AuthorizationResolver(sessions)
        assert not (await resolver.resolve(identity)).capabilities
        for pid in definitions.values():
            await provision.grant(role, pid, window, actor)
        resolved = await resolver.resolve(identity)
        assert resolved.capabilities == frozenset(REFERRAL_PERMISSIONS)
        app = create_app(
            Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"]))
        )
        try:
            async with httpx.AsyncClient(
                transport=httpx.ASGITransport(app=app), base_url="http://test"
            ) as client:
                body = command(referral_env).model_dump(mode="json")
                assert (
                    await client.post(
                        f"/api/v1/cases/{cid}/referrals",
                        json=body,
                        headers={"Idempotency-Key": "record"},
                    )
                ).status_code == 401
                assert (await client.get(f"/api/v1/cases/{cid}/referrals")).status_code == 401
                app.dependency_overrides[get_actor] = lambda: resolved
                created = await client.post(
                    f"/api/v1/cases/{cid}/referrals",
                    json=body,
                    headers={"Idempotency-Key": "record"},
                )
                assert created.status_code == 201, created.text
                identifier = created.json()["id"]
                assert (await client.get(f"/api/v1/cases/{cid}/referrals")).json()["items"][0][
                    "id"
                ] == identifier
                assert (await client.get(f"/api/v1/referrals/{identifier}")).status_code == 200
                app.dependency_overrides.clear()
                assert (await client.get(f"/api/v1/referrals/{identifier}")).status_code == 401
        finally:
            await app.state.engine.dispose()
    finally:
        async with admin_engine.begin() as conn:
            await conn.execute(
                text("TRUNCATE actor_role_assignment,role_permission_grant,authorization_audit")
            )


@pytest.mark.parametrize(
    "action",
    ["accept", "reject", "dispatch", "complete", "cancel", "escalate", "correct", "schedule"],
)
async def test_no_lifecycle_endpoints(action):
    app = create_app(Settings(database_url=PostgresDsn("postgresql://unused@127.0.0.1:1/unused")))
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            assert (
                await client.post(f"/api/v1/referrals/{uuid4()}/{action}", json={})
            ).status_code == 404
    finally:
        await app.state.engine.dispose()


@pytest.mark.parametrize("change", ["correction", "reassignment_different", "reassignment_same"])
async def test_real_source_or_assignment_change_race(
    referral_env, service, manager, caregiver, admin_engine, change
):
    ref, cid, aid, nid, actor = referral_env
    if change == "correction":
        mutation = service.mutate(
            "observation_correct",
            CorrectObservation(
                expected_current_assignment_id=aid,
                expected_current_record_id=nid,
                record_type="NEED_CAPTURE",
                occurred_at=datetime.now(UTC),
                content="correction",
                correction_reason="test race",
            ),
            caregiver,
            "race-change",
            cid,
            nid,
        )
    else:
        mutation = service.mutate(
            "reassign",
            ReassignCaregiver(
                expected_current_assignment_id=aid,
                caregiver_actor_id=caregiver.actor_id
                if change == "reassignment_same"
                else "successor",
                reason="test race",
            ),
            manager,
            "race-change",
            cid,
        )
    recorded, changed = await asyncio.gather(
        ref.create(cid, command(referral_env), actor, "race"), mutation, return_exceptions=True
    )
    assert isinstance(changed, dict)
    if isinstance(recorded, DomainError):
        assert (
            recorded.code
            == {
                "correction": "STALE_RECORD_REVISION",
                "reassignment_same": "CASE_ASSIGNMENT_CHANGED",
                "reassignment_different": "ASSIGNED_CAREGIVER_REQUIRED",
            }[change]
        )
        assert await counts(admin_engine) == (0, 0, 0, 0)
    else:
        assert isinstance(recorded, dict)
        assert await counts(admin_engine) == (1, 1, 1, 1)


@pytest.mark.parametrize(
    "invalid",
    [
        "cross_case",
        "ordinary",
        "superseded",
        "actor_type",
        "blank_reason",
        "newline_reason",
        "missing",
        "AI",
    ],
)
async def test_direct_sql_source_and_provenance_guards(
    referral_env, service, manager, caregiver, admin_engine, invalid
):
    _, cid, aid, nid, actor = referral_env
    if invalid == "cross_case":
        _, _, nid = await seed_need(service, manager, caregiver, key="cross-case")
    if invalid == "ordinary":
        observation = await service.mutate(
            "observation_add",
            RecordObservation(
                expected_current_assignment_id=aid,
                record_type="OBSERVATION",
                occurred_at=datetime.now(UTC),
                content="ordinary",
            ),
            caregiver,
            "ordinary",
            cid,
        )
        nid = UUID(observation["id"])
    if invalid == "superseded":
        await service.mutate(
            "observation_correct",
            CorrectObservation(
                expected_current_assignment_id=aid,
                expected_current_record_id=nid,
                record_type="NEED_CAPTURE",
                occurred_at=datetime.now(UTC),
                content="updated",
                correction_reason="correct",
            ),
            caregiver,
            "correct",
            cid,
            nid,
        )
    if invalid == "missing":
        nid = uuid4()
    row = ReferralRecord(
        id=uuid4(),
        case_id=cid,
        source_need_observation_id=nid,
        created_at=datetime.now(UTC),
        created_by_actor_id=actor.actor_id,
        created_by_actor_type="WRONG"
        if invalid == "actor_type"
        else "AI"
        if invalid == "AI"
        else "HUMAN",
        reason=" "
        if invalid == "blank_reason"
        else "\n"
        if invalid == "newline_reason"
        else "record",
        correlation_id="test",
    )
    async with make_sessions(admin_engine)() as session:
        with pytest.raises(DBAPIError) as error:
            async with session.begin():
                session.add(row)
                await session.flush()
        assert "Atomic referral effects required" not in str(error.value)
    assert await counts(admin_engine) == (0, 0, 0, 0)


async def test_case_timeline_does_not_disclose_referral_data_without_permission(
    referral_env, service, caregiver
):
    ref, cid, _, _, actor = referral_env
    await ref.create(cid, command(referral_env), actor, "record")
    page = await service.read("timeline", cid, caregiver)
    assert len(page.items) == 2
    assert all(item.action.startswith("case.") for item in page.items)
    assert all(item.reason != command(referral_env).reason for item in page.items)


@pytest.mark.parametrize("method", ["PATCH", "DELETE"])
async def test_no_arbitrary_referral_edit_or_delete(referral_env, method):
    ref, cid, _, _, actor = referral_env
    result = await ref.create(cid, command(referral_env), actor, "record")
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    try:
        app.dependency_overrides[get_actor] = lambda: actor
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            assert (
                await client.request(method, f"/api/v1/referrals/{result['id']}")
            ).status_code == 405
    finally:
        await app.state.engine.dispose()


async def test_idempotency_scope_separates_trusted_actor_types(referral_env, admin_engine):
    ref, cid, _, _, actor = referral_env
    human = await ref.create(cid, command(referral_env), actor, "same-key")
    automation = actor.model_copy(update={"actor_type": ActorType.AUTOMATION})
    other = await ref.create(cid, command(referral_env), automation, "same-key")
    assert human["id"] != other["id"]
    assert other["created_by_actor_type"] == "AUTOMATION"
    assert await counts(admin_engine) == (2, 2, 2, 2)


async def test_migration_rollback_with_authorization_history_fails_closed(admin_engine, manager):
    import subprocess

    sessions = make_sessions(admin_engine)
    async with admin_engine.begin() as conn:
        await conn.execute(
            text("TRUNCATE actor_role_assignment,role_permission_grant,authorization_audit")
        )
    async with sessions() as session:
        role = await session.scalar(
            select(RoleDefinition.id).where(
                RoleDefinition.code == "caregiver", RoleDefinition.revision_no == 1
            )
        )
        permission = await session.scalar(
            select(PermissionDefinition.id).where(
                PermissionDefinition.code == "referral.create.assigned"
            )
        )
    assert role and permission
    try:
        await Provisioning(sessions).grant(
            role,
            permission,
            Window(starts_at=datetime.now(UTC), reason="Isolated rollback integrity test"),
            manager,
        )
        environment = os.environ.copy()
        environment["NASIM_DATABASE_URL"] = os.environ["NASIM_TEST_DATABASE_URL"]
        # This is an expected failure on a dedicated test DB, never a hosted rollback.
        run = await asyncio.to_thread(
            subprocess.run,
            ["alembic", "downgrade", "0002_ts05"],
            env=environment,
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True,
            text=True,
            timeout=30,
        )
        assert run.returncode != 0
        assert (
            "Referral authorization history requires an approved rollback data plan" in run.stderr
        )
        async with admin_engine.connect() as conn:
            assert (
                await conn.scalar(text("SELECT version_num FROM alembic_version"))
                == "0005_provider_qe"
            )
            assert await conn.scalar(text("SELECT to_regclass('referral_record') IS NOT NULL"))
    finally:
        async with admin_engine.begin() as conn:
            await conn.execute(
                text("TRUNCATE actor_role_assignment,role_permission_grant,authorization_audit")
            )
