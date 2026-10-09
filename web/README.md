# Nasim Operational Web — read-only, real backend only

Scope: **Draft frontend operational foundation**, not a deployed product or approved Figma design.

- React 19, TypeScript, Vite; Persian RTL responsive UI.
- Real same-origin backend reads: `GET /api/v1/authorization/self`, `GET /api/v1/cases`, `GET /api/v1/cases/{id}/journey-workspace`, `GET /api/v1/provider-candidates`, and `GET /api/v1/provider-candidates/{id}/qualification-review-workspace`.
- Scope: Case list and recorded Case/Need/Referral/Follow-up; Provider Candidate and evidence/review request inspection. **No real service completion, verified outcome, qualification decision, dispatch or automated AI output.** No write button or mutation endpoint.
- No dummy/principal headers, token inputs, sample data, guessed eligibility, localStorage, sessionStorage or a fake login. API requests use same-origin credentials, no-store, and strict JSON response. 401 removes the operational component. 403 shows a denied state.
- Production browser auth requires a real approved identity provider and a trusted same-origin adapter that installs `ActorContext` on backend requests. **That service is not implemented yet**; without it, the UI intentionally cannot access protected information. A generic frontend-only login would be an unsafe bypass.
- Developer proxy to http://127.0.0.1:8000 does not create credentials, impersonate users or turn 401 into 200.
- UI has no Figma signoff (product owner requested software before Figma).

Development: Node >=22.12, `npm ci`, `npm run dev` (Vite on localhost). CI: `npm run check`; tests use test-only mocked fetch and static SSR, **never mock runtime product data**.

Deployment: static frontend assets must be hosted **same origin** as backend via an operator-configured TLS reverse proxy after IdP integration, explicit security review and Stage/Production approval; until then no real-world access should be claimed. Open tasks: approved IdP integration, security headers/CSP at trusted gateway, browser-based end-to-end tests with real authenticated principals, and independent design/accessibility QA.

## Caregiver recording slice — Sprint 012 (Draft)

When an existing trusted principal is authenticated, the Case Journey now contains explicit human recording forms for the **already-authorized** TS-03 and Referral commands: `RecordObservation` (including NEED_CAPTURE), `RecordInteraction` (CONTACT or MONITORING), `CreateReferral` from a selected recorded Need, and `RecordReferralFollowUp` from a selected Referral. Only current assigned HUMAN users holding the corresponding existing capability can see each form. Backend independently rechecks the actor, current Case assignment, source observation currency and idempotency.

- Explicit `datetime-local` input for occurred-at; the operator can correct it before submission. Displayed default is current local time, not AI-derived history.
- The current `expected_current_assignment_id` comes from live Case Profile read; no actor-provided name or role-based authority.
- A cryptographic UUID `Idempotency-Key` stays tied to the **identical** request payload across uncertain network retries and changes on any edit/new accepted submission. The UI never performs an automatic repeat POST. On conflict 409 it directs human review, not state guessing.
- A successful 201 triggers re-reading from the backend; raw errors and sensitive response payloads are not written to the browser console/localStorage or leaked to external APIs.
- This is **not** a Provider dispatch, proof of accepted service, verified outcome, consent, contact delivery or training signal. No write can execute while the authentication gate is blocked.

**Security gate:** There is still no selected/implemented browser IdP, protected browser session, final SameSite/CSRF middleware or approved host origin. Merely using `credentials: same-origin` does **not** supply CSRF protection for a future cookie-backed identity layer. Before any real browser-auth deployment, the trusted host must implement origin and CSRF protections, server-owned sessions and independent E2E authorization tests. This Draft slice cannot be exposed to personal data as a standalone production app.
