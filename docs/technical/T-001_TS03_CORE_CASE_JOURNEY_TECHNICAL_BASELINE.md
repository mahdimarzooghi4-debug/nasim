# T-001 — TS-03 Core Case / Journey Technical Baseline

- **Status:** ACCEPTED TECHNICAL BASELINE
- **Stage:** Technical — TS-03
- **Date:** 2026-10-07
- **Source basis:** SG-001 + D-0012 + D-0013 + D-0014 + D-0015 + D-0021 + D-0028 + D-0119…D-0127
- **Scope:** backend-first technical foundation for post-enrollment Case/Profile, Contact, Monitoring, Observation/Need capture, assignment/history, correction history, audit and provenance.

> This baseline does not implement Referral, Provider, Outcome, AI runtime, Dataset Builder, Enrollment or final RBAC.

## 1. Architecture decision

TS-03 uses a **modular monolith** with explicit domain/application/infrastructure/API boundaries.

Rationale:
- first slice is one bounded domain
- strong transactional consistency is required for assignment/history/audit/outbox
- no current evidence requires microservices
- later slices can consume stable domain contracts/events without premature distribution

## 2. Technical stack

Backend:
- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy 2.x async
- Alembic
- Pydantic v2

Quality:
- Pytest
- Ruff
- Pyright

API:
- REST/JSON
- OpenAPI generated from FastAPI contracts

Deployment/runtime topology is not frozen beyond one backend service + PostgreSQL for this slice.

Frontend is **not part of TS-03 first code sprint**. The first implementation establishes backend contracts and tests.

## 3. Module boundaries

Recommended source modules:
- `identity_context` — abstract authenticated actor context only; no final RBAC registry
- `casework` — Case/Profile aggregate and application commands/queries
- `assignment` — current caregiver assignment + history/reassignment rules
- `interaction` — Contact/Monitoring records
- `observation` — Observation / Need capture
- `audit` — immutable business audit trail
- `outbox` — transactional domain-event persistence

Cross-module imports must use public service/contracts, not persistence internals.

## 4. Core aggregate boundary

Primary aggregate: **ElderCase**.

Rules:
- Case exists only after an upstream Enrollment reference is supplied.
- TS-03 does not validate Enrollment Eligibility.
- Case has exactly one current caregiver assignment after creation.
- caregiver assignment does not imply permission; permission is evaluated from ActorContext capabilities.
- Case has no invented lifecycle/status machine in TS-03.
- Case closure/suspension is not implemented.

## 5. Case creation technical rule

To avoid an ownerless Case, Case creation and initial caregiver assignment are one transaction.

Creation requires:
- `upstream_enrollment_ref`
- `elder_reference`
- `initial_caregiver_actor_id`
- authenticated actor with abstract `case.assignment.manage` capability
- idempotency key

TS-03 does not verify the business truth of the upstream enrollment; it records the supplied upstream reference and provenance.

## 6. Persistence model

### 6.1 elder_case
- `id` UUID primary key
- `upstream_enrollment_ref` text, required
- `created_at` timestamptz, required
- `created_by_actor_id` text, required
- `created_by_actor_type` enum/string constrained to HUMAN/SYSTEM/AI/AUTOMATION vocabulary

No case status column is introduced in TS-03.

### 6.2 case_profile_revision
Append-only revisions for profile/reference facts:
- `id` UUID
- `case_id` UUID
- `revision_no` integer
- `elder_reference` text
- `supersedes_revision_id` nullable UUID
- `correction_reason` nullable text
- `recorded_at` timestamptz
- `recorded_by_actor_id` text
- `recorded_by_actor_type`

Current profile is the highest valid revision. Previous revisions are never updated/deleted by normal application commands.

### 6.3 contact_point_revision
Append-only logical contact records:
- `id` UUID
- `case_id` UUID
- `logical_contact_id` UUID
- `revision_no` integer
- `contact_kind` text
- `contact_value` text
- `supersedes_revision_id` nullable UUID
- correction metadata + actor provenance

No fixed phone/email/address taxonomy is invented in TS-03; `contact_kind` is a bounded technical string until a later business catalog exists.

