"""Referral application boundary, consuming TS-03 references and shared effect contracts."""

from typing import Any
from uuid import UUID, uuid4

from sqlalchemy import func, literal, select, tuple_
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from nasim.application.case_references import CaseReferences
from nasim.application.pagination import decode_cursor, encode_cursor
from nasim.domain.contracts import Page
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import (
    ActorContext,
    ActorType,
    require_assigned,
    require_capability,
)
from nasim.infrastructure.referral_effects import ReferralEffects, digest
from nasim.referral.contracts import CreateReferral, ReferralView
from nasim.referral.models import ReferralRecord


class Referrals:
    def __init__(
        self,
        sessions: async_sessionmaker[AsyncSession],
        references: CaseReferences | None = None,
        effects: ReferralEffects | None = None,
    ):
        self.sessions = sessions
        self.references = references or CaseReferences()
        self.effects = effects or ReferralEffects()

    async def create(
        self, case_id: UUID, command: CreateReferral, actor: ActorContext, key: str
    ) -> dict[str, Any]:
        require_capability(actor, "referral.create.assigned")
        if not key.strip() or len(key) > 200:
            raise DomainError("INVALID_IDEMPOTENCY_KEY", 422)
        scope = self.effects.scope(actor, case_id, key)
        payload_hash = digest(command.model_dump(mode="json"))
        async with self.sessions() as session, session.begin():
            await self.effects.lock(session, scope)
            assignment = await self.references.lock_assignment(session, case_id)
            require_assigned(actor, "referral.create.assigned", assignment.caregiver_actor_id)
            prior = await self.effects.prior(session, scope, payload_hash)
            if assignment.id != command.expected_current_assignment_id:
                raise DomainError("CASE_ASSIGNMENT_CHANGED", 409)
            need = await self.references.current_need(
                session, case_id, command.source_need_observation_id
            )
            if prior is not None:
                return prior
            now = (await session.execute(select(func.statement_timestamp()))).scalar_one()
            row = ReferralRecord(
                id=uuid4(),
                case_id=case_id,
                source_need_observation_id=need.id,
                created_at=now,
                created_by_actor_id=actor.actor_id,
                created_by_actor_type=actor.actor_type.value,
                reason=command.reason,
                correlation_id=actor.correlation_id,
            )
            session.add(row)
            await session.flush()
            record = ReferralView.model_validate(row)
            await self.effects.append(session, record, actor, scope, payload_hash)
            return record.model_dump(mode="json")

    @staticmethod
    def _require_read(actor: ActorContext) -> None:
        if actor.actor_type == ActorType.AI or not actor.capabilities.intersection(
            {"referral.read.assigned", "referral.read.oversight"}
        ):
            raise DomainError("CAPABILITY_REQUIRED", 403)

    async def _authorize_read(
        self, session: AsyncSession, case_id: UUID, actor: ActorContext
    ) -> None:
        current = await self.references.lock_assignment(session, case_id)
        if "referral.read.oversight" not in actor.capabilities:
            require_assigned(actor, "referral.read.assigned", current.caregiver_actor_id)

    async def list(
        self, case_id: UUID, actor: ActorContext, cursor: str | None = None, limit: int = 50
    ) -> Page[ReferralView]:
        self._require_read(actor)
        if not 1 <= limit <= 100:
            raise DomainError("INVALID_PAGE_LIMIT", 422)
        async with self.sessions() as session, session.begin():
            await self._authorize_read(session, case_id, actor)
            query = select(ReferralRecord).where(ReferralRecord.case_id == case_id)
            if cursor:
                stamp, identifier = decode_cursor(cursor)
                query = query.where(
                    tuple_(ReferralRecord.created_at, ReferralRecord.id)
                    > tuple_(literal(stamp), literal(identifier))
                )
            rows = (
                await session.scalars(
                    query.order_by(ReferralRecord.created_at, ReferralRecord.id).limit(limit + 1)
                )
            ).all()
            selected = rows[:limit]
            return Page[ReferralView](
                items=[ReferralView.model_validate(r) for r in selected],
                next_cursor=encode_cursor(selected[-1].created_at, selected[-1].id)
                if len(rows) > limit
                else None,
            )

    async def get(self, referral_id: UUID, actor: ActorContext) -> ReferralView:
        self._require_read(actor)
        async with self.sessions() as session, session.begin():
            row = await session.get(ReferralRecord, referral_id)
            if row is None:
                raise DomainError("REFERRAL_NOT_FOUND", 404)
            await self._authorize_read(session, row.case_id, actor)
            return ReferralView.model_validate(row)
