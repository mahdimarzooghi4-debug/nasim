import asyncio
from datetime import UTC, datetime
from uuid import UUID, uuid4

import pytest
from sqlalchemy import func, select, text
from sqlalchemy.exc import DBAPIError, IntegrityError

from nasim.domain.contracts import (
    AddContactPoint,
    CorrectCaseProfile,
    CorrectContactPoint,
    CorrectInteraction,
    CorrectObservation,
    CreateCase,
    ReassignCaregiver,
    RecordInteraction,
    RecordObservation,
)
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType
from nasim.infrastructure.models import (
    Assignment,
    AuditEntry,
    ElderCase,
    IdempotencyRecord,
    OutboxEvent,
)

pytestmark = pytest.mark.integration


def create_command():
    return CreateCase(
        upstream_enrollment_ref="upstream-1",
        elder_reference="elder-1",
        initial_caregiver_actor_id="caregiver-a",
    )


async def seed(service, manager):
    result = await service.mutate("create", create_command(), manager, "create")
    return result, UUID(result["case"]["id"]), UUID(result["current_assignment"]["id"])


async def effects(admin_engine):
    async with admin_engine.connect() as conn:
        return tuple(
            [
                await conn.scalar(select(func.count()).select_from(table))
                for table in (ElderCase, Assignment, AuditEntry, OutboxEvent, IdempotencyRecord)
            ]
        )


async def test_atomic_creation_idempotency(service, admin_engine, manager, caregiver):
    created, case_id, _ = await seed(service, manager)
    retry = await service.mutate("create", create_command(), manager, "create")
    assert retry == created
    assert await effects(admin_engine) == (1, 1, 1, 1, 1)
    result = await service.read("profile", case_id, caregiver)
    assert result.profile.elder_reference == "elder-1"
    assert result.current_assignment.caregiver_actor_id == caregiver.actor_id
    async with admin_engine.connect() as conn:
        payload = await conn.scalar(select(OutboxEvent.payload))
        assert payload["actor_type"] == "HUMAN"
        assert payload["profile_revision_id"] == created["profile"]["id"]
        assert "elder_reference" not in payload


@pytest.mark.parametrize("operation", ["create", "reassign", "contact_add", "profile_correct"])
async def test_case_idempotent_replay_cross_actor_type_is_rejected(
    service, admin_engine, manager, caregiver, operation
):
    """Same actor_id across trusted actor types cannot receive cached TS-03 effects."""
    if operation == "create":
        actor = manager
        case_id = None
        command = create_command()
    else:
        original, case_id, assignment_id = await seed(service, manager)
        if operation == "reassign":
            actor = manager
            command = ReassignCaregiver(
                expected_current_assignment_id=assignment_id,
                caregiver_actor_id="new-caregiver",
                reason="actor type provenance test",
            )
        elif operation == "contact_add":
            actor = caregiver
            command = AddContactPoint(
                expected_current_assignment_id=assignment_id,
                contact_kind="phone",
                contact_value="synthetic-test-contact",
            )
        else:
            actor = manager
            command = CorrectCaseProfile(
                expected_current_assignment_id=assignment_id,
                expected_current_revision_id=UUID(original["profile"]["id"]),
                elder_reference="synthetic-corrected",
                correction_reason="actor type provenance test",
            )

    key = "actor-type-replay"
    original_result = await service.mutate(operation, command, actor, key, case_id)
    before = await effects(admin_engine)
    # Same business request, key, actor ID and permissions; only trusted actor type differs.
    cross_type = actor.model_copy(update={"actor_type": ActorType.AUTOMATION})
    with pytest.raises(DomainError) as error:
        await service.mutate(operation, command, cross_type, key, case_id)
    assert error.value.code == "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"
    assert error.value.status == 409
    assert await effects(admin_engine) == before
    # The original human principal retains ordinary idempotent replay.
    assert await service.mutate(operation, command, actor, key, case_id) == original_result
    assert await effects(admin_engine) == before


