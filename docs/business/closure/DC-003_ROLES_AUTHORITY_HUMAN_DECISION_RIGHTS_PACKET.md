# DC-003 — Roles, Authority & Human Decision Rights Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-005 + BC-013 + BC-014 + BC-022

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند. هدف، تفکیک Role، Responsibility، Authority و Permission و آماده‌سازی تصمیم‌های قابل پذیرش بدون اختراع Approval Matrix یا RBAC است.

## 1. Source-confirmed actor separation

طرح اولیه حکمرانی را بر تفکیک مسئولیت‌ها بنا می‌کند:

- **کارفرما:** تعریف نیازها و اهداف، تأمین مالی خدمات مورد توافق، نظارت بر اجرای تعهدات.
- **اپراتور نسیم:** طراحی مدل اجرایی، راهبری عملیات، توسعه شبکه سالمندیاران، تضمین کیفیت، توسعه فناوری و مدیریت شرکا.
- **Provider تخصصی:** ارائه خدمت تخصصی در دامنه همکاری.

### Candidate D-0011
سه نقش «کارفرما»، «اپراتور نسیم» و «Provider تخصصی» متمایز هستند و هیچ‌کدام به‌صورت پیش‌فرض اختیار نقش دیگر را ندارد.

**Assessment:** Source-supported; recommended for acceptance.

## 2. Source-confirmed elder-care worker role

سالمندیار در منبع «نیروی عملیاتی شبکه» و «نخستین حلقه ارتباطی سالمند» است و مسئول ارتباط، پایش، شناسایی نیاز، هدایت به خدمات تخصصی، تسهیل، هماهنگی و پیگیری است.

### Candidate D-0012
دامنه پایه سالمندیار شامل ارتباط، پایش، ثبت، هماهنگی، Referral و Follow-up است. از این مسئولیت‌ها اختیار تخصصی پزشکی/درمانی، اختیار مالی، Provider activation یا Eligibility نهایی استنتاج نمی‌شود.

**Assessment:** Source-supported boundary; recommended for acceptance.

## 3. Career path is not an authority matrix

منبع مسیر رشد زیر را معرفی می‌کند:

`سالمندیار → سالمندیار ارشد → سرپرست محله → سرپرست منطقه → مدیر شبکه شهرستان → مدیر شبکه استان`

اما Permissionهای هر سطح را تعیین نمی‌کند.

### Candidate D-0013
عنوان شغلی یا جایگاه در مسیر رشد، به‌تنهایی Permission یا Approval Right ایجاد نمی‌کند. Authority هر سطح باید در Authority Matrix مستقل تصویب شود.

**Assessment:** Governance-safe conclusion; recommended for acceptance.

## 4. System authority boundary

سامانه نسیم برای مدیریت اطلاعات، فعالیت‌ها، خدمات، ارجاعات، کیفیت، گزارش و تحلیل داده به‌کار می‌رود.

### Candidate D-0014
سامانه قواعد مصوب را اجرا و ثبت می‌کند و به‌صرف خودکار بودن Workflow، صاحب مستقل Business Decision Right نمی‌شود.

**Assessment:** Governance-derived; recommended for acceptance.

## 5. AI authority remains open

D-0004 AI را «دستیار کنار سالمند و سالمندیار» تعریف می‌کند و D-0005 حضور آن را از روز اول الزامی کرده است؛ اما Approval Rightهای AI هنوز تعیین نشده‌اند.

تا تصمیم صریح:
- AI suggestion معادل Decision نیست.
- AI output به‌خودی‌خود Official Record نیست.
- Model/Dataset automation اختیار حاکمیتی ایجاد نمی‌کند.
- Human Review و Human Owner برای تصمیم‌های حساس باید جداگانه تعیین شوند.

## 6. Human/System/AI traceability

### Candidate D-0015
Actionهای مهم نسیم باید از نظر منشأ **Human / System / AI / Automation** قابل تفکیک و Audit باشند. AI suggestion، System execution و Human decision نباید به‌صورت یک Actor مبهم ثبت شوند.

**Assessment:** Derived from D-0004/D-0005 and governance requirements; recommended for acceptance.

## 7. Elder decision rights — still open

