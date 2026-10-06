# BC-024 — Business Configuration, Policy Versioning & Change Governance

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** D-0002 + D-0003 + D-0004 + D-0005 + BC-007 + BC-010 + BC-013 + BC-018 + BC-020 + BC-022 + BC-023
- **Depends on:** BC-005, BC-006, BC-007, BC-010, BC-012, BC-013, BC-014, BC-018, BC-019, BC-020, BC-022, BC-023

> این سند یک نیاز حاکمیتی جدید برای نسیم را صورت‌بندی می‌کند: Ruleها، Catalogها، Taxonomyها و Policyهای اثرگذار بر رفتار محصول نباید به‌صورت بی‌نسخه، بی‌Owner یا بدون Approval تغییر کنند. طرح اولیه مکانیزم Configuration/Versioning را تعریف نکرده است؛ این Contract از تصمیمات مصوب پروژه و نیازهای ایجادشده در Business Contractهای قبلی مشتق شده است.

## 1. Governance Principle

نسیم باید میان این سه مفهوم تفکیک داشته باشد:

- **Business Decision:** تصمیم مصوب درباره اینکه چه قاعده‌ای باید حاکم باشد
- **Policy / Configuration:** بیان عملیاتی و نسخه‌دار آن تصمیم
- **Runtime Execution:** اجرای همان Policy/Configuration توسط سامانه

اصل:

`Decision ≠ Configuration ≠ Runtime Execution`

سامانه نباید خودش Policy جدید بسازد یا Decision Business را تغییر دهد.

## 2. Repository Decision Governance

بر اساس D-0002، مخزن `mahdimarzooghi4-debug/nasim` مرجع رسمی تصمیمات پروژه است.

بر اساس D-0003، تصمیم‌های مصوب باید پیش از عبور به Technical/Code مبنای مراحل بعدی باشند.

بنابراین:

- تصمیم محصولی/حاکمیتی پذیرفته‌شده باید در Decision Register ثبت شود.
- Draft Business Contract به‌تنهایی Decision Accepted محسوب نمی‌شود.
- Runtime Configuration نباید منبع مستقل تصمیم محصول باشد.

## 3. Draft ≠ Accepted ≠ Active

این وضعیت‌ها باید از هم جدا بمانند:

- **DRAFT:** هنوز تصمیم مصوب نیست
- **ACCEPTED:** تصمیم Business/Governance تصویب شده است
- **ACTIVE/EFFECTIVE:** Policy/Configuration مصوب برای یک Scope و زمان مشخص قابل اجرا شده است
- **SUPERSEDED/RETIRED:** نسخه جدید جایگزین شده یا استفاده جدید از آن متوقف شده است

این Vocabulary فعلاً Frame است و State Machine نهایی نیست.

## 4. Configuration Domains

Business Configuration آینده ممکن است حداقل این حوزه‌ها را پوشش دهد:

- Target/eligibility rules
- Need Taxonomy
- Service Catalog
- Need-to-Service mapping
- Referral eligibility
- Provider eligibility/mapping
- Consent/privacy policies
- Data classification/access policies
- Training Eligibility
- Dataset preparation/curation rules
- AI use-case policies
- AI guardrails / forbidden actions
- Human-review requirements
- KPI/metric definitions
- Reporting definitions
- Incident/risk rules
- Workforce/training requirements
- Communication/notification rules
- Integration contracts/configuration
- Continuity/backup governance parameters
- Security/access governance policies

وجود در این فهرست به معنی نهایی‌شدن هیچ Rule نیست.

## 5. Policy as a Versioned Business Object

هر Policy مهم باید در آینده بتواند حداقل این اطلاعات را داشته باشد:

- policy identifier
- policy type/domain
- version
- status
- business owner
- approver
- scope
- effective-from
- effective-to در صورت وجود
- content/rules
- rationale
- evidence/reference
- supersedes/superseded-by
- change history
- related decision
- audit trail

Data Model فنی بعداً تعیین می‌شود.

## 6. Effective Dating

