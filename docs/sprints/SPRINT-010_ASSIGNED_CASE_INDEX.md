# Sprint 010 — Assigned Case Operational Index

- Date: 2026-10-09. Source: existing TS-03/TS-05 accepted technical boundaries → SG-010 → T-010 → PB-010.
- Branch `sprint-010-assigned-case-operational-index` based on unmerged PR #21 HEAD `0d95d54d8c113281206b6dcc9a1d83e980897e64`.
- Goal: safe case discovery for a *currently assigned and explicitly authorized* caregiver or an explicitly privileged oversight actor, without inventing work states.
- Code sequence: typed contract → PostgreSQL security tests → deterministic query → FastAPI route/OpenAPI → container smoke → exact-head CI → technical Code Review.
- No migration/new grants; no role-lookup shortcuts, provider dispatch, scoring or AI. Keep #14–#21 and new PR Draft/Open; do not merge/mark ready/deploy real Stage/Production. D-0130 remains active.
