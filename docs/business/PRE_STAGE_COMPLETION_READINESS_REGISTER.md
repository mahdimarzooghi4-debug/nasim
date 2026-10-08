# Nasim — Pre-Stage Completion & Readiness Register

- **Project:** نسیم — نظام سالمند‌یاری محله‌محور
- **Status:** WORKING PLAN / NOT A BUSINESS ACCEPTANCE
- **Prepared:** 2026-10-08
- **Process:** Business → Technical → Scrum/Product Backlog → Sprint → Code → Code Review → Stage → QA/Testing → Release Approval → Production → Monitoring → Improvement
- **Baseline:** `main` `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`, exact-main CI [run #95](https://github.com/mahdimarzooghi4-debug/nasim/actions/runs/37803350724) SUCCESS (migration, test, quality, disposable container smoke)
- **Stage boundary:** D-0130 — Hosted Stage is currently **UNAVAILABLE**; Stage has **not** been deleted and may not be declared passed based on CI, container smoke, or this register.
- **Related draft:** [Provider Qualification Business Packet DC-016](https://github.com/mahdimarzooghi4-debug/nasim/blob/business/provider-qualification-decision-packet/docs/business/closure/DC-016_PROVIDER_QUALIFICATION_DECISION_AUTHORITY_PACKET.md) exists only on the separate branch `business/provider-qualification-decision-packet` at preparation time; it is **not** in `main` and does not constitute an Accepted Decision.

> This register coordinates pre-Stage development. It does not accept any OPEN Business Decision, create implicit authority, define qualification/credential rules, authorize implementation of blocked work, create an SG/T/PB/Sprint, or replace an exact-head Code Review/CI gate. `OPEN ≠ DEFERRED ≠ ACCEPTED`. Planned work is **not** completed work.

## 1. Verified implementation baseline

| Area | Existing implementation (not Stage-certified) | What is not implied |
|---|---|---|
| TS-03 / Sprint 001 | Case/Profile, assignments, contacts, interactions/monitoring/observations, append-only history, audit/outbox/idempotency and bounded authorization | Enrollment rules, full Need/Case resolution, Outcome/Reassessment |
| TS-05 / Sprint 002 | Identity-context and capability/role registry foundations; permission vocabulary | Live external IdP, actual actor-role/role-permission authorizations, Provider/Elder access |
| Sprint 003 | Bounded immutable Referral recording, list/detail | Provider selection, Referral response/lifecycle, service delivery |
| Sprint 004 | Pre-operational Provider Candidate Registry | Onboarding qualification, eligibility, selection or activation |
| Sprint 005 | Immutable descriptive Provider Qualification Evidence records | Sufficiency, credential validity, qualification decision |
| Sprint 006 | Immutable Provider Qualification Review Requests, list/detail | Review assignment, decision, approval, activation |
| CI | Exact-main run #95 fully successful | Hosted Stage, Stage Admission, Stage-based QA, Release or Production |

Sprint 006's reviewed HEAD is already contained in `main`; PR #7 was reconciled by closing **without merge**. The old run #94 remains a stale queued run, but the replacement exact-main run #95 is SUCCESS.

The inspected `backend/src/nasim` packages cover `api`, `application`, `authorization`, `domain`, `identity_context`, `infrastructure`, `provider_registry` and `referral`; no dedicated implemented AI Runtime, Dataset Builder, Training, Evaluation or Model Registry was found. The current repository root also has no separate frontend application directory. This is an inspection finding, not a commitment to a UI platform.

## 2. Pre-Stage workstreams — status and necessary business triggers

The final amount of work mandatory **before** Stage depends on the Product Owner's accepted Phase/Pilot scope; this register does not silently convert all possible future features into Stage blockers.

| Workstream | Current status | Minimum missing decision or prerequisite before relevant implementation | Delivery target **only if in accepted Phase/Pilot scope** |
|---|---|---|---|
| P1. Qualification Decision | **Business OPEN / code absent** | DC-016 QD-01…QD-07: purpose/scope, reviewer/approver authority, criteria, evidence sufficiency/expiry, evidence pinning, decision vocabulary/rework, relation to Service/Geography/Capacity | Bounded human-auditable decision workflow with immutable time-specific evidence basis |
| P2. Provider Approval & Activation | **OPEN / code absent** | Independent activation authority, prerequisites, scope, effective date, suspension/deactivation/revocation, consequences for referrals/access | Explicit governed activation; qualification alone never activates |
| P3. Provider Network / Operational Eligibility | **OPEN / foundation only** | Provider Type, service eligibility and mapping, geography, capacity semantics, Provider access, provider-selection authority | Only the approved operating slices; no score/ranking or auto-selection by default |
| P4. Service Catalog / Need / Referral Operations | **Business OPEN / Referral recording only** | Active service scope, Need/Service mapping, referral authority, response/rejection, fallback, completion evidence and ownership | Versioned service/need definitions and bounded referral lifecycle |
| P5. Case completion / Outcome / Reassessment | **Business OPEN / observation capture only** | Formal Accepted State authority, baseline, definition versions, reassessment trigger, Need resolution/reopen, outcome source validity | Longitudinal auditable human-governed outcome/reassessment foundation; no inferred causal impact |
| P6. Identity / operational access | **Technical foundation; real integration absent** | Organization/actor grants for each in-scope action; external IdP choice/integration and actual credentials only when legitimately selected | Secure authenticated operational workflow without default grants |
| P7. Elder & Caregiver internal AI | **D-0004/D-0005 accepted intent; no runtime code** | Minimum selected Day-one use case(s), allowed/prohibited actions, human owner/review, runtime data classes, privacy/consent, failure behavior | Internal AI assistance with provenance and explicit human decision boundary |
| P8. Automatic versioned Dataset lifecycle | **Business intent accepted; code absent** | Training-eligible Data Classes, exclusions, legal basis, source/provenance, verification/curation, versioning, correction/withdrawal effects | Automatic dataset versions **only** from policy-eligible data, never automatic eligibility policy changes |
| P9. Training, independent Evaluation, Model Governance | **Code absent / Technical not decided** | Chosen family/architecture from evidence, dataset rules, evaluation contract, accountable human promotion/rollback, model/runtime infrastructure, meaningful tests | Reproducible training/evaluation, immutable lineage, separately approved Production promotion |
| P10. Security, operations, event delivery, observability | **Partial platform foundation** | Scope-specific data-access matrix, retention/consent decisions, event consumer contracts, real integration ownership and operational infrastructure | In-scope workers, data controls, audit, telemetry, incident/fail-safe evidence |
| P11. External partners/payments/notifications | **Not integrated** | Selected partner, source of truth, data-sharing contract, real endpoint/credentials, fallback, explicit Phase/Pilot necessity | Integrate **only** selected and authorized external dependencies; never fake payments/provider responses |
| P12. End-user/admin interface(s) | **Not present in inspected repo root** | Approved actor journeys, accessibility and scope, role/data boundaries and interaction model | UI only for accepted Phase/Pilot workflows; UI stack/design are not decided here |

No item above by itself authorizes permissions, scores, qualifications, threshold numbers, Provider settlement or activation. A workstream that is outside the accepted Phase/Pilot scope may be **explicitly deferred** only by an actual recorded deferral decision with scope, owner, future gate and constraints. Being OPEN is not a deferral.

## 3. Suggested fast execution order — each slice retains the mother-process gates

### Wave A — Close only context-triggered Business decisions
1. Product Owner determines what **must** be in the first operational Phase/Pilot and what is actually outside scope; do not ask for all future-scale decisions.
2. For P1, review DC-016 and decide the minimum safe Qualification Decision contract; **no SG-007/T-007/PB/Sprint/Code before that**.
3. Independently, for P7/P8 select the first Day-one AI use case and resolve its human ownership, allowed data, legal/consent/training eligibility and fail-safe. Do not copy model choices from other products.
4. For P2/P3/P4/P5/P6, close only the authority, scope, vocabulary and data decisions needed for the selected bounded implementation.
5. Record each binding acceptance in `docs/DECISIONS.md` and its matching slice gate. If outside evidence/real institutional authority is missing, keep OPEN rather than guessing.

### Wave B — Provider and core operational backend (after Wave A gates)
Each bounded slice uses:
`Accepted minimal Business decisions → SG record → Technical contract → PB → Sprint authorization → Code → Code Review → exact-HEAD CI success`.

Candidate order (not approved sprint IDs): Qualification Decision → separate Approval/Activation → permitted Provider/Service scope → Referral response/completion → Outcome/Reassessment. Reorder only according to explicitly accepted dependencies. Do not assume Qualification implies Approval or Activation, or Service Completion implies Outcome.

### Wave C — Internal AI in parallel (after its own Business gate)
The minimum Day-one AI contract must respect:
`AI Output ≠ Official Record` and `Operational Data ≠ Automatically Training Eligible`.

Possible delivery sequence, subject to accepted Business/Technical contracts:
1. Bounded internal runtime and single selected use case with strict data access and provenance.
2. Human Review/Accept-Reject-Edit linkage for consequential outputs.
3. Policy-gated ingestion/curation and automatic versioned Dataset lifecycle.
4. Independently versioned Training and Evaluation evidence; candidate lineage and immutable model artifact handling.
5. Explicit human-controlled model promotion/rollback and safe behavior when no valid model exists.

No specific model family, algorithm, inference service, training cadence, evaluation threshold, GPU size, provider, endpoint, bucket or credential is assumed. Dataset automation does not authorize model auto-promotion.

### Wave D — Hardening and local/pre-Stage verification
- Exact-commit CI covering migrations, tests, type/lint and available local/ephemeral integration smoke.
- Access-control negative tests, actor/permission boundaries, tenant/scope isolation where applicable, append-only history, idempotency/race conditions and stale-data rejection.
- Domain invariants and AI governance tests for each accepted workflow.
- Real external integration proof only for integrations actually in the accepted Phase/Pilot scope; otherwise an explicit documented deferral.
- Readiness inventory for authentication, secrets, backup/restore, telemetry, provider contracts and any selected deployment target, with no invented values.
- Product Owner/technical Code Review records and explicit handoff for Hosted Stage once a real environment exists.

## 4. Minimum user decisions currently blocking actual next implementation

**B1 — Phase/Pilot boundary:** Which operational capabilities in P1–P12 are non-negotiable for the first deployment, and which can be explicitly deferred? The current concept documents do not supply a complete accepted launch scope.

**B2 — Qualification human authority:** For DC-016, the accountable reviewer/decision maker and possible independent approver/maker-checker are unknown. Exact criteria, evidence validity, pinning and outcome vocabulary are also OPEN. Request existence alone is not an approval.

**B3 — First internal AI use case:** Which one elder/caregiver function is authorized first, who is the human owner, which data classes may be used in runtime/training and how should failure be handled?

**B4 — Identity / data / external dependencies:** Real login, access grants, consent basis, Provider access and selected integration contracts require source-of-truth and responsible-party evidence.

These are **decision prompts, not a request to prematurely accept all undecided business matters**. D-0124 allows accelerated grounded design choices up to the Code boundary but does not authorize invention of institution-specific authorities, credentials, legal basis or eligibility.

## 5. Pre-Stage exit criteria

A pre-Stage handoff can be declared **READY FOR HOSTED STAGE CONSIDERATION** only if all of the following are evidenced for the explicit accepted Phase/Pilot scope:

- Required Business decisions accepted or genuinely deferred with owner/scope/future gate and safe constraints; no blocking OPEN decision hidden.
- Required Technical designs, backlogs, sprint records, code review approvals and exact-revision green CI exist; no unreviewed implementation asserted complete.
- Full accepted in-scope workflow can be exercised locally or in disposable CI **without** claiming this is Hosted Stage.
- In-scope AI Day-one capability and policy-gated dataset workflow have real implementation/evidence rather than a placeholder demo.
- Local security and integration verification is explicit about mocked, missing or unverified **external** services; no mock is accepted as production proof.
- Any required environment provision, secret, identity, storage, external service, model artifact/hardware and operational requirements are recorded as actual external inputs.

**Current overall outcome: NOT READY FOR STAGE HANDOFF.** Even after pre-Stage Code Review and CI have succeeded, Hosted Stage Admission and Stage-based QA remain blocked by D-0130 until the real Hosted Stage exists. Release Approval/Production are subsequent separate gates.

## 6. Immediate next action

Finish the smallest binding Business decision set for **Qualification Decision** (DC-016) and define the **first AI Day-one Use Case** in parallel. Until those decisions are accepted, do not open an implementation Sprint for them. In parallel, implementation-neutral preparations and audit/checklist work can continue.

**This register is a planning document only; it neither claims that the above work is implemented nor replaces the Product Owner.**
