# T-020 — Concurrent durable source-purpose exclusion

Source: SG-020, draft BC-007, T-018 and T-019. Only metadata safety, not an operational Dataset Builder.

Migration `0009_learning_partition_claim` adds `learning_source_purpose_claim(namespace, source_id, purpose)` with primary key `(namespace,source_id)`, purpose TRAINING/EVALUATION and immutable UPDATE/DELETE trigger. One PostgreSQL BEFORE INSERT trigger on `learning_proposed_source` derives purpose from the parent manifest and atomically reserves the exact source key via INSERT ... ON CONFLICT DO NOTHING. After the concurrent-unique fence, it reads the persisted claim and rejects any opposite purpose with SQLSTATE 23514. A contradictory historical registry fails the upgrade rather than being grandfathered. Existing row updates/deletes remain forbidden; no source data is copied or exported.

`ProposedManifestRegistry.propose` maps **only** the known trigger conflict to `TRAINING_EVALUATION_SOURCE_OVERLAP`; unexpected DB errors propagate. Same-purpose separate manifest versions and concurrent idempotent replay remain possible. A transaction failure rolls back all new metadata. The runtime database role is forbidden to read or write the new table in dev/CI and Stage-like provisioning.

Tests: same and changed-version overlap, concurrency opposite and same purpose, direct SQL bypass attempt, immutable trigger and serving role denial, migration upgrade/downgrade/check, existing full regression. All identifiers in tests are synthetic UUIDs with synthetic admission only.

**Limit:** absence of exact source-key overlap is not household or lineage independence. No actual eligibility/legal/consent verifier is installed; no approved Dataset, ingestion, training, evaluation, or promotion can run from this work.
