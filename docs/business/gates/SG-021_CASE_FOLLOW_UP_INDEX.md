# SG-021 — Descriptive Case-wide human Referral follow-up index

Status: **Technical entry for a read-only safe projection of existing authorized records**, 2026-10-09.

Source: TS-03 D-0119–D-0125, accepted SG-008 human Referral follow-up, SG-009 descriptive Case Journey and SG-011 authenticated-only Web reads; BC-003 Referral final states/cadence/closure and BC-019 outcomes remain DRAFT/OPEN. Main remains unmerged; this work stacks on Draft PR #32 at `4e1cf18a307274e0d098500ee82ad9725aa1d66a`.

**Allowed:** list existing human Referral follow-up note records for all Referral IDs already belonging to one Case, ordered by original recorded timestamp/ID, with bounded pagination. No new data source or new authority: require independent Case read + Referral read + Follow-up read capability families, each authorized against the current Case assignment (or its own oversight grant). AI denied. No new state, privacy exception, cross-Case leakage or mutable record.

**Blocked:** service completion/Provider result, outcome, satisfaction, Need resolved, next-action scheduling/priority, inferred SLA, training signal, email/SMS notification and public access. Real browser identities remain fail-closed until an actual approved IdP/session. No Stage/QA/Release while D-0130 is active.

Evidence: SG-021 → T-021 → PB-021 → Sprint 021; backend API, PostgreSQL and browser contract tests, CI and non-approving Code Review. All stacked PRs Draft/Open without explicit merge/Stage authority.
