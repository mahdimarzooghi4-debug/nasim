# T-002 — TS-05 Identity / Authorization Technical Baseline

Status: FOUNDATION BASELINE under SG-002 and explicit user instruction.

Versioned immutable RoleDefinition and PermissionDefinition use logical codes,
revision number and same-code predecessor foreign keys. Assignments and explicit
grants pin exact definition versions; no version automatically inherits authority.
Assignment principal identity includes actor ID and ActorType. Start/end windows
are explicit. Ending preserves original row, adds end provenance, and creates
append-only audit in the same transaction; replacement references the same logical
actor/role or role/permission pair. DB uniqueness forbids duplicate unended pairs,
including expired reservations until explicitly ended. Revocation is irreversible.

Internal persistence commands are trusted provisioning primitives, NOT authorized
public management APIs. Their caller must supply an externally approved authority
and recorded ActorContext. No role mapping or bootstrap administrator is seeded.
Runtime serving can SELECT authorization tables; it cannot manage grants.

Resolver is one PostgreSQL statement/snapshot, using database statement time:
Actor+type → active assignments → active explicit grants → registered permissions.
No role/expired/revoked grant = empty. No wildcards. AI TS-03 capabilities stay denied.
Overlapping concurrent changes resolve wholly before or after commit, never through
a multi-query mixed snapshot. Resolution is request-time, not a persistent token;
no claim that already-issued ActorContext is live-revocable inside a running command.
That stronger transaction-bound enforcement remains an explicit future design question.

Trusted in-process authenticated principal → resolver → immutable ActorContext →
existing TS-03 guards. No HTTP identity headers/JWT/password/IdP. Existing trusted
in-process ActorContext integration remains supported. GET authorization/self exposes
only the caller's resolved context, no other actor or management authority.

case.create is registered but reserved: T-001 §5 and Casework require
case.assignment.manage for atomic creation + initial assignment. Do not silently
change existing behavior; case.create alone does not authorize creation. The decision
whether it becomes an additional/alternative guard remains OPEN.

Alembic 0002_ts05 follows 0001_ts03; immutable history and atomic audit constraints.
Readiness and smoke track the current schema head. Upgrade/downgrade test must
restore TS-03 unchanged. Preserve all existing authorization and concurrency checks.
