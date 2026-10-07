# T-004 — Provider Candidate Registry Foundation

Status: **FOUNDATION ONLY** under SG-004.

Architecture remains the existing modular monolith with Python 3.12, FastAPI,
PostgreSQL, async SQLAlchemy, Alembic and the existing ActorContext/TS-05 authorization boundary.

## Bounded context

Create a separate `provider_registry` bounded context. It must not import Referral persistence
models or Case persistence models and must not create cross-context foreign keys.

## Aggregate

`ProviderCandidateRecord` only:

- `id: UUID`
- `display_name: str`
- `registered_at: timestamptz`
- `registered_by_actor_id: str`
- `registered_by_actor_type: HUMAN|SYSTEM|AI|AUTOMATION`
- `reason: str`
- `correlation_id: str`

The internal UUID is the canonical record identity. `display_name` is descriptive only and
MUST NOT be treated as a unique identity key.

Explicitly forbidden fields in this slice: status, active, approved, provider_type,
service/service_family, geography, capacity, credential, qualification, contract, ranking,
score, price, settlement, Case/Elder reference, Referral reference.

## Integrity

- append-only / immutable record;
- no UPDATE/DELETE API;
- DB-level history protection;
- nonblank display_name/reason/actor/correlation;
- no uniqueness assumption on display_name;
- correction/deduplication semantics remain OPEN.

## Authorization

Register technical permission vocabulary only:

- `provider_candidate.register`
- `provider_candidate.read`

No RolePermissionGrant or ActorRoleAssignment seed.

Registration requires `provider_candidate.register`; reads require
`provider_candidate.read`. Role title alone never grants either.

AI MUST fail closed for registration even if an erroneous grant exists. No new
authentication adapter/header/JWT/IdP is introduced.

## Commands / queries

Command:
- `RegisterProviderCandidate(display_name, reason)`

Queries:
- list provider candidates, cursor-paginated;
- get provider candidate by ID.

## HTTP

- `POST /api/v1/provider-candidates` → 201
- `GET /api/v1/provider-candidates`
- `GET /api/v1/provider-candidates/{candidate_id}`

All mutations require `Idempotency-Key`.

Do not add activate/approve/reject/suspend/qualify/map-service/select/capacity/contract endpoints.

## Transactional effects

Registration persists in one transaction:

- ProviderCandidateRecord
- AuditEntry
- OutboxEvent
- IdempotencyRecord

Event: `provider.candidate_registered.v1`.

Event payload is identifier/provenance-only; do not copy display name unless an existing
platform contract requires it.

## Concurrency / idempotency

Scope idempotency by trusted actor identity/type + operation + key. Same key/same payload returns
the same record; same key/different payload returns 409. First-use races must be serialized using
the existing PostgreSQL pattern and backed by DB uniqueness.

## Migration / runtime

Create the next linear Alembic migration after `0003_referral`; do not fork migration history.
Runtime serving role receives only the minimum SELECT/INSERT permissions required for this
foundation and no destructive privilege.

## Explicit exclusions

No operational Provider Registry, Provider Type, qualification, activation, Service Catalog,
Service mapping, Referral destination/selection, acceptance/rejection, Capacity, Service Delivery,
Completion Evidence, Provider data access, ranking, quality score, contract, finance, external
integration, UI, Hosted Stage or Production behavior.
