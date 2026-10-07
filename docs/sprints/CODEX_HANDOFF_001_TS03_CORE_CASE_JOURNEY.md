# CODEX-HANDOFF-001 — Sprint 001 TS-03 Core Case / Journey

- **Status:** READY FOR CODEX
- **Date:** 2026-10-07
- **Repository:** `mahdimarzooghi4-debug/nasim`
- **Target branch:** `sprint-001-ts03-core-case-journey`
- **Base:** current `main` after D-0129

## Read first

- `docs/DECISIONS.md`
- `docs/business/gates/SG-001_TS03_TECHNICAL_ENTRY_GATE_RECORD.md`
- `docs/technical/T-001_TS03_CORE_CASE_JOURNEY_TECHNICAL_BASELINE.md`
- `docs/technical/TG-001_TS03_TECHNICAL_REVIEW_BACKLOG_ENTRY_GATE.md`
- `docs/backlog/PB-001_TS03_CORE_CASE_JOURNEY_PRODUCT_BACKLOG.md`
- `docs/sprints/SPRINT-001_TS03_CORE_CASE_JOURNEY_FOUNDATION.md`

## Mission

Implement Sprint 001 exactly within TS-03 scope.

Implement BL-001…BL-012 with backend/contracts/tests first.

## Non-negotiable boundaries

- TS-03 begins after Enrollment.
- no Enrollment eligibility engine.
- no Case closure/status state machine.
- no Referral/Service/Provider/Outcome/Reassessment/Emergency implementation.
- no AI runtime or Dataset Builder.
- no named job-title RBAC mapping.
- no generic arbitrary edit API.
- no silent overwrite.
- Provider/Family/Employer/AI access denied by default for TS-03.
- all accepted mutations write business state + audit + outbox atomically.
- stale mutations fail closed.

## Technical stack

- Python 3.12
- FastAPI
- PostgreSQL
- async SQLAlchemy 2.x
- Alembic
- Pydantic v2
- Pytest
- Ruff
- Pyright

Do not pin dependency versions by guess. Resolve currently compatible versions during implementation and commit the lock/config used.

## Required implementation order

1. backend project skeleton and quality tooling
2. database/config/Alembic
3. ActorContext + capability guard
4. persistence models and DB constraints
5. application/domain services
6. Case creation + initial assignment
7. reassignment/history
8. contacts + revisions
9. interactions + corrections
10. observations/need capture + corrections
11. audit + outbox
12. reads/workspace/timeline
13. REST/OpenAPI
14. concurrency/idempotency/security tests
15. run/developer docs

## Required API and error contracts

Use exactly the T-001 API surface unless a repository-level technical contradiction is discovered.

Preserve at least these stable error codes:
- `CASE_ASSIGNMENT_CHANGED`
- `STALE_RECORD_REVISION`
- `IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD`
- `CAPABILITY_REQUIRED`
- `ASSIGNED_CAREGIVER_REQUIRED`

## Database requirements

Create migrations for:
- elder_case
- case_profile_revision
- contact_point_revision
- case_assignment
- case_interaction
- case_observation
- audit_entry
- outbox_event
- idempotency_record

Enforce:
- at most one active assignment per Case
- revision uniqueness
- idempotency uniqueness
- lineage FKs
- no orphan children
- protected audit history

## Required negative-path tests

- missing ActorContext
- insufficient capability
- non-assigned caregiver
- Provider/Family/Employer/AI access
- stale reassignment
- concurrent reassignment
- stale correction
- missing correction reason
- idempotency key payload conflict
- transaction rollback with no partial audit/outbox
- excluded-scope endpoint absence

## Delivery rules

- work only on `sprint-001-ts03-core-case-journey`
- keep changes reviewable and coherent
- run full test/quality suite before reporting completion
- do not merge to `main` automatically
- after implementation, stop at **Code Review** and report exact commit SHA, tests and any deviations

## If blocked

If implementation reveals a missing Business rule, do not invent it. Stop that path, document the exact blocker, and keep unrelated implementation moving where safe.

## Completion report expected from Codex

- branch HEAD
- changed files/modules
- migration identifiers
- test counts/results
- Ruff/Pyright status
- OpenAPI/contract test status
- any explicit blocker/deviation
- confirmation that excluded scopes were not implemented

Next process stage after successful implementation: **Code Review**.