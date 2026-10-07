# Sprint 005 — Provider Qualification Evidence Foundation

- **Status:** READY FOR CODE
- **Business gate:** SG-005
- **Technical baseline:** T-005
- **Backlog:** PB-005
- **Decision:** D-0132
- **Baseline main:** `b022d7fd522fc0ffc3c87d8b9235692180d55e19`
- **Branch:** `sprint-005-provider-qualification-evidence-foundation`

## Goal

Implement only immutable Qualification Evidence capture/read for existing Provider Candidates.

## Build order

contracts/tests → permission registry → model/migration → candidate-reference validation →
application service → transactional effects → REST/OpenAPI → DB/security/concurrency tests →
full regression → migration cycle → Stage-like smoke → commit/push → Draft PR → exact-HEAD CI.

## Definition of Done

QE-001…QE-009 complete and:

- existing business behavior remains green;
- full Pytest passes on PostgreSQL;
- Ruff and Ruff format pass;
- Pyright passes;
- Alembic upgrade → downgrade → upgrade and `alembic check` pass;
- Stage-like container smoke/restart/schema-drift check passes;
- exact branch HEAD has green GitHub Actions;
- Draft PR remains unmerged;
- implementation stops at Code Review.

## Hard boundaries

This Sprint MUST NOT implement:

- Qualification Decision;
- qualified/approved/active state;
- reviewer/approver workflow;
- mandatory document rules;
- credential verification;
- evidence expiry/validity;
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
- external document storage/integration;
- UI;
- Hosted Stage;
- Release;
- Production.

`Qualification Evidence ≠ Qualification Decision ≠ Activation`

**Code implementation is assigned to Codex unless the Product Owner explicitly asks to continue coding here.**
