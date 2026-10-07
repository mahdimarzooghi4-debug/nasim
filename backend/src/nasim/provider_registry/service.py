"""Provider Candidate registration/read application boundary."""

from typing import Any
from uuid import UUID, uuid4

from sqlalchemy import func, literal, select, tuple_
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from nasim.application.pagination import decode_cursor, encode_cursor
from nasim.domain.contracts import Page
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType, require_capability
from nasim.infrastructure.provider_candidate_effects import ProviderCandidateEffects, digest
from nasim.provider_registry.contracts import RegisterProviderCandidate, ProviderCandidateView
from nasim.provider_registry.models import ProviderCandidateRecord


class ProviderCandidates:
    def __init__(
        self,
        sessions: async_sessionmaker[AsyncSession],
        effects: ProviderCandidateEffects | None = None,
    ) -> None:
        self.sessions = sessions
        self.effects = effects or ProviderCandidateEffects()

    async def register(
        self,
        command: RegisterProviderCandidate,
        actor: ActorContext,
        key: str,
    ) -> dict[str, Any]:
        require_capability(actor, "provider_candidate.register")
        if actor.actor_type == ActorType.AI:
            raise DomainError("CAPABILITY_REQUIRED", 403)
        if not key.strip() or len(key) > 200:
            raise DomainError("INVALID_IDEMPOTENCY_KEY", 422)

        scope = self.effects.scope(actor, key)
        payload_hash = digest(command.model_dump(mode="json"))
        async with self.sessions() as session, session.begin():
            await self.effects.lock(session, scope)
            prior = await self.effects.prior(session, scope, payload_hash)
            if prior is not None:
                return prior

            now = (await session.execute(select(func.statement_timestamp()))).scalar_one()
            row = ProviderCandidateRecord(
                id=uuid4(),
                display_name=command.display_name,
                registered_at=now,
                registered_by_actor_id=actor.actor_id,
                registered_by_actor_type=actor.actor_type.value,
                reason=command.reason,
                correlation_id=actor.correlation_id,
            )
            session.add(row)
            await session.flush()
            record = ProviderCandidateView.model_validate(row)
            await self.effects.append(session, record, actor, scope, payload_hash)
            return record.model_dump(mode="json")

    @staticmethod
    def _require_read(actor: ActorContext) -> None:
        require_capability(actor, "provider_candidate.read")

    async def list(
        self,
        actor: ActorContext,
        cursor: str | None = None,
        limit: int = 50,
    ) -> Page[ProviderCandidateView]:
        self._require_read(actor)
        if not 1 <= limit <= 100:
            raise DomainError("INVALID_PAGE_LIMIT", 422)
        async with self.sessions() as session:
            query = select(ProviderCandidateRecord)
            if cursor:
                stamp, identifier = decode_cursor(cursor)
                query = query.where(
                    tuple_(ProviderCandidateRecord.registered_at, ProviderCandidateRecord.id)
                    > tuple_(literal(stamp), literal(identifier))
                )
            rows = (
                await session.scalars(
                    query.order_by(
                        ProviderCandidateRecord.registered_at, ProviderCandidateRecord.id
                    ).limit(limit + 1)
                )
            ).all()
            selected = rows[:limit]
            return Page[ProviderCandidateView](
                items=[ProviderCandidateView.model_validate(row) for row in selected],
                next_cursor=encode_cursor(selected[-1].registered_at, selected[-1].id)
                if len(rows) > limit
                else None,
            )

    async def get(self, candidate_id: UUID, actor: ActorContext) -> ProviderCandidateView:
        self._require_read(actor)
        async with self.sessions() as session:
            row = await session.get(ProviderCandidateRecord, candidate_id)
            if row is None:
                raise DomainError("PROVIDER_CANDIDATE_NOT_FOUND", 404)
            return ProviderCandidateView.model_validate(row)
