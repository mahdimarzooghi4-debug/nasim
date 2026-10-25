"""Referral record foundation only: no lifecycle, routing or provider decisions."""

from datetime import datetime
from uuid import UUID

from nasim.domain.contracts import AssignedCommand, Contract, Text
from nasim.identity_context.contracts import ActorType

REFERRAL_PERMISSIONS = (
    "referral.create.assigned",
    "referral.read.assigned",
    "referral.read.oversight",
)


class CreateReferral(AssignedCommand):
    source_need_observation_id: UUID
    reason: Text


class ReferralView(Contract):
    id: UUID
    case_id: UUID
    source_need_observation_id: UUID
    created_at: datetime
    created_by_actor_id: str
    created_by_actor_type: ActorType
    reason: str
    correlation_id: str


REFERRAL_FOLLOW_UP_PERMISSIONS = (
    "referral.follow_up.record.assigned",
    "referral.follow_up.read.assigned",
    "referral.follow_up.read.oversight",
)


class RecordReferralFollowUp(AssignedCommand):
    """Recorded human observation, not a Provider response or verified outcome."""

    note: Text
    reason: Text


class ReferralFollowUpView(Contract):
    id: UUID
    referral_id: UUID
    recorded_at: datetime
    recorded_by_actor_id: str
    recorded_by_actor_type: ActorType
    note: str
    reason: str
    correlation_id: str
