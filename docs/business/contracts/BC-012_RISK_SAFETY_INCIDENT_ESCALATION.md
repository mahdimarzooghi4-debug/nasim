# BC-012 — Risk, Safety, Incident & Escalation Governance

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-003 + BC-006 + BC-007 + BC-008 + BC-010 + BC-011
- **Depends on:** BC-003, BC-005, BC-006, BC-007, BC-008, BC-010, BC-011

> این سند چارچوب کسب‌وکاری مدیریت ریسک، ایمنی، Incident و Escalation در نسیم را تعریف می‌کند. Severity، SLA، مسیرهای اضطراری، مالک نهایی هر Incident و Thresholdهای Escalation هنوز تصمیم نشده‌اند و نباید در Technical یا Code اختراع شوند.

## 1. Risk Governance Principle

طرح مبنا مدیریت ریسک را جزء ارکان حکمرانی شبکه می‌داند و تأکید می‌کند که ریسک‌ها باید در تمام مراحل طراحی، اجرا، توسعه و بهره‌برداری شناسایی، ارزیابی و مدیریت شوند.

نسیم باید بتواند ریسک را از رخداد واقعی تفکیک کند:

- **Risk:** احتمال وقوع یک وضعیت نامطلوب
- **Incident:** رخداد واقعی که نیازمند ثبت، رسیدگی و پیگیری است
- **Escalation:** انتقال مسئله به سطح مسئولیت بالاتر طبق Rule مصوب
- **Emergency:** وضعیت فوری مرتبط با ایمنی/سلامت که مسیر عملیاتی مستقل نیاز دارد

این واژگان Frame کسب‌وکاری هستند و Workflow نهایی هنوز تعیین نشده است.

## 2. Source-confirmed Risk Families

طرح اولیه پنج خانواده اصلی ریسک را مشخص می‌کند:

### A. Strategic Risk
نمونه‌های منبع:
- تغییر سیاست‌های کلان رفاه و حمایت اجتماعی
- تغییر نیازهای جامعه سالمندان
- ورود بازیگران جدید
- تغییرات اقتصادی و اجتماعی

### B. Operational Risk
نمونه‌های منبع:
- کمبود نیروی انسانی متخصص
- کاهش کیفیت خدمات
- اختلال در فرآیندهای اجرایی
- ناهماهنگی میان شرکای شبکه
- ضعف در نظام ارجاع

### C. Financial Risk
نمونه‌های منبع:
- تأخیر در دریافت مطالبات
- افزایش هزینه‌های عملیاتی
- کاهش درآمدهای قراردادی
- محدودیت منابع توسعه‌ای

### D. Legal & Regulatory Risk
طرح اولیه بر تنظیم قراردادها، فرآیندها، حفاظت از اطلاعات سالمندان و همکاری شرکا مطابق قوانین و مقررات تأکید دارد.

### E. Technology Risk
طرح اولیه بر این موارد تأکید می‌کند:
- امنیت اطلاعات
- پایداری سامانه
- حفاظت از داده سالمندان
- پشتیبان‌گیری
- کنترل دسترسی
- پایش امنیت

## 3. Elder Safety Boundary

نسیم با سالمندان و داده‌های مرتبط با سلامت، وضعیت اجتماعی و خدمات آنها سروکار دارد.

برای طراحی آینده باید میان حداقل این وضعیت‌ها تمایز وجود داشته باشد:

- Service issue
- Welfare/safety concern
- Health-related concern
- Urgent situation
- Emergency situation
- Complaint
- Operational incident

طرح اولیه فقط آموزش «مدیریت شرایط اضطراری» را برای سالمندیار ذکر می‌کند و Emergency Workflow نهایی را تعریف نکرده است.

بنابراین BC-012 هیچ تعهد 24/7، Triage پزشکی، شماره تماس یا SLA اضطراری را تصویب نمی‌کند.

## 4. Operational Incident Domains

سامانه و عملیات آینده باید بتوانند Incidentهای حداقل این حوزه‌ها را از هم تفکیک کنند:

- Elder service failure
- Referral failure
- Provider failure
- Elder-care-worker operational issue
- Quality failure
- Complaint-related incident
- System outage
- Security incident
- Data/privacy incident
- AI incident
- Dataset pipeline incident
- Governance/control failure
- Financial/control incident

این دسته‌ها Taxonomy نهایی نیستند.

## 5. Referral & Service Escalation

BC-003 وجود ارجاع و پیگیری را تثبیت کرده، اما Escalation Rule هنوز باز است.

