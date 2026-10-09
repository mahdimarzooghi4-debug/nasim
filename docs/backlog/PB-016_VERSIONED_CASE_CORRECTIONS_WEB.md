# PB-016 — Governed Versioned Case Corrections

- COR-016-01 P0: human manager can correct Case Profile with current Profile ID, current Assignment and mandatory rationale, no history update.
- COR-016-02 P0: current assigned HUMAN with explicit contact permission can correct latest visible Contact logical record, pinning expected current revision ID.
- COR-016-03 P0: currently assigned HUMAN with monitor permission can correct recorded Interaction with explicit occurred_at/type/content/reason, exact expected record ID and conflict handling.
- COR-016-04 P0: currently assigned HUMAN with observation permission can correct recorded Observation or NEED_CAPTURE with exact expected ID, explicit occurred_at/type/content/reason; no automatic Referral/Outcome change.
- COR-016-05 P0: immutable correction API adapter, no custom Actor headers/third-party call, browser crypto intent replay, 401/403/409 fail-closed, 201 authoritative server re-read, no optimistic state or PII logging.
- COR-016-06 P0: paginated existing read models, latest Contact revision selection only, SSR and TS tests, exact-head Web/Backend CI and non-approving technical Code Review.

Excludes real Login/IdP, approved browser sessions, Provider selection, consent, service delivery/Outcome, AI Dataset/Training, Stage/Production and any newly invented Business criterion. Previous PRs remain unmerged Draft.
