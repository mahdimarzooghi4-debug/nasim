# Nasim initial seed candidate package — v0.1.0

- **Package ID:** `NASIM-SEED-CANDIDATE-001`
- **Status:** `CANDIDATE_NOT_AUTHORIZED` — prepared for source/content review only
- **Prepared from repository revision:** `c2dba855a88f5295af3b044a37098344b19b6880`
- **Record count:** 94
- **Model intended for future evaluation:** Qwen/Qwen3.5-9B at the D-0179 pinned revision

## Contents

| Source group | Count | Origin | Current disposition |
|---|---:|---|---|
| Synthetic behavior examples v0.1 | 52 | Nasim-authored synthetic Q/A | Source set identified under D-0154. D-0160/D-0162 report human content review, but exact reviewed-version reconciliation remains open. |
| Synthetic grounded-positive examples v0.2 | 32 | Nasim-authored examples grounded in explicitly fictional fixtures | Same reported review and version-reconciliation limits; fictional fixtures are not Nasim policy or real service facts. |
| Internet-derived candidate records v0.3 | 10 | Source-attributed research summaries from the existing candidate inventory | D-0177 permits candidate preparation. Source-specific rights/use approval and human localization/content review remain open. |

The JSONL package keeps each original record verbatim inside `record`, with a wrapper carrying the source file's Git blob SHA, source set, and permission/review state. Original record flags are not rewritten. IDs are unique across all 94 records.

## Initial review scope and structural audit

On 2026-10-25, the Operations Manager selected **internal evaluation only** as the intended future use of the 84 Nasim-authored synthetic candidates (52 behavior examples + 32 grounded-positive examples). This records intended scope only; it does not grant Training or Evaluation permission, approve a held-out set, or change any candidate record's status.

A read-only structural audit of this package found 94 parseable JSONL records, 94 unique IDs, no duplicate IDs, and no missing prompt/target-answer or source-lineage fields. All 10 internet-derived candidates contain citation and license metadata. All 94 records remain unassigned and unauthorized for Training, Evaluation, and runtime publication.

## Use state

Every package record is marked:

- `admission_state: CANDIDATE_NOT_AUTHORIZED`
- `training_permission: NOT_AUTHORIZED`
- `evaluation_permission: NOT_AUTHORIZED`
- `runtime_publication_permission: NOT_AUTHORIZED`
- `partition: UNASSIGNED`

This is a prepared candidate package, **not an approved Training Dataset or Evaluation Set**. No Training/Finetuning, evaluation run, model inference, model loading, API, runtime activation, or Production promotion was performed. The package has no Train/Evaluation split; assigning one now would imply a use-specific data decision that has not been recorded.

## Remaining admission evidence

1. Reconcile the exact versions of all 84 synthetic records against the reported human content review and record per-record outcomes/evidence.
2. For each of the 10 Internet-derived records, record source-specific rights for the intended purpose (Training versus Evaluation), the applicable permission/attribution conditions, and the Operations Manager's source-specific eligibility decision.
3. Complete human Persian/localization and factual review, including the fictional nature and boundaries of the synthetic grounded-positive examples.
4. Only after those gates, create a new content-addressed Dataset version, define and verify an independent held-out split, and record the relevant authorization before using T-026's Qwen acceptance preflight.

No public Nasim official-content corpus is created by this package. D-0135 still requires the runtime assistant to use verified, approved, current Nasim content for actual service answers.
