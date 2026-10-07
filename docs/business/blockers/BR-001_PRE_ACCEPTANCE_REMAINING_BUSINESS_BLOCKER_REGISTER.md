# BR-001 — Pre-Acceptance Remaining Business Blocker Register

- **Status:** REFERENCE / CONTEXTUAL BLOCKER REGISTER
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** DC-015 + DA-008 + D-0118 + BX-015
- **Purpose:** نگهداری فهرست مرجع Blockerهای Business بدون فرض Acceptance برای D-0006…D-0117؛ هر Blocker فقط وقتی Slice/Work Item مرتبط آن را نیاز داشته باشد Context Triggered می‌شود.

> این سند به معنی Acceptance هیچ Candidate Decision نیست. طبق D-0118، subset مربوط به یک Slice فقط زمانی نیازمند تصمیم می‌شود که همان Slice صریحاً انتخاب و Dependency آن Trigger شود؛ Decisionهای نامرتبط OPEN می‌مانند.

## 1. Current governance state

- Accepted decisions: D-0001…D-0005 + D-0118
- Pending candidates: D-0006…D-0117
- Pending count: 112
- Global Technical Entry Gate: **NOT PASSED**
- DA-001…DA-008: prepared, awaiting Product Owner decision

اصل:

`Pending Candidate ≠ Accepted Baseline`

## 2. Classification rule

هر موضوع باز باید در یکی از این کلاس‌ها قرار گیرد:

- **A — MUST DECIDE BEFORE RELEVANT TECHNICAL SLICE WHEN TRIGGERED**
- **B — EXPLICITLY DEFER FOR CURRENT PILOT**
- **C — TECHNICAL DECISION**
- **D — LATER DELIVERY / OPERATIONS**

تا زمانی که Deferral صریح وجود ندارد:

`Unknown ≠ Deferred`

## 3. A — MUST DECIDE BEFORE RELEVANT TECHNICAL SLICE WHEN TRIGGERED

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

The following list is a **cross-domain inventory**, not a requirement to close all items before every Technical activity.

For a selected Technical Slice, only applicable items become required and must be traceable Accepted decisions or explicit Deferrals:

1. Pilot/scope baseline if the Slice depends on it
2. active service baseline if service/referral is in scope
3. authority baseline for consequential actions in scope
4. legal/data/access baseline for Data Classes in scope
5. AI Day-one governance if AI behavior is in scope
6. Training Eligibility if Dataset Builder/learning is in scope
7. Provider baseline if Provider capability is in scope
8. KPI/evidence baseline if measurement is in scope
9. Funding/payment scope if financial capability is in scope
10. Integration Inventory if external integration is in scope
11. Safety/Continuity baseline if safety/continuity behavior is in scope
12. Outcome/Reassessment baseline if longitudinal outcome is in scope
13. Policy/Activation governance for versioned runtime rules in scope
14. Explicit Deferrals used by the Slice Gate
15. Slice Gate Record

Unrelated items remain OPEN under D-0118.

## 8. Acceptance dependency

This Register currently assumes **nothing** from D-0006…D-0117 as Accepted.

After Product Owner Acceptance:

- accepted items will be removed from the unresolved set where applicable;
- open values explicitly preserved by their Boundaries will remain blockers;
- rejected/modified candidates will be re-evaluated;
- explicit Deferrals will move from Class A to Class B;
- the Technical Entry Gate will be re-run.

## 9. Current result

**Global Business → Technical: NOT PASSED**

Reason:
- D-0006…D-0117 remain not accepted.
- no bounded Technical Slice has been selected.
- therefore no minimal Slice-specific blocker set has been fully closed/gated.

The existence of 112 pending Candidate Decisions does **not** require bulk closure under D-0118.

## 10. Next allowed step without implicit acceptance

The safe next action is:
- complete documentation/gate preparation;
- then explicitly select one bounded Technical Slice using BX-015;
- Context Trigger only that Slice's minimal blocker set.

BR-002 remains a reference input sheet for values that a selected Slice actually needs.

## 11. Next step after explicit acceptance

When Product Owner explicitly accepts or defers a Slice-specific decision:
- update Decision/Deferral records;
- remove only resolved blockers from that Slice's unresolved set;
- preserve unrelated OPEN items;
- re-run only the relevant Slice Gate.

This Register does not require D-0006…D-0117 to be accepted as one batch.
