# BX-003 — Elder Journey & Domain Interaction Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** BX-002 + BC-003 + BC-005 + BC-016 + BC-017 + DC-004 + DC-013
- **Purpose:** شکستن Journey سالمند به Interactionهای مفهومی و مشخص‌کردن Actorها، Inputs، Outputs، Handoffها، Provenance و Decision Triggerها؛ بدون ساخت State Machine، API یا Data Model.

> این سند Flow مفهومی است، نه Workflow فنی. ترتیب Interactionها الزاماً به معنی State Machine قطعی، SLA، Permission یا Automation نیست.

## 1. Canonical journey frame

Flow سطح بالا:

`Contact → Case/Profile → Monitoring → Observation → Need → Initial Assessment → Referral → Provider/Service → Follow-up → Satisfaction → Reassessment → Accepted State/Outcome → Continued Monitoring`

این Flow حلقوی است؛ Journey پس از یک Service لزوماً پایان نمی‌یابد.

## 2. Interaction I1 — Contact / Entry

### Purpose
ایجاد نخستین ارتباط عملیاتی میان سالمند و شبکه نسیم.

### Primary actors
- Elder
- Caregiver

### Possible supporting actors
- Family Contact
- Employer/Sponsor
- NASIM Operations

### Input
- وجود یک مسیر ارتباط/معرفی
- حداقل اطلاعات لازم برای آغاز تعامل

### Output
- ارتباط اولیه ثبت‌شده
- Candidate Case/Profile context

### Handoff
به تشکیل/به‌روزرسانی Case/Profile.

### Provenance needed
- چه کسی ارتباط را آغاز کرد
- زمان
- کانال/منبع معرفی
- Actor ثبت‌کننده

### OPEN / Decision trigger
Trigger زمانی ایجاد می‌شود که Onboarding/Enrollment Workflow وارد طراحی رسمی شود:
- enrollment channel
- eligibility
- consent prerequisite
- authorized representative
- duplicate handling

## 3. Interaction I2 — Case/Profile Establishment

### Purpose
ساخت یا به‌روزرسانی ظرف مفهومی اطلاعات و سابقه سالمند.

### Primary actor
- Caregiver

### Supporting actors
- Elder
- Family Contact / Authorized Representative where valid
- NASIM System

### Input
- contact context
- data supplied by valid sources

### Output
- Case/Profile context sufficient for ongoing monitoring

### Handoff
به Monitoring.

### Provenance needed
- source of each material fact
- actor
- time
- correction history

### Invariant
`Recorded data ≠ automatically verified fact`

### OPEN / Decision trigger
قبل از Case Data Contract:
- minimum profile fields
- ownership
- correction rules
- access boundaries
- consent/legal basis

## 4. Interaction I3 — Monitoring

### Purpose
پایش مستمر وضعیت سالمند و شناسایی تغییرات قابل توجه.

### Primary actor
- Caregiver

### Supporting actors
- Elder
- Family Contact where allowed
- Provider input when available
- Internal AI only in approved assistant scope

### Input
- prior Case/Profile context
- ongoing interactions
- prior observations

### Output
- new Observation candidates
- possible Need candidate
- possible follow-up item

### Provenance needed
- observation source
- observation time
- observing actor
- context/version if structured instrument exists later

### Invariant
`Monitoring ≠ Diagnosis`

### OPEN / Decision trigger
قبل از Monitoring workflow:
- cadence
- instrument
- alert/threshold behavior
- unreachable handling

## 5. Interaction I4 — Observation Capture

### Purpose
ثبت چیزی که دیده، گزارش یا اندازه‌گیری شده است بدون تبدیل خودکار آن به وضعیت رسمی یا Outcome.

### Actors
- Caregiver
- Elder
- Authorized source/Provider where allowed
- NASIM System as recorder
- Internal AI may summarize/flag but not invent Observation

### Input
- interaction/event/evidence

### Output
- Observation with provenance

### Handoff
ممکن است به Need identification، Reassessment، Incident review یا later Outcome analysis منجر شود.

### Invariants
- `Observation ≠ Accepted State`
- `AI Inference ≠ Observed Fact`

### OPEN / Decision trigger
قبل از formal Observation contract:
- observation classes
- validity
- review/acceptance path
- correction policy

## 6. Interaction I5 — Need Identification

### Purpose
بیان اینکه سالمند یک نیاز قابل پیگیری دارد.

### Primary actor
- Caregiver within approved boundary

### Supporting actors
- Elder
- valid representative
- Provider result
- approved AI assistant can flag/suggest, not finalize

### Input
- Observation(s)
- elder report
- history/context

### Output
- Need candidate/record suitable for initial assessment

### Invariant
`Need identified ≠ Service selected`

### OPEN / Decision trigger
قبل از Need Contract:
- Need Taxonomy
- severity/priority
- evidence minimum
- duplicate/recurrence behavior
- authority to finalize Need

## 7. Interaction I6 — Initial Assessment

### Purpose
فهم اولیه Need و مسیر احتمالی بعدی، بدون فرض تشخیص تخصصی.

### Primary actor
- Human actor according to future Authority policy

### Likely participant
- Caregiver

### Supporting tools
- NASIM System
- Internal AI in approved assistant mode

### Input
- Need
- relevant Observation/history
- approved Service Catalog/Need mapping when available

### Output
- assessed context
- candidate route/service family
- escalation candidate where applicable

### Invariant
`Initial Assessment ≠ Specialist Diagnosis`

### OPEN / Decision trigger
قبل از routing logic:
- assessment authority
- assessment method
- required evidence
- urgent/emergency boundary
- human review rule

## 8. Interaction I7 — Referral Preparation / Authorization

### Purpose
تبدیل Need واجد مسیر تخصصی به Referral قابل ارسال.

### Actors
- Caregiver / Supervisor / other Human Owner depending future policy
- NASIM System
- Elder/Representative where consent/choice is required

### Input
- Need
- assessment context
- Service Catalog version
- eligibility/routing policies when approved

### Output
- Referral candidate
- authorization decision
- selected service family / target class

### Invariants
- `Eligibility ≠ Provider Selection`
- `AI Suggestion ≠ Human Decision`
- `System ≠ Business Authority`

### OPEN / Decision trigger
This is a major context trigger before Referral mutation contract:
- referral authorization
- consent requirement
- service eligibility
- provider selection authority
- elder choice
- financial approval if applicable

## 9. Interaction I8 — Provider Routing / Handoff

### Purpose
انتقال Referral مجاز به Provider یا مسیر تخصصی مناسب.

### Actors
- NASIM Operations
- Provider
- Caregiver
- Human authority per future rule

### Input
- authorized Referral
- service/provider eligibility
- capacity/availability if defined

### Output
- routed Referral
- provider response/evidence

### Handoff
به Provider interaction and service delivery.

### Provenance needed
- referral version
- selected Provider
- selector/authority
- time
- policy/catalog versions

### OPEN / Decision trigger
قبل از Provider routing implementation:
- Provider Types
- onboarding/activation
- selection policy
- capacity semantics
- accept/reject/no-response
- fallback/re-route

## 10. Interaction I9 — Specialist Service Delivery

### Purpose
ارائه Service تخصصی توسط Provider مجاز.

### Primary actor
- Provider

### Supporting actors
- Elder
- Caregiver as coordinator/follow-up
- NASIM System as recorder

### Input
- Referral
- service definition
- required data within approved access boundary

### Output
- Service delivery evidence
- Provider Result
- possible Completion evidence

### Invariants
- `Caregiver ≠ Specialist Provider`
- `Provider Result ≠ Final Elder Outcome`
- `Service Completion ≠ Need Resolution`

### OPEN / Decision trigger
قبل از Service Completion contract:
- Service Definition
- Provider Type
- required evidence
- professional/legal responsibility
- SLA
- data-sharing fields

## 11. Interaction I10 — Follow-up

### Purpose
پیگیری اینکه خدمت انجام شده، مسئله‌ای ایجاد نشده و Journey بدون رهاشدگی ادامه دارد.

### Primary actor
- Caregiver

### Supporting actors
- Elder
- Provider
- Supervisor where escalation is needed

### Input
- Referral/Service context
- Provider response/result
- elder interaction

### Output
- Follow-up evidence
- unresolved issue
- re-route/escalation candidate
- satisfaction input
- reassessment candidate

### Invariant
Follow-up جزء Journey است؛ Completion به‌تنهایی Follow-up را حذف نمی‌کند.

### OPEN / Decision trigger
قبل از operational follow-up workflow:
- cadence
- owner by stage
- no-response rule
- provider failure handling
- escalation trigger

## 12. Interaction I11 — Satisfaction Capture

### Purpose
ثبت تجربه/رضایت سالمند از تعامل یا Service.

### Primary actor
- Elder

### Recorder/facilitator
- Caregiver / NASIM System according to future process

### Input
- elder feedback

### Output
- satisfaction evidence
- complaint/escalation candidate when applicable

### Invariant
`Satisfaction ≠ Outcome`

### OPEN / Decision trigger
قبل از measurement workflow:
- method
- scale
- timing
- anonymity/identity
- complaint linkage
- effect on closure/reopen

## 13. Interaction I12 — Reassessment

### Purpose
مقایسه وضعیت فعلی با Baseline/وضعیت قبلی و فهم تغییر، تداوم Need یا نیاز به اقدام بعدی.

### Actors
- Human reviewer according to future policy
- Caregiver
- Elder
- Provider evidence
- Internal AI may assist analysis under approved human-review rule

### Input
- prior state/baseline
- new observations
- service/referral history
- satisfaction/provider evidence where relevant

### Output
- reassessment evidence
- updated state candidate
- Need continuation/resolution/reopen candidate
- Outcome candidate

### Invariants
- Reassessment باید Definition Version خود را حفظ کند.
- AI cannot finalize official reassessment unless future explicit policy says otherwise.

### OPEN / Decision trigger
قبل از Reassessment contract:
- definition
- trigger
- cadence
- instrument
- reviewer
- accepted evidence

## 14. Interaction I13 — Accepted State / Outcome Review

### Purpose
تبدیل Evidence معتبر به وضعیت رسمی/Outcome قابل اتکا، بدون ادعای علّی خودکار.

### Human-governed actors
- reviewer/authority to be defined

### Input
- reassessment
- observations
- Provider Result
- satisfaction where relevant
- historical state/baseline

### Output
- Accepted State update and/or Outcome record when approved
- possible Need Resolution/Reopen decision
- learning-signal candidate

### Invariants
- `Observation ≠ Accepted State ≠ Outcome`
- `Service Completion ≠ Referral Closure ≠ Need Resolution ≠ Outcome`
- `Observed Change ≠ Proven Causal Effect`
- `Recorded Outcome ≠ Automatically Verified Training Label`

### OPEN / Decision trigger
قبل از Outcome contract:
- acceptance authority
- Outcome taxonomy
- evidence validity
- Need Resolution criteria
- causal-claim policy
- correction/restatement policy

## 15. Interaction I14 — Continued Monitoring

### Purpose
بازگشت Journey به پایش مستمر پس از Service/Outcome/Need action.

### Input
- updated Case context
- unresolved/resolved Needs
- follow-up/reassessment evidence

### Output
- ongoing monitoring
- future Observation/Need cycles

### Invariant
نسیم Journey را صرفاً با پایان یک Service خاتمه‌یافته فرض نمی‌کند.

## 16. Exception interaction classes

اینها Conceptual exception classes هستند و State نهایی نیستند:

### Provider failure
Possible triggers:
- rejection
- no response
- no capacity
- delay
- failed service

Needs future decisions:
- re-route
- escalation
- incident
- notification
- ownership

### Unreachable elder
Needs future decisions:
- attempts/channels
- family/representative involvement
- escalation
- temporary hold/closure behavior

### Complaint
Must remain distinct from:
- dissatisfaction
- incident
- emergency
- provider failure

### Escalation
Must remain distinct from:
- complaint
- incident
- emergency

### Incident
Must remain distinct from:
- risk
- alert
- emergency

### Urgent/Emergency
No 24/7, medical triage or direct emergency-service commitment is inferred from the source.

## 17. Human / System / AI interaction boundary

### Human
Final consequential business actions remain Human-governed unless a later Accepted Decision says otherwise.

### System
May:
- record
- enforce approved rules
- route according to active policy
- preserve audit/lineage

Must not:
- invent authority
- infer permission from role name
- activate Draft policy

### Internal AI
May in approved use cases:
- summarize
- explain
- flag
- suggest questions
- suggest candidate service family/path
- compare new data with history

Must not, without explicit accepted policy:
- finalize Need
- finalize emergency/severity
- authorize Referral
- select Provider finally
- close Need
- finalize Outcome
- create causal claim
- convert recorded data automatically to verified training label

## 18. Provenance spine

هر Interaction مهم باید در آینده بتواند حداقل این زنجیره را حفظ کند:

`Actor/Source → Time → Context/Definition Version → Input Evidence → Action/Observation → Review/Decision → Result → Related Policy Version`

در صورت دخالت AI:
- Model Version
- AI Policy Version
- input/context version
- AI output
- reviewer action

## 19. Decision-trigger matrix

| Interaction | Decision required before freeze |
|---|---|
| Contact/Entry | enrollment/eligibility/consent |
| Case/Profile | minimum fields/access/correction |
| Monitoring | cadence/instrument/unreachable |
| Observation | validity/review/correction |
| Need | taxonomy/severity/authority |
| Initial Assessment | authority/method/emergency boundary |
| Referral | authorization/consent/eligibility |
| Provider Routing | provider type/selection/fallback |
| Service | definition/evidence/data boundary |
| Follow-up | cadence/failure/escalation |
| Satisfaction | method/complaint linkage |
| Reassessment | trigger/cadence/reviewer |
| Outcome | evidence/authority/causal boundary |
| Continued Monitoring | case ownership/substitution |

## 20. What this map does not define

BX-003 does **not** define:
- state machine
- enum names
- API endpoints
- database entities
- permissions
- notification timings
- SLAs
- numeric thresholds
- provider ranking
- payment/billing
- exact Pilot scope
- emergency service commitment
- AI model/runtime
- Dataset implementation

## 21. Downstream use

این Map می‌تواند مبنای Exploration بعدی برای:
- Responsibility Map
- Data/Provenance Map
- AI Interaction Map
- Provider Lifecycle Map
- Outcome/Learning Lineage Map

باشد، ولی هیچ‌کدام نباید Open Business Decision را به‌صورت ضمنی ببندند.

## 22. Next artifact

**BX-004 — Actor Responsibility & Handoff Map**

Scope:
- Actor-by-Interaction responsibility mapping
- ownership vs participation vs review separation
- human/system/AI boundary
- handoff/accountability gaps
- decision triggers for Authority Matrix
- بدون RBAC، Permission enum یا Code

## 23. Current stage

- Stage: **Business**
- Journey exploration baseline: **ACTIVE**
- Business → Technical: **NOT READY**
- Code: **NOT STARTED**
- Codex handoff: **NOT YET TRIGGERED**
