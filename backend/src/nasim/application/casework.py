"""One transactional application boundary for the ElderCase aggregate.

Infrastructure is private to this application module; the API consumes contracts only.
Every mutation acquires idempotency then Case locks in the same order.
"""

import hashlib
import json
from datetime import UTC, datetime
from typing import Any
from uuid import UUID, uuid4

from sqlalchemy import literal, select, text, tuple_
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from nasim.application.pagination import decode_cursor, encode_cursor
from nasim.domain.contracts import (
    AddContactPoint,
    AssignedCommand,
    AssignmentView,
    CaseProfileView,
    CaseView,
    Command,
    ContactView,
    CorrectCaseProfile,
    CorrectContactPoint,
    CorrectInteraction,
    CorrectObservation,
    CreateCase,
    InteractionView,
    ObservationView,
    Page,
    ProfileView,
    ReassignCaregiver,
    RecordInteraction,
    RecordObservation,
    TimelineEntry,
    WorkspaceView,
)
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, require_assigned, require_capability
from nasim.infrastructure.models import (
    Assignment,
    AuditEntry,
    ContactRevision,
    ElderCase,
    IdempotencyRecord,
    Interaction,
    Observation,
    OutboxEvent,
    ProfileRevision,
)

EVENTS = {
    "create": "case.created.v1",
    "profile_correct": "case.profile_corrected.v1",
    "contact_add": "case.contact_recorded.v1",
    "contact_correct": "case.contact_corrected.v1",
    "interaction_add": "case.interaction_recorded.v1",
    "interaction_correct": "case.interaction_corrected.v1",
    "observation_add": "case.observation_recorded.v1",
    "observation_correct": "case.observation_corrected.v1",
    "reassign": "case.caregiver_reassigned.v1",
}
CAPABILITIES = {
    "create": "case.assignment.manage",
    "reassign": "case.assignment.manage",
    "profile_correct": "case.assignment.manage",
    "contact_add": "case.contact.manage.assigned",
    "contact_correct": "case.contact.manage.assigned",
    "interaction_add": "case.monitor.assigned",
    "interaction_correct": "case.monitor.assigned",
    "observation_add": "case.observe.assigned",
    "observation_correct": "case.observe.assigned",
}


def canonical_hash(payload: dict[str, Any]) -> str:
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def _result_actor_type(operation: str, result: dict[str, Any]) -> str | None:
    """Read immutable actor provenance from a stored TS-03 idempotency response."""
    if operation == "create":
        case = result.get("case")
        return case.get("created_by_actor_type") if isinstance(case, dict) else None
    field = "assigned_by_actor_type" if operation == "reassign" else "recorded_by_actor_type"
    value = result.get(field)
    return value if isinstance(value, str) else None


