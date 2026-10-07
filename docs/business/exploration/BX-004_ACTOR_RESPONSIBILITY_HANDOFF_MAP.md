# BX-004 — Actor Responsibility & Handoff Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** BX-003 + BC-005 + BC-013 + BC-016 + BR-004
- **Purpose:** روشن‌کردن Responsibility، Participation، Review و Handoff میان Actorهای نسیم، بدون ساخت RBAC، Permission Enum، Authority Matrix نهایی یا Workflow فنی.

> این سند «مسئولیت مفهومی» را از «اختیار نهایی» جدا می‌کند. هرجا Final Authority در منبع تعیین نشده، عمداً OPEN باقی می‌ماند.

## 1. Core rule

`Responsibility ≠ Authority ≠ Permission`

و:

`Participation ≠ Approval`

و:

`System Execution ≠ Business Decision`

و:

`AI Assistance ≠ Human Accountability`

## 2. Responsibility labels

برای این Map از این برچسب‌ها استفاده می‌شود:

- **PRIMARY PARTICIPANT** — Actor اصلی در انجام Interaction.
- **CONTRIBUTOR** — داده، Evidence یا همکاری فراهم می‌کند.
- **COORDINATOR** — هماهنگی و پیگیری جریان را انجام می‌دهد.
- **RECORDER** — ثبت یا نگهداری اطلاعات را انجام می‌دهد.
- **REVIEWER CANDIDATE** — ممکن است طبق Policy آینده نقش Review داشته باشد؛ هنوز Authority نهایی نیست.
- **FINAL AUTHORITY: OPEN** — تصمیم نهایی هنوز بسته نشده است.
- **NOT AUTHORITY BY DEFAULT** — عنوان/نقش به‌تنهایی اختیار نهایی نمی‌دهد.

## 3. Actor boundaries

### Elder
- محور دریافت خدمت و منبع مهم تجربه/بازخورد.
- ممکن است Contributor اصلی برای Need، Satisfaction و Reassessment باشد.
- حق‌های نهایی انتخاب، رد، لغو یا رضایت باید جداگانه تعیین شوند.
- **Not equivalent to:** Payor، Employer، Authorized Representative.

### Family Contact
- ممکن است Contributor در ارتباط و اطلاعات باشد.
- تا Decision صریح، نماینده مجاز نیست.
- **NOT AUTHORITY BY DEFAULT.**

### Authorized Representative
- فقط در صورت Rule معتبر و Scope مشخص می‌تواند از طرف سالمند اقدام کند.
- تعریف، احراز، Scope و Revocation هنوز OPEN است.

### Caregiver
- PRIMARY PARTICIPANT در ارتباط، پایش، Need capture، coordination و Follow-up.
- Recorder/Coordinator در بسیاری از Interactionهای Journey.
- از این نقش نباید Diagnosis، Financial Approval، Provider Selection نهایی یا Permission اضافی استنتاج شود.

### Supervisor hierarchy
- منبع وجود مسیر سرپرستی را پشتیبانی می‌کند.
- می‌تواند برای Review/Escalation/Reassignment در آینده Candidate باشد.
- Authority هر سطح هنوز OPEN است.

### NASIM Operations
- مسئول راهبری عملیات شبکه و هماهنگی کلان.
- می‌تواند Owner عملیاتی برخی Handoffها باشد، اما Decision Rights جزئی باید جداگانه تعیین شوند.

### Provider
- PRIMARY PARTICIPANT در Service Delivery تخصصی.
- Contributor برای Service Result و Completion Evidence.
- Provider Result به‌تنهایی Outcome نهایی سالمند نیست.

### Employer / Sponsor
- نقش کلان در هدف‌گذاری، تأمین مالی توافق‌شده و نظارت.
- دسترسی موردی به Case یا Authority عملیاتی از این نقش استنتاج نمی‌شود.

### Quality / Audit
- Conceptual reviewer function برای کیفیت، Evidence و Audit.
- Actor/organization نهایی، Scope و Decision Rights هنوز OPEN است.

### NASIM System
- RECORDER / rule executor / audit carrier.
- می‌تواند Rule مصوب را enforce کند.
- **NOT BUSINESS AUTHORITY.**

### Internal AI
- assistant برای سالمند/سالمندیار در Use Case مصوب.
- می‌تواند summarize / explain / flag / suggest کند.
- **NOT FINAL AUTHORITY.**
- خروجی AI تا مسیر معتبر انسانی/Policy رسمی، Official Record نیست.

## 4. Actor-by-interaction map

