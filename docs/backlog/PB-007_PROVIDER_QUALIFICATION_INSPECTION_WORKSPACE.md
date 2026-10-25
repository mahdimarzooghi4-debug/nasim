# PB-007 — Provider Qualification Inspection Workspace

Status: **ACCEPTED FOR SPRINT PLANNING** under SG-007 / T-007 (bounded informational composition).

- BL-007-01 (P0): Provide strict typed read model joining only existing three Provider Registry views, with independently bounded keyset pagination and no evaluation fields. DoD: exact T-007 shape, no Provider/Case/Referral state change.
- BL-007-02 (P0): Enforce intersection of three existing read capabilities on trusted ActorContext; block AI even with grants; reject anonymous, cross-actor and malformed queries. DoD: negative-path tests for each capability, actor type and missing Candidate.
- BL-007-03 (P0): End-to-end PostgreSQL-backed service and HTTP regression for independent cursors, cross-candidate isolation, no side effects and OpenAPI. DoD: integration evidence and exact-head CI green.
- BL-007-04 (P1): Record bounded technical review and ensure Draft PR and all D-0130 exclusions are respected.

**Explicit exclusions:** qualification decision/review action, reviewer identity, evidence pinning policy, activation, service selection, Case/Referral data access, provider dispatch, AI, thresholds, SLA, external integration, UI, Stage/Release/Production.
