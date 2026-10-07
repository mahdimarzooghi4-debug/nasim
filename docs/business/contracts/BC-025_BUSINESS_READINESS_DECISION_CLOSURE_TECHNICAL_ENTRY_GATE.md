# BC-025 — Business Readiness, Decision Closure & Technical Entry Gate

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** D-0002 + D-0003 + D-0004 + D-0005 + D-0118 + `docs/PRODUCT_PROCESS.md` + `docs/business/OPEN_QUESTIONS.md` + BC-001…BC-024 + BX-014 + BX-015
- **Depends on:** BC-001…BC-024

> این سند Gate عبور رسمی نسیم از مرحله **Business** به **Technical** را تعریف می‌کند. این Gate به معنی Accepted شدن خودکار هیچ Business Contract یا Open Decision نیست. طبق D-0118، فقط Blockerهایی که برای Scope/Technical Slice انتخاب‌شده واقعاً لازم‌اند باید Context Triggered و سپس Accepted یا صریحاً Deferred شوند؛ Technical نباید پاسخ Decisionهای OPEN را اختراع کند.

## 1. Parent Process

فرآیند مصوب D-0003:

`Business → Technical → Scrum/Product Backlog → Sprint → Code → Code Review → Stage → QA/Testing → Release Approval → Production → Monitoring → Improvement`

قاعده پایه:

`Technical derives from approved Business; Technical does not complete missing Business decisions by guess.`

## 2. Purpose of the Technical Entry Gate

هدف Gate این است که پیش از شروع طراحی فنی مشخص شود:

- چه چیزی قرار است ساخته شود
- برای چه کسی ساخته می‌شود
- چه رفتارهای کسب‌وکاری قطعی هستند
- چه تصمیم‌هایی انسانی‌اند
- چه Ruleهایی باید قابل پیکربندی باشند
- چه داده‌ای مجاز است
- AI چه کارهایی مجاز/ممنوع دارد
- چه ریسک‌ها و قیود ایمنی وجود دارند
- موفقیت Pilot چگونه سنجیده می‌شود
- چه موضوعاتی عمداً به Technical واگذار می‌شوند
- چه موضوعاتی عمداً Deferred شده‌اند

Gate برای جلوگیری از تبدیل «ابهام Business» به «فرض فنی پنهان» است.

## 3. Documentation Coverage ≠ Decision Closure

نسیم اکنون پوشش مستند گسترده‌ای در BC-001 تا BC-024 دارد.

اما:

`Documented Question ≠ Accepted Answer`

و:

`Draft Contract ≠ Closed Business Decision`

تعداد زیاد Contractها به‌تنهایی اجازه عبور به Technical ایجاد نمی‌کند.

## 4. Current Readiness Assessment

ارزیابی به‌روزشده در 2026-10-07:

- D-0001 تا D-0005 و D-0118 در Decision Register وضعیت **Accepted** دارند.
- D-0006…D-0117 همچنان **Not Accepted** هستند.
- BX-001…BX-015 Business Exploration و Technical-entry preparation را پوشش داده‌اند.
- Candidate Technical Sliceها Map شده‌اند، اما **هیچ Slice انتخاب نشده است**.
- Open Decisionها طبق D-0118 فقط وقتی Slice/Work Item واقعی به آنها وابسته شود Context Triggered می‌شوند.

بنابراین:

**Global Business → Technical Gate: NOT PASSED**

این نتیجه به معنی توقف Exploration نیست. یک Technical Slice محدود فقط بعد از انتخاب صریح Slice، بستن یا Deferral صریح Blockerهای همان Slice و ثبت Slice Gate Evidence می‌تواند برای Technical توصیه شود.

## 5. Closure Classification

هر Open Decision که برای Technical Scope/Slice انتخاب‌شده لازم شود باید در Gate همان Scope در یکی از این کلاس‌ها قرار گیرد. Decisionهای نامرتبط می‌توانند OPEN بمانند:

### A. BUSINESS BLOCKER
بدون پاسخ آن، Technical مجبور به اختراع رفتار محصول، اختیار، داده، Safety Rule یا Scope می‌شود.

### B. EXPLICITLY DEFERRED
برای فاز/پایلوت فعلی لازم نیست و با Decision صریح از Scope خارج شده است.

### C. TECHNICAL DECISION
Business Intent روشن است و انتخاب Implementation می‌تواند در مرحله Technical انجام شود.

### D. LATER DELIVERY / OPERATIONS DECISION
برای Technical Architecture اولیه Blocking نیست و می‌تواند در Gate بعدی قبل از Stage/Production بسته شود.

