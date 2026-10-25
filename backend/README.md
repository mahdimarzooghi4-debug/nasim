# Nasim backend — implementation and development guide

The backend uses Python 3.12, FastAPI, PostgreSQL, async SQLAlchemy 2.x, Alembic and Pydantic v2. Work through Sprint 025 is merged into `main`; the backend includes the assigned-caregiver daily-routine foundation. This README documents the original TS-03 Case foundation and its boundaries. It is not a complete product/API inventory. Hosted Stage remains unavailable under D-0130, and no Stage QA or Production release is claimed.

The original TS-03 scope is described in [T-001](../docs/technical/T-001_TS03_CORE_CASE_JOURNEY_TECHNICAL_BASELINE.md).

## Start a development environment

Run these commands from the current checkout. Keep local changes intact when switching branches; implementation work should follow the repository's current branch/PR workflow rather than the original Sprint 001 branch instructions.

Prerequisites: Python 3.12, `uv`, Docker with a working daemon and Docker Compose v2.
From the repository root:

```bash
bash backend/scripts/setup-dev.sh
bash backend/scripts/start-dev.sh
```

Setup installs `backend/uv.lock` with `uv sync --locked`, starts the checksum-pinned
PostgreSQL 17.11 container, creates a separate test database if needed, upgrades both
databases and grants a restricted application role. Setup is safe to repeat; it does not
reset development data. Start serves FastAPI on loopback port 8000. Internal readiness:

```bash
curl --fail --silent http://127.0.0.1:8000/health
```

Expected response: `{"status":"ok"}`. Health verifies database connectivity and migration
revision `0010_care_routines`; it returns 503 if unavailable/unmigrated. Processes must be restarted
in future cloud tasks; an installed dependency or retained database volume is not a live
service. Stop only the server you started (Ctrl-C). `docker compose stop postgres` stops
the repository's database without removing its volume.

The Compose database is bound to loopback port 55432. Its public, development-only login
values are in `compose.yaml` and `scripts/setup-dev.sh`; never reuse them in production.
The application uses the non-superuser `nasim_app`, not the migration owner `nasim`.
`NASIM_DATABASE_URL` overrides the application's default development connection.
`UV_CACHE_DIR` defaults to `/tmp/nasim-uv-cache` for read-only-home cloud environments.
No GitHub token, broker or external API credential is required for this slice.

## Identity boundary

`identity_context.ActorContext` is the trusted, immutable identity contract. An upstream
in-process authentication adapter can set `request.state.actor`; all business endpoints
reject requests without that context with 401. TS-05 owns the identity provider and named
role mapping. This Sprint does not implement an identity provider, accept self-asserted
identity/capability headers, or supply a development authentication bypass. Consequently,
a standalone server's anonymous business requests are intentionally denied. Tests inject
ActorContext using FastAPI dependency overrides **only in the test process**.

Assignment ownership does not grant permission. Operations require both current assignment
and the appropriate abstract capability. The assignment manager capability authorizes
creation, reassignment and bounded profile-reference correction; oversight permits TS-03
reads only. `case.create` by itself does not authorize initial assignment. Contact-point
commands require `case.contact.manage.assigned`; CONTACT/MONITORING records require
`case.monitor.assigned`; observations require `case.observe.assigned`. Reads require
`case.read.assigned` plus assignment match, or `case.read.oversight`. AI actors are denied
even if incorrectly granted a TS-03 capability. Family/Provider/Employer/Elder identities
receive no default capability grants. Job titles are absent from the authorization model.

## Check and migrate

```bash
# From the repository root; setup must have completed first:
bash backend/scripts/validate-migrations.sh
bash backend/scripts/check.sh

# Independent tests without PostgreSQL:
cd backend
UV_CACHE_DIR=/tmp/nasim-uv-cache uv run --locked pytest -m 'not integration'
```

`check.sh` runs **all** Pytest tests against the restricted application role and dedicated
`nasim_test` database, then Ruff, Ruff format checking and Pyright. PostgreSQL integration
fixtures truncate only the explicit `*_test` database using its administrative login;
never point them at a development or production database. The `integration` marker is
skipped when `NASIM_TEST_DATABASE_URL` is absent; a unit-only pass does not validate DB
behavior. The full script sets both `NASIM_TEST_DATABASE_URL` (migration/test owner) and
`NASIM_TEST_APP_DATABASE_URL` (restricted runtime role). Override both for another test
server. The app test role is named `nasim_app` so privilege tests can verify its grants.
Tests are sequential by default; race tests intentionally create multiple real connections.
Do not run multiple test suites against the same database concurrently.

