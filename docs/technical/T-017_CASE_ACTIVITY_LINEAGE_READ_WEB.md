# T-017 — Case History and Immutable Revision Lineage Web

Status **contract-preserving, read-only browser UI**. No backend migration/endpoint/permission addition.

## Exact existing Casework HTTP read models

1. `GET /api/v1/cases/{case_id}/timeline?cursor&limit=20` → Page[TimelineEntry] with `id,case_id,actor_id,actor_type,action,resource_type,resource_id,timestamp,correlation_id,before_reference,after_reference,reason`. Technical Casework `AuditEntry` actions only, not a global event ledger. Cursor is existing timestamp+UUID order.
2. `GET /api/v1/cases/{case_id}/assignments` → list[AssignmentView] with actual `started_at,ended_at,caregiver_actor_id,assigned_by_actor_id,reason`. Do not infer services delivered or "approved provider" from an open assignment.
3. `GET /api/v1/cases/{case_id}/interactions?cursor&limit=20` → Page[InteractionView] including `supersedes_interaction_id` and `correction_reason`.
4. `GET /api/v1/cases/{case_id}/observations?cursor&limit=20` → Page[ObservationView] including `supersedes_observation_id` and `correction_reason`.

Typed frontend read paths use the preexisting same-origin JSON `getJson` with no-store, no redirect, no custom actor headers, no new login or remote service. Every request independently requires current authorized Case read context; the frontend hides the tab for non-HUMAN, missing Case read grant or AI and does not infer Case read from assignment-manage. Backend is authoritative. On 401 the whole protected workspace is unmounted; 403 shows denial and never substitutes cached/mock Case data.

Each cursor feed maintains its own navigation stack, supports next/back, aborts in-flight fetches on scope, tab or cursor changes, and clears old results before re-fetching. UI never composes a global snapshot or assumes newer events leave older read identities unchanged. Assignment endpoint is full-list according to current existing contract and must not be mislabeled as paginated. No unbounded cursor-forged API.

## Verification

Strict TS and SSR contracts confirm exact URLs/query/headers/role denial, 401/403 generic fail-closed behavior, no arbitrary data or mutation, independent assignment handling and pagination capability. Exact-head Web CI (Vitest/typecheck/build via npm ci) and full Backend CI (real PostgreSQL tests, Ruff, Pyright, Alembic, disposable container smoke) required. No qualified Figma/UI acceptance, server session, real IdP, Origin+CSRF or hosted Stage under D-0130; no claim that Draft UI is production-usable.
