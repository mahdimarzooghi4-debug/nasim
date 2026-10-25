# Sprint 018 — Fail-Closed Versioned Dataset Manifest Foundation

Date 2026-10-09. Source SG-018→T-018→PB-018. Branch `sprint-018-controlled-dataset-manifest-foundation` stacked on unmerged Draft PR #29 HEAD `14cdc6f0f681622786ece58aac71b66d83cc0c47`; unchanged main `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`.

Implementation is only a pure Python typed core, no runtime or active pipeline. Tests are synthetic and prove absent eligibility policy fails closed, no operational free text, exact member attestation, version digest stability, deduplication, partition exact-ID exclusion. Real users' data are **not** used and the Dataset Builder is **not yet automatically operational**. Future policy/consent/approval must be specified before that work.

Required gate: backend core/contracts → unit tests → exact-head full CI including unchanged Web → bounded technical Code Review. PR stays Draft/Open and cannot merge independently of PRs #14–#29, or run hosted Stage/QA/Release/Production while D-0130 remains active. No new positive Business decision is invented.
