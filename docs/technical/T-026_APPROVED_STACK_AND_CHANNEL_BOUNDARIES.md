# T-026 — Nasim Approved Technology Baseline and Channel Boundaries

**Status:** Accepted target-stack direction (D-0171). **Not** an implementation or deployment acceptance.
**Date:** 2026-10-09.
**Depends on:** D-0169 (Keycloak target), D-0170 (family self-funded purchase in initial scope), BC-003, BC-005, BC-007, BC-014, BC-022, T-024 (Stage identity).

## 1. Real vs target architecture

| Layer or channel | Approved technology | Evidence/status |
|---|---|---|
| Backend / API | Python 3.12, FastAPI, Pydantic | Implemented foundation and Draft feature stack |
| Database | PostgreSQL 17 with SQLAlchemy async / asyncpg / Alembic | Development and CI, not Hosted Stage |
| Organization/admin web | React 19, TypeScript, Vite | Actual Case/Provider operational slices in Draft PRs; support organization and full admin are not built |
| Elder + family companion mobile | React Native + TypeScript | **Approved technical direction; not implemented** |
| Professional caregiver mobile | React Native + TypeScript | **Approved technical direction; not implemented** |
| Identity | Keycloak OIDC, secure approved session boundary | Architecture selected, provider/realm/login not provisioned; fail-closed |
| AI and learning | Internal Nasim-controlled Python-compatible AI and governed datasets | Synthetic offline sources/partitions exist; no selected Production model or auto-promotion |
| Local dev/CI | Docker / GitHub Actions / Pytest / Ruff / Pyright / Vitest | Existing; disposable Stage-like smoke is NOT Hosted Stage |

## 2. Actor/client responsibilities

- **Elder mobile / elder mode:** elder's own experience only, with accessibility and explicit capability gates.
- **Elder mobile / family companion mode:** independent authenticated child's account, with *separately authorized* assistance and scope; not an implicit elder impersonation or full medical/case access. Child is the initial proposed order payer from their own account, not from elder credit. There is **no real purchase/payment workflow currently**.
- **Professional caregiver mobile:** current Case assignments, human observation/need/referral/follow-up only where actual Backend capabilities allow; no automatic provider selection or verified service-outcome claim.
- **Support-organization web:** scope/aggregated reporting and support workflows subject to a future Business/Technical contract; not a permission to inspect all elder records.
- **Operations/admin web:** management and governance capabilities remain separately scoped. Admin does not grant default full elder-record access.

## 3. Implementation boundaries

1. Keep Python/FastAPI and existing PostgreSQL schemas; don't rewrite core services just for a mobile framework.
2. Define versioned API contracts and generated/validated TypeScript types for web/mobile; share types deliberately, **never** shared credentials or client claims as authorization.
3. Decide mobile build/distribution targets (Android and/or iOS), native accessibility/privacy requirements, offline behavior, notifications, device policy, and release sequence in separate contracts; do not invent them from React Native selection.
4. Authentication remains fail-closed until real Keycloak, issuer/client, secure token handling, mobile redirect/deep-link policies, session/CSRF for web and contract/E2E tests are in place.
5. App UI does not imply payment, provider activation, completed referral/service or live AI before authorized backend contracts and external integrations.
6. AI remains entirely internal and controlled; model choice, trainer, queue/worker technology, infra sizing and benchmarks remain open, not implied by approval of Python.
7. Follow the parent delivery lifecycle; Draft PRs must not be merged/marked Ready or deployed to Stage/Production without the relevant explicit release and review gates.

## 4. Figma planning

Design four **target experiences** as editable designs with Design System tokens: (a) dual-mode elder/family mobile; (b) caregiver mobile; (c) support organization web; (d) Nasim operations/admin web. The existing desktop Case Index belongs to an operational/admin-web concept, **not** the sole interface for caregiver. UX prototypes must mark fictitious values and features not yet implemented.

Do not represent these screen artifacts as accepted legal, financial, or automatic routing decisions.
