"""Assigned-caregiver routine planning and explicit occurrence recording."""

import hashlib
import json
from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4
from zoneinfo import ZoneInfo

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.orm import aliased

from nasim.application.case_references import CaseReferences
from nasim.care_routines.contracts import (
    CareRoutineEventView,
    CareRoutineView,
    CreateCareRoutine,
    RecordCareRoutineEvent,
)
from nasim.care_routines.models import CareRoutineEventRecord, CareRoutineRecord
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType, require_assigned
from nasim.infrastructure.models import AuditEntry, IdempotencyRecord, OutboxEvent


def _digest(value: dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


class CareRoutines:
    def __init__(
        self,
        sessions: async_sessionmaker[AsyncSession],
        references: CaseReferences | None = None,
    ) -> None:
        self.sessions = sessions
        self.references = references or CaseReferences()

    @staticmethod
    def _human(actor: ActorContext) -> None:
        if actor.actor_type != ActorType.HUMAN:
            raise DomainError("HUMAN_ACTION_REQUIRED", 403)

    @staticmethod
    def _scope(actor: ActorContext, operation: str, target: UUID, key: str) -> dict[str, str]:
        return {
            "actor_id": actor.actor_id,
            "operation": f"{operation}.{actor.actor_type.value}",
            "target": str(target),
            "key": key,
        }

    async def _lock_idempotency(self, session: AsyncSession, scope: dict[str, str]) -> None:
        lock_id = int.from_bytes(bytes.fromhex(_digest(scope))[:8], signed=True)
        await session.execute(text("SELECT pg_advisory_xact_lock(:id)"), {"id": lock_id})

    async def _prior(
        self, session: AsyncSession, scope: dict[str, str], payload_hash: str
    ) -> dict[str, Any] | None:
        row = await session.scalar(select(IdempotencyRecord).filter_by(**scope))
        if row is None:
            return None
        if row.payload_hash != payload_hash:
            raise DomainError("IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD", 409)
        return row.response

    async def _append_effects(
        self,
        session: AsyncSession,
        *,
        case_id: UUID,
        event_type: str,
        resource_type: str,
        resource_id: UUID,
        before_reference: UUID | None,
        occurred_at: datetime,
        actor: ActorContext,
        scope: dict[str, str],
        payload_hash: str,
        response: dict[str, Any],
    ) -> None:
        session.add(
            AuditEntry(
                case_id=case_id,
                actor_id=actor.actor_id,
                actor_type=actor.actor_type.value,
                action=event_type,
                resource_type=resource_type,
                resource_id=resource_id,
                timestamp=occurred_at,
                correlation_id=actor.correlation_id,
                before_reference=before_reference,
                after_reference=resource_id,
                reason="Daily care routine record",
            )
        )
        # Keep routine titles, schedules and completion details out of the shared outbox.
        session.add(
            OutboxEvent(
                case_id=case_id,
                event_type=event_type,
                occurred_at=occurred_at,
                payload={
                    "case_id": str(case_id),
                    "resource_id": str(resource_id),
                    "actor_id": actor.actor_id,
                    "actor_type": actor.actor_type.value,
                    "recorded_at": occurred_at.isoformat(),
                    "correlation_id": actor.correlation_id,
                },
            )
        )
        session.add(
            IdempotencyRecord(
                **scope,
                payload_hash=payload_hash,
                response=response,
                created_at=occurred_at,
            )
        )
        await session.flush()

    @staticmethod
    def _check_key(key: str) -> None:
        if not key.strip() or len(key) > 200:
            raise DomainError("INVALID_IDEMPOTENCY_KEY", 422)

    async def list(self, case_id: UUID, actor: ActorContext, limit: int = 50) -> list[CareRoutineView]:
        self._human(actor)
        async with self.sessions() as session, session.begin():
            assignment = await self.references.lock_assignment(session, case_id)
            require_assigned(actor, "care_routine.read.assigned", assignment.caregiver_actor_id)
            successor = aliased(CareRoutineRecord)
            rows = await session.scalars(
                select(CareRoutineRecord)
                .where(CareRoutineRecord.case_id == case_id, CareRoutineRecord.active.is_(True))
                .where(
                    ~select(successor.id)
                    .where(successor.supersedes_routine_id == CareRoutineRecord.id)
                    .exists()
                )
                .order_by(CareRoutineRecord.recorded_at, CareRoutineRecord.id)
                .limit(limit)
            )
            return [CareRoutineView.model_validate(row) for row in rows]

    async def create(
        self,
        case_id: UUID,
        command: CreateCareRoutine,
        actor: ActorContext,
        key: str,
    ) -> dict[str, Any]:
        self._human(actor)
        self._check_key(key)
        scope = self._scope(actor, "care_routine.create", case_id, key)
        payload_hash = _digest(command.model_dump(mode="json"))
        async with self.sessions() as session, session.begin():
            await self._lock_idempotency(session, scope)
            prior = await self._prior(session, scope, payload_hash)
            if prior is not None:
                return prior
            assignment = await self.references.lock_assignment(session, case_id)
            require_assigned(actor, "care_routine.manage.assigned", assignment.caregiver_actor_id)
            if assignment.id != command.expected_current_assignment_id:
                raise DomainError("CASE_ASSIGNMENT_CHANGED", 409)
            if command.supersedes_routine_id is not None:
                previous = await session.scalar(
                    select(CareRoutineRecord)
                    .where(
                        CareRoutineRecord.case_id == case_id,
                        CareRoutineRecord.id == command.supersedes_routine_id,
                    )
                    .with_for_update()
                )
                if previous is None:
                    raise DomainError("CARE_ROUTINE_NOT_FOUND", 404)
                if previous.routine_type != command.routine_type:
                    raise DomainError("CARE_ROUTINE_TYPE_IMMUTABLE", 409)
                successor = await session.scalar(
                    select(CareRoutineRecord.id).where(
                        CareRoutineRecord.supersedes_routine_id == previous.id
                    )
                )
                if successor is not None:
                    raise DomainError("STALE_RECORD_REVISION", 409)
            now = datetime.now(UTC)
            record = CareRoutineRecord(
                id=uuid4(),
                case_id=case_id,
                routine_type=command.routine_type,
                title=command.title,
                schedule=command.schedule.model_dump(mode="json"),
                active=command.active,
                supersedes_routine_id=command.supersedes_routine_id,
                recorded_at=now,
                recorded_by_actor_id=actor.actor_id,
                recorded_by_actor_type=actor.actor_type.value,
                correlation_id=actor.correlation_id,
            )
            response = CareRoutineView.model_validate(record).model_dump(mode="json")
            session.add(record)
            await self._append_effects(
                session,
                case_id=case_id,
                event_type="care_routine.plan_recorded.v1",
                resource_type="care_routine_record",
                resource_id=record.id,
                before_reference=command.supersedes_routine_id,
                occurred_at=now,
                actor=actor,
                scope=scope,
                payload_hash=payload_hash,
                response=response,
            )
            return response

    async def record_event(
        self,
        case_id: UUID,
        routine_id: UUID,
        command: RecordCareRoutineEvent,
        actor: ActorContext,
        key: str,
    ) -> dict[str, Any]:
        self._human(actor)
        self._check_key(key)
        scope = self._scope(actor, "care_routine.event", routine_id, key)
        payload_hash = _digest(command.model_dump(mode="json"))
        async with self.sessions() as session, session.begin():
            await self._lock_idempotency(session, scope)
            prior = await self._prior(session, scope, payload_hash)
            if prior is not None:
                return prior
            assignment = await self.references.lock_assignment(session, case_id)
            require_assigned(
                actor, "care_routine.event.record.assigned", assignment.caregiver_actor_id
            )
            if assignment.id != command.expected_current_assignment_id:
                raise DomainError("CASE_ASSIGNMENT_CHANGED", 409)
            routine = await session.scalar(
                select(CareRoutineRecord)
                .where(CareRoutineRecord.case_id == case_id, CareRoutineRecord.id == routine_id)
                .with_for_update()
            )
            if routine is None:
                raise DomainError("CARE_ROUTINE_NOT_FOUND", 404)
            successor = await session.scalar(
                select(CareRoutineRecord.id).where(
                    CareRoutineRecord.supersedes_routine_id == routine.id
                )
            )
            if successor is not None:
                raise DomainError("STALE_RECORD_REVISION", 409)
            if not routine.active:
                raise DomainError("CARE_ROUTINE_INACTIVE", 409)
            schedule = routine.schedule
            local_date = command.occurred_at.astimezone(ZoneInfo(schedule["timezone"])).date()
            if local_date != command.occurrence_date:
                raise DomainError("CARE_ROUTINE_OCCURRENCE_DATE_MISMATCH", 422)
            if (
                schedule["cadence"] == "WEEKLY"
                and command.occurrence_date.weekday() not in schedule["weekdays"]
            ):
                raise DomainError("CARE_ROUTINE_DATE_NOT_SCHEDULED", 422)
            existing = await session.scalar(
                select(CareRoutineEventRecord.id).where(
                    CareRoutineEventRecord.routine_id == routine_id,
                    CareRoutineEventRecord.occurrence_date == command.occurrence_date,
                )
            )
            if existing is not None:
                raise DomainError("CARE_ROUTINE_OCCURRENCE_ALREADY_RECORDED", 409)
            now = datetime.now(UTC)
            record = CareRoutineEventRecord(
                id=uuid4(),
                case_id=case_id,
                routine_id=routine_id,
                occurrence_date=command.occurrence_date,
                status=command.status,
                occurred_at=command.occurred_at,
                recorded_at=now,
                recorded_by_actor_id=actor.actor_id,
                recorded_by_actor_type=actor.actor_type.value,
                correlation_id=actor.correlation_id,
            )
            response = CareRoutineEventView.model_validate(record).model_dump(mode="json")
            session.add(record)
            await self._append_effects(
                session,
                case_id=case_id,
                event_type="care_routine.event_recorded.v1",
                resource_type="care_routine_event_record",
                resource_id=record.id,
                before_reference=routine.id,
                occurred_at=now,
                actor=actor,
                scope=scope,
                payload_hash=payload_hash,
                response=response,
            )
            return response

    async def list_events(
        self, case_id: UUID, routine_id: UUID, actor: ActorContext, limit: int = 100
    ) -> list[CareRoutineEventView]:
        self._human(actor)
        async with self.sessions() as session, session.begin():
            assignment = await self.references.lock_assignment(session, case_id)
            require_assigned(actor, "care_routine.event.read.assigned", assignment.caregiver_actor_id)
            exists = await session.scalar(
                select(CareRoutineRecord.id).where(
                    CareRoutineRecord.case_id == case_id,
                    CareRoutineRecord.id == routine_id,
                )
            )
            if exists is None:
                raise DomainError("CARE_ROUTINE_NOT_FOUND", 404)
            rows = await session.scalars(
                select(CareRoutineEventRecord)
                .where(
                    CareRoutineEventRecord.case_id == case_id,
                    CareRoutineEventRecord.routine_id == routine_id,
                )
                .order_by(CareRoutineEventRecord.occurrence_date.desc())
                .limit(limit)
            )
            return [CareRoutineEventView.model_validate(row) for row in rows]