Policyها باید بتوانند از یک زمان مشخص مؤثر شوند.

اصل:

`Approved now ≠ necessarily effective immediately`

ممکن است نسخه‌ای:

- Approved باشد ولی هنوز Effective نشده باشد
- فقط برای Pilot فعال باشد
- فقط در Geography یا Organization مشخصی فعال باشد
- در تاریخ آینده جایگزین نسخه قبلی شود

Rule دقیق Activation هنوز تصمیم نشده است.

## 7. Historical Integrity

تغییر Policy نباید معنای داده تاریخی را بی‌صدا عوض کند.

برای Recordهای مهم باید بتوان نسخه Policy مرتبط را در زمان وقوع حفظ کرد.

Candidate examples:

- Need Taxonomy version
- Service Catalog version
- Eligibility Rule version
- KPI definition version
- Consent policy version
- Access policy version
- AI policy/version
- Training Eligibility version
- Integration contract version

اصل:

`New Policy ≠ Retroactive Silent Rewrite`

## 8. Taxonomy Versioning

همسو با BC-018، Need Taxonomy باید Versionable باشد.

در تغییر Taxonomy باید آینده مشخص شود:

- code continuity
- renamed categories
- split/merge mapping
- deprecated categories
- historical interpretation
- dataset impact
- reporting impact

Technical نباید Codeهای قدیمی را بی‌صدا به معنای جدید تبدیل کند.

## 9. Service Catalog Versioning

Service Catalog باید بتواند تغییرات زیر را Version کند:

- service definition
- family
- target need
- direct/referral-only
- provider mapping
- preconditions
- required data
- completion criteria
- quality criteria
- funding/pricing در صورت تصویب
- availability

Referral/Service تاریخی باید به نسخه‌ای که در آن زمان معتبر بوده قابل ردیابی باشد.

## 10. Eligibility Rule Versioning

Eligibility Ruleها باید Versioned و Effective-dated باشند.

برای هر Eligibility Decision آینده باید بتوان مشخص کرد:

- rule version
- input/evidence
- evaluation time
- result
- actor/process
- override/review در صورت وجود

Rule جدید نباید نتیجه تاریخی را بی‌صدا بازنویسی کند.

## 11. KPI / Metric Definition Versioning

همسو با BC-010 و BC-020، KPI Definition باید Versionable باشد.

تغییر در:

- numerator
- denominator
- inclusion/exclusion
- time window
- source data
- target/threshold

باید Version جدید ایجاد کند یا طبق Policy مصوب مدیریت شود.

گزارش تاریخی باید Metric Version خود را حفظ کند.

## 12. Data & Access Policy Versioning

همسو با BC-007 و BC-022، تغییر در این موارد باید قابل ردیابی باشد:

- Data Classification
- Purpose Matrix
- Data Access Matrix
- Provider access
- Employer access
- Family/representative access
- AI runtime access
- Training-pipeline access
- Export permissions

Access Decisionهای جدید نباید بی‌ردپا جای نسخه قبلی را بگیرند.

## 13. Consent / Privacy Policy Versioning

اگر Consent/Privacy Rule تغییر کند باید مشخص باشد:

- نسخه متن/Policy
- effective date
- affected population
- whether re-consent/re-notice is required
- effect on existing data
- effect on future processing
- effect on AI Training Eligibility

Rule حقوقی نهایی در BC-014 همچنان باز است.

## 14. Training Eligibility Versioning

با توجه به D-0005، Datasetها به‌صورت خودکار و مستمر ساخته می‌شوند.

بنابراین Training Eligibility Rule باید حتماً Versionable باشد.

هر Dataset Version باید بتواند به نسخه Eligibility Rule خود اشاره کند.

اصل:

`Automatic Dataset Generation ≠ Automatic Policy Change`

Pipeline Rule مصوب را اجرا می‌کند؛ Rule را خودش تغییر نمی‌دهد.

## 15. Dataset Preparation/Curation Policy Versioning

اگر Preparation/Curation تغییر کند، باید نسخه آن نیز قابل ردیابی باشد.

Candidate changes:

- exclusion
- filtering
- de-identification
- normalization
- annotation/labeling
- quality gates
- deduplication

Dataset Version باید بداند با چه Policy Versionی ساخته شده است.

## 16. AI Use-case Policy Versioning

برای هر AI Use Case باید در آینده بتوان نسخه Policy آن را ثبت کرد.

Candidate fields:

- use-case scope
- intended users
- allowed data
- allowed outputs
- forbidden actions
- human-review rule
- escalation
- fail-safe
- logging
- evaluation requirements

فعال‌شدن یک Use Case جدید نباید صرفاً با Deploy Code انجام شود؛ Business/Governance approval لازم است.

## 17. AI Guardrail Change

تغییر Guardrail یا Forbidden Action باید Change Governance مستقل داشته باشد.

AI، Model یا Automation نباید Guardrail خود را خودکار تغییر دهد.

اصل:

`Model improvement ≠ authority to change policy`

## 18. Model Version vs Policy Version

این دو باید جدا بمانند:

- **Model Version:** نسخه Artifact/Model
- **AI Policy Version:** قواعد کسب‌وکاری استفاده از Model

ممکن است یک Model Version با Policy متفاوت یا یک Policy با Modelهای مختلف ارزیابی شود.

Technical نباید این دو Version را یکی فرض کند.

## 19. Configuration Scope

هر Configuration ممکن است Scope محدود داشته باشد:

- national/global
- employer/organization
- geography
- pilot
- service
- provider type
- workforce role
- AI use case

Scope inheritance/override Rule هنوز تصمیم نشده است.

## 20. Override Governance

اگر Override لازم باشد، باید Business Rule تعیین کند:

- چه چیزی قابل Override است
- چه کسی مجاز است
- Scope
- duration
- reason
- evidence
- approval
- expiry
- audit

Technical نباید امکان Override نامحدود/بی‌Audit ایجاد کند.

## 21. Policy Conflict

ممکن است Policyها با هم تعارض داشته باشند.

Candidate conflict examples:

- Organization-specific vs global policy
- old vs new effective version
- service rule vs provider rule
- privacy rule vs operational convenience
- AI policy vs data-access policy

Conflict-resolution precedence باید صریح باشد و نباید در Code حدس زده شود.

## 22. Change Proposal

هر تغییر مهم باید در آینده بتواند Proposal قابل بررسی داشته باشد.

Candidate fields:

- proposed change
- reason
- affected domains
- expected benefit
- risks
- data/privacy impact
- operational impact
- AI/dataset impact
- backward compatibility
- rollout proposal
- rollback proposal
- evidence

Workflow نهایی Change Proposal هنوز تصمیم نشده است.

## 23. Change Impact Assessment

پیش از فعال‌سازی Policy جدید باید اثر آن در حد متناسب بررسی شود.

Candidate dimensions:

- elder safety
- operations
- provider network
- workforce
- legal/privacy
- data
- security
- integrations
- reporting/KPI
- AI runtime
- dataset/training
- continuity
- economics

سطح بررسی برای هر نوع Change هنوز تعیین نشده است.

## 24. Approval Before Activation

اصل:

`Configured ≠ Approved ≠ Active`

وجود Configuration در سامانه به معنی مجاز بودن اجرای آن نیست.

برای Changeهای Governance-sensitive باید Approval قبل از Activation وجود داشته باشد.

Owner/Approver نهایی در BC-013 باز است.

## 25. Separation of Duties

برای Changeهای حساس، Business آینده باید بررسی کند آیا یک Actor می‌تواند هم:

- پیشنهاد دهد
- Approve کند
- Activate کند
- Audit کند

یا خیر.

Candidate sensitive domains:

- Training Eligibility
- Data Access
- AI Guardrails
- Model Promotion Policy
- Provider suspension rules
- Risk Acceptance
- Financial rules
- Scale Gate rules

## 26. Testing Before Effective Use

