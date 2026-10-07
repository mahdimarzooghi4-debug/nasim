# PB-001 — TS-03 Core Case / Journey Product Backlog

- **Status:** ACCEPTED FOR SPRINT PLANNING
- **Stage:** Scrum / Product Backlog
- **Date:** 2026-10-07
- **Source basis:** D-0128 + T-001 + TG-001
- **Scope:** TS-03 backend-first implementation

## Backlog operating rules

- Business exclusions from SG-001/T-001 are hard constraints.
- Backend/contracts/tests first.
- no final named RBAC mapping.
- no Referral/Provider/Outcome/AI/Enrollment implementation.
- all mutation paths are idempotent, audited and transactional.
- history must be non-destructive.

## BL-001 — Backend foundation

Deliver:
- Python 3.12 FastAPI application
- async SQLAlchemy + PostgreSQL integration
- Alembic migration foundation
- Pydantic settings/contracts
- health endpoint
- Pytest/Ruff/Pyright configuration

Acceptance:
- app starts with configured database
- migrations upgrade/downgrade in test environment
- quality commands run deterministically
- no business endpoint bypasses application services

Priority: P0

## BL-002 — ActorContext and fail-closed capability guard

Deliver:
- ActorContext contract
- HUMAN/SYSTEM/AI/AUTOMATION actor provenance vocabulary
- capability guard dependency
- assigned-caregiver predicate
- oversight/assignment capability boundary

Acceptance:
- missing actor context is denied
- job titles are not permissions
- AI/Provider/Family/Employer receive no TS-03 grants by default
- tests can inject ActorContext without creating a production auth bypass

Priority: P0

## BL-003 — Case creation with initial caregiver assignment

Deliver:
- ElderCase aggregate
- post-enrollment creation contract
- case profile first revision
- initial caregiver assignment in same transaction
- idempotent POST `/api/v1/cases`

Acceptance:
- upstream enrollment reference required
- initial caregiver required
- assignment-manage capability required
- Case + profile revision + assignment + audit + outbox commit atomically
- duplicate same request returns same accepted result
- reused idempotency key with different payload returns 409

Priority: P0

## BL-004 — Caregiver reassignment and assignment history

Deliver:
- reassignment command/API
- current assignment query
- assignment history
- optimistic stale guard using expected current assignment id

Acceptance:
- reason required
- actor/time recorded
- previous assignment retained
- at most one active assignment
- stale/concurrent reassignment returns 409 and writes nothing partial

Priority: P0

## BL-005 — Contact information revisions

Deliver:
- logical contact record
- append-only contact revisions
- add/correct APIs
- current contact read model

Acceptance:
- correction reason required
- prior revision remains readable/auditable
- assigned caregiver access enforced
- unsupported broader access denied

Priority: P1

## BL-006 — Contact and Monitoring interactions

Deliver:
- immutable interaction records
- interaction types limited to CONTACT and MONITORING
- record/correct/list APIs

Acceptance:
- no Service/Referral interaction type
- correction creates superseding record
- stale correction returns 409
- actor provenance and audit persisted

Priority: P0

## BL-007 — Observation / Need capture

Deliver:
- immutable Observation/Need records
- record types limited to OBSERVATION and NEED_CAPTURE
- record/correct/list APIs

Acceptance:
- no Need taxonomy/severity/eligibility/referral/outcome fields
- corrections are append-only
- assigned caregiver capability required
- provenance maintained

Priority: P0

## BL-008 — Audit and transactional outbox

Deliver:
- append-only audit_entry persistence
- outbox_event persistence
- domain event contracts from T-001

Acceptance:
- every accepted mutation writes audit + outbox in same transaction
- rollback removes all partial business/audit/outbox writes
- normal application role cannot update/delete audit history
- events carry lineage/provenance but no AI-training implication

Priority: P0

## BL-009 — Case workspace and timeline read models

Deliver:
- GET Case
- GET workspace
- assignment history
- contacts
- interactions
- observations
- combined chronological timeline with cursor pagination

Acceptance:
- only TS-03 data is exposed
- access predicates enforced on every read
- no Provider/Outcome/AI fields appear

Priority: P1

## BL-010 — OpenAPI and error contract hardening

Deliver:
- documented request/response schemas
- stable error codes
- OpenAPI contract tests

Required conflict/error examples:
- `CASE_ASSIGNMENT_CHANGED`
- `STALE_RECORD_REVISION`
- `IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD`
- `CAPABILITY_REQUIRED`
- `ASSIGNED_CAREGIVER_REQUIRED`

Acceptance:
- OpenAPI exposes only intended TS-03 routes
- error codes are deterministic and tested

Priority: P1

## BL-011 — Security, concurrency and rollback test matrix

Deliver automated coverage for:
- authorization denial
- cross-Case access denial
- non-assigned caregiver denial
- concurrent reassignment
- stale correction
- idempotency races
- audit/outbox atomicity
- revision preservation
- no destructive history path

Acceptance:
- all critical negative-path tests pass
- concurrency tests prove one accepted winner where required
- no test depends on production auth bypass

Priority: P0

## BL-012 — Developer/operations documentation

Deliver:
- local run instructions
- migration commands
- test/quality commands
- TS-03 boundary notes
- explicit list of non-goals

Acceptance:
- a new developer/Codex session can start the backend, migrate DB and run tests from repository documentation

Priority: P2

## Definition of Ready for Sprint

Backlog item is Sprint-ready only if:
- traced to T-001
- acceptance criteria are testable
- no unresolved Business decision is required
- no excluded domain behavior is implied

## Definition of Done for TS-03 code sprint

- BL-001…BL-011 accepted
- migration and test suite green
- API/OpenAPI contract tests green
- concurrency/idempotency/security negative paths green
- code review complete
- no scope creep into excluded slices

BL-012 may finish in the same sprint or immediately before Code Review completion.

## Recommended sprint

One focused backend Sprint can implement BL-001…BL-012 because all items belong to one bounded aggregate and one database transaction model.

Next artifact: Sprint plan and Code-entry gate.