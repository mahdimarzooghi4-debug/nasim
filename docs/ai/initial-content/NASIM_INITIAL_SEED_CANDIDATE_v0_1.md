# Nasim initial seed candidate package — v0.1.0

- **Package ID:** `NASIM-SEED-CANDIDATE-001`
- **Status:** `CANDIDATE_NOT_AUTHORIZED` — prepared for source/content review only
- **Prepared from repository revision:** `c2dba855a88f5295af3b044a37098344b19b6880`
- **Record count:** 94
- **Model intended for future evaluation:** Qwen/Qwen3.5-9B at the D-0179 pinned revision

## Contents

| Source group | Count | Origin | Current disposition |
|---|---:|---|---|
| Synthetic behavior examples v0.1 | 52 | Nasim-authored synthetic Q/A | Source set identified under D-0154. D-0160/D-0162 report human content review; on 2026-10-25, the Operations Manager confirmed that review covered this exact source version (blob `9495f38c53eeb30db2b07824fdcb2b70a9e3ff52`). |
| Synthetic grounded-positive examples v0.2 | 32 | Nasim-authored examples grounded in explicitly fictional fixtures | The Operations Manager confirmed that the reported review covered this exact source version (blob `3f8af141213ad111a646be3ff6a2c4fad277511c`); fictional fixtures are not Nasim policy or real service facts. |
| Internet-derived candidate records v0.3 | 10 | Source-attributed research summaries from the existing candidate inventory | D-0177 permits candidate preparation. Source-specific rights/use approval and human localization/content review remain open. |

The JSONL package keeps each original record verbatim inside `record`, with a wrapper carrying the source file's Git blob SHA, source set, and permission/review state. Original record flags are not rewritten. IDs are unique across all 94 records.

## Initial review scope and structural audit

On 2026-10-25, the Operations Manager selected **internal evaluation only** as the intended future use of the 84 Nasim-authored synthetic candidates (52 behavior examples + 32 grounded-positive examples). On the same date, the Operations Manager confirmed the content review covered the exact two source versions identified above. This records review/version reconciliation and intended scope only; it does not grant Training or Evaluation permission, approve a held-out set, or change any candidate record's use permission.

A read-only structural audit of this package found 94 parseable JSONL records, 94 unique IDs, no duplicate IDs, and no missing prompt/target-answer or source-lineage fields. All 10 internet-derived candidates contain citation and license metadata. The original 94-record candidate package remains unassigned and unauthorized for Training, Evaluation, and runtime publication. A separate 84-record derivative is authorized for internal Evaluation only, pending technical preflight.

## Derived internal Evaluation set

The Operations Manager explicitly authorized internal Evaluation use of the 84 synthetic records on 2026-10-25. The derived file places all 84 records in `EVALUATION_ONLY`, leaves Training and runtime publication unauthorized, and excludes all 10 internet-derived candidates. This is not an Evaluation Run or model activation. The exact UTF-8 JSONL SHA-256 is `85a4383e17b47de3206ed1bbc694f4096312e054e44c265bcc7bd096c76b9857`. Verify no overlap with any training input before a run, and pass T-026's fail-closed preflight.

See `NASIM_INTERNAL_EVALUATION_AUTHORIZATION_v0_1.md` for the scope and source-version confirmation.

## Use state

Every package record is marked:

- `admission_state: CANDIDATE_NOT_AUTHORIZED`
- `training_permission: NOT_AUTHORIZED`
- `evaluation_permission: NOT_AUTHORIZED`
- `runtime_publication_permission: NOT_AUTHORIZED`
- `partition: UNASSIGNED`

This is a prepared candidate package, **not an approved Training Dataset or Evaluation Set**. No Training/Finetuning, evaluation run, model inference, model loading, API, runtime activation, or Production promotion was performed. The package has no Train/Evaluation split; assigning one now would imply a use-specific data decision that has not been recorded.

## Remaining admission evidence

1. Record the separate authorization and acceptance criteria for the intended internal Evaluation use of the 84 reviewed synthetic records; keep the Evaluation permission denied until that decision is documented.
2. For each of the 10 Internet-derived records, record source-specific rights for the intended purpose (Training versus Evaluation), the applicable permission/attribution conditions, and the Operations Manager's source-specific eligibility decision.
3. Complete human Persian/localization and factual review for the 10 internet-derived candidates. The synthetic grounded-positive records are reviewed against fictional fixtures only; those fixtures are not Nasim policy or real service facts.
4. Only after those gates, create a new content-addressed Dataset version, define and verify an independent held-out split, and record the relevant authorization before using T-026's Qwen acceptance preflight.

No public Nasim official-content corpus is created by this package. D-0135 still requires the runtime assistant to use verified, approved, current Nasim content for actual service answers.
