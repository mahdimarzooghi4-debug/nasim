# STAGE-001 — Repository-side Stage Foundation

- **Status:** READY FOR STAGE REVIEW; review/admission is not claimed.
- **Base:** `main` at `e97f01eb17aaf864b263c451fe3fb86690fc77aa`.
- **Branch:** `stage-foundation`.
- **Scope:** repeatable packaging, configuration and Stage-like validation for the existing TS-03 backend.
- **Governance:** [D-0130](../DECISIONS.md) still applies. Hosted Stage is **UNAVAILABLE**; this foundation does not pass Stage Admission, QA, Release or Production.
- **Source:** [T-001](../technical/T-001_TS03_CORE_CASE_JOURNEY_TECHNICAL_BASELINE.md), [Code Review PASS](../sprints/SPRINT-001_CODE_REVIEW_RESULT.md), [product process](../PRODUCT_PROCESS.md).

## Delivered foundation

`backend/Dockerfile` is a multi-stage Python 3.12 image. Official Python/uv/PostgreSQL base
images have resolved digest pins; uv is 0.12.19. Runtime dependency installation uses
`uv sync --locked --no-dev --no-install-project`; application source is imported directly
from `/app/src`, avoiding an unlocked package build backend. `backend/uv.lock` and dependency
versions are unchanged. The image contains neither uv nor Pytest/Ruff/Pyright/httpx.
UID/GID 10001 runs Uvicorn; application/migration source ownership remains usable even on
restricted-permission cloud checkouts. Compose makes the runtime filesystem read-only,
provides a temporary `/tmp`, drops capabilities and enables no-new-privileges.

The Stage factory uses `StageSettings`, exclusively from process environment variables.
It has no dotenv loading or development fallback. Missing/invalid configuration fails before
serving. Errors do not reflect submitted credentials. `NASIM_ENVIRONMENT=stage` is explicit;
a PostgreSQL runtime DSN with host, database, username and password is required. Loopback,
known development credentials/databases, unsupported drivers and unfilled example
placeholders are rejected. Single-destination `postgresql://` and `postgresql+asyncpg://`
are supported. Secrets never belong in tracked configuration or image build arguments.

`compose.stage.yaml` is separate from `compose.yaml`. Its explicit project name gives it a
separate network and **stage_pgdata** volume; PostgreSQL has no host-published port.
`postgres` is Docker's internal service discovery name in this validation composition,
not a chosen external domain or hosted DNS record. A small PostgreSQL image copies an
initialization script that creates the externally supplied runtime role for a fresh volume.
Existing volumes retain their data and role credentials; environment edits do not rotate
an existing database password automatically.

A one-shot `migrate` container uses the **same backend image** with a distinct owner DSN,
upgrades Alembic to head, runs `alembic check`, and grants bounded runtime access. Its login
is not injected into the serving container. The runtime role must pre-exist without
superuser/role-creation/database-creation/replication/bypass-RLS or destructive table/audit
privileges. The application receives SELECT/INSERT and only the column UPDATE permissions
needed for assignment ending and aggregate locking. History triggers still prohibit actual
Case/audit/history overwrites. Backend startup depends on successful migration and healthy
PostgreSQL. The serving command itself never runs migrations. The explicit image command is
`bash /app/stage-migrate.sh`, backed by `backend/scripts/stage-migrate.sh` and the validated
Python migration module; migration failures exit nonzero.

Readiness remains `/health`: HTTP 200 and `{"status":"ok"}` require database connectivity
and current revision `0006_provider_qreview` (the historical Stage Foundation started from `0001_ts03`). A missing/unavailable/wrong-revision database returns 503.
The image includes an HTTP readiness healthcheck. All anonymous business operations still
fail closed; no identity adapter, self-asserted identity headers or authentication bypass
was added. The hosted identity integration boundary remains TS-05.

## Configuration contract

No variable below has a credential or hosted-address default. The committed
`backend/stage/validation.env.example` contains **REPLACE_ placeholders only**; it cannot
successfully boot a Stage factory unchanged. Supply values from an external environment
or a protected, untracked configuration file, without shell tracing or printing them.
Percent-encode reserved characters when constructing DSNs; raw database initialization
password variables and decoded DSN passwords must identify the same login.

