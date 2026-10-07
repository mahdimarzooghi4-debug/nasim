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
from nasim.provider_registry.contracts import RegisterProviderCandidate
from nasim.provider_registry.models import ProviderCandidateRecord
from nasim.provider_registry.service import ProviderCandidates


@pytest.fixture
def provider_actor() -> ActorContext:
    return ActorContext(
        actor_id="provider-registrar",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset({"provider_candidate.register", "provider_candidate.read"}),
        correlation_id="provider-test",
    )


@pytest.fixture
async def provider_service(admin_engine):
    url = os.environ.get("NASIM_TEST_APP_DATABASE_URL") or os.environ["NASIM_TEST_DATABASE_URL"]
    engine = make_engine(Settings(database_url=PostgresDsn(url)))
    yield ProviderCandidates(make_sessions(engine))
    await engine.dispose()


def command(name: str = "Candidate Alpha", reason: str = "Network candidate registration"):
    return RegisterProviderCandidate(display_name=name, reason=reason)


async def counts(admin_engine) -> tuple[int, int, int, int]:
    async with admin_engine.connect() as conn:
        return (
            await conn.scalar(select(func.count()).select_from(ProviderCandidateRecord)),
            await conn.scalar(
                select(func.count())
                .select_from(AuditEntry)
                .where(AuditEntry.action == "provider.candidate_registered.v1")
            ),
            await conn.scalar(
                select(func.count())
                .select_from(OutboxEvent)
                .where(OutboxEvent.event_type == "provider.candidate_registered.v1")
            ),
            await conn.scalar(
                select(func.count())
                .select_from(IdempotencyRecord)
                .where(IdempotencyRecord.operation.like("provider.candidate.register.%"))
            ),
        )


async def test_register_provider_candidate_foundation_only(
    provider_service, provider_actor, admin_engine
):
    result = await provider_service.register(command(), provider_actor, "register-1")
    assert result["display_name"] == "Candidate Alpha"
    assert result["registered_by_actor_id"] == provider_actor.actor_id
    assert result["registered_by_actor_type"] == "HUMAN"
    assert await counts(admin_engine) == (1, 1, 1, 1)

    async with admin_engine.connect() as conn:
        payload = await conn.scalar(
            select(OutboxEvent.payload).where(
                OutboxEvent.event_type == "provider.candidate_registered.v1"
            )
        )
        audit_case = await conn.scalar(
            select(AuditEntry.case_id).where(
                AuditEntry.action == "provider.candidate_registered.v1"
            )
        )
        outbox_case = await conn.scalar(
            select(OutboxEvent.case_id).where(
                OutboxEvent.event_type == "provider.candidate_registered.v1"
            )
        )
    assert payload["provider_candidate_id"] == result["id"]
    assert "display_name" not in payload
    assert audit_case is None
    assert outbox_case is None


@pytest.mark.parametrize(
    "field",
    [
        "status",
        "active",
        "approved",
        "provider_type",
        "service",
        "service_family",
        "geography",
        "capacity",
        "credential",
        "qualification",
        "contract",
        "ranking",
        "score",
        "price",
        "settlement",
        "case_id",
        "referral_id",
    ],
)
def test_contract_rejects_operational_provider_fields(field):
    with pytest.raises(ValidationError):
        RegisterProviderCandidate(
            display_name="Candidate",
            reason="foundation",
            **{field: "invented"},
        )


@pytest.mark.parametrize("field", ["display_name", "reason"])
@pytest.mark.parametrize("value", ["", " ", "\n"])
def test_registration_text_is_nonblank(field, value):
    body = {"display_name": "Candidate", "reason": "foundation"}
    body[field] = value
    with pytest.raises(ValidationError):
        RegisterProviderCandidate(**body)


async def test_duplicate_display_names_are_allowed(provider_service, provider_actor, admin_engine):
    first = await provider_service.register(command("Same Name"), provider_actor, "one")
    second = await provider_service.register(command("Same Name"), provider_actor, "two")
    assert first["id"] != second["id"]
    assert await counts(admin_engine) == (2, 2, 2, 2)


