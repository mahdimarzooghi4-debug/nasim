# T-011 — Live Operational Read-only Web

Source SG-011; status **front-end foundation**, explicitly not production login readiness.

React 19 + TypeScript + Vite, Persian RTL, responsive semantics. Single-origin calls use `fetch` with `credentials=same-origin`, `mode=same-origin`, `cache=no-store`, `redirect=error`, GET only and JSON-only responses. Fixed application-relative /api/v1 route builder; no arbitrary external URL, access token input, authorization headers, Actor impersonation, browser storage or runtime fake data.

## API composition

1. `GET /api/v1/authorization/self`: real trusted ActorContext. A 401 blocks entire UI and unmounts operational views; a 403 resource response shows denial, no fallback Case. ActorType AI remains denied. Client hides workspace navigation only when corresponding capability group is absent; final permission is always checked on Backend.
2. `GET /api/v1/cases?cursor&limit=20`: currently assigned Case/Profile or explicit oversight. Display immutable Case ID, latest profile revision, current assignment.
3. `GET /api/v1/cases/{case_id}/journey-workspace?...`: three *independent* bounded observation/referral/selected Follow-up cursors; no frozen snapshot claim. Referral selection includes only its own Follow-up notes.
4. `GET /api/v1/provider-candidates?cursor&limit=20`: descriptive Candidate list, gated by `provider_candidate.read`.
5. `GET /api/v1/provider-candidates/{id}/qualification-review-workspace?...`: independent Evidence/Review Request cursors and the existing permission intersection, not qualification decision.

All routes are *read only*. All backend fields are treated as recorded data only and rendered with React text nodes (no HTML injection). No local persistence, auto-refresh caching or fake auth. Abort stale in-flight requests on navigation/session loss.

## Build/test contract

Automated web workflow on this same exact SHA: Node 22, TS strict typecheck, Vitest typed API auth/permission/JSON and SSR fail-closed tests, Vite static bundle. Existing Backend 4 jobs also run on web changes to ensure exact-HEAD compatibility. Because no preapproved auth issuer or production gateway exists, real browser/real login E2E and hosted Stage remain blocked. Dependency lockfile, gateway security headers, and production image require later gate; no claim that Draft UI is deployable to real elderly data.

No DB schema/migration, backend endpoint or permission changes.
