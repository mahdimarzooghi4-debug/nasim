# Nasim Operational Web — read-only, real backend only

Scope: **Draft frontend operational foundation**, not a deployed product or approved Figma design.

- React 19, TypeScript, Vite; Persian RTL responsive UI.
- Real same-origin backend reads: `GET /api/v1/authorization/self`, `GET /api/v1/cases`, `GET /api/v1/cases/{id}/journey-workspace`, `GET /api/v1/provider-candidates`, and `GET /api/v1/provider-candidates/{id}/qualification-review-workspace`.
- Scope: Case list and recorded Case/Need/Referral/Follow-up; Provider Candidate and evidence/review request inspection. **No real service completion, verified outcome, qualification decision, dispatch or automated AI output.** No write button or mutation endpoint.
- No dummy/principal headers, token inputs, sample data, guessed eligibility, localStorage, sessionStorage or a fake login. API requests use same-origin credentials, no-store, and strict JSON response. 401 removes the operational component. 403 shows a denied state.
- Production browser auth requires a real approved identity provider and a trusted same-origin adapter that installs `ActorContext` on backend requests. **That service is not implemented yet**; without it, the UI intentionally cannot access protected information. A generic frontend-only login would be an unsafe bypass.
- Developer proxy to http://127.0.0.1:8000 does not create credentials, impersonate users or turn 401 into 200.
- UI has no Figma signoff (product owner requested software before Figma).

Development: Node >=22.12, `npm install`, `npm run dev` (Vite on localhost). CI: `npm run check`; tests use test-only mocked fetch and static SSR, **never mock runtime product data**.

Deployment: static frontend assets must be hosted **same origin** as backend via an operator-configured TLS reverse proxy after IdP integration, explicit security review and Stage/Production approval; until then no real-world access should be claimed. Open tasks: lockfile/reproducible install, approved IdP integration, security headers/CSP at trusted gateway, browser-based end-to-end tests with real authenticated principals, and independent design/accessibility QA.
