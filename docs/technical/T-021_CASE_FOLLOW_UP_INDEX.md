# T-021 — Restricted descriptive Case follow-up index

Endpoint `GET /api/v1/cases/{case_id}/referral-follow-ups?cursor&limit`, returns existing `Page[ReferralFollowUpView]`. No POST, migration or new permission. Reuse Referral-owned note and Referral models and TS-03 CaseReferences current-assignment boundary.

All three independent groups are required: `case.read.assigned|case.read.oversight`, `referral.read.assigned|referral.read.oversight`, `referral.follow_up.read.assigned|referral.follow_up.read.oversight`. Each family must pass Case-scoped assignment or its **own** oversight grant; an oversight grant in only one group never widens the others. AI denied. Authorization and Case existence happen before cursor parsing; no Case ownership/mutation by Referral module. Query joins only existing immutable Referral/Follow-up tables within the same Case; keyset `(recorded_at,id)` strictly increasing; limit 1..100; invalid cursors fail closed. Read never persists events/audit/idempotency.

Web: new read-only CaseFollowUpIndex loads same-origin strict JSON only, clears prior page on each request, aborts old requests, relocks after 401, independent per-Case cursor and refresh on a successful new record. It does not display synthetic data, infer status or bypass unconfigured browser sessions.

Tests: real PostgreSQL Case partitioning, multi-Referral pagination, immutable side-effects, per-group authorization, cross-family oversight non-escalation, AI/old caregiver denial, stale cursor, missing case; HTTP 401/403/422/405, OpenAPI exact paths, Web read contract/typechecking; disposable Stage-like CI smoke is not Hosted Stage.
