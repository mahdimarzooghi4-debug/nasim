# T-005 — Provider Qualification Evidence Foundation

- **Status:** FOUNDATION ONLY
- **Business gate:** SG-005
- **Decision:** D-0132

Architecture remains the current Python 3.12 / FastAPI / PostgreSQL / async SQLAlchemy / Alembic
modular monolith and existing TS-05 ActorContext authorization boundary.

## Bounded-context rule

Extend the existing `provider_registry` bounded context. Do not import Case/Referral persistence
models and do not create cross-context foreign keys.

The only required relationship is internal to the Provider Registry bounded context:

`ProviderCandidateRecord 1 → N ProviderQualificationEvidenceRecord`

Multiplicity is evidence history only and does not imply business qualification.

## Aggregate / record

Add `ProviderQualificationEvidenceRecord` with only:

- `id: UUID`
- `provider_candidate_id: UUID`
- `evidence_label: str`
- `evidence_reference: str`
- `recorded_at: timestamptz`
- `recorded_by_actor_id: str`
- `recorded_by_actor_type: HUMAN|SYSTEM|AI|AUTOMATION`
- `reason: str`
- `correlation_id: str`

`evidence_label` and `evidence_reference` are descriptive/opaque fields only. They MUST NOT become
a qualification taxonomy, document type enum, storage URL contract or credential-verification result.

Forbidden fields in this Slice include:

- qualified / approved / active / status;
- result / decision / score / threshold;
- valid / verified / expired;
- reviewer / approver;
- provider_type;
- service/service_family;
- geography;
- capacity;
- contract;
- licence/credential semantics;
- case_id / elder_id / referral_id;
- ranking / pricing / settlement.

## Integrity

- Evidence row is immutable.
- No UPDATE/DELETE API.
- DB-level history protection.
- Candidate FK must point to an existing Provider Candidate.
- Nonblank label/reference/reason/actor/correlation.
- Duplicate label/reference values are allowed.
- No evidence record may mutate the candidate row.
- Evidence correction/replacement semantics remain OPEN.

## Authorization

Register only technical permission vocabulary:

- `provider_qualification_evidence.record`
- `provider_qualification_evidence.read`

Do not seed RolePermissionGrant or ActorRoleAssignment.

Record requires `provider_qualification_evidence.record`.
Read requires `provider_qualification_evidence.read`.

AI must fail closed for record operations even if an erroneous explicit grant exists.
No new authentication adapter, self-asserted header, JWT, IdP or dev bypass is allowed.

## Command / queries

Command:

- `RecordProviderQualificationEvidence(provider_candidate_id, evidence_label, evidence_reference, reason)`

Queries:

- list evidence for one Provider Candidate, cursor-paginated;
- get evidence by ID.

## HTTP

- `POST /api/v1/provider-candidates/{candidate_id}/qualification-evidence` → 201
- `GET /api/v1/provider-candidates/{candidate_id}/qualification-evidence`
- `GET /api/v1/provider-qualification-evidence/{evidence_id}`

All mutations require `Idempotency-Key`.

Do not add review/verify/qualify/approve/reject/activate/suspend/expire/replace endpoints.

## Transactional effects

Recording evidence persists in one transaction:

- ProviderQualificationEvidenceRecord
- AuditEntry
- OutboxEvent
- IdempotencyRecord

Event:

`provider.qualification_evidence_recorded.v1`

The event payload must contain only identifiers/provenance required to trace the event.
Do not copy `evidence_label` or `evidence_reference` into the event payload.

Shared non-Case audit/outbox constraints introduced by Sprint 004 must be expanded only for the exact
new Provider Qualification Evidence shapes. They must continue to reject unrelated NULL-`case_id`
audit/outbox effects.

## Idempotency / concurrency

Scope idempotency by trusted actor identity/type + operation + candidate + key.

- same key + same payload → same result;
- same key + different payload → 409;
- first-use races must serialize using the existing PostgreSQL advisory-lock pattern.

Do not make `evidence_reference` unique.

## Migration

Create one linear migration after:

`0004_provider_candidate`

No migration branch/fork.

Runtime role receives only bounded SELECT/INSERT needed for this foundation and no destructive privilege.

## Explicit exclusions

No Qualification Decision, review result, activation, Provider Type, Service mapping, geography
eligibility, capacity, Provider Selection, Referral response, Service Delivery, Provider access,
ranking/score, finance, external document storage/integration, UI, Hosted Stage or Production behavior.