Policy/Configuration جدید ممکن است نیازمند Test قبل از Activation باشد.

Candidate test domains:

- rule correctness
- regression
- permissions
- reporting impact
- integration compatibility
- dataset impact
- AI behavior
- rollback
- audit

Test type و Gate دقیق در مرحله Technical/QA تعیین می‌شود.

## 27. Rollout Strategy — Open

Business آینده باید بتواند برای تغییرات مهم Rollout مناسب تعریف کند.

Candidate approaches:

- all-at-once
- pilot-only
- geography-limited
- organization-limited
- percentage/controlled rollout

هیچ Rollout Strategy نهایی در BC-024 تصویب نمی‌شود.

## 28. Rollback

هر Change حساس باید در صورت امکان Strategy بازگشت داشته باشد.

Rollback باید مشخص کند:

- previous valid version
- affected records
- effective time
- reconciliation
- audit
- dataset/reporting impact

Rollback Policy با Data Restore یا Model Rollback لزوماً یکی نیست.

## 29. Configuration Change Audit

برای هر Change مهم باید حداقل قابل ردیابی باشد:

- who proposed
- who reviewed
- who approved
- who activated
- what changed
- previous version
- new version
- scope
- effective time
- reason/evidence
- rollback/reversal

## 30. Runtime Traceability

برای تصمیم‌های مهمی که سامانه بر اساس Rule اجرا می‌کند باید در آینده بتوان نسخه Rule را بازسازی کرد.

Candidate cases:

- eligibility evaluation
- access decision
- referral rule
- notification rule
- KPI calculation
- dataset eligibility
- AI guardrail/application

اصل:

`Runtime Result must be traceable to the rule version that produced it.`

## 31. Policy Registry — DRAFT BUSINESS NEED

نسیم در آینده نیازمند یک Registry منطقی از Policy/Configurationها است.

Candidate fields:

- policy ID
- domain
- version
- status
- scope
- owner
- approver
- effective dates
- dependency
- supersession chain
- audit reference

این الزام، Database یا Configuration Platform خاصی را تصویب نمی‌کند.

## 32. Dependency Between Policies

Policyها می‌توانند به هم وابسته باشند.

مثلاً:

- Need-to-Service mapping به Need Taxonomy و Service Catalog وابسته است.
- Dataset Eligibility به Data Classification/Consent وابسته است.
- KPI به Source Definitions وابسته است.
- AI Use Case به Access Policy و Human Review وابسته است.

Activation نباید Dependency ناسازگار ایجاد کند.

## 33. Dataset Impact Assessment

هر Change در Ruleهایی که بر Learning اثر دارد باید مشخص کند آیا روی:

- future Dataset versions
- existing Dataset interpretation
- lineage
- labels
- training eligibility
- evaluation comparability

اثر دارد یا خیر.

Dataset تاریخی نباید بی‌ردپا بازسازی/بازنویسی شود.

## 34. Reporting Impact Assessment

تغییر Rule یا Definition ممکن است Trend را بشکند.

Business آینده باید تعیین کند:

- آیا گزارش قبل/بعد قابل مقایسه است
- آیا Restatement لازم است
- آیا Version Boundary باید نمایش داده شود
- آیا KPI continuity شکسته است

Dashboard نباید دو تعریف متفاوت را بدون علامت در یک Trend ادغام کند.

## 35. Integration Configuration Change

همسو با BC-023، تغییر در Integration Contract باید Versioned باشد.

Candidate changes:

- data fields
- direction
- source-of-truth
- interface contract
- consent/legal basis
- retry/reconciliation behavior

Technical Interface Version باید به Business Integration Contract قابل ردیابی باشد.

## 36. Emergency Change — Open

ممکن است در Incident جدی نیاز به Change فوری وجود داشته باشد.

Business آینده باید تعیین کند:

- چه چیزی Emergency Change محسوب می‌شود
- چه کسی مجاز است
- چه Approval حداقلی لازم است
- چه مدت موقت است
- چه Audit لازم است
- چه Post-review لازم است
- چه زمانی باید Formalize یا Rollback شود

