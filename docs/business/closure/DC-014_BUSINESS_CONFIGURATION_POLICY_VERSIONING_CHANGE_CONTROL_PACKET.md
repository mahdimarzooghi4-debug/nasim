# DC-014 — Business Configuration, Policy Versioning & Change Control Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** D-0002 + D-0003 + D-0004 + D-0005 + BC-013 + BC-018 + BC-020 + BC-024
- **Purpose:** بستن مرزهای Business Decision، Policy/Configuration، Versioning، Activation، Change Control و Runtime Traceability بدون انتخاب Policy Engine، Feature Flag Platform یا Workflow فنی.

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند. طرح اولیه «بهبود مستمر» و اصلاح فرآیندها/استانداردها بر پایه ارزیابی و داده را تأیید می‌کند، اما مکانیزم Policy Versioning و Change Control را تعریف نمی‌کند؛ این Packet از نیازهای حاکمیتی ایجادشده در تصمیمات و Business Contractهای نسیم مشتق شده است.

## 1. Why this packet is blocking

Technical باید بتواند Business Ruleهای مصوب را اجرا کند، اما نباید:
- Rule را از Code حدس بزند
- Draft را Active فرض کند
- Policy جدید را بدون Approval اجرا کند
- داده تاریخی را با Rule جدید بازتفسیر کند
- AI/Dataset automation را صاحب Governance کند

## 2. Candidate D-0105 — Decision, configuration and runtime execution are distinct

- **تصمیم پیشنهادی:** نسیم باید میان Business Decision، Policy/Configuration و Runtime Execution تفکیک صریح داشته باشد.

`Decision ≠ Configuration ≠ Runtime Execution`

سامانه Rule مصوب را اجرا می‌کند؛ خودِ Runtime منبع مستقل Business Decision نیست.

**Assessment:** governance-derived; recommended for acceptance.

## 3. Candidate D-0106 — Draft, accepted and active are distinct

- **تصمیم پیشنهادی:** وجود یک Draft Contract یا Config به معنی Accepted یا Active بودن آن نیست.

حداقل مفاهیم:
- DRAFT
- ACCEPTED
- ACTIVE / EFFECTIVE
- SUPERSEDED / RETIRED

اینها Vocabulary کسب‌وکاری‌اند و State Machine فنی نهایی نیستند.

**Assessment:** recommended for acceptance.

## 4. Candidate D-0107 — Policies must be versioned and owned

- **تصمیم پیشنهادی:** Policyهای اثرگذار بر رفتار Business باید Version، Owner، Scope، Approval و Effective Time قابل ردیابی داشته باشند.
- **Boundary:** Data Model و Configuration Technology در Technical تعیین می‌شوند.

**Assessment:** recommended for acceptance.

## 5. Policy domains requiring versioning

حداقل Domainهای آینده:
- Target/Eligibility
- Need Taxonomy
- Service Catalog
- Need-to-Service mapping
- Referral eligibility
- Provider eligibility/mapping
- Consent/privacy
- Data classification/access
- Training Eligibility
- Dataset preparation/curation
- AI use-case policy
- AI guardrails/forbidden actions
- Human review
- KPI/metric definitions
- reporting definitions
- incident/risk rules
- workforce/training
- communication/notification
- integrations
- continuity/security governance

وجود در این فهرست به معنی نهایی‌شدن Rule نیست.

## 6. Effective dating

Policy ممکن است Accepted باشد اما:
- هنوز Effective نشده باشد
- فقط برای Pilot فعال باشد
- فقط در Geography/Organization خاص فعال باشد
- در تاریخ آینده جایگزین نسخه قبلی شود

## 7. Candidate D-0108 — Approval does not necessarily mean immediate activation

- **تصمیم پیشنهادی:** Approval و Activation دو رخداد جدا هستند و نسخه Approved فقط در Scope/Effective Time مصوب باید فعال شود.

`Approved ≠ Automatically Active`

**Assessment:** recommended for acceptance.

## 8. Historical integrity

برای تصمیم‌های تاریخی باید Rule Version زمان رخداد قابل بازسازی باشد، از جمله:
- Eligibility
- Service Catalog
- Need Taxonomy
- KPI
- Access
- Consent
- AI policy
- Training Eligibility
- Integration Contract

## 9. Candidate D-0109 — New policy must not silently rewrite history

