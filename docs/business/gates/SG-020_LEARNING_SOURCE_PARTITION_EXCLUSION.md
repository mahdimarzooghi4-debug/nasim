# SG-020 — Persisted source-purpose partition exclusion

Status: **technical safety admission only**. Based on draft BC-007, BC-006, accepted SG-018/019 safety scopes, and Sprint 019 immutable proposed manifest registry. No Business eligibility, legal basis, household identity or Dataset approval is accepted by this document.

**Problem:** T-018 compares one Training/Evaluation manifest pair in memory. The proposed registry could store two separate, conflicting purposes for one opaque source key, including concurrent proposals.

**Admitted scope:** one durable technical claim per exact `(namespace, source_id)`, sourced from the parent's already-recorded TRAINING/EVALUATION purpose. It must be append-only and enforced inside PostgreSQL for every insert, even privileged writers. Same-purpose replay and distinct source versions remain allowed. Existing conflicting rows prevent upgrade; no silent cleanup. A failed competing proposal leaves no header/source row.

**Not admitted:** household/member-level separation, linked relatives, temporal leakage, consent/withdrawal, source eligibility, admission verifier, Dataset Builder scheduling, Training Run, Evaluation, AI service, real data, policy defaults, or model promotion. Exact source-ID separation is necessary but **not sufficient** to authorize evaluation. The current serving runtime still has no read/write rights on all three learning tables.

Gate: Business SG-020 (safety only) → Technical T-020 → Backlog PB-020 → Sprint 020 → PostgreSQL tests → exact-head CI → non-approving technical review. PRs remain Draft/Open; Stage D-0130 unavailable. No merge/deploy without explicit authorization.
