# PB-002 — TS-05 Product Backlog

Derived from SG-002 / T-002. Sprint scope:

1. TS05-001: contracts and source-backed vocabulary/permission registry, no grants.
2. TS05-002: versioned definitions, relational lineage, temporal assignments/grants.
3. TS05-003: atomic immutable authorization audit and stale revocation guards.
4. TS05-004: deterministic snapshot resolver and trusted-principal boundary.
5. TS05-005: safe self inspection; no public authorization management mutation.
6. TS05-006: default-deny, provenance, integrity/race and TS-03 regression tests.
7. TS05-007: migrations/Stage smoke/CI and developer documentation.

Acceptance: no implicit mapping, no invented management authority; full tests,
quality, migration cycle, metadata check and exact-HEAD CI pass. All OPEN business
mapping/IdP decisions stay OPEN, not silently deferred/accepted. Stop at Code Review.
