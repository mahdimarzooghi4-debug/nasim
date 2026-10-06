# BR-001 — Pre-Acceptance Remaining Business Blocker Register

- **Status:** PRE-ACCEPTANCE DRAFT
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** DC-015 + DA-008
- **Purpose:** آماده‌سازی فهرست Blockerهای واقعی باقی‌مانده بدون فرض Acceptance برای D-0006…D-0117.

> این سند به معنی Acceptance هیچ Candidate Decision نیست. تا زمانی که مالک محصول D-0006…D-0117 یا subset مربوطه را صریحاً Accept نکند، این Register فقط یک Working Draft برای مرحله بعد است.

## 1. Current governance state

- Accepted decisions: D-0001…D-0005
- Pending candidates: D-0006…D-0117
- Pending count: 112
- Technical Entry Gate: **NOT READY**
- DA-001…DA-008: prepared, awaiting Product Owner decision

اصل:

`Pending Candidate ≠ Accepted Baseline`

## 2. Classification rule

هر موضوع باز باید در یکی از این کلاس‌ها قرار گیرد:

- **A — MUST DECIDE BEFORE TECHNICAL**
- **B — EXPLICITLY DEFER FOR CURRENT PILOT**
- **C — TECHNICAL DECISION**
- **D — LATER DELIVERY / OPERATIONS**

تا زمانی که Deferral صریح وجود ندارد:

`Unknown ≠ Deferred`

## 3. A — MUST DECIDE BEFORE TECHNICAL

### A1. Pilot Scope
- Pilot geography
- Pilot elder count / operating size
- Pilot duration
- detailed enrollment eligibility
- exit / suspension rules
- active Phase-1 Service Items
- in-scope / out-of-scope service boundary
- Pilot Provider scope
- Pilot Sponsor / Funding direction

### A2. Operational Authority
- Pilot role inventory
- Case assignment / reassignment authority
- Referral authorization
- Provider selection authority
- Provider acceptance / rejection semantics
- Need Resolution / Reopen authority
- Complaint owner / path
- Incident / Risk ownership
- Emergency safe-handling ownership
- Delegation / substitution

### A3. Legal / Consent / Data Access
- Consent / legal-basis direction per Purpose
- Authorized Representative model
- minimum Data Access Matrix
- Provider data-sharing boundary
- Employer reporting boundary
- AI Runtime data boundary
- Training-eligible Data Classes
- minimum Retention / Deletion direction required for Pilot
- Export / Sharing constraints

### A4. AI / Learning Governance
- final Phase-1 elder AI Use Cases
- final Phase-1 caregiver AI Use Cases
- Forbidden Actions
- Human Owner per consequential Use Case
- Human Review rule
- Training Eligibility / Exclusion rules
- Learning-label validity boundary
- Evaluation Governance
- Model Promotion authority
- Model Rollback authority
- AI fail-safe behavior
- AI / Dataset Incident owner

### A5. Provider Model
- Provider Types for Pilot
- onboarding / qualification minimum
- activation authority
- Service-to-Provider mapping
- Referral response semantics
- minimum Completion Evidence
- re-routing / fallback
- suspension authority
- Provider data-sharing boundary

### A6. KPI / Pilot / Scale
- Pilot KPI catalog sufficient for evidence capture
- metric business definitions
- evidence source per KPI
- Pilot Success dimensions
- minimum Evidence Package
- Scale Gate owner
- GO / CONDITIONAL GO / NO-GO governance
- Risk / Incident evidence in Scale Gate

### A7. Economics / Funding
- Pilot Sponsor
- Payor scope
- whether direct elder payment is in scope
- whether Billing is in scope
- whether Provider Settlement is in scope
- Financial Approval ownership
- minimum economic evidence required from Pilot

### A8. Integration / Continuity
- Pilot Integration Inventory
- Mandatory / Optional / Deferred classification
- Tarannom Pilot requirement
- Source-of-Truth direction for mandatory integrations
- minimum data-sharing contract
- dependency / fallback behavior
- critical business capabilities
- minimum operation during outage
- security constraints during recovery

