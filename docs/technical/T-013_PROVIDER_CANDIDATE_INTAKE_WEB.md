# T-013 — Provider Registry Human Intake (No Qualification Decision)

- Status: FOUNDATION / exact existing HTTP contract only.
- Build: React+TS same-origin POST adapter, frontend read-only Candidate screens extended with secure human intake forms. No backend migration or endpoint addition.

Server methods:
1. `POST /api/v1/provider-candidates` -> 201 ProviderCandidateView; `display_name`, `reason`; explicit `provider_candidate.register`.
2. `POST /api/v1/provider-candidates/{candidate_id}/qualification-evidence` -> 201 ProviderQualificationEvidenceView; `evidence_label`, `evidence_reference`, `reason`; explicit `provider_qualification_evidence.record`.
3. `POST /api/v1/provider-candidates/{candidate_id}/qualification-review-requests` -> 201 ProviderQualificationReviewRequestView; `reason`; explicit `provider_qualification_review.request`.

Backend alone validates actor, permission, Candidate identity, transactional audit/idempotency/outbox. UI enables commands only for HUMAN ActorContext with exact action capability; registration does not confer Candidate read access. Evidence/review request forms only appear for a selected Candidate that the actor may inspect. Any missing Candidate or denied grant fails closed with 401/403/404. The UI makes no implicit "approved", "verified" or "active" interpretation and never changes persisted official state except those explicit immutable records.

Use browser crypto UUID Idempotency-Key bound to exact submitted form body; preserve across uncertain network failures until edited, then rotate. Accept only 201 application/json, no redirects or raw backend error text. On success clear form and re-fetch; on 401 drop protected UI; on 409 do not guess and do not retry automatically.

Real browser IdP, server-side Origin/CSRF protections, approved consent/data-sharing policy, real document evidence provenance, Provider decision criteria and human authority, browser E2E and Stage must be independently specified and validated later. `credentials: same-origin` is not CSRF protection.

Tests: TS strict, path/headers/payload and 401/403/409/no mock production data, authorized SSR conditional, Web CI exact SHA plus all inherited 4 Backend CI jobs. No new schema/roles/capabilities.