BC-024 هیچ Break-glass Change Rule نهایی تصویب نمی‌کند.

## 37. Technical Configuration Boundary

BC-024 Business Policy را از Technical Configuration جدا می‌کند.

نمونه Technical Configuration:

- timeout
- connection pool
- deployment replica count
- infrastructure tuning

نمونه Business Policy:

- Eligibility Rule
- Access Rule
- Service Definition
- KPI Formula
- AI Forbidden Action

هر Technical Setting الزاماً نیازمند Business Approval نیست؛ اما نباید Business Meaning را پنهانی تغییر دهد.

## 38. Code Change ≠ Business Policy Change

اصل:

`Code deployment must not silently redefine business policy.`

اگر Code Change باعث تغییر رفتار Business Rule شود، باید Policy/Decision اثرگذار مشخص و Traceable باشد.

## 39. Environment Promotion

بر اساس فرآیند مادر D-0003، تغییر باید از مسیر Delivery Governance عبور کند.

اما BC-024 Environmentها یا CI/CD را تعیین نمی‌کند.

قاعده Business:

- نسخه‌ای که در Production مؤثر می‌شود باید همان نسخه Approved باشد.
- تفاوت Policy بین Stage و Production باید قابل تشخیص باشد.
- Production activation باید Audit داشته باشد.

## 40. AI Cannot Author or Approve Policy

AI می‌تواند در آینده برای تحلیل Change، Draft، Impact Summary یا Evidence کمک کند.

اما:

- AI Policy را نهایی تصویب نمی‌کند
- AI Eligibility Rule را خودسرانه تغییر نمی‌دهد
- AI Guardrail را خودکار حذف نمی‌کند
- AI Data Access را توسعه نمی‌دهد
- AI خودش Model Promotion Rule را تغییر نمی‌دهد

## 41. Automatic Learning Cannot Change Governance

D-0005 Dataset Lifecycle را خودکار کرده است، نه Governance را.

اصل:

`Automatic Learning Pipeline ≠ Automatic Governance Evolution`

Dataset generation می‌تواند خودکار باشد؛ Policy Change همچنان نیازمند مسیر مصوب است.

## 42. Explicit Non-Decisions

BC-024 موارد زیر را تصویب نمی‌کند:

- Configuration technology
- Feature-flag product
- Policy engine
- rules engine
- database/storage model
- config file format
- approval workflow نهایی
- policy status enum نهایی
- scope inheritance algorithm
- override precedence
- rollout percentage
- emergency-change authority
- automatic rollback
- GitOps architecture
- CI/CD mechanism
- environment topology
- who exactly approves each policy domain

## 43. Open Decisions Required to Accept BC-024

1. Policy/configuration inventory
2. Policy status lifecycle
3. Effective-dating rules
4. Scope model
5. Inheritance/override rules
6. Conflict precedence
7. Owner/approver per domain
8. Change-proposal workflow
9. Impact-assessment requirements
10. Separation-of-duties rules
11. Testing requirements by change type
12. Activation rule
13. Rollout strategy
14. Rollback rule
15. Emergency-change process
16. Policy Registry requirements
17. Runtime rule-version traceability
18. Dataset impact governance
19. Reporting/restatement governance
20. Integration-change governance
21. Production activation governance
22. Audit/retention of policy history

## 44. Downstream Constraints

تا پیش از Accepted شدن BC-024:

- Technical نباید Business Ruleها را به‌صورت بی‌نسخه Hard-code کند.
- Runtime نباید Draft Policy را اجرا کند.
- Code deployment نباید Business Policy را بی‌ردپا تغییر دهد.
- Dataset automation نباید Eligibility/Consent/Data Policy را خودش تغییر دهد.
- AI نباید Policy Author/Approver باشد.
- Historical records باید Rule/Policy Version مربوط به زمان خود را قابل ردیابی نگه دارند.
- Production Activation باید به نسخه Approved و Audit قابل ردیابی باشد.