async def test_key_payload_conflict(service, admin_engine, manager):
    await seed(service, manager)
    with pytest.raises(DomainError, match="IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"):
        await service.mutate(
            "create",
            create_command().model_copy(update={"elder_reference": "other"}),
            manager,
            "create",
        )
    assert await effects(admin_engine) == (1, 1, 1, 1, 1)


async def test_unauthorized_self_assignment(service, admin_engine, caregiver):
    with pytest.raises(DomainError, match="CAPABILITY_REQUIRED"):
        await service.mutate("create", create_command(), caregiver, "create")
    assert await effects(admin_engine) == (0, 0, 0, 0, 0)


@pytest.mark.parametrize(
    "kind",
    ["profile", "workspace", "assignments", "contacts", "interactions", "observations", "timeline"],
)
async def test_each_read_requires_current_caregiver(service, manager, caregiver, kind):
    _, case_id, _ = await seed(service, manager)
    other = caregiver.model_copy(update={"actor_id": "caregiver-b"})
    with pytest.raises(DomainError, match="ASSIGNED_CAREGIVER_REQUIRED"):
        await service.read(kind, case_id, other)
    await service.read(kind, case_id, caregiver)
    await service.read(kind, case_id, manager)


@pytest.mark.parametrize("kind", ["interactions", "observations", "timeline"])
@pytest.mark.parametrize("limit", [-1, 0, 101])
async def test_ts03_paginated_reads_reject_invalid_service_limits(
    service, admin_engine, manager, kind, limit
):
    """Service-level callers get the same 422 bound as REST and other bounded contexts."""
    _, case_id, _ = await seed(service, manager)
    before = await effects(admin_engine)
    with pytest.raises(DomainError) as error:
        await service.read(kind, case_id, manager, limit=limit)
    assert error.value.code == "INVALID_PAGE_LIMIT"
    assert error.value.status == 422
    assert await effects(admin_engine) == before


@pytest.mark.parametrize("kind", ["interactions", "observations", "timeline"])
@pytest.mark.parametrize("limit", [1, 100])
async def test_ts03_paginated_reads_accept_service_limit_boundaries(service, manager, kind, limit):
    _, case_id, _ = await seed(service, manager)
    page = await service.read(kind, case_id, manager, limit=limit)
    assert len(page.items) <= limit
    assert page.next_cursor is None


async def test_ts03_paginated_reads_deny_unauthorized_actor_before_limit_validation(
    service, manager, caregiver
):
    _, case_id, _ = await seed(service, manager)
    outsider = caregiver.model_copy(update={"capabilities": frozenset()})
    with pytest.raises(DomainError) as error:
        await service.read("timeline", case_id, outsider, limit=0)
    assert error.value.code == "CAPABILITY_REQUIRED"
    assert error.value.status == 403


@pytest.mark.parametrize("actor_id", ["family", "provider", "employer", "elder"])
async def test_external_actor_has_no_default_grants(service, manager, actor_id):
    _, case_id, _ = await seed(service, manager)
    outsider = ActorContext(
        actor_id=actor_id,
        actor_type=ActorType.HUMAN,
        capabilities=frozenset(),
        correlation_id="outsider",
    )
    with pytest.raises(DomainError, match="CAPABILITY_REQUIRED"):
        await service.read("workspace", case_id, outsider)
    with pytest.raises(DomainError, match="CAPABILITY_REQUIRED"):
        await service.mutate("create", create_command(), outsider, "key")


async def test_ai_denied_all_grants(service, manager):
    _, case_id, _ = await seed(service, manager)
    ai = manager.model_copy(update={"actor_type": ActorType.AI})
    with pytest.raises(DomainError, match="CAPABILITY_REQUIRED"):
        await service.read("workspace", case_id, ai)
    with pytest.raises(DomainError, match="CAPABILITY_REQUIRED"):
        await service.mutate("create", create_command(), ai, "key")


async def test_oversight_is_read_only_for_records(service, manager):
    _, case_id, assignment_id = await seed(service, manager)
    await service.read("workspace", case_id, manager)
    with pytest.raises(DomainError, match="CAPABILITY_REQUIRED"):
        await service.mutate(
            "contact_add",
            AddContactPoint(
                expected_current_assignment_id=assignment_id,
                contact_kind="phone",
                contact_value="number",
            ),
            manager,
            "key",
            case_id,
        )


