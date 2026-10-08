# DC-016 — Provider Qualification Decision & Authority — Business Decision Packet

- **Project:** نسیم — نظام سالمند‌یاری محله‌محور
- **Status:** DRAFT DECISION PACKET — BUSINESS DECISIONS OPEN
- **Stage:** Business / contextual decision closure only
- **Prepared:** 2026-10-08
- **Owner for decisions:** Product Owner (decision authority mapping is **not** implied)
- **Purpose:** روشن‌کردن کوچک‌ترین مجموعه تصمیم‌های کسب‌وکاری لازم پیش از طراحی Qualification Decision، بدون تعیین خودکار Rule، Role، Threshold، Credential، State یا Activation Policy.
- **Source basis:** `docs/DECISIONS.md` (D-0036…D-0042, D-0118, D-0124, D-0130…D-0133); `docs/business/contracts/BC-008_PROVIDER_NETWORK_PARTNER_GOVERNANCE.md`; `docs/business/closure/DC-003_ROLES_AUTHORITY_HUMAN_DECISION_RIGHTS_PACKET.md`; `docs/business/closure/DC-007_PROVIDER_MODEL_ONBOARDING_REFERRAL_ACCEPTANCE_SERVICE_EVIDENCE_PACKET.md`; `docs/business/blockers/BR-004_CONTEXTUAL_OPEN_DECISION_REGISTER.md`; Sprint 004–006 foundations.
- **Naming note:** `DC-008` already belongs to the Quality/KPI/Pilot/Scale packet. This packet uses the next free closure identifier `DC-016`; no existing packet is overwritten or renumbered.

> **Decision status contract:** This is a question/decision packet, not an Accepted Decision, Decision Register update, Authority Matrix, Technical contract, implementation authorization, or approval to activate any Provider. Each item below remains **OPEN**, unless separately resolved by an explicit Product Owner decision and recorded in the official decision register. `OPEN ≠ DEFERRED ≠ ACCEPTED`.

## 1. Confirmed baseline — not a new decision

Sprint 004 implemented only a Provider Candidate Registry foundation; Sprint 005 implemented only immutable descriptive Qualification Evidence references; Sprint 006 implemented only Qualification Review Requests linked to Provider Candidates. Sprint 006 code has already been incorporated in `main` (reviewed `e8de2cc519714dbaec46b3d8a62ed17bc2845b3b`; `main` `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`; exact-main CI [#95](https://github.com/mahdimarzooghi4-debug/nasim/actions/runs/37803350724) SUCCESS). Historical PR [#7](https://github.com/mahdimarzooghi4-debug/nasim/pull/7) has been closed without merge to reconcile its stale state.

Existing product boundaries remain:

- `Registry Entry ≠ Operational Activation`.
- `Provider Eligibility ≠ Provider Selection`.
- `Qualification Evidence ≠ Qualification Decision ≠ Activation`.
- `Review Request ≠ Review Decision ≠ Activation`.
- `Qualification Decision ≠ Approval ≠ Activation` — exact authority and semantics of each step are OPEN.
- Role title does not grant permissions; ActorType does not prove decision authority; AI/System/Automation have no implicit human decision right.
- Mere evidence existence or request existence is not proof of qualification.
- Historical decisions must remain immutable and auditable; later evidence cannot silently rewrite the evidence basis or result of an earlier decision.

No Qualification Decision implementation, Provider Approval, Activation, Selection, Service mapping, Capacity, Provider Case/Elder access, Ranking, Finance/Settlement, or external Provider integration is authorized or delivered by this packet.

## 2. Business decision set — all OPEN

| Ref | OPEN decision | Product Owner must determine | Non-decision / forbidden shortcut |
|---|---|---|---|
| QD-01 | **Decision purpose and scope** | What exactly does a Qualification Decision attest? Candidate-wide vs per Provider Type / Service / Geography / other scope? Is it distinct from organizational Approval and independent operational Activation, and what consequences (if any) follow each? | Do not infer qualified, approved, eligible, selected, or active from any existing Candidate/Evidence/Request. |
| QD-02 | **Reviewer and approver identity/authority** | Which accountable human actor may review, which may issue an authoritative qualification decision, whether a second approver is required, permitted scope, delegation, conflict of interest, separation of duties / maker-checker, reassignment, and audit requirements? | A Role title, system permission string, ActorType or submitted request is not authority. Maker-checker is not yet decided. |
| QD-03 | **Qualification criteria and mandatory credentials** | Which criteria, documents/credentials, licensing/legal verification and sources of truth apply to which qualification scope, who owns policy definitions and versions, and what exceptions (if any) are legitimate? | No mandatory document list, credential verification shortcut, default criterion, scoring formula, threshold, or automatic pass. |
| QD-04 | **Evidence sufficiency, validity and review cadence** | What constitutes adequate, verified, current, trustworthy evidence? How are missing, disputed, expired, revoked, superseded or stale evidence treated? Who determines expiry/refresh, if any, and when is review/re-review required? | An attached evidence reference alone proves neither validity nor sufficiency. No invented validity duration, SLA, renewal cadence, or default `valid=true`. |
| QD-05 | **Evidence pinning and historical decision lineage** | Does a decision bind to a precisely identified immutable Evidence set/bundle and policy/criterion version? At what point is that basis frozen: request, review opening, or decision? How is replacement/additional evidence handled? | Evidence uploaded later may inform a **new** decision/review but must not mutate an earlier decision, its time-specific evidence basis, actor, rationale, or audit trail. No bundle policy is accepted yet. |
| QD-06 | **Decision vocabulary and lifecycle** | Which exact outcomes and transitions are legal? Define open/review, insufficient evidence, rejection, correction/rework, appeal/re-review, withdrawal, expiry/supersession, and who can initiate/approve each. Distinguish a negative qualification result from an incomplete review. | No guessed enums, numeric scores, approval by request submission, background transition, or implicit retry-to-pass. |
| QD-07 | **Qualification dimensions and dependency boundaries** | Do Provider Type, Service-to-Provider mapping, Geography, Capacity, Contract state or other dimensions belong inside qualification, later Approval, or Activation/Referral Eligibility? How are changes in any dimension handled? | No service mapping, geographic entitlement, operational capacity or permission from qualification alone. Referral destination/Provider Selection is a separate decision domain. |

**All QD-01…QD-07 are OPEN.** Their labels are packet references, not new official D-numbers or implementation state constants.

## 3. Explicit separation of business concepts

| Concept | Already exists? | What it means / does not mean |
|---|---|---|
| Provider Candidate Registry Entry | Foundation implemented | Descriptive candidate identity/provenance, **not** an operational entitlement. |
| Qualification Evidence Reference | Foundation implemented | Historical evidence record/reference, **not** validation, sufficiency, criterion satisfaction, or approval. |
| Qualification Review Request | Foundation implemented | A request for review, **not** reviewer assignment, decision, qualification, or activation. |
| Qualification Review / Decision | **Not implemented; business semantics OPEN** | Human accountability, scope, criteria, evidence, decision effects and lifecycle must be explicitly determined first. |
| Separate Approval | **Business purpose / authority OPEN** | May not be conflated with qualification or derived from a reviewer title. |
| Operational Activation | **Independent OPEN contract** | Not a side effect of Qualification Decision, Approval, or Registry entry. |
| Provider Eligibility and Selection | **Independent OPEN contracts** | Eligibility is not selection; no automated ranking/routing or access arises from this packet. |

## 4. Historical integrity questions for Product Owner

The **accepted boundary** is that a historical decision must be immutable/auditable, with no silent rewrite by subsequent Evidence. The **operational policy** is still OPEN:

1. Which evidence identities and versions must be pinned, and which event/time constitutes the decision's evidence cutoff?
2. Must reviewers acknowledge the exact bundle and criteria version before decision? What is the approved correction mechanism for a mistaken bundle or decision?
3. How is newly supplied, withdrawn or expired evidence linked to **reassessment / a new decision**, while preserving the historical result?
4. How should an earlier decision be displayed when policy, evidence, provider identity or qualification scope changes?
5. What are the permitted retention, restricted access, inspection and audit boundaries for historical qualification materials?

These questions do **not** authorize a persistence schema, API, event, command or status vocabulary.

## 5. Activation is a separate, unresolved decision package

Even after Qualification Decision is defined and implemented, Activation is **not** implicitly approved. Before any activation work, Business must separately decide:

- accountable activation authority and any independent approval / maker-checker requirements;
- prerequisites (including qualification result, contract/legal conditions and required verification where applicable);
- activation scope and effective date;
- changes in scope; suspension, deactivation, expiry and revocation triggers and authority;
- consequences for existing referrals, provider access, notification, service availability and historical records;
- reactivation and reinstatement governance.

**Status for every point:** OPEN. No activation API, rule, status or effective date is defined here.

## 6. Product Owner decision agenda (sequenced, no presumed answers)

A. **Authority first:** distinguish Review, Qualification Decision, Approval and Activation; identify authorized humans and whether separation of duties is necessary (QD-01/02).

B. **Qualification basis:** agree which criteria/evidence policies exist and by what scope and version, and how sufficiency, validity and provenance are established (QD-03/04).

C. **Record and lifecycle:** approve historical evidence pinning, immutable decision lineage, outcomes and review/rework/re-review semantics (QD-05/06).

D. **Dependencies and boundaries:** identify whether Provider Type/Service/Geography/Capacity are qualification dimensions or separate controls (QD-07). Treat Activation as a separate subsequent business closure, not a default outcome.

For each answered item, record **decision wording, evidence/source, accountable business authority, status (ACCEPTED / explicitly DEFERRED / still OPEN), date, scope, version and downstream gate effect** in the actual decision process. Do not turn discussion notes or candidate options into Accepted decisions.

## 7. Gate and implementation effect

**Current disposition: BUSINESS DECISION PACKET PREPARED; Qualification Decision Business Gate NOT PASSED.**

- Allowed now: Product Owner review, clarification, evidence gathering, alternatives/risk comparison, explicit decision recording.
- Not authorized by this artifact: SG-007, T-007, Backlog, Sprint planning, Qualification Decision code, new role grants, fake reviewer authority, Provider activation, production/real-world Provider interactions.
- A future Qualification Decision technical slice may start **only after** the smallest relevant QD decision set is expressly accepted (or any permissible deferral is documented with owner, scope, future gate and safe constraint), with its own normal Business → Technical → Backlog → Sprint → Code sequence.
- **D-0130 remains in force:** Hosted Stage is UNAVAILABLE, not omitted from the process. CI container smoke is not Hosted Stage Admission or Stage-based QA; no Release Approval or Production is asserted.

**Next action:** Product Owner to resolve only the context-triggered QD questions necessary for a bounded future slice. **Stop at this Business packet.**