async def test_missing_capability_and_actor_type_alone_deny(provider_service, provider_actor):
    for actor_type in ActorType:
        actor = provider_actor.model_copy(
            update={"actor_type": actor_type, "capabilities": frozenset()}
        )
        with pytest.raises(DomainError) as error:
            await provider_service.register(command(), actor, f"missing-{actor_type.value}")
        assert error.value.code == "CAPABILITY_REQUIRED"


async def test_ai_denied_even_with_explicit_capability(
    provider_service, provider_actor, admin_engine
):
    ai = provider_actor.model_copy(update={"actor_type": ActorType.AI})
    with pytest.raises(DomainError) as error:
        await provider_service.register(command(), ai, "ai")
    assert error.value.code == "CAPABILITY_REQUIRED"
    assert await counts(admin_engine) == (0, 0, 0, 0)


async def test_role_title_alone_does_not_create_provider_authority(admin_engine, provider_actor):
    sessions = make_sessions(admin_engine)
    provision = Provisioning(sessions)
    resolver = AuthorizationResolver(sessions)
    principal = TrustedPrincipal(
        actor_id=f"candidate-role-only-{uuid4()}",
        actor_type=ActorType.HUMAN,
        correlation_id="role-only",
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
        provider_actor,
    )
    try:
        resolved = await resolver.resolve(principal)
        assert "provider_candidate.register" not in resolved.capabilities
        assert "provider_candidate.read" not in resolved.capabilities
    finally:
        await provision.revoke(
            "assignment",
            assignment_id,
            provider_actor,
            "Test cleanup preserves history",
        )


async def test_idempotent_retry_and_payload_conflict(
    provider_service, provider_actor, admin_engine
):
    first = await provider_service.register(command(), provider_actor, "same-key")
    assert await provider_service.register(command(), provider_actor, "same-key") == first

    with pytest.raises(DomainError) as error:
        await provider_service.register(
            command(reason="different reason"), provider_actor, "same-key"
        )
    assert error.value.code == "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"
    assert await counts(admin_engine) == (1, 1, 1, 1)


async def test_registration_race_is_serialized(provider_service, provider_actor, admin_engine):
    results = await asyncio.gather(
        provider_service.register(command(), provider_actor, "race"),
        provider_service.register(command(), provider_actor, "race"),
    )
    assert results[0] == results[1]
    assert await counts(admin_engine) == (1, 1, 1, 1)


