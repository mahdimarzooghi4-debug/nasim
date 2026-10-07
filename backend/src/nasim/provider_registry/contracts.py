"""Pre-operational Provider Candidate contracts only."""

from datetime import datetime
from uuid import UUID

from nasim.domain.contracts import Contract, Text
from nasim.identity_context.contracts import ActorType

PROVIDER_CANDIDATE_PERMISSIONS = (
    "provider_candidate.register",
    "provider_candidate.read",
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
