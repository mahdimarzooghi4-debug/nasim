# BX-007 — Provider Lifecycle, Referral Response & Service Evidence Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** BC-002 + BC-003 + BC-008 + BC-019 + BR-004 + BX-003 + BX-004 + BX-005 + BX-006
- **Purpose:** روشن‌کردن Lifecycle مفهومی Provider، Referral Handoff/Response، Service Evidence، Failure/Re-route و Data-sharing Boundary؛ بدون ساخت Provider Schema، SLA عددی، Ranking Algorithm، Settlement Formula، API یا State Machine.

> این سند Candidate Decisionها را Accepted نمی‌کند. Provider Types، Qualification، Activation، Selection، SLA، Suspension و Settlement تا Context واقعی خود OPEN می‌مانند.

## 1. Core provider boundaries

- `Caregiver ≠ Specialist Provider`
- `NASIM Operator ≠ Direct Provider of every specialist service`
- `Provider Eligibility ≠ Provider Selection`
- `Provider Access ≠ Full Elder Record Access`
- `Provider Result ≠ Final Elder Outcome`
- `Service Completion ≠ Need Resolution`
- `Referral Closure ≠ Need Resolution`
- `Provider Data ≠ Automatically Training Eligible`
- `Provider Ranking ≠ Automatic Selection Authority`

## 2. Provider lifecycle frame

Conceptual lifecycle:

`Candidate → Qualification Review → Contracted/Eligible → Activated → Available for Referral → Referral Response → Service Delivery → Evidence/Result → Quality Monitoring → Suspension/End where applicable`

این فقط Lifecycle مفهومی است و State Machine نهایی محسوب نمی‌شود.

## 3. Provider Candidate

### Meaning
یک شخص/سازمان بالقوه برای ورود به شبکه تخصصی نسیم.

### Can be explored now
- identity
- service domain
- geographic scope
- contact/operational information
- candidate qualification evidence

### Must remain OPEN
- exact Provider Types
- mandatory documents
- licensing criteria
- contract form
- eligibility thresholds

### Trigger
قبل از Provider Registry schema یا onboarding workflow.

## 4. Qualification Review

### Purpose
بررسی اینکه Provider از نظر Ruleهای مصوب آینده اصولاً واجد شرایط همکاری هست یا نه.

### Possible evidence
- credentials
- service scope
- legal/contractual documents
- quality prerequisites
- geographic/service capability

### Invariant
`Qualification ≠ Activation`

### OPEN
- reviewer
- criteria
- review cadence
- expiration/renewal
- evidence validity

## 5. Activation

### Meaning
اجازه ورود Provider به Scope عملیاتی مشخص پس از Qualification/Contract/Governance لازم.

### Invariant
`Registered Provider ≠ Activated Provider`

### OPEN
- activation authority
- activation scope
- effective date
- geography/service scope
- temporary suspension
- reactivation

### Trigger
قبل از Provider Activation workflow.

## 6. Service-to-Provider eligibility

برای Referral معتبر، Provider باید با Service/Scope مربوط سازگار باشد.

Conceptual inputs:
- Service Catalog version
- Service Item / Family
- geography
- Provider activation status
- qualification scope
- capacity where applicable

### Invariant
`Eligible Provider Set ≠ Selected Provider`

### OPEN
- mapping rule
- geography rule
- professional scope
- capacity rule
- exception/override

## 7. Provider selection boundary

Provider Selection یک Business Decision جدا از Eligibility است.

ممکن است آینده شامل:
- elder choice
- human selection
- operational coordination
- candidate recommendation
- AI-assisted suggestion

باشد.

### AI boundary
AI ممکن است در آینده Candidate Provider یا Candidate Route پیشنهاد دهد، اما Selection نهایی تا Decision صریح Human-governed باقی می‌ماند.

### Trigger
قبل از Provider Matching/Selection workflow.

## 8. Referral handoff to Provider

Referral Handoff آینده باید بتواند حداقل این Context را منتقل کند:

- Referral identifier/context
- related Need
- Service definition/version
- minimum necessary elder context
- approved shared data
- authorization/consent evidence where required
- requested service
- timing/context needed for service

