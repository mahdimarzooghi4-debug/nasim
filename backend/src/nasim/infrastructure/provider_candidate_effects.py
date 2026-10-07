"""Atomic technical effects for Provider Candidate registration."""

import hashlib
import json
from typing import Any

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent
from nasim.provider_registry.contracts import ProviderCandidateView


def digest(payload: dict[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


class ProviderCandidateEffects:
    TARGET = "provider-candidate"

    @classmethod
    def scope(cls, actor: ActorContext, key: str) -> dict[str, str]:
        return {
            "actor_id": actor.actor_id,
            "operation": f"provider.candidate.register.{actor.actor_type.value}",
            "target": cls.TARGET,
            "key": key,
        }

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
        record: ProviderCandidateView,
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
                action="provider.candidate_registered.v1",
                resource_type="provider_candidate_record",
                resource_id=record.id,
                timestamp=record.registered_at,
                correlation_id=actor.correlation_id,
                before_reference=None,
                after_reference=record.id,
                reason=record.reason,
            )
        )
        session.add(
            OutboxEvent(
                case_id=None,
                event_type="provider.candidate_registered.v1",
                occurred_at=record.registered_at,
                payload={
                    "provider_candidate_id": str(record.id),
                    "actor_id": actor.actor_id,
                    "actor_type": actor.actor_type.value,
                    "registered_at": record.registered_at.isoformat(),
                    "correlation_id": actor.correlation_id,
                },
            )
        )
        session.add(
            IdempotencyRecord(
                **scope,
                payload_hash=payload_hash,
                response=response,
                created_at=record.registered_at,
            )
        )
        await session.flush()
