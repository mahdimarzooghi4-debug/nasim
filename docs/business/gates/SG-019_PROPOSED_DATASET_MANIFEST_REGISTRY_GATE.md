# SG-019 — Inert Proposed Dataset Manifest Registry

Status: **Technical foundation only / not approved learning data**, 2026-10-09.

Sources: Sprint 018 SG-018/T-018/PB-018 pure opaque, deterministic manifest core; draft BC-007 (eligibility/legal basis/consent/curation and approval authority **OPEN**), BC-006 controlled internal AI. Upstream branch PR #30 HEAD `b252b46e0b1c57824d780b220d682958fa1a46d8`, still Draft/unmerged.

This gate admits **only** a migration-versioned durable registry for *proposed* technical dataset manifest digests and exact, opaque source/version attestations. No real Dataset, TrainingRun, model, routing, inference, autonomous learning or eligibility decision is authorized. Runtime has neither read nor write privileges to registry tables, no route, scheduler, Dataset Builder, default verifier, consent assumption, source connector, outbox consumer, artifact export or production callback.

The registry writes only behind an explicitly injected `AdmissionVerifier` (there is **no deployed implementation**). All positive tests use synthetic UUIDs and a synthetic admission stub, never real data. The proposal store must fail closed before connecting to the database if verifier is absent. Concurrent identical requests must be idempotent. Persisted records are append-only, protected by database triggers. Read verifies the full pinned digest and member count. A database identifier/digest by itself is not proof of legal authority or independent Evaluation.

A distinct future Business decision must authorize source classes, legal basis, independent consent/withdrawal and purpose limits, curator identity/quality and review, Dataset approval, de-identification, retention/access, household-level Training/Evaluation independence and responsible AI usage before **any** actual automated Dataset formation. Do not invent numeric thresholds or providers.

Lifecycle: Business SG-019 → Technical T-019 → Backlog PB-019 → Sprint 019 → code/real PostgreSQL tests → exact-head CI → technical nonapproving review. No Merge/Ready/Hosted Stage/QA/Release/Production under D-0130 without explicit owner instruction. All source PRs remain Draft/Open.
