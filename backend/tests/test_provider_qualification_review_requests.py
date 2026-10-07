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
    ProviderQualificationReviewRequests,
)


@pytest.fixture
def review_actor() -> ActorContext:
    return ActorContext(
        actor_id="qualification-review-requester",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset(
            {
                "provider_qualification_review.request",
                "provider_qualification_review.read",
            }
        ),
        correlation_id="qualification-review-test",
    )


@pytest.fixture
def candidate_actor() -> ActorContext:
    return ActorContext(
        actor_id="candidate-registrar-for-review-tests",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset({"provider_candidate.register", "provider_candidate.read"}),
        correlation_id="qualification-review-candidate-setup",
    )


@pytest.fixture
async def review_service(admin_engine):
    url = os.environ.get("NASIM_TEST_APP_DATABASE_URL") or os.environ["NASIM_TEST_DATABASE_URL"]
    engine = make_engine(Settings(database_url=PostgresDsn(url)))
    yield ProviderQualificationReviewRequests(make_sessions(engine))
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
            display_name="Review Candidate",
            reason="Qualification review request test setup",
        ),
        candidate_actor,
        f"candidate-{uuid4()}",
    )
    return UUID(result["id"])


def command(
    reason: str = "Request human qualification review",
) -> RequestProviderQualificationReview:
    return RequestProviderQualificationReview(reason=reason)


async def review_counts(admin_engine) -> tuple[int, int, int, int]:
    async with admin_engine.connect() as conn:
        return (
            await conn.scalar(
                select(func.count()).select_from(ProviderQualificationReviewRequestRecord)
            ),
            await conn.scalar(
                select(func.count())
                .select_from(AuditEntry)
                .where(AuditEntry.action == "provider.qualification_review_requested.v1")
            ),
            await conn.scalar(
                select(func.count())
                .select_from(OutboxEvent)
                .where(OutboxEvent.event_type == "provider.qualification_review_requested.v1")
            ),
            await conn.scalar(
                select(func.count())
                .select_from(IdempotencyRecord)
                .where(IdempotencyRecord.operation.like("provider.qualification_review.request.%"))
            ),
        )


async def test_request_review_foundation_only(
    review_service, review_actor, candidate_id, admin_engine
):
    async with admin_engine.connect() as conn:
        before_candidate = (
            await conn.execute(
                select(
                    ProviderCandidateRecord.id,
                    ProviderCandidateRecord.display_name,
                    ProviderCandidateRecord.registered_at,
                ).where(ProviderCandidateRecord.id == candidate_id)
            )
        ).one()
        evidence_before = await conn.scalar(
            select(func.count()).select_from(ProviderQualificationEvidenceRecord)
        )

    result = await review_service.request(candidate_id, command(), review_actor, "request-1")

    assert result["provider_candidate_id"] == str(candidate_id)
    assert result["requested_by_actor_id"] == review_actor.actor_id
    assert result["requested_by_actor_type"] == "HUMAN"
    assert await review_counts(admin_engine) == (1, 1, 1, 1)

    async with admin_engine.connect() as conn:
        payload = await conn.scalar(
            select(OutboxEvent.payload).where(
                OutboxEvent.event_type == "provider.qualification_review_requested.v1"
            )
        )
        audit_case = await conn.scalar(
            select(AuditEntry.case_id).where(
                AuditEntry.action == "provider.qualification_review_requested.v1"
            )
        )
        outbox_case = await conn.scalar(
            select(OutboxEvent.case_id).where(
                OutboxEvent.event_type == "provider.qualification_review_requested.v1"
            )
        )
        after_candidate = (
            await conn.execute(
                select(
                    ProviderCandidateRecord.id,
                    ProviderCandidateRecord.display_name,
                    ProviderCandidateRecord.registered_at,
                ).where(ProviderCandidateRecord.id == candidate_id)
            )
        ).one()
        evidence_after = await conn.scalar(
            select(func.count()).select_from(ProviderQualificationEvidenceRecord)
        )

    assert payload["provider_qualification_review_request_id"] == result["id"]
    assert payload["provider_candidate_id"] == str(candidate_id)
    assert "reason" not in payload
    assert audit_case is None
    assert outbox_case is None
    assert before_candidate == after_candidate
    assert evidence_before == evidence_after == 0


