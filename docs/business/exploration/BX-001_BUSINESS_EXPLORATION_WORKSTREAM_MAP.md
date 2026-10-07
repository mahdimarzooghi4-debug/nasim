# BX-001 — Business Exploration Workstream Map

- **Status:** ACTIVE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** D-0001…D-0005 + D-0118 + BR-004 + PRODUCT_PROCESS
- **Purpose:** مشخص‌کردن Workstreamهایی که می‌توانند بدون بستن زودهنگام Open Decisionها جلو بروند، همراه با Trigger دقیق برای زمانی که تصمیم واقعی لازم می‌شود.

## 1. Operating principle

نسیم در مرحله Business باقی می‌ماند، اما تصمیم‌های OPEN نباید باعث توقف غیرضروری Exploration شوند.

اصل:

`Explore broadly; decide just in time; never guess a blocker.`

و:

`OPEN ≠ DEFERRED ≠ ACCEPTED`

## 2. Workstream map

### BX-W1 — Domain Vocabulary & Bounded Concepts

**Can proceed now**
- Elder
- Caregiver
- Supervisor
- Provider
- Need
- Referral
- Service
- Follow-up
- Satisfaction
- Observation
- Accepted State
- Reassessment
- Outcome
- Incident
- Risk
- Policy
- Dataset
- Model Version
- AI Use Case

**Must not decide yet**
- final workflow states
- permissions
- numeric thresholds
- exact eligibility
- exact Provider type per service

**Decision trigger**
وقتی یک اصطلاح قرار است وارد Contract رسمی، State Machine یا API/Data Model شود.

---

### BX-W2 — Elder Journey Decomposition

**Can proceed now**
Journey سطح بالا می‌تواند به مراحل قابل تحلیل شکسته شود:

`Contact → Case/Profile → Monitoring → Need → Initial Assessment → Referral → Service → Follow-up → Satisfaction → Reassessment/Continuation`

**Can explore**
- information produced at each step
- actor involved
- handoff points
- possible exception classes
- audit/provenance needs

**Must not decide yet**
- final referral authorization
- final closure semantics
- emergency rules
- exact reassessment cadence

**Decision trigger**
قبل از freeze شدن workflow/state contract.

---

### BX-W3 — Service & Need Model Exploration

**Can proceed now**
- three-layer service architecture
- direct-caregiver vs specialist-provider distinction
- Need-to-Service conceptual mapping
- Service Catalog versioning concept
- in-scope/out-of-scope representation

**Must not decide yet**
- active Pilot service list
- Provider type per service
- service eligibility
- pricing
- SLA
- Completion Evidence details

**Decision trigger**
قبل از final Service Catalog یا Referral routing contract.

---

### BX-W4 — Roles, Responsibility & Authority Model

**Can proceed now**
- actor inventory candidates
- responsibility boundaries
- Human/System/AI separation
- Role ≠ Permission
- Human review points
- separation-of-duties candidates

**Must not decide yet**
- final role inventory
- final authority matrix
- provider selection authority
- incident/risk owner
- emergency ownership

**Decision trigger**
قبل از Identity/Authorization design یا consequential workflow freeze.

---

### BX-W5 — Data, Consent & Provenance Model

**Can proceed now**
- data-class taxonomy
- Purpose-of-use taxonomy
- operational vs learning separation
- provenance/lineage requirements
- correction/history preservation
- runtime access vs training permission distinction

**Must not decide yet**
- final consent/legal basis
- final access matrix
- retention period
- export/sharing policy
- Training Eligibility details

**Decision trigger**
قبل از Production data collection, authorization or Dataset Builder contract.

---

### BX-W6 — AI Product Boundary Exploration

**Can proceed now**
- elder-facing assistant use-case families
- caregiver-facing assistant use-case families
- human-review pattern
- official-record boundary
- AI transparency/provenance
- fail-safe concepts
- evaluation/promotion separation
- automatic Dataset lifecycle conceptual flow

**Must not decide yet**
- final model family
- training algorithm
- final use-case activation list
- Training Eligibility
- evaluation thresholds
- promotion/rollback authority

**Decision trigger**
قبل از AI runtime contract, Dataset Builder or Production model lifecycle design.

---

### BX-W7 — Provider Network Exploration

**Can proceed now**
- Provider lifecycle concepts
- Registry concept
- qualification/activation separation
- referral acceptance/rejection concept
- service-result vs elder-outcome separation
- failure/re-route concepts

**Must not decide yet**
- exact Provider types
- qualification criteria
- SLAs
- ranking algorithm
- settlement model

**Decision trigger**
قبل از Provider Registry schema, referral routing or provider workflow freeze.

---

### BX-W8 — Outcome & Longitudinal State Exploration

**Can proceed now**
- Observation vs Accepted State vs Outcome
- Service Completion vs Need Resolution
- baseline/reassessment concept
- longitudinal history
- causal-claim boundary
- learning-signal provenance

**Must not decide yet**
- exact Outcome taxonomy
- outcome evidence validity
- reassessment cadence
- training-label validation rule

