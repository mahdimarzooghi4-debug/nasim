# Nasim Internet-derived training candidate package — v0.2.0

- **Package ID:** `NASIM-TRAIN-CANDIDATE-001`
- **Status:** `CANDIDATE_NOT_AUTHORIZED`
- **Created:** 2026-10-25
- **Record count:** 10
- **UTF-8 JSONL SHA-256:** `6233e577ae21b71125047f5f2f4b29d6eddc54076bd51f58587a78e55fbbb074`
- **Source inventory blob SHA-1:** `34b35d892b42051833b14c2a0d59f8d10a1002e2`
- **Source repository revision:** `c2dba855a88f5295af3b044a37098344b19b6880`

## Scope

On 2026-10-25, the Operations Manager selected all 10 Internet-derived records across five sources for the internal Training-candidate path. This derivative separates them from the 84-record internal Evaluation-only synthetic set.

This file is a **candidate package**, not an approved Training Dataset. All ten records remain unauthorized for Training, Evaluation, and runtime publication, and all remain unassigned to a dataset partition. The Operations Manager accepted the summarized Persian content scope for JMIR records 001–004. Source facts for all 10 candidates were checked against official publisher/source pages; this does not replace Persian-language review for records 005–010.

## Source inventory

| Source | Records | Exact source-byte hash | Remaining source review |
|---|---:|---|---|
| JMIR Aging, CC BY 4.0 | 4 | Official Version-of-Record PDF, SHA-256 `b685406284902eaa01005d844be864ea19a5e321592d8c18d22a883fa5b7ea0c` | Attribution verification, Persian review accepted for summary scope only, and purpose-specific eligibility |
| GOV.UK healthy-ageing guide, OGL v3.0 | 1 | Official live HTML response captured 2026-10-25, SHA-256 `270e9c57f3fd666939f33319fa774b00d097fede2b0acea39c0fb941146ab289` | Third-party material/rights, attribution, England-to-Nasim localization, and Persian review |
| MDPI family-support study, CC BY 4.0 | 1 | Official Version-of-Record PDF, SHA-256 `f22d14132728c6cd487d8a8318a23d0a1bba44c152fa01e20c35f8e592c42ca7` | Attribution and Persian review |
| Springer/BMC caregiver study, CC BY 4.0 | 2 | Version-of-Record PDF SHA-256 recorded per record | Attribution/third-party credit-line review and Persian review |
| Bentham social-support study, CC BY 4.0 | 2 | PDF SHA-256 recorded per record | Attribution and Persian review |

The hashes identify the exact bytes fetched from the source URLs recorded in each record; the source files themselves are not stored in this repository. For GOV.UK, this is a live page response, not an immutable archival edition. The hashes establish provenance only; they do not grant any use permission. The GOV.UK page specifically warns that third-party content may require separate permission. Research summaries are not Nasim policy, service facts, or individualized care advice.

## Admission gates

Before these candidates can enter any Training Dataset, each source needs attribution/rights review and completed human Persian/content review, plus any source-specific eligibility decision. Any source-specific exclusion or unresolved rights condition keeps its records unauthorized. Separate data admission and Training authorization must be recorded before T-026 or any Training workflow can use these records.

No model loading, inference, Training, Evaluation Run, runtime publication, or Production action was performed while preparing this package.
