# Sprint 008 — Referral Follow-up Record Foundation

- Date: 2026-10-09
- Source: D-0124 + D-0012/13/14/15 + SG-008 → T-008 → PB-008.
- Status: **Code foundation / Draft PR only**; review does not imply merge permission.
- Branch: `sprint-008-referral-follow-up-record-foundation`, based on main `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`.
- Delivery: strict typed contract → tests → append-only Referral-owned model, one linear migration and registry-only grants → HTTP/transactional audit/outbox/idempotency → PostgreSQL tests, quality, migrations, disposable container smoke → exact HEAD CI → technical Code Review.

Stop at Draft PR. PRs #14–#18 remain independently Draft/Open. D-0130 Hosted Stage unavailable; do not equate CI smoke with Stage/QA or declare Release/Production. Any subsequent merge must explicitly reconcile overlapping cursor hardening from PRs #17/#18, not replace approval gates.
