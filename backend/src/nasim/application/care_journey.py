"""Read-only composition of existing independently authorized Elder Case workflows.

This view never authorizes a service, decides a need outcome or freezes evidence.
Existing module-owned read services retain their own authorization checks.
"""

from uuid import UUID

from nasim.application.casework import Casework
from nasim.domain.contracts import (
    CaseProfileView,
    Contract,
    ObservationView,
    Page,
)
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType
from nasim.referral.contracts import ReferralFollowUpView, ReferralView
from nasim.referral.follow_up import ReferralFollowUps
from nasim.referral.service import Referrals


class CareJourneyWorkspaceView(Contract):
    case: CaseProfileView
    observations: Page[ObservationView]
    referrals: Page[ReferralView]
    selected_referral: ReferralView | None
    follow_ups: Page[ReferralFollowUpView] | None


class CareJourneyWorkspace:
    """A descriptive read across existing public services, never a frozen snapshot."""

    def __init__(
        self, casework: Casework, referrals: Referrals, follow_ups: ReferralFollowUps
    ) -> None:
        self.casework = casework
        self.referrals = referrals
        self.follow_ups = follow_ups

    @staticmethod
    def _require_all_reads(actor: ActorContext) -> None:
        required_groups = (
            {"case.read.assigned", "case.read.oversight"},
            {"referral.read.assigned", "referral.read.oversight"},
            {"referral.follow_up.read.assigned", "referral.follow_up.read.oversight"},
        )
        if actor.actor_type == ActorType.AI or any(
            actor.capabilities.isdisjoint(group) for group in required_groups
        ):
            raise DomainError("CAPABILITY_REQUIRED", 403)

    async def read(
        self,
        case_id: UUID,
        actor: ActorContext,
        referral_id: UUID | None = None,
        observation_cursor: str | None = None,
        referral_cursor: str | None = None,
        follow_up_cursor: str | None = None,
        limit: int = 50,
    ) -> CareJourneyWorkspaceView:
        # Refuse partial cross-domain disclosures if even one permission is absent.
        self._require_all_reads(actor)
        if not 1 <= limit <= 100:
            raise DomainError("INVALID_PAGE_LIMIT", 422)
        if referral_id is None and follow_up_cursor is not None:
            raise DomainError("INVALID_CURSOR", 422)

        # These are intentionally independent module-owned reads. The view does
        # not promise an immutable cross-service snapshot or status at a time.
        summary = CaseProfileView.model_validate(
            await self.casework.read("profile", case_id, actor)
        )
        observations = Page[ObservationView].model_validate(
            await self.casework.read(
                "observations", case_id, actor, cursor=observation_cursor, limit=limit
            )
        )
        referrals = Page[ReferralView].model_validate(
            await self.referrals.list(case_id, actor, cursor=referral_cursor, limit=limit)
        )
        selected: ReferralView | None = None
        follow_ups: Page[ReferralFollowUpView] | None = None
        if referral_id is not None:
            selected = await self.referrals.get(referral_id, actor)
            if selected.case_id != case_id:
                # A referral belonging to another Case cannot be selected in this workspace.
                raise DomainError("REFERRAL_NOT_FOUND", 404)
            follow_ups = Page[ReferralFollowUpView].model_validate(
                await self.follow_ups.list(referral_id, actor, cursor=follow_up_cursor, limit=limit)
            )
        return CareJourneyWorkspaceView(
            case=summary,
            observations=observations,
            referrals=referrals,
            selected_referral=selected,
            follow_ups=follow_ups,
        )
