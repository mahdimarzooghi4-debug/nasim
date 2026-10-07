# BX-002 — Canonical Domain Vocabulary & Concept Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** Business Concept Baseline + BC-002 + BC-003 + BC-005 + BC-006 + BC-007 + BC-008 + BC-012 + BC-018 + BC-019 + BC-024 + D-0004 + D-0005 + D-0118 + BX-001
- **Purpose:** یکسان‌سازی زبان مفهومی نسیم برای ادامه تحلیل Business، بدون ساخت Data Model، API، Permission Model یا State Machine.

> «Canonical» در این سند یعنی واژگان مرجع برای Exploration و جلوگیری از اختلاط مفاهیم. این سند Candidate Decisionهای D-0006…D-0117 را Accepted نمی‌کند و Policy باز را نمی‌بندد.

## 1. Vocabulary confidence labels

هر مفهوم یکی از این وضعیت‌های معنایی را دارد:

- **ACCEPTED DIRECTION:** مستقیماً بر تصمیم Accepted متکی است.
- **SOURCE-SUPPORTED:** در Concept/Baseline یا Business Contractها پشتوانه روشن دارد.
- **BOUNDED EXPLORATION:** تفکیک مفهومی لازم برای جلوگیری از خطاست، اما Definition/Policy نهایی آن هنوز OPEN است.
- **OPEN:** تا Context Trigger نباید مقدار، Authority، State یا Rule نهایی برای آن ساخته شود.

## 2. People and organizational actors

### Elder / سالمند
**Meaning:** فردی که خدمات نسیم حول نیاز، تجربه، وضعیت و پیگیری او سازمان‌دهی می‌شود.  
**Confidence:** SOURCE-SUPPORTED.  
**Not equivalent to:** Payor، Employer، Family Contact، Authorized Representative.

### Family Contact / خانواده یا همراه
**Meaning:** فرد خانواده/همراهی که ممکن است در ارتباط با سالمندیار حضور داشته باشد.  
**Confidence:** SOURCE-SUPPORTED.  
**Invariant:** `Family Contact ≠ Automatically Authorized Representative`.  
**OPEN:** دسترسی، رضایت، اعلان، حق تصمیم‌گیری.

### Authorized Representative / نماینده مجاز
**Meaning:** شخصی که در صورت وجود Rule/مبنای مصوب، می‌تواند در Scope معین از طرف سالمند اقدام کند.  
**Confidence:** BOUNDED EXPLORATION.  
**OPEN:** eligibility، verification، scope، revocation، consent authority.

### Caregiver / سالمندیار
**Meaning:** نخستین حلقه ارتباطی محله‌محور؛ مسئول ارتباط، پایش، ثبت/گزارش Need، هماهنگی، Referral و Follow-up در مرزهای مصوب.  
**Confidence:** SOURCE-SUPPORTED.  
**Invariant:** `Caregiver ≠ Specialist Provider`.  
**Invariant:** عنوان سالمندیار به‌تنهایی مجوز تخصصی یا Permission ایجاد نمی‌کند.

### Supervisor / سطوح سرپرستی
**Meaning:** سطوح رشد و مدیریت شبکه سالمندیاران از سالمندیار ارشد تا سطوح منطقه/شهرستان/استان.  
**Confidence:** SOURCE-SUPPORTED.  
**OPEN:** Authority و Permission هر سطح.

### NASIM Operator / اپراتور نسیم
**Meaning:** موجودیت مسئول طراحی مدل اجرایی، راهبری شبکه، کیفیت، فناوری، استانداردها، آموزش و مدیریت شرکا.  
**Confidence:** SOURCE-SUPPORTED.  
**Invariant:** `Network Operator ≠ Direct Provider of every specialist service`.

### Employer / Sponsor / کارفرما
**Meaning:** طرفی که در سطح کلان نیاز/هدف را تعریف می‌کند، تأمین مالی توافق‌شده دارد و بر تعهدات نظارت می‌کند.  
**Confidence:** SOURCE-SUPPORTED.  
**Invariant:** `Employer ≠ NASIM Operator`.  
**OPEN:** دسترسی فردی، دخالت عملیاتی، Payor scope.

### Provider / ارائه‌دهنده تخصصی
**Meaning:** Actor جداگانه‌ای که خدمت تخصصی را در شبکه ارائه می‌کند.  
**Confidence:** SOURCE-SUPPORTED.  
**OPEN:** Type، qualification، activation، capacity، SLA، settlement، data access.

### NASIM System / سامانه نسیم
**Meaning:** سامانه ثبت، مدیریت، پایش، ارجاع، گزارش و پشتیبانی از تصمیم‌سازی بر اساس Ruleهای مصوب.  
**Confidence:** SOURCE-SUPPORTED.  
**Invariant:** `System ≠ Independent Business Authority`.

### Internal AI / هوش مصنوعی داخلی
**Meaning:** دستیار داخلی نسیم در کنار سالمند و سالمندیار، با حضور از روز اول بهره‌برداری عملیاتی.  
**Confidence:** ACCEPTED DIRECTION — D-0004/D-0005.  
**Invariant:** `AI Suggestion ≠ Human Decision`.  
**Invariant:** `AI Output ≠ Official Record` تا زمانی که مسیر انسانی/مصوب آن را رسمی کند.  
**OPEN:** final use cases، model، algorithm، runtime، review rules، promotion authority.

## 3. Elder journey concepts

### Case / Profile / پرونده
**Meaning:** ظرف مفهومی اطلاعات و سابقه لازم برای ادامه ارتباط و خدمت به سالمند.  
**Confidence:** SOURCE-SUPPORTED.  
**OPEN:** حداقل fields، lifecycle، ownership، closure semantics.

### Monitoring / پایش
**Meaning:** پیگیری مستمر وضعیت سالمند، با توجه به تغییرات جسمی، روانی و اجتماعی ذکرشده در منبع.  
**Confidence:** SOURCE-SUPPORTED.  
**OPEN:** cadence، instrument، threshold.

### Observation / مشاهده
**Meaning:** چیزی که از تعامل، پایش، Provider، System یا منبع دیگر ثبت می‌شود و هنوز لزوماً وضعیت رسمی پذیرفته‌شده نیست.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Observation ≠ Accepted State`.

### Need / نیاز
**Meaning:** نیاز شناسایی‌شده سالمند که می‌تواند ثبت، ارزیابی اولیه و در صورت لزوم به مسیر خدمت/Referral هدایت شود.  
**Confidence:** SOURCE-SUPPORTED.  
**OPEN:** taxonomy، severity، priority، evidence، lifecycle.

### Initial Assessment / ارزیابی اولیه
**Meaning:** بررسی اولیه برای فهم Need و مسیر احتمالی بعدی؛ نه لزوماً ارزیابی تخصصی/بالینی.  
**Confidence:** SOURCE-SUPPORTED AT HIGH LEVEL.  
**Invariant:** `Initial Assessment ≠ Specialist Diagnosis`.  
**OPEN:** actor authority، method، evidence.

### Follow-up / پیگیری
**Meaning:** پیگیری ارائه خدمت و تجربه/رضایت سالمند پس از Referral یا Service.  
**Confidence:** SOURCE-SUPPORTED.  
**OPEN:** cadence، owner by stage، escalation behavior.

### Satisfaction / رضایت
**Meaning:** بازخورد سالمند درباره تجربه یا خدمت.  
**Confidence:** SOURCE-SUPPORTED.  
**Invariant:** `Satisfaction ≠ Outcome`.  
**OPEN:** scale، timing، measurement method، effect on workflow.

## 4. Service concepts

### Service Family / خانواده خدمت
**Meaning:** دسته سطح‌بالای خدمات مانند Health یا Welfare/Complementary و زیرخانواده‌های ذکرشده در Concept.  
**Confidence:** SOURCE-SUPPORTED.  
**Invariant:** `Service Family ≠ Active Pilot Service Item`.

### Service Item / خدمت اجرایی
**Meaning:** خدمت تعریف‌شده‌ای که برای اجرا/ارجاع به Business Definition، Preconditions، Provider boundary، Completion Evidence و سایر Policyهای لازم نیاز دارد.  
**Confidence:** BOUNDED EXPLORATION.  
**OPEN:** Pilot activation و Definition نهایی.

### Service Catalog / کاتالوگ خدمات
**Meaning:** مجموعه Versioned از Service Itemهای مجاز و Definitionهای آنها برای Scope مشخص.  
**Confidence:** BOUNDED EXPLORATION, strongly required by BC-002/BC-018/BC-024.  
**Invariant:** Catalog جدید نباید معنای Referral تاریخی را بی‌صدا بازنویسی کند.

### Need Taxonomy
**Meaning:** طبقه‌بندی Versioned برای بیان انواع Need.  
**Confidence:** BOUNDED EXPLORATION.  
**OPEN:** categories، codes، hierarchy، version migration.

### Need-to-Service Mapping
**Meaning:** Rule/Mapping مصوب که مشخص می‌کند یک Need تحت چه شرایطی به Candidate Serviceها مرتبط می‌شود.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Need identified ≠ automatic service selection`.