async def test_reassignment_stale_history_and_revoked_access(
    service, admin_engine, manager, caregiver
):
    _, case_id, assignment_id = await seed(service, manager)
    command = ReassignCaregiver(
        expected_current_assignment_id=assignment_id,
        caregiver_actor_id="caregiver-b",
        reason="handoff",
    )
    result = await service.mutate("reassign", command, manager, "reassign", case_id)
    history = await service.read("assignments", case_id, manager)
    assert len(history) == 2
    assert history[0].ended_at is not None and history[1].ended_at is None
    assert history[1].reason == "handoff"
    assert history[1].assigned_by_actor_id == manager.actor_id
    assert result["id"] == str(history[1].id)
    with pytest.raises(DomainError, match="CASE_ASSIGNMENT_CHANGED"):
        await service.mutate("reassign", command, manager, "stale", case_id)
    with pytest.raises(DomainError, match="ASSIGNED_CAREGIVER_REQUIRED"):
        await service.read("profile", case_id, caregiver)
    assert await effects(admin_engine) == (1, 2, 2, 2, 2)


async def test_profile_correction_lineage(service, manager):
    original, case_id, assignment_id = await seed(service, manager)
    command = CorrectCaseProfile(
        expected_current_assignment_id=assignment_id,
        expected_current_revision_id=UUID(original["profile"]["id"]),
        elder_reference="corrected",
        correction_reason="reference correction",
    )
    corrected = await service.mutate("profile_correct", command, manager, "correct", case_id)
    assert corrected["revision_no"] == 2
    assert corrected["supersedes_revision_id"] == original["profile"]["id"]
    workspace = await service.read("workspace", case_id, manager)
    assert [r.elder_reference for r in workspace.profile_history] == ["elder-1", "corrected"]
    with pytest.raises(DomainError, match="STALE_RECORD_REVISION"):
        await service.mutate("profile_correct", command, manager, "stale", case_id)


async def test_contact_correction_history(service, manager, caregiver):
    _, case_id, assignment_id = await seed(service, manager)
    add = AddContactPoint(
        expected_current_assignment_id=assignment_id,
        contact_kind="phone",
        contact_value="old-number",
    )
    original = await service.mutate("contact_add", add, caregiver, "add", case_id)
    correction = CorrectContactPoint(
        **add.model_dump(),
        expected_current_revision_id=UUID(original["id"]),
        correction_reason="transcription error",
    ).model_copy(update={"contact_value": "new-number"})
    corrected = await service.mutate(
        "contact_correct",
        correction,
        caregiver,
        "correct",
        case_id,
        UUID(original["logical_contact_id"]),
    )
    assert corrected["supersedes_revision_id"] == original["id"]
    assert corrected["revision_no"] == 2
    assert corrected["recorded_by_actor_id"] == caregiver.actor_id
    history = await service.read("contacts", case_id, caregiver)
    assert [r.contact_value for r in history] == ["old-number", "new-number"]
    workspace = await service.read("workspace", case_id, caregiver)
    assert [r.contact_value for r in workspace.contacts] == ["new-number"]
    with pytest.raises(DomainError, match="STALE_RECORD_REVISION"):
        await service.mutate(
            "contact_correct",
            correction,
            caregiver,
            "stale",
            case_id,
            UUID(original["logical_contact_id"]),
        )


