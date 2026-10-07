# PB-003 — Referral Foundation Product Backlog

Derived from SG-003/T-003; acceptance is foundation only.

- RF-001: strict create/read contracts and public TS-03 transaction reference boundary.
- RF-002: immutable ReferralRecord, same-case/type/current source integrity and migration.
- RF-003: TS-05 registry vocabulary with zero role/actor grants; default-deny integration.
- RF-004: create/read services, assignment checks, idempotency and transactional effects.
- RF-005: minimal REST/OpenAPI endpoints; no lifecycle/correction or arbitrary edits.
- RF-006: real PostgreSQL security, source/race/rollback/history and regression tests.
- RF-007: migration/quality/Docker/CI validation and developer run documentation.

Done: all prior tests retained, full suite/quality/migration metadata/Stage-like smoke
and exact-HEAD Actions green; commit/push and Draft PR, stop at Code Review.
All SG-003 OPEN decisions stay OPEN. No invented one-Referral-per-Need invariant.
