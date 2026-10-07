# Sprint 002 — TS-05 Identity / Role / Authorization Foundation

Status: IMPLEMENTATION AUTHORIZED by explicit user instruction. Baseline: main
c8c079c7e8adfccbf670648734f31542ba533327. Branch:
`sprint-002-ts05-identity-authorization-foundation`.

Contracts/tests first, then registry/models/migration, internal transactional
persistence, snapshot resolver, trusted integration/self inspection, race/security
regressions and developer guide. Dependencies/lockfile unchanged.

Definition of done: PB-002 acceptance, full PostgreSQL Pytest, Ruff/format, Pyright,
Alembic upgrade/downgrade/upgrade/check and Docker Stage-like smoke; commit/push,
Draft PR and verified CI. Stop at Code Review; no merge. No IdP, auth flows,
UI, Hosted Stage, Production or wider Business features. SG-002 OPEN questions
block management APIs, not infrastructure. No claim D-0126 final mapping closed.