async def test_registration_race_with_different_payload_has_one_conflict(
    provider_service, provider_actor, admin_engine
):
    results = await asyncio.gather(
        provider_service.register(command(reason="one"), provider_actor, "race-conflict"),
        provider_service.register(command(reason="two"), provider_actor, "race-conflict"),
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
    assert await counts(admin_engine) == (1, 1, 1, 1)


async def test_atomic_rollback_after_effects_flush(
    provider_service, provider_actor, admin_engine, monkeypatch
):
    original = provider_service.effects.append

    async def fail_after_flush(*args, **kwargs):
        await original(*args, **kwargs)
        raise RuntimeError("injected rollback")

    monkeypatch.setattr(provider_service.effects, "append", fail_after_flush)
    with pytest.raises(RuntimeError):
        await provider_service.register(command(), provider_actor, "rollback")
    assert await counts(admin_engine) == (0, 0, 0, 0)

    monkeypatch.setattr(provider_service.effects, "append", original)
    await provider_service.register(command(), provider_actor, "rollback")
    assert await counts(admin_engine) == (1, 1, 1, 1)


@pytest.mark.parametrize("operation", ["UPDATE", "DELETE"])
async def test_provider_candidate_history_is_immutable(
    provider_service, provider_actor, admin_engine, operation
):
    result = await provider_service.register(command(), provider_actor, "immutable")
    statement = (
        "DELETE FROM provider_candidate_record WHERE id=:id"
        if operation == "DELETE"
        else "UPDATE provider_candidate_record SET display_name='tampered' WHERE id=:id"
    )
    async with admin_engine.begin() as conn:
        with pytest.raises(DBAPIError):
            await conn.execute(text(statement), {"id": UUID(result["id"])})


async def test_direct_insert_without_atomic_effects_fails(admin_engine, provider_actor):
    row = ProviderCandidateRecord(
        id=uuid4(),
        display_name="Unlogged candidate",
        registered_at=datetime.now(UTC),
        registered_by_actor_id=provider_actor.actor_id,
        registered_by_actor_type=provider_actor.actor_type.value,
        reason="must fail",
        correlation_id=provider_actor.correlation_id,
    )
    async with make_sessions(admin_engine)() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                session.add(row)
                await session.flush()
    assert await counts(admin_engine) == (0, 0, 0, 0)


@pytest.mark.parametrize("effect_kind", ["audit", "outbox"])
async def test_nullable_shared_effects_remain_bounded_to_provider_candidate(
    admin_engine, provider_actor, effect_kind
):
    identifier = uuid4()
    now = datetime.now(UTC)
    effect = (
        AuditEntry(
            case_id=None,
            actor_id=provider_actor.actor_id,
            actor_type=provider_actor.actor_type.value,
            action="unrelated.event.v1",
            resource_type="unrelated_resource",
            resource_id=identifier,
            timestamp=now,
            correlation_id=provider_actor.correlation_id,
            before_reference=None,
            after_reference=identifier,
            reason="must remain Case-linked",
        )
        if effect_kind == "audit"
        else OutboxEvent(
            case_id=None,
            event_type="unrelated.event.v1",
            occurred_at=now,
            payload={"id": str(identifier)},
        )
    )
    async with make_sessions(admin_engine)() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                session.add(effect)
                await session.flush()


async def test_read_list_detail_and_pagination(provider_service, provider_actor):
    first = await provider_service.register(command("One"), provider_actor, "one")
    second = await provider_service.register(command("Two"), provider_actor, "two")
    page = await provider_service.list(provider_actor, limit=1)
    assert len(page.items) == 1
    assert page.next_cursor
    next_page = await provider_service.list(provider_actor, cursor=page.next_cursor, limit=1)
    assert len(next_page.items) == 1
    assert {str(page.items[0].id), str(next_page.items[0].id)} == {first["id"], second["id"]}
    assert (await provider_service.get(UUID(first["id"]), provider_actor)).display_name == "One"

    no_read = provider_actor.model_copy(
        update={"capabilities": frozenset({"provider_candidate.register"})}
    )
    with pytest.raises(DomainError) as error:
        await provider_service.list(no_read)
    assert error.value.code == "CAPABILITY_REQUIRED"


async def test_http_anonymous_denial_and_no_operational_routes(provider_actor):
    app = create_app(Settings(database_url=PostgresDsn("postgresql://unused@127.0.0.1:1/unused")))
    candidate_id = uuid4()
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                "/api/v1/provider-candidates",
                json={"display_name": "Candidate", "reason": "foundation"},
                headers={"Idempotency-Key": "key"},
            )
            assert response.status_code == 401
            assert (await client.get("/api/v1/provider-candidates")).status_code == 401
            assert (
                await client.get(f"/api/v1/provider-candidates/{candidate_id}")
            ).status_code == 401

            for action in (
                "activate",
                "approve",
                "reject",
                "suspend",
                "qualify",
                "map-service",
                "select",
                "capacity",
                "contract",
            ):
                assert (
                    await client.post(
                        f"/api/v1/provider-candidates/{candidate_id}/{action}",
                        json={},
                        headers={"Idempotency-Key": "key"},
                    )
                ).status_code == 404
    finally:
        await app.state.engine.dispose()


async def test_http_registration_with_trusted_context(
    provider_service, provider_actor, admin_engine
):
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    app.dependency_overrides[get_actor] = lambda: provider_actor
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            created = await client.post(
                "/api/v1/provider-candidates",
                json={"display_name": "HTTP Candidate", "reason": "foundation"},
                headers={"Idempotency-Key": "http"},
            )
            assert created.status_code == 201, created.text
            candidate_id = created.json()["id"]
            listed = await client.get("/api/v1/provider-candidates")
            assert listed.status_code == 200
            assert listed.json()["items"][0]["id"] == candidate_id
            detail = await client.get(f"/api/v1/provider-candidates/{candidate_id}")
            assert detail.status_code == 200
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()
    assert await counts(admin_engine) == (1, 1, 1, 1)