- **تصمیم پیشنهادی:** Policy جدید نباید داده، تصمیم یا معنای تاریخی را بدون Traceable Migration/Restatement بازنویسی کند.

`New Policy ≠ Retroactive Silent Rewrite`

**Assessment:** recommended for acceptance.

## 10. Candidate D-0110 — Runtime results must be traceable to rule version

- **تصمیم پیشنهادی:** هر Runtime Result مهم که از Rule ناشی می‌شود باید بتواند به نسخه Rule/Policy مؤثر در همان زمان متصل شود.

نمونه‌ها:
- eligibility evaluation
- access decision
- referral eligibility
- KPI calculation
- notification rule
- dataset eligibility
- AI guardrail application

**Assessment:** recommended for acceptance.

## 11. Service Catalog and Taxonomy changes

تغییر در Need Taxonomy یا Service Catalog باید بتواند:
- rename
- split/merge
- deprecate
- mapping
- historical interpretation
- reporting impact
- dataset impact

را کنترل کند.

Technical نباید Code قدیمی را بی‌صدا به معنای جدید تبدیل کند.

## 12. KPI/reporting changes

تغییر numerator، denominator، inclusion/exclusion، time window، source یا target باید Versionable باشد.

گزارش تاریخی باید Metric Version را حفظ کند و دو تعریف متفاوت نباید بدون علامت در یک Trend ادغام شوند.

## 13. Training Eligibility and Dataset policy

طبق D-0005 Dataset Lifecycle خودکار است، اما Ruleهای Eligibility/Curation نباید خودکار تغییر کنند.

## 14. Candidate D-0111 — Automatic dataset generation does not change governance

- **تصمیم پیشنهادی:** Dataset Pipeline فقط Policy مصوب را اجرا می‌کند و حق تغییر Training Eligibility، Curation Rule یا Governance را ندارد.

`Automatic Dataset Generation ≠ Automatic Policy Change`

**Assessment:** directly aligned with D-0005; recommended for acceptance.

## 15. AI model and AI policy separation

دو مفهوم مستقل:
- Model Version
- AI Policy Version

تغییر Model نباید به‌صورت خودکار Forbidden Actions، Data Access، Human Review یا Service Authority را تغییر دهد.

## 16. Candidate D-0112 — Model improvement does not authorize policy change

- **تصمیم پیشنهادی:** بهبود Model یا Training Result هیچ اختیار مستقلی برای تغییر AI Policy، Guardrail یا Business Authority ایجاد نمی‌کند.

`Model Improvement ≠ Authority to Change Policy`

**Assessment:** recommended for acceptance.

## 17. Change proposal and impact assessment

Changeهای مهم باید قبل از Activation قابل بررسی باشند از منظر:
- elder safety
- operations
- workforce/provider
- legal/privacy
- data/security
- integrations
- reporting/KPI
- AI/dataset
- continuity
- economics

Workflow دقیق در Technical/Delivery Governance تعیین می‌شود.

## 18. Candidate D-0113 — Governance-sensitive changes require approval before activation

- **تصمیم پیشنهادی:** Changeهای اثرگذار بر Business Meaning، Data Access، AI Guardrails، Training Eligibility، Risk/Financial/Scale Rules باید پیش از Activation Approval صریح داشته باشند.

`Configured ≠ Approved ≠ Active`

**Assessment:** recommended for acceptance.

## 19. Scope and override — blocking

Business هنوز باید تعیین کند:
- global vs organization vs geography vs pilot scope
- inheritance
- precedence
- overrideable policies
- override authority
- duration
- expiry
- audit

Technical نباید precedence را خودش اختراع کند.

## 20. Candidate D-0114 — Overrides must be bounded and auditable

- **تصمیم پیشنهادی:** هر Override مجاز باید Scope، Actor، Reason، Duration/Expiry و Audit داشته باشد؛ Override نامحدود و بی‌ردپا مجاز نیست.

**Assessment:** recommended for acceptance.

## 21. Policy conflict — blocking

Conflict Resolution Rule برای مواردی مانند:
- global vs organization
- old vs new effective version
- service vs provider
- privacy vs operational convenience
- AI policy vs data-access policy

باید Business-approved باشد.

## 22. Rollout and rollback

Policy Change حساس باید در صورت نیاز بتواند Rollout محدود و Rollback کنترل‌شده داشته باشد.

Rollback باید:
- previous valid version
- effective time
- impacted records
- reconciliation
- audit
- dataset/reporting impact

