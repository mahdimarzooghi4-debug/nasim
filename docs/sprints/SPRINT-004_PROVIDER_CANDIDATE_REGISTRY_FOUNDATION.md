# Sprint 004 — Provider Candidate Registry Foundation

Status: **READY FOR CODE** under D-0124/D-0131 after SG-004 → T-004 → PB-004.

Baseline at slice selection: main `1eccc4cd4c2326ef270655823de9f6c22cae59a5`.

Branch: `sprint-004-provider-candidate-registry-foundation`.

Implementation order:

contracts/tests → permission registry → model/migration → application service →
transactional effects → REST/OpenAPI → full regression/security/concurrency tests →
migration cycle → Docker Stage-like smoke → commit/push → Draft PR → exact-HEAD CI.

Definition of done:

- PC-001…PC-007 complete;
- existing TS-03/TS-05/Referral behavior remains green;
- full Pytest, Ruff/format, Pyright, Alembic upgrade/downgrade/upgrade/check and current
  container-stage-smoke pass;
- Draft PR remains unmerged;
- implementation stops at Code Review.

No activation, Provider Type, qualification, Service mapping, Referral selection, capacity,
service delivery, Provider access, ranking, finance, external integration, UI, Hosted Stage or
Production is allowed.

**Code implementation is assigned to Codex.**
