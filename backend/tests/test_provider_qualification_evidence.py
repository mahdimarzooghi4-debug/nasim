import asyncio
import os
from datetime import UTC, datetime
from uuid import UUID, uuid4

import httpx
import pytest
from pydantic import PostgresDsn, ValidationError
from sqlalchemy import func, select, text
from sqlalchemy.exc import DBAPIError

from nasim.api.app import create_app, get_actor
from nasim.authorization.contracts import TrustedPrincipal, Window
from nasim.authorization.models import RoleDefinition
from nasim.authorization.service import AuthorizationResolver, Provisioning
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType
from nasim.infrastructure.config import Settings
from nasim.infrastructure.database import make_engine, make_sessions
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent
from nasim.provider_registry.contracts import (
    RecordProviderQualificationEvidence,
    RegisterProviderCandidate,
)
from nasim.provider_registry.models import (
    ProviderCandidateRecord,
    ProviderQualificationEvidenceRecord,
)
from nasim.provider_registry.service import ProviderCandidates, ProviderQualificationEvidence


@pytest.fixture
def qualification_actor() -> ActorContext:
    return ActorContext(
        actor_id="qualification-evidence-recorder",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset(
            {
                "provider_qualification_evidence.record",
                "provider_qualification_evidence.read",
            }
        ),
        correlation_id="qualification-evidence-test",
    )


@pytest.fixture
def candidate_actor() -> ActorContext:
    return ActorContext(
        actor_id="candidate-registrar-for-qualification-tests",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset({"provider_candidate.register", "provider_candidate.read"}),
        correlation_id="qualification-candidate-setup",
    )


@pytest.fixture
async def qualification_service(admin_engine):
    url = os.environ.get("NASIM_TEST_APP_DATABASE_URL") or os.environ["NASIM_TEST_DATABASE_URL"]
    engine = make_engine(Settings(database_url=PostgresDsn(url)))
    yield ProviderQualificationEvidence(make_sessions(engine))
    await engine.dispose()


@pytest.fixture
async def candidate_service(admin_engine):
    url = os.environ.get("NASIM_TEST_APP_DATABASE_URL") or os.environ["NASIM_TEST_DATABASE_URL"]
    engine = make_engine(Settings(database_url=PostgresDsn(url)))
    yield ProviderCandidates(make_sessions(engine))
    await engine.dispose()


@pytest.fixture
async def candidate_id(candidate_service, candidate_actor) -> UUID:
    result = await candidate_service.register(
        RegisterProviderCandidate(
            display_name="Qualification Candidate",
            reason="Qualification evidence test setup",
        ),
        candidate_actor,
        f"candidate-{uuid4()}",
    )
    return UUID(result["id"])


def command(
    label: str = "Professional credential reference",
    reference: str = "opaque-reference-001",
    reason: str = "Evidence capture only",
) -> RecordProviderQualificationEvidence:
    return RecordProviderQualificationEvidence(
        evidence_label=label,
        evidence_reference=reference,
        reason=reason,
    )


async def evidence_counts(admin_engine) -> tuple[int, int, int, int]:
    async with admin_engine.connect() as conn:
        return (
            await conn.scalar(
                select(func.count()).select_from(ProviderQualificationEvidenceRecord)
            ),
            await conn.scalar(
                select(func.count())
                .select_from(AuditEntry)
                .where(AuditEntry.action == "provider.qualification_evidence_recorded.v1")
            ),
            await conn.scalar(
                select(func.count())
                .select_from(OutboxEvent)
                .where(OutboxEvent.event_type == "provider.qualification_evidence_recorded.v1")
            ),
            await conn.scalar(
                select(func.count())
                .select_from(IdempotencyRecord)
                .where(IdempotencyRecord.operation.like("provider.qualification_evidence.record.%"))
            ),
        )


