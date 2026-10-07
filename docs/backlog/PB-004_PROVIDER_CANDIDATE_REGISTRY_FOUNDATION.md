# PB-004 — Provider Candidate Registry Foundation

Derived from SG-004 / T-004.

- PC-001: strict ProviderCandidate contracts and permission vocabulary.
- PC-002: immutable ProviderCandidateRecord + linear migration and DB history guard.
- PC-003: deterministic authorized register/read application service.
- PC-004: atomic audit/outbox/idempotency with race-safe retry behavior.
- PC-005: minimal POST/list/detail REST and exact OpenAPI surface.
- PC-006: security/integrity/concurrency/regression tests.
- PC-007: migration, quality, Stage-like smoke and exact-HEAD CI evidence.

Acceptance requires full existing suite plus new tests green, no implicit Role mapping, and no
operational Provider semantics. All SG-004 OPEN decisions remain OPEN.