Classification هر موضوع باید Traceable باشد.

## 6. Deferral Rule

یک موضوع فقط زمانی قابل Deferred است که حداقل این موارد مشخص باشند:

- چه چیزی Deferred شده است
- چرا برای فاز فعلی لازم نیست
- Scope اثر
- چه رفتار جایگزینی در فاز فعلی حاکم است
- Owner
- Deadline/Gate آینده
- Risk/constraint
- چه چیزی Technical نباید درباره آن فرض کند

اصل:

`Unknown ≠ Deferred`

Deferred بودن نیازمند تصمیم صریح است.

## 7. Product & Scope Blockers

حداقل این تصمیم‌ها باید برای Phase/Pilot فعلی بسته شوند:

- جامعه هدف فاز اول
- Entry/Eligibility حداقل فاز
- محدوده جغرافیایی
- Pilot population/operating scope
- In-scope / out-of-scope services
- Phase-1 Service Catalog
- Direct vs Referral-only boundary
- نقش AI از Day 1 در Scope واقعی Pilot

Technical بدون این موارد نمی‌تواند Boundary سیستم را به‌طور معتبر تعیین کند.

## 8. Elder Journey & Operations Blockers

حداقل باید Business Intent این حوزه‌ها روشن شود:

- Journey شروع تا Follow-up
- Case ownership
- Referral trigger
- Referral authorization
- Referral lifecycle حداقل فاز
- Provider acceptance/rejection boundary
- Follow-up ownership
- Reassessment trigger
- Need resolution/closure boundary
- Complaint path
- عدم دسترسی/غیبت/جانشینی
- Urgent/Emergency safe handling برای Scope Pilot

تمام Stateها و SLAها لزوماً قبل از Technical نیاز نیستند، اما رفتار Safety-critical نباید مبهم باقی بماند.

## 9. Role & Decision-right Blockers

برای Technical Entry باید حداقل مشخص باشد:

- Role inventory فاز
- Actor boundaries
- چه کسی چه Business Actionهایی را نهایی می‌کند
- چه چیزی Approval انسانی می‌خواهد
- Provider authority
- Employer boundary
- Family/authorized-representative boundary
- Incident/Risk ownership
- Model/AI governance ownership
- Scale/Pilot decision ownership

Technical نباید Permission را از Job Title حدس بزند.

## 10. Data, Privacy & Legal Blockers

برای داده‌ای که در Phase/Pilot استفاده می‌شود، حداقل باید مشخص شود:

- Data classes اصلی
- Purpose of processing
- Consent/legal-basis direction
- Data-sharing boundary
- Employer reporting boundary
- Provider data boundary
- Family/representative access boundary
- AI runtime data boundary
- Training Eligibility boundary
- Retention/deletion direction لازم برای Pilot
- privacy/security constraints

Legal Review ممکن است جزئیات حقوقی نهایی را بعداً Formalize کند، اما Technical نباید با فرض «همه داده مجاز است» آغاز شود.

## 11. Security & Access Blockers

برای Technical Entry باید Business Boundary کافی برای طراحی امنیت وجود داشته باشد:

- Identity actor classes
- organization boundaries
- least-privilege principle
- sensitive action classes
- privileged action boundary
- audit-required actions
- export/sharing boundary
- non-human identity boundary
- AI runtime access vs Training access
- recovery/security constraints

انتخاب IdP، MFA، RBAC/ABAC و فناوری امنیتی همچنان Technical Decision است.

## 12. AI Day-one Blockers

با توجه به D-0004 و D-0005، AI نمی‌تواند از Technical Scope حذف شود.

قبل از Technical Entry باید حداقل این Business Decisions بسته شوند:

- Phase-1 elder AI use cases
- Phase-1 caregiver AI use cases
- forbidden actions
- human-review requirements
- official-record boundary
- AI transparency boundary
- runtime data access boundary
- training-eligible data classes/rules
- Dataset governance ownership
- model evaluation governance
- model promotion authority
- model rollback authority
- fail-safe behavior when AI unavailable/invalid
- AI incident boundary

Model، algorithm، training implementation و infrastructure انتخاب Technical هستند مگر Product Decision جداگانه‌ای خلاف آن ثبت شود.

## 13. Automatic Dataset Lifecycle Blockers

D-0005 ساخت Dataset خودکار و مستمر را الزام کرده است.

Technical Entry نیازمند Business clarity حداقل در این موارد است:

- چه داده‌ای اصولاً Candidate Learning Data است
- چه Rule/Ownerی Training Eligibility را تعیین می‌کند
- چه داده‌هایی Excluded هستند
- Provenance/Lineage requirements
- Dataset versioning requirement
- Human/AI label validity boundaries
- Outcome/Reassessment training-signal boundary
- external-data training boundary

Trigger، batching، orchestration و storage Technical Decision هستند.

## 14. Provider Network Blockers

برای Provider-related Technical Design باید مشخص شود:

- Provider types لازم برای Phase/Pilot
- onboarding/activation boundary
- service-to-provider mapping
- Provider access boundary
- referral acceptance/rejection intent
- completion/result evidence direction
- suspension/incident authority
- integration requirement برای Providerهای Pilot

Ranking/algorithm یا SLA عددی در صورت عدم نیاز به Pilot می‌تواند طبق Decision صریح Deferred شود.

## 15. Economic / Funding Blockers

همه جزئیات Business Model لزوماً Technical Blocker نیستند.

اما برای Phase/Pilot باید روشن باشد:

- چه کسی Funding/Payer اصلی است
- آیا End-user payment در Scope است یا خیر
- آیا Billing/Settlement در Product Scope فاز وجود دارد یا خیر
- اگر وجود دارد، Actor و Business flow آن چیست
- چه Financial Actions نیازمند Approval هستند

Technical نباید Payment/Billing را صرفاً از Concept اقتصادی حدس بزند.

## 16. KPI, Quality & Pilot Blockers

پیش از Technical Entry باید معلوم باشد که Pilot چه چیزی را باید بتواند Measure کند.

حداقل:

- KPI families مورد نیاز Pilot
- Success dimensions
- Data evidence required
- AI quality evidence
- Dataset lifecycle evidence
- Risk/incident evidence
- Scale Gate evidence package

Target/Threshold عددی می‌تواند فقط در صورتی Deferred شود که Technical برای ثبت Evidence لازم همچنان Specification کافی داشته باشد.

## 17. Reporting Blockers

Technical باید بداند چه گروه‌های گزارش اصلی در Phase/Pilot لازم‌اند:

- operational
- supervisory
- management
- employer/governance در صورت Scope

همچنین باید روشن باشد:

- aggregate vs individual boundary
- sensitive drill-down boundary
- KPI versioning requirement
- AI-generated insight boundary
- required audit/provenance

Dashboard UI و BI Tool Technical/Product Design بعدی هستند.

## 18. Integration Blockers

برای Pilot باید Integration Inventory حداقل مشخص شود:

- required external systems
- purpose
- direction
- required data classes
- source of truth
- organization boundary
- legal/data-sharing boundary
- failure behavior
- whether integration is mandatory for Pilot

Protocol/API/schema Technical Decision است.

Integrationای که برای Pilot ضروری نیست باید Explicitly Deferred شود، نه implicitly ignored.

## 19. Continuity & Recovery Blockers

قبل از Technical باید Business Criticality کافی تعیین شود تا Architecture قابل طراحی باشد.

حداقل:

- critical business capabilities
- minimum operation during outage
- which functions may degrade
- AI outage business behavior
- Dataset-pipeline failure business boundary
- backup/recovery business requirement
- security must remain enforced during recovery

RTO/RPO اگر برای Architecture sizing ضروری باشند باید قبل از نهایی‌شدن Technical Architecture بسته شوند.

## 20. Configuration & Change Governance Blockers

Technical باید از ابتدا بداند کدام Business Rules نباید Hard-code و بی‌نسخه باشند.

حداقل باید Versionable فرض شوند:

- Need Taxonomy
- Service Catalog
- Eligibility Rules
- Data/Access Policies
- Training Eligibility
- AI Use-case/Guardrail Policies
- KPI Definitions
- Integration Contracts
- other approved configurable policies

Runtime نباید Draft Policy را اجرا کند.

## 21. Technical Decisions That May Remain Open

نمونه موضوعاتی که در صورت روشن بودن Business Intent می‌توانند وارد Technical شوند:

- system architecture
- service decomposition
- database technology
- API style
- event/messaging technology
- hosting topology
- programming language/framework
- identity technology
- storage technologies
- observability stack
- backup implementation
- AI model/algorithm
- training orchestration
- dataset storage/layout
- deployment mechanism
- CI/CD
- infrastructure sizing

این فهرست به معنی انتخاب هیچ موردی نیست.

## 22. Technical Must Not Backfill Business

در مرحله Technical ممنوع است که برای رفع ابهام موارد زیر اختراع شوند:

- Service Catalog
- Eligibility policy
- role authority
- consent rule
- provider selection authority
- pricing/funding policy
- KPI target
- AI permission
- Training Eligibility
- model promotion authority
- emergency business process
- legal access rights

ابهام این موارد باید به Business برگردد.

## 23. Required Business Exit Package

برای عبور از Business باید یک Exit Package قابل بازبینی وجود داشته باشد که حداقل شامل این موارد باشد:

1. Current Decision Register
2. Business Contract index + status
3. Phase/Pilot Scope
4. Accepted/approved Service Catalog baseline
5. Elder Journey / Referral business baseline
6. Role & Decision Rights baseline
7. Provider business baseline
8. Data/Consent/Access baseline
9. AI Day-one Use-case & Governance baseline
10. Training Eligibility / Dataset Governance baseline
11. Quality/KPI/Pilot evidence baseline
12. Risk/Safety/Incident baseline
13. Security/Continuity business requirements
14. Required Integration inventory
15. Configuration/versioning requirements
16. Explicit Deferred Decisions register
17. Remaining Technical-only Questions

Artifact format نهایی هنوز تصمیم نشده است.

## 24. Contract Status Rule

برای Gate، هر BC باید یکی از این وضعیت‌های Governance-relevant را داشته باشد:

- Accepted for Phase/Pilot
- Accepted with explicit conditions
- Explicitly deferred/not applicable for Phase/Pilot
- Blocking / unresolved

Vocabulary رسمی Status هنوز در BC-024 باز است؛ این بخش فقط نیاز Gate را بیان می‌کند.

## 25. Cross-contract Consistency

پیش از Gate باید تعارض‌های مهم میان Contractها حل شوند.

Candidate checks:

- Role vs Permission
- Service vs Provider
- Need vs Outcome
- Consent vs Data Access
- Runtime Access vs Training Permission
- AI Use Case vs Forbidden Actions
- Dataset Automation vs Governance
- KPI Definition vs Reporting
- Integration vs Source of Truth
- Continuity vs Security
- Configuration vs Effective Version

وجود دو Contract متعارض نباید با انتخاب دلخواه Technical حل شود.

## 26. Decision Register Closure

وقتی یک Open Decision پذیرفته شد باید مطابق D-0002 در `docs/DECISIONS.md` ثبت شود.

اگر Decision قبلی تغییر کند:

- Decision قبلی حذف نمی‌شود
- Superseded می‌شود
- جایگزین Traceable ثبت می‌شود

Technical باید از Decision Version معتبر استفاده کند.

## 27. Gate Evidence Record

عبور از Business → Technical باید یک Gate Record صریح داشته باشد.

Candidate fields:

- gate ID
- date
- product scope/version
- contracts reviewed
- decisions accepted
- blockers remaining
- deferred decisions
- constraints
- risks accepted
- technical-entry decision
- decision owner/approver
- evidence links

قالب و Approver نهایی هنوز باید در Governance بسته شود.

## 28. Gate Outcomes — DRAFT FRAME

برای Gate می‌توان این Outcomeهای مفهومی را بررسی کرد:

### READY
هیچ Business Blocker شناخته‌شده‌ای برای Technical Scope باقی نمانده است.

### READY WITH EXPLICIT DEFERRALS
موضوعات باز وجود دارند، اما صریحاً خارج از Technical Scope فعلی قرار گرفته‌اند و Constraint روشن دارند.

### NOT READY
حداقل یک Business Blocker وجود دارد که Technical را مجبور به حدس رفتار/اختیار/داده/Safety می‌کند.

این Vocabulary هنوز Decision Status رسمی نیست.

## 29. Current Gate Result

بر اساس وضعیت فعلی مخزن در 2026-10-07:

**Global Business → Technical Gate: NOT PASSED**

دلایل:

- Accepted baseline اکنون D-0001…D-0005 + D-0118 است.
- D-0006…D-0117 هنوز Accepted نشده‌اند.
- Candidate Technical Sliceها در BX-015 Map شده‌اند، اما Slice منتخب وجود ندارد.
- تا زمانی که Slice انتخاب نشود، Blockerهای آن Slice نیز نباید دسته‌ای Context Triggered شوند.
- هیچ Slice Gate Record پاس‌شده‌ای وجود ندارد.

بنابراین ورود رسمی و سراسری به Technical مجاز نیست. ورود محدود به یک Technical Slice نیز فقط پس از Selection صریح و Gate همان Slice ممکن است.

## 30. Recommended Closure Sequence — DRAFT

