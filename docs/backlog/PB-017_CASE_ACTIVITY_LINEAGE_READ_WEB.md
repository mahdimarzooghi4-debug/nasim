# PB-017 — Case History & Traceability Read UI

Status: implementation backlog of existing TS-03 read contracts only.

- CASE-017-01 P0: Case reader can view bounded historical technical AuditEntry Case actions with actor, time, reason, correlation and before/after resource lineage.
- CASE-017-02 P0: already-authorized reader can view actual assignment start/end history; display not a service/outcome verdict.
- CASE-017-03 P0: inspect immutable Interaction correction records and `supersedes_interaction_id` via bounded pagination.
- CASE-017-04 P0: inspect immutable Observation/Need correction records and `supersedes_observation_id` via bounded pagination.
- CASE-017-05 P0: independent cursors, stable empty/loading/denied states, cancellation on tab change, refresh from server, no stale cached fallback or inferred merged snapshot.
- CASE-017-06 P0: exact existing Case read permission and HUMAN only in UI, Backend-per-request authorization remains final; no actor, cookie or grant bypass.
- CASE-017-07 P0: tests for URL/permissions/failed reads/SSR and full exact-head Web+Backend CI; nonapproving Draft PR review.

Exclusions: new lifecycle states, global cross-domain audit claims, Provider/referral acceptance, verified Outcome, clinical decision, AI dataset ingestion, retention policies, new DB, hosted Stage, deployment and Figma acceptance.
