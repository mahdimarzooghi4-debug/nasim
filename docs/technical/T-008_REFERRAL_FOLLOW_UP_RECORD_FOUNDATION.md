# T-008 — Referral Follow-up Record Foundation

Status: **Foundation-only**; SG-008. Reuse current Referral bounded context and TS-03 `CaseReferences` transaction-scoped current-assignment predicate. No new Case/Need ownership and no invented Referral lifecycle.

## Persistence contract

Append-only `ReferralFollowUpRecord` with UUID `id`, FK `referral_id`, database `recorded_at`, `recorded_by_actor_id`, `recorded_by_actor_type=HUMAN`, opaque free-text `note`, recording `reason`, `correlation_id`. No status, Provider response, success, approval, appointment, Service, satisfaction score, Need resolution, Outcome, due_at, medical priority, verified flag or training eligibility.

One Referral → many note records; no one-note-per-referral uniqueness. No correction/edit/delete endpoint. Original referral and Need remain unchanged. Migration `0007_referral_follow_up` follows `0006_provider_qreview` in one linear Alembic chain, with immutable trigger, evidence provenance constraints and deferred audit/outbox/idempotency integrity enforcement. Downgrade refuses live records/authorization dependencies.

## Command and API

- `POST /api/v1/referrals/{referral_id}/follow-up-records` body `expected_current_assignment_id`, `note`, `reason`, required Idempotency-Key. Result 201 `ReferralFollowUpView`.
- `GET /api/v1/referrals/{referral_id}/follow-up-records` with cursor/limit 1..100, paginated by database `recorded_at,id`.
- `GET /api/v1/referral-follow-up-records/{record_id}` returns bounded single note.

Technical capability vocabulary: `referral.follow_up.record.assigned`, `referral.follow_up.read.assigned`, `referral.follow_up.read.oversight`. No seeded grants or Role mapping. Creation requires HUMAN ActorType, record capability, current Case assignment and matching `expected_current_assignment_id`. AI denied even if granted. Read requires read capability and current assignment or explicit oversight; anonymous 401. System/Automation cannot write descriptive human notes. Cached POST retry rechecks current assignment/authorization. Race ordering: idempotency advisory lock → Referral reference → Case lock → assignment. New first-use races serialize, DB uniqueness is backstop.

The row + `referral.follow_up_recorded.v1` audit/outbox + idempotency commit atomically. Outbox contains only IDs/ActorType/timestamp/correlation; **neither note nor reason**. Shared Case timeline remains restricted to TS-03 event vocabulary and cannot leak Referral note. Backend must not route free text to AI Training/Outcome.

## Checks

PostgreSQL actual migrations and restricted runtime role; response/idempotency conflict and concurrency, stale caregiver, invalid/missing Referral, authorized list/detail and deny paths, cursor bounds, DB history/update/delete rejection, direct insert effects guard, atomic rollback, OpenAPI exact inventory and disposable Container Smoke. Hosted Stage unavailable. No AI, external service, UI or Production.
