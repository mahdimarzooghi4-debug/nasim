# T-019 — Immutable Proposed Dataset Registry (Dormant)

A PostgreSQL technical persistence foundation for the Sprint 018 internal opaque Manifest, **not a Dataset Builder or runtime**.

## Schema and invariants

Migration `0008_learning_manifest` from `0007_referral_follow_up`. Tables:
- `learning_proposed_manifest`: content-addressed deterministic UUID PK, unique lowercase SHA-256 manifest digest, TRAINING/EVALUATION purpose, SHA-256 policy and approval-evidence references, positive source count, recorded timestamp. **Proposed only**, no approved state.
- `learning_proposed_source`: compound PK (`manifest_id`, sanitized namespace, UUID `source_id`), attested source-version and curation-evidence SHA-256. No raw Case data, labels, notes, contact values or Provider text. FK RESTRICT.
- SQL CHECKs reject malformed namespace/digests/purpose/count. Shared `nasim_reject_history_change()` trigger blocks UPDATE and DELETE on both tables. Downgrade refuses if stored lineage exists.

No serving runtime SELECT/INSERT/UPDATE/DELETE/TRUNCATE grants on either table. Runtime migration/CI provisioning explicitly checks write privileges absent; dev grants explicitly REVOKE ALL after broad app SELECT. No API, ORM dependency or builder wired to `create_app`, login, background process, Outbox, worker, Training or external storage.

## Internal store

`ProposedManifestRegistry` defaults to **deny without an explicitly injected independent AdmissionVerifier**. The future privileged writer is **not provisioned**. The insert path reuses `VersionedManifestBuilder` exact eligible-membership checks, canonical digest, sorted source identity and policy/approval evidence SHA-256; idempotent content-addressed POSTGRES `INSERT ... ON CONFLICT DO NOTHING`. Inserted header and children commit atomically; concurrent replay reads and compares all returned data before accepting identity. On read, the store reconstructs, checks source count, duplicates, pinned digest and UUID; corrupt historical material fails closed. No automatic semantics of lawful or approved Dataset from successful synthetic storage.

## Verification and non-decisions

Tests use PostgreSQL migration owner only with synthetic evidence, verify determinism, replay concurrency, append-only trigger errors, fail-closed unauthorized runtime reads/writes, tamper detection and default denial. No real client or actual personal information. No dataset automation is activated; BC-007 remains a blocker. Independent household isolation, consent withdrawal, approval identity/attestation and audit governance not implemented. No silent approval or assumed source eligibility.

Production-use gate: future Business accepted BC-007 → verified authorizing policy/evidence source and separate writer identity → idempotent automatic Dataset Version orchestration → independent Evaluation lineage → human model governance. Hosted Stage unavailable D-0130; this version does not relax that restriction.