async def test_record_qualification_evidence_foundation_only(
    qualification_service,
    qualification_actor,
    candidate_id,
    admin_engine,
):
    before_candidate = None
    async with admin_engine.connect() as conn:
        before_candidate = (
            await conn.execute(
                select(ProviderCandidateRecord).where(ProviderCandidateRecord.id == candidate_id)
            )
        ).scalar_one()

    result = await qualification_service.record(
        candidate_id, command(), qualification_actor, "record-1"
    )

    assert result["provider_candidate_id"] == str(candidate_id)
    assert result["evidence_label"] == "Professional credential reference"
    assert result["evidence_reference"] == "opaque-reference-001"
    assert result["recorded_by_actor_id"] == qualification_actor.actor_id
    assert result["recorded_by_actor_type"] == "HUMAN"
    assert await evidence_counts(admin_engine) == (1, 1, 1, 1)

    async with admin_engine.connect() as conn:
        payload = await conn.scalar(
            select(OutboxEvent.payload).where(
                OutboxEvent.event_type == "provider.qualification_evidence_recorded.v1"
            )
        )
        audit_case = await conn.scalar(
            select(AuditEntry.case_id).where(
                AuditEntry.action == "provider.qualification_evidence_recorded.v1"
            )
        )
        outbox_case = await conn.scalar(
            select(OutboxEvent.case_id).where(
                OutboxEvent.event_type == "provider.qualification_evidence_recorded.v1"
            )
        )
        after_candidate = (
            await conn.execute(
                select(ProviderCandidateRecord).where(ProviderCandidateRecord.id == candidate_id)
            )
        ).scalar_one()

    assert payload["provider_qualification_evidence_id"] == result["id"]
    assert payload["provider_candidate_id"] == str(candidate_id)
    assert "evidence_label" not in payload
    assert "evidence_reference" not in payload
    assert audit_case is None
    assert outbox_case is None
    assert before_candidate.id == after_candidate.id
    assert before_candidate.display_name == after_candidate.display_name
    assert before_candidate.registered_at == after_candidate.registered_at


@pytest.mark.parametrize(
    "field",
    [
        "qualified",
        "approved",
        "active",
        "status",
        "result",
        "decision",
        "score",
        "threshold",
        "valid",
        "verified",
        "expired",
        "reviewer",
        "approver",
        "provider_type",
        "service",
        "service_family",
        "geography",
        "capacity",
        "contract",
        "case_id",
        "elder_id",
        "referral_id",
        "ranking",
        "price",
        "settlement",
    ],
)
def test_contract_rejects_qualification_decision_fields(field):
    with pytest.raises(ValidationError):
        RecordProviderQualificationEvidence(
            evidence_label="Evidence",
            evidence_reference="opaque",
            reason="capture",
            **{field: "invented"},
        )


@pytest.mark.parametrize("field", ["evidence_label", "evidence_reference", "reason"])
@pytest.mark.parametrize("value", ["", " ", "\n"])
def test_evidence_text_is_nonblank(field, value):
    body = {
        "evidence_label": "Evidence",
        "evidence_reference": "opaque",
        "reason": "capture",
    }
    body[field] = value
    with pytest.raises(ValidationError):
        RecordProviderQualificationEvidence(**body)


async def test_duplicate_evidence_references_are_allowed(
    qualification_service,
    qualification_actor,
    candidate_id,
    admin_engine,
):
    first = await qualification_service.record(
        candidate_id, command(reference="same-reference"), qualification_actor, "one"
    )
    second = await qualification_service.record(
        candidate_id, command(reference="same-reference"), qualification_actor, "two"
    )
    assert first["id"] != second["id"]
    assert await evidence_counts(admin_engine) == (2, 2, 2, 2)


async def test_missing_candidate_fails_without_side_effects(
    qualification_service, qualification_actor, admin_engine
):
    with pytest.raises(DomainError) as error:
        await qualification_service.record(
            uuid4(), command(), qualification_actor, "missing-candidate"
        )
    assert error.value.code == "PROVIDER_CANDIDATE_NOT_FOUND"
    assert await evidence_counts(admin_engine) == (0, 0, 0, 0)


async def test_missing_capability_and_actor_type_alone_deny(
    qualification_service, qualification_actor, candidate_id
):
    for actor_type in ActorType:
        actor = qualification_actor.model_copy(
            update={"actor_type": actor_type, "capabilities": frozenset()}
        )
        with pytest.raises(DomainError) as error:
            await qualification_service.record(
                candidate_id,
                command(),
                actor,
                f"missing-{actor_type.value}",
            )
        assert error.value.code == "CAPABILITY_REQUIRED"


async def test_ai_denied_even_with_explicit_capability(
    qualification_service,
    qualification_actor,
    candidate_id,
    admin_engine,
):
    ai = qualification_actor.model_copy(update={"actor_type": ActorType.AI})
    with pytest.raises(DomainError) as error:
        await qualification_service.record(candidate_id, command(), ai, "ai")
    assert error.value.code == "CAPABILITY_REQUIRED"
    assert await evidence_counts(admin_engine) == (0, 0, 0, 0)


