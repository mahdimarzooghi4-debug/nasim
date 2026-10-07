# Sprint 006 — Provider Qualification Review Request Foundation

- **Status:** READY FOR CODE
- **Business gate:** SG-006
- **Technical baseline:** T-006
- **Backlog:** PB-006
- **Decision:** D-0133
- **Baseline main:** `a525841e89d9c70f52de10076305ac08f2b25176`
- **Branch:** `sprint-006-provider-qualification-review-request-foundation`

## Goal

Implement only immutable Qualification Review Request capture/read for existing Provider Candidates.

## Build order

contracts/tests → permission registry → model/migration → candidate validation → application service →
transactional effects → REST/OpenAPI → DB/security/concurrency tests → full regression → migration
cycle → Stage-like smoke → commit/push → Draft PR → exact-HEAD CI.

## Definition of Done

QR-001…QR-009 complete and:

- existing behavior remains green;
- full Pytest passes on PostgreSQL;
- Ruff / Ruff format pass;
- Pyright passes;
- Alembic upgrade → downgrade → upgrade and `alembic check` pass;
- Stage-like container smoke/restart/schema-drift check passes;
- exact branch HEAD has green GitHub Actions;
- Draft PR remains unmerged;
- implementation stops at Code Review.

## Hard boundaries

Do not implement:

- reviewer assignment;
- reviewer/approver authority mapping;
- qualification criteria;
- evidence sufficiency or evidence-bundle policy;
- review state machine;
- qualification decision;
- qualified/approved/active state;
- rejection/rework workflow;
- activation;
- Provider Type;
- Service mapping;
- geography eligibility;
- Capacity;
- Provider Selection;
- Referral response;
- Service Delivery;
- Provider Case/Elder access;
- ranking/score;
- financial/settlement;
- external integration;
- UI;
- Hosted Stage;
- Release;
- Production.

`Review Request ≠ Review Decision ≠ Activation`

**Code implementation continues here under the Product Owner's explicit instruction to continue coding in this chat while Codex is limited.**
