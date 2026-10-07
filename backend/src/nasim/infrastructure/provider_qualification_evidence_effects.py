"""Atomic technical effects for Provider Qualification Evidence recording."""

import hashlib
import json
from typing import Any
from uuid import UUID

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent
from nasim.provider_registry.contracts import ProviderQualificationEvidenceView


def evidence_digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


class ProviderQualificationEvidenceEffects:
    @staticmethod
    def scope(actor: ActorContext, candidate_id: UUID, key: str) -> dict[str, str]:
        return {
            "actor_id": actor.actor_id,
            "operation": f"provider.qualification_evidence.record.{actor.actor_type.value}",
            "target": str(candidate_id),
            "key": key,
        }

    async def lock(self, session: AsyncSession, scope: dict[str, str]) -> None:
        lock_id = int.from_bytes(bytes.fromhex(evidence_digest(scope))[:8], signed=True)
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
        record: ProviderQualificationEvidenceView,
        actor: ActorContext,
        scope: dict[str, str],
        payload_hash: str,
    ) -> None:
        response = record.model_dump(mode="json")
        session.add(
            AuditEntry(
                case_id=None,
                actor_id=actor.actor_id,
                actor_type=actor.actor_type.value,
                action="provider.qualification_evidence_recorded.v1",
                resource_type="provider_qualification_evidence_record",
                resource_id=record.id,
                timestamp=record.recorded_at,
                correlation_id=actor.correlation_id,
                before_reference=None,
                after_reference=record.id,
                reason=record.reason,
            )
        )
        session.add(
            OutboxEvent(
                case_id=None,
                event_type="provider.qualification_evidence_recorded.v1",
                occurred_at=record.recorded_at,
                payload={
                    "provider_qualification_evidence_id": str(record.id),
                    "provider_candidate_id": str(record.provider_candidate_id),
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
                response=response,
                created_at=record.recorded_at,
            )
        )
        await session.flush()