`validate-migrations.sh` checks upgrade → downgrade to base → upgrade and `alembic check`.
**Downgrade destroys the dedicated test database's TS-03 data.** The script refuses database
names not ending in `_test`, and restores local runtime grants after recreating tables.
For custom servers their administrator must apply equivalent grants separately.
For a normal development upgrade:

```bash
cd backend
export NASIM_DATABASE_URL='postgresql://nasim:nasim_dev_only@127.0.0.1:55432/nasim_dev'
UV_CACHE_DIR=/tmp/nasim-uv-cache uv run --locked alembic upgrade head
```

Migration `0001_ts03` creates nine tables: `elder_case`, `case_profile_revision`,
`contact_point_revision`, `case_assignment`, `case_interaction`, `case_observation`,
`audit_entry`, `outbox_event`, `idempotency_record`. Use a migration owner distinct from
runtime authentication. `dev/grants.sql` demonstrates local least-privilege grants:
SELECT/INSERT, UPDATE only `case_assignment.ended_at`, and UPDATE on `elder_case.id` solely
for SELECT FOR UPDATE (immutable trigger rejects actual modification). Runtime must not
own tables, be a superuser or have DDL/TRUNCATE privileges. Append-only triggers reject
normal UPDATE/DELETE of history, audit, original Case and idempotency rows. Assignment
history permits only ending an active assignment. An administrative owner can perform
explicit migrations; these protections are not a defense against a database administrator.

To refresh dependencies, edit declared compatibility constraints deliberately, run `uv lock`,
then rerun validation and commit the new lock. Exact resolved versions are in `uv.lock`;
installation does not guess package versions or regenerate the lock.

## Structure and integrity

```text
src/nasim/
  domain/             typed commands, views and errors (no persistence imports)
  identity_context/   ActorContext and capability/assignment predicates
  application/        ElderCase transactional commands, queries, cursors
  infrastructure/     PostgreSQL ORM models, sessions, environment settings
  api/                REST adapter, injected identity, error/OpenAPI contracts
migrations/           frozen initial schema + immutable-history triggers
scripts/              repeatable setup/start/check/migration validation
 tests/               contracts, OpenAPI, REST, PostgreSQL integrity/race tests
```

The application owns one bounded ElderCase aggregate. API handlers delegate to its public
commands/queries; persistence models stay inside the application/infrastructure boundary.
All nine mutations persist business state + audit + outbox + idempotency result in one
transaction. Versioned outbox events contain identifiers, provenance and lineage, not
contact values or note content. No broker or event consumer is implemented in TS-03.

Idempotency is scoped by actor id, operation, target Case and key. Canonical JSON includes
the typed payload and route resource id. Same key/payload returns the accepted response;
different payload gives 409. Transaction-scoped PostgreSQL advisory locks handle absent-row
races, and a unique constraint independently prevents duplicate scope rows. Current
capability and assignment authorization are rechecked before cached sensitive responses.

Mutations lock the Case row and compare `expected_current_assignment_id`. Reassignment ends
the current row and inserts its successor, preserving history; a partial unique index
ensures at most one active assignment. Profile/contact corrections require
`expected_current_revision_id`. Interaction/observation correction paths refer to the
current record and also require `expected_current_record_id`. Stale requests fail closed.
Read transactions lock the same aggregate to avoid returning data after a concurrent
assignment revocation. Corrections append new actor/time/reason-bearing rows with
same-Case (and for contacts same-logical-contact) lineage foreign keys. Originals remain
readable. No normal destructive edit/delete API exists.

Workspace returns current profile, profile history, active assignment and current records.
Contacts endpoint returns all contact revisions; interaction/observation lists return
immutable history. Timeline combines all nine mutation types through their audit entries.
The three paginated lists use ascending `(recorded_at/timestamp, UUID)` keyset cursors;
`limit` is 1–100, default 50. Cursors are opaque positions, not authorization or immutable
snapshot tokens; every page rechecks Case authorization.

## HTTP contract

Every POST requires `Idempotency-Key`. All existing-Case commands require
`expected_current_assignment_id`. Unknown body fields, invalid record types, naive timestamps
and blank correction reasons are rejected with 422. Errors use
`{"error":{"code":"...","message":"..."}}` without reflecting submitted personal data.
OpenAPI is generated from the typed request and response contracts.

