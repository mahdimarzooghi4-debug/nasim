# BX-008 — Outcome, Reassessment & Learning Lineage Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** BC-019 + DC-013 + BR-004 + BX-005 + BX-006 + BX-007
- **Purpose:** روشن‌کردن زنجیره مفهومی Observation، Accepted State، Reassessment، Outcome، Need Resolution و Learning Signal؛ بدون ساخت State Machine، Score، Instrument، Model یا Training Implementation.

> این سند Candidate Decisionها را Accepted نمی‌کند. Definition، Trigger، Cadence، Reviewer، Outcome Taxonomy، Need Resolution و Training Eligibility تا Context واقعی خود OPEN می‌مانند.

## 1. Core outcome boundaries

- `Observation ≠ Accepted State ≠ Outcome`
- `Service Delivered ≠ Outcome Achieved`
- `Service Completion ≠ Referral Closure ≠ Need Resolution ≠ Outcome`
- `Provider Result ≠ Final Elder Outcome`
- `Satisfaction ≠ Outcome`
- `Observed Change ≠ Proven Causal Effect`
- `AI Inference ≠ Observed Fact`
- `Recorded Outcome ≠ Automatically Verified Training Label`
- `Correction ≠ Silent Overwrite`

## 2. Longitudinal principle

نسیم باید بتواند وضعیت سالمند را در طول زمان مقایسه کند بدون اینکه داده جدید، گذشته را بی‌صدا بازنویسی کند.

Conceptual timeline:

`Observation(s) → Reviewed/Accepted State → Service/Referral history → Reassessment → New Observation(s) → Outcome interpretation → Continued Monitoring`

این Flow مفهومی است، نه State Machine.

## 3. Observation

### Meaning
داده/مشاهده ثبت‌شده درباره سالمند از یک Source مشخص.

### Possible sources
- Elder
- Caregiver
- Authorized Representative where valid
- Provider
- System-generated operational evidence
- External source where governed

### AI boundary
AI می‌تواند Observation موجود را summarize/compare کند، اما AI inference به‌تنهایی Observation رسمی نیست.

### Provenance
- source
- time
- context
- definition/version where relevant
- evidence
- correction history

### Trigger
قبل از Observation contract باید validity/review/correction rule بسته شود.

## 4. Accepted State

### Meaning
تصویر رسمی/پذیرفته‌شده از وضعیت سالمند در یک زمان یا Context مشخص.

### Important boundary
وجود Observation به‌تنهایی Accepted State ایجاد نمی‌کند.

### OPEN
- acceptance authority
- minimum evidence
- whether state is whole-person or domain-specific
- correction/revision rule
- effective time

### Trigger
قبل از رسمی‌شدن longitudinal state در workflow.

## 5. Baseline

### Meaning
نقطه مرجع معتبر برای مقایسه وضعیت بعدی.

Potential sources:
- initial assessment
- prior reassessment
- prior Accepted State
- need-specific baseline

### OPEN
- baseline definition
- instrument
- source validity
- refresh rule
- versioning

### Invariant
Baseline جدید نباید معنای Baseline تاریخی را بی‌صدا تغییر دهد.

## 6. Reassessment

### Purpose
بررسی مجدد وضعیت سالمند برای فهم تغییر نسبت به Baseline یا State قبلی.

Reassessment باید بتواند در آینده حداقل این سؤال‌ها را پشتیبانی کند:
- چه چیزی تغییر کرده؟
- Need هنوز وجود دارد؟
- شدت/اولویت تغییر کرده؟
- Follow-up بیشتری لازم است؟
- Referral/Service دیگری لازم است؟
- Outcome قابل مشاهده است؟
- Need قابل Resolution است؟

### Versioning
هر Reassessment باید به Definition Version خودش متصل باشد.

### OPEN
- trigger
- cadence
- instrument
- reviewer
- accepted evidence
- relation to Need closure

### Trigger
قبل از Reassessment workflow freeze.

## 7. Service / Referral separation

### Service Completion
ثبت اینکه Provider طبق Service Definition مربوطه به Completion رسیده است.

### Referral Closure
ثبت پایان Lifecycle یک Referral طبق Rule آینده.

### Need Resolution
تصمیم رسمی درباره وضعیت Need طبق Evidence و Rule مصوب.

### Outcome
تفسیر تغییر مشاهده‌شده در وضعیت سالمند.