### 6.4 case_assignment
Assignment history:
- `id` UUID
- `case_id` UUID
- `caregiver_actor_id` text
- `started_at` timestamptz
- `ended_at` nullable timestamptz
- `assigned_by_actor_id` text
- `assigned_by_actor_type`
- `reason` text, required for reassignment/substitution; creation may use `INITIAL_ASSIGNMENT` technical reason

Constraint: at most one active assignment (`ended_at IS NULL`) per Case.

### 6.5 case_interaction
Immutable interaction records:
- `id` UUID
- `case_id` UUID
- `interaction_type` = CONTACT | MONITORING
- `occurred_at` timestamptz
- `content` text
- `recorded_at` timestamptz
- actor provenance
- `supersedes_interaction_id` nullable UUID for correction
- `correction_reason` nullable text

### 6.6 case_observation
Immutable Observation / Need capture:
- `id` UUID
- `case_id` UUID
- `record_type` = OBSERVATION | NEED_CAPTURE
- `occurred_at` timestamptz
- `content` text
- `recorded_at` timestamptz
- actor provenance
- `supersedes_observation_id` nullable UUID
- `correction_reason` nullable text

No Need taxonomy, severity, eligibility, referral decision or outcome field is introduced.

### 6.7 audit_entry
Append-only audit:
- actor id/type
- action
- resource type/id
- case id
- timestamp
- request/correlation id
- before/after reference when applicable
- reason when required

Application role must not UPDATE/DELETE existing audit rows.

### 6.8 outbox_event
Transactional outbox persisted in the same database transaction as domain changes.

TS-03 persists outbox events but does not require a broker/transport implementation yet.

## 7. Correction model

Technical choice: **append-only superseding revisions**.

Rules:
- corrections create a new revision/record
- prior row is retained
- new row references the superseded row
- correction reason is mandatory
- actor/time are mandatory
- provenance is copied/preserved and new correction provenance is added
- normal application API has no destructive edit/delete command for historical records

This satisfies D-0125 without choosing event sourcing.

## 8. Actor and authorization contract

Define an injected `ActorContext`:
- `actor_id`
- `actor_type` = HUMAN | SYSTEM | AI | AUTOMATION
- `capabilities: set[str]`
- `correlation_id`

TS-03 capability names:
- `case.create`
- `case.read.assigned`
- `case.monitor.assigned`
- `case.observe.assigned`
- `case.contact.manage.assigned`
- `case.assignment.manage`
- `case.read.oversight`

Rules:
- assigned caregiver operations require both the relevant capability and current-assignment match
- assignment/reassignment requires `case.assignment.manage`
- no job title is hard-coded
- missing ActorContext fails closed
- Family/Provider/Employer/AI access has no TS-03 capability grant

Identity provider / named-role mapping remains TS-05.

## 9. Command contracts

Commands:
- `CreateCase`
- `CorrectCaseProfile`
- `AddContactPoint`
- `CorrectContactPoint`
- `RecordInteraction`
- `CorrectInteraction`
- `RecordObservation`
- `CorrectObservation`
- `ReassignCaregiver`

Every mutation:
- requires authenticated ActorContext
- accepts idempotency key
- writes audit in same transaction
- writes outbox event in same transaction
- validates Case/assignment concurrency

## 10. Query contracts

Queries:
- `GetCaseWorkspace(case_id)`
- `GetCaseProfile(case_id)`
- `GetCurrentAssignment(case_id)`
- `GetAssignmentHistory(case_id)`
- `ListInteractions(case_id, cursor)`
- `ListObservations(case_id, cursor)`
- `ListContactPoints(case_id)`
- `GetCaseTimeline(case_id, cursor)`

Read models expose only TS-03 fields.

## 11. REST API baseline

