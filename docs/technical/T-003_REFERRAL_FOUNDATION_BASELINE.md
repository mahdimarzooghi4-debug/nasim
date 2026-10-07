# T-003 — Referral Foundation Technical Baseline

Status: FOUNDATION ONLY under SG-003 and explicit user implementation authority.
Modular monolith, Python 3.12/PostgreSQL, existing locked stack. Separate Referral
bounded context; TS-03 exposes reference contracts and a transaction-scoped adapter
for current assignment/current NEED_CAPTURE. Referral never owns Case/Observation.

ReferralRecord: id, case_id, source_need_observation_id, created_at,
created_by_actor_id/type, reason, correlation_id. Immutable, no state/status,
provider/service ID, SLA, priority/severity or cost fields. Same-case composite FK,
nonblank reason/correlation/actor, ActorType check, source type/currentness DB guard,
and UPDATE/DELETE history protection. Source is valid at recording time; a later
TS-03 correction does not rewrite or invalidate a historical referral.

CreateReferral requires source UUID, expected_current_assignment_id and nonblank
reason; extra fields forbidden. Permission referral.create.assigned AND current
assignment must match the actor. Current means no successor in TS-03 observation
lineage. Missing/cross-case source: RECORD_NOT_FOUND; ordinary observation:
NEED_CAPTURE_REQUIRED; superseded source: STALE_RECORD_REVISION. Stale assignment:
CASE_ASSIGNMENT_CHANGED. Existing capability/assignment/idempotency error codes persist.

Three versioned registry codes only: referral.create.assigned, referral.read.assigned,
referral.read.oversight. No role grants. Existing TS-05 resolver feeds ActorContext.
AI denied regardless of grant. System/Automation require explicit capability and
current assignment like any other actor, not inferred Business authority.

POST /api/v1/cases/{case_id}/referrals (201), GET same route (paginated),
GET /api/v1/referrals/{referral_id} (bounded detail). Assigned reads require permission
and current Case match; oversight read is capability-only, no job-title inheritance.
No lifecycle/management/correction mutations. Anonymous remains 401, no new auth adapter.

Transaction lock order: idempotency advisory scope → existing TS-03 Case row lock.
Source correction/reassignment use the same Case lock. Recheck assignment/source even
on cached retries: fail closed if preconditions are now stale. Hash exact body; scope
actor ID + ActorType-partitioned operation + Case + key, independent of Need count. Same payload retry returns same
record; different payload 409. Multiple different keys may create multiple referrals
for one Need because multiplicity is OPEN. No hidden unique source constraint.

Business record + shared technical audit/outbox/idempotency are one transaction.
referral.recorded.v1 contains IDs, ActorType/time/correlation only; no Need free text.
Event is record evidence, not dispatch/acceptance. Shared effect persistence is platform
infrastructure, not cross-domain ownership. History of TS-03 audit remains append-only.

Migration 0003_referral follows 0002_ts05 (no parallel chain). Test downgrade restores
TS-05 definitions. Serving gets bounded SELECT/INSERT only on Referral, no destructive
privileges. Readiness/exact OpenAPI/Stage smoke advance explicitly. Test source lineage,
authorization, retries/races, correction/reassignment races, rollback and DB protections.
Request-time ActorContext retains the reviewed TS-05 snapshot semantics; no stronger
live-revocation Business policy is silently added.


TS-03 timeline is explicitly restricted to its existing Case event vocabulary;
case.read.* alone cannot disclose Referral recording reason/audit through that route.
The shared technical audit store does not imply cross-context read authorization.
DB deferred guards additionally require matching audit/outbox/idempotency at commit.
0003→0002 rollback removes migration vocabulary seeds only when no grant or revised
permission depends on them. Otherwise it fails closed and needs an approved data plan;
it never silently deletes real authorization history. Disposable base migration cycles
remain authorized test validation, not a hosted rollback procedure.