| Variable | Consumer / purpose |
| --- | --- |
| `NASIM_ENVIRONMENT=stage` | Stage backend and migration factories; Compose sets this explicit profile |
| `NASIM_DATABASE_URL` | Restricted runtime PostgreSQL DSN; mandatory for Stage |
| `NASIM_MIGRATION_DATABASE_URL` | Migration owner DSN; same host/port/database, distinct username; migration container only |
| `NASIM_STAGE_PROJECT` | Explicit isolated validation Compose project name |
| `NASIM_STAGE_IMAGE` | Explicit local validation image tag or approved image reference |
| `NASIM_STAGE_DB_NAME` | Compose validation database name |
| `NASIM_STAGE_MIGRATION_USER` / `NASIM_STAGE_MIGRATION_PASSWORD` | Initial Compose owner login; supplied externally |
| `NASIM_STAGE_DB_USER` / `NASIM_STAGE_DB_PASSWORD` | Initial restricted Compose runtime login; supplied externally |
| `NASIM_STAGE_BIND_ADDRESS` / `NASIM_STAGE_HTTP_PORT` | Explicit validation HTTP binding; no hosted exposure policy is assumed |
| `NASIM_STAGE_SMOKE_URL` | HTTP address reachable by the local/CI smoke runner |
| `NASIM_STAGE_COMPOSE_OVERRIDE` | Optional external build/network override for an existing managed proxy |
| `NASIM_STAGE_ARTIFACT_DIR` | Optional external diagnostics directory; retained on failure |

The local/CI composition is validation infrastructure, not a hosted deployment configuration.
Its database initialization inputs are not needed by an already provisioned hosted database;
that database administrator provisions its owner and restricted runtime roles separately.
Hosted serving needs only the Stage profile/runtime DSN and whatever approved trust/network
configuration the selected infrastructure requires.

## Local validation

Use the existing checkout; cloud tasks are already isolated. Do not create a Git worktree
unless explicitly requested. Preserve existing user changes. Prerequisites: Python 3.12,
uv, Docker/Compose v2 with BuildKit, and access to the pinned image/package registries.
From the repository root:

```bash
# Existing tests use their own development/test composition, not the Stage-like database.
bash backend/scripts/setup-dev.sh
bash backend/scripts/validate-migrations.sh
bash backend/scripts/check.sh

# Prepare an external environment file from the placeholder template, then edit it.
cp backend/stage/validation.env.example /tmp/nasim-stage-validation.env
chmod 600 /tmp/nasim-stage-validation.env
# Replace every REPLACE_ entry with your explicit local validation inputs.
# Choose a loopback HTTP bind for local-only testing, a free port, a unique project name,
# internal service host postgres in both validation DSNs, and distinct DB roles.
set -a
source /tmp/nasim-stage-validation.env
set +a
export NASIM_STAGE_SMOKE_URL="http://${NASIM_STAGE_BIND_ADDRESS}:${NASIM_STAGE_HTTP_PORT}"
bash backend/scripts/stage-validate.sh
```

For **disposable local/CI validation only**, public sentinel strings such as the
`CI_ONLY_NOT_A_SECRET_*` values in the workflow are intentionally not secrets. Never use
them for Hosted Stage or any real data. No hosted credential is generated by these scripts.
Supply actual hosted credentials through the infrastructure's external secret mechanism
once its owner has selected and authorized it; do not commit or chat-post their values.

`stage-validate.sh` builds both images, waits for database/migration/backend readiness,
checks non-root runtime/no development packages/restricted database role/current migration,
runs real HTTP smoke, restarts backend, reruns the repeatable migration command and compares
full schema dumps before/after. Only pg_dump's randomized `\restrict`/`\unrestrict` client
tokens are normalized; schema definitions must match exactly. HTTP smoke is repeated after
restart. It checks `/health=200`, anonymous POST `/api/v1/cases=401` with
`ACTOR_CONTEXT_REQUIRED`, anonymous reads, exact TS-03 OpenAPI paths/methods, and GET/POST
404s for excluded Enrollment/Referral/Provider/Outcome/Emergency/AI routes.

The script stops/removes its own validation containers on exit and preserves the data volume.
On failure it retains diagnostic logs and schema dumps in an external protected artifact
directory (`NASIM_STAGE_ARTIFACT_DIR`, default `/tmp/${NASIM_STAGE_PROJECT}-stage-validation`).
It preserves the failing command's exit status; successful cleanup is also required.
The script preserves validation data. To stop this project's services without deleting data:

```bash
docker compose -f compose.stage.yaml down
```

`down --volumes` destroys the selected project's validation data; reserve it for explicitly
disposable CI/test projects. Do not use test-suite truncation/downgrade commands on a Stage
database containing real data. Full Pytest continues to use only the separate `nasim_test` DB.

### Managed cloud build proxy