برای هر Service/Referral آینده باید تصمیم شود:

- چه چیزی Escalation را Trigger می‌کند
- چه کسی Escalate می‌کند
- مقصد Escalation چیست
- مهلت پاسخ چیست
- آیا Referral در حین Escalation متوقف می‌شود
- آیا Provider تغییر می‌کند
- آیا سالمند/خانواده مطلع می‌شوند
- چه Evidence برای بستن Escalation لازم است

## 6. Provider Incident Governance

همسو با BC-008، Incidentهای Provider می‌توانند شامل موضوعاتی مانند این باشند:

- عدم پذیرش یا عدم پاسخ
- عدم انجام خدمت
- تأخیر
- نقص کیفیت
- شکایت
- تکرار خطا
- عدم ظرفیت
- نقض الزامات داده/محرمانگی
- تعلیق یا خاتمه همکاری

Rule نهایی برای Suspension، Re-routing، Remediation یا Contract action هنوز تعیین نشده است.

## 7. Data & Privacy Incident Governance

همسو با BC-007، Data Incident باید از سایر Incidentها قابل تفکیک باشد.

موضوعات طراحی آینده حداقل شامل:

- دسترسی غیرمجاز
- اشتراک داده خارج از Purpose
- ورود داده غیرمجاز به Dataset
- نقص Provenance
- شکست Lineage
- حذف یا نگهداری نامعتبر
- Consent/authorization mismatch
- افشای ناخواسته
- Dataset contamination

Severity، Notification و Remediation Rule هنوز باز هستند.

## 8. AI Incident Governance

با توجه به D-0004 و D-0005، AI از روز اول عملیاتی است؛ بنابراین AI Incident نیز از روز اول بخشی از Incident Management نسیم است.

Candidate AI incident domains:

- خروجی نادرست یا گمراه‌کننده
- خروجی نامناسب/ناایمن
- پیشنهاد خارج از حدود اختیار AI
- استفاده از داده خارج از مجوز Runtime
- ثبت خروجی AI به‌عنوان تصمیم انسانی بدون مسیر معتبر
- خطای Model/Runtime
- عدم دسترس‌پذیری AI
- خطای Version/Provenance
- رفتار غیرمنتظره پس از تغییر Model Version

اینها Candidate domain هستند و Severity نهایی ندارند.

## 9. Dataset Pipeline Incident Governance

به دلیل D-0005، چرخه خودکار Dataset از روز اول فعال است.

بنابراین Pipeline باید بتواند رخدادهایی مانند اینها را شناسایی و قابل رسیدگی کند:

- ورود داده‌ای که Eligibility Rule را پاس نکرده است
- از دست رفتن Dataset lineage
- ساخت Dataset ناقص یا خراب
- Duplicate/incorrect inclusion
- خطای Preparation/Curation
- Versioning failure
- استفاده از Dataset اشتباه در Training/Evaluation
- عدم تطابق Source Window

جزئیات Detection و Recovery در Technical تعیین می‌شوند.

## 10. Automatic Dataset ≠ Automatic Risk Acceptance

خودکار بودن Dataset Lifecycle نباید باعث شود خطاهای Pipeline یا داده به‌صورت خودکار پذیرفته شوند.

اصل:

`Automation does not remove governance accountability.`

Dataset generation می‌تواند خودکار باشد، اما Incident، Audit و Quality Gate باید قابل اعمال باقی بمانند.

## 11. AI Fail-safe Boundary

همسو با BC-006:

در صورت خطای AI، نبود مدل معتبر، نبود داده کافی یا شرایطی که AI قادر به پاسخ معتبر نیست:

- نباید تصمیم رسمی جعل شود
- نباید پرونده رسمی بدون مسیر معتبر تغییر کند
- نباید AI به‌صورت پنهان جای تصمیم انسانی را بگیرد

رفتار دقیق Fail-safe و Fallback هنوز باید تصمیم شود.

## 12. Incident Lifecycle — DRAFT FRAME

برای طراحی آینده، Incident Lifecycle باید بتواند حداقل این مراحل مفهومی را پوشش دهد:

`Detected → Logged → Assessed → Assigned → Handled/Contained → Reviewed → Closed → Follow-up`

این فقط Frame تحلیلی است و State Machine نهایی محسوب نمی‌شود.

## 13. Incident Record — DRAFT REQUIREMENT

هر Incident آینده باید بتواند حداقل این اطلاعات را نگه دارد:

