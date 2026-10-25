import base64
import json
from datetime import UTC, datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from nasim.application.casework import canonical_hash
from nasim.application.pagination import decode_cursor, encode_cursor
from nasim.domain.contracts import (
    CorrectCaseProfile,
    CorrectContactPoint,
    CorrectInteraction,
    CorrectObservation,
    CreateCase,
    ReassignCaregiver,
    RecordInteraction,
    RecordObservation,
)
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import (
    ActorContext,
    ActorType,
    require_assigned,
    require_capability,
)


@pytest.mark.parametrize(
    "field", ["upstream_enrollment_ref", "elder_reference", "initial_caregiver_actor_id"]
)
@pytest.mark.parametrize("value", ["", "   ", None])
def test_creation_requires_references(field, value):
    data = dict(
        upstream_enrollment_ref="enrollment-1",
        elder_reference="elder-1",
        initial_caregiver_actor_id="caregiver-1",
    )
    data[field] = value
    with pytest.raises(ValidationError):
        CreateCase.model_validate(data)


@pytest.mark.parametrize(
    "contract,extra",
    [
        (
            CorrectCaseProfile,
            {"elder_reference": "ref", "expected_current_revision_id": str(uuid4())},
        ),
        (
            CorrectContactPoint,
            {
                "contact_kind": "phone",
                "contact_value": "number",
                "expected_current_revision_id": str(uuid4()),
            },
        ),
        (
            CorrectInteraction,
            {
                "interaction_type": "CONTACT",
                "occurred_at": datetime.now(UTC),
                "content": "note",
                "expected_current_record_id": str(uuid4()),
            },
        ),
        (
            CorrectObservation,
            {
                "record_type": "OBSERVATION",
                "occurred_at": datetime.now(UTC),
                "content": "note",
                "expected_current_record_id": str(uuid4()),
            },
        ),
    ],
)
@pytest.mark.parametrize("reason", [None, "", "  "])
def test_correction_requires_reason(contract, extra, reason):
    with pytest.raises(ValidationError):
        contract.model_validate(
            {"expected_current_assignment_id": str(uuid4()), "correction_reason": reason, **extra}
        )


@pytest.mark.parametrize("kind", ["REFERRAL", "SERVICE", "EMERGENCY", "OUTCOME"])
def test_interaction_excludes_other_scopes(kind):
    with pytest.raises(ValidationError):
        RecordInteraction.model_validate(
            dict(
                expected_current_assignment_id=uuid4(),
                interaction_type=kind,
                occurred_at=datetime.now(UTC),
                content="note",
            )
        )


@pytest.mark.parametrize(
    "field", ["severity", "eligibility", "referral_id", "outcome", "training_eligible"]
)
def test_observation_rejects_unknown_business_fields(field):
    with pytest.raises(ValidationError):
        RecordObservation.model_validate(
            dict(
                expected_current_assignment_id=uuid4(),
                record_type="OBSERVATION",
                occurred_at=datetime.now(UTC),
                content="note",
                **{field: "value"},
            )
        )


def test_requires_aware_datetime():
    with pytest.raises(ValidationError):
        RecordInteraction.model_validate(
            dict(
                expected_current_assignment_id=uuid4(),
                interaction_type="CONTACT",
                occurred_at="2026-10-07T12:00:00",
                content="note",
            )
        )


def test_reassignment_requires_reason():
    with pytest.raises(ValidationError):
        ReassignCaregiver.model_validate(
            dict(expected_current_assignment_id=uuid4(), caregiver_actor_id="next")
        )


def test_ownership_is_not_permission(caregiver):
    with pytest.raises(DomainError, match="CAPABILITY_REQUIRED"):
        require_capability(caregiver, "case.assignment.manage")
    with pytest.raises(DomainError, match="ASSIGNED_CAREGIVER_REQUIRED"):
        require_assigned(caregiver, "case.read.assigned", "someone-else")


@pytest.mark.parametrize("kind", list(ActorType))
def test_actor_vocabulary_preserved(kind):
    actor = ActorContext(
        actor_id="actor", actor_type=kind, capabilities=frozenset(), correlation_id="x"
    )
    assert actor.model_dump(mode="json")["actor_type"] == kind.value


def test_ai_denied_even_with_capability():
    actor = ActorContext(
        actor_id="ai",
        actor_type=ActorType.AI,
        capabilities=frozenset({"case.read.oversight"}),
        correlation_id="x",
    )
    with pytest.raises(DomainError, match="CAPABILITY_REQUIRED"):
        require_capability(actor, "case.read.oversight")


def test_canonical_payload_order():
    assert canonical_hash({"a": 1, "b": 2}) == canonical_hash({"b": 2, "a": 1})
    assert canonical_hash({"a": 2}) != canonical_hash({"a": 1})


def test_cursor_round_trip():
    pair = datetime.now(UTC), uuid4()
    assert decode_cursor(encode_cursor(*pair)) == pair


@pytest.mark.parametrize("cursor", ["?", "e30=", "bnVsbA==", "W10=", "WyJubyIsIm5vIl0="])
def test_malformed_cursor(cursor):
    with pytest.raises(DomainError, match="INVALID_CURSOR"):
        decode_cursor(cursor)


@pytest.mark.parametrize(
    "payload",
    [
        ["2026-10-08T12:00:00+00:00", 123],
        ["2026-10-08T12:00:00+00:00", None],
        ["2026-10-08T12:00:00+00:00", {"id": "malformed"}],
        ["2026-10-08T12:00:00+00:00", ["uuid"]],
        [123, "123e4567-e89b-12d3-a456-426614174000"],
        [None, "123e4567-e89b-12d3-a456-426614174000"],
        [{}, "123e4567-e89b-12d3-a456-426614174000"],
        ["2026-10-08T12:00:00", "123e4567-e89b-12d3-a456-426614174000"],
    ],
)
def test_cursor_rejects_wrong_json_element_types(payload):
    """Untrusted cursors fail as contract errors, never as UUID/parser exceptions."""
    token = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()
    with pytest.raises(DomainError) as error:
        decode_cursor(token)
    assert error.value.code == "INVALID_CURSOR"
    assert error.value.status == 422


def test_settings_load_environment(monkeypatch):
    from nasim.infrastructure.config import load_settings

    monkeypatch.setenv("NASIM_DATABASE_URL", "postgresql://test@localhost/nasim_test")
    assert load_settings().async_url == "postgresql+asyncpg://test@localhost/nasim_test"


def test_settings_require_postgresql(monkeypatch):
    from nasim.infrastructure.config import load_settings

    monkeypatch.setenv("NASIM_DATABASE_URL", "sqlite:///fallback.db")
    with pytest.raises(ValidationError):
        load_settings()
