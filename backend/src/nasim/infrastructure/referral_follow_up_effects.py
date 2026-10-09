"""Atomic audit/outbox/idempotency for Referral follow-up recording."""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from nasim.identity_context.contracts import ActorContext
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent
from nasim.infrastructure.referral_effects import ReferralEffects
from nasim.referral.contracts import ReferralFollowUpView


class ReferralFollowUpEffects(ReferralEffects):
    @staticmethod
    def scope(actor: ActorContext, referral_id: UUID, key: str) -> dict[str, str]:
        return {
            "actor_id": actor.actor_id,
            "operation": f"referral.follow_up.record.{actor.actor_type.value}",
            "target": str(referral_id),
            "key": key,
        }

    async def append(
        self,
        session: AsyncSession,
        case_id: UUID,
        record: ReferralFollowUpView,
        actor: ActorContext,
        scope: dict[str, str],
        payload_hash: str,
    ) -> None:
        session.add(
            AuditEntry(
                case_id=case_id,
                actor_id=actor.actor_id,
                actor_type=actor.actor_type.value,
                action="referral.follow_up_recorded.v1",
                resource_type="referral_follow_up_record",
                resource_id=record.id,
                timestamp=record.recorded_at,
                correlation_id=actor.correlation_id,
                before_reference=record.referral_id,
                after_reference=record.id,
                reason=record.reason,
            )
        )
        # Neither note nor reason enters the event payload or any AI Dataset.
        session.add(
            OutboxEvent(
                case_id=case_id,
                event_type="referral.follow_up_recorded.v1",
                occurred_at=record.recorded_at,
                payload={
                    "follow_up_record_id": str(record.id),
                    "referral_id": str(record.referral_id),
                    "case_id": str(case_id),
                    "actor_id": actor.actor_id,
                    "actor_type": actor.actor_type.value,
                    "recorded_at": record.recorded_at.isoformat(),
                    "correlation_id": actor.correlation_id,
                },
            )
        )
        session.add(
            IdempotencyRecord(
                **scope,
                payload_hash=payload_hash,
                response=record.model_dump(mode="json"),
                created_at=record.recorded_at,
            )
        )
        await session.flush()