### Eligibility
**Meaning:** نتیجه ارزیابی Ruleهای مصوب برای اینکه شخص/Need/Service/Provider در Scope معینی واجد شرایط است یا نه.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** Eligibility باید از Authority/Selection/Payment جدا بماند.  
**OPEN:** rule set، evidence، override، approver.

## 5. Referral and provider concepts

### Referral / ارجاع
**Meaning:** اتصال رسمی یک Need به لایه خدمت یا Provider/مسیر تخصصی برای ادامه ارائه خدمت.  
**Confidence:** SOURCE-SUPPORTED.  
**OPEN:** states، authorization، acceptance/rejection، cancellation، closure، SLA.

### Provider Selection
**Meaning:** تعیین Provider مشخص برای Referral از میان گزینه‌های مجاز.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Eligibility ≠ Provider Selection`.  
**OPEN:** human authority، ranking assistance، elder choice، conflict rules.

### Service Completion
**Meaning:** ثبت اینکه یک Service طبق Definition مربوطه به نقطه Completion رسیده است.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Service Completion ≠ Referral Closure ≠ Need Resolution ≠ Outcome`.

### Provider Result
**Meaning:** نتیجه/گزارشی که Provider از اجرای خدمت برمی‌گرداند.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Provider Result ≠ Final Elder Outcome`.

## 6. Longitudinal state and outcome concepts

### Accepted State / وضعیت پذیرفته‌شده
**Meaning:** وضعیت رسمی سالمند که پس از مسیر معتبر ثبت/بازبینی، برای کاربرد عملیاتی پذیرفته شده است.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Observation ≠ Accepted State`.  
**OPEN:** acceptance authority، evidence rule، revision policy.

### Baseline
**Meaning:** نقطه مرجع معتبر برای مقایسه تغییرات بعدی.  
**Confidence:** BOUNDED EXPLORATION.  
**OPEN:** definition، timing، version.

### Reassessment / ارزیابی مجدد
**Meaning:** ارزیابی دوباره وضعیت/Need در زمان یا Trigger بعدی برای فهم تغییر نسبت به Baseline/وضعیت قبلی.  
**Confidence:** BOUNDED EXPLORATION.  
**OPEN:** cadence، trigger، definition version.

### Need Resolution
**Meaning:** تصمیم رسمی درباره اینکه Need موردنظر طبق معیار مصوب حل‌شده تلقی می‌شود.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** Service completion به‌تنهایی Need Resolution نیست.

### Outcome / پیامد
**Meaning:** ثبت/تفسیر تغییر مشاهده‌شده در وضعیت سالمند نسبت به Baseline یا ارزیابی قبلی، با Evidence و Provenance لازم.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Observed Change ≠ Proven Causal Effect`.  
**Invariant:** `AI Inference ≠ Observed Fact`.  
**OPEN:** taxonomy، evidence validity، reviewer، causal policy.

### Learning Signal
**Meaning:** داده/سیگنالی که پس از عبور از Governance لازم می‌تواند برای Learning مورد استفاده قرار گیرد.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Recorded Outcome ≠ Automatically Verified Training Label`.

## 7. Data and learning concepts

### Operational Data
**Meaning:** داده‌ای که برای عملیات، خدمت، پایش، گزارش یا Governance در نسیم تولید/استفاده می‌شود.  
**Confidence:** SOURCE-SUPPORTED / BOUNDED.  
**Invariant:** `Operationally Available ≠ Training Eligible`.

### AI Runtime Access
**Meaning:** داده‌ای که AI برای اجرای یک Use Case مصوب در لحظه مجاز به استفاده از آن است.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `AI Runtime Access ≠ Training Permission`.

