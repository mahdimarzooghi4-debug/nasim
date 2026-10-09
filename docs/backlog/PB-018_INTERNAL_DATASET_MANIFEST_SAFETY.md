# PB-018 — Internal AI Dataset Manifest Safety Core

Stage: implementation backlog under SG-018/T-018. Zero approved Production Dataset sources.

- LEARN-018-01 P0: define typed, opaque, immutable technical CuratedSourceRef without free-text inputs, manifest identity and clearly non-approved/proposed status.
- LEARN-018-02 P0: require independent injected AdmissionVerifier; production default is DENY, no self-proclaimed approval; no source import, no endpoint, no artifact.
- LEARN-018-03 P0: reject zero entries, duplicate source identity, malformed SHA-256, missing/stale/surplus attestation and unsupported purposes.
- LEARN-018-04 P0: hash deterministic sorted canonical manifest with version identity pinned to policy/approval/source attestations. Replays are identical; changes create distinct proposed versions.
- LEARN-018-05 P0: reject exact source overlap in Training vs Evaluation even across versions; explicitly do NOT claim household-level leakage prevention.
- LEARN-018-06 P0: synthetic-only test suite, exact-head Backend/Web CI, technical Code Review without false acceptance of eligibility or model.
- LEARN-018-07 BLOCKED: legally approved purpose/source/consent/withdrawal/curation, real admission evidence registry, automated Dataset Builder with persisted version and lineage, independent Evaluation Dataset and Human Promotion. No guessed implementation.

Excludes: real data ingestion, model selection, AI decision, Production candidate, external AI API, schema migration, default 'eligible' classification, routine dataset export or policy changes.
