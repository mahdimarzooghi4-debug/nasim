# IT-001 — Case / Referral / Provider / Follow-up Integration Reconciliation

Date: 2026-10-09. Status: **DRAFT technical integration verification**.

## Source contracts, not new policy

- PR #17, exact HEAD `fac802f7eced83ebd53637b5e8b19a991d770fba`: TS-03 cursor, idempotency ActorType replay isolation, read limit guards.
- PR #18, exact HEAD `aaadcd4e527e19484f736d156f8f12a0ec2ec480`: SG-007 / T-007 / PB-007 Provider qualification descriptive workspace.
- PR #19, exact HEAD `593f7a55638f4bde098f8aa088b03e5a4feba32b`: SG-008 / T-008 / PB-008 immutable human Referral follow-up evidence.
- Baseline `main f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`; this branch is **based on PR #19** and has **no right to merge** into main.

No new Business Decision or permission is introduced. This integration is a compatibility test of **separately authorized** contracts; it does not create a combined outcome, Provider decision, case lifecycle or dispatch. `OPEN ≠ ACCEPTED`. D-0130 Hosted Stage remains unavailable.

## Explicit integration boundaries

- Case Profile → immutable NEED_CAPTURE → independently recorded Referral → immutable *human* follow-up note is a historical chain, not a final service outcome. Follow-up actor is a currently assigned caregiver with explicit capability; stale current assignment fails closed; same-key retry remains guarded.
- Provider Candidate → Evidence + Qualification Review Request → read-only Provider inspection remains an independent domain. Its existing three permission intersection never implies the Case, Referral or Follow-up permissions and never selects a provider.
- Shared pagination validation from PR #17 is present **once**; preserving actor-type idempotency isolation and Case read bounds must not alter Provider or Referral bounded reads. All source tests are retained.
- OpenAPI, runtime API surface and disposable container smoke must include both previously independent endpoints. No new field, route, DB migration, seeded grant, UI or external credential is introduced by reconciliation.
- New cross-workflow PostgreSQL-backed HTTP test covers the complete permitted Case/Need/Referral/Follow-up chain, independent Provider inspection, cross-domain 403 denial, no note leakage into Provider, TS-03 timeline or Outbox, and stale caregiver access after reassignment. Tests cannot be construed as actual service delivery.

## Test, review and promotion gates

Preserve all pre-existing source regression tests and execute one exact-HEAD full CI: Ruff, Format, Pyright, Pytest/PostgreSQL including races, Alembic migration and disposable Stage-like container smoke. Perform scoped integration Code Review after green. Keep PR #20 Draft/Open as a temporary integration record; PR #14–#19 remain Draft/Open. No Ready-for-Review, Merge, real Stage, QA admission, Release or Production without separate explicit human/owner authorization. Avoid treating an AI-assisted review as an independent human sign-off.

When any source PR HEAD changes, rebase/reconcile from exact sources and rerun CI and review before merge consideration. This integration branch is not an authorization to modify original PRs.
