# DC-015 — Business Exit Review, Decision Closure Matrix & Technical Entry Recommendation

- **Status:** DRAFT EXIT REVIEW
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** D-0001…D-0005 + D-0118 + BC-001…BC-025 + DC-001…DC-014 + BX-014 + BX-015
- **Purpose:** جمع‌بندی Business، تفکیک «پوشش مستند» از «تصمیم پذیرفته‌شده»، شناسایی Blockerهای واقعی و ارائه Recommendation برای ورود یا عدم ورود به Technical.

> این سند Decision Register نیست و هیچ Candidate Decision را Accepted نمی‌کند. Decision Register همچنان مرجع رسمی Acceptance است.

## 1. Executive result

### Current Business documentation coverage

**SUBSTANTIALLY COVERED**

نسیم اکنون برای حوزه‌های اصلی Business دارای Baseline، Business Contracts و Decision Closure Packets است.

### Current Business decision closure

**NOT CLOSED**

Decision Register در وضعیت به‌روزشده D-0001 تا D-0005 و D-0118 را به‌عنوان **Accepted** دارد.

### Technical Entry Gate recommendation

**NOT READY**

دلیل اصلی کمبود Document نیست؛ دلیل اصلی این است که Candidate Decisionهای آماده هنوز توسط Product Owner Accepted/Rejected/Modified نشده‌اند و چند Decision عملیاتی Phase/Pilot نیز هنوز نیازمند انتخاب صریح هستند.

اصل:

`Documentation Coverage ≠ Decision Closure`

و:

`Draft Candidate ≠ Accepted Decision`

## 2. Closure packet matrix

| Packet | Domain | Candidate Decisions | Current status |
|---|---|---:|---|
| DC-001 | Phase / Pilot Scope | D-0006…D-0007 | Prepared, not accepted |
| DC-002 | Service Architecture / Caregiver Boundary | D-0008…D-0010 | Prepared, not accepted |
| DC-003 | Roles / Authority / Human Decision Rights | D-0011…D-0015 | Prepared, not accepted |
| DC-004 | Journey / Referral / Escalation / Emergency | D-0016…D-0020 | Prepared, not accepted |
| DC-005 | Legal / Consent / Data / Training Eligibility | D-0021…D-0028 | Prepared, not accepted |
| DC-006 | Day-one AI / Human Oversight / Model Governance | D-0029…D-0035 | Prepared, not accepted |
| DC-007 | Provider Model / Onboarding / Evidence | D-0036…D-0042 | Prepared, not accepted |
| DC-008 | Quality / KPI / Pilot Success / Scale | D-0043…D-0050 | Prepared, not accepted |
| DC-009 | Economics / Funding / Financial Rights | D-0051…D-0060 | Prepared, not accepted |
| DC-010 | Integrations / External Dependencies | D-0061…D-0070 | Prepared, not accepted |
| DC-011 | Risk / Continuity / Security / Resilience | D-0071…D-0082 | Prepared, not accepted |
| DC-012 | Workforce / Scheduling / Communication / Case Ops | D-0083…D-0093 | Prepared, not accepted |
| DC-013 | Outcome / Reassessment / Learning Signal | D-0094…D-0104 | Prepared, not accepted |
| DC-014 | Configuration / Versioning / Change Control | D-0105…D-0117 | Prepared, not accepted |

### Summary

- Accepted decisions: **D-0001…D-0005 + D-0118**
- Prepared candidate decisions: **D-0006…D-0117**
- Candidate count: **112**
- Automatic acceptance from this matrix: **0**

## 3. What is now sufficiently framed

The following domains are sufficiently framed for Product Owner decision-making and do not require more exploratory Business Contracts before decisions can begin:

- Phase/Pilot scope
- Service layers and direct/referral boundary
- Roles and authority principles
- Elder journey and referral concepts
- Data/consent/access boundaries
- Day-one AI boundaries
- Dataset automation governance
- Provider-network governance
- KPI/quality/scale framework
- economic/funding framework
- integration governance
- risk/continuity/security framework
- workforce/operations/communication framework
- outcome/reassessment/learning framework
- policy/configuration/change governance

This does **not** mean these domains are Accepted.

## 4. Business blockers requiring explicit Product Owner decisions

The remaining Business Blockers can now be compressed into a smaller set of decision groups.

### A. Phase/Pilot Definition

Must close:
- Phase-1 target population
- Pilot geography
- enrollment/eligibility rule
- Pilot size
- Pilot duration
- active Phase-1 Service Catalog
- in-scope / out-of-scope services
- Provider scope
- Sponsor/Payor scope

### B. Operational Authority

Must close:
- Role inventory for Pilot
- Case assignment/reassignment authority
- Referral authorization
- Provider selection authority
- Provider acceptance/rejection boundary
- Need resolution/reopen authority
- complaint/escalation authority
- Incident/Risk authority
- Emergency safe-handling ownership
- delegation/substitution

### C. Legal / Data / Access

