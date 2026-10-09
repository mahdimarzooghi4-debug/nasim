"""Human Referral follow-up: descriptive history only, not a lifecycle result."""

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
from nasim.infrastructure.referral_effects import digest
from nasim.infrastructure.referral_follow_up_effects import ReferralFollowUpEffects
from nasim.referral.contracts import RecordReferralFollowUp, ReferralFollowUpView
from nasim.referral.models import ReferralFollowUpRecord, ReferralRecord


class ReferralFollowUps:
    def __init__(
        self,
        sessions: async_sessionmaker[AsyncSession],
        references: CaseReferences | None = None,
        effects: ReferralFollowUpEffects | None = None,
    ) -> None:
        self.sessions = sessions
        self.references = references or CaseReferences()
        self.effects = effects or ReferralFollowUpEffects()

    async def _referral(self, session: AsyncSession, referral_id: UUID) -> ReferralRecord:
        referral = await session.get(ReferralRecord, referral_id)
        if referral is None:
            raise DomainError("REFERRAL_NOT_FOUND", 404)
        return referral

    async def record(
        self, referral_id: UUID, command: RecordReferralFollowUp, actor: ActorContext, key: str
    ) -> dict[str, Any]:
        require_capability(actor, "referral.follow_up.record.assigned")
        if actor.actor_type != ActorType.HUMAN:
            raise DomainError("CAPABILITY_REQUIRED", 403)
        if not key.strip() or len(key) > 200:
            raise DomainError("INVALID_IDEMPOTENCY_KEY", 422)

        scope = self.effects.scope(actor, referral_id, key)
        payload_hash = digest(command.model_dump(mode="json"))
        async with self.sessions() as session, session.begin():
            await self.effects.lock(session, scope)
            referral = await self._referral(session, referral_id)
            assignment = await self.references.lock_assignment(session, referral.case_id)
            require_assigned(
                actor, "referral.follow_up.record.assigned", assignment.caregiver_actor_id
            )
            # Assignment is checked even for idempotent replay.
            if assignment.id != command.expected_current_assignment_id:
                raise DomainError("CASE_ASSIGNMENT_CHANGED", 409)
            prior = await self.effects.prior(session, scope, payload_hash)
            if prior is not None:
                return prior
            now = (await session.execute(select(func.statement_timestamp()))).scalar_one()
            row = ReferralFollowUpRecord(
                id=uuid4(),
                referral_id=referral_id,
                recorded_at=now,
                recorded_by_actor_id=actor.actor_id,
                recorded_by_actor_type=actor.actor_type.value,
                note=command.note,
                reason=command.reason,
                correlation_id=actor.correlation_id,
            )
            session.add(row)
            await session.flush()
            record = ReferralFollowUpView.model_validate(row)
            await self.effects.append(session, referral.case_id, record, actor, scope, payload_hash)
            return record.model_dump(mode="json")

    @staticmethod
    def _require_read(actor: ActorContext) -> None:
        if actor.actor_type == ActorType.AI or not actor.capabilities.intersection(
            {"referral.follow_up.read.assigned", "referral.follow_up.read.oversight"}
        ):
            raise DomainError("CAPABILITY_REQUIRED", 403)

    async def _authorize_read(
        self, session: AsyncSession, case_id: UUID, actor: ActorContext
    ) -> None:
        assignment = await self.references.lock_assignment(session, case_id)
        if "referral.follow_up.read.oversight" not in actor.capabilities:
            require_assigned(
                actor, "referral.follow_up.read.assigned", assignment.caregiver_actor_id
            )

    async def list(
        self,
        referral_id: UUID,
        actor: ActorContext,
        cursor: str | None = None,
        limit: int = 50,
    ) -> Page[ReferralFollowUpView]:
        self._require_read(actor)
        if not 1 <= limit <= 100:
            raise DomainError("INVALID_PAGE_LIMIT", 422)
        async with self.sessions() as session, session.begin():
            referral = await self._referral(session, referral_id)
            await self._authorize_read(session, referral.case_id, actor)
            query = select(ReferralFollowUpRecord).where(
                ReferralFollowUpRecord.referral_id == referral_id
            )
            if cursor:
                stamp, identifier = decode_cursor(cursor)
                query = query.where(
                    tuple_(ReferralFollowUpRecord.recorded_at, ReferralFollowUpRecord.id)
                    > tuple_(literal(stamp), literal(identifier))
                )
            rows = (
                await session.scalars(
                    query.order_by(
                        ReferralFollowUpRecord.recorded_at, ReferralFollowUpRecord.id
                    ).limit(limit + 1)
                )
            ).all()
            selected = rows[:limit]
            return Page[ReferralFollowUpView](
                items=[ReferralFollowUpView.model_validate(row) for row in selected],
                next_cursor=encode_cursor(selected[-1].recorded_at, selected[-1].id)
                if len(rows) > limit
                else None,
            )


    async def list_for_case(
        self, case_id: UUID, actor: ActorContext, cursor: str | None = None, limit: int = 50
    ) -> Page[ReferralFollowUpView]:
        """Authorized descriptive index of already-recorded notes across one Case.

        This does not imply a service status, follow-up cadence, verified outcome
        or frozen cross-context snapshot. The underlying Referral tables remain
        owned by this bounded context.
        """

        self._require_read(actor)
        # All three independent grants are required; role labels cannot widen
        # visibility of sensitive note text through a Case-level index.
        families = (
            ("case.read.assigned", "case.read.oversight"),
            ("referral.read.assigned", "referral.read.oversight"),
            ("referral.follow_up.read.assigned", "referral.follow_up.read.oversight"),
        )
        if any(actor.capabilities.isdisjoint(family) for family in families):
            raise DomainError("CAPABILITY_REQUIRED", 403)
        if not 1 <= limit <= 100:
            raise DomainError("INVALID_PAGE_LIMIT", 422)

        async with self.sessions() as session, session.begin():
            assignment = await self.references.lock_assignment(session, case_id)
            # Every capability family must independently authorize this Case.
            # An oversight grant in one family cannot bypass another family's
            # current-assignment scope.
            for assigned, oversight in families:
                if oversight not in actor.capabilities:
                    require_assigned(actor, assigned, assignment.caregiver_actor_id)
            query = (
                select(ReferralFollowUpRecord)
                .join(ReferralRecord, ReferralFollowUpRecord.referral_id == ReferralRecord.id)
                .where(ReferralRecord.case_id == case_id)
            )
            if cursor:
                stamp, identifier = decode_cursor(cursor)
                query = query.where(
                    tuple_(ReferralFollowUpRecord.recorded_at, ReferralFollowUpRecord.id)
                    > tuple_(literal(stamp), literal(identifier))
                )
            rows = (
                await session.scalars(
                    query.order_by(
                        ReferralFollowUpRecord.recorded_at, ReferralFollowUpRecord.id
                    ).limit(limit + 1)
                )
            ).all()
            selected = rows[:limit]
            return Page[ReferralFollowUpView](
                items=[ReferralFollowUpView.model_validate(row) for row in selected],
                next_cursor=encode_cursor(selected[-1].recorded_at, selected[-1].id)
                if len(rows) > limit
                else None,
            )

    async def get(self, record_id: UUID, actor: ActorContext) -> ReferralFollowUpView:
        self._require_read(actor)
        async with self.sessions() as session, session.begin():
            row = await session.get(ReferralFollowUpRecord, record_id)
            if row is None:
                raise DomainError("REFERRAL_FOLLOW_UP_NOT_FOUND", 404)
            referral = await self._referral(session, row.referral_id)
            await self._authorize_read(session, referral.case_id, actor)
            return ReferralFollowUpView.model_validate(row)
