# PB-006 — Provider Qualification Review Request Foundation

Derived from SG-006 / T-006 / D-0133.

- **QR-001** — strict request/read contracts and technical permission vocabulary.
- **QR-002** — immutable ProviderQualificationReviewRequestRecord and linear migration.
- **QR-003** — candidate-existence validation without Candidate/Evidence mutation.
- **QR-004** — authorized request/list/detail application service.
- **QR-005** — race-safe idempotency and atomic audit/outbox/idempotency.
- **QR-006** — exact minimal REST/OpenAPI surface.
- **QR-007** — DB immutability and bounded non-Case audit/outbox constraints.
- **QR-008** — security, concurrency, rollback and regression tests.
- **QR-009** — migration/quality/Stage-like smoke/exact-HEAD CI evidence.

Acceptance requires:

- all existing TS-03/TS-05/Referral/Provider Candidate/Qualification Evidence tests remain green;
- no Role → Permission mapping;
- no reviewer/approver/decision/activation semantics;
- no one-active-request rule;
- all SG-006 OPEN decisions remain OPEN.