| Method | Path under `/api/v1/cases` | Result |
| --- | --- | --- |
| POST | root | Case, first profile and active assignment |
| POST | `/{case_id}/profile/corrections` | New profile revision |
| POST | `/{case_id}/reassignments` | New assignment |
| POST | `/{case_id}/contacts` | First contact revision |
| POST | `/{case_id}/contacts/{logical_contact_id}/corrections` | New contact revision |
| POST | `/{case_id}/interactions` | CONTACT or MONITORING record |
| POST | `/{case_id}/interactions/{interaction_id}/corrections` | Superseding interaction |
| POST | `/{case_id}/observations` | OBSERVATION or NEED_CAPTURE record |
| POST | `/{case_id}/observations/{observation_id}/corrections` | Superseding observation |
| GET | `/{case_id}` | Case/current profile/assignment |
| GET | `/{case_id}/workspace` | Current TS-03 workspace and profile history |
| GET | `/{case_id}/assignments` | Assignment history |
| GET | `/{case_id}/contacts` | Contact revision history |
| GET | `/{case_id}/interactions` | Paginated interaction history |
| GET | `/{case_id}/observations` | Paginated observation history |
| GET | `/{case_id}/timeline` | Paginated chronological audit timeline |

Stable conflicts: `CASE_ASSIGNMENT_CHANGED`, `STALE_RECORD_REVISION`,
`IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD`. Authorization errors:
`ACTOR_CONTEXT_REQUIRED`, `CAPABILITY_REQUIRED`, `ASSIGNED_CAREGIVER_REQUIRED`.

## Current scope and release boundary

The repository includes completed code through Sprint 025, including the Case, Referral, Provider, learning-metadata and assigned-caregiver daily-routine foundations. Read the relevant technical guides and Decision Register for the current slice contracts; the historical TS-03 sections below describe that slice, not every current capability.

The repository does not yet provide an end-to-end operational service lifecycle, real Provider activation, a production-connected identity provider, or a live Hosted Stage. The learning metadata is not an operational Dataset Builder, Trainer, Evaluation pipeline or Model Registry. Existing operational events and synthetic examples do not automatically qualify for AI training or evaluation.

Do not infer operational authority from a technical record, role name, CI result or merged code. Provider qualification/activation criteria, official published AI content, lawful source-specific Training eligibility, actual identity grants and first Phase/Pilot scope remain separate business or infrastructure inputs. See the [Pre-Stage Readiness Register](../docs/business/PRE_STAGE_COMPLETION_READINESS_REGISTER.md).

Code review and main-branch CI have completed for the merged work. Hosted Stage admission, independent Stage QA, Release approval and Production are later gates; D-0130 still blocks Hosted Stage until a real environment is provisioned.

## Stage Foundation

The provider-neutral container, explicit Stage environment contract, independent validation
composition and GitHub Actions pipeline are documented in
[STAGE-001](../docs/stage/STAGE-001_ENVIRONMENT_FOUNDATION.md). This repository-side
foundation is distinct from Hosted Stage; D-0130's Stage-unavailable decision remains in
force until actual provisioning and admission. It adds no identity or TS-03 business feature.


## TS-05 Identity / Authorization foundation

See [TS-05 developer contract](../docs/technical/TS05_DEVELOPER_GUIDE.md).
The current repository migration head is `0010_care_routines`. Care routines are exposed to assigned caregivers through `/api/v1/cases/{case_id}/care-routines`; app reminders and caregiver-required tasks remain distinct. The API records explicit occurrence status and does not infer an outcome from no response. Notification delivery and elder self-access are not included in this backend slice. The registry seeds vocabulary only;
no actor-role assignments or role-permission grants are seeded. The serving DB
role has read-only access to authorization tables. External authentication and
public management commands remain outside scope.


## Sprint 003 Referral record foundation

See [Referral developer guide](../docs/technical/REFERRAL_FOUNDATION_DEVELOPER_GUIDE.md).
Migration `0003_referral` adds immutable `referral_record` and three technical
permission definitions, with no role/actor grants. Only record create/list/detail
APIs are added. Provider selection, lifecycle, delivery and final authorization
policy remain OPEN. The serving role receives SELECT/INSERT, never UPDATE/DELETE.


## Provider Candidate foundation

Sprint 004 adds a pre-operational, immutable Provider Candidate registry. A candidate record is
not an activated Provider, has no Service eligibility or Referral selection authority, and does
not grant Case/Elder access. The Provider Candidate migration is `0004_provider_candidate`.


## Provider Qualification Evidence foundation

Migration `0005_provider_qe` adds immutable, opaque qualification evidence references for
existing Provider Candidates. Evidence existence does not create a qualification decision,
approval, activation or Service eligibility.

## Provider Qualification Review Request foundation

Migration `0006_provider_qreview` adds immutable review-request records only. A request
does not assign a reviewer and does not mean reviewed, qualified, approved or active. The
only new technical permissions are `provider_qualification_review.request` and
`provider_qualification_review.read`; no Role → Permission grant is seeded.