class Casework:
    def __init__(self, sessions: async_sessionmaker[AsyncSession]) -> None:
        self.sessions = sessions

    async def _assignment(self, session: AsyncSession, case_id: UUID) -> Assignment:
        assignment = await session.scalar(
            select(Assignment).where(Assignment.case_id == case_id, Assignment.ended_at.is_(None))
        )
        if assignment is None:
            raise DomainError("CASE_ASSIGNMENT_UNAVAILABLE", 409)
        return assignment

    async def _lock_case(self, session: AsyncSession, case_id: UUID) -> ElderCase:
        # Reads take the same lock so assignment authorization and returned data are consistent.
        case = await session.scalar(
            select(ElderCase).where(ElderCase.id == case_id).with_for_update()
        )
        if case is None:
            raise DomainError("CASE_NOT_FOUND", 404)
        return case

    async def mutate(
        self,
        operation: str,
        command: Command,
        actor: ActorContext,
        key: str,
        case_id: UUID | None = None,
        resource_id: UUID | None = None,
    ) -> dict[str, Any]:
        capability = CAPABILITIES[operation]
        require_capability(actor, capability)
        if not key.strip() or len(key) > 200:
            raise DomainError("INVALID_IDEMPOTENCY_KEY", 422)
        target = str(case_id) if case_id else ""
        payload_hash = canonical_hash(
            {
                "body": command.model_dump(mode="json"),
                "resource_id": str(resource_id) if resource_id else None,
            }
        )
        scope = {"actor_id": actor.actor_id, "operation": operation, "target": target, "key": key}
        lock_id = int.from_bytes(bytes.fromhex(canonical_hash(scope))[:8], signed=True)
        async with self.sessions() as session, session.begin():
            # Advisory lock handles the absent-row race on first use of a key, including creation.
            # DB uniqueness is the independent backstop; lock collisions only serialize callers.
            await session.execute(text("SELECT pg_advisory_xact_lock(:id)"), {"id": lock_id})
            assignment = None
            if case_id is not None:
                await self._lock_case(session, case_id)
                assignment = await self._assignment(session, case_id)
                if capability.endswith(".assigned"):
                    require_assigned(actor, capability, assignment.caregiver_actor_id)
            prior = await session.scalar(select(IdempotencyRecord).filter_by(**scope))
            if prior:
                if prior.payload_hash != payload_hash or (
                    _result_actor_type(operation, prior.response) != actor.actor_type.value
                ):
                    # TS-05 treats (actor_id, actor_type) as distinct trusted principals.
                    # Scope rows predate an actor_type column: use immutable result
                    # provenance to deny cross-type replay without invalidating old keys.
                    raise DomainError("IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD", 409)
                # Recheck current authorization before returning any cached sensitive data.
                return prior.response
            if isinstance(command, AssignedCommand):
                if assignment is None or command.expected_current_assignment_id != assignment.id:
                    raise DomainError("CASE_ASSIGNMENT_CHANGED", 409)
            now = datetime.now(UTC)
            result, new_case_id, resource_type, after_id, before_id, reason = await self._execute(
                session, command, actor, now, case_id, resource_id, assignment
            )
            await self._record_effects(
                session,
                actor,
                now,
                operation,
                new_case_id,
                resource_type,
                after_id,
                before_id,
                reason,
                result,
            )
            session.add(
                IdempotencyRecord(
                    **scope, payload_hash=payload_hash, response=result, created_at=now
                )
            )
            await session.flush()
            return result

    async def _record_effects(
        self,
        session: AsyncSession,
        actor: ActorContext,
        now: datetime,
        operation: str,
        case_id: UUID,
        resource_type: str,
        after_id: UUID,
        before_id: UUID | None,
        reason: str | None,
        result: dict[str, Any],
    ) -> None:
        session.add(
            AuditEntry(
                case_id=case_id,
                actor_id=actor.actor_id,
                actor_type=actor.actor_type,
                action=EVENTS[operation],
                resource_type=resource_type,
                resource_id=after_id,
                timestamp=now,
                correlation_id=actor.correlation_id,
                before_reference=before_id,
                after_reference=after_id,
                reason=reason,
            )
        )
        # Identifier/provenance-only event payload. Contact values/content never leave in events.
        event_payload = {
            "case_id": str(case_id),
            "resource_id": str(after_id),
            "supersedes_id": str(before_id) if before_id else None,
            "actor_id": actor.actor_id,
            "actor_type": actor.actor_type,
            "timestamp": now.isoformat(),
            "correlation_id": actor.correlation_id,
        }
        if operation == "create":
            event_payload["profile_revision_id"] = result["profile"]["id"]
            event_payload["assignment_id"] = result["current_assignment"]["id"]
        session.add(
            OutboxEvent(
                case_id=case_id,
                event_type=EVENTS[operation],
                occurred_at=now,
                payload=event_payload,
            )
        )

    async def _execute(
        self,
        session: AsyncSession,
        command: Command,
        actor: ActorContext,
        now: datetime,
        case_id: UUID | None,
        resource_id: UUID | None,
        assignment: Assignment | None,
    ) -> tuple[dict[str, Any], UUID, str, UUID, UUID | None, str | None]:
        provenance = dict(
            recorded_at=now,
            recorded_by_actor_id=actor.actor_id,
            recorded_by_actor_type=actor.actor_type,
        )
        if isinstance(command, CreateCase):
            case = ElderCase(
                id=uuid4(),
                upstream_enrollment_ref=command.upstream_enrollment_ref,
                created_at=now,
                created_by_actor_id=actor.actor_id,
                created_by_actor_type=actor.actor_type,
            )
            session.add(case)
            await session.flush()
            profile = ProfileRevision(
                id=uuid4(),
                case_id=case.id,
                revision_no=1,
                elder_reference=command.elder_reference,
                **provenance,
            )
            initial = Assignment(
                id=uuid4(),
                case_id=case.id,
                caregiver_actor_id=command.initial_caregiver_actor_id,
                started_at=now,
                assigned_by_actor_id=actor.actor_id,
                assigned_by_actor_type=actor.actor_type,
                reason="INITIAL_ASSIGNMENT",
            )
            session.add_all([profile, initial])
            await session.flush()
            response = CaseProfileView(
                case=CaseView.model_validate(case),
                profile=ProfileView.model_validate(profile),
                current_assignment=AssignmentView.model_validate(initial),
            )
            return response.model_dump(mode="json"), case.id, "elder_case", case.id, None, None
        assert case_id is not None and assignment is not None
        if isinstance(command, ReassignCaregiver):
            assignment.ended_at = now
            await session.flush()  # Release partial unique-index slot before inserting successor.
            successor = Assignment(
                id=uuid4(),
                case_id=case_id,
                caregiver_actor_id=command.caregiver_actor_id,
                started_at=now,
                assigned_by_actor_id=actor.actor_id,
                assigned_by_actor_type=actor.actor_type,
                reason=command.reason,
            )
            session.add(successor)
            await session.flush()
            return (
                AssignmentView.model_validate(successor).model_dump(mode="json"),
                case_id,
                "case_assignment",
                successor.id,
                assignment.id,
                command.reason,
            )
        if isinstance(command, CorrectCaseProfile):
            current = await session.scalar(
                select(ProfileRevision)
                .where(ProfileRevision.case_id == case_id)
                .order_by(ProfileRevision.revision_no.desc())
            )
            if current is None or current.id != command.expected_current_revision_id:
                raise DomainError("STALE_RECORD_REVISION", 409)
            profile = ProfileRevision(
                id=uuid4(),
                case_id=case_id,
                revision_no=current.revision_no + 1,
                elder_reference=command.elder_reference,
                supersedes_revision_id=current.id,
                correction_reason=command.correction_reason,
                **provenance,
            )
            session.add(profile)
            await session.flush()
            return (
                ProfileView.model_validate(profile).model_dump(mode="json"),
                case_id,
                "case_profile_revision",
                profile.id,
                current.id,
                command.correction_reason,
            )
        if isinstance(command, AddContactPoint):
            before = None
            revision_no = 1
            logical_id = uuid4()
            reason = None
            if isinstance(command, CorrectContactPoint):
                current_contact = await session.scalar(
                    select(ContactRevision)
                    .where(
                        ContactRevision.case_id == case_id,
                        ContactRevision.logical_contact_id == resource_id,
                    )
                    .order_by(ContactRevision.revision_no.desc())
                )
                if current_contact is None:
                    raise DomainError("RECORD_NOT_FOUND", 404)
                if current_contact.id != command.expected_current_revision_id:
                    raise DomainError("STALE_RECORD_REVISION", 409)
                before = current_contact.id
                logical_id = current_contact.logical_contact_id
                revision_no = current_contact.revision_no + 1
                reason = command.correction_reason
            contact = ContactRevision(
                id=uuid4(),
                case_id=case_id,
                logical_contact_id=logical_id,
                revision_no=revision_no,
                contact_kind=command.contact_kind,
                contact_value=command.contact_value,
                supersedes_revision_id=before,
                correction_reason=reason,
                **provenance,
            )
            session.add(contact)
            await session.flush()
            return (
                ContactView.model_validate(contact).model_dump(mode="json"),
                case_id,
                "contact_point_revision",
                contact.id,
                before,
                reason,
            )
        if isinstance(command, RecordInteraction):
            before = None
            reason = None
            if isinstance(command, CorrectInteraction):
                current_interaction = await session.scalar(
                    select(Interaction).where(
                        Interaction.id == resource_id, Interaction.case_id == case_id
                    )
                )
                if current_interaction is None:
                    raise DomainError("RECORD_NOT_FOUND", 404)
                successor_id = await session.scalar(
                    select(Interaction.id).where(
                        Interaction.supersedes_interaction_id == current_interaction.id
                    )
                )
                if successor_id or current_interaction.id != command.expected_current_record_id:
                    raise DomainError("STALE_RECORD_REVISION", 409)
                before = current_interaction.id
                reason = command.correction_reason
            interaction = Interaction(
                id=uuid4(),
                case_id=case_id,
                interaction_type=command.interaction_type,
                occurred_at=command.occurred_at,
                content=command.content,
                supersedes_interaction_id=before,
                correction_reason=reason,
                **provenance,
            )
            session.add(interaction)
            await session.flush()
            return (
                InteractionView.model_validate(interaction).model_dump(mode="json"),
                case_id,
                "case_interaction",
                interaction.id,
                before,
                reason,
            )
        if isinstance(command, RecordObservation):
            before = None
            reason = None
            if isinstance(command, CorrectObservation):
                current_observation = await session.scalar(
                    select(Observation).where(
                        Observation.id == resource_id, Observation.case_id == case_id
                    )
                )
                if current_observation is None:
                    raise DomainError("RECORD_NOT_FOUND", 404)
                successor_id = await session.scalar(
                    select(Observation.id).where(
                        Observation.supersedes_observation_id == current_observation.id
                    )
                )
                if successor_id or current_observation.id != command.expected_current_record_id:
                    raise DomainError("STALE_RECORD_REVISION", 409)
                before = current_observation.id
                reason = command.correction_reason
            observation = Observation(
                id=uuid4(),
                case_id=case_id,
                record_type=command.record_type,
                occurred_at=command.occurred_at,
                content=command.content,
                supersedes_observation_id=before,
                correction_reason=reason,
                **provenance,
            )
            session.add(observation)
            await session.flush()
            return (
                ObservationView.model_validate(observation).model_dump(mode="json"),
                case_id,
                "case_observation",
                observation.id,
                before,
                reason,
            )
        raise ValueError("Unsupported command")

    async def read(
        self,
        kind: str,
        case_id: UUID,
        actor: ActorContext,
        cursor: str | None = None,
        limit: int = 50,
    ) -> Any:
        if actor.actor_type == "AI":
            raise DomainError("CAPABILITY_REQUIRED", 403)
        if not (actor.capabilities & {"case.read.assigned", "case.read.oversight"}):
            raise DomainError("CAPABILITY_REQUIRED", 403)
        async with self.sessions() as session, session.begin():
            case = await self._lock_case(session, case_id)
            assignment = await self._assignment(session, case_id)
            if "case.read.oversight" not in actor.capabilities:
                require_assigned(actor, "case.read.assigned", assignment.caregiver_actor_id)
            if kind in {"profile", "workspace"}:
                profiles = (
                    await session.scalars(
                        select(ProfileRevision)
                        .where(ProfileRevision.case_id == case_id)
                        .order_by(ProfileRevision.revision_no)
                    )
                ).all()
                summary = CaseProfileView(
                    case=CaseView.model_validate(case),
                    profile=ProfileView.model_validate(profiles[-1]),
                    current_assignment=AssignmentView.model_validate(assignment),
                )
                if kind == "profile":
                    return summary
                contacts = (
                    await session.scalars(
                        select(ContactRevision)
                        .where(ContactRevision.case_id == case_id)
                        .order_by(ContactRevision.logical_contact_id, ContactRevision.revision_no)
                    )
                ).all()
                current_contacts = {
                    row.logical_contact_id: ContactView.model_validate(row) for row in contacts
                }
                interactions = (
                    await session.scalars(
                        select(Interaction)
                        .where(Interaction.case_id == case_id)
                        .order_by(Interaction.recorded_at, Interaction.id)
                    )
                ).all()
                observations = (
                    await session.scalars(
                        select(Observation)
                        .where(Observation.case_id == case_id)
                        .order_by(Observation.recorded_at, Observation.id)
                    )
                ).all()
                superseded_interactions = {r.supersedes_interaction_id for r in interactions}
                superseded_observations = {r.supersedes_observation_id for r in observations}
                return WorkspaceView(
                    **summary.model_dump(),
                    profile_history=[ProfileView.model_validate(r) for r in profiles],
                    contacts=list(current_contacts.values()),
                    interactions=[
                        InteractionView.model_validate(r)
                        for r in interactions
                        if r.id not in superseded_interactions
                    ],
                    observations=[
                        ObservationView.model_validate(r)
                        for r in observations
                        if r.id not in superseded_observations
                    ],
                )
            if kind == "assignments":
                rows = (
                    await session.scalars(
                        select(Assignment)
                        .where(Assignment.case_id == case_id)
                        .order_by(Assignment.started_at, Assignment.id)
                    )
                ).all()
                return [AssignmentView.model_validate(r) for r in rows]
            if kind == "contacts":
                rows = (
                    await session.scalars(
                        select(ContactRevision)
                        .where(ContactRevision.case_id == case_id)
                        .order_by(ContactRevision.logical_contact_id, ContactRevision.revision_no)
                    )
                ).all()
                # All contact revisions are readable; workspace exposes only current revisions.
                return [ContactView.model_validate(r) for r in rows]
            if kind == "interactions":
                statement = select(Interaction).where(Interaction.case_id == case_id)
                if cursor:
                    stamp, identifier = decode_cursor(cursor)
                    statement = statement.where(
                        tuple_(Interaction.recorded_at, Interaction.id)
                        > tuple_(literal(stamp), literal(identifier))
                    )
                rows = (
                    await session.scalars(
                        statement.order_by(Interaction.recorded_at, Interaction.id).limit(limit + 1)
                    )
                ).all()
                selected = rows[:limit]
                next_cursor = (
                    encode_cursor(selected[-1].recorded_at, selected[-1].id)
                    if len(rows) > limit
                    else None
                )
                return Page[InteractionView](
                    items=[InteractionView.model_validate(r) for r in selected],
                    next_cursor=next_cursor,
                )
            if kind == "observations":
                statement = select(Observation).where(Observation.case_id == case_id)
                if cursor:
                    stamp, identifier = decode_cursor(cursor)
                    statement = statement.where(
                        tuple_(Observation.recorded_at, Observation.id)
                        > tuple_(literal(stamp), literal(identifier))
                    )
                rows = (
                    await session.scalars(
                        statement.order_by(Observation.recorded_at, Observation.id).limit(limit + 1)
                    )
                ).all()
                selected = rows[:limit]
                next_cursor = (
                    encode_cursor(selected[-1].recorded_at, selected[-1].id)
                    if len(rows) > limit
                    else None
                )
                return Page[ObservationView](
                    items=[ObservationView.model_validate(r) for r in selected],
                    next_cursor=next_cursor,
                )
            if kind == "timeline":
                statement = select(AuditEntry).where(
                    AuditEntry.case_id == case_id, AuditEntry.action.in_(EVENTS.values())
                )
                if cursor:
                    stamp, identifier = decode_cursor(cursor)
                    statement = statement.where(
                        tuple_(AuditEntry.timestamp, AuditEntry.id)
                        > tuple_(literal(stamp), literal(identifier))
                    )
                rows = (
                    await session.scalars(
                        statement.order_by(AuditEntry.timestamp, AuditEntry.id).limit(limit + 1)
                    )
                ).all()
                selected = rows[:limit]
                next_cursor = (
                    encode_cursor(selected[-1].timestamp, selected[-1].id)
                    if len(rows) > limit
                    else None
                )
                return Page[TimelineEntry](
                    items=[TimelineEntry.model_validate(r) for r in selected],
                    next_cursor=next_cursor,
                )
            raise ValueError("Unsupported query")