Mutation endpoints:
- `POST /api/v1/cases`
- `POST /api/v1/cases/{case_id}/profile/corrections`
- `POST /api/v1/cases/{case_id}/contacts`
- `POST /api/v1/cases/{case_id}/contacts/{logical_contact_id}/corrections`
- `POST /api/v1/cases/{case_id}/interactions`
- `POST /api/v1/cases/{case_id}/interactions/{interaction_id}/corrections`
- `POST /api/v1/cases/{case_id}/observations`
- `POST /api/v1/cases/{case_id}/observations/{observation_id}/corrections`
- `POST /api/v1/cases/{case_id}/reassignments`

Read endpoints:
- `GET /api/v1/cases/{case_id}`
- `GET /api/v1/cases/{case_id}/workspace`
- `GET /api/v1/cases/{case_id}/assignments`
- `GET /api/v1/cases/{case_id}/contacts`
- `GET /api/v1/cases/{case_id}/interactions`
- `GET /api/v1/cases/{case_id}/observations`
- `GET /api/v1/cases/{case_id}/timeline`

No generic arbitrary record-edit endpoint is allowed.

## 12. Idempotency

All POST mutations require `Idempotency-Key`.

Idempotency scope:
- authenticated actor id
- operation name
- target Case when applicable
- idempotency key

Same key + same canonical payload returns the prior accepted result.

Same key + different payload fails with `409 IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD`.

Implementation must be race-safe with a database uniqueness constraint.

## 13. Concurrency

Reassignment requires `expected_current_assignment_id`.

If current assignment changed:
- fail with `409 CASE_ASSIGNMENT_CHANGED`
- do not partially write audit/outbox/history

Profile/contact/interaction/observation corrections require the expected current revision/record id and fail stale updates with a 409 conflict.

## 14. Domain events

Persist these versioned outbox event types:
- `case.created.v1`
- `case.profile_corrected.v1`
- `case.contact_recorded.v1`
- `case.contact_corrected.v1`
- `case.interaction_recorded.v1`
- `case.interaction_corrected.v1`
- `case.observation_recorded.v1`
- `case.observation_corrected.v1`
- `case.caregiver_reassigned.v1`

Events contain identifiers, actor provenance, timestamps and lineage references only; no AI-training eligibility implication.

## 15. Fail-closed rules

Reject rather than guess when:
- ActorContext missing
- required capability missing
- caregiver is not current assignment
- upstream enrollment reference missing at Case creation
- stale assignment/revision detected
- correction reason missing
- unsupported interaction/record type supplied
- request attempts Provider/AI/Outcome/Referral behavior

## 16. Database protections

Required DB protections:
- unique one active assignment per Case
- unique `(case_id, revision_no)` where revisioned
- unique idempotency scope
- FK lineage for superseding revisions
- no orphan Case child records
- audit history protected from normal UPDATE/DELETE
- outbox inserted transactionally

## 17. Test requirements

Minimum automated tests:
- create Case with initial assignment
- reject Case creation without upstream enrollment reference
- reject self/unauthorized assignment
- assigned caregiver can read/record permitted TS-03 data
- non-assigned caregiver denied
- oversight actor bounded access
- Provider/Family/Employer/AI actor access denied by default
- reassignment requires reason
- stale reassignment returns 409
- concurrent reassignment accepts at most one winner
- correction creates a new revision and preserves old value
- correction requires reason
- stale correction returns 409
- provenance actor type preserved
- idempotent retry returns same result
- key reuse with different payload returns 409
- mutation rollback leaves no partial audit/outbox rows
- OpenAPI contains only TS-03 routes/contracts

## 18. Explicit non-goals

Do not implement:
- Enrollment/eligibility engine
- Case status/closure state machine
- Referral
- Service Catalog
- Provider
- Outcome/Reassessment
- Emergency
- AI/runtime/training
- external integrations
- payment/billing
- named organizational RBAC mapping

## 19. Technical completion criteria

Technical is complete for TS-03 when:
- domain/persistence/API contracts are internally consistent
- Business exclusions are enforceable
- correction/audit/provenance design satisfies D-0125/D-0028
- authorization remains capability-based and fail-closed
- concurrency/idempotency rules are explicit
- test matrix is sufficient for implementation
- no OPEN Business decision is silently encoded.

## 20. Next stage

After Technical review passes, create Product Backlog for TS-03. Code remains prohibited until Sprint planning is complete.