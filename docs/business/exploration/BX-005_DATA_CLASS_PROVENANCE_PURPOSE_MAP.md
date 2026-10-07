# BX-005 — Data Class, Provenance & Purpose-of-Use Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** BX-004 + BC-007 + BC-014 + BC-017 + BC-019 + DC-005 + D-0004 + D-0005 + D-0118
- **Purpose:** مشخص‌کردن Data Classهای مفهومی نسیم، Source/Provenance، Purposeهای قابل بررسی، مرز AI Runtime و Training Candidate، و الزامات Correction/History؛ بدون ساخت Database Schema، Retention Period، Access Matrix نهایی یا Training Eligibility Policy.

> این سند «وجود یا نیاز مفهومی به یک Data Class» را از «اجازه پردازش، دسترسی یا Training» جدا می‌کند.

## 1. Core data-governance rules

این قواعد در تمام Exploration بعدی باید حفظ شوند:

`Operationally Available ≠ Training Eligible`

`AI Runtime Access ≠ Training Permission`

`Provider Access ≠ Full Elder Record Access`

`Employer Supervision ≠ Unrestricted Individual Access`

`Recorded Data ≠ Automatically Verified Fact`

`AI Output ≠ Official Record`

`AI Inference ≠ Observed Fact`

`Recorded Outcome ≠ Automatically Verified Training Label`

`Automatic Dataset Generation ≠ Automatic Governance Change`

و طبق D-0118:

`OPEN ≠ DEFERRED ≠ ACCEPTED`

## 2. Purpose-of-use frame

برای جلوگیری از اختلاط Purposeها، داده ممکن است برای یک یا چند Purpose زیر بررسی شود؛ هر Purpose نیازمند مجوز/Policy مستقل است:

- **P1 — Service Delivery**
- **P2 — Caregiver Operations**
- **P3 — Referral / Provider Coordination**
- **P4 — Quality / Audit**
- **P5 — Management Reporting**
- **P6 — Employer / Sponsor Reporting**
- **P7 — Outcome / Reassessment**
- **P8 — AI Runtime Assistance**
- **P9 — AI Evaluation**
- **P10 — AI Training / Dataset**
- **P11 — Research / Impact Evaluation**, only if later approved
- **P12 — Security / Incident / Compliance**
- **P13 — Financial / Settlement**, only if later in scope

وجود Purpose در این Frame به معنی مجاز بودن آن نیست.

## 3. Provenance model — conceptual

هر Data Item مهم باید در آینده بتواند حداقل این ابعاد را حفظ کند:

- source actor / system
- source type
- capture time
- event / interaction context
- related elder/case/need/referral/service where applicable
- definition/taxonomy/policy version where relevant
- whether original, derived, summarized or inferred
- reviewer/acceptance status where applicable
- correction/supersession history
- AI involvement, if any

### Source families

- Elder
- Family Contact
- Authorized Representative
- Caregiver
- Supervisor
- Provider
- NASIM Operations
- Employer/Sponsor
- NASIM System
- External System
- Internal AI
- Human-reviewed AI Output

### Invariant

`Source must remain distinguishable across operations, audit and dataset lineage.`

## 4. Data class map — Identity & Contact

### DCL-01 — Elder Identity
Examples:
- identifying information
- identifiers
- identity-verification references

**Primary source:** Elder / authorized source / employer source where valid.  
**Operational purposes:** P1, P2, P3, P12.  
**AI Runtime:** only if approved Use Case needs it.  
**Training candidate:** **NOT AUTOMATIC**.  
**OPEN:** exact fields, sensitivity classification, legal basis, de-identification requirement.

### DCL-02 — Contact Information
Examples:
- phone/contact route
- address/location context
- preferred contact channel

**Operational purposes:** P1, P2, P3.  
**AI Runtime:** conditional, use-case limited.  
**Training candidate:** not automatic.  
**OPEN:** field list, family contact boundaries, communication preferences.

### DCL-03 — Family / Representative Relationship Data
Examples:
- relation to elder
- contact status
- representative status if formally established

**Invariant:** `Family Contact ≠ Authorized Representative`.  
**Operational purposes:** P1, P2, possibly P3/P12.  
**AI Runtime:** only when approved and necessary.  
**Training candidate:** not automatic.  
**OPEN:** verification, authority scope, access, expiration/revocation.

## 5. Data class map — Case & Operations

### DCL-04 — Case/Profile Context
Examples:
- operational profile
- current assignments
- active work context
- relevant open obligations

**Source:** Caregiver / Operations / valid source records.  
**Operational purposes:** P1, P2, P3.  
**AI Runtime:** likely candidate for approved caregiver-assistant use cases, but access is not yet approved.  
**Training candidate:** only after Training Eligibility.  
**Correction rule:** history must not be silently overwritten.

### DCL-05 — Contact / Interaction Record
Examples:
- interaction occurrence
- actor/channel/time
- purpose
- follow-up need

**Operational purposes:** P2, P4, P7.  
**AI Runtime:** possible for summarization/reminders under approved policy.  
**Training candidate:** conditional; conversation content is not automatically eligible.  
**OPEN:** content level, channel-specific rules, recording/retention.

### DCL-06 — Work / Task Evidence
Examples:
- planned follow-up
- completed operational task
- missed work
- handoff/substitution evidence

**Operational purposes:** P2, P4, P5.  
**AI Runtime:** possible for task summary/prioritization assistance.  
**Training candidate:** conditional.  
**Invariant:** AI-suggested task must remain distinguishable from human/system-created obligation.

## 6. Data class map — Observation, Need & Assessment

### DCL-07 — Observation
Examples:
- elder report
- caregiver observation
- Provider observation
- structured measure where later defined

**Operational purposes:** P1, P2, P7.  
**AI Runtime:** may be summarized/compared if approved.  
**Training candidate:** conditional and provenance-sensitive.  
**Invariant:** `Observation ≠ Accepted State`.  
**Correction:** original/corrected history must remain traceable.

### DCL-08 — Need
Examples:
- identified Need
- category/version when taxonomy exists
- supporting evidence
- status/lifecycle only after later decision

**Operational purposes:** P1, P2, P3, P7.  
**AI Runtime:** AI may flag/suggest candidate Need in approved use case, not finalize by default.  
**Training candidate:** conditional.  
**OPEN:** taxonomy, authority, severity, duplicate/recurrence rule.

### DCL-09 — Assessment / Reassessment Evidence
Examples:
- assessment inputs
- definition/version
- reviewer/source
- result

**Operational purposes:** P1, P7.  
**AI Runtime:** AI-assisted analysis possible under human review.  
**Training candidate:** potentially valuable but not automatically eligible.  
**Invariant:** assessment/reassessment definition version must remain traceable.

## 7. Data class map — Referral & Service

### DCL-10 — Referral Data
Examples:
- related Need
- service family/item
- referral rationale
- target Provider/route
- authorization evidence when later defined

**Operational purposes:** P1, P2, P3, P4.  
**AI Runtime:** may explain/summarize or suggest candidate path under approved policy.  
**Training candidate:** conditional.  
**OPEN:** lifecycle states, authorization, consent, selection, SLA.

### DCL-11 — Provider Data
Examples:
- provider identity
- qualification/activation evidence
- service scope
- capacity/availability where later defined

**Operational purposes:** P3, P4, P5.  
**AI Runtime:** possible for catalog/search/recommendation support, not final selection authority.  
**Training candidate:** depends on purpose and class; not automatic.  
**OPEN:** Provider Registry fields, qualification, access, ranking.

### DCL-12 — Service Delivery Evidence
Examples:
- service performed
- time
- service definition/version
- completion evidence
- exceptions/failure

**Operational purposes:** P1, P3, P4, P7.  
**AI Runtime:** may support follow-up summaries.  
**Training candidate:** conditional.  
**Invariant:** `Service Completion ≠ Need Resolution ≠ Outcome`.

### DCL-13 — Provider Result
Examples:
- provider-reported service result
- professional report
- completion/result evidence

**Operational purposes:** P1, P3, P7.  
**AI Runtime:** may be summarized when approved.  
**Training candidate:** conditional and must preserve Provider provenance.  
**Invariant:** `Provider Result ≠ Final Elder Outcome`.

## 8. Data class map — Satisfaction, Complaint, Incident & Risk

### DCL-14 — Satisfaction / Experience Feedback
**Source:** primarily Elder, possibly valid representative under future policy.  
**Operational purposes:** P4, P5, P7.  
**AI Runtime:** may summarize/identify themes if approved.  
**Training candidate:** conditional.  
**Invariant:** `Satisfaction ≠ Outcome`.

### DCL-15 — Complaint
**Operational purposes:** P4, P12.  
**AI Runtime:** possible classification/summarization assistance only if approved.  
**Training candidate:** highly governance-sensitive; not automatic.  
**Invariant:** Complaint remains distinct from dissatisfaction, Incident and Emergency.

### DCL-16 — Incident
**Operational purposes:** P12, P4, possibly P5.  
**AI Runtime:** may flag/support analysis; no autonomous final incident decision by default.  
**Training candidate:** conditional/high-sensitivity.  
**Invariant:** `Alert ≠ Confirmed Incident`.

### DCL-17 — Risk Record
**Operational purposes:** P12, P4, P5.  
**AI Runtime:** analytical support may be possible.  
**Training candidate:** conditional.  
**Invariant:** `Risk ≠ Incident`.

## 9. Data class map — Longitudinal State & Outcome

### DCL-18 — Accepted State
**Meaning:** official state accepted through a valid future process.  
**Operational purposes:** P1, P7.  
**AI Runtime:** may be used if allowed for the Use Case.  
**Training candidate:** conditional.  
**Invariant:** `Observation ≠ Accepted State`.  
**OPEN:** acceptance authority and evidence rule.

### DCL-19 — Baseline
**Operational purposes:** P7.  
**AI Runtime:** may support comparison.  
**Training candidate:** conditional.  
**OPEN:** baseline definition/instrument/version.

### DCL-20 — Outcome
**Operational purposes:** P7, P4, P5.  
**AI Runtime:** AI may assist analysis under review.  
**Training candidate:** conditional and label-governed.  
**Invariants:**
- `Observed Change ≠ Proven Causal Effect`
- `Recorded Outcome ≠ Automatically Verified Training Label`

### DCL-21 — Need Resolution / Reopen Evidence
**Operational purposes:** P1, P7.  
**AI Runtime:** may support review, not final decision by default.  
**Training candidate:** conditional.  
**OPEN:** criteria, authority, recurrence/reopen semantics.

## 10. Data class map — Communications

### DCL-22 — Communication Metadata
Examples:
- sender/recipient role
- channel
- time
- delivery/result metadata where applicable

**Operational purposes:** P2, P4, P12.  
**AI Runtime:** conditional.  
**Training candidate:** conditional.  
**OPEN:** approved channels, retention, family/provider communication rules.

### DCL-23 — Communication Content
Examples:
- message/call-note content
- text entered by Elder/Caregiver/Provider

**Operational purposes:** dependent on approved channel/use.  
**AI Runtime:** possibly needed for assistant Use Cases.  
**Training candidate:** **NOT AUTOMATIC; governance-sensitive**.  
**Invariant:** `Message/Conversation ≠ Official Record` unless promoted through a valid process.  
**OPEN:** capture, consent/legal basis, retention, redaction/de-identification.

## 11. Data class map — AI

### DCL-24 — AI Runtime Input
Examples:
- prompt
- context assembled for approved use case
- referenced record versions

**Purpose:** P8.  
**Training candidate:** not automatic.  
**Must preserve:** use-case/policy version, context lineage as appropriate.  
**OPEN:** allowed classes per use case, storage/retention.

### DCL-25 — AI Output
Examples:
- summary
- suggestion
- explanation
- draft
- flagged inconsistency

**Purpose:** P8, possibly P9.  
**Training candidate:** conditional.  
**Invariant:** `AI Output ≠ Official Record`.  
**Must distinguish:** generated output vs human-approved/edited result.

### DCL-26 — Human Review of AI
Examples:
- accept
- reject
- edit
- rationale where later required

**Purpose:** P8, P9, potentially P10.  
**Training candidate:** potentially important Learning Signal but not automatically a verified label.  
**Provenance:** reviewer, original AI output, final action, time, model/policy version.

### DCL-27 — AI Model / Policy Runtime Metadata
Examples:
- Model Version
- AI Policy Version
- generation time
- evaluation/runtime context identifier

**Purpose:** P8, P9, P12.  
**Training candidate:** metadata for lineage, not necessarily model-training content.  
**Invariant:** `Model Version ≠ AI Policy Version`.

### DCL-28 — AI Evaluation Evidence
Examples:
- offline evaluation result
- reviewer evidence
- comparison evidence

**Purpose:** P9.  
**Training candidate:** only under separate policy.  
**OPEN:** metrics, thresholds, approver.

## 12. Data class map — Dataset & Learning

### DCL-29 — Training Eligibility Decision
**Meaning:** traceable result of applying an approved Training Eligibility Policy to candidate data.  
**Purpose:** P10 / Governance.  
**Must carry:** policy version, data class, eligibility result, exclusion reason where applicable, provenance references.  
**OPEN:** owner, rules, legal/consent basis.

### DCL-30 — Dataset Membership
**Meaning:** record that an eligible data item/version belongs to a Dataset Version.  
**Purpose:** P10.  
**Invariant:** automatic dataset generation must preserve traceability to eligibility and source lineage.

### DCL-31 — Dataset Version Metadata
Examples:
- dataset version
- creation time
- eligibility policy version
- preparation/curation version
- lineage summary

**Purpose:** P10, P9, P12.  
**Accepted direction:** automatic/versioned Dataset lifecycle exists from day one.  
**OPEN:** physical format/storage/trigger/orchestration.

### DCL-32 — Training / Evaluation Lineage
Examples:
- Dataset Version
- training/evaluation run reference
- Model Version
- policy/version dependencies

**Purpose:** P9, P10, P12.  
**Invariant:** Training/Evaluation success does not itself authorize Production Promotion.

## 13. Data class map — Governance & Audit

### DCL-33 — Consent / Legal-Basis Evidence
**Purpose:** demonstrate whether a given processing purpose is authorized under future approved policy.  
**Operational use:** P12 and any processing that depends on it.  
**AI Runtime/Training:** must be purpose-specific; one purpose does not imply another.  
**OPEN:** model, evidence, withdrawal effects, legal review.

### DCL-34 — Access / Authorization Decision Evidence
Examples:
- actor/context
- requested action/data
- policy version
- decision/result

**Purpose:** P12.  
**OPEN:** final Access Matrix and technical authorization mechanism.

### DCL-35 — Approval / Governance Decision Evidence
Examples:
- human approval
- rejection
- activation
- rollback
- policy change decision

**Purpose:** P12, P4.  
**Invariant:** System/AI must not impersonate human approval.

### DCL-36 — Audit / Change History
**Purpose:** reconstruct who/what/when/why/version across consequential actions and corrections.  
**Invariant:** history must not be silently overwritten.  
**OPEN:** retention, access, storage architecture.

## 14. Data class map — Workforce, Quality, Reporting & Financial

### DCL-37 — Workforce Activity / Training / Performance
**Operational purposes:** P2, P4, P5.  
**AI Runtime:** possible assistant use under approved policy.  
**Training candidate:** conditional.  
**OPEN:** performance definitions, access, employment implications.

### DCL-38 — Quality / KPI Evidence
**Operational purposes:** P4, P5, Pilot/Scale evidence.  
**AI Runtime:** analytical assistance may be allowed later.  
**Training candidate:** depends on underlying data and policy.  
**Must preserve:** metric definition/version.

### DCL-39 — Management / Aggregate Reporting Data
**Operational purposes:** P5, possibly P6.  
**Invariant:** aggregate/report access does not imply access to underlying individual record.  
**OPEN:** drill-down and employer reporting boundary.

### DCL-40 — Financial / Funding / Settlement Data
**Operational purposes:** P13 only if capability enters scope.  
**AI Runtime:** no permission inferred.  
**Training candidate:** not automatic.  
**OPEN:** whether Billing/Settlement is in Pilot scope, actor rights, data access.

## 15. Purpose separation matrix — conceptual

| Data family | Operational | AI Runtime | AI Evaluation | AI Training |
|---|---|---|---|---|
| Identity/Contact | likely required | conditional | generally not implied | not automatic |
| Case/Operational | required | conditional | conditional | conditional |
| Observation/Need | required | conditional | conditional | conditional |
| Referral/Service | required | conditional | conditional | conditional |
| Provider Result | required | conditional | conditional | conditional |
| Satisfaction | required for quality | conditional | conditional | conditional |
| Complaint/Incident | required when applicable | tightly conditional | conditional | high-governance conditional |
| Outcome/Reassessment | required for longitudinal use | conditional | important candidate | conditional + label governance |
| Communication content | channel-dependent | use-case dependent | use-case dependent | not automatic |
| AI input/output | AI-use dependent | inherent to approved use | important | not automatic |
| Human AI review | governance/evaluation | part of review flow | important | candidate only |
| Consent/Access/Audit | governance required | policy evidence | policy evidence | policy evidence |
| Aggregate reporting | reporting | optional | optional | not implied |
| Financial | scope-dependent | not implied | not implied | not automatic |

این Matrix Permission نهایی نیست.

## 16. AI Runtime boundary

برای هر AI Use Case آینده باید جداگانه مشخص شود:

- intended user
- allowed Data Classes
- minimum necessary context
- prohibited Data Classes
- whether identity is required
- whether prior history may be used
- whether Provider/Employer data may be used
- output type
- Human Review rule
- logging/provenance rule

اصل:

`Approved AI Use Case does not imply access to every operational data class.`

## 17. Training-candidate boundary

یک Data Item فقط زمانی می‌تواند Candidate Learning Data باشد که حداقل:

- Data Class آن تحت Policy مربوطه بررسی شده باشد
- Purpose برای Learning مجاز باشد
- consent/legal basis requirement رعایت شده باشد
- exclusion rule آن را حذف نکرده باشد
- provenance کافی وجود داشته باشد
- quality/verification rule رعایت شده باشد
- preparation/de-identification rule در صورت نیاز اعمال شود
- Training Eligibility Decision قابل ردیابی باشد

اصل:

`Generated in Production ≠ Eligible for Training`

## 18. Correction, supersession & history

برای داده‌ای که تصحیح یا بازبینی می‌شود باید بتوان مشخص کرد:

- original value/content
- corrected/replacement value
- actor
- reason
- time
- evidence
- whether original remains operationally valid
- downstream effect on Outcome/KPI/Dataset
- whether previous Dataset Versions are impacted semantically

### Invariant
`Correction ≠ Silent Overwrite`

Dataset تاریخی نیز نباید بدون Trace بی‌صدا بازنویسی شود.

## 19. Derived and inferred data

داده Derived باید از Source Data قابل تفکیک باشد.

Examples:
- calculated KPI
- system-generated status
- AI summary
- AI risk flag
- aggregated report
- inferred trend

هر داده Derived باید در آینده بتواند به:
- source inputs
- definition/rule/model version
- generation time
- review status where applicable

قابل ردیابی باشد.

## 20. External data

داده دریافتی از Integration خارجی:

- باید Source خارجی خود را حفظ کند
- نباید خودکار «Accepted Truth» شود
- نباید با Internal Source بی‌ردپا Merge شود
- نباید صرف دریافت، Training Eligible شود

اصل:

`External Data Received ≠ Automatically Accepted Truth`

و:

`External Data Available ≠ Training Eligible`

## 21. Data-sharing boundary

برای هر Sharing باید در آینده مشخص شود:

- recipient actor/organization
- purpose
- exact Data Classes/fields
- minimum necessary scope
- legal/consent basis
- retention/use restrictions if applicable
- provenance/audit
- onward-sharing boundary

این سند هیچ Sharing Permission نهایی صادر نمی‌کند.

## 22. Decision-trigger matrix

| Decision | Context trigger |
|---|---|
| Consent/legal basis per purpose | before real collection/use/sharing for that purpose |
| Authorized Representative data rights | before representative access |
| Data Access Matrix | before authorization design freeze |
| Provider shared fields | before Provider integration/referral data contract |
| Employer reporting boundary | before employer reporting/drill-down |
| AI Runtime data classes | before each AI use-case contract |
| Training-eligible Data Classes | before Dataset Builder implementation |
| Training exclusions/preparation | before Dataset Builder implementation |
| Training Eligibility owner | before automated eligibility execution |
| Retention/deletion | before Production data lifecycle freeze |
| Withdrawal effect | before consent/withdrawal workflow |
| Export/sharing rules | before export/share capability |
| Communication capture/retention | before production communication channel |
| Outcome label validation | before outcome-to-learning pipeline |
| External-data acceptance | before mandatory integration |
| External-data training use | before external data enters learning path |

## 23. What this map does not define

BX-005 does **not** define:
- database schema
- table/entity names
- storage technology
- encryption implementation
- RBAC/ABAC
- Access Matrix values
- legal basis values
- consent UI
- retention periods
- deletion implementation
- anonymization algorithm
- Dataset format
- training model/algorithm
- AI context-building architecture
- API fields
- integration schemas

## 24. Downstream use

این Map مبنای Exploration بعدی برای:
- AI Human-Oversight & Use-case Map
- Provider Data Boundary
- Outcome/Learning Lineage
- Consent/Access decision closure
- Training Eligibility decision closure

خواهد بود.

## 25. Next artifact

**BX-006 — AI Use-case, Human Oversight & Learning Boundary Map**

Scope:
- elder-facing and caregiver-facing AI interaction families
- allowed assistance vs consequential action
- Human Review points
- AI input/output provenance
- runtime-data vs training-data separation
- evaluation/promotion boundary
- failure/fail-safe interaction concepts
- بدون انتخاب Model، Algorithm، API یا Runtime Architecture

## 26. Current stage

- Stage: **Business**
- Data/Provenance exploration: **ACTIVE**
- Business → Technical: **NOT READY**
- Code: **NOT STARTED**
- Codex handoff: **NOT YET TRIGGERED**