This cloud machine's Docker build required its already injected egress proxy, DNS mapping
and existing CA trust bundle. TLS and locked artifact checksums remained enabled. A
**build-only** external Compose override can set backend `build.network`, `build.args`
(`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` inherited from the existing environment), resolved
proxy `build.extra_hosts`, and `build.secrets: [proxy_ca]`. Define the top-level `proxy_ca`
secret's `file` as the existing trusted CA bundle path. Set
`NASIM_STAGE_COMPOSE_OVERRIDE` to that external file for repeatable validation here.
No proxy URL/credential, trust bundle or external DNS mapping is committed. On ordinary
CI networking this override is unnecessary. Never disable TLS verification or add guessed
proxy destinations. The optional BuildKit CA mount is not copied into the runtime image.
A hosted database's approved CA/TLS policy remains an external deployment input.

## CI workflow

[`.github/workflows/backend-ci.yml`](../../.github/workflows/backend-ci.yml)
runs for relevant PRs, pushes to `main`/`stage-foundation`, and manual dispatch. It uses
Python 3.12, resolved SHA-pinned checkout/setup actions, uv 0.12.19, contents-read permission
and no hosted cloud secrets or deployment permissions. Each job validates:

1. `quality`: frozen installation, Ruff, Ruff format check and Pyright (including CI provisioning helper).
2. `test`: a real PostgreSQL service, dedicated `nasim_ci_test` database, migration and restricted `nasim_app` role, then full Pytest including integration/race/OpenAPI/Stage tests.
3. `migration`: a separate PostgreSQL service/test database; upgrade → downgrade base → upgrade and `alembic check`.
4. `container-stage-smoke`: after all three jobs pass, build images, boot independent Stage-like composition, run real HTTP and restricted runtime checks, restart and verify no schema drift.
5. Preserve failure diagnostics in job logs; remove only the smoke job's disposable Compose data. GitHub manages the separate test/migration service containers.

Workflow credentials are explicitly public **CI-only sentinel values** used to initialize
its disposable local databases. They are not Hosted Stage secrets and are never promoted.
The workflow does not publish an image, provision infrastructure, deploy or approve a gate.
PRs do not receive hosted credentials. CI cancellation isolates each run's Stage project by
run ID/attempt. GitHub-hosted workflow results must be checked for the exact pushed SHA
during Stage Review; local execution evidence alone does not claim an Actions run passed.
API inspection initially encountered a managed-proxy CONNECT 403. Access subsequently
became available using the existing injected GitHub binding; no duplicate token was
requested. The first pushed commit triggered the workflow and its run was inspected.

## Validation evidence from this change

- Base `main` refreshed and matched the user-supplied SHA; no incompatible external changes.
- **152 Pytest passed**: all original 124 plus 28 Stage configuration/readiness tests; no skips/failures.
- Ruff and format checks passed; Pyright zero errors/warnings. GitHub workflow syntax also passed actionlint.
- Readiness negative tests cover unreachable DB, missing revision table and incorrect revision, returning 503 without weakening existing tests.
- Test-only Alembic upgrade → downgrade base → upgrade and metadata check passed.
- Backend image built with Python **3.12.15**, exact locked runtime dependencies, no dev dependencies.
- Independent PostgreSQL **17.11** composition booted; migration completed before serving.
- Runtime UID was non-root and DB role was restricted; revision `0001_ts03` confirmed directly.
- Real HTTP smoke passed before and after backend restart; full schema dump comparison was unchanged.
- The separate CI-style PostgreSQL service/provisioning helper was exercised locally too: all 152 tests, quality checks and test-only migration cycle passed there.
- Dependency declarations/lockfile and original tests were not modified.
- Hosted Stage was not provisioned. GitHub Actions execution status is independent of these local checks.

## Hosted Stage inputs still required

These are prerequisites for a later hosted environment, not blockers for this repository
foundation. An authorized owner must supply:

- Hosting/runtime choice, operational owner, resources, region/placement, persistence and backup/restore requirements.
- Approved immutable image delivery location/reference and access mechanism if a private registry is used.
- Provisioned PostgreSQL endpoint/database and distinct restricted-runtime/migration roles; their credentials through external secret storage/injection.
- Approved network exposure/access controls, database connectivity and TLS/trust policy. Supply approved DNS and certificates only if the chosen access model requires them; none are selected here.
- Logging/monitoring, availability, restore/rollback ownership and retention policy.
- Explicit Stage admission/review authorization and evidence from an actual hosted Stage.
- A trusted identity integration decision when authenticated hosted business journeys are required; TS-05 remains the governing boundary. Anonymous acceptance remains denial.