async def test_role_title_alone_does_not_create_qualification_authority(
    admin_engine, qualification_actor
):
    sessions = make_sessions(admin_engine)
    provision = Provisioning(sessions)
    resolver = AuthorizationResolver(sessions)
    principal = TrustedPrincipal(
        actor_id=f"qualification-role-only-{uuid4()}",
        actor_type=ActorType.HUMAN,
        correlation_id="qualification-role-only",
    )
    async with sessions() as session:
        role_id = await session.scalar(
            select(RoleDefinition.id).where(
                RoleDefinition.code == "specialist_provider",
                RoleDefinition.revision_no == 1,
            )
        )
    assert role_id is not None
    assignment_id = await provision.assign(
        principal,
        role_id,
        Window(starts_at=datetime.now(UTC), reason="Role vocabulary only"),
        qualification_actor,
    )
    try:
        resolved = await resolver.resolve(principal)
        assert "provider_qualification_evidence.record" not in resolved.capabilities
        assert "provider_qualification_evidence.read" not in resolved.capabilities
    finally:
        await provision.revoke(
            "assignment",
            assignment_id,
            qualification_actor,
            "Test cleanup preserves history",
        )


async def test_idempotent_retry_and_payload_conflict(
    qualification_service,
    qualification_actor,
    candidate_id,
    admin_engine,
):
    first = await qualification_service.record(
        candidate_id, command(), qualification_actor, "same-key"
    )
    assert (
        await qualification_service.record(candidate_id, command(), qualification_actor, "same-key")
        == first
    )

    with pytest.raises(DomainError) as error:
        await qualification_service.record(
            candidate_id,
            command(reason="different reason"),
            qualification_actor,
            "same-key",
        )
    assert error.value.code == "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"
    assert await evidence_counts(admin_engine) == (1, 1, 1, 1)


async def test_same_key_is_scoped_to_candidate(
    qualification_service,
    qualification_actor,
    candidate_service,
    candidate_actor,
    candidate_id,
    admin_engine,
):
    second = await candidate_service.register(
        RegisterProviderCandidate(
            display_name="Second Qualification Candidate",
            reason="Scope isolation",
        ),
        candidate_actor,
        "candidate-two",
    )
    first_result = await qualification_service.record(
        candidate_id, command(), qualification_actor, "candidate-scoped"
    )
    second_result = await qualification_service.record(
        UUID(second["id"]), command(), qualification_actor, "candidate-scoped"
    )
    assert first_result["id"] != second_result["id"]
    assert await evidence_counts(admin_engine) == (2, 2, 2, 2)


async def test_record_race_is_serialized(
    qualification_service,
    qualification_actor,
    candidate_id,
    admin_engine,
):
    results = await asyncio.gather(
        qualification_service.record(candidate_id, command(), qualification_actor, "race"),
        qualification_service.record(candidate_id, command(), qualification_actor, "race"),
    )
    assert results[0] == results[1]
    assert await evidence_counts(admin_engine) == (1, 1, 1, 1)


async def test_record_race_with_different_payload_has_one_conflict(
    qualification_service,
    qualification_actor,
    candidate_id,
    admin_engine,
):
    results = await asyncio.gather(
        qualification_service.record(
            candidate_id,
            command(reason="one"),
            qualification_actor,
            "race-conflict",
        ),
        qualification_service.record(
            candidate_id,
            command(reason="two"),
            qualification_actor,
            "race-conflict",
        ),
        return_exceptions=True,
    )
    assert sum(not isinstance(result, Exception) for result in results) == 1
    assert (
        sum(
            isinstance(result, DomainError)
            and result.code == "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"
            for result in results
        )
        == 1
    )
    assert await evidence_counts(admin_engine) == (1, 1, 1, 1)


async def test_atomic_rollback_after_effects_flush(
    qualification_service,
    qualification_actor,
    candidate_id,
    admin_engine,
    monkeypatch,
):
    original = qualification_service.effects.append

    async def fail_after_flush(*args, **kwargs):
        await original(*args, **kwargs)
        raise RuntimeError("injected rollback")

    monkeypatch.setattr(qualification_service.effects, "append", fail_after_flush)
    with pytest.raises(RuntimeError):
        await qualification_service.record(candidate_id, command(), qualification_actor, "rollback")
    assert await evidence_counts(admin_engine) == (0, 0, 0, 0)

    monkeypatch.setattr(qualification_service.effects, "append", original)
    await qualification_service.record(candidate_id, command(), qualification_actor, "rollback")
    assert await evidence_counts(admin_engine) == (1, 1, 1, 1)


@pytest.mark.parametrize("operation", ["UPDATE", "DELETE"])
async def test_qualification_evidence_history_is_immutable(
    qualification_service,
    qualification_actor,
    candidate_id,
    admin_engine,
    operation,
):
    result = await qualification_service.record(
        candidate_id, command(), qualification_actor, "immutable"
    )
    statement = (
        "DELETE FROM provider_qualification_evidence_record WHERE id=:id"
        if operation == "DELETE"
        else (
            "UPDATE provider_qualification_evidence_record "
            "SET evidence_reference='tampered' WHERE id=:id"
        )
    )
    async with admin_engine.begin() as conn:
        with pytest.raises(DBAPIError):
            await conn.execute(text(statement), {"id": UUID(result["id"])})


