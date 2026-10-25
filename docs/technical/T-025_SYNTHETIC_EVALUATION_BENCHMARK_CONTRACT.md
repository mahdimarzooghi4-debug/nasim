# T-025 — Offline initial synthetic evaluation and internal model benchmark contract

2026-10-09; model-selection addendum 2026-10-25. Source D-0166, D-0167, D-0179. Qwen/Qwen3.5-9B at the pinned revision below is the selected base model. Acceptance thresholds and activation remain undecided. This remains **technical evaluation design**, not a deployed/activated AI model.

1. Use versioned, source-attested **84 synthetic author-generated questions/answers**, never actual operational elder/Provider data without legal/purpose-specific manager approval.
2. Apply D-0164 edits as a **new content-addressed successor**, retaining original 52+32 unchanged; no fictional source ever becomes authoritative Nasim policy.
3. First technical group-independent split is versioned, not a business percentage rule. For source `category`-grouped behavior and `source_fixture_id`-grouped grounded positives, reserve whole groups of four behavior categories and two fictional fixtures for EVALUATION. No shared ID/scenario fixture/category group between Training and Evaluation; use exact pinned digest and source lineage. This does not prove absence of broader lexical/semantic leakage or real-household independence.
4. Evaluate only the selected pinned Qwen revision after the required internal runtime and permitted, versioned evaluation data are ready. **No challenger model or competitive model comparison is required** (D-0179). Use predeclared acceptance cases for grounded accuracy, unsupported-answer abstention, audience/access boundaries, Persian elder comprehensibility, freshness, human escalation and uncertainty. Report full per-category coverage and provenance, calibration where meaningful, instability and unresolved errors. Acceptance criteria and any numeric thresholds must be recorded before execution; no metric or threshold may be invented after results are observed.
5. No external inference/training API, model auto-promotion, medical/financial/referral decision, or unattended online learning. Human governance gate applies before real production AI.
6. The 84-item starter corpus is **small and artificial**, insufficient to establish clinical/service competence or real-world safety by itself. It may support offline smoke evaluation/early training prototypes only.

Reproducible version inputs are the Git source blobs, D-0163..0166 decisions, technical held-out group set, and the content-addressed manifest. Any source, split or edit change creates a new version; invalidate earlier evaluation claims.


## 7. Lead benchmark candidate — Qwen3.5-9B (2026-10-25)

D-0179 selects **Qwen/Qwen3.5-9B** as the base model for Nasim's internal assistant, at the immutable revision below. No competing model is requested. This selects model identity/version only; it does not authorize model training, evaluation data use, runtime activation, or Production promotion.

- **Immutable model repository revision:** `c202236235762e1c871ad0ccb60c8ee5ba337b9a` ([pinned model card](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md)).
- **Publisher metadata:** the pinned card identifies a 9B-parameter model and claims coverage of 201 languages and dialects. That claim is not proof of Persian accuracy or suitability for Nasim; Persian behavior must be evaluated on the intended task.
- **License metadata:** the pinned repository identifies Apache-2.0 and includes its `LICENSE` file ([pinned license](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/LICENSE)). Recheck the exact snapshot and all applicable third-party components before redistribution or use.
- **Implementation evidence:** the card documents local loading with Transformers and serving examples for vLLM/SGLang. Those are compatibility options only; Nasim has not selected its inference runtime, deployment topology, or hardware.
- **Evaluation disposition:** conduct a single-model acceptance assessment against the permitted, versioned evaluation contract described above; no challenger or model-ranking exercise. Apply the existing evaluation dimensions. Do not start until runtime, evaluation data/rights, and required review gates are ready.
- **Current status:** `SELECTED_NOT_ACTIVATED`; no Training/Fine-tuning, Evaluation Run or use of unauthorized sources, Runtime, Dataset inclusion, or Production promotion is approved. The 10 Internet-source candidate records remain unauthorized for evaluation and are not benchmark data.

The single-model acceptance assessment may still block activation. D-0179 selects the model; evaluation and Production promotion remain separately governed.
