"""Pre-operational Provider Candidate contracts only."""

from datetime import datetime
from uuid import UUID

from nasim.domain.contracts import Contract, Page, Text
from nasim.identity_context.contracts import ActorType

PROVIDER_CANDIDATE_PERMISSIONS = (
    "provider_candidate.register",
    "provider_candidate.read",
)

PROVIDER_QUALIFICATION_EVIDENCE_PERMISSIONS = (
    "provider_qualification_evidence.record",
    "provider_qualification_evidence.read",
)

PROVIDER_QUALIFICATION_REVIEW_PERMISSIONS = (
    "provider_qualification_review.request",
    "provider_qualification_review.read",
)


class RegisterProviderCandidate(Contract):
    display_name: Text
    reason: Text


class ProviderCandidateView(Contract):
    id: UUID
    display_name: str
    registered_at: datetime
    registered_by_actor_id: str
    registered_by_actor_type: ActorType
    reason: str
    correlation_id: str


class RecordProviderQualificationEvidence(Contract):
    evidence_label: Text
    evidence_reference: Text
    reason: Text


class ProviderQualificationEvidenceView(Contract):
    id: UUID
    provider_candidate_id: UUID
    evidence_label: str
    evidence_reference: str
    recorded_at: datetime
    recorded_by_actor_id: str
    recorded_by_actor_type: ActorType
    reason: str
    correlation_id: str


class RequestProviderQualificationReview(Contract):
    reason: Text


class ProviderQualificationReviewRequestView(Contract):
    id: UUID
    provider_candidate_id: UUID
    requested_at: datetime
    requested_by_actor_id: str
    requested_by_actor_type: ActorType
    reason: str
    correlation_id: str


class ProviderQualificationReviewWorkspaceView(Contract):
    """Bounded descriptive read model; never a qualification evaluation."""

    candidate: ProviderCandidateView
    evidence: Page[ProviderQualificationEvidenceView]
    review_requests: Page[ProviderQualificationReviewRequestView]
