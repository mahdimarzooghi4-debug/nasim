# T-010 — Assigned Case Operational Index (read-only)

Status: **Technical read foundation**, bounded by SG-010 and existing TS-03 access.

## Contract

`GET /api/v1/cases?limit=50&cursor=<opaque>` returns `Page[CaseProfileView]` using exactly the existing typed Case/Profile/current Assignment read models. Only GET is added to the existing `/api/v1/cases` POST route; no new mutations or migration. Cursor is existing strict timestamp+UUID format, sorted ascending by `elder_case.created_at, elder_case.id`; 1..100 bounds and `422 INVALID_CURSOR` on malformed values.

For each Case, select its **unended current** Assignment (`ended_at IS NULL`) and latest ProfileRevision by **highest revision_no**. One PostgreSQL statement reads Case, Assignment and Profile under one committed statement snapshot. Do not issue a separate per-item authorization query that could generate mixed snapshots or an N+1 loop. Cursor is not a frozen dataset snapshot; created Cases/reassignments between page requests may change visibility.

## Security

Require existing `case.read.assigned` or `case.read.oversight` from trusted ActorContext. If explicit oversight exists, show records the existing Casework.read('profile') oversight policy allows; otherwise require `Assignment.caregiver_actor_id=actor.actor_id` in the *SQL WHERE*. Deny AI even if erroneously granted. Anonymous 401; no caller-supplied caregiver ID or arbitrary actor filters. Mere current assignment, manager grant or role title cannot see data without read capability. No extra permission seeding.

No status, urgency, SLA, need count, Referral state, Provider or AI data added. The index query is read-only and must not mutate domain/audit/outbox/idempotency rows.

## Test contract

Real PostgreSQL: mixed caregivers, oversight/assignment-manager/no-permission/AI, latest profile after correction, independent bounded pagination and malformed cursors, current assignment revocation and new assignee visibility, empty results, no side effects, HTTP/OpenAPI and anonymous container smoke. No schema migration, no Stage, no credentials or production deployment.
