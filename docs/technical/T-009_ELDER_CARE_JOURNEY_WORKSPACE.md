# T-009 — Elder Care Journey Read Workspace

Status: **FOUNDATION/READ ONLY**, derived from existing accepted TS-03/TS-05 and Referral scopes. Under SG-009, NOT a new authoritative longitudinal state.

## Typed API

`GET /api/v1/cases/{case_id}/journey-workspace`

Query: `referral_id?`, `observation_cursor?`, `referral_cursor?`, `follow_up_cursor?`, `limit=50` (1..100). Each existing timestamp/UUID cursor applies **only** to its own list. `follow_up_cursor` without `referral_id` fails `422 INVALID_CURSOR`. Invalid limit returns `422 INVALID_PAGE_LIMIT`. All read-only, zero schema migrations.

Response `CareJourneyWorkspaceView`:
- `case: CaseProfileView` (authoritative profile/current assignment from Casework owner)
- `observations: Page[ObservationView]` (existing Casework history, no Need verdict)
- `referrals: Page[ReferralView]` (descriptive Referral records only)
- `selected_referral: ReferralView | null`
- `follow_ups: Page[ReferralFollowUpView] | null`

No implicit `follow_ups` when a Referral is not selected. Selected Referral must have the exact requested Case ID or return masked `404 REFERRAL_NOT_FOUND`; it is not a join or a Provider dispatch. The client must not treat the response as a frozen snapshot. Mutation via workspace URL is unsupported.

## Implementation and security

Create an application-layer composition of three **existing public services** (Casework, Referrals, ReferralFollowUps). Never reach across modules to their DB tables or invent one cross-context transaction. Every called read retains its existing Case lock/current assignment and authorization. Preflight the intersection of all three existing read-capability families; fail closed for AI even with apparent grants. Follow-up record text is returned **only** to a specifically authorized reader; do not place text in Outbox, public API metadata or AI datasets. No permission registry/grant changes.

Do not use the read response to claim a stable multi-service decision snapshot; new data can be appended between owner service reads. No new temporal cutoff, status/priority, external trigger, or outcome inference.

## Verification

PostgreSQL-backed tests for all three pagination dimensions independently, safe selected-referral membership, missing permission for each family, AI and wrong-assignee denial, explicit oversight, stale Caregiver after reassignment, read-only side effects, invalid cursor/limit, HTTP anonymous rejection, exact OpenAPI response and container smoke. Existing suite from PR #20 must remain green. Stage-like container smoke is NOT hosted Stage.
