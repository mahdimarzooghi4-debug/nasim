from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from nasim.domain.errors import DomainError


class ActorType(StrEnum):
    HUMAN = "HUMAN"
    SYSTEM = "SYSTEM"
    AI = "AI"
    AUTOMATION = "AUTOMATION"


class ActorContext(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    actor_id: str = Field(min_length=1, max_length=200)
    actor_type: ActorType
    capabilities: frozenset[str]
    correlation_id: str = Field(min_length=1, max_length=200)


def require_capability(actor: ActorContext, capability: str) -> None:
    # AI access is explicitly outside TS-03 even with a misconfigured capability grant.
    if actor.actor_type == ActorType.AI or capability not in actor.capabilities:
        raise DomainError("CAPABILITY_REQUIRED", 403)


def require_assigned(actor: ActorContext, capability: str, caregiver_id: str) -> None:
    require_capability(actor, capability)
    if actor.actor_id != caregiver_id:
        raise DomainError("ASSIGNED_CAREGIVER_REQUIRED", 403)
