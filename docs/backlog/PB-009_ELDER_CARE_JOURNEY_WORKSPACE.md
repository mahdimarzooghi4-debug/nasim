# PB-009 — Elder Care Journey Read Workspace

Status: **FOUNDATION IMPLEMENTATION BACKLOG** under SG-009/T-009; not a Provider/Outcome approval.

- CJ-001 P0: typed bounded Case Journey read including existing Case Profile, Observations, Referral records, and optional selected-Referral follow-ups; no invented summary/status fields.
- CJ-002 P0: composition through existing bounded public owner services; no cross-bounded-context persistence imports or DB migration.
- CJ-003 P0: intersection of existing read permission families, additional owner checks, no AI, no implicit caregiver access, no cross-Case Referral follow-up disclosure.
- CJ-004 P0: independent cursors; invalid/unscoped cursor and limit rejection; no frozen snapshot claim.
- CJ-005 P0: real PostgreSQL/HTTP integration, reassignment revocation and zero read side effects; OpenAPI and disposable container smoke.
- CJ-006 P0: exact-head full CI, AI-assisted technical review comment and Draft PR only.

Explicit exclusions: new role policy, Provider qualification/selection/dispatch, Referral lifecycle transition, service completion, Outcome, Reassessment, medical/financial authority, AI Training, data sharing, scheduling, SLA, UI, hosted Stage/QA/Release/Production.
