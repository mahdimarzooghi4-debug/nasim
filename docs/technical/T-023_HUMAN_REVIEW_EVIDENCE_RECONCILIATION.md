# Sprint 023 — Human review evidence reconciliation (offline, fail-closed)

Date 2026-10-09. Source: D-0160 (owner reports **the Nasim Operations Manager personally reviewed all 84 examples**) and D-0161 (Operations Manager is the organizational Training Eligibility decision authority). Base: unmerged Draft PR #34; previous main unchanged.

## SG-023 Business
Product Owner's report that review took place is **accepted** and must not be re-asked. Distinguish this from (a) each of the 84 review **outcomes**, (b) exact pinned version and reviewer evidence reference, (c) decisions on two proposed author edits, (d) source/content rights and health/safety specialist review where required, and (e) Training/Evaluation or Production admission. No outcome has been supplied in the conversation: NEVER invent 84 content ACCEPT records.

The Operations Manager is the organizational decision owner for use of real Nasim data in Training. This does not supersede lawful purpose, consent or authority evidence, Data Class approval, exclusions and retention/withdrawal, or reviewer roles distinct from the case-data author. See BC-007, Issues #12/#13.

## T-023 Technical contract
Offline `reconcile_initial_review_evidence()` validates externally supplied review *metadata*: complete exact 84 reviewed source IDs + their canonical row SHA-256, matching inventory digest and source commit, claimed Operations Manager role, opaque batch/item review evidence references, timezone-aware timestamps, and content outcomes limited to `CONTENT_ACCEPTED`, `REWRITE_REQUIRED`, `CONTENT_REJECTED` (technical representation of the three options in AI-BOOT-003, **not** a final policy to include examples in Training). Reject unknown/stale/duplicate/missing IDs, unsupported disposition, unsafe metadata and untrusted extra grant fields. Proposed edit evidence is optional and never auto-applied; patch outcomes are descriptive only.

**Critical:** the evidence file is a self-declaration; a hash checks integrity/coverage but **does not** authenticate a real manager or prove signature, review authority or legal basis. Therefore the resulting status ALWAYS remains `FORMAT_AND_COVERAGE_CHECKED_EXTERNAL_AUTHENTICITY_UNVERIFIED`, `dataset_status=NOT_APPROVED`, partition `UNASSIGNED`, no Training Run, no Promotion. Only opaque counts and digest are emitted; source texts, reviewer names, consent records, elder data and full evidence references are omitted.

Required external metadata shape (schema exemplar only — these values are NOT real evidence):

```json
{
  "schema": "nasim.synthetic-human-review-evidence.v1",
  "source_commit": "faf33342497ec23f7c0969930ce808787e476be6",
  "inventory_sha256": "<real digest from trusted inventory>",
  "reviewer_organizational_role": "NASIM_OPERATIONS_MANAGER",
  "review_batch_evidence_ref": "<real external approved restricted reference>",
  "records": [
    {
      "record_id": "<one of 84 canonical IDs>",
      "record_sha256": "<pinned canonical source row digest>",
      "outcome": "CONTENT_ACCEPTED|REWRITE_REQUIRED|CONTENT_REJECTED",
      "evidence_ref": "<real restricted evidence reference>",
      "reviewed_at": "<actual timezone-aware timestamp>"
    }
  ],
  "patches": []
}
```

The example is incomplete and MUST NOT be used as an actual evidence file. Reference destination and permissions must be real. Never paste actual reviewer personal identifiers/PII or secrets in GitHub.

Offline CLI from `backend/`: `uv run --locked python -m nasim.learning.inspect_review /approved/local/review-metadata.json`. No file is provisioned, no IdP selected (Keycloak preference only), no runtime API, no DB schema, no Dataset created.

## PB-023 / Sprint 023 / delivery controls
Scope: Decision Register update D-0160..0161, review evidence parser and CLI, exhaustive tests of 84/duplicates/staleness/role/purpose coercion and tamper, full CI, non-approving technical Code Review. Exclusions: creating sample outcomes, fabricating reviewer signatures, inventing real legal data eligibility, changing source flags, real Dataset partitions, Training/Model/AI API, Provider workflow, Hosted Stage (D-0130), merge absent independent code approval.
