# T-014 — Case Operations via existing TS-03 API

Status: **approved foundation command wiring only**, no Backend code/schema/migration.

## Exact existing contracts
1. `POST /api/v1/cases` with `CreateCase` {upstream_enrollment_ref, elder_reference, initial_caregiver_actor_id} and header `Idempotency-Key`, receives 201 `CaseProfileView`. Backend requires existing `case.assignment.manage` and records unverified upstream Enrollment reference with provenance. This UI must not synthesize a valid reference.
2. `POST /api/v1/cases/{case_id}/reassignments` with `ReassignCaregiver` {expected_current_assignment_id, caregiver_actor_id, reason}, receives 201 `AssignmentView`. Explicit management capability, mandatory reason, stale assignment conflict 409; keep history immutable.
3. `POST /api/v1/cases/{case_id}/contacts` with `AddContactPoint` {expected_current_assignment_id, contact_kind, contact_value}, receives 201 `ContactView`. Exact `case.contact.manage.assigned` AND current actor match. There is no approved enum/taxonomy for `contact_kind`; the human supplies a bounded technical label. No delivery or validation claim.
4. Narrow `GET /api/v1/cases/{case_id}` (existing Case profile) and `GET /api/v1/cases/{case_id}/contacts` for users with existing Case read capabilities. A management-only actor must never infer a read grant.

Use a fixed same-origin JSON POST adapter and 201 typed response, no arbitrary proxy, local persistent Case data, Actor spoofing headers, tokens or client-side role policy. Cryptographic browser UUID `Idempotency-Key` bound to the identical payload; preserve only for an uncertain failed submission without changed fields. Success or form edit rotates intent. On 409 do not create a new key or override expected assignment; prompt backend refresh and human review. On 401 unmount all protected UI. Client never interprets a Record as service completed/verified, and never sends data to AI dataset.

Test: TypeScript/SSR, explicit capabilities, AI denial and current-caregiver match, independent Case creation without read grant, narrow Case view without Referral permission, exact URL/JSON/header and 401/403/409, stale assignment, no optimistic status, Backend full regression unchanged (537 PostgreSQL tests before this slice). Real IdP/Origin/CSRF/trusted browser session, legal data-sharing, browser E2E, and Hosted Stage D-0130 are separate blockers.