No provider, external DNS, actual certificate or production-like secret is invented. No
AWS/Azure/GCP/Render/Fly/Railway/Kubernetes or other infrastructure is selected/provisioned.
There is no Production deployment, business feature, TS-03 expansion or identity provider.

## Migration and rollback procedure

For a provisioned environment, use the **approved built image** for a single serialized
migration job with externally supplied `NASIM_ENVIRONMENT`, `NASIM_DATABASE_URL` and
`NASIM_MIGRATION_DATABASE_URL`:

```bash
bash /app/stage-migrate.sh
```

Run only after the database administrator has provisioned the two distinct roles. The owner
performs Alembic DDL; serving uses only the restricted runtime role. Back up the database to
an external protected location and test restore before any destructive migration. Do not
serialize secrets into shell history, logs, image layers or tracked files.

If migration/schema validation fails, serving must remain stopped/unready. Inspect the
failure, preserve database evidence and retry only after correcting its prerequisite.
Never force a revision with `alembic stamp` to hide schema drift. A backend-only rollback
must use a previously approved immutable image **only if compatible with the current
schema**; readiness and smoke must pass after replacement. If schema is incompatible,
restore the approved database backup under the owner-approved recovery procedure before
starting the compatible image. No previous hosted image or recovery policy is guessed here.

`0001_ts03` is the initial schema: **downgrade to base drops all nine TS-03 tables and their
data**. The automated downgrade test is exclusively on a dedicated `*_test` database.
It is not a safe default hosted rollback. Do not run it against retained Stage/Production
data without an explicit recovery plan, verified backup and authorization.

## Stage entry checklist — still pending review/admission

- [x] Sprint 001 Code Review PASS is recorded.
- [x] Repository-side container/config/migration/smoke foundation exists and was locally validated.
- [ ] GitHub Actions successful for the exact reviewed/pushed SHA.
- [ ] Stage Foundation review accepted; no automatic main merge.
- [ ] Hosted runtime/database/network/secret inputs supplied and authorized.
- [ ] Actual Hosted Stage provisioned, persistent storage and backup/restore verified.
- [ ] Correct immutable image, migration revision, restricted roles and health verified there.
- [ ] Fail-closed identity and TS-03 route boundaries verified there; authenticated scope separately authorized if needed.
- [ ] Actual restart/rollback evidence and operational ownership recorded.
- [ ] Explicit Stage Admission decision recorded before Stage-based QA/Release claims.

Stop at **Stage Review**. D-0130 remains unchanged until a real Stage environment and its
entry evidence exist; this document does not revise the delivery process or grant release approval.


## TS-05 compatibility update

Sprint 002 adds the authenticated-only `GET /api/v1/authorization/self` inspection
contract and five authorization tables in `0002_ts05`. Current smoke verifies this
explicit API surface and anonymous self inspection remains 401. All original TS-03
routes and exclusions remain checked. Serving has SELECT-only authorization table
access; migration fails closed if its runtime role has authorization write privileges.
Original STAGE-001 validation evidence above describes its reviewed historical SHA;
Sprint 002 validation evidence belongs to its own Code Review handoff.


## Sprint 003 compatibility update

Current historical Sprint 003 schema was 0003_referral, following the original TS-03 and TS-05 migrations.
Exact smoke contract now includes the three Referral create/list/detail operations;
anonymous Referral requests remain 401 and lifecycle mutations remain absent (404).
Existing TS-03/TS-05 routes and exclusions are preserved. Original review/validation
records above remain historical evidence for their exact SHAs, not a new Stage gate.
The change does not provision Hosted Stage or alter D-0130.


## Sprint 004 compatibility update

Current repository schema is `0004_provider_candidate`. The Stage-like smoke contract now
includes Provider Candidate register/list/detail routes, verifies anonymous denial, and verifies
that operational Provider mutation routes remain absent. Shared audit/outbox `case_id` is nullable
only so non-Case bounded contexts can emit technical effects; existing Case/Referral events retain
their Case linkage. The runtime role receives bounded SELECT/INSERT access to
`provider_candidate_record` and no destructive privilege. This remains repository-side
validation only; Hosted Stage is still unavailable under D-0130.


## Sprint 005–006 compatibility update

The current repository schema head is `0006_provider_qreview`.

Stage-like smoke now includes Provider Qualification Evidence and Provider Qualification
Review Request record/list/detail surfaces. Anonymous access remains fail-closed and
qualification decision/approval/activation routes remain absent. Runtime database access
is limited to bounded SELECT/INSERT for the new immutable provider-registry tables.

This is repository-side validation only. It does not create a Hosted Stage and does not
change D-0130, Stage Admission, QA, Release or Production status.
