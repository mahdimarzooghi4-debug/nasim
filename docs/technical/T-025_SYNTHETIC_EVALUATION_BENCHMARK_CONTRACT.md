# T-025 — Offline initial synthetic evaluation and internal model benchmark contract

2026-10-09; candidate addendum 2026-10-25. Source D-0166, D-0167, D-0147. Final model and thresholds remain undecided. The Product Owner has approved Qwen/Qwen3.5-9B as the lead candidate for a future benchmark only. This remains **technical evaluation design**, not a selected/activated AI model.

1. Use versioned, source-attested **84 synthetic author-generated questions/answers**, never actual operational elder/Provider data without legal/purpose-specific manager approval.
2. Apply D-0164 edits as a **new content-addressed successor**, retaining original 52+32 unchanged; no fictional source ever becomes authoritative Nasim policy.
3. First technical group-independent split is versioned, not a business percentage rule. For source `category`-grouped behavior and `source_fixture_id`-grouped grounded positives, reserve whole groups of four behavior categories and two fictional fixtures for EVALUATION. No shared ID/scenario fixture/category group between Training and Evaluation; use exact pinned digest and source lineage. This does not prove absence of broader lexical/semantic leakage or real-household independence.
4. Benchmark multiple self-hosted candidates and an explicit baseline only **after** a viable internal runtime/trainer is built, using identical immutable partitions, comparable metrics for grounded accuracy, hallucination/safety, access/authority boundary, Persian elder comprehensibility, freshness, human escalation and uncertainty. Report full per-category coverage and provenance, calibration where meaningful, instability and unresolved errors; no single metric decides a winner. Exact model family and quantitative acceptance thresholds require evaluated evidence.
5. No external inference/training API, model auto-promotion, medical/financial/referral decision, or unattended online learning. Human governance gate applies before real production AI.
6. The 84-item starter corpus is **small and artificial**, insufficient to establish clinical/service competence or real-world safety by itself. It may support offline smoke evaluation/early training prototypes only.

Reproducible version inputs are the Git source blobs, D-0163..0166 decisions, technical held-out group set, and the content-addressed manifest. Any source, split or edit change creates a new version; invalidate earlier evaluation claims.


## 7. Lead benchmark candidate — Qwen3.5-9B (2026-10-25)

The Product Owner approved **Qwen/Qwen3.5-9B** as the lead candidate to include in the future model benchmark. This is a candidate choice only; it does not amend D-0147's deferral of final model/version selection, select a Production model, authorize model training, or authorize runtime activation.

- **Immutable model repository revision:** `c202236235762e1c871ad0ccb60c8ee5ba337b9a` ([pinned model card](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md)).
- **Publisher metadata:** the pinned card identifies a 9B-parameter model and claims coverage of 201 languages and dialects. That claim is not proof of Persian accuracy or suitability for Nasim; Persian behavior must be evaluated on the intended task.
- **License metadata:** the pinned repository identifies Apache-2.0 and includes its `LICENSE` file ([pinned license](https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/LICENSE)). Recheck the exact snapshot and all applicable third-party components before redistribution or use.
- **Implementation evidence:** the card documents local loading with Transformers and serving examples for vLLM/SGLang. Those are compatibility options only; Nasim has not selected its inference runtime, deployment topology, or hardware.
- **Evaluation disposition:** include this immutable revision as the lead candidate alongside at least one self-hosted challenger and an explicit baseline under the same immutable, permitted evaluation split described above. Apply the existing evaluation dimensions; do not invent numeric pass thresholds. Do not start the benchmark until the runtime, evaluation data/rights, and required review gates are ready.
- **Current status:** `APPROVED_FOR_BENCHMARK_CANDIDACY`; **not** approved for Training, Evaluation Run, Runtime, Dataset inclusion, or Production promotion. The 10 Internet-source candidate records remain unauthorized for evaluation and are not benchmark data.

A benchmark may reject this candidate. The final model/version decision remains under D-0147 and requires recorded evaluation evidence and the applicable authority.
