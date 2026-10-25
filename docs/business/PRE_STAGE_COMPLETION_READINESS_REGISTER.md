# Nasim — Pre-Stage Completion & Readiness Register

- **Project:** نسیم — نظام سالمند‌یاری محله‌محور
- **Status:** WORKING PLAN / NOT A BUSINESS ACCEPTANCE
- **Prepared:** 2026-10-08
- **Process:** Business → Technical → Scrum/Product Backlog → Sprint → Code → Code Review → Stage → QA/Testing → Release Approval → Production → Monitoring → Improvement
- **Baseline:** `main` `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`, exact-main CI [run #95](https://github.com/mahdimarzooghi4-debug/nasim/actions/runs/37803350724) SUCCESS (migration, test, quality, disposable container smoke)
- **Stage boundary:** D-0130 — Hosted Stage is currently **UNAVAILABLE**; Stage has **not** been deleted and may not be declared passed based on CI, container smoke, or this register.
- **Related independent drafts (all Draft/Open when rechecked 2026-10-08):** [PR #9 — Provider Qualification DC-016](https://github.com/mahdimarzooghi4-debug/nasim/pull/9) on `business/provider-qualification-decision-packet`, and [PR #10 — AI Business/content preparation](https://github.com/mahdimarzooghi4-debug/nasim/pull/10) on `business/ai-day-one-minimal-use-case-packet`. Their decisions/documents **are not merged into `main` or this PR #8**. The product's current pre-Stage preparation must *consider* them as explicit branch-specific decisions without treating them as already incorporated into the accepted main baseline.

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
| P7. Elder & Caregiver internal AI | **D-0004/D-0005 main Accepted; on separate Draft PR #10, D-0135 information-only first use case and D-0136…D-0146 bounded content/human direction recorded; no AI runtime code** | Not re-select the first AI use case from scratch. Need **actual official published source/version/audience proof** (#11), authenticated identity/scope/privacy, real human handoff/contact, final bounded technical entry. Do not claim PR #10 is merged | Read-only official information for **both elder and caregiver**, no Case/Provider/Referral/clinical/financial write or default personal-case access |
| P8. Automatic versioned Dataset lifecycle | **D-0005 Accepted in main; code absent** | Actual purpose- and source-class-specific Training Eligibility/legal basis, exclusions, quality/provenance, human approval, correction/withdrawal/retention (#12). Existing Case/Referral/Provider `*.v1` Outbox is **not approved Training data** | **Day-one mandatory:** automatic versioned Dataset creation from new **actually policy-eligible** operational data; never permissive ingestion or automatic model promotion |
| P9. Training, independent Evaluation, Model Governance | **Code absent; 84 synthetic content authoring candidates on separate Draft PR #10; no actual Training/Eval** | Independent qualified sample review (#13), separate lawful Train/Eval rights (#12), actual versioned evaluation material, model/runtime infrastructure. **D-0147 on PR #10 defers only final model choice**, not the Day-one AI requirement | Evidence-based candidate selection, reproducible offline assessment and independently approved Production promotion; fictional samples **do not** satisfy First-party Dataset Builder |
| P10. Security, operations, event delivery, observability | **Partial platform foundation** | Scope-specific data-access matrix, retention/consent decisions, event consumer contracts, real integration ownership and operational infrastructure | In-scope workers, data controls, audit, telemetry, incident/fail-safe evidence |
| P11. External partners/payments/notifications | **Not integrated** | Selected partner, source of truth, data-sharing contract, real endpoint/credentials, fallback, explicit Phase/Pilot necessity | Integrate **only** selected and authorized external dependencies; never fake payments/provider responses |
| P12. End-user/admin interface(s) | **Not present in inspected repo root** | Approved actor journeys, accessibility and scope, role/data boundaries and interaction model | UI only for accepted Phase/Pilot workflows; UI stack/design are not decided here |

No item above by itself authorizes permissions, scores, qualifications, threshold numbers, Provider settlement or activation. A workstream that is outside the accepted Phase/Pilot scope may be **explicitly deferred** only by an actual recorded deferral decision with scope, owner, future gate and constraints. Being OPEN is not a deferral.

## 3. Suggested fast execution order — each slice retains the mother-process gates

### Wave A — Close only context-triggered Business decisions
1. Product Owner determines what **must** be in the first operational Phase/Pilot and what is actually outside scope; do not ask for all future-scale decisions.
2. For P1, review DC-016 and decide the minimum safe Qualification Decision contract; **no SG-007/T-007/PB/Sprint/Code before that**.
3. Independently, reconcile **PR #10's selected D-0135 first informational use case** (for both audiences) *if and when its Business changes are properly accepted/integrated*, rather than repeating the already recorded selection. Its content/audience and conditional human-follow-up decisions remain branch-scoped. Resolve **real published source and permission evidence #11**, actual source-class Training Eligibility **#12**, and qualified sample-review evidence **#13**, keeping each permission and gate separate. **Only model selection** is explicitly deferred in PR #10's D-0147; do not copy model choices from other products.
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
1. Following accepted integrated Business content and actual source evidence, implement **D-0135 bounded informational/read-only AI for BOTH elder and caregiver** with current approved/published audience-permitted sources, provenance, and fail-safe, without inventing personal-case access.
2. Define **real human-contact continuity** for elder (actually assigned caregiver first, conditional future support only after authorized organization) and caregiver-specific help route; do not claim either exists merely because directions appear in PR #10.
3. Independently gate and implement **D-0005 automatic, continuously versioned Dataset production** from newly observed **eligible-only** operational sources. Existing Outbox data and author-generated examples are neither automatically eligible nor substitute for this Day-one requirement.
4. Handle independent qualified review of the 84 **synthetic authoring candidates** (#13) and legal Training/Evaluation authorization (#12). The 84 examples, while useful for content preparation, are **not model training evidence, a versioned first-party Dataset, or a model benchmark**.
5. Future consequential AI outputs (if separately approved in later Use Cases) require Human Review/Accept-Reject-Edit and proper provenance; do **not** imply this read-only first slice can mutate official state.
6. Select a Production model only after real, comparable evaluation evidence per PR #10's **D-0147 narrow deferral**, and separately govern promotion/rollback and fail-safe behavior. No automatic selection from a passed Evaluation.

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

**B3 — Day-one AI evidence and authorization (partially resolved only on unmerged Draft PR #10):** The *first bounded use case* is already recorded there as **D-0135 — read-only, source-grounded official information for both audiences**. D-0136…D-0146 address *part* of content and human continuity in Business; D-0147 **explicitly defers only exact model selection**. **Still OPEN and actually blocking:** authenticated publication and per-audience source validity (#11); human contact/real legal organizational authority; runtime access/consent; eligible operational Training source classes and Dataset governance (#12); qualified independent review of 84 synthetic candidates (#13); accepted integration of these Business decisions into any actual slice gate. Do **not** re-ask which first use case is selected or represent PR #10 as merged.

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

The smallest Qualification Decision Business/authority set remains **OPEN on PR #9**; no human decision-maker, Qualification rule or Activation may be inferred. The **first AI informational use case has already been selected in Draft PR #10**, so its immediate next actions are **external factual evidence and authorized review**, not another selection packet: [#11 source and publication evidence](https://github.com/mahdimarzooghi4-debug/nasim/issues/11), [#12 source-specific Training Eligibility](https://github.com/mahdimarzooghi4-debug/nasim/issues/12) and [#13 independent human review of the 84 draft AI samples](https://github.com/mahdimarzooghi4-debug/nasim/issues/13). All are **OPEN**. No actual reviewer/staff or external dataset is supplied by this register.

**Recheck at every gate:** branch-specific Accepted Decision records are not silently promoted into `main`, Code/Technical, an approved Phase/Pilot, Hosted Stage or Production. Independently chosen Stage infrastructure is also still absent (D-0130); Product Owner's accepted pilot minimum and permissible explicit scope deferrals remain OPEN.

**This register is a planning document only; it neither claims that the above work is implemented nor replaces the Product Owner.**
