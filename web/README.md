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

## Provider Candidate human intake — Sprint 013 (Draft)

The existing `ProviderCandidates`, `ProviderQualificationEvidence` and `ProviderQualificationReviewRequests` POST contracts now have **explicit permission-gated real web forms** for human operators. These records are descriptive registration/submission/review-request records, *not* qualification approval, completed verification, service-capacity grant, activation, assignment or Provider selection. The UI does not guess missing Provider type, geographic reach, service mapping or qualification score.

- Candidate registration requires `provider_candidate.register`, and an existing read grant is separately required to display the Candidate directory. A user authorized only to register does not receive implicit directory visibility.
- Evidence and Review Request submission require their separate `provider_qualification_evidence.record` / `provider_qualification_review.request` capabilities and a selected known Candidate. Backend re-enforces each scoped permission.
- Three exact immutable 201 POST routes, secure per-payload idempotency identities, same-origin JSON only, generic 401/403/409 handling, no hidden retry and fresh Backend read on accepted records. No dummy Provider or forged status is created.
- A real browser IdP, session/CSRF/origin protection, user-role mapping, document upload/validation provider, privacy and approved legal sharing authority remain **unimplemented**. Before any protected web release, close those gates and perform real E2E browser QA. D-0130 Hosted Stage remains unavailable.

## Sprint 014 — Case Creation, Assignment and Contact (Draft)

The approved TS-03 immutable Case writes can be exercised by authenticated **HUMAN** operators through the RTL panel. This is not a new Enrollment/eligibility workflow.

- `POST /api/v1/cases`: explicit `case.assignment.manage` grant, required externally supplied `upstream_enrollment_ref`, `elder_reference` and initial caregiver actor ID. The system **records** the upstream reference; it does not verify that Enrollment was legal/completed or invent a default caregiver.
- `POST /api/v1/cases/{case_id}/reassignments`: management capability, human-entered new caregiver ID and reason, exact `expected_current_assignment_id` from live backend read. DB enforces one active assignment and no silent history mutation; conflict triggers fresh read and human review.
- `POST /api/v1/cases/{case_id}/contacts`: the currently assigned HUMAN with exact `case.contact.manage.assigned` may register an explicit contact type/value, not claim message delivery, ownership proof or preferred communication. Existing contact records are loaded from the protected `GET /api/v1/cases/{id}/contacts` route.
- `GET /api/v1/cases/{id}`: for a user who can read a Case but has no Referral/Follow-up read grants, a separate narrow profile/operations view prevents an invented Referral grant. A management-only human can create a Case without gaining list/read access.
- Browser commands are fixed same-origin 201 JSON, cryptographically secured per-payload idempotency and no actor/authorization spoofing. 401 closes the operational UI; 403/409 fail closed; accepted results prompt fresh server reads; client renders no optimistic official Case state.

**Not authorized by this code:** Enrollment verification, real browser Identity Provider, cookie-session/CSRF/Origin defenses, final RBAC provisioning, outbound contact, Provider choice, Case closure, service Outcome or AI Training. Before real protected use, these require separate approved contracts and security/E2E evidence. CI container smoke is not Hosted Stage (D-0130).

## Sprint 017 — Auditable Case Activity & Revision Lineage (Draft)

Human users with existing `case.read.assigned` or `case.read.oversight` may inspect **only already-authorized Case data** via four separate read models: cursor-bounded `GET /cases/{id}/timeline` (technical Casework audit events, reason, actor and before/after resource identifiers), `GET /cases/{id}/assignments` (actual starting/ending assignment history), cursor-bounded `GET /cases/{id}/interactions` and `GET /cases/{id}/observations` (all immutable revisions with supersession references). The React UI uses 20-item pages for cursor feeds, supports manual refresh, generic error handling and cancels in-flight requests on view/cursor switches.

A Case timeline is **not** a cross-context health, Provider, Referral or Outcome event ledger; it includes only Casework events accepted by that existing API. No invented status, work priority, eligibility, compliance verdict or downstream effect is derived from events. An unended assignment is shown only as lacking an end timestamp, not interpreted as verified service delivery. Timeline pages are not an immutable snapshot: data may change between reads. Client access gating supplements existing backend's per-request actor/assignment authorization and does not grant new roles.

The unconfigured browser IdP/session remains *fully blocked* by Sprint 015. Real browser authentication, legal access and Stage require separate explicit governance. This Sprint does not create a login or change Backend schema/permissions. No Figma signoff and no real Production access claimed.


## Sprint 021 — Case-wide Referral follow-up index (Draft)

A separate read-only list under an authorized Case Journey displays the actual human Follow-up notes already recorded for all Referrals in that Case, with referral identity, recorder, recorded timestamp, original note/reason, bounded server-side keyset pages and a back-navigation control. The Backend independently validates **all three** existing Case, Referral and Follow-up read grants, each against the current assigned caregiver or an explicit oversight grant for that exact read family. AI and stale assignees are rejected. No note data is stored locally, inferred, turned into a Training Label, or sent to an external service.

A Case-wide follow-up view is **not** an action-required queue, due date, service completion, verified Outcome, satisfaction score, real-time notification, or a new Provider workflow. Without an approved real browser IdP/session, the existing fail-closed browser barrier still prevents operational usage. Hosted Stage/Production remain unapproved.