### A9. Outcome / Reassessment
- Reassessment definition
- Reassessment trigger / cadence needed for Pilot
- Baseline rule
- Need Resolution criteria
- Reopen / Recurrence rule
- Outcome evidence-validity boundary
- Outcome owner / reviewer
- Outcome Training Eligibility / Label Validation boundary

### A10. Policy / Change Governance
- Policy Owner / Approver model
- Activation authority
- minimum Scope / Precedence rule
- bounded Override rule
- Emergency Change authority
- Production Policy Activation ownership

## 4. B — GOOD CANDIDATES FOR EXPLICIT DEFERRAL

These are not automatically deferred. They are candidates only if Product Owner explicitly places them outside the Pilot Technical Scope:

- Provider ranking / scoring algorithm
- advanced Provider quality ranking
- exact non-safety SLA values
- long-term caregiver compensation formula
- long-term Provider tariff / settlement formula
- full-market Revenue Model
- mature Unit Economics / Break-even targets
- employer advanced drill-down reporting
- optional communication channels
- Voice Assistant
- advanced forecasting / predictive analytics
- non-Pilot integrations
- national-scale organization design
- advanced rollout strategies
- long-term concentration limits
- mature-scale workforce promotion thresholds
- non-critical report layouts
- advanced dashboard presentation

Every Deferral must have:
- scope
- reason
- owner
- future gate
- constraint
- what Technical must not assume

## 5. C — TECHNICAL DECISIONS

These may remain open once Business Intent above is closed:

- system architecture
- service decomposition
- database technology
- API style
- event / messaging technology
- hosting topology
- programming language / framework
- identity technology
- observability stack
- backup implementation
- DR implementation
- AI model family
- training algorithm
- fine-tuning approach
- training orchestration
- dataset storage / layout
- runtime / inference implementation
- integration protocol
- CI/CD
- infrastructure sizing
- policy-engine technology
- workflow-engine technology

## 6. D — LATER DELIVERY / OPERATIONS

Can be closed at later gates only if not required for initial Technical architecture:

- final dashboard layout
- non-critical report formatting
- non-safety notification timing
- some operational cadence values
- mature-scale organization refinements
- optimization of workforce ratios
- non-critical convenience features
- advanced rollout percentages
- mature-market commercial refinements

## 7. Minimum package required before Technical Entry

Before Business → Technical can change from NOT READY, at minimum the following must become traceable Accepted Business decisions or explicit Deferrals:

1. Pilot scope baseline
2. active service baseline
3. minimum authority matrix
4. minimum legal/data/access baseline
5. AI Day-one governance baseline
6. Training Eligibility baseline
7. Provider Pilot baseline
8. KPI/evidence baseline
9. Funding/payment scope baseline
10. Integration Inventory
11. minimum Safety/Continuity baseline
12. Outcome/Reassessment baseline
13. Policy/Activation governance baseline
14. Explicit Deferred Decision Register
15. Business Exit Gate Record

## 8. Acceptance dependency

This Register currently assumes **nothing** from D-0006…D-0117 as Accepted.

After Product Owner Acceptance:

- accepted items will be removed from the unresolved set where applicable;
- open values explicitly preserved by their Boundaries will remain blockers;
- rejected/modified candidates will be re-evaluated;
- explicit Deferrals will move from Class A to Class B;
- the Technical Entry Gate will be re-run.

## 9. Current result

**Business → Technical: NOT READY**

Reason:
- 112 Candidate Decisions remain Pending.
- multiple Pilot-specific values remain unresolved.
- no Explicit Deferred Register exists yet.
- no passable Business Exit Gate Record exists yet.

## 10. Next allowed step without implicit acceptance

Because Product Owner has not yet explicitly accepted D-0006…D-0117, the next safe action is:

**BR-002 — Pilot-specific Decision Input Sheet**

It will request only the remaining concrete values that cannot be inferred from the source, while keeping all pending Candidate Decisions untouched.

## 11. Next step after explicit acceptance

If Product Owner explicitly accepts D-0006…D-0117, this BR-001 should be revised into the authoritative **Remaining Business Blocker Register**, then Decision Register and Gate status should be updated.