@pytest.mark.parametrize(
    "kind,record_type",
    [
        ("interaction", "CONTACT"),
        ("interaction", "MONITORING"),
        ("observation", "OBSERVATION"),
        ("observation", "NEED_CAPTURE"),
    ],
)
async def test_immutable_record_correction(
    service, admin_engine, manager, caregiver, kind, record_type
):
    _, case_id, assignment_id = await seed(service, manager)
    record_cls = RecordInteraction if kind == "interaction" else RecordObservation
    correct_cls = CorrectInteraction if kind == "interaction" else CorrectObservation
    type_field = "interaction_type" if kind == "interaction" else "record_type"
    record = record_cls.model_validate(
        dict(
            expected_current_assignment_id=assignment_id,
            occurred_at=datetime.now(UTC),
            content="original",
            **{type_field: record_type},
        )
    )
    original = await service.mutate(f"{kind}_add", record, caregiver, "add", case_id)
    correction = correct_cls.model_validate(
        dict(
            **record.model_dump(),
            expected_current_record_id=original["id"],
            correction_reason="clarify",
        )
    ).model_copy(update={"content": "corrected"})
    corrected = await service.mutate(
        f"{kind}_correct", correction, caregiver, "correct", case_id, UUID(original["id"])
    )
    assert corrected[f"supersedes_{kind}_id"] == original["id"]
    page = await service.read(f"{kind}s", case_id, caregiver, limit=1)
    assert page.items[0].content == "original"
    assert page.next_cursor
    second = await service.read(f"{kind}s", case_id, caregiver, cursor=page.next_cursor, limit=1)
    assert second.items[0].content == "corrected"
    assert second.next_cursor is None
    workspace = await service.read("workspace", case_id, caregiver)
    assert getattr(workspace, f"{kind}s")[0].content == "corrected"
    with pytest.raises(DomainError, match="STALE_RECORD_REVISION"):
        await service.mutate(
            f"{kind}_correct", correction, caregiver, "stale", case_id, UUID(original["id"])
        )
    assert await effects(admin_engine) == (1, 1, 3, 3, 3)


async def test_cross_case_correction_rejected(service, manager, caregiver):
    _, case_id, assignment_id = await seed(service, manager)
    other = await service.mutate("create", create_command(), manager, "other")
    other_id = UUID(other["case"]["id"])
    contact = await service.mutate(
        "contact_add",
        AddContactPoint(
            expected_current_assignment_id=UUID(other["current_assignment"]["id"]),
            contact_kind="phone",
            contact_value="other",
        ),
        caregiver,
        "contact",
        other_id,
    )
    with pytest.raises(DomainError, match="RECORD_NOT_FOUND"):
        await service.mutate(
            "contact_correct",
            CorrectContactPoint(
                expected_current_assignment_id=assignment_id,
                expected_current_revision_id=UUID(contact["id"]),
                contact_kind="phone",
                contact_value="changed",
                correction_reason="reason",
            ),
            caregiver,
            "cross-case",
            case_id,
            UUID(contact["logical_contact_id"]),
        )


async def test_stale_assignment_blocks_new_mutation(service, admin_engine, manager, caregiver):
    _, case_id, assignment_id = await seed(service, manager)
    await service.mutate(
        "reassign",
        ReassignCaregiver(
            expected_current_assignment_id=assignment_id,
            caregiver_actor_id=caregiver.actor_id,
            reason="renew",
        ),
        manager,
        "renew",
        case_id,
    )
    with pytest.raises(DomainError, match="CASE_ASSIGNMENT_CHANGED"):
        await service.mutate(
            "contact_add",
            AddContactPoint(
                expected_current_assignment_id=assignment_id,
                contact_kind="phone",
                contact_value="number",
            ),
            caregiver,
            "add",
            case_id,
        )
    assert await effects(admin_engine) == (1, 2, 2, 2, 2)


async def test_cached_sensitive_result_requires_current_authorization(service, manager, caregiver):
    _, case_id, assignment_id = await seed(service, manager)
    command = AddContactPoint(
        expected_current_assignment_id=assignment_id, contact_kind="phone", contact_value="private"
    )
    await service.mutate("contact_add", command, caregiver, "key", case_id)
    await service.mutate(
        "reassign",
        ReassignCaregiver(
            expected_current_assignment_id=assignment_id, caregiver_actor_id="new", reason="handoff"
        ),
        manager,
        "handoff",
        case_id,
    )
    with pytest.raises(DomainError, match="ASSIGNED_CAREGIVER_REQUIRED"):
        await service.mutate("contact_add", command, caregiver, "key", case_id)


