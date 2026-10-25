# Nasim internal evaluation authorization — v0.1

- **Authorization reference:** `NASIM-EVAL-AUTH-001`
- **Date:** 2026-10-25
- **Decision authority:** Nasim Operations Manager (explicit confirmation in this project conversation)
- **Authorized artifact:** `nasim_internal_evaluation_set_v0_1.jsonl`
- **Records:** 84 Nasim-authored synthetic records (52 behavior + 32 grounded-positive)
- **Purpose:** Internal evaluation of the selected Qwen model only

## Decision

The Operations Manager explicitly authorizes the 84 synthetic records for **internal model evaluation only**. The Operations Manager also confirmed that the reported content review covered the exact source versions:

| Source set | Records | Source file blob SHA-1 |
|---|---:|---|
| Synthetic behavior v0.1 | 52 | `9495f38c53eeb30db2b07824fdcb2b70a9e3ff52` |
| Synthetic grounded-positive v0.2 | 32 | `3f8af141213ad111a646be3ff6a2c4fad277511c` |

The source records are author-generated synthetic examples. The grounded-positive set uses explicitly fictional fixtures; those fixtures do not represent Nasim policy, current services, real people, or authoritative service facts.

## Permission scope

- Internal Evaluation: **AUTHORIZED** for the 84 records in this exact artifact.
- Training/Fine-tuning: **NOT AUTHORIZED**.
- Runtime/publication: **NOT AUTHORIZED**.
- Hosted Stage/Production: **NOT AUTHORIZED**.
- Internet-derived candidates: excluded from this authorization.
- Real elder or caregiver records: not included.

This is a data-use authorization only. It does **not** authorize loading or running the model, conducting an evaluation run, activating a runtime, publishing responses, or promoting a model. Those actions remain subject to T-026's fail-closed Qwen preflight, including exact artifact hashing, scorecard evidence, the approved internal runtime evidence, and all other required checks.

The evaluation set is reserved exclusively for Evaluation and is not part of any Training Dataset. Before a future evaluation run, verify its exact content hash and confirm there is no record overlap with any training input. No model loading, inference, Training, or Evaluation Run was performed while preparing this authorization package.