Must close:
- Consent/legal-basis direction per Purpose
- Authorized Representative model
- Data Access Matrix
- Provider data-sharing scope
- Employer reporting boundary
- AI Runtime access
- Retention/deletion direction required for Pilot
- export/sharing constraints

### D. AI / Learning Governance

Must close:
- final Phase-1 elder AI use cases
- final Phase-1 caregiver AI use cases
- Forbidden Actions
- Human Owner / Human Review per consequential use case
- Candidate Training Data Classes
- Training Eligibility / Exclusion rules
- Learning-label validity boundary
- Evaluation governance
- Model Promotion authority
- Model Rollback authority
- AI fail-safe behavior
- AI/Dataset incident ownership

### E. Provider Model

Must close:
- Provider types used in Pilot
- onboarding/qualification minimum
- activation authority
- service-to-provider mapping
- referral response semantics
- minimum Completion Evidence
- fallback/re-routing
- suspension authority
- data-sharing boundary

### F. KPI / Pilot / Scale

Must close:
- Pilot KPI catalog sufficient for evidence capture
- metric definitions
- Pilot Success dimensions
- required Evidence Package
- Scale Gate owner
- GO / CONDITIONAL GO / NO-GO governance
- risk/incident input to Gate

Numeric Targets may be Deferred only when the Technical design can still capture all required evidence and the Deferral is explicit.

### G. Economics / Funding Scope

Must close:
- Pilot Sponsor/Funding source
- whether elder payment is in scope
- whether Billing is in scope
- whether Provider Settlement is in scope
- Financial Approval ownership
- minimum economic evidence required from Pilot

Detailed long-term pricing, Margin and Break-even may be deferred if explicitly outside Pilot implementation scope.

### H. Integration / Continuity

Must close:
- Pilot Integration Inventory
- Mandatory / Optional / Deferred classification
- Tarannom Pilot requirement
- Source-of-Truth direction for mandatory integrations
- minimum data-sharing contract
- dependency/fallback behavior
- critical business capabilities
- minimum outage operation
- security constraints during recovery

### I. Policy / Change Governance

Must close:
- Policy Owner/Approver model
- activation authority
- minimum scope/precedence rule
- bounded override rule
- emergency-change authority
- Production policy activation ownership

## 5. Recommended closure classification

### Class A — BUSINESS BLOCKER

The decision groups in Section 4 are Class A unless explicitly moved to Class B with a recorded Deferral Decision.

### Class B — EXPLICITLY DEFERRED

Good candidates for explicit deferral when not required by Pilot:
- Provider ranking/scoring algorithm
- exact numeric SLA beyond safety-critical minimum
- long-term compensation formula
- long-term Provider tariff/settlement formula
- full-market Revenue Model
- advanced employer reporting/drill-down
- optional communication channels
- Voice Assistant
- advanced predictive/forecasting analytics
- non-Pilot integrations
- detailed national-scale organization design
- advanced rollout strategies

Deferral requires Scope, Owner, future Gate and constraint.

### Class C — TECHNICAL DECISION

May remain open after Business blockers close:
- system architecture
- service decomposition
- database
- API/protocol
- event/messaging technology
- hosting
- programming stack
- IdP technology
- observability
- backup technology
- AI model family
- training algorithm
- training orchestration
- dataset storage
- infrastructure sizing
- CI/CD

### Class D — LATER DELIVERY / OPERATIONS

Can be closed before later gates if Pilot architecture does not depend on exact values:
- some report layouts
- some operational cadences
- non-critical notification timing
- final dashboard layout
- certain non-safety numeric thresholds
- mature-scale organizational refinements

## 6. Cross-contract consistency review

Current Closure Packets intentionally preserve these invariants:

- Role ≠ Permission
- Caregiver ≠ Specialist Provider
- Family ≠ Automatically Authorized Representative
- System ≠ Independent Business Authority
- AI Suggestion ≠ Human Decision
- AI Output ≠ Official Record
- AI Inference ≠ Observed Fact
- Runtime Access ≠ Training Permission
- Operational Data ≠ Training Eligible
- Dataset Automation ≠ Governance Automation
- Model Version ≠ AI Policy Version
- Training/Evaluation Success ≠ Production Promotion
- Service Completion ≠ Need Resolution
- Outcome ≠ Proven Causal Impact
- Provider Result ≠ Final Elder Outcome
- Reporting/Analysis ≠ Approved Decision
- Integration Access ≠ Data Ownership
- External Data ≠ Automatically Trusted Truth
- Backup ≠ Proven Recovery
- Alert ≠ Confirmed Incident
- Code Deployment ≠ Silent Business Policy Change

No Technical design should violate these invariants unless a later Accepted Decision explicitly supersedes one.

## 7. Business exit package status