### Invariant

`Service Completion ≠ Referral Closure ≠ Need Resolution ≠ Outcome`

هیچ‌کدام نباید از دیگری به‌طور خودکار استنتاج شود.

## 8. Provider Result

Provider Result یک Evidence Source است، نه Outcome نهایی.

Must preserve:
- Provider identity
- service/referral context
- time
- result/evidence type
- review status where applicable

### Invariant
`Provider Result ≠ Final Elder Outcome`

Provider Result ممکن است به Follow-up/Reassessment نیاز داشته باشد.

## 9. Satisfaction

رضایت سالمند باید مستقل از Outcome نگه داشته شود.

ممکن است:
- Satisfaction بالا ولی Need حل‌نشده باشد.
- Service تکمیل شده ولی Outcome مطلوب نباشد.
- Outcome بهتر شده ولی Experience ضعیف باشد.

### Invariant
`Satisfaction ≠ Outcome`

## 10. Outcome

### Meaning
تغییر مشاهده‌شده نسبت به Baseline/State قبلی، با Evidence و Provenance کافی.

### Outcome dimensions — exploratory
- physical condition
- psychological condition
- social condition
- access to services
- service continuity
- perceived quality of life
- unresolved need burden

اینها Taxonomy یا Instrument نهایی نیستند.

### OPEN
- Outcome Taxonomy
- evidence validity
- reviewer
- formal acceptance rule
- relation to Need Resolution
- correction/restatement behavior

## 11. Outcome vs Impact

- **Outcome:** تغییر مشاهده‌شده در سطح سالمند/Need/Service.
- **Impact:** اثر گسترده‌تر یا بلندمدت‌تر در سطح فرد/شبکه/جامعه.

### Invariant
یک Outcome موردی به‌تنهایی Impact کلان را اثبات نمی‌کند.

## 12. Causality boundary

اگر بعد از Service تغییری مشاهده شود، از این توالی به‌تنهایی رابطه علّی نتیجه نمی‌شود.

`Observed Change ≠ Proven Causal Effect`

اگر Causal Impact در آینده لازم باشد، Methodology مستقلی باید تصویب شود.

## 13. Need Resolution

Need Resolution یک Business Decision جدا از Service/Referral completion است.

Future rule باید بتواند مشخص کند:
- resolution criterion
- required evidence
- authority
- reassessment requirement
- role of elder feedback
- reopen rule
- recurrence handling
- chronic/ongoing need handling

### Trigger
قبل از Need closure workflow.

## 14. Reopen / Recurrence

Business آینده باید تفکیک کند:
- Reopen همان Need قبلی است یا Need جدید
- recurrence چگونه تشخیص داده می‌شود
- Baseline جدید چیست
- ارتباط با Referral/Service قبلی چگونه حفظ می‌شود

این Rule اکنون OPEN است.

## 15. Correction & historical integrity

اگر Observation، State یا Outcome اصلاح شود، باید آینده بتوان تشخیص داد:

- مقدار/محتوای قبلی
- مقدار جدید
- actor
- reason
- time
- evidence
- اثر بر Need/Outcome بعدی
- اثر بر KPI
- اثر بر Dataset lineage

### Invariant
`Correction ≠ Silent Overwrite`

Dataset تاریخی نیز نباید بدون Trace بازنویسی شود.

## 16. Provenance spine

برای Outcome معتبر باید بتوان زنجیره زیر را بازسازی کرد:

`Source Observation → Definition Version → Accepted/Reviewed State → Need → Referral/Service → Provider Result → Follow-up → Reassessment → Outcome Review → Final Outcome Record`

در صورت دخالت AI:
- Model Version
- AI Policy Version
- input/context versions
- AI output
- human review
- final human action

## 17. AI in reassessment/outcome

AI در Use Case مصوب می‌تواند:
- Observationها را خلاصه کند
- داده جدید را با سابقه مقایسه کند
- تغییرات را Flag کند
- سؤال Reassessment پیشنهاد دهد
- evidence gaps را برجسته کند

AI بدون Decision صریح نباید:
- Reassessment رسمی را نهایی کند
- Accepted State را تعیین کند
- Outcome را نهایی کند
- Need را Resolve/Close کند
- Causal Claim رسمی بسازد

## 18. Outcome to learning signal

