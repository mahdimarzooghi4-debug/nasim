"""Shared technical audit/outbox/idempotency persistence in the caller's transaction."""

import hashlib
import json
from typing import Any
from uuid import UUID

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent
from nasim.referral.contracts import ReferralView


def digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


class ReferralEffects:
    @staticmethod
    def scope(actor: ActorContext, case_id: UUID, key: str) -> dict[str, str]:
        # ActorType is part of trusted identity in TS-05; avoid cross-type retry collisions.
        return dict(
            actor_id=actor.actor_id,
            operation=f"referral.record.{actor.actor_type.value}",
            target=str(case_id),
            key=key,
        )

    async def lock(self, session: AsyncSession, scope: dict[str, str]) -> None:
        lock_id = int.from_bytes(bytes.fromhex(digest(scope))[:8], signed=True)
        await session.execute(text("SELECT pg_advisory_xact_lock(:id)"), {"id": lock_id})

    async def prior(
        self, session: AsyncSession, scope: dict[str, str], payload_hash: str
    ) -> dict[str, Any] | None:
        row = await session.scalar(select(IdempotencyRecord).filter_by(**scope))
        if row is None:
            return None
        if row.payload_hash != payload_hash:
            raise DomainError("IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD", 409)
        return row.response

    async def append(
        self,
        session: AsyncSession,
        record: ReferralView,
        actor: ActorContext,
        scope: dict[str, str],
        payload_hash: str,
    ) -> None:
        response = record.model_dump(mode="json")
        session.add(
            AuditEntry(
                case_id=record.case_id,
                actor_id=actor.actor_id,
                actor_type=actor.actor_type.value,
                action="referral.recorded.v1",
                resource_type="referral_record",
                resource_id=record.id,
                timestamp=record.created_at,
                correlation_id=actor.correlation_id,
                before_reference=record.source_need_observation_id,
                after_reference=record.id,
                reason=record.reason,
            )
        )
        session.add(
            OutboxEvent(
                case_id=record.case_id,
                event_type="referral.recorded.v1",
                occurred_at=record.created_at,
                payload={
                    "referral_id": str(record.id),
                    "case_id": str(record.case_id),
                    "source_need_observation_id": str(record.source_need_observation_id),
                    "actor_id": actor.actor_id,
                    "actor_type": actor.actor_type.value,
                    "recorded_at": record.created_at.isoformat(),
                    "correlation_id": actor.correlation_id,
                },
            )
        )
        session.add(
            IdempotencyRecord(
                **scope, payload_hash=payload_hash, response=response, created_at=record.created_at
            )
        )
        await session.flush()
