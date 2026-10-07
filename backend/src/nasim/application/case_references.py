"""Public transaction-scoped TS-03 reference boundary for other bounded contexts.

Owns Case/Observation lookup semantics. Consumers receive identifiers, not persistence
objects or Need content. The caller's unit of work holds the shared Case lock.
"""

from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from nasim.domain.errors import DomainError
from nasim.infrastructure.models import Assignment, ElderCase, Observation


@dataclass(frozen=True)
class CurrentAssignmentReference:
    id: UUID
    caregiver_actor_id: str


@dataclass(frozen=True)
class NeedReference:
    id: UUID
    case_id: UUID


class CaseReferences:
    async def lock_assignment(
        self, session: AsyncSession, case_id: UUID
    ) -> CurrentAssignmentReference:
        case_id_found = await session.scalar(
            select(ElderCase.id).where(ElderCase.id == case_id).with_for_update()
        )
        if case_id_found is None:
            raise DomainError("CASE_NOT_FOUND", 404)
        row = await session.scalar(
            select(Assignment).where(Assignment.case_id == case_id, Assignment.ended_at.is_(None))
        )
        if row is None:
            raise DomainError("CASE_ASSIGNMENT_UNAVAILABLE", 409)
        return CurrentAssignmentReference(row.id, row.caregiver_actor_id)

    async def current_need(
        self, session: AsyncSession, case_id: UUID, identifier: UUID
    ) -> NeedReference:
        row = await session.scalar(
            select(Observation).where(Observation.case_id == case_id, Observation.id == identifier)
        )
        if row is None:
            raise DomainError("RECORD_NOT_FOUND", 404)
        if row.record_type != "NEED_CAPTURE":
            raise DomainError("NEED_CAPTURE_REQUIRED", 422)
        successor = await session.scalar(
            select(Observation.id).where(Observation.supersedes_observation_id == identifier)
        )
        if successor is not None:
            raise DomainError("STALE_RECORD_REVISION", 409)
        return NeedReference(row.id, row.case_id)