| Interaction | Primary participant | Contributors / support | Coordination / recording | Final authority |
|---|---|---|---|---|
| Contact / Entry | Elder + Caregiver | Family/Employer where relevant | Caregiver / System | OPEN for enrollment |
| Case/Profile establishment | Caregiver | Elder, valid sources | Caregiver / System | OPEN for acceptance/access |
| Monitoring | Caregiver | Elder, family where allowed, Provider input | Caregiver / System | No implied final authority |
| Observation capture | Human/source actor | Elder/Provider/valid source | System records provenance | OPEN for official acceptance |
| Need identification | Caregiver within boundary | Elder, valid representative, evidence | Caregiver / System | OPEN for final Need authority |
| Initial assessment | Human actor TBD | Caregiver, Elder, evidence, AI assist | System | OPEN |
| Referral preparation | Human operator TBD | Caregiver, Elder/Representative, AI assist | System | OPEN |
| Referral authorization | Human authority TBD | Caregiver/Supervisor/Operations | System executes | **OPEN — must be explicit** |
| Provider routing | Operations/Human owner TBD | Caregiver, Provider | System | Provider selection authority OPEN |
| Specialist service delivery | Provider | Elder | Provider/System evidence | Provider within professional scope |
| Follow-up | Caregiver | Elder, Provider, Supervisor if needed | Caregiver/System | OPEN for escalation/closure |
| Satisfaction capture | Elder | Caregiver/System facilitator | System | Elder is feedback source, not closure authority by default |
| Reassessment | Human reviewer TBD | Caregiver, Elder, Provider evidence, AI assist | System | **OPEN** |
| Accepted State / Outcome review | Human reviewer/authority TBD | evidence sources + AI assist | System | **OPEN — consequential human authority required** |
| Continued monitoring | Caregiver | Elder, relevant actors | Caregiver/System | Case ownership OPEN |

## 5. Handoff H1 — Entry to Case/Profile

### From
Elder / introduction source

### To
Caregiver / NASIM operations context

### Must carry
- source of introduction
- minimum contact context
- time
- consent/authorization status when later required

### Accountability gap
هنوز مشخص نیست چه کسی Enrollment را نهایی می‌کند.

### Trigger
قبل از Enrollment Workflow freeze.

## 6. Handoff H2 — Case/Profile to Monitoring

### From
Case/Profile establishment

### To
Assigned/operational caregiver function

### Must carry
- current profile context
- known Needs/risks where valid
- data provenance
- open actions

### Accountability gap
Primary ownership / substitution model هنوز OPEN است.

### Trigger
قبل از Case Ownership / Assignment design.

## 7. Handoff H3 — Monitoring to Need

### From
Caregiver monitoring / observations

### To
Need handling

### Must carry
- observation source
- time
- evidence/context
- elder input where available

### Accountability gap
چه کسی Need را رسمی/نهایی می‌کند هنوز OPEN است.

### Trigger
قبل از Need lifecycle contract.

## 8. Handoff H4 — Need to Initial Assessment

### From
Need context

### To
Human assessment function

### Must carry
- Need definition/version when available
- supporting observations
- relevant history
- unresolved uncertainty

### Accountability gap
Assessment authority و روش هنوز OPEN.

### Trigger
قبل از routing/triage logic.

## 9. Handoff H5 — Assessment to Referral Authorization

### From
Assessment / candidate service path

### To
Human referral authority

### Must carry
- Need
- evidence
- candidate Service Family
- consent status where required
- eligibility result where later applicable

### Accountability gap
Referral authorization owner مشخص نشده.

### Trigger
قبل از Referral mutation contract.

## 10. Handoff H6 — Authorized Referral to Provider

### From
NASIM operational flow

### To
Provider

### Must carry
فقط داده‌ای که طبق Policy آینده برای اجرای Service لازم و مجاز است.

### Must preserve
- Referral lineage
- Service Catalog version
- Provider selection provenance
- data-sharing basis

### Accountability gap
Provider selection، data-sharing fields و response semantics هنوز OPEN.

### Trigger
قبل از Provider integration/routing.

## 11. Handoff H7 — Provider to Follow-up

### From
Provider

### To
Caregiver / NASIM operations

### Must carry
- Provider Result
- Completion Evidence if applicable
- exceptions/failure information

### Invariant
`Provider Result ≠ Final Elder Outcome`

### Accountability gap
no-response / failure / reroute authority هنوز OPEN.

### Trigger
قبل از Provider response workflow.

## 12. Handoff H8 — Follow-up to Reassessment

### From
Caregiver follow-up

### To
Reassessment function

### Must carry
- service/referral history
- elder feedback
- unresolved Need context
- relevant new observations

### Accountability gap
Reassessment trigger، cadence و reviewer هنوز OPEN.

### Trigger
قبل از Reassessment workflow.

## 13. Handoff H9 — Reassessment to Outcome / Accepted State

### From
Reassessment evidence

### To
Human-governed review

### Must carry
- definition version
- baseline/previous state
- evidence/provenance
- AI analysis separately identified if used

### Invariants
- `Observation ≠ Accepted State ≠ Outcome`
- `AI Inference ≠ Observed Fact`
- `Observed Change ≠ Proven Causal Effect`

