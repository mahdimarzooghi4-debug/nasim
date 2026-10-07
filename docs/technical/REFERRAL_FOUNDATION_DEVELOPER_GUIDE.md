# Referral Foundation developer guide

Scope and OPEN decisions: SG-003, T-003, PB-003 and Sprint 003. This records entry
of a current NEED_CAPTURE into a future Referral process; it does not dispatch,
activate a Provider, create a state machine, final approval, consent or funding rule.

## Contracts and bounded contexts

CreateReferral has source_need_observation_id, expected_current_assignment_id and
nonblank reason. ReferralView has only the eight record/provenance fields. Extra
fields are rejected. ReferralRecord is append-only: no PATCH/DELETE/correction API.
TS-03 public CaseReferences exposes current assignment and validated current Need
identifiers in the caller's transaction, not persistence ownership or Need free text.
Current = no successor under existing observation lineage; no new current-status flag.
A later source correction preserves historical referrals referencing their original
source. No cascade rewrite, new status or invalidation policy is inferred.

Three TS-05 definitions are registered in 0003_referral, with SYSTEM migration audit:
referral.create.assigned, referral.read.assigned, referral.read.oversight. No grants,
actor assignments, named mappings or bootstrap admin are seeded. Existing trusted
principal/ActorContext boundary remains; no self-asserted HTTP auth or external IdP.
AI is denied even with an erroneous grant. System/Automation must have explicit
permissions and current assignment, never get authority by actor type. Final Business
policy/mapping remains OPEN. Internal provisioning examples exist ONLY as isolated
test fixtures, not deployable policy or public management commands.

## HTTP surface

- POST /api/v1/cases/{case_id}/referrals: 201, requires Idempotency-Key.
- GET same route: bounded cursor Page[ReferralView], default 50, max 100.
- GET /api/v1/referrals/{referral_id}: immutable record inspection.

Creation requires referral.create.assigned plus current assignment and expected ID.
Assigned reads require referral.read.assigned plus current assignment. Oversight reads
require referral.read.oversight; a title or existing Case oversight permission alone
is insufficient. Anonymous requests stay 401. Only Case event vocabulary is returned
by TS-03 timeline; Referral audit details cannot bypass Referral read guards through it.

Errors preserve CAPABILITY_REQUIRED, ASSIGNED_CAREGIVER_REQUIRED,
CASE_ASSIGNMENT_CHANGED, STALE_RECORD_REVISION,
IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD. Additional source failure:
NEED_CAPTURE_REQUIRED (422), RECORD_NOT_FOUND (404), REFERRAL_NOT_FOUND (404).

## Atomicity and source races

Idempotency scope: actor ID, ActorType-partitioned referral.record operation, Case,
key. Hash includes the full normalized command. Same key/body returns same result;
different body is 409. Assignment authorization/source currentness are rechecked on
cached retries. A reassigned actor or superseded source fails closed on retry.
Distinct keys may record multiple referrals for the same Need: no source uniqueness
because multiplicity policy is OPEN.

Transaction order: advisory idempotency lock → TS-03 Case row lock → source check →
Referral → shared audit/outbox/idempotency → commit. Existing Case corrections and
reassignment use the same Case lock. DB source trigger repeats lock/type/current checks;
composite FK enforces same-case lineage. Deferred guard requires matching effects at
commit; UPDATE/DELETE history triggers and runtime privileges reject destructive changes.
referral.recorded.v1 contains IDs and actor/time/correlation only, no Need/reason free text.
It means recording, not acceptance or dispatch. TS-05 request snapshot semantics remain;
no new policy for already-issued contexts/live revocation is silently introduced.

## Run and validate

From repository root: bash backend/scripts/setup-dev.sh and
bash backend/scripts/validate-migrations.sh (dedicated *_test only, destructive).
From backend, supply the documented NASIM_TEST_DATABASE_URL / NASIM_TEST_APP_DATABASE_URL
and run uv run --locked pytest, ruff check ., ruff format --check ., pyright.
Dependencies/uv.lock unchanged. Alembic head is 0003_referral, following 0002_ts05.
Stage-like Docker smoke uses the existing external-input STAGE-001 procedure and
backend/scripts/stage-validate.sh; health expects 0003_referral and checks exact API,
anonymous Referral denial and absent lifecycle/Provider/Service/Emergency/AI routes.

Downgrade 0003→0002 drops Referral data; export/approve a rollback plan before any
non-test use. It removes only unused migration permission seeds. If explicit grants
or later permission revisions exist, downgrade fails closed before deleting history.
An approved migration/data plan is then needed; never weaken the guard for green tests.
Base downgrade cycle is disposable-test-only. No Hosted Stage or Production action.

## OPEN

Final referral authorization/Role mapping, Provider selection/acceptance, lifecycle,
SLA/escalation, cancellation/closure/reopen, cost approval, consent, Emergency,
Referral correction, multiplicity constraints remain OPEN (not accepted/deferred).