طبق D-0118 مسیر پیش‌فرض دیگر بستن همه Decisionهای Pilot به‌صورت یک‌جا نیست.

Sequence فعلی:

1. **Select one bounded Technical Slice explicitly**
2. **Identify only the Business decisions required by that Slice**
3. **Move only those decisions to CONTEXT TRIGGERED**
4. **Accept / Modify / Reject / Explicitly Defer only that minimal set**
5. **Create Slice Gate Evidence**
6. **Enter Technical only for that bounded Slice if the Gate passes**

Candidate Sliceها و Minimal Decision Set هرکدام در BX-015 ثبت شده‌اند.

این Sequence هیچ Slice یا Decision را به‌صورت خودکار انتخاب/پذیرفته نمی‌کند.

## 31. No Premature Architecture Freeze

قبل از Gate می‌توان Technical Exploration محدود انجام داد، اما نباید:

- Architecture را Final اعلام کرد
- API Contract نهایی ساخت
- State Machineهای باز را Hard-code کرد
- Data Model را بر فرض‌های Business ناتمام بنا کرد
- AI behavior را از روی حدس تعیین کرد
- Backlog implementation-ready را بر Decisionهای باز ساخت

Exploration باید به‌وضوح Non-binding باشد.

## 32. Backlog Entry Rule

موضوعی فقط زمانی باید به Product Backlog implementation-ready وارد شود که:

- Business requirement قابل استناد باشد
- Open Decision مرتبط Blocking نباشد
- Acceptance boundary روشن باشد
- Technical Design مربوطه وجود داشته باشد

بنابراین:

`Draft Business Question → not implementation-ready backlog`

## 33. Business Exit Review

پیش از اعلام پایان Business باید Review نهایی بررسی کند:

- آیا Open Question بدون Classification باقی مانده؟
- آیا Blocking Decision بدون Owner باقی مانده؟
- آیا Draft Rule در Scope Production/Pilot وجود دارد؟
- آیا Contractها با Accepted Decisions همسو هستند؟
- آیا AI از Day 1 واقعاً در Scope و Governance پوشش دارد؟
- آیا Dataset Automation governance-ready است؟
- آیا Safety/Privacy/Security gaps به Technical واگذار نشده‌اند؟
- آیا Pilot Evidence قابل اندازه‌گیری طراحی شده است؟

## 34. Acceptance of BC-025 Does Not Automatically Pass the Gate

اصل مهم:

`Accepting the Gate Definition ≠ Passing the Gate`

حتی اگر BC-025 بعداً Accepted شود، پروژه فقط زمانی وارد Technical می‌شود که Gate Evidence نشان دهد Blocking Decisionها بسته شده‌اند و Gate Decision صریح ثبت شده است.

## 35. Explicit Non-Decisions

BC-025 موارد زیر را تصویب نمی‌کند:

- پاسخ هیچ Open Question
- Accepted شدن BC-001…BC-024
- پایان مرحله Business
- شروع مرحله Technical
- Phase-1 scope نهایی
- Pilot geography/size
- Service Catalog نهایی
- AI Use Case نهایی
- KPI target
- Technical architecture
- technology stack
- Gate approver نهایی
- formal workflow/status enum

## 36. Open Decisions Required to Accept BC-025

این فهرست مربوط به Governance خود Gate است و نباید به معنی اجبار به بستن همه Domain Decisionهای نامرتبط پیش از یک Slice محدود تفسیر شود.

1. Technical Entry Gate owner/approver
2. Formal gate outcomes/statuses
3. Required vs optional Business Exit artifacts
4. Which BCs must be Accepted for Pilot
5. Deferral approval authority
6. Deferred-decision register format
7. Minimum legal review required before Technical
8. Minimum AI governance closure required
9. Minimum training-eligibility closure required
10. Minimum security/continuity targets required
11. Gate evidence format
12. Whether Technical Exploration is allowed before Gate and under what constraints
13. Business Exit Review participants
14. Formal Decision record for Business → Technical transition

## 37. Downstream Constraints

تا زمانی که Gate صریحاً Pass نشده است:

- وضعیت پروژه همچنان **Business** است.
- Technical Design رسمی نباید Business Decisionهای باز را قطعی فرض کند.
- Backlog implementation-ready نباید بر فرض‌های Business باز ساخته شود.
- Code نباید به‌عنوان راه‌حل برای تصمیم نگرفته‌شده Business استفاده شود.
- AI/Data/Security/Safety boundaries نباید در Technical اختراع شوند.
- ورود رسمی به Technical فقط با Gate Record و Decision پذیرفته‌شده مجاز است.
