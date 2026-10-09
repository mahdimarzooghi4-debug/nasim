"""Operational Case index using existing TS-03 permissions and current assignment.

This index has no lifecycle status, priority, outcome, or inferred work queue.
"""

from sqlalchemy import literal, select, tuple_
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from nasim.application.pagination import decode_cursor, encode_cursor
from nasim.domain.contracts import (
    AssignmentView,
    CaseProfileView,
    CaseView,
    Page,
    ProfileView,
)
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType
from nasim.infrastructure.models import Assignment, ElderCase, ProfileRevision


class AssignedCaseIndex:
    def __init__(self, sessions: async_sessionmaker[AsyncSession]) -> None:
        self.sessions = sessions

    async def list(
        self, actor: ActorContext, cursor: str | None = None, limit: int = 50
    ) -> Page[CaseProfileView]:
        # A role title or assignment by itself conveys no access.
        if actor.actor_type == ActorType.AI or not actor.capabilities.intersection(
            {"case.read.assigned", "case.read.oversight"}
        ):
            raise DomainError("CAPABILITY_REQUIRED", 403)
        if not 1 <= limit <= 100:
            raise DomainError("INVALID_PAGE_LIMIT", 422)

        # Latest profile is selected by revision number, not by timestamp.
        # A single PostgreSQL statement sees a consistent committed snapshot
        # for assignment, Case, and profile at this read boundary.
        latest_profile_id = (
            select(ProfileRevision.id)
            .where(ProfileRevision.case_id == ElderCase.id)
            .order_by(ProfileRevision.revision_no.desc())
            .limit(1)
            .correlate(ElderCase)
            .scalar_subquery()
        )
        statement = (
            select(ElderCase, Assignment, ProfileRevision)
            .join(
                Assignment,
                (Assignment.case_id == ElderCase.id) & Assignment.ended_at.is_(None),
            )
            .join(ProfileRevision, ProfileRevision.id == latest_profile_id)
        )
        # Explicitly authorized oversight sees all existing Cases. Otherwise
        # only current caregiver assignments matching the authenticated actor
        # are returned; caller-controlled actor IDs and filters are forbidden.
        if "case.read.oversight" not in actor.capabilities:
            statement = statement.where(Assignment.caregiver_actor_id == actor.actor_id)

        if cursor is not None:
            stamp, identifier = decode_cursor(cursor)
            statement = statement.where(
                tuple_(ElderCase.created_at, ElderCase.id)
                > tuple_(literal(stamp), literal(identifier))
            )
        async with self.sessions() as session:
            rows = (
                await session.execute(
                    statement.order_by(ElderCase.created_at, ElderCase.id).limit(limit + 1)
                )
            ).all()
        selected = rows[:limit]
        return Page[CaseProfileView](
            items=[
                CaseProfileView(
                    case=CaseView.model_validate(case),
                    current_assignment=AssignmentView.model_validate(assignment),
                    profile=ProfileView.model_validate(profile),
                )
                for case, assignment, profile in selected
            ],
            next_cursor=(
                encode_cursor(selected[-1][0].created_at, selected[-1][0].id)
                if len(rows) > limit
                else None
            ),
        )