منبع سالمندمحور است، اما موارد زیر را نهایی نمی‌کند:
- انتخاب Provider
- رد/لغو Referral
- دسترسی به پرونده
- اصلاح اطلاعات
- شکایت
- Consent mechanics
- AI interaction rights

این موارد نیازمند Product/Legal Decision جداگانه‌اند.

## 8. Family boundary

منبع فقط ارتباط منظم سالمندیار با سالمند و خانواده را تأیید می‌کند. از متن منبع نمی‌توان اختیار دسترسی به پرونده، Consent یا تصمیم‌گیری از طرف سالمند را برای خانواده نتیجه گرفت.

پس Family contact به‌تنهایی Decision Authority ایجاد نمی‌کند.

## 9. Provider authority — still open

ارائه خدمت تخصصی توسط Provider قطعی است؛ اما پذیرش/رد Referral، Completion authority، Data Access، Service exception، Complaint response و Closure authority هنوز باز هستند.

## 10. Employer authority — still open

کارفرما نقش نظارتی دارد، اما Approval روی Pilot Scope، Service Catalog، Provider، Scale Gate یا Case-level operation در منبع تعیین نشده است.

نظارت نباید خودکار به Case Authority تبدیل شود.

## 11. Supervisor authority — still open

وجود سطوح سرپرستی قطعی است، اما این موارد هنوز باید تعیین شوند:
- assignment/reassignment
- referral review
- quality review
- escalation
- complaint
- incident
- performance review
- data access
- geographic scope
- override rights

Technical نباید hierarchy را RBAC فرض کند.

## 12. Organization structure in source

طرح اولیه یک ساختار **پیشنهادی** شامل هیئت‌مدیره، مدیرعامل، معاونت‌های عملیات، توسعه شبکه، توسعه کسب‌وکار، فناوری اطلاعات، آموزش و توسعه سرمایه انسانی، مالی و اداری، کنترل کیفیت و ارزیابی، و حقوقی و قراردادها ارائه می‌کند.

چون خود منبع آن را پیشنهادی بیان کرده، این Packet آن را ساختار الزام‌آور نسیم اعلام نمی‌کند.

## 13. Governance functions that still need owners

صرف‌نظر از ساختار سازمانی نهایی، این Functionها باید Owner داشته باشند:
- Product/Business
- Operations
- Service
- Workforce
- Provider
- Quality
- Data
- AI
- Dataset/Learning
- Risk/Incident
- Financial
- Pilot/Scale
- Technology

وجود Function الزاماً به معنی ایجاد Committee یا Department جدا نیست.

## 14. Approval Matrix — blocking

برای تصمیم‌های مهم باید در ادامه مشخص شود:
- Decision subject
- Recommender
- Reviewer
- Approver
- Executor
- Informed
- Evidence
- Escalation
- Audit

Actor نهایی هر مورد هنوز باز است.

## 15. Product-owner decisions still blocking

1. Role inventory نهایی Pilot
2. Elder decision rights
3. Family/authorized-representative model
4. Caregiver Authority Matrix
5. Supervisor Authority Matrix
6. Provider Decision Rights
7. Employer Decision Rights
8. Final organization model
9. Referral Approval authority
10. Case assignment/reassignment authority
11. Complaint owner
12. Incident severity/closure authority
13. Risk Acceptance authority
14. Data Governance owner
15. AI Governance owner
16. Training Eligibility owner
17. Model Promotion/Rollback authority
18. Financial approval rights
19. Pilot/Scale Gate authority
20. Delegation/Substitution
21. Separation of Duties
22. Conflict-resolution path

## 16. Gate effect

اگر D-0011 تا D-0015 پذیرفته شوند، مرز Actorها و Accountability روشن‌تر می‌شود؛ اما Technical Entry Gate همچنان **NOT READY** می‌ماند تا Authority Matrix و Human Owners تصمیم‌های Blocking بسته شوند.

## 17. Next closure packet

**DC-004 — Elder Journey, Referral Authority, Escalation & Emergency Decision Packet**

هدف: بستن حداقل Journey عملیاتی، Referral authority، Follow-up/Closure و مرز Urgent/Emergency بدون اختراع SLA یا Medical Triage.
