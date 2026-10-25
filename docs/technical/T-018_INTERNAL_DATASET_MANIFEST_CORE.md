# T-018 — Deterministic Dataset Manifest Core (Not a Dataset Builder Runtime)

Status: **policy-neutral and dormant infrastructure**.

Package `backend/src/nasim/learning/dataset_manifest.py`:
- `CuratedSourceRef` contains ONLY opaque `namespace`, immutable UUID source identifier, source version SHA-256 and curation evidence SHA-256. It does not contain raw free-text, sensitive field values, inferred labels or eligibility flags.
- `DatasetAdmissionRequest` requires one explicit technical purpose (TRAINING or EVALUATION) and a non-empty immutable source-ref tuple.
- `AdmissionVerifier` is a Protocol ONLY. There is **no Production implementation** and the default builder has no verifier. `AdmissionEvidence` returned by a future reviewed verifier must attest exact full membership and policy/approval evidence digests. Mere supplied digest strings never establish lawful use; a verified external authority is prerequisite.
- `VersionedManifestBuilder.build` rejects duplicate identity across differing versions, unconfigured policy, malformed hash or purported approval, stale/missing/excess membership, empty batches. It sorts independent of input order and derives an idempotent manifest digest and deterministic UUID from purpose, opaque sources, exact source version/curation attestations, and policy/approval evidence digests.
- `verify_partition_isolation` rejects identical source namespace+ID across TRAINING/EVALUATION even across different versions; this is only an **exact-ID technical lower bound** and does not check households, consent, social relationships, time leakage, labels or approved evaluation criteria.
- Proposed immutable manifest is **not** a persisted Dataset, accepted Data Curation, Training Run, model artifact, evaluation or human Production promotion; no fake Dataset is created from Production Outbox.

Limits: no ORM, migrations, HTTP/CLI/API, secret/token, cron/event source, artifact storage, dataset upload, model type/hyperparameters, runtime model execution. Do not add an allowed training class, default inclusion, invented policy version or de-identification method. Approval must be backed by lawful source eligibility and audit, not a caller-supplied self-attestation. Only tests use a `SyntheticOnlyAdmission` stub; it must never be wired to `create_app`.

Next gated stage, once BC-007 decisions are formally accepted: build real source-of-truth policy/approval records, consent/withdrawal and independent curation; implement a real verifying admission service; then automatic idempotent Dataset Version persistence and trigger from approved eligible data; followed by Training/Evaluation/Human Promotion controls, each separately gated. Test with real authorized consent and policy evidence before any real ingestion.

Validation: synthetic no-PII pytest checks default fail closed, SHA format, immutable identity/deduplication, exact policy/evidence membership, deterministic replay, version/partition lineage and overlap; full Backend CI including PostgreSQL regression, Pyright, Ruff and Alembic; unchanged web CI on the same HEAD.
