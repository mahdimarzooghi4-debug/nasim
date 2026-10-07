# PB-005 — Provider Qualification Evidence Foundation

Derived from SG-005 / T-005 / D-0132.

- **QE-001** — strict contracts and technical permission vocabulary.
- **QE-002** — immutable ProviderQualificationEvidenceRecord and linear migration.
- **QE-003** — candidate-existence validation without candidate mutation.
- **QE-004** — authorized record/list/detail application service.
- **QE-005** — race-safe idempotency and atomic audit/outbox/idempotency effects.
- **QE-006** — exact minimal REST/OpenAPI surface.
- **QE-007** — DB immutability and bounded non-Case audit/outbox constraints.
- **QE-008** — security, concurrency, rollback and regression tests.
- **QE-009** — migration/quality/Stage-like smoke/exact-HEAD CI evidence.

Acceptance requires:

- all existing TS-03/TS-05/Referral/Provider Candidate tests preserved;
- no Role → Permission mapping;
- no qualification/activation semantics;
- no document-type taxonomy or credential-verification rule invented;
- all SG-005 OPEN decisions remain OPEN.
