# PB-020 — Source-purpose partition collision guard

Trace: SG-020 → T-020 → Sprint 020. Priority: prevent persisted cross-purpose exact-ID contamination before future approved learning ingestion.

Acceptance: database-enforced one purpose per opaque source identity across all proposed manifests (even concurrent and direct SQL insert); immutable claims, same-purpose versions/replays, fail-closed migration of historic conflicts, no unintended runtime rights, PostgreSQL regression, entire CI and non-approving code review.

Exclusions: any eligibility decision, household lineage assertion, legal basis, consent, data read, dataset production, training or AI runtime, or new user-facing state. PR Draft/Open only; no Stage/Release.