async def test_direct_insert_without_atomic_effects_fails(
    admin_engine, qualification_actor, candidate_id
):
    row = ProviderQualificationEvidenceRecord(
        id=uuid4(),
        provider_candidate_id=candidate_id,
        evidence_label="Unlogged evidence",
        evidence_reference="opaque-unlogged",
        recorded_at=datetime.now(UTC),
        recorded_by_actor_id=qualification_actor.actor_id,
        recorded_by_actor_type=qualification_actor.actor_type.value,
        reason="must fail",
        correlation_id=qualification_actor.correlation_id,
    )
    async with make_sessions(admin_engine)() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                session.add(row)
                await session.flush()
    assert await evidence_counts(admin_engine) == (0, 0, 0, 0)


async def test_read_list_detail_and_pagination(
    qualification_service,
    qualification_actor,
    candidate_id,
):
    first = await qualification_service.record(
        candidate_id, command(label="One"), qualification_actor, "one"
    )
    second = await qualification_service.record(
        candidate_id, command(label="Two"), qualification_actor, "two"
    )
    page = await qualification_service.list(candidate_id, qualification_actor, limit=1)
    assert len(page.items) == 1
    assert page.next_cursor
    next_page = await qualification_service.list(
        candidate_id,
        qualification_actor,
        cursor=page.next_cursor,
        limit=1,
    )
    assert len(next_page.items) == 1
    assert {str(page.items[0].id), str(next_page.items[0].id)} == {
        first["id"],
        second["id"],
    }
    assert (
        await qualification_service.get(UUID(first["id"]), qualification_actor)
    ).evidence_label == "One"

    no_read = qualification_actor.model_copy(
        update={"capabilities": frozenset({"provider_qualification_evidence.record"})}
    )
    with pytest.raises(DomainError) as error:
        await qualification_service.list(candidate_id, no_read)
    assert error.value.code == "CAPABILITY_REQUIRED"


async def test_http_anonymous_denial_and_no_qualification_decision_routes():
    app = create_app(Settings(database_url=PostgresDsn("postgresql://unused@127.0.0.1:1/unused")))
    candidate_id = uuid4()
    evidence_id = uuid4()
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                f"/api/v1/provider-candidates/{candidate_id}/qualification-evidence",
                json={
                    "evidence_label": "Evidence",
                    "evidence_reference": "opaque",
                    "reason": "capture",
                },
                headers={"Idempotency-Key": "key"},
            )
            assert response.status_code == 401
            assert (
                await client.get(
                    f"/api/v1/provider-candidates/{candidate_id}/qualification-evidence"
                )
            ).status_code == 401
            assert (
                await client.get(f"/api/v1/provider-qualification-evidence/{evidence_id}")
            ).status_code == 401

            for action in (
                "review",
                "verify",
                "qualify",
                "approve",
                "reject",
                "activate",
                "expire",
                "replace",
            ):
                assert (
                    await client.post(
                        f"/api/v1/provider-qualification-evidence/{evidence_id}/{action}",
                        json={},
                        headers={"Idempotency-Key": "key"},
                    )
                ).status_code == 404
    finally:
        await app.state.engine.dispose()


async def test_http_record_with_trusted_context(
    qualification_actor,
    candidate_service,
    candidate_actor,
    admin_engine,
):
    candidate = await candidate_service.register(
        RegisterProviderCandidate(
            display_name="HTTP Qualification Candidate",
            reason="HTTP qualification setup",
        ),
        candidate_actor,
        "http-candidate",
    )
    candidate_id = UUID(candidate["id"])
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    app.dependency_overrides[get_actor] = lambda: qualification_actor
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            created = await client.post(
                f"/api/v1/provider-candidates/{candidate_id}/qualification-evidence",
                json={
                    "evidence_label": "HTTP evidence",
                    "evidence_reference": "opaque-http",
                    "reason": "capture",
                },
                headers={"Idempotency-Key": "http-evidence"},
            )
            assert created.status_code == 201, created.text
            evidence_id = created.json()["id"]

            listed = await client.get(
                f"/api/v1/provider-candidates/{candidate_id}/qualification-evidence"
            )
            assert listed.status_code == 200
            assert listed.json()["items"][0]["id"] == evidence_id

            detail = await client.get(f"/api/v1/provider-qualification-evidence/{evidence_id}")
            assert detail.status_code == 200
            assert detail.json()["provider_candidate_id"] == str(candidate_id)
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()

    assert await evidence_counts(admin_engine) == (1, 1, 1, 1)