async def test_timeline_cursor_is_stable_and_complete(service, manager, caregiver):
    _, case_id, assignment_id = await seed(service, manager)
    for index in range(3):
        await service.mutate(
            "contact_add",
            AddContactPoint(
                expected_current_assignment_id=assignment_id,
                contact_kind="phone",
                contact_value=str(index),
            ),
            caregiver,
            str(index),
            case_id,
        )
    first = await service.read("timeline", case_id, caregiver, limit=2)
    second = await service.read("timeline", case_id, caregiver, cursor=first.next_cursor, limit=2)
    assert len(first.items) == len(second.items) == 2
    assert not set(r.id for r in first.items) & set(r.id for r in second.items)
    assert first.items[0].action == "case.created.v1"
    assert first.next_cursor and second.next_cursor is None


async def test_rollback_after_business_and_audit_outbox_flush(
    service, admin_engine, manager, monkeypatch
):
    original = service._record_effects

    async def fail_after_effects(*args, **kwargs):
        await original(*args, **kwargs)
        await args[0].flush()
        raise RuntimeError("injected after domain and audit/outbox flush")

    monkeypatch.setattr(service, "_record_effects", fail_after_effects)
    with pytest.raises(RuntimeError, match="injected"):
        await service.mutate("create", create_command(), manager, "create")
    assert await effects(admin_engine) == (0, 0, 0, 0, 0)
    monkeypatch.setattr(service, "_record_effects", original)
    await service.mutate("create", create_command(), manager, "create")
    assert await effects(admin_engine) == (1, 1, 1, 1, 1)


async def test_rollback_restores_ended_assignment(service, admin_engine, manager, monkeypatch):
    _, case_id, assignment_id = await seed(service, manager)

    async def fail(*args, **kwargs):
        raise RuntimeError("injected")

    monkeypatch.setattr(service, "_record_effects", fail)
    with pytest.raises(RuntimeError):
        await service.mutate(
            "reassign",
            ReassignCaregiver(
                expected_current_assignment_id=assignment_id,
                caregiver_actor_id="new",
                reason="handoff",
            ),
            manager,
            "key",
            case_id,
        )
    assert await effects(admin_engine) == (1, 1, 1, 1, 1)
    history = await service.read("assignments", case_id, manager)
    assert history[0].id == assignment_id and history[0].ended_at is None


async def run_race(*operations):
    # Concurrent tasks use separate SQLAlchemy sessions/connections, not shared mocks.
    gate = asyncio.Event()

    async def contender(operation):
        await gate.wait()
        return await operation

    tasks = [asyncio.create_task(contender(op)) for op in operations]
    gate.set()
    return await asyncio.gather(*tasks, return_exceptions=True)


async def test_real_concurrent_reassignment_single_winner(service, admin_engine, manager):
    _, case_id, assignment_id = await seed(service, manager)
    outcomes = await run_race(
        *[
            service.mutate(
                "reassign",
                ReassignCaregiver(
                    expected_current_assignment_id=assignment_id,
                    caregiver_actor_id=f"caregiver-{index}",
                    reason="race",
                ),
                manager,
                f"key-{index}",
                case_id,
            )
            for index in range(6)
        ]
    )
    assert sum(isinstance(value, dict) for value in outcomes) == 1
    losers = [v for v in outcomes if isinstance(v, DomainError)]
    assert len(losers) == 5 and all(v.code == "CASE_ASSIGNMENT_CHANGED" for v in losers)
    assert await effects(admin_engine) == (1, 2, 2, 2, 2)
    async with admin_engine.connect() as conn:
        assert (
            await conn.scalar(
                select(func.count()).select_from(Assignment).where(Assignment.ended_at.is_(None))
            )
            == 1
        )


async def test_real_concurrent_creation_idempotency(service, admin_engine, manager):
    outcomes = await run_race(
        *[service.mutate("create", create_command(), manager, "same") for _ in range(8)]
    )
    assert all(isinstance(value, dict) for value in outcomes)
    assert all(value == outcomes[0] for value in outcomes)
    assert await effects(admin_engine) == (1, 1, 1, 1, 1)


