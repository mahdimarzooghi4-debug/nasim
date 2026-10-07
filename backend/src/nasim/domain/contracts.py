from datetime import datetime
from typing import Annotated, Literal
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, StringConstraints

Text = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=10000)]
Identifier = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=200)]
ContactKind = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]


class Contract(BaseModel):
    model_config = ConfigDict(extra="forbid", from_attributes=True)


class CreateCase(Contract):
    upstream_enrollment_ref: Identifier
    elder_reference: Identifier
    initial_caregiver_actor_id: Identifier


class AssignedCommand(Contract):
    expected_current_assignment_id: UUID


class CorrectCaseProfile(AssignedCommand):
    expected_current_revision_id: UUID
    elder_reference: Identifier
    correction_reason: Text


class ReassignCaregiver(AssignedCommand):
    caregiver_actor_id: Identifier
    reason: Text


class AddContactPoint(AssignedCommand):
    contact_kind: ContactKind
    contact_value: Text


class CorrectContactPoint(AddContactPoint):
    expected_current_revision_id: UUID
    correction_reason: Text


class RecordInteraction(AssignedCommand):
    interaction_type: Literal["CONTACT", "MONITORING"]
    occurred_at: AwareDatetime
    content: Text


class CorrectInteraction(RecordInteraction):
    expected_current_record_id: UUID
    correction_reason: Text


class RecordObservation(AssignedCommand):
    record_type: Literal["OBSERVATION", "NEED_CAPTURE"]
    occurred_at: AwareDatetime
    content: Text


class CorrectObservation(RecordObservation):
    expected_current_record_id: UUID
    correction_reason: Text


Command = (
    CreateCase
    | CorrectCaseProfile
    | ReassignCaregiver
    | AddContactPoint
    | CorrectContactPoint
    | RecordInteraction
    | CorrectInteraction
    | RecordObservation
    | CorrectObservation
)


class ProvenanceView(Contract):
    recorded_at: datetime
    recorded_by_actor_id: str
    recorded_by_actor_type: Literal["HUMAN", "SYSTEM", "AI", "AUTOMATION"]


class CaseView(Contract):
    id: UUID
    upstream_enrollment_ref: str
    created_at: datetime
    created_by_actor_id: str
    created_by_actor_type: Literal["HUMAN", "SYSTEM", "AI", "AUTOMATION"]


class ProfileView(ProvenanceView):
    id: UUID
    case_id: UUID
    revision_no: int
    elder_reference: str
    supersedes_revision_id: UUID | None
    correction_reason: str | None


class AssignmentView(Contract):
    id: UUID
    case_id: UUID
    caregiver_actor_id: str
    started_at: datetime
    ended_at: datetime | None
    assigned_by_actor_id: str
    assigned_by_actor_type: Literal["HUMAN", "SYSTEM", "AI", "AUTOMATION"]
    reason: str


class ContactView(ProvenanceView):
    id: UUID
    case_id: UUID
    logical_contact_id: UUID
    revision_no: int
    contact_kind: str
    contact_value: str
    supersedes_revision_id: UUID | None
    correction_reason: str | None


class InteractionView(ProvenanceView):
    id: UUID
    case_id: UUID
    interaction_type: Literal["CONTACT", "MONITORING"]
    occurred_at: datetime
    content: str
    supersedes_interaction_id: UUID | None
    correction_reason: str | None


class ObservationView(ProvenanceView):
    id: UUID
    case_id: UUID
    record_type: Literal["OBSERVATION", "NEED_CAPTURE"]
    occurred_at: datetime
    content: str
    supersedes_observation_id: UUID | None
    correction_reason: str | None


class CaseProfileView(Contract):
    case: CaseView
    profile: ProfileView
    current_assignment: AssignmentView


class WorkspaceView(CaseProfileView):
    profile_history: list[ProfileView]
    contacts: list[ContactView]
    interactions: list[InteractionView]
    observations: list[ObservationView]


class Page[T](Contract):
    items: list[T]
    next_cursor: str | None


class TimelineEntry(Contract):
    id: UUID
    case_id: UUID
    actor_id: str
    actor_type: str
    action: str
    resource_type: str
    resource_id: UUID
    timestamp: datetime
    correlation_id: str
    before_reference: UUID | None
    after_reference: UUID
    reason: str | None


class ErrorDetail(Contract):
    code: str
    message: str


class ErrorResponse(Contract):
    error: ErrorDetail
