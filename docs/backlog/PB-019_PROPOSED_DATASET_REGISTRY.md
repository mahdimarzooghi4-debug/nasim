# PB-019 — Proposed Manifest Persistence Technical Foundation

Only technical invariants admitted by SG-019/T-019:
- LEARN-019-01 create versioned PostgreSQL proposed manifest and source schemas using opaque hashes/UUID references, not raw operational payload.
- LEARN-019-02 append-only DB triggers, DB CHECKs and FK/unique keys; non-destructive rollback guard.
- LEARN-019-03 never grant serving runtime any privilege on proposed registry; separate owner/worker future decision remains open.
- LEARN-019-04 deterministic atomic persisted proposal and idempotent concurrent replay, full content verification on read, reject corrupt/extra membership.
- LEARN-019-05 require explicitly injected independent verifier, default deny; do not wire any production source, scheduler, HTTP endpoint, Training, Model or consent/eligibility stub.
- LEARN-019-06 real migrated PostgreSQL tests with synthetic references, replay, tamper, runtime permission checks; CI including schema migration upgrade/downgrade and full regression.
- LEARN-019-07 draft technical Code Review only and no merge/stage/production.

Blocked prerequisites: accepted lawful basis and purpose/source policies, consent/withdrawal and provenance, independent curation, approved source authority, privileged worker, automatic Dataset builder and eligible source triggers, de-identification, Training/Evaluation household isolation, model evaluation/promotion and external production infra.