- Incident ID
- Domain/type
- Related elder/case/referral/provider/model/dataset در صورت وجود
- Detection time
- Reporting actor/source
- Description
- Severity در صورت تعریف
- Owner
- Actions taken
- Escalations
- Evidence
- Resolution
- Closure decision
- Follow-up/remediation
- Audit trail

فیلدهای نهایی در Technical و Contractهای تکمیلی تعیین می‌شوند.

## 14. Severity & Priority — Open

طرح اولیه Severity Model تعریف نکرده است.

برای Incident و Emergency باید بعداً مشخص شود:

- Levels
- Definition
- Response expectation
- Escalation owner
- Notification rule
- Closure authority
- Reopen rule

هیچ Level یا زمان عددی در BC-012 تصویب نمی‌شود.

## 15. Complaint vs Incident

شکایت و Incident یکی فرض نمی‌شوند.

یک Complaint ممکن است:
- فقط بازخورد باشد
- نیازمند بررسی کیفیت باشد
- Incident واقعی را آشکار کند

Rule تبدیل Complaint به Incident یا Escalation هنوز باید تعیین شود.

## 16. Human Authority

AI و سامانه می‌توانند در آینده Incident را Detect یا Flag کنند، اما تا تصمیم صریح:

- AI Incident را نهایی نمی‌بندد
- AI Severity نهایی را تعیین نمی‌کند
- AI Suspension نهایی Provider را اعمال نمی‌کند
- AI Emergency decision نهایی نمی‌گیرد
- AI Risk acceptance انجام نمی‌دهد

Owner انسانی هر حوزه باید در Authority Matrix آینده تعیین شود.

## 17. Risk Register — DRAFT BUSINESS NEED

برای Governance آینده، نسیم باید بتواند Risk Register نسخه‌دار داشته باشد که حداقل شامل:

- Risk
- Category
- Cause
- Potential impact
- Owner
- Mitigation
- Monitoring evidence
- Review status
- Related incident history

باشد.

Scoring formula و Risk Appetite هنوز تعیین نشده‌اند.

## 18. Risk to Scale Gate

همسو با BC-010 و BC-011، Risk/Incident evidence باید ورودی تصمیم توسعه باشد.

وجود Incident لزوماً به معنی No-Go نیست و نبود Incident ثبت‌شده نیز لزوماً به معنی ایمنی نیست.

Business آینده باید تعیین کند:

- چه Incidentهایی Gate-blocking هستند
- چه Riskهایی نیازمند Remediation هستند
- چه شرایطی Conditional Go ایجاد می‌کند
- چه کسی Risk Acceptance را امضا می‌کند

## 19. Continuous Improvement Link

طرح اولیه بهبود مستمر را بر پایه ارزیابی و داده می‌داند.

بنابراین Incident و Risk Finding باید بتوانند در آینده به این خروجی‌ها متصل شوند:

- Process change
- Service standard change
- Training update
- Provider remediation
- Product change
- Data rule change
- AI guardrail change
- Monitoring improvement

Change approval process هنوز باید تعریف شود.

## 20. Explicit Non-Decisions

BC-012 موارد زیر را تصویب نمی‌کند:

- Incident Severity Levels
- Emergency SLA
- 24/7 operation
- Medical triage protocol
- Emergency contact routing
- Incident response time
- Risk scoring formula
- Risk appetite
- Provider suspension threshold
- AI shutdown threshold
- Dataset rollback threshold
- Notification recipients
- Regulatory reporting rule
- Compensation/remedy formula

## 21. Open Decisions Required to Accept BC-012

1. Risk taxonomy نهایی
2. Incident taxonomy نهایی
3. Severity model
4. Emergency workflow
5. Escalation matrix
6. Incident ownership
7. Complaint-to-incident rule
8. Provider incident/remediation policy
9. Data/privacy incident policy
10. AI incident policy
11. Dataset incident policy
12. Fail-safe/fallback rules
13. Notification rules
14. Closure/reopen rules
15. Risk register ownership
16. Risk acceptance authority
17. Gate-blocking incident rules
18. Post-incident improvement workflow

## 22. Downstream Constraints

تا پیش از Accepted شدن BC-012:

- Technical نباید Severity یا Escalation SLA را اختراع کند.
- Emergency workflow نباید از UI یا Service Catalog حدس زده شود.
- AI نباید Incident closure یا Risk acceptance نهایی انجام دهد.
- Dataset automation باید دارای قابلیت Audit و Incident detection قابل طراحی باشد.
- Provider suspension نباید فقط از یک Score خودکار نتیجه شود.
- Scale Gate باید Risk/Incident evidence را قابل دریافت و Review کند.
