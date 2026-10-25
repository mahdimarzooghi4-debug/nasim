# T-027 — Internal Qwen inference runtime contract

- **Date:** 2026-10-25
- **Status:** SELECTED FOR INTERNAL EVALUATION ONLY — not deployed or activated
- **Selected model:** `Qwen/Qwen3.5-9B` at `c202236235762e1c871ad0ccb60c8ee5ba337b9a` (D-0179)
- **Purpose:** prepare an internal-only runtime path for the accepted single-model evaluation scorecard (D-0180)

## Selected runtime

Use **vLLM 0.32.0** as the internal serving engine for the initial single-model evaluation path. Pin its release artifact digest after the GPU/CUDA target is selected. The exact Qwen model card documents vLLM serving and its local OpenAI-compatible API. vLLM added Qwen3.5 dense support in v0.27.0; the current v0.32.0 release includes additional Qwen3.5 compatibility fixes. The Qwen card also documents `--language-model-only` for text-only serving, which fits Nasim's first informational assistant scope and avoids loading its vision encoder for this use case.

This runtime selection is **not a deployment or activation decision**. The exact image digest/package lock, GPU/CUDA combination, service host, capacity, and load profile remain unselected. Before activation, run a compatibility smoke against the exact pinned model snapshot on the selected hardware and record the resulting artifacts.

## Service boundary

1. The application backend is the only Nasim caller of the model service. Elders and caregivers do not call vLLM directly.
2. Keep vLLM on a private service network. Do not publish its port to the public Internet or provide a managed/external inference fallback.
3. Stage the exact model files as a local, immutable snapshot. Verify its repository revision and content manifest before startup; do not resolve a mutable `main` revision at runtime.
4. Run the model service with outbound Internet access blocked. Model download/update is a separate controlled preparation task.
5. Keep authorization, audience filtering, source retrieval, prompt assembly, audit, rate limits, and human handoff in Nasim's application layer. A model response is not an official record or a human decision.
6. Start with text-only serving. Do not enable image, audio, video, tools, fine-tuning, or online learning for D-0135.

## Configuration gates

The following must be decided and pinned before a runtime manifest can satisfy T-026's evaluation preflight:

- exact vLLM package/container version **and artifact digest**, plus Python/PyTorch/CUDA/driver compatibility;
- actual GPU/VRAM and host memory available to this isolated service;
- bounded context length, output length, and concurrency for the first evaluation workload;
- approved request/response retention and redaction behavior for logs;
- private-network address, service identity/authentication, health checks, restart policy, and operational owner;
- verified model file manifest and license/attribution record.

The 9B parameter count implies about **18 GB of raw BF16 weights** (9 billion × 2 bytes), before runtime allocations and KV cache. This is a lower-bound storage estimate, not a GPU sizing recommendation. The 100-elder / 100-caregiver initial population does not define simultaneous inference demand; capacity must be measured from a real, agreed workload profile.

## Readiness status

`RUNTIME_DESIGN_PROPOSED`. No server has been selected or provisioned; no model weights were downloaded or loaded; no inference, evaluation, training, API exposure, or activation was performed. Hosted Stage remains unavailable under D-0130. T-026's data authorization and human-review gates remain independently required.

## Evidence

- Pinned Qwen model card and its vLLM/text-only serving instructions: https://huggingface.co/Qwen/Qwen3.5-9B/blob/c202236235762e1c871ad0ccb60c8ee5ba337b9a/README.md
- vLLM v0.32.0 release notes (current release and Qwen3.5 fixes): https://github.com/vllm-project/vllm/releases/tag/v0.32.0
- vLLM Qwen3.5 serving recipe: https://docs.vllm.ai/projects/recipes/en/stable/Qwen/Qwen3.5.html