Outcome/Reassessment می‌تواند منبع بالقوه Learning باشد چون زنجیره زیر را قابل تحلیل می‌کند:

`Need → Referral/Service → Delivery → Follow-up → Observed Outcome`

اما قبل از Learning باید مسیر Governance طی شود:

`Outcome Evidence → Training Eligibility → Quality/Verification → Label Validation → Eligible Learning Signal → Dataset Version`

### Invariant
`Recorded Outcome ≠ Automatically Verified Training Label`

## 19. Learning lineage

اگر Outcome/Reassessment وارد Dataset شود، باید حداقل این Versionها/References قابل ردیابی باشند:

- Observation source
- Assessment/Reassessment Definition Version
- Need Taxonomy Version
- Service Catalog Version
- Provider/Service context
- Outcome definition/version where applicable
- Training Eligibility Policy Version
- Preparation/Curation Version
- Dataset Version
- Model Version if AI contributed to source/review

## 20. Human review as outcome-learning evidence

Human Review روی AI-generated analysis ممکن است Learning Signal مهمی باشد، اما به‌تنهایی Ground Truth نیست.

Examples:
- AI summary accepted
- AI summary edited
- AI recommendation rejected
- AI-flagged change confirmed/not confirmed

### Invariant
`Human Review Event ≠ Automatically Verified Training Label`

Label semantics و Eligibility هنوز OPEN است.

## 21. External/provider evidence boundary

External یا Provider data:
- باید Source خود را حفظ کند.
- نباید خودکار Accepted Truth شود.
- نباید خودکار Outcome نهایی شود.
- نباید خودکار Training Eligible شود.

`External/Provider Evidence ≠ Automatically Accepted State`

## 22. Longitudinal comparison integrity

برای مقایسه دو نقطه زمانی باید Future Design بتواند تشخیص دهد:
- Definitionها یکسان بوده‌اند یا نه
- Taxonomy/Service Policy تغییر کرده یا نه
- داده تصحیح شده یا نه
- Source تغییر کرده یا نه
- AI در یکی از نقاط نقش داشته یا نه

در غیر این صورت Trend نباید بدون علامت «قابل مقایسه» فرض شود.

## 23. Decision-trigger matrix

| Decision | Trigger |
|---|---|
| Observation validity/review | before Observation contract |
| Accepted State authority | before formal longitudinal state |
| Baseline rule | before Outcome comparison logic |
| Reassessment definition | before reassessment contract |
| Reassessment trigger/cadence | before scheduler/workflow |
| Outcome Taxonomy | before formal Outcome records |
| Outcome evidence validity | before Outcome acceptance |
| Need Resolution criteria | before Need closure |
| Reopen/recurrence | before reopen workflow |
| Causal policy | before causal claims/reporting |
| AI Human Review for Outcome | before AI-assisted outcome workflow |
| Outcome Training Eligibility | before outcome-to-learning pipeline |
| Label Validation | before supervised learning from outcomes |
| Correction/restatement | before production longitudinal analytics |

## 24. Explicit non-decisions

BX-008 does **not** define:
- Outcome State Machine
- Outcome Score
- Reassessment Instrument
- Cadence
- Baseline Scale
- Need Status Enum
- Clinical Outcome Definition
- Causal Attribution Method
- Automatic Outcome Determination
- AI autonomous reassessment
- AI autonomous Need closure
- Training Label formula
- Provider ranking from Outcome
- Worker ranking from Outcome
- Dataset format
- Model/Algorithm
- Training implementation

## 25. Downstream use

این Map مبنای Exploration بعدی برای:
- KPI / Evidence Map
- Pilot measurement
- Outcome decision closure
- Training Eligibility / Label Governance
- later Technical longitudinal-state design

خواهد بود.

## 26. Next artifact

**BX-009 — KPI, Evidence & Pilot Measurement Map**

Scope:
- KPI families
- evidence sources
- metric-definition versioning
- Pilot evidence package
- AI/Dataset evidence
- Risk/Incident evidence
- Scale Gate inputs
- بدون Target/Threshold عددی یا GO/NO-GO authority

## 27. Current stage

- Stage: **Business**
- Outcome/Reassessment/Learning exploration: **ACTIVE**
- Business → Technical: **NOT READY**
- Code: **NOT STARTED**
- Codex handoff: **NOT YET TRIGGERED**
