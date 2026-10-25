# Sprint 007 — Provider Qualification Inspection Workspace

- Planned date: 2026-10-08
- Source: D-0124 → SG-007 → T-007 → PB-007
- Status: **Code candidate / Draft PR only**; not a Stage or Release gate.
- Scope: one read-only Provider Registry inspection workspace composed from existing Candidate, Evidence and Review Request query contracts.
- Sequence: typed API contract → PostgreSQL/HTTP security regression tests → bounded read implementation → Draft PR → full exact-head CI → technical Code Review.
- No database migration, role/permission grant or state machine. Business decisions about real reviewer authority, qualification thresholds/criteria, activation and Provider Selection remain OPEN.
- Approval boundary: PR stays Draft/Open until separate explicit instructions. No merge, Ready for Review, Hosted Stage/QA/Release/Production while D-0130 applies.
