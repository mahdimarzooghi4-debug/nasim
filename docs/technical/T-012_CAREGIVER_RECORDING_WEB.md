# T-012 — Governed Caregiver Recording Web

- Status: **Approved command wiring only / Draft**
- Frontend: existing React/TypeScript/Vite Persian RTL UI. Backend endpoints/models are unmodified.

## Server-owned command contracts

- `POST /api/v1/cases/{case_id}/observations`: `expected_current_assignment_id`, `record_type=OBSERVATION|NEED_CAPTURE`, user-visible `occurred_at`, `content`.
- `POST /api/v1/cases/{case_id}/interactions`: `expected_current_assignment_id`, `interaction_type=CONTACT|MONITORING`, user-visible `occurred_at`, `content`.
- `POST /api/v1/cases/{case_id}/referrals`: `expected_current_assignment_id`, `source_need_observation_id` selected from existing need records, `reason`. Only descriptive recording, not dispatch.
- `POST /api/v1/referrals/{referral_id}/follow-up-records`: `expected_current_assignment_id`, `note`, `reason`. Only human follow-up, not verified Provider service or Outcome.

The `Idempotency-Key` is a browser crypto UUID held with an exact request payload and reused only after an uncertain failed attempt with unchanged fields. After confirmed 201 or any edit, a new identity is required for a new intent. Backend retains full race-safe idempotency/assignment/current observation validity, 401/403/409 semantics and append-only audit/outbox. No client optimistic business state. On 201 the application re-reads the backend; on 401 it closes the full operational view. On 409 it alerts the human without advancing anything or automatically retrying with another key. No client storage of sensitive data, headers impersonating an Actor, external proxy or invented token.

The relevant create forms are shown only when `actor_type=HUMAN`, the authenticated actor ID matches the current caregiver from the read model, and the exact existing creation capability is present. The server is the authorization authority. A selected Referral is required before follow-up; a recorded NEED_CAPTURE is required before Referral selection. A paginated read may omit valid older sources, so the UI must not infer that no Need exists in the Case.

## Test and security gates

Strict TS contract tests for 4 endpoint routes, validation, 409/401 fail-closed and no duplication across network failures, no token or actor headers; SSR tests for permission-gated rendering; `npm ci`, TS typecheck, Vitest, static build and exact-head full Backend CI. No new DB or OpenAPI route. No Prod browser login yet: before real cookie-backed auth, implement trusted Origin+CSRF/session validation, CSP/TLS, controlled allowed-host/proxy, browser E2E with real authenticated principals, and human sign-off. `credentials: same-origin` is **not** itself CSRF defense. D-0130 Stage remains unavailable.