### Training Eligibility
**Meaning:** Policy Versioned که تعیین می‌کند کدام داده تحت چه شروطی اجازه ورود به مسیر Learning/Dataset را دارد.  
**Confidence:** REQUIRED BY D-0005, details OPEN.  
**Invariant:** Dataset automation خود Policy را تغییر نمی‌دهد.

### Dataset Version
**Meaning:** یک نسخه قابل ردیابی از Dataset که از داده‌های eligible/approved طبق Rule/Preparation Version مربوطه ساخته می‌شود.  
**Confidence:** ACCEPTED DIRECTION for automatic/versioned lifecycle; implementation OPEN.  
**Invariant:** `Automatic Dataset Generation ≠ Automatic Governance Change`.

### Model Version
**Meaning:** نسخه مشخص از Model/Artifact مورد استفاده یا ارزیابی.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Model Version ≠ AI Policy Version`.

### AI Policy Version
**Meaning:** نسخه Ruleهای Business/Governance مربوط به Use Case، allowed data/output، forbidden actions، human review، fail-safe و سایر محدودیت‌های AI.  
**Confidence:** BOUNDED EXPLORATION.

## 8. Governance concepts

### Decision
**Meaning:** انتخاب مصوب Product/Business/Governance که در Decision Register ثبت می‌شود.  
**Confidence:** ACCEPTED GOVERNANCE.

### Policy
**Meaning:** Rule کسب‌وکاری/حاکمیتی Versioned که رفتار مجاز را برای Scope و زمان مشخص تعریف می‌کند.  
**Confidence:** BOUNDED EXPLORATION.

### Configuration
**Meaning:** مقدار/تنظیمی که Rule یا رفتار Approved را در Scope مشخص اجرایی می‌کند؛ وجود آن به‌تنهایی Approval نیست.  
**Confidence:** BOUNDED EXPLORATION.

### Runtime Execution
**Meaning:** اجرای Rule/Policy فعال روی یک Case/Request/Context واقعی.  
**Confidence:** BOUNDED EXPLORATION.

**Core invariant:**  
`Decision ≠ Configuration ≠ Runtime Execution`

**Lifecycle invariant:**  
`Draft ≠ Accepted ≠ Active`

### Policy Version
**Meaning:** نسخه مشخص و قابل ردیابی یک Policy با Scope/زمان اثرگذاری.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `New Policy ≠ Retroactive Silent Rewrite`.

## 9. Risk and safety concepts

### Risk
**Meaning:** احتمال/شرایطی که می‌تواند بر سالمند، عملیات، داده، AI، Provider، اقتصاد یا Governance اثر نامطلوب بگذارد.  
**Confidence:** BOUNDED EXPLORATION.

### Incident
**Meaning:** رخداد واقعی یا وضعیت ثبت‌شده‌ای که نیازمند بررسی/پاسخ عملیاتی یا Governance است.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Risk ≠ Incident`.

### Alert
**Meaning:** علامت/هشداری که ممکن است نیازمند بررسی باشد.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** `Alert ≠ Confirmed Incident`.

### Escalation
**Meaning:** انتقال موضوع به سطح/Actor دیگری برای بررسی یا اقدام به دلیل Rule یا شرایط تعیین‌شده.  
**Confidence:** BOUNDED EXPLORATION.

### Urgent / Emergency
**Meaning:** مفاهیم Safety-sensitive که نیازمند Definition و مسیر عملیاتی صریح هستند.  
**Confidence:** OPEN.  
**Invariant:** ذکر آموزش شرایط اضطراری در Concept، تعهد 24/7 یا Medical Triage ایجاد نمی‌کند.

## 10. Measurement and rollout concepts

### KPI
**Meaning:** Metric با Definition Versioned برای سنجش یکی از ابعاد عملکرد/کیفیت/اقتصاد/اثر اجتماعی.  
**Confidence:** SOURCE-SUPPORTED at family level; exact definitions OPEN.

### Evidence
**Meaning:** داده/مدرک قابل ردیابی که برای Review، KPI، Decision، Outcome یا Gate استفاده می‌شود.  
**Confidence:** BOUNDED EXPLORATION.

