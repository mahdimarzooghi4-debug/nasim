# Sprint 001 — Code Review evidence

- Stage: **Code Review requested**; no review/Stage/QA/Release approval claimed.
- Branch: `sprint-001-ts03-core-case-journey`.
- Refreshed `main` and remote Sprint branch: both `83df114d798c76639d21ff2a79338d24fba7e0b6` before delivery; no incompatible external changes.
- Scope: BL-001…BL-012 under T-001, TG-001, PB-001 and the accepted Sprint handoff.

## Verification in the actual cloud machine

Python 3.12.14; PostgreSQL 17.11 via Docker Compose with a digest-pinned official image.
Exact Python dependency versions are committed in `backend/uv.lock` and were resolved and
installed on Python 3.12. Installation uses the frozen lock.

| Check | Result |
| --- | --- |
| Full Pytest | **124 passed**, zero failures/skips/xfails; 67 PostgreSQL/REST integration tests + 57 contract/OpenAPI/identity tests |
| Ruff | Passed |
| Ruff format | Passed |
| Pyright | Zero errors/warnings |
| Package build | Wheel and source distribution built successfully |
| Alembic | `0001_ts03`: upgrade → downgrade base → upgrade passed on dedicated test DB |
| Schema comparison | `alembic check`: no new upgrade operations |
| OpenAPI | Exact intended paths/methods, typed requests/responses, required idempotency headers, correction fields, errors and excluded fields verified |
| Live server | Uvicorn started; real HTTP health returned 200 and `status=ok`; anonymous mutation returned 401 `ACTOR_CONTEXT_REQUIRED` |
| Repository setup | Repeatable `setup-dev.sh`, restricted role grants and `check.sh` exercised |

## Backlog evidence

| Item | Delivered |
| --- | --- |
| BL-001 | Installable backend, locked dependencies, settings, DB-backed health and quality tools |
| BL-002 | Trusted ActorContext, abstract capability/assignment guards; default denial, no identity header bypass |
| BL-003 | Atomic post-enrollment Case + profile + initial assignment |
| BL-004 | Reassignment, actor/time/reason, immutable history, unique active assignment |
| BL-005 | Append-only contact revisions with logical-contact lineage |
| BL-006 | CONTACT/MONITORING records and superseding corrections |
| BL-007 | OBSERVATION/NEED_CAPTURE and superseding corrections |
| BL-008 | Immutable audit, identifier/provenance outbox in domain transaction |
| BL-009 | Current workspace, histories and paginated chronological audit timeline |
| BL-010 | All 9 POST and 7 GET business operations, typed OpenAPI and stable errors |
| BL-011 | PostgreSQL race/integrity/rollback and REST authorization matrix |
| BL-012 | Developer setup/start/migration/test/operations instructions and scripts |

## Race and integrity results

All contenders use independent real SQLAlchemy sessions/PostgreSQL connections:

- Reassignment with six competing keys: one accepted winner, five `CASE_ASSIGNMENT_CHANGED`; exactly one active assignment and no loser audit/outbox/idempotency rows.
- Eight simultaneous identical Case creations with one key: eight identical results, one Case/assignment/audit/outbox/idempotency record.
- Six different creation payloads with one key: one winner, five `IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD`.
- Four competing profile corrections: one winner, three `STALE_RECORD_REVISION`, old revision preserved.
- Six simultaneous identical reassignments with one key: one state change and six identical responses.
- Direct database tests reject duplicate active assignment/idempotency scope, cross-Case and cross-contact lineage, missing correction reason and orphan revisions.
- Failure injected after business + audit/outbox flush rolls everything back. Failed reassignment restores the original active assignment.
- Ordinary administrative SQL UPDATE/DELETE is rejected by immutable-history triggers. The tested runtime role cannot DELETE/TRUNCATE history or UPDATE audit.

## Boundaries and review considerations

No unresolved Business decision or environment blocker prevented this Sprint implementation.
No Enrollment eligibility, Case lifecycle, Referral/Service/Provider, Outcome/Reassessment,
Emergency, AI runtime/Dataset Builder, named-role RBAC or SQLite fallback was implemented.

Identity provider/named-role mapping is intentionally TS-05. Current production-facing
identity dependency fails closed until trusted in-process middleware supplies ActorContext;
test identity injection is confined to test dependency overrides. This is an integration
boundary, not an anonymous/development authentication mode.

Outbox is persistence-only, per T-001. No delivery worker/broker is required for TS-03.
Deployment and production credentials are outside this development Sprint. Database role
owners must preserve the least-privilege separation documented in the backend guide.
Review must still assess T-001 compliance, access predicates, transaction/concurrency
semantics and migration safety. Stop here: do not merge main or promote to Stage automatically.
