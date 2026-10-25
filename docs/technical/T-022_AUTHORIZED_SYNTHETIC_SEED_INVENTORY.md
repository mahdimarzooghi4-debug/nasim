# SG-022 / T-022 / PB-022 — Owner-authorized synthetic initial seed, technical intake

Date: 2026-10-09. Status: **Technical admission only for OFFLINE synthetic source inventory**.

## Business
- Product Owner D-0154 authorizes the 84 **author-generated** samples as an initial synthetic source set; D-0155 limits subsequent real inputs to separately verified approved Nasim data. Original AI-BOOT-003 states 52 v0.1 + 32 v0.2, eight **fictional** fixtures and two merely proposed author edits v0.3.
- The original `NOT_AUTHORIZED` flags describe the **historical artifact state** and are kept intact; the later owner source authorization is linked as a separate decision. Neither means every answer has qualified independent human review, official Nasim publication, a Training/Evaluation partition, an approved Dataset or a Production model.
- Issue #13 for per-record independent 84-sample QA; Issue #11 for actually verifiable published official content; Issue #12 for real Operational Data Training/Eval scope remain OPEN. Do not re-ask whether the Operations Manager approved/authored content; D-0152/D-0153 reports this. Ask only for versioned evidence and independent review.

## Technical
- Originals are copied verbatim from unmerged PR #10 commit `faf33342497ec23f7c0969930ce808787e476be6` to this stacked Draft development branch. Git object blob hashes are pinned for the 52, 32, 8, 2 files; see `nasim.learning.synthetic_seed.SOURCE_SPECS`.
- `build_initial_synthetic_inventory()` verifies exact original byte/Git blob SHA1, ordinal IDs, required synthetic/no-PII *declarations* (not independently verified privacy), original candidate NOT_AUTHORIZED flags, fixture reference existence, and author edit target/pending status. One-byte tampering fails closed.
- The stable SHA-256 inventory enumerates only **opaque synthetic IDs + record SHA-256 + source file**; it never exports sample prose, case text or personal data. The report is reproducible and has explicit `SOURCE_ATTESTED_NOT_APPROVED` + `PENDING_INDEPENDENT_PER_RECORD` + `UNASSIGNED` partition flags. No database read or write, operational API, TrainingRun, Dataset registry approval, or model activation. For no-real-data initial synthesis, the actual Trust/Quality gates still apply.
- Offline CLI: from `backend/`, `uv run --locked python -m nasim.learning.inspect_seed` (stdout only). Tests run in existing Backend CI.

## Backlog / Sprint 022
Full code + tests of an authenticated-source, immutable first synthetic seed **inventory**; not a ready-to-train Dataset. No guessed Training/Evaluation ratio, eligibility policy for real people, human signature, Keycloak instance, model family/threshold, retention duration, Provider activation or browser session.

Trace: Owner decisions D-0154–D-0159 → SG/T/PB-022 → Sprint-022 source attestation, explicit fail-closed state → full CI → non-approving Code Review. PR Draft/Open. No Merge before independent review/reconciliation; no Hosted Stage under D-0130.
