"""Foundation contracts; never derive permissions from job titles or actor types."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from nasim.identity_context.contracts import ActorType
from nasim.provider_registry.contracts import (
    PROVIDER_CANDIDATE_PERMISSIONS,
    PROVIDER_QUALIFICATION_EVIDENCE_PERMISSIONS,
)
from nasim.referral.contracts import REFERRAL_PERMISSIONS

PERMISSIONS = (
    "case.create",
    "case.read.assigned",
    "case.monitor.assigned",
    "case.observe.assigned",
    "case.contact.manage.assigned",
    "case.assignment.manage",
    "case.read.oversight",
    *REFERRAL_PERMISSIONS,
    *PROVIDER_CANDIDATE_PERMISSIONS,
    *PROVIDER_QUALIFICATION_EVIDENCE_PERMISSIONS,
)
# BC-005 §§1/5 and DC-003 §§1/3. Vocabulary only, not final Pilot inventory/authority.
ROLES = {
    "elder": "سالمند",
    "family": "خانواده / همراه سالمند",
    "caregiver": "سالمندیار",
    "senior_caregiver": "سالمندیار ارشد",
    "neighborhood_supervisor": "سرپرست محله",
    "regional_supervisor": "سرپرست منطقه",
    "county_network_manager": "مدیر شبکه شهرستان",
    "province_network_manager": "مدیر شبکه استان",
    "nasim_operator": "شرکت / اپراتور نسیم",
    "employer": "کارفرما",
    "specialist_provider": "شریک / ارائه‌دهنده تخصصی",
    "nasim_system": "سامانه نسیم",
    "nasim_ai": "هوش مصنوعی داخلی نسیم",
}


class TrustedPrincipal(BaseModel):
    """Only a trusted in-process authentication adapter may construct/install this object."""

    model_config = ConfigDict(frozen=True, extra="forbid")
    actor_id: str = Field(min_length=1, max_length=200)
    actor_type: ActorType
    correlation_id: str = Field(min_length=1, max_length=200)


class Window(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    starts_at: datetime
    expires_at: datetime | None = None
    reason: str = Field(min_length=1, max_length=2000)
    supersedes_id: UUID | None = None

    @field_validator("reason")
    @classmethod
    def nonblank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Reason required")
        return value

    @field_validator("starts_at", "expires_at")
    @classmethod
    def aware(cls, value: datetime | None) -> datetime | None:
        if value is not None and (value.tzinfo is None or value.utcoffset() is None):
            raise ValueError("Timezone required")
        return value

    @model_validator(mode="after")
    def valid_window(self) -> "Window":
        if self.expires_at is not None and self.expires_at <= self.starts_at:
            raise ValueError("Expiry must follow start")
        return self