| Required artifact | Current assessment |
|---|---|
| Decision Register | EXISTS — D-0001…D-0005 + D-0118 Accepted |
| Business Contract set | EXISTS — BC-001…BC-025, currently Draft |
| Decision Closure Packets | EXISTS — DC-001…DC-014 |
| Phase/Pilot baseline | PARTIAL — decision candidates prepared |
| Service Catalog baseline | PARTIAL — architecture/boundary prepared, active catalog unresolved |
| Journey/Referral baseline | PARTIAL — high-level flow prepared, authority/lifecycle unresolved |
| Role/Decision Rights baseline | PARTIAL — principles prepared, authority matrix unresolved |
| Provider baseline | PARTIAL — governance prepared, Pilot provider decisions unresolved |
| Data/Consent/Access baseline | PARTIAL — principles prepared, matrix/legal basis unresolved |
| AI Day-one baseline | PARTIAL — candidate use cases/boundaries prepared, owners/governance unresolved |
| Training Eligibility/Dataset baseline | PARTIAL — automation direction accepted, eligibility rules unresolved |
| Quality/KPI/Pilot baseline | PARTIAL — framework prepared, definitions/gate ownership unresolved |
| Risk/Safety/Incident baseline | PARTIAL — framework prepared, severity/authority/emergency unresolved |
| Security/Continuity baseline | PARTIAL — principles prepared, criticality/minimum outage behavior unresolved |
| Integration Inventory | NOT CLOSED |
| Explicit Deferred Register | NOT YET CREATED |
| Technical-only Questions | IDENTIFIED conceptually, not yet formalized as exit artifact |
| Gate Record | NOT PASSABLE yet |

## 8. Technical Entry recommendation

### Recommendation: GLOBAL TECHNICAL ENTRY REMAINS NOT READY

D-0118 supersedes the old operational assumption that the next step must be a bulk acceptance round.

The repository is now ready for **bounded Technical-entry preparation**:

`Select Technical Slice → Resolve only slice blockers → Slice Gate → Technical for that Slice`

Starting Technical for an unselected or ungated scope would still force Business guessing and remains prohibited.

Candidate D-0006…D-0117 remain available as references when a selected Slice actually triggers them.

## 9. Recommended next action — Bounded Technical Slice Selection

The current default next action is **not** bulk review of D-0006…D-0117.

Current path under D-0118:

1. Select one bounded Technical Slice explicitly.
2. Use BX-015 to identify the smallest required Business decision set.
3. Move only that set to CONTEXT TRIGGERED.
4. Record accepted decisions or explicit deferrals.
5. Run a Slice Gate.

DA-001…DA-008 remain useful reference packets if their decisions are triggered by the selected Slice.

## 10. Historical acceptance batches — reference only

The following batches remain available as reference groupings, but D-0118 means Product Owner is not required to process them in bulk or in this order:

1. **Pilot Scope + Service Boundary** — D-0006…D-0010
2. **Roles + Journey + Safety** — D-0011…D-0020
3. **Data + Consent + AI Learning Boundary** — D-0021…D-0035
4. **Provider + Quality + Scale** — D-0036…D-0050
5. **Economics + Integration** — D-0051…D-0070
6. **Risk + Workforce + Operations** — D-0071…D-0093
7. **Outcome + Configuration Governance** — D-0094…D-0117

After each batch:
- update Decision Register
- mark superseded/merged candidates where needed
- update remaining Blocker Matrix

## 11. Conditions for changing recommendation to READY

Business → Technical may be recommended **READY** or **READY WITH EXPLICIT DEFERRALS** only when:

1. Class-A blockers actually required by the selected Technical Scope/Slice are Accepted or explicitly Deferred; unrelated decisions may remain OPEN.
2. Any Deferred item used to pass that Slice has owner, scope and future gate.
3. Pilot scope/service boundary is explicit only to the extent required by the selected Slice.
4. Authority and access boundaries are sufficient for Identity/Workflow design.
5. AI Day-one use cases, forbidden actions, data boundary and governance ownership are explicit.
6. Training Eligibility boundary is explicit enough to design automated Dataset Lifecycle.
7. Provider and Integration dependencies for Pilot are known.
8. Minimum Safety/Continuity behavior is defined.
9. KPI/Evidence requirements are sufficient to design measurement.
10. A Business Exit Gate Record is approved and registered.

## 12. Current gate record

- **Gate:** Business → Technical
- **Date:** 2026-10-07
- **Current global outcome:** **NOT PASSED**
- **Accepted baseline:** D-0001…D-0005 + D-0118
- **Selected Technical Slice:** NONE
- **Reason:** no bounded Slice has been explicitly selected and no Slice Gate Record has passed.
- **Allowed next activity:** documentation consistency cleanup, explicit bounded Slice selection, then contextual closure of only that Slice's blockers.
- **Not allowed yet:** global architecture freeze, implementation-ready backlog, or code based on unresolved Business assumptions.

## 13. Next artifact

No forced Decision Acceptance artifact is required under D-0118.

Current reference path:
- BX-015 — Technical Entry Slice Candidate Map
- BX-016 — Gate Preparation / Documentation Consistency Cleanup
- after cleanup verification, Product Owner explicitly selects the first bounded Technical Slice
- only that Slice's minimal Business blocker set becomes CONTEXT TRIGGERED

DA-001…DA-008 remain reference material and may be reused when a selected Slice triggers their decisions.
