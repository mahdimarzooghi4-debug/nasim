from uuid import uuid4

import pytest
from pydantic import ValidationError

from nasim.referral.contracts import CreateReferral, ReferralView


@pytest.mark.parametrize(
    "field",
    [
        "status",
        "state",
        "provider_id",
        "service_id",
        "sla",
        "priority",
        "severity",
        "cost",
        "payment",
        "dispatch",
        "consent",
        "correction_reason",
    ],
)
def test_referral_contract_excludes_undecided_fields(field):
    with pytest.raises(ValidationError):
        CreateReferral(
            source_need_observation_id=uuid4(),
            expected_current_assignment_id=uuid4(),
            reason="record only",
            **{field: "invented"},
        )


@pytest.mark.parametrize("reason", ["", " ", "\n"])
def test_referral_reason_required(reason):
    with pytest.raises(ValidationError):
        CreateReferral(
            source_need_observation_id=uuid4(),
            expected_current_assignment_id=uuid4(),
            reason=reason,
        )


def test_referral_view_is_only_foundation_evidence():
    assert set(ReferralView.model_fields) == {
        "id",
        "case_id",
        "source_need_observation_id",
        "created_at",
        "created_by_actor_id",
        "created_by_actor_type",
        "reason",
        "correlation_id",
    }
