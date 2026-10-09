# PB-008 — Referral Follow-up Record Foundation

Status: **ACCEPTED FOR SPRINT PLANNING** within SG-008/T-008 Foundation only.

- RFU-001 P0: strict follow-up creation/read contracts; forbid all status/Provider/Outcome fields and free-text outbox leakage.
- RFU-002 P0: append-only relational record and FK to existing Referral; human actor provenance, DB immutability and deferred effect-integrity guard.
- RFU-003 P0: technical permission version seeds without actor grants; assigned-human write, bounded assigned/oversight read, AI deny, assignment id stale protection and privacy tests.
- RFU-004 P0: atomic idempotent write + audit/outbox/row; stable conflict/rollback/race semantics and independent pagination.
- RFU-005 P0: HTTP/OpenAPI, PostgreSQL suite, restricted runtime grants, Alembic validation and disposable container smoke.
- RFU-006 P1: exact final HEAD CI, bounded technical Code Review and Draft PR status.

**Exclusions:** Referral status transitions, closure/cancellation/escalation, provider selection/acceptance/dispatch, satisfaction/outcome, AI classification/training, priority, cadence/SLA, data sharing/consent, UI, Hosted Stage and Production. No grant/decision policy invented from source Draft contracts.
