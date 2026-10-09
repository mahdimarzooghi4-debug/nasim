# PB-021 — Operational Case follow-up index (non-decisioning)

Deliverables: an assigned/oversight permission-gated descriptive, paginated, Case-wide read across existing Referral human follow-up notes; live RTL view; zero new state, workflow or grant; Backend/PostgreSQL security tests, Web contract tests, OpenAPI/smoke, green exact-head CI. Gate SG-021 → T-021 → PB-021 → Sprint 021.

Acceptance: all three existing read permission families enforced independently against same current Case assignment, AI denied, note never in Outbox/log, no wrong-Case disclosure, cursor bounds, immutable original records, 401 clears browser view. Every backend read is request-scoped rather than a frozen snapshot.

Not in scope: Provider dispatch or outcome, SLA/future follow-up plan, AI learning, session issuer, Figma approval, Hosted Stage/QA/Production.