را روشن کند.

## 23. Candidate D-0115 — Sensitive policy changes require rollback consideration

- **تصمیم پیشنهادی:** برای Changeهای حساس، Rollback/Recovery Impact باید پیش از Activation بررسی و ثبت شود؛ عدم امکان Rollback نیز باید صریحاً معلوم باشد.

**Assessment:** recommended for acceptance.

## 24. Code and policy boundary

Technical Configuration مثل timeout یا replica count لزوماً Business Policy نیست.

اما اگر Code Change Business Meaning را تغییر دهد، باید Policy/Decision مرتبط قابل ردیابی باشد.

## 25. Candidate D-0116 — Code deployment must not silently redefine business policy

- **تصمیم پیشنهادی:** Deploy یا Code Change نباید بدون Business Decision/Policy Trace رفتار Business Rule را تغییر دهد.

`Code Deployment ≠ Silent Business Policy Change`

**Assessment:** aligned with D-0003; recommended for acceptance.

## 26. Production activation

نسخه‌ای که در Production فعال می‌شود باید همان نسخه Approved برای همان Scope باشد.

Stage/Production policy differences باید قابل مشاهده باشند و Activation Production باید Audit شود.

## 27. AI cannot author or approve governance

AI ممکن است Change Draft یا Impact Summary تولید کند، اما نباید:
- Policy را Approve کند
- Eligibility Rule را تغییر دهد
- Guardrail را حذف کند
- Access را توسعه دهد
- Model Promotion Rule را تغییر دهد

## 28. Candidate D-0117 — Automatic learning cannot evolve governance automatically

- **تصمیم پیشنهادی:** Learning Pipeline، AI یا Model Training حق Evolution خودکار Governance را ندارد.

`Automatic Learning Pipeline ≠ Automatic Governance Evolution`

**Assessment:** aligned with D-0005; recommended for acceptance.

## 29. Emergency change — still open

Business باید تعیین کند:
- Emergency Change چیست
- چه Actorی مجاز است
- حداقل Approval چیست
- مدت موقت
- Post-review
- formalization/rollback

هیچ Break-glass Change Rule نهایی در این Packet تصویب نمی‌شود.

## 30. Policy registry — business need

نسیم در آینده نیازمند Registry منطقی Policyهاست که حداقل:
- ID/domain
- version
- status
- scope
- owner/approver
- effective dates
- dependency
- supersession
- audit reference

را نگه دارد.

این نیاز، Technology خاصی را تصویب نمی‌کند.

## 31. Product-owner decisions still blocking

1. policy status lifecycle نهایی
2. Policy owner/approver matrix
3. activation authority
4. scope model
5. inheritance/precedence
6. override policy
7. conflict resolution
8. change classifications
9. impact-assessment depth
10. testing requirement by change type
11. rollout rules
12. rollback rules
13. emergency-change path
14. restatement/migration rules
15. policy registry ownership
16. production activation authority
17. separation-of-duties requirements

## 32. Candidates ready for acceptance

- **D-0105:** Decision ≠ Configuration ≠ Runtime Execution.
- **D-0106:** Draft ≠ Accepted ≠ Active.
- **D-0107:** Policies are versioned and owned.
- **D-0108:** Approved ≠ Automatically Active.
- **D-0109:** New Policy ≠ Retroactive Silent Rewrite.
- **D-0110:** Runtime result traces to rule version.
- **D-0111:** Automatic Dataset Generation ≠ Automatic Policy Change.
- **D-0112:** Model Improvement ≠ Authority to Change Policy.
- **D-0113:** Configured ≠ Approved ≠ Active.
- **D-0114:** Overrides are bounded/auditable.
- **D-0115:** Sensitive changes require rollback consideration.
- **D-0116:** Code deployment must not silently redefine Business Policy.
- **D-0117:** Automatic Learning Pipeline ≠ Automatic Governance Evolution.

## 33. Gate effect

پذیرش D-0105 تا D-0117 چارچوب Change Governance را روشن می‌کند، اما Technical Entry Gate تا تعیین **Policy Owner/Approver Matrix، Activation Authority، Scope/Override/Precedence و Emergency Change Rule** همچنان **NOT READY** می‌ماند.

## 34. Next closure packet

**DC-015 — Business Exit Review, Decision Closure Matrix & Technical Entry Recommendation**
