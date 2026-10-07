# SPRINT-001 — TS-03 Core Case / Journey Foundation

- **Status:** READY FOR CODE
- **Stage:** Sprint
- **Date:** 2026-10-07
- **Source basis:** D-0128 + PB-001 + T-001 + TG-001
- **Goal:** implement the complete backend foundation for the bounded TS-03 Case/Journey slice with fail-closed access, append-only correction history, concurrency safety, audit and transactional outbox.

## Sprint scope

Included backlog:
- BL-001 Backend foundation
- BL-002 ActorContext and capability guard
- BL-003 Case creation + initial assignment
- BL-004 Reassignment + history
- BL-005 Contact revisions
- BL-006 Contact/Monitoring interactions
- BL-007 Observation/Need capture
- BL-008 Audit + transactional outbox
- BL-009 Workspace/timeline reads
- BL-010 OpenAPI/error contracts
- BL-011 security/concurrency/rollback tests
- BL-012 developer/operations documentation

## Build order

1. repository/backend skeleton + quality tooling
2. database + migrations
3. ActorContext/capability guard
4. domain models + services
5. Case creation/assignment
6. interaction/observation/contact revisions
7. audit/outbox
8. read models
9. API/OpenAPI
10. concurrency/idempotency/security tests
11. documentation

## Non-negotiable constraints

- TS-03 starts after Enrollment.
- no Enrollment eligibility engine.
- no Case status/closure lifecycle.
- no Referral/Service/Provider/Outcome/AI runtime.
- no named job-title RBAC mapping.
- no silent overwrite.
- no generic arbitrary edit endpoint.
- no production auth bypass.
- all accepted mutations write business state + audit + outbox atomically.
- stale mutations fail closed.
- Provider/Family/Employer/AI access is denied by default for this slice.

## Required migration objects

- elder_case
- case_profile_revision
- contact_point_revision
- case_assignment
- case_interaction
- case_observation
- audit_entry
- outbox_event
- idempotency_record

## Required API surface

Mutations:
- POST `/api/v1/cases`
- POST `/api/v1/cases/{case_id}/profile/corrections`
- POST `/api/v1/cases/{case_id}/contacts`
- POST `/api/v1/cases/{case_id}/contacts/{logical_contact_id}/corrections`
- POST `/api/v1/cases/{case_id}/interactions`
- POST `/api/v1/cases/{case_id}/interactions/{interaction_id}/corrections`
- POST `/api/v1/cases/{case_id}/observations`
- POST `/api/v1/cases/{case_id}/observations/{observation_id}/corrections`
- POST `/api/v1/cases/{case_id}/reassignments`

Reads:
- GET `/api/v1/cases/{case_id}`
- GET `/api/v1/cases/{case_id}/workspace`
- GET `/api/v1/cases/{case_id}/assignments`
- GET `/api/v1/cases/{case_id}/contacts`
- GET `/api/v1/cases/{case_id}/interactions`
- GET `/api/v1/cases/{case_id}/observations`
- GET `/api/v1/cases/{case_id}/timeline`

## Required error contracts

- 401/403 fail closed for missing/insufficient actor context
- 409 `CASE_ASSIGNMENT_CHANGED`
- 409 `STALE_RECORD_REVISION`
- 409 `IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD`
- 403 `CAPABILITY_REQUIRED`
- 403 `ASSIGNED_CAREGIVER_REQUIRED`
- 422 validation for malformed inputs

## Required tests before Code Review

- happy-path case creation + initial assignment
- unauthorized creation denied
- non-assigned caregiver denied
- assigned caregiver allowed only bounded actions
- oversight actor bounded access
- default denial for Family/Provider/Employer/AI
- reassignment reason required
- stale/concurrent reassignment safety
- contact correction revision preservation
- interaction correction revision preservation
- observation correction revision preservation
- correction reason required
- stale correction safety
- idempotent retry
- idempotency conflict
- transaction rollback includes audit/outbox
- OpenAPI route/contract snapshot
- no excluded-scope endpoint exists

## Code Review gate

Code Review must verify:
- T-001 compliance
- no Business assumption added
- no scope creep
- DB constraints enforce invariants
- tests cover negative paths
- migration downgrade path is safe for pre-production development
- audit/outbox integrity

## Stage boundary

After Code Review, move to Stage only with a separate Stage admission artifact.

## Code entry status

All prerequisite artifacts exist:
- Business slice gate: SG-001 PASS WITH EXPLICIT DEFERRAL
- Technical baseline: T-001 ACCEPTED
- Technical gate: TG-001 PASSED
- Product backlog: PB-001 ACCEPTED FOR SPRINT PLANNING
- Sprint plan: SPRINT-001 READY FOR CODE

**Next process step: Code.**

Per project operating rule, implementation must now move to Codex.