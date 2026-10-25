# DC-016 — Provider Qualification Decision & Authority — Business Decision Packet

- **Project:** نسیم — نظام سالمند‌یاری محله‌محور
- **Status:** DRAFT DECISION PACKET — D-0134 ACCEPTED (bounded three-function split); remaining qualification decisions OPEN
- **Stage:** Business / contextual decision closure only
- **Prepared:** 2026-10-08
- **Owner for decisions:** Product Owner (decision authority mapping is **not** implied)
- **Purpose:** روشن‌کردن کوچک‌ترین مجموعه تصمیم‌های کسب‌وکاری لازم پیش از طراحی Qualification Decision، بدون تعیین خودکار Rule، Role، Threshold، Credential، State یا Activation Policy.
- **Source basis:** `docs/DECISIONS.md` (D-0036…D-0042, D-0118, D-0124, D-0130…D-0134); `docs/business/contracts/BC-008_PROVIDER_NETWORK_PARTNER_GOVERNANCE.md`; `docs/business/closure/DC-003_ROLES_AUTHORITY_HUMAN_DECISION_RIGHTS_PACKET.md`; `docs/business/closure/DC-007_PROVIDER_MODEL_ONBOARDING_REFERRAL_ACCEPTANCE_SERVICE_EVIDENCE_PACKET.md`; `docs/business/blockers/BR-004_CONTEXTUAL_OPEN_DECISION_REGISTER.md`; Sprint 004–006 foundations.
- **Naming note:** `DC-008` already belongs to the Quality/KPI/Pilot/Scale packet. This packet uses the next free closure identifier `DC-016`; no existing packet is overwritten or renumbered.

> **Decision status contract:** This remains a draft decision packet, not a Technical contract or implementation authorization. Only the bounded three-function human responsibility separation has been Accepted as D-0134 on this branch's Decision Register; the other Business decisions remain **OPEN**. This introduces no actual organizational or technical authority, qualification criteria, permission, or Provider Activation. `OPEN ≠ DEFERRED ≠ ACCEPTED`.

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

## 1.1 Accepted Product Owner direction — D-0134 (bounded)

The Product Owner approved the recommended three-function human-responsibility structure:

1. **سالمندیار** — introduces Providers, performs field evaluation, records evidence and offers a recommendation; may not be final qualification decision maker for their own proposal merely by virtue of caregiver role.
2. **بازبین واجد صلاحیت تخصصی** — performs accountable specialist review of relevant evidence against approved criteria; the actual qualification/appointment standards for this human remain undefined.
3. **مسئول دارای اختیار مصوب شبکه Provider نسیم** — accountable for the final Qualification Decision **only after** an explicit authority assignment is approved; this is a proposed organizational function, not an already instantiated role or permission grant.

The functional responsibilities are separate; the field proposer must not be final decision maker for the same proposed Provider. Actual authorized human identities, precise reviewer competence, person-level segregation / extra checker, permission matrix, conflicts, delegation, assignment, evidence criteria and state workflow are **still OPEN**. Do not infer a mandatory separate maker-checker requirement beyond this approved responsibility boundary.

**D-0134 does not approve Provider Qualification, organizational Approval, Activation, Service Eligibility, Provider Selection or Provider Case/Elder access.**

## 2. Business decision set — remaining OPEN (QD-02 partially resolved)

| Ref | OPEN decision | Product Owner must determine | Non-decision / forbidden shortcut |
|---|---|---|---|
| QD-01 | **Decision purpose and scope** | What exactly does a Qualification Decision attest? Candidate-wide vs per Provider Type / Service / Geography / other scope? Is it distinct from organizational Approval and independent operational Activation, and what consequences (if any) follow each? | Do not infer qualified, approved, eligible, selected, or active from any existing Candidate/Evidence/Request. |
| QD-02 | **Reviewer and approver identity/authority — PARTIALLY RESOLVED by D-0134** | Three functional responsibilities Accepted: caregiver field proposer → specialist reviewer → authorized network final qualification decision owner. Still OPEN: named/organizational assignments, human competence checks, actual authority and technical permissions, person-level checker/separation beyond the field-proposer prohibition, permitted scope, delegation, conflict of interest, reassignment and audit contract. | Functional titles confer no permission. Actual authority, specialist qualifications and any further maker-checker/approval rule remain OPEN. |
| QD-03 | **Qualification criteria and mandatory credentials** | Which criteria, documents/credentials, licensing/legal verification and sources of truth apply to which qualification scope, who owns policy definitions and versions, and what exceptions (if any) are legitimate? | No mandatory document list, credential verification shortcut, default criterion, scoring formula, threshold, or automatic pass. |
| QD-04 | **Evidence sufficiency, validity and review cadence** | What constitutes adequate, verified, current, trustworthy evidence? How are missing, disputed, expired, revoked, superseded or stale evidence treated? Who determines expiry/refresh, if any, and when is review/re-review required? | An attached evidence reference alone proves neither validity nor sufficiency. No invented validity duration, SLA, renewal cadence, or default `valid=true`. |
| QD-05 | **Evidence pinning and historical decision lineage** | Does a decision bind to a precisely identified immutable Evidence set/bundle and policy/criterion version? At what point is that basis frozen: request, review opening, or decision? How is replacement/additional evidence handled? | Evidence uploaded later may inform a **new** decision/review but must not mutate an earlier decision, its time-specific evidence basis, actor, rationale, or audit trail. No bundle policy is accepted yet. |
| QD-06 | **Decision vocabulary and lifecycle** | Which exact outcomes and transitions are legal? Define open/review, insufficient evidence, rejection, correction/rework, appeal/re-review, withdrawal, expiry/supersession, and who can initiate/approve each. Distinguish a negative qualification result from an incomplete review. | No guessed enums, numeric scores, approval by request submission, background transition, or implicit retry-to-pass. |
| QD-07 | **Qualification dimensions and dependency boundaries** | Do Provider Type, Service-to-Provider mapping, Geography, Capacity, Contract state or other dimensions belong inside qualification, later Approval, or Activation/Referral Eligibility? How are changes in any dimension handled? | No service mapping, geographic entitlement, operational capacity or permission from qualification alone. Referral destination/Provider Selection is a separate decision domain. |

**Only the three-function boundary within QD-02 is ACCEPTED (D-0134).** The remaining QD-02 details, QD-01 and QD-03…QD-07 are **OPEN**. Packet labels are not official D-numbers or implementation state constants.

## 2.1 QD-02 — Source of formal authority: decision input (OPEN)

The accepted D-0134 *function* `authorized Provider-network final qualification decision owner` is **not** itself an institutional issuer of authority. The Product Owner has not named the real organization/body empowered to appoint that decision owner. Do not assume the CEO, Board, a supervisor, a named department, or a technical admin has that authority.

**Non-binding possibilities to verify against real institutional documentation:**

| Candidate source for decision-owner appointment | Evidence needed before Product Owner can accept it |
|---|---|
| Accountable executive within the actual Nasim legal entity | Real organizational authority, its scope/limits, and documented authority to delegate qualification decisions |
| Authorized board / organizational governance body | Actual charter/resolution or other valid governance authority granting the body this decision right |
| Delegated network-governance officer under an authorized principal | Proven primary issuer, explicit documented delegation, scope, duration/withdrawal rules and traceable assignee |
| Another legally/organizationally empowered decision body | Its identity and independently verifiable source of authority |

**These are examples, not an approved authority matrix or an assumption that such offices exist.**

**Smallest Product Owner answer needed:** identify (a) the real authority-issuing person/body, (b) the evidence/basis for its appointment power, (c) the scope and boundaries of its delegation, and (d) whether the specialist reviewer and final decision signer must be different people, beyond the already accepted separation of responsibilities. Until this is answered, it remains **QD-02 / OPEN** and no role-to-permission grant, qualification decision endpoint or SG-007 is authorized.

## 3. Explicit separation of business concepts

| Concept | Already exists? | What it means / does not mean |
|---|---|---|
| Provider Candidate Registry Entry | Foundation implemented | Descriptive candidate identity/provenance, **not** an operational entitlement. |
| Qualification Evidence Reference | Foundation implemented | Historical evidence record/reference, **not** validation, sufficiency, criterion satisfaction, or approval. |
| Qualification Review Request | Foundation implemented | A request for review, **not** reviewer assignment, decision, qualification, or activation. |
| Qualification Review / Decision | **Not implemented; business semantics OPEN** | Only D-0134's human responsibility split is accepted; real authority assignments, qualification scope/criteria, evidence, decision effects and lifecycle must still be explicitly determined. |
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

A. **Authority first:** D-0134 establishes three human accountability functions. Still distinguish Review, Qualification Decision, Approval and Activation operationally; identify actual authorized humans and decide precise separation, checker, delegation, conflicts and permission mapping (QD-01 and remaining QD-02).

B. **Qualification basis:** agree which criteria/evidence policies exist and by what scope and version, and how sufficiency, validity and provenance are established (QD-03/04).

C. **Record and lifecycle:** approve historical evidence pinning, immutable decision lineage, outcomes and review/rework/re-review semantics (QD-05/06).

D. **Dependencies and boundaries:** identify whether Provider Type/Service/Geography/Capacity are qualification dimensions or separate controls (QD-07). Treat Activation as a separate subsequent business closure, not a default outcome.

For each answered item, record **decision wording, evidence/source, accountable business authority, status (ACCEPTED / explicitly DEFERRED / still OPEN), date, scope, version and downstream gate effect** in the actual decision process. Do not turn discussion notes or candidate options into Accepted decisions.

## 7. Gate and implementation effect

**Current disposition: D-0134 ACCEPTED for functional responsibility split only; Qualification Decision Business Gate NOT PASSED.**

- Allowed now: Product Owner review, clarification, evidence gathering, alternatives/risk comparison, explicit decision recording.
- Not authorized by this artifact: SG-007, T-007, Backlog, Sprint planning, Qualification Decision code, new role grants, fake reviewer authority, Provider activation, production/real-world Provider interactions.
- A future Qualification Decision technical slice may start **only after** the smallest relevant QD decision set is expressly accepted (or any permissible deferral is documented with owner, scope, future gate and safe constraint), with its own normal Business → Technical → Backlog → Sprint → Code sequence.
- **D-0130 remains in force:** Hosted Stage is UNAVAILABLE, not omitted from the process. CI container smoke is not Hosted Stage Admission or Stage-based QA; no Release Approval or Production is asserted.

**Next action:** Resolve QD-01, remaining QD-02 and only the context-triggered QD-03…QD-07 needed for a bounded future slice. **Stop at Business; no SG-007/T-007/Backlog/Sprint/Code.**
