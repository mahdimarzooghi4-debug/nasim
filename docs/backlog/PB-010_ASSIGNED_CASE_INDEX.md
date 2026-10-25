# PB-010 — Assigned Case Operational Index

Status: **ACCEPTED FOR SPRINT 010 IMPLEMENTATION only**, under SG-010/T-010.

- CI-001 P0: typed `GET /api/v1/cases` Page[CaseProfileView] contract with cursor/limit, preserving existing POST semantics and exact OpenAPI.
- CI-002 P0: single-statement Case→active Assignment→latest Profile SQL; current caregiver filter in query and independent oversight; no other principal filter, no per-row leakage.
- CI-003 P0: fail closed absent read capability and for AI; no default grants or new data fields. Former caregiver denied following reassignment.
- CI-004 P0: real DB, HTTP, API surface and Container Smoke tests, limit/cursor bounds, atomic snapshot, profile correction, history unchanged, no side effects.
- CI-005 P1: full exact-head CI and AI-assisted technical Code Review; leave Draft/Open.

Explicitly exclude Case lifecycle/status/closure, task scheduling, priority/triage, provider/service choice, referral dispatch, consent sharing, AI/runtime, model/dataset, UI/Figma, Stage or Production.
