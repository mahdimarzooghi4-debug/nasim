# Nasim Internet-derived training candidate package — v0.3.0

- **Package ID:** `NASIM-TRAIN-CANDIDATE-001`
- **Status:** `AUTHORIZED_INTERNAL_TRAINING_PENDING_DATASET_ADMISSION`
- **Decision:** D-0161, Operations Manager, 2026-10-25
- **Record count:** 10
- **UTF-8 JSONL SHA-256:** `ed77f17ec5e511f491465e2e9d43646fd1de759ec8e8973273d76a6bff110347`
- **Source inventory blob SHA-1:** `34b35d892b42051833b14c2a0d59f8d10a1002e2`
- **Source repository revision:** `c2dba855a88f5295af3b044a37098344b19b6880`

## Permission decision

The Nasim Operations Manager explicitly authorized internal model-training use for all 10 records on 2026-10-25. The authorization is recorded in each wrapper and its derived record. It does not grant rights on behalf of publishers, authors, or third parties. Use only within the source license terms and preserve the recorded authors/title/source URL/license URL and Persian-adaptation notice. Creative Commons BY 4.0 requires appropriate credit, a license link, and an indication of changes when relying on that license. The GOV.UK record is limited to OGL-covered government content; exclude any British Geriatrics Society or other third-party material unless separately cleared.

The decision authorizes internal Training only. Evaluation and runtime publication remain unauthorized. Dataset partition remains `UNASSIGNED`; this file is not a completed Training Dataset admission, and no Training Run was started. Human Persian review remains pending for records 005–010. Exact source-byte hashes are in the records; source files themselves are not archived in this repository. The GOV.UK hash identifies a live HTML response rather than an immutable archived edition.

## Source inventory

| Source | Records | Source basis and remaining controls |
|---|---:|---|
| JMIR Aging, CC BY 4.0 | 4 | Internal Training authorized; preserve attribution, license link, and change notice. Ops Manager accepted summary scope for these records. |
| GOV.UK healthy-ageing guide, OGL v3.0 | 1 | Internal Training authorized only for OGL-covered government content; exclude third-party content; live page response hash, England-specific scope, and human Persian review remain relevant. |
| MDPI family-support study, CC BY 4.0 | 1 | Internal Training authorized; preserve attribution, license link, and change notice; human Persian review pending. |
| Springer/BMC caregiver study, CC BY 4.0 | 2 | Internal Training authorized; preserve attribution, license link, and change notice; inspect credit lines; human Persian review pending. |
| Bentham social-support study, CC BY 4.0 | 2 | Internal Training authorized; preserve attribution, license link, and change notice; human Persian review pending. |

## Execution boundaries

- `training_permission` records the Operations Manager's internal approval. It is not a source-owner license or legal opinion.
- `evaluation_permission` remains `NOT_AUTHORIZED`; do not use this package in an Evaluation Run.
- `runtime_publication_permission` remains `NOT_AUTHORIZED`; do not publish these source-derived records or treat them as official Nasim guidance.
- `partition` remains `UNASSIGNED`; no dataset admission, model loading, inference, Training Run, Evaluation Run, or publication occurred.