**Decision trigger**
قبل از Outcome/Reassessment contract or learning-label pipeline.

---

### BX-W9 — KPI, Evidence & Pilot Measurement Exploration

**Can proceed now**
- KPI family structure
- evidence package concept
- metric versioning
- operational / quality / economic / social dimensions
- AI quality evidence
- Dataset lifecycle evidence
- Risk/Incident evidence

**Must not decide yet**
- numeric targets
- thresholds
- Pilot success score
- GO/NO-GO authority

**Decision trigger**
قبل از formal Pilot launch or automated measurement/gate behavior.

---

### BX-W10 — Economics & Funding Exploration

**Can proceed now**
- Customer / Payor / Beneficiary distinction
- funding-flow concepts
- cost-category taxonomy
- economic-unit candidates
- billing/settlement boundary analysis

**Must not decide yet**
- sponsor/payor final values
- pricing
- compensation
- settlement formula
- break-even target

**Decision trigger**
قبل از any financial capability or Pilot budget contract.

---

### BX-W11 — Integration & Source-of-Truth Exploration

**Can proceed now**
- integration inventory template
- inbound/outbound/bidirectional categories
- source-of-truth patterns
- reconciliation concepts
- failure visibility
- provenance and external-data boundaries

**Must not decide yet**
- mandatory Pilot integrations
- Tarannom requirement
- exact external contracts
- protocol/API details

**Decision trigger**
قبل از external integration design.

---

### BX-W12 — Risk, Safety & Continuity Exploration

**Can proceed now**
- Risk vs Incident vs Escalation vs Emergency
- business criticality categories
- degraded-mode concepts
- recovery evidence
- audit during recovery
- AI/Dataset failure classes

**Must not decide yet**
- severity taxonomy values
- emergency ownership
- RTO/RPO
- 24/7 service
- medical triage responsibility

**Decision trigger**
قبل از Safety-critical workflow or continuity architecture freeze.

---

### BX-W13 — Policy, Configuration & Change Governance Exploration

**Can proceed now**
- Decision vs Configuration vs Runtime Execution
- Draft/Accepted/Active separation
- versioned policy concept
- effective dating
- override/rollback concepts
- no retroactive silent rewrite
- code deployment ≠ policy activation

**Must not decide yet**
- final policy owner/approver
- precedence rules
- emergency-change authority
- Production activation authority

**Decision trigger**
قبل از Policy Registry/activation workflow.

## 3. Cross-workstream dependencies

Key dependency order for later closure:

`Vocabulary → Journey/Service/Role → Data/Authority → AI/Provider/Outcome → KPI/Economics/Integration → Safety/Policy → Technical Gate`

این ترتیب الزام نمی‌کند که همه Workstreamها کامل بسته شوند؛ فقط وابستگی منطقی آنها را نشان می‌دهد.

## 4. What can be produced before Technical Entry

Business Exploration می‌تواند بدون عبور از Gate این Artifactها را تولید کند:

- canonical domain glossary
- conceptual journey map
- conceptual domain map
- actor/responsibility map
- data-class & provenance map
- AI use-case map
- provider lifecycle map
- outcome/learning lineage map
- KPI/evidence map
- integration inventory template
- risk/continuity map
- policy/configuration map
- decision-trigger matrix

این خروجی‌ها **non-binding** هستند تا زمانی که Decision مرتبط Accepted نشده باشد.

## 5. What must wait

تا قبل از Business → Technical Gate نباید Final اعلام شوند:

- architecture
- database/data model
- API contracts
- workflow state machines
- authorization model
- AI runtime design
- Dataset Builder implementation
- integration implementation
- implementation-ready backlog

## 6. Code boundary / Codex handoff

فرآیند رسمی نسیم همچنان:

`Business → Technical → Scrum/Product Backlog → Sprint → Code → ...`

وقتی پروژه واقعاً به مرحله **Code** برسد، ادامه پیاده‌سازی کد باید در **Codex** انجام شود.

Operational protocol:
1. قبل از هر اقدام کدنویسی، به Product Owner اعلام شود: **«اینجا نقطه ورود به کد است؛ ادامه را در Codex انجام بده.»**
2. در این گفتگو بدون دستور صریح Product Owner وارد Code implementation نشویم.
3. Business، Technical، Backlog و Sprint preparation می‌توانند پیش از آن در همین مسیر ادامه پیدا کنند.

## 7. Recommended next workstream

با توجه به اینکه بیشترین Workstreamهای بعدی به واژگان دقیق وابسته‌اند، گام بعدی:

**BX-002 — Canonical Domain Vocabulary & Concept Map**

Scope:
- تعریف دقیق مفاهیم اصلی Business
- تفکیک مفاهیم مشابه
- ثبت invariants
- مشخص‌کردن مفاهیمی که هنوز OPEN هستند
- بدون ساخت Data Model یا API

## 8. Current stage

- Current stage: **Business**
- Exploration: **ACTIVE**
- Business → Technical: **NOT READY**
- Code: **NOT STARTED**
- Codex handoff: **NOT YET TRIGGERED**