### Pilot
**Meaning:** مرحله عملیاتی پیش از توسعه شبکه برای تولید Evidence واقعی درباره مدل نسیم.  
**Confidence:** SOURCE-SUPPORTED at high level.  
**OPEN:** geography، size، duration، exact success criteria.

### Scale Gate
**Meaning:** Gate انسانی/حاکمیتی برای تصمیم درباره توسعه بعد از Pilot بر اساس Evidence.  
**Confidence:** BOUNDED EXPLORATION.  
**Invariant:** Reporting یا AI Analysis به‌تنهایی تصمیم Scale نیست.

## 11. Core concept separations

این تفکیک‌ها باید در همه Artifactهای بعدی حفظ شوند:

- Elder ≠ Family Contact ≠ Authorized Representative
- Caregiver ≠ Specialist Provider
- Employer ≠ NASIM Operator
- Role ≠ Permission
- System ≠ Business Authority
- AI Suggestion ≠ Human Decision
- AI Output ≠ Official Record
- Observation ≠ Accepted State ≠ Outcome
- Satisfaction ≠ Outcome
- Service Family ≠ Service Item
- Need ≠ Service
- Need Identified ≠ Service Selected
- Eligibility ≠ Provider Selection
- Referral ≠ Service
- Service Completion ≠ Referral Closure
- Referral Closure ≠ Need Resolution
- Need Resolution ≠ Outcome
- Provider Result ≠ Final Elder Outcome
- Operational Data ≠ Training Eligible Data
- Runtime Access ≠ Training Permission
- Recorded Outcome ≠ Verified Training Label
- Dataset Version ≠ Model Version
- Model Version ≠ AI Policy Version
- Risk ≠ Incident ≠ Escalation ≠ Emergency
- Alert ≠ Confirmed Incident
- Decision ≠ Configuration ≠ Runtime Execution
- Draft ≠ Accepted ≠ Active
- Code Deployment ≠ Business Policy Change

## 12. Concept relationship map

High-level conceptual relationship:

`Elder → Case/Profile → Monitoring → Observation → Need → Initial Assessment → Referral → Provider/Service → Service Completion → Follow-up/Satisfaction → Reassessment → Accepted State/Outcome`

Learning/governance path:

`Operational Data → Training Eligibility Policy → Eligible Data → Dataset Version → Training/Evaluation → Model Version → Human-governed Production Use`

Policy path:

`Decision → Versioned Policy → Approval → Activation for Scope/Time → Runtime Execution → Audit/Lineage`

این سه Flow مفهومی هستند و State Machine یا Technical Architecture نیستند.

## 13. Explicit OPEN concepts

موارد زیر عمداً باز می‌مانند تا Context واقعی آنها Trigger شود:

- exact enrollment eligibility
- exact Pilot geography/size/duration
- final Service Catalog
- Need Taxonomy values
- Referral states
- final Authority Matrix
- Provider types and selection policy
- Consent/legal basis
- Data Access Matrix
- Retention
- Training-eligible Data Classes
- Outcome taxonomy/evidence rules
- KPI formulas/targets
- Risk severity values
- Emergency path
- Policy owner/approver/precedence
- AI model/algorithm/runtime
- Model promotion/rollback authority

طبق D-0118، باز بودن این موارد مانع Exploration نیست و اجازه Guessing نیز ایجاد نمی‌کند.

## 14. Downstream rule

از این سند می‌توان برای Business Exploration بعدی استفاده کرد، اما نباید مستقیم از آن:

- database entity
- API resource
- enum
- workflow state
- permission
- numeric threshold
- production policy

استخراج و Final اعلام شود مگر Decision/Contract مرتبط آن را پشتیبانی کند.

## 15. Next artifact

**BX-003 — Elder Journey & Domain Interaction Map**

Scope:
- استفاده از Vocabulary این سند
- شکستن Journey به Interactionهای مفهومی
- مشخص‌کردن Inputs/Outputs/Actors/Handoffs/Provenance
- مشخص‌کردن Decision Triggerها
- بدون State Machine، API یا Code

## 16. Current stage

- Stage: **Business**
- Vocabulary exploration baseline: **ACTIVE**
- Business → Technical: **NOT READY**
- Code: **NOT STARTED**
- Codex handoff: **NOT YET TRIGGERED**
