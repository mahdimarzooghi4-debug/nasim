# T-006 — Provider Qualification Review Request Foundation

- **Status:** FOUNDATION ONLY
- **Business gate:** SG-006
- **Decision:** D-0133

Architecture remains the current Python 3.12 / FastAPI / PostgreSQL / async SQLAlchemy / Alembic
modular monolith and existing TS-05 ActorContext authorization boundary.

## Bounded-context rule

Extend the existing `provider_registry` bounded context. Do not import Case/Referral persistence
models and do not create cross-context foreign keys.

## Record

Add `ProviderQualificationReviewRequestRecord` with only:

- `id: UUID`
- `provider_candidate_id: UUID`
- `requested_at: timestamptz`
- `requested_by_actor_id: str`
- `requested_by_actor_type: HUMAN|SYSTEM|AI|AUTOMATION`
- `reason: str`
- `correlation_id: str`

Forbidden fields:

- status/state;
- reviewer/approver;
- assigned_to;
- decision/result;
- qualified/approved/active;
- score/threshold;
- evidence_complete/evidence_sufficient;
- SLA/due_at;
- provider_type;
- service/service_family;
- geography/capacity;
- contract;
- case/elder/referral;
- ranking/pricing/settlement.

## Integrity

- Request row is immutable.
- No UPDATE/DELETE API.
- DB-level history protection.
- Candidate FK must point to an existing Provider Candidate.
- Nonblank reason/actor/correlation.
- Repeated review requests are allowed.
- No request may mutate Candidate or Qualification Evidence.
- No active-request uniqueness rule.

## Authorization

Register only:

- `provider_qualification_review.request`
- `provider_qualification_review.read`

Do not seed RolePermissionGrant or ActorRoleAssignment.

Request requires `provider_qualification_review.request`.
Read requires `provider_qualification_review.read`.

AI must fail closed for request creation even if an erroneous explicit grant exists.

## Command / queries

Command:

- `RequestProviderQualificationReview(provider_candidate_id, reason)`

Queries:

- list review requests for one Provider Candidate, cursor-paginated;
- get review request by ID.

## HTTP

- `POST /api/v1/provider-candidates/{candidate_id}/qualification-review-requests` → 201
- `GET /api/v1/provider-candidates/{candidate_id}/qualification-review-requests`
- `GET /api/v1/provider-qualification-review-requests/{request_id}`

All mutations require `Idempotency-Key`.

Do not add assign/review/decide/qualify/approve/reject/activate/close/reopen endpoints.

## Transactional effects

Request creation persists atomically:

- ProviderQualificationReviewRequestRecord
- AuditEntry
- OutboxEvent
- IdempotencyRecord

Event:

`provider.qualification_review_requested.v1`

Payload contains identifiers/provenance only. Do not copy reason or qualification evidence into the
event payload.

Shared NULL-`case_id` audit/outbox constraints must be expanded only for the exact new review-request
event/audit shapes.

## Idempotency / concurrency

Scope by trusted actor identity/type + candidate + key.

- same key + same payload → same result;
- same key + different payload → 409;
- first-use races serialize using existing PostgreSQL advisory lock pattern.

## Migration

Create one linear migration after `0005_provider_qe`.

No migration fork.

Runtime role receives only bounded SELECT/INSERT required for this foundation.

## Explicit exclusions

No reviewer assignment, qualification decision, review outcome, approval, activation, Provider Type,
Service mapping, Provider Selection, Capacity, Referral response, Provider data access, finance,
external integration, UI, Hosted Stage or Production behavior.
