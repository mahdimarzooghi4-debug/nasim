# T-007 — Provider Qualification Inspection Workspace

Status: **read-only foundation**, SG-007. Continue the existing Python 3.12 / FastAPI / PostgreSQL modular monolith. No migration or state mutation.

## Contract

`GET /api/v1/provider-candidates/{candidate_id}/qualification-review-workspace`
Query: `evidence_cursor?`, `request_cursor?`, `limit=50` (1..100). Each cursor is the **existing** base64 timestamp+UUID keyset token for its own list; bad cursors return existing `422 INVALID_CURSOR`.

Response is exactly:
- `candidate: ProviderCandidateView`
- `evidence: Page[ProviderQualificationEvidenceView]`
- `review_requests: Page[ProviderQualificationReviewRequestView]`

Two independent, bounded, ascending time/UUID pages. The client must not treat the composite read as an immutable evidence snapshot. No calculated decision/status/label, queue, counts implying sufficiency or qualification. No cross-context joins/FKs. Do not expose hidden audit/outbox/idempotency payloads.

## Enforcement

Trusted ActorContext required; **all three** existing read capabilities required, checked before existence or cursor validation. AI denied even if granted. Missing candidate returns existing `404 PROVIDER_CANDIDATE_NOT_FOUND`. Page bound returns `422 INVALID_PAGE_LIMIT` at service boundary. Read under a database transaction; no write, no audit or outbox side effect. Do not claim transaction is a pinned review evidence set.

## Tests

- Complete candidate + both descriptive lists on one read.
- Independent next cursors and absence of cross-candidate records.
- Missing candidate, anonymous access and forbidden capabilities (each missing individually).
- AI denied despite all grants; invalid service limits/cursors fail 422.
- No mutation of Candidate, Evidence, Request, Audit, Outbox or Idempotency rows.
- OpenAPI response shape and non-existent decision/activation routes.

No migration, new permission, registry seed or Stage.