### Data rule
فقط Data Classهای موردنیاز Purpose خدمت باید منتقل شوند.

`Referral Handoff ≠ Full Case Sharing`

## 9. Provider response model — conceptual

Provider Response ممکن است در آینده نیاز داشته باشد مفاهیمی مانند:

- can accept
- cannot accept
- insufficient information
- no capacity
- scheduling needed
- service not in scope

را پوشش دهد.

اینها فقط Interaction Class هستند، نه State/Enum نهایی.

### OPEN
- exact response semantics
- response deadline
- who may respond
- reason taxonomy
- whether response is binding

### Trigger
قبل از Provider response contract.

## 10. Capacity boundary

نسیم احتمالاً باید بتواند Capacity را برای جلوگیری از Referral غیرقابل انجام در نظر بگیرد، اما Unit و Rule هنوز OPEN است.

Candidate dimensions:
- service-specific capacity
- geography
- availability window
- temporary pause
- operational load

### Not decided
- daily/weekly/monthly limits
- capacity score
- hard threshold
- auto-routing by capacity

## 11. Service delivery

Provider در دامنه مصوب Service تخصصی را ارائه می‌دهد.

### Inputs
- valid Referral
- applicable Service definition
- minimum necessary data
- Provider scope/activation

### Outputs
- Service Delivery Evidence
- Provider Result
- exception/failure information

### Invariant
`Service Delivery ≠ Outcome Achievement`

## 12. Service evidence

برای هر Service آینده باید مشخص شود چه چیزی Completion Evidence معتبر است.

Candidate evidence dimensions:
- service performed
- date/time
- actor/provider
- service definition/version
- evidence type
- exception reason
- verification/review status

### OPEN
- exact evidence type
- who records
- who verifies
- whether elder confirmation is required
- minimum evidence

### Trigger
قبل از Service Completion contract.

## 13. Provider Result

Provider Result باید به‌عنوان منبع مستقل با Provenance خود ثبت شود.

Must preserve:
- Provider identity
- service/referral context
- time
- source actor
- result/evidence class
- review status where applicable

### Invariant
`Provider Result ≠ Final Elder Outcome`

Outcome ممکن است به Follow-up/Reassessment مستقل نیاز داشته باشد.

## 14. Referral closure boundary

Referral Closure نباید از Service Completion یا Provider Result به‌صورت خودکار استنتاج شود.

Need to decide later:
- closure criteria
- who closes
- incomplete service handling
- failed service handling
- reopen/re-referral
- elder feedback requirement
- outstanding obligations

### Invariant
`Service Completion ≠ Referral Closure ≠ Need Resolution ≠ Outcome`

## 15. Failure and exception classes

Conceptual failure classes:
- rejection
- no response
- no capacity
- delay
- unavailable Provider
- incomplete service
- failed delivery
- quality issue
- data/access blocker
- contract/activation issue

اینها State نهایی نیستند.

## 16. Re-route / fallback

در Failure باید امکان Conceptual Re-route/Fallback بررسی شود.

Potential actions:
- another eligible Provider
- human review
- escalation
- temporary hold
- incident/quality review where justified

### OPEN
- re-route authority
- automatic vs human
- elder notification
- escalation trigger
- fallback ordering
- maximum attempts

### Trigger
قبل از Provider failure workflow.

## 17. Quality monitoring

Provider quality future framework may consider:
- service quality
- response behavior
- completion evidence
- complaints/incidents
- elder satisfaction
- repeat/rework
- data completeness
- audit findings

هیچ Score، Weight یا Threshold فعلاً تصویب نشده است.

### Invariant
`Quality Evidence ≠ Automatic Suspension Decision`

## 18. Suspension / termination boundary

Provider Suspension/End نیازمند Decision Governance مستقل است.

OPEN:
- triggering conditions
- authority
- immediate vs reviewed action
- open referral handling
- elder notification
- re-routing
- reactivation
- contract implications

### Trigger
قبل از Provider governance commands.

## 19. Complaint / incident linkage

Provider-related Complaint، Incident، Quality Issue و Service Failure نباید یکی فرض شوند.

- Complaint = grievance/issue raised through complaint process
- Incident = actual event requiring incident handling
- Quality Issue = evidence of quality concern
- Service Failure = failure to deliver/complete as expected