### Accountability gap
Outcome authority / Need Resolution authority هنوز OPEN.

### Trigger
قبل از Outcome contract.

## 14. Handoff H10 — Outcome / Accepted State to Learning

### From
Approved operational/Outcome evidence

### To
Training Eligibility / Dataset path

### Must carry
- source/evidence lineage
- definition versions
- correction history
- eligibility-policy version

### Invariant
`Recorded Outcome ≠ Automatically Verified Training Label`

### Accountability gap
Training Eligibility owner و Label validation authority هنوز OPEN.

### Trigger
قبل از Dataset Builder implementation.

## 15. Human/System/AI accountability rule

### Human
برای Actionهای consequential، Final accountability باید به Actor انسانی/حاکمیتی مصوب قابل ردیابی باشد مگر Decision صریح دیگری در آینده ثبت شود.

### System
وظیفه System:
- اجرای Rule فعال
- ثبت action
- حفظ lineage
- جلوگیری از اجرای Draft/invalid Policy

System نباید:
- authority ایجاد کند
- role را permission فرض کند
- تصمیم انسانی را جعل کند

### AI
AI می‌تواند در Use Case مصوب:
- اطلاعات را خلاصه کند
- inconsistency را flag کند
- گزینه/سؤال/مسیر candidate پیشنهاد دهد
- history را مقایسه کند

AI نباید بدون Decision صریح:
- Referral را authorize کند
- Provider را نهایی انتخاب کند
- Incident/Emergency را نهایی کند
- Need را resolve کند
- Outcome را رسمی کند
- Policy را approve/activate کند
- Training Eligibility را تغییر دهد
- Model خود را Production promote کند

## 16. Accountability gaps register

این Gapها در حال حاضر عمداً OPEN هستند:

- Enrollment authority
- Case assignment authority
- Reassignment authority
- Need finalization authority
- Assessment authority
- Referral authorization
- Provider selection
- Provider activation/suspension
- Complaint closure
- Escalation ownership
- Incident severity/closure
- Risk Acceptance
- Emergency operational authority
- Need Resolution/Reopen
- Reassessment reviewer
- Outcome reviewer
- Training Eligibility owner
- Label validation authority
- AI Evaluation approver
- Model Promotion/Rollback authority
- Scale Gate approver
- Policy Production Activation authority
- Financial exception authority

## 17. Authority trigger matrix

| Authority decision | Trigger |
|---|---|
| Enrollment authority | before enrollment workflow |
| Case assignment/reassignment | before case ownership workflow |
| Need finalization | before Need lifecycle freeze |
| Referral authorization | before referral mutation API/contract |
| Provider selection | before provider matching/routing |
| Provider activation/suspension | before Provider Registry workflow |
| Incident/Risk authority | before Incident/Risk command model |
| Emergency authority | before safety-critical workflow |
| Need Resolution/Reopen | before Need closure workflow |
| Reassessment reviewer | before reassessment contract |
| Outcome reviewer | before official Outcome path |
| Training Eligibility owner | before Dataset Builder |
| Model Promotion/Rollback | before Production model lifecycle |
| Scale Gate approver | before Pilot exit |
| Policy activation authority | before Policy Registry activation |
| Financial approval | before financial capability |

## 18. Handoff audit requirement

هر Handoff مهم در آینده باید بتواند حداقل این موارد را Trace کند:

- from actor/function
- to actor/function
- subject/context
- time
- input evidence
- decision/policy version
- accepted/rejected/edited where applicable
- unresolved obligations
- next owner
- AI involvement, if any

این requirement مفهومی است و Audit schema فنی را تعیین نمی‌کند.

## 19. What this map does not define

BX-004 هیچ‌کدام از موارد زیر را نهایی نمی‌کند:
- RBAC / ABAC
- permission names
- database ownership
- user groups
- approval workflow
- state machine
- delegation rule
- supervisor authority
- geographic hierarchy permissions
- organization tenancy
- SLA
- numeric workload limits
- automatic assignment
- AI authority
- emergency authority
- financial authority

## 20. Downstream use

این Map مبنای Exploration بعدی برای:
- Data & Provenance Map
- AI Human-Oversight Map
- Provider Lifecycle Map
- Outcome/Learning Lineage
- later Authority Matrix closure

خواهد بود.

## 21. Next artifact

**BX-005 — Data Class, Provenance & Purpose-of-Use Map**

Scope:
- data classes generated across Journey
- source/provenance
- operational purpose
- AI runtime boundary
- training-candidate boundary
- correction/history expectations
- decision triggers for Consent, Access and Training Eligibility
- بدون Database Schema، retention period یا final Access Matrix

## 22. Current stage

- Stage: **Business**
- Responsibility/Handoff exploration: **ACTIVE**
- Business → Technical: **NOT READY**
- Code: **NOT STARTED**
- Codex handoff: **NOT YET TRIGGERED**