async def test_real_concurrent_idempotency_conflict(service, admin_engine, manager):
    outcomes = await run_race(
        *[
            service.mutate(
                "create",
                create_command().model_copy(update={"elder_reference": str(index)}),
                manager,
                "same",
            )
            for index in range(6)
        ]
    )
    assert sum(isinstance(value, dict) for value in outcomes) == 1
    losers = [v for v in outcomes if isinstance(v, DomainError)]
    assert len(losers) == 5 and all(
        v.code == "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD" for v in losers
    )
    assert await effects(admin_engine) == (1, 1, 1, 1, 1)


async def test_real_concurrent_corrections_single_winner(service, admin_engine, manager):
    original, case_id, assignment_id = await seed(service, manager)
    command = CorrectCaseProfile(
        expected_current_assignment_id=assignment_id,
        expected_current_revision_id=UUID(original["profile"]["id"]),
        elder_reference="corrected",
        correction_reason="fix",
    )
    outcomes = await run_race(
        *[service.mutate("profile_correct", command, manager, str(i), case_id) for i in range(4)]
    )
    assert sum(isinstance(value, dict) for value in outcomes) == 1
    assert (
        sum(
            isinstance(value, DomainError) and value.code == "STALE_RECORD_REVISION"
            for value in outcomes
        )
        == 3
    )
    assert await effects(admin_engine) == (1, 1, 2, 2, 2)


async def test_database_unique_active_assignment(service, admin_engine, manager):
    _, case_id, _ = await seed(service, manager)
    async with admin_engine.connect() as conn:
        with pytest.raises(IntegrityError):
            async with conn.begin():
                await conn.execute(
                    text("""INSERT INTO case_assignment
                    (id,case_id,caregiver_actor_id,started_at,assigned_by_actor_id,assigned_by_actor_type,reason)
                    VALUES (:id,:case_id,'other',now(),'manager','HUMAN','race')"""),
                    {"id": uuid4(), "case_id": case_id},
                )


@pytest.mark.parametrize(
    "table,column",
    [
        ("audit_entry", "reason"),
        ("case_profile_revision", "elder_reference"),
        ("contact_point_revision", "contact_value"),
        ("case_interaction", "content"),
        ("case_observation", "content"),
    ],
)
@pytest.mark.parametrize("operation", ["update", "delete"])
async def test_database_history_protected(
    service, admin_engine, manager, caregiver, table, column, operation
):
    _, case_id, assignment_id = await seed(service, manager)
    await service.mutate(
        "contact_add",
        AddContactPoint(
            expected_current_assignment_id=assignment_id,
            contact_kind="phone",
            contact_value="original",
        ),
        caregiver,
        "contact",
        case_id,
    )
    await service.mutate(
        "interaction_add",
        RecordInteraction(
            expected_current_assignment_id=assignment_id,
            interaction_type="CONTACT",
            occurred_at=datetime.now(UTC),
            content="original",
        ),
        caregiver,
        "interaction",
        case_id,
    )
    await service.mutate(
        "observation_add",
        RecordObservation(
            expected_current_assignment_id=assignment_id,
            record_type="OBSERVATION",
            occurred_at=datetime.now(UTC),
            content="original",
        ),
        caregiver,
        "observation",
        case_id,
    )
    # Administrative login also encounters the immutable-history trigger on ordinary SQL.
    sql = (
        f"UPDATE {table} SET {column}='changed'"
        if operation == "update"
        else f"DELETE FROM {table}"
    )
    async with admin_engine.connect() as conn:
        with pytest.raises(DBAPIError, match="append-only"):
            async with conn.begin():
                await conn.execute(text(sql))


async def test_application_role_has_no_destructive_privileges(service, manager):
    await seed(service, manager)
    async with service.sessions() as session:
        role = await session.scalar(text("SELECT current_user"))
        assert role == "nasim_app", (
            "Run test suite with NASIM_TEST_APP_DATABASE_URL for least-privilege validation"
        )
        for table in [
            "elder_case",
            "audit_entry",
            "case_profile_revision",
            "case_interaction",
            "case_observation",
        ]:
            assert not await session.scalar(
                text("SELECT has_table_privilege(current_user, :table, 'DELETE')"), {"table": table}
            )
            assert not await session.scalar(
                text("SELECT has_table_privilege(current_user, :table, 'TRUNCATE')"),
                {"table": table},
            )
        assert not await session.scalar(
            text("SELECT has_table_privilege(current_user, 'audit_entry', 'UPDATE')")
        )