ارتباط میان آنها Policy آینده می‌خواهد.

## 20. Provider data-sharing boundary

Provider فقط باید داده‌ای را ببیند که برای Service Purpose مصوب لازم است.

Future sharing contract must define:
- exact Data Classes/fields
- purpose
- recipient/provider scope
- access duration
- consent/legal basis where required
- onward-sharing restriction
- audit/provenance
- correction/update behavior

### Invariant
`Provider Access ≠ Full Elder Record Access`

## 21. Provider-generated data and learning

Provider-generated data ممکن است برای Operations، Outcome، Quality و Learning ارزش داشته باشد؛ ولی:

- Source Provider باید حفظ شود.
- Provider Result خودکار Accepted State نیست.
- Provider data خودکار Training Eligible نیست.
- AI Summary از Provider Result نباید جای Source Record را بگیرد.

`Provider Data Generated ≠ Training Eligible`

## 22. Financial boundary

Referral/Service lifecycle به‌تنهایی هیچ Pricing/Billing/Settlement Rule ایجاد نمی‌کند.

OPEN:
- tariff
- reimbursement
- invoice
- commission/fee
- settlement cycle
- payment approval
- penalty/credit

### Invariant
`Service Completion ≠ Automatic Billing/Settlement`

## 23. Provider registry conceptual needs

Provider Registry در آینده احتمالاً باید بتواند این مفاهیم را نگه دارد:
- identity
- type/domain
- service scope
- geography
- qualification evidence
- activation scope/status
- contract reference
- capacity context
- operational contact
- quality evidence
- suspension/end history

این فهرست Business need است، نه Database Schema.

## 24. Provenance spine

برای Provider-related interactions باید آینده بتوان این Lineage را بازسازی کرد:

`Need → Referral → Service Definition Version → Provider Eligibility Context → Selection Decision → Provider Response → Service Evidence → Provider Result → Follow-up/Reassessment`

در صورت دخالت AI:
- Model Version
- AI Policy Version
- AI recommendation
- human reviewer/selector
- final human decision

## 25. Decision-trigger matrix

| Decision | Trigger |
|---|---|
| Provider Types | before Provider Registry freeze |
| Qualification criteria | before onboarding workflow |
| Activation authority | before activation command/workflow |
| Service-to-Provider mapping | before referral routing |
| Provider selection authority | before matching/selection workflow |
| Elder choice rule | before provider-selection UX |
| Response semantics | before Provider response contract |
| Capacity model | before capacity-aware routing |
| Completion Evidence | before Service Completion contract |
| Re-route/fallback | before provider failure workflow |
| Suspension authority | before governance commands |
| Data-sharing fields | before provider integration |
| Quality/KPI rules | before automated monitoring/scoring |
| SLA values | only when operational commitment requires them |
| Settlement model | before financial capability |

## 26. Explicit non-decisions

BX-007 does **not** define:
- Provider schema
- Provider type list
- licensing criteria
- onboarding state machine
- activation state machine
- referral state machine
- ranking/scoring formula
- auto-routing
- SLA number
- capacity number
- quality threshold
- suspension threshold
- data field list
- payment/billing/settlement
- API/integration protocol
- AI autonomous provider selection

## 27. Downstream use

این Map مبنای Exploration بعدی برای:
- Outcome / Reassessment / Learning Lineage
- KPI / Evidence Map
- Provider decision closure
- Data-sharing closure
- later Technical Provider design

خواهد بود.

## 28. Next artifact

**BX-008 — Outcome, Reassessment & Learning Lineage Map**

Scope:
- Observation → Accepted State → Reassessment → Outcome
- Service Completion / Referral Closure / Need Resolution separation
- evidence/provenance
- causal boundary
- Outcome-to-Learning signal
- correction/history
- decision triggers
- بدون Outcome State Machine، Score، Instrument، Model یا Training implementation

## 29. Current stage

- Stage: **Business**
- Provider lifecycle exploration: **ACTIVE**
- Business → Technical: **NOT READY**
- Code: **NOT STARTED**
- Codex handoff: **NOT YET TRIGGERED**
