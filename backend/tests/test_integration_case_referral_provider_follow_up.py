"""Real HTTP / PostgreSQL integration across independently governed contexts."""

import os
from datetime import UTC, datetime
from uuid import UUID, uuid4

import httpx
import pytest
from pydantic import PostgresDsn
from sqlalchemy import select

from nasim.api.app import create_app, get_actor
from nasim.domain.contracts import CreateCase, ReassignCaregiver, RecordObservation
from nasim.identity_context.contracts import ActorContext, ActorType
from nasim.infrastructure.config import Settings
from nasim.infrastructure.models import OutboxEvent
from nasim.provider_registry.contracts import (
    RecordProviderQualificationEvidence,
    RegisterProviderCandidate,
    RequestProviderQualificationReview,
)
from nasim.provider_registry.service import (
    ProviderCandidates,
    ProviderQualificationEvidence,
    ProviderQualificationReviewRequests,
)

pytestmark = pytest.mark.integration


async def test_real_care_journey_and_provider_boundary_with_caregiver_handover(
    service, manager, caregiver, admin_engine
):
    created = await service.mutate(
        "create",
        CreateCase(
            upstream_enrollment_ref="authorized-external-enrollment-ref",
            elder_reference="opaque-elder-ref",
            initial_caregiver_actor_id=caregiver.actor_id,
        ),
        manager,
        "int-case",
    )
    case_id = UUID(created["case"]["id"])
    assignment_id = UUID(created["current_assignment"]["id"])
    need = await service.mutate(
        "observation_add",
        RecordObservation(
            expected_current_assignment_id=assignment_id,
            record_type="NEED_CAPTURE",
            occurred_at=datetime.now(UTC),
            content="Sensitive Need not for Provider registry or Outbox",
        ),
        caregiver,
        "int-need",
        case_id,
    )

    care_actor = caregiver.model_copy(
        update={
            "capabilities": caregiver.capabilities
            | {
                "referral.create.assigned",
                "referral.read.assigned",
                "referral.follow_up.record.assigned",
                "referral.follow_up.read.assigned",
            }
        }
    )
    provider_actor = ActorContext(
        actor_id="provider-registry-inspector",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset(
            {
                "provider_candidate.register",
                "provider_candidate.read",
                "provider_qualification_evidence.record",
                "provider_qualification_evidence.read",
                "provider_qualification_review.request",
                "provider_qualification_review.read",
            }
        ),
        correlation_id="integration-provider",
    )

    candidates = ProviderCandidates(service.sessions)
    evidence = ProviderQualificationEvidence(service.sessions)
    reviews = ProviderQualificationReviewRequests(service.sessions)
    candidate = await candidates.register(
        RegisterProviderCandidate(
            display_name="Unqualified candidate — no service rights",
            reason="Descriptive record only",
        ),
        provider_actor,
        "int-candidate",
    )
    candidate_id = UUID(candidate["id"])
    await evidence.record(
        candidate_id,
        RecordProviderQualificationEvidence(
            evidence_label="Document received",
            evidence_reference="opaque-document",
            reason="Submitted, not verified",
        ),
        provider_actor,
        "int-evidence",
    )
    await reviews.request(
        candidate_id,
        RequestProviderQualificationReview(reason="Please inspect, not approve"),
        provider_actor,
        "int-request",
    )

    app = create_app(
        Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"]))
    )
    referral_path = f"/api/v1/cases/{case_id}/referrals"
    provider_path = (
        f"/api/v1/provider-candidates/{candidate_id}/qualification-review-workspace"
    )
    note = "Sensitive human referral follow-up note — never a service success"
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            assert (await client.get(provider_path)).status_code == 401
            assert (await client.get(referral_path)).status_code == 401

            app.dependency_overrides[get_actor] = lambda: care_actor
            recorded = await client.post(
                referral_path,
                json={
                    "source_need_observation_id": need["id"],
                    "expected_current_assignment_id": str(assignment_id),
                    "reason": "Record-only referral, not dispatched",
                },
                headers={"Idempotency-Key": "int-referral"},
            )
            assert recorded.status_code == 201, recorded.text
            referral_id = recorded.json()["id"]
            follow_path = f"/api/v1/referrals/{referral_id}/follow-up-records"
            follow = await client.post(
                follow_path,
                json={
                    "expected_current_assignment_id": str(assignment_id),
                    "note": note,
                    "reason": "Human follow-up activity",
                },
                headers={"Idempotency-Key": "int-follow-up"},
            )
            assert follow.status_code == 201, follow.text
            assert (await client.get(follow_path)).json()["items"][0]["note"] == note
            assert (await client.get(provider_path)).status_code == 403

            timeline = await client.get(f"/api/v1/cases/{case_id}/timeline")
            assert timeline.status_code == 200
            assert note not in timeline.text
            assert all(item["action"].startswith("case.") for item in timeline.json()["items"])

            app.dependency_overrides[get_actor] = lambda: provider_actor
            workspace = await client.get(provider_path)
            assert workspace.status_code == 200, workspace.text
            assert workspace.json()["candidate"]["id"] == str(candidate_id)
            assert len(workspace.json()["evidence"]["items"]) == 1
            assert len(workspace.json()["review_requests"]["items"]) == 1
            assert note not in workspace.text
            assert "decision" not in workspace.json()
            assert (await client.get(follow_path)).status_code == 403
            assert (await client.get(referral_path)).status_code == 403

            app.dependency_overrides[get_actor] = lambda: care_actor
            await service.mutate(
                "reassign",
                ReassignCaregiver(
                    expected_current_assignment_id=assignment_id,
                    caregiver_actor_id="successor-caregiver",
                    reason="Explicit managed handover",
                ),
                manager,
                "int-handover",
                case_id,
            )
            assert (await client.get(follow_path)).status_code == 403
            cached = await client.post(
                follow_path,
                json={
                    "expected_current_assignment_id": str(assignment_id),
                    "note": note,
                    "reason": "Human follow-up activity",
                },
                headers={"Idempotency-Key": "int-follow-up"},
            )
            assert cached.status_code == 403
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()

    async with admin_engine.connect() as conn:
        event = await conn.scalar(
            select(OutboxEvent.payload).where(
                OutboxEvent.event_type == "referral.follow_up_recorded.v1"
            )
        )
        assert event is not None
        assert note not in str(event)
        assert "note" not in event and "reason" not in event


async def test_cross_context_unauthorized_actor_has_no_implicit_combined_access(service):
    """Even the same human identity must have grants for each context separately."""
    from nasim.domain.errors import DomainError
    from nasim.provider_registry.service import ProviderQualificationReviewWorkspace
    from nasim.referral.follow_up import ReferralFollowUps

    actor = ActorContext(
        actor_id="limited-human",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset({"referral.read.assigned", "provider_candidate.read"}),
        correlation_id="integration-limited",
    )
    with pytest.raises(DomainError) as provider_error:
        await ProviderQualificationReviewWorkspace(service.sessions).read(uuid4(), actor)
    assert provider_error.value.code == "CAPABILITY_REQUIRED"
    with pytest.raises(DomainError) as referral_error:
        await ReferralFollowUps(service.sessions).list(uuid4(), actor)
    assert referral_error.value.code == "CAPABILITY_REQUIRED"