async def test_lineage_fk_prevents_cross_case_and_orphans(service, admin_engine, manager):
    original, case_id, _ = await seed(service, manager)
    other = await service.mutate("create", create_command(), manager, "other")
    for child_case_id in [UUID(other["case"]["id"]), uuid4()]:
        async with admin_engine.connect() as conn:
            with pytest.raises(IntegrityError):
                async with conn.begin():
                    await conn.execute(
                        text("""INSERT INTO case_profile_revision
                        (id,case_id,revision_no,elder_reference,supersedes_revision_id,correction_reason,
                         recorded_at,recorded_by_actor_id,recorded_by_actor_type)
                        VALUES (:id,:case_id,2,'ref',:before,'correction',
                                now(),'manager','HUMAN')"""),
                        {
                            "id": uuid4(),
                            "case_id": child_case_id,
                            "before": UUID(original["profile"]["id"]),
                        },
                    )


@pytest.mark.parametrize("actor_type", [ActorType.SYSTEM, ActorType.AUTOMATION])
async def test_execution_provenance_is_preserved(service, admin_engine, manager, actor_type):
    actor = manager.model_copy(update={"actor_type": actor_type})
    original, case_id, assignment_id = await seed(service, actor)
    assert original["case"]["created_by_actor_type"] == actor_type
    correction = CorrectCaseProfile(
        expected_current_assignment_id=assignment_id,
        expected_current_revision_id=UUID(original["profile"]["id"]),
        elder_reference="corrected",
        correction_reason="fix",
    )
    result = await service.mutate("profile_correct", correction, manager, "correct", case_id)
    assert result["recorded_by_actor_type"] == ActorType.HUMAN
    workspace = await service.read("workspace", case_id, manager)
    assert workspace.profile_history[0].recorded_by_actor_type == actor_type
    async with admin_engine.connect() as conn:
        assert (
            await conn.scalar(
                select(AuditEntry.actor_type).where(AuditEntry.action == "case.created.v1")
            )
            == actor_type
        )


async def test_database_idempotency_uniqueness(service, admin_engine, manager):
    await seed(service, manager)
    async with admin_engine.connect() as conn:
        with pytest.raises(IntegrityError):
            async with conn.begin():
                await conn.execute(
                    text("""INSERT INTO idempotency_record
                    (id,actor_id,operation,target,key,payload_hash,response,created_at)
                    SELECT :id,actor_id,operation,target,key,payload_hash,response,created_at
                    FROM idempotency_record LIMIT 1"""),
                    {"id": uuid4()},
                )


async def test_same_key_scoped_to_actor_operation_case(service, admin_engine, manager, caregiver):
    _, case_id, assignment_id = await seed(service, manager)
    other = await service.mutate("create", create_command(), manager, "other")
    command = AddContactPoint(
        expected_current_assignment_id=assignment_id, contact_kind="phone", contact_value="value"
    )
    first = await service.mutate("contact_add", command, caregiver, "same", case_id)
    assert await service.mutate("contact_add", command, caregiver, "same", case_id) == first
    second = await service.mutate(
        "contact_add",
        command.model_copy(
            update={"expected_current_assignment_id": UUID(other["current_assignment"]["id"])}
        ),
        caregiver,
        "same",
        UUID(other["case"]["id"]),
    )
    assert first["id"] != second["id"]
    observation = await service.mutate(
        "observation_add",
        RecordObservation(
            expected_current_assignment_id=assignment_id,
            record_type="OBSERVATION",
            occurred_at=datetime.now(UTC),
            content="note",
        ),
        caregiver,
        "same",
        case_id,
    )
    assert observation["id"] != first["id"]
    assert await effects(admin_engine) == (2, 2, 5, 5, 5)


