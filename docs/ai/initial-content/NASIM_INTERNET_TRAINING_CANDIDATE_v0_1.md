# Nasim Internet-derived training candidate package — v0.1.0

- **Package ID:** `NASIM-TRAIN-CANDIDATE-001`
- **Status:** `CANDIDATE_NOT_AUTHORIZED`
- **Created:** 2026-10-25
- **Record count:** 10
- **UTF-8 JSONL SHA-256:** `2e2cf32352d2402b42ec334006007c094e516d051104b8b76923dbfb7ae26250`
- **Source inventory blob SHA-1:** `34b35d892b42051833b14c2a0d59f8d10a1002e2`
- **Source repository revision:** `c2dba855a88f5295af3b044a37098344b19b6880`

## Scope

On 2026-10-25, the Operations Manager selected all 10 Internet-derived records across five sources for the internal Training-candidate path. This derivative separates them from the 84-record internal Evaluation-only synthetic set.

This file is a **candidate package**, not an approved Training Dataset. Every outer record has:

- `candidate_state: CANDIDATE_NOT_AUTHORIZED`
- `training_permission: NOT_AUTHORIZED`
- `evaluation_permission: NOT_AUTHORIZED`
- `runtime_publication_permission: NOT_AUTHORIZED`
- `partition: UNASSIGNED`

Original source candidate records are preserved under `record`; their content and original review flags are not rewritten. The Operations Manager accepted the summarized Persian content scope for JMIR records 001–004. Source facts for all 10 candidates were checked against the publisher/official pages on 2026-10-25; this does not replace Persian-language review for records 005–010.

## Source inventory

| Source | Records | Exact source snapshot/hash | Remaining source review |
|---|---:|---|---|
| JMIR Aging, CC BY 4.0 | 4 | Pending | Attribution verification and exact snapshot/hash capture |
| GOV.UK healthy-ageing guide, OGL v3.0 | 1 | Pending | Exact snapshot/hash, inspect third-party material, attribution, and England-to-Nasim localization |
| MDPI family-support study, CC BY 4.0 | 1 | Pending | Exact snapshot/hash, attribution, and Persian review |
| Springer/BMC caregiver study, CC BY 4.0 | 2 | Version-of-record PDF SHA-256 recorded per record | Attribution/third-party credit-line review and Persian review |
| Bentham social-support study, CC BY 4.0 | 2 | PDF SHA-256 recorded per record | Attribution and Persian review |

The official source license statements and source-fact findings are documented in `NASIM_INTERNET_SEED_RIGHTS_EVIDENCE_v0_1.md`. The GOV.UK page specifically warns that third-party content may require separate permission. The research summaries are not Nasim policy, service facts, or individualized care advice.

## Admission gates

Before these candidates can enter any Training Dataset, each source needs exact-version evidence, attribution/rights review, and completed human Persian/content review. Any source-specific exclusion or unresolved rights condition keeps its records unauthorized. Separate data admission and Training authorization must be recorded before T-026 or any Training workflow can use these records.

No model loading, inference, Training, Evaluation Run, runtime publication, or Production action was performed while preparing this package.
