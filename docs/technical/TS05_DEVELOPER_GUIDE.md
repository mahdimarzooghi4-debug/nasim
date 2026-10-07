# TS-05 developer contract

See SG-002, T-002, PB-002 and Sprint 002. All Business role-to-permission and
management-authority questions remain OPEN; D-0126 is not declared closed.

## Registry and persistence

`0002_ts05` follows `0001_ts03`. Five tables: role_definition,
permission_definition, role_permission_grant, actor_role_assignment,
authorization_audit. Immutable definitions have code/revision/predecessor. The
13 source-backed vocabulary entries cite BC-005 §§1/5 and DC-003 §§1/3; their
existence is not a final Pilot inventory. Seven exact T-001 TS-03 permission codes
are registered. Registry seeds create SYSTEM migration audit only, ZERO grants
and ZERO actor assignments. Public serving cannot INSERT/UPDATE authorization data.

Assignments include actor ID AND type, exact role revision and explicit start/expiry.
Grants pin exact role and permission revisions. End preserves initial provenance
and adds end actor/type/time/reason/correlation. Replacement is a new row with
same-pair predecessor; no overwrite/delete. Unended rows reserve their pair even
if future/expired; explicitly end them before replacement. Revocation is one-way.
DB constraints, triggers and deferred matching audit enforce uniqueness, lineage,
immutable history and atomic audit, including direct SQL attempts under normal writes.
Privileged destructive test migration/TRUNCATE is not a serving operation.

## Internal provisioning is not management authorization

`Provisioning.register/grant/assign/revoke` are trusted internal persistence/domain
primitives. They are NOT public authorized commands and are not reachable over HTTP
or shipped as a bootstrap-management CLI. The caller must obtain approved management
authority outside these primitives; passed ActorContext is provenance, not a grant
of management authority. Until that Business decision closes, use only migration
vocabulary registration and isolated test fixtures. Never deploy test grants as policy.
Definition registration only accepts source vocabulary and exact TS-03 registry codes.
Conflicts: AUTHORIZATION_CONFLICT or STALE_AUTHORIZATION_REVISION (409).

## Resolver and authentication boundary

`AuthorizationResolver.resolve(TrustedPrincipal)` executes ONE SELECT with DB statement
time/snapshot; output ActorContext is immutable. Roles with no grants give no capability;
expired/revoked/future windows give none; role/permission revisions do not inherit.
AI stays denied TS-03, including accidental explicit grants. Other actor types require
explicit assignment and grant, never gain authority solely from their type.
Trusted middleware may populate `request.state.trusted_principal` ONLY after external
authentication. No adapter/provider/auth flow is implemented here. Existing trusted
in-process ActorContext injection remains compatible. Client headers cannot populate
request.state, and spoofed identity/JWT headers still get 401. Malformed installed
principal fails closed instead of falling back to an existing actor.

GET `/api/v1/authorization/self` returns only the resolved caller ActorContext.
There is no other-actor inspection or authorization management mutation endpoint.
TS-03 guards remain unchanged: assigned caregiver AND capability. Case creation still
requires case.assignment.manage (T-001 §5); case.create is reserved registry vocabulary,
not a new guard. Its future meaning requires a Business/technical reconciliation.

Resolution is request-time and not cached in a token. A principal resolution sees either
committed before or committed after a concurrent revoke. An ActorContext already issued
to an in-flight command is a snapshot, not a promise of transaction-bound live revocation.
That stronger TOCTOU policy is not silently invented and remains a future design question.

## Repeatable validation

From repository root: `bash backend/scripts/setup-dev.sh`, then
`bash backend/scripts/validate-migrations.sh` (destructive *_test DB only).
From backend, set documented NASIM_TEST_DATABASE_URL and NASIM_TEST_APP_DATABASE_URL,
then `uv run --locked pytest`, `uv run --locked ruff check .`,
`uv run --locked ruff format --check .`, `uv run --locked pyright`.
Full Pytest must run from backend (or specify its pyproject pytest config).
All existing tests remain; expected schema revision and exact OpenAPI surface advance
with the explicit migration/self contract, never by disabling assertions.
Stage-like validation: use STAGE-001 external-input procedure and
`bash backend/scripts/stage-validate.sh`. No Hosted Stage/Production admission.
Downgrade 0002→0001 removes authorization tables/history only; export and authorize
rollback first. Downgrade base is strictly disposable test validation.