@pytest.mark.parametrize(
    "field",
    [
        "status",
        "state",
        "reviewer",
        "approver",
        "assigned_to",
        "decision",
        "result",
        "qualified",
        "approved",
        "active",
        "score",
        "threshold",
        "evidence_complete",
        "evidence_sufficient",
        "sla",
        "due_at",
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
def test_contract_rejects_review_decision_fields(field):
    with pytest.raises(ValidationError):
        RequestProviderQualificationReview(
            reason="foundation",
            **{field: "invented"},
        )


@pytest.mark.parametrize("value", ["", " ", "\n"])
def test_review_reason_is_nonblank(value):
    with pytest.raises(ValidationError):
        RequestProviderQualificationReview(reason=value)


async def test_repeated_review_requests_are_allowed(
    review_service, review_actor, candidate_id, admin_engine
):
    first = await review_service.request(candidate_id, command("first"), review_actor, "one")
    second = await review_service.request(candidate_id, command("second"), review_actor, "two")
    assert first["id"] != second["id"]
    assert await review_counts(admin_engine) == (2, 2, 2, 2)


async def test_missing_candidate_fails_without_side_effects(
    review_service, review_actor, admin_engine
):
    with pytest.raises(DomainError) as error:
        await review_service.request(uuid4(), command(), review_actor, "missing-candidate")
    assert error.value.code == "PROVIDER_CANDIDATE_NOT_FOUND"
    assert await review_counts(admin_engine) == (0, 0, 0, 0)


async def test_missing_capability_and_actor_type_alone_deny(
    review_service, review_actor, candidate_id
):
    for actor_type in ActorType:
        actor = review_actor.model_copy(
            update={"actor_type": actor_type, "capabilities": frozenset()}
        )
        with pytest.raises(DomainError) as error:
            await review_service.request(
                candidate_id,
                command(),
                actor,
                f"missing-{actor_type.value}",
            )
        assert error.value.code == "CAPABILITY_REQUIRED"


async def test_ai_denied_even_with_explicit_capability(
    review_service, review_actor, candidate_id, admin_engine
):
    ai = review_actor.model_copy(update={"actor_type": ActorType.AI})
    with pytest.raises(DomainError) as error:
        await review_service.request(candidate_id, command(), ai, "ai")
    assert error.value.code == "CAPABILITY_REQUIRED"
    assert await review_counts(admin_engine) == (0, 0, 0, 0)


async def test_role_title_alone_does_not_create_review_authority(admin_engine, review_actor):
    sessions = make_sessions(admin_engine)
    provision = Provisioning(sessions)
    resolver = AuthorizationResolver(sessions)
    principal = TrustedPrincipal(
        actor_id=f"review-role-only-{uuid4()}",
        actor_type=ActorType.HUMAN,
        correlation_id="review-role-only",
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
        review_actor,
    )
    try:
        resolved = await resolver.resolve(principal)
        assert "provider_qualification_review.request" not in resolved.capabilities
        assert "provider_qualification_review.read" not in resolved.capabilities
    finally:
        await provision.revoke(
            "assignment",
            assignment_id,
            review_actor,
            "Test cleanup preserves history",
        )


async def test_idempotent_retry_and_payload_conflict(
    review_service, review_actor, candidate_id, admin_engine
):
    first = await review_service.request(candidate_id, command(), review_actor, "same-key")
    assert await review_service.request(candidate_id, command(), review_actor, "same-key") == first

    with pytest.raises(DomainError) as error:
        await review_service.request(
            candidate_id,
            command("different reason"),
            review_actor,
            "same-key",
        )
    assert error.value.code == "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"
    assert await review_counts(admin_engine) == (1, 1, 1, 1)


async def test_same_key_is_scoped_to_candidate(
    review_service,
    review_actor,
    candidate_service,
    candidate_actor,
    candidate_id,
    admin_engine,
):
    second = await candidate_service.register(
        RegisterProviderCandidate(
            display_name="Second Review Candidate",
            reason="Scope isolation",
        ),
        candidate_actor,
        "candidate-two",
    )
    first_result = await review_service.request(
        candidate_id, command(), review_actor, "candidate-scoped"
    )
    second_result = await review_service.request(
        UUID(second["id"]), command(), review_actor, "candidate-scoped"
    )
    assert first_result["id"] != second_result["id"]
    assert await review_counts(admin_engine) == (2, 2, 2, 2)


async def test_review_request_race_is_serialized(
    review_service, review_actor, candidate_id, admin_engine
):
    results = await asyncio.gather(
        review_service.request(candidate_id, command(), review_actor, "race"),
        review_service.request(candidate_id, command(), review_actor, "race"),
    )
    assert results[0] == results[1]
    assert await review_counts(admin_engine) == (1, 1, 1, 1)


async def test_review_request_race_with_different_payload_has_one_conflict(
    review_service, review_actor, candidate_id, admin_engine
):
    results = await asyncio.gather(
        review_service.request(candidate_id, command("one"), review_actor, "race-conflict"),
        review_service.request(candidate_id, command("two"), review_actor, "race-conflict"),
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
    assert await review_counts(admin_engine) == (1, 1, 1, 1)


async def test_atomic_rollback_after_effects_flush(
    review_service,
    review_actor,
    candidate_id,
    admin_engine,
    monkeypatch,
):
    original = review_service.effects.append

    async def fail_after_flush(*args, **kwargs):
        await original(*args, **kwargs)
        raise RuntimeError("injected rollback")

    monkeypatch.setattr(review_service.effects, "append", fail_after_flush)
    with pytest.raises(RuntimeError):
        await review_service.request(candidate_id, command(), review_actor, "rollback")
    assert await review_counts(admin_engine) == (0, 0, 0, 0)

    monkeypatch.setattr(review_service.effects, "append", original)
    await review_service.request(candidate_id, command(), review_actor, "rollback")
    assert await review_counts(admin_engine) == (1, 1, 1, 1)


@pytest.mark.parametrize("operation", ["UPDATE", "DELETE"])
async def test_review_request_history_is_immutable(
    review_service, review_actor, candidate_id, admin_engine, operation
):
    result = await review_service.request(candidate_id, command(), review_actor, "immutable")
    statement = (
        "DELETE FROM provider_qualification_review_request_record WHERE id=:id"
        if operation == "DELETE"
        else (
            "UPDATE provider_qualification_review_request_record "
            "SET reason='tampered' WHERE id=:id"
        )
    )
    async with admin_engine.begin() as conn:
        with pytest.raises(DBAPIError):
            await conn.execute(text(statement), {"id": UUID(result["id"])})


async def test_direct_insert_without_atomic_effects_fails(
    admin_engine, review_actor, candidate_id
):
    row = ProviderQualificationReviewRequestRecord(
        id=uuid4(),
        provider_candidate_id=candidate_id,
        requested_at=datetime.now(UTC),
        requested_by_actor_id=review_actor.actor_id,
        requested_by_actor_type=review_actor.actor_type.value,
        reason="must fail",
        correlation_id=review_actor.correlation_id,
    )
    async with make_sessions(admin_engine)() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                session.add(row)
                await session.flush()
    assert await review_counts(admin_engine) == (0, 0, 0, 0)


async def test_read_list_detail_and_pagination(
    review_service, review_actor, candidate_id
):
    first = await review_service.request(candidate_id, command("One"), review_actor, "one")
    second = await review_service.request(candidate_id, command("Two"), review_actor, "two")
    page = await review_service.list(candidate_id, review_actor, limit=1)
    assert len(page.items) == 1
    assert page.next_cursor
    next_page = await review_service.list(
        candidate_id,
        review_actor,
        cursor=page.next_cursor,
        limit=1,
    )
    assert len(next_page.items) == 1
    assert {str(page.items[0].id), str(next_page.items[0].id)} == {
        first["id"],
        second["id"],
    }
    assert (
        await review_service.get(UUID(first["id"]), review_actor)
    ).reason == "One"

    no_read = review_actor.model_copy(
        update={"capabilities": frozenset({"provider_qualification_review.request"})}
    )
    with pytest.raises(DomainError) as error:
        await review_service.list(candidate_id, no_read)
    assert error.value.code == "CAPABILITY_REQUIRED"


async def test_http_anonymous_denial_and_no_review_decision_routes():
    app = create_app(
        Settings(database_url=PostgresDsn("postgresql://unused@127.0.0.1:1/unused"))
    )
    candidate_id = uuid4()
    request_id = uuid4()
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.post(
                f"/api/v1/provider-candidates/{candidate_id}/qualification-review-requests",
                json={"reason": "foundation"},
                headers={"Idempotency-Key": "key"},
            )
            assert response.status_code == 401
            assert (
                await client.get(
                    f"/api/v1/provider-candidates/{candidate_id}/qualification-review-requests"
                )
            ).status_code == 401
            assert (
                await client.get(
                    f"/api/v1/provider-qualification-review-requests/{request_id}"
                )
            ).status_code == 401

            for action in (
                "assign",
                "review",
                "decide",
                "qualify",
                "approve",
                "reject",
                "activate",
                "close",
                "reopen",
            ):
                assert (
                    await client.post(
                        f"/api/v1/provider-qualification-review-requests/{request_id}/{action}",
                        json={},
                        headers={"Idempotency-Key": "key"},
                    )
                ).status_code == 404
    finally:
        await app.state.engine.dispose()


async def test_http_request_with_trusted_context(
    review_actor, candidate_service, candidate_actor, admin_engine
):
    candidate = await candidate_service.register(
        RegisterProviderCandidate(
            display_name="HTTP Review Candidate",
            reason="HTTP review request setup",
        ),
        candidate_actor,
        "http-candidate",
    )
    candidate_id = UUID(candidate["id"])
    app = create_app(
        Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"]))
    )
    app.dependency_overrides[get_actor] = lambda: review_actor
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            created = await client.post(
                f"/api/v1/provider-candidates/{candidate_id}/qualification-review-requests",
                json={"reason": "request human review"},
                headers={"Idempotency-Key": "http-review"},
            )
            assert created.status_code == 201, created.text
            request_id = created.json()["id"]

            listed = await client.get(
                f"/api/v1/provider-candidates/{candidate_id}/qualification-review-requests"
            )
            assert listed.status_code == 200
            assert listed.json()["items"][0]["id"] == request_id

            detail = await client.get(
                f"/api/v1/provider-qualification-review-requests/{request_id}"
            )
            assert detail.status_code == 200
            assert detail.json()["provider_candidate_id"] == str(candidate_id)
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()

    assert await review_counts(admin_engine) == (1, 1, 1, 1)