async def test_rejected_correction_does_not_write_effects(service, admin_engine, manager):
    original, case_id, assignment_id = await seed(service, manager)
    with pytest.raises(DomainError, match="STALE_RECORD_REVISION"):
        await service.mutate(
            "profile_correct",
            CorrectCaseProfile(
                expected_current_assignment_id=assignment_id,
                expected_current_revision_id=uuid4(),
                elder_reference="invalid",
                correction_reason="fix",
            ),
            manager,
            "stale",
            case_id,
        )
    assert await effects(admin_engine) == (1, 1, 1, 1, 1)
    workspace = await service.read("workspace", case_id, manager)
    assert str(workspace.profile.id) == original["profile"]["id"]


async def test_database_correction_cannot_omit_reason(service, admin_engine, manager):
    original, case_id, _ = await seed(service, manager)
    async with admin_engine.connect() as conn:
        with pytest.raises(IntegrityError):
            async with conn.begin():
                await conn.execute(
                    text("""INSERT INTO case_profile_revision
                    (id,case_id,revision_no,elder_reference,supersedes_revision_id,
                     recorded_at,recorded_by_actor_id,recorded_by_actor_type)
                    VALUES (:id,:case_id,2,'ref',:before,now(),'manager','HUMAN')"""),
                    {"id": uuid4(), "case_id": case_id, "before": UUID(original["profile"]["id"])},
                )


async def test_contact_lineage_preserves_logical_identity(
    service, admin_engine, manager, caregiver
):
    _, case_id, assignment_id = await seed(service, manager)
    contact = await service.mutate(
        "contact_add",
        AddContactPoint(
            expected_current_assignment_id=assignment_id,
            contact_kind="phone",
            contact_value="original",
        ),
        caregiver,
        "contact",
        case_id,
    )
    async with admin_engine.connect() as conn:
        with pytest.raises(IntegrityError):
            async with conn.begin():
                await conn.execute(
                    text("""INSERT INTO contact_point_revision
                    (id,case_id,logical_contact_id,revision_no,contact_kind,contact_value,
                     supersedes_revision_id,correction_reason,
                     recorded_at,recorded_by_actor_id,recorded_by_actor_type)
                    VALUES (:id,:case_id,:logical,2,'phone','new',:before,'fix',
                            now(),'actor','HUMAN')"""),
                    {
                        "id": uuid4(),
                        "case_id": case_id,
                        "logical": uuid4(),
                        "before": UUID(contact["id"]),
                    },
                )


@pytest.mark.parametrize(
    "operation,command_cls,extra",
    [
        ("contact_add", AddContactPoint, {"contact_kind": "phone", "contact_value": "value"}),
        (
            "interaction_add",
            RecordInteraction,
            {"interaction_type": "CONTACT", "occurred_at": datetime.now(UTC), "content": "note"},
        ),
        (
            "observation_add",
            RecordObservation,
            {"record_type": "OBSERVATION", "occurred_at": datetime.now(UTC), "content": "note"},
        ),
    ],
)
async def test_record_mutations_need_both_assignment_and_capability(
    service, admin_engine, manager, caregiver, operation, command_cls, extra
):
    _, case_id, assignment_id = await seed(service, manager)
    command = command_cls.model_validate({"expected_current_assignment_id": assignment_id, **extra})
    no_capability = caregiver.model_copy(update={"capabilities": frozenset()})
    other_caregiver = caregiver.model_copy(update={"actor_id": "other-caregiver"})
    with pytest.raises(DomainError, match="CAPABILITY_REQUIRED"):
        await service.mutate(operation, command, no_capability, "key", case_id)
    with pytest.raises(DomainError, match="ASSIGNED_CAREGIVER_REQUIRED"):
        await service.mutate(operation, command, other_caregiver, "key", case_id)
    assert await effects(admin_engine) == (1, 1, 1, 1, 1)


async def test_real_concurrent_reassignment_idempotent_retry(service, admin_engine, manager):
    _, case_id, assignment_id = await seed(service, manager)
    command = ReassignCaregiver(
        expected_current_assignment_id=assignment_id,
        caregiver_actor_id="new-caregiver",
        reason="handoff",
    )
    outcomes = await run_race(
        *[service.mutate("reassign", command, manager, "same-key", case_id) for _ in range(6)]
    )
    assert all(isinstance(result, dict) and result == outcomes[0] for result in outcomes)
    assert await effects(admin_engine) == (1, 2, 2, 2, 2)
