# BC-011 — Pilot Model, Success Criteria & Go/No-Go Governance

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0005 + BC-009 + BC-010
- **Depends on:** BC-001, BC-002, BC-003, BC-004, BC-005, BC-006, BC-007, BC-008, BC-009, BC-010

> این سند مدل کسب‌وکاری پایلوت نسیم را تعریف می‌کند، اما هیچ شهر، تعداد سالمند، مدت، بودجه، Threshold یا Go/No-Go Rule عددی که در منبع اولیه تعیین نشده باشد اختراع نمی‌کند.

## 1. Pilot Role

در طرح مبنا، پایلوت بخشی از مرحله «ایجاد زیرساخت» است و قبل از توسعه گسترده شبکه قرار می‌گیرد.

هدف پایلوت فقط نمایش نرم‌افزار نیست. پایلوت باید امکان اعتبارسنجی هم‌زمان این اجزا را فراهم کند:

- مدل سالمندیاری محله‌محور
- Journey سالمند
- نظام ارجاع
- همکاری با Providerها
- کیفیت خدمت
- عملکرد سالمندیار
- سامانه نسیم
- Data Governance
- مدل اقتصادی اولیه
- AI داخلی از روز اول
- چرخه خودکار Dataset
- Governance و آمادگی توسعه

## 2. Day-one AI Requirement

بر اساس D-0005، پایلوت نسیم باید از روز اول شامل AI داخلی باشد.

بنابراین پایلوتی که AI را بعداً اضافه کند، نماینده محصول هدف نسیم نیست.

حداقل از منظر Business، پایلوت باید بتواند نشان دهد:

- AI برای Use Caseهای مصوب سالمند قابل استفاده است
- AI برای Use Caseهای مصوب سالمندیار قابل استفاده است
- خروجی AI از تصمیم انسانی قابل تفکیک است
- Human Review در موارد لازم ثبت می‌شود
- Datasetهای Versioned به‌صورت خودکار از داده‌های مجاز ساخته/به‌روزرسانی می‌شوند
- Dataset lineage قابل ردیابی است
- کیفیت و رخدادهای AI قابل پایش است

## 3. Pilot Hypothesis Categories

پایلوت باید حداقل این دسته فرضیه‌ها را اعتبارسنجی کند:

### A. Elder Value
آیا مدل نسیم برای سالمند دسترسی، پیگیری، هماهنگی و تجربه خدمت معنادار ایجاد می‌کند؟

### B. Elder-Care Worker Model
آیا سالمندیار می‌تواند نقش پایش، ثبت، ارجاع و پیگیری را با کیفیت و ظرفیت عملیاتی قابل قبول انجام دهد؟

### C. Referral Model
آیا نیاز از شناسایی تا ارجاع، ارائه خدمت و پیگیری قابل اجرا و قابل ردیابی است؟

### D. Provider Network
آیا Providerهای مورد نیاز قابل جذب، فعال، هماهنگ و پایش هستند؟

### E. Technology
آیا سامانه می‌تواند عملیات واقعی را بدون اتکا به فرآیندهای خارج از سیستم که Product آنها را رسمی نکرده است پشتیبانی کند؟

### F. Data & Governance
آیا داده مورد نیاز با Provenance، دسترسی و Governance قابل مدیریت است؟

### G. AI Assistance
آیا AI در نقش دستیار برای سالمند و سالمندیار ارزش ایجاد می‌کند بدون اینکه مرز مسئولیت انسانی را مخدوش کند؟

### H. Learning System
آیا سیستم می‌تواند داده مجاز جدید را به‌صورت خودکار به Dataset Version جدید تبدیل کند و Lineage را حفظ کند؟

### I. Economics
آیا Cost Structure، Funding و Unit Economics قابل اندازه‌گیری و تحلیل هستند؟

### J. Governance & Quality
آیا شبکه می‌تواند کیفیت، شکایت، رخداد، ارزیابی و تصمیم توسعه را به‌صورت کنترل‌شده مدیریت کند؟

## 4. Pilot Scope Must Be Explicit

قبل از شروع پایلوت باید حداقل این موارد Business-approved شوند:

- جامعه هدف
- Eligibility
- محدوده جغرافیایی
- تعداد سالمندان
- تعداد سالمندیاران
- Service Catalog فاز پایلوت
- Provider scope
- Journey و Referral rules
- Role/Authority matrix
- Data/Consent rules
- AI use cases
- Dataset eligibility rules
- Quality/KPI definitions
- Budget/Funding
- مدت پایلوت
- Decision owner

تا تعیین این موارد، «شروع پایلوت» یک تصمیم کامل کسب‌وکاری محسوب نمی‌شود.

## 5. Pilot Baseline

قبل از اولین روز عملیاتی باید Baseline قابل ثبت باشد.

Candidate baseline domains:

- تعداد سالمندان واجد شرایط
- وضعیت اولیه پرونده‌ها
- ظرفیت سالمندیاران
- ظرفیت Providerها
- وضعیت Service Catalog
- کیفیت و کامل بودن داده اولیه
- وضعیت فنی سامانه
- AI model/version فعال
- Dataset baseline
- منابع و هزینه‌های آغازین

فیلدها و مقادیر دقیق هنوز تصمیم نشده‌اند.

## 6. Evidence Model

هر ادعای موفقیت پایلوت باید به Evidence متصل باشد.

حداقل دسته‌های Evidence:

- operational records
- service/referral records
- satisfaction evidence
- quality/audit evidence
- workforce evidence
- provider evidence
- financial evidence
- incident/risk evidence
- AI quality evidence
- Dataset/version lineage
- governance decisions

Dashboard به‌تنهایی جای Evidence پایه را نمی‌گیرد.

## 7. Success Criteria Framework

Success Criteria نهایی باید چندبعدی باشد و فقط Coverage یا تعداد فعالیت را نسنجد.

دسته‌های اصلی:

1. Operational readiness
2. Service quality
3. Elder/family satisfaction
4. Elder-care-worker readiness
5. Provider readiness
6. Technology readiness
7. Data quality/governance readiness
8. AI readiness
9. Automatic Dataset lifecycle readiness
10. Economic viability
11. Risk/incident acceptability
12. Governance readiness

برای هر دسته باید بعداً Metric، Target و Evidence تعیین شود.

## 8. AI Success Boundary

موفقیت AI در پایلوت نباید صرفاً با «وجود AI» سنجیده شود.

باید در آینده برای AI حداقل این حوزه‌ها Metric داشته باشند:

- usefulness
- correctness
- human acceptance/rejection
- override/edit rate
- escalation
- unsafe/harmful output
- availability
- data-quality dependency
- version traceability

Thresholdها هنوز باز هستند.

## 9. Dataset Lifecycle Success Boundary

برای D-0005، پایلوت باید بتواند نشان دهد که:

- داده جدید تولید می‌شود
- Eligibility Rule روی آن اجرا می‌شود
- داده واجد شرایط وارد Pipeline می‌شود
- Dataset جدید یا Version جدید ساخته می‌شود
- Lineage ثبت می‌شود
- Dataset برای Training/Evaluation قابل استفاده است

این چرخه باید خودکار باشد؛ اما مقدار Trigger/Cadence و آستانه ساخت Version جدید هنوز در Technical تعیین خواهد شد.

## 10. Pilot Incident Model

پایلوت باید بتواند رخدادها را ثبت و برای تصمیم توسعه لحاظ کند.

Candidate domains:

- service failure
- referral failure
- provider failure
- data/privacy incident
- security incident
- AI incident
- dataset pipeline failure
- operational overload
- complaint
- financial/control issue

Severity model هنوز تصمیم نشده است.

## 11. Go / Conditional Go / No-Go — DRAFT FRAME

برای پایان پایلوت، مدل تصمیم می‌تواند حداقل سه خروجی داشته باشد:

- **GO** — اجازه ورود به مرحله توسعه
- **CONDITIONAL GO** — توسعه محدود مشروط به اصلاحات مشخص
- **NO-GO** — توقف توسعه و بازگشت به اصلاح

این Vocabulary در این مرحله DRAFT است و هنوز Decision Rule نهایی نیست.

## 12. Scale Gate Inputs

مطابق BC-010 و طرح اولیه، تصمیم توسعه باید حداقل بر پایه این شواهد باشد:

- KPI evidence
- stakeholder satisfaction
- operational readiness
- service quality
- workforce readiness
- provider readiness
- economic evidence
- data/governance readiness
- AI readiness
- dataset lifecycle evidence
- risk/incidents

هیچ‌کدام نباید به‌تنهایی جای کل Gate را بگیرد.

## 13. Decision Authority — Open

طرح اولیه مالک نهایی Go/No-Go را تعیین نکرده است.

باید مشخص شود:

- چه کسی Recommendation می‌دهد
- چه کسی Evidence را Review می‌کند
- چه کسی تصمیم نهایی می‌گیرد
- آیا کارفرما Approval لازم دارد
- آیا نسیم Approval داخلی جدا دارد
- Conditional Go را چه کسی می‌بندد
- اختلاف نظر چگونه حل می‌شود

تا تصمیم صریح، Go/No-Go نباید خودکار باشد.

## 14. AI Has No Final Scale Authority

AI می‌تواند در آینده شواهد را خلاصه یا تحلیل کند، اما:

- GO/NO-GO را نهایی نمی‌کند
- Threshold را تغییر نمی‌دهد
- Evidence را به‌تنهایی معتبر نمی‌کند
- Incident را خودکار بی‌اثر نمی‌کند

تصمیم Scale Gate یک تصمیم حاکمیتی انسانی باقی می‌ماند مگر بعداً خلاف آن صریحاً تصویب شود.

## 15. Pilot Change Control

اگر در طول پایلوت یکی از موارد اصلی تغییر کند، باید اثر آن بر اعتبار نتایج ثبت شود، از جمله:

- جامعه هدف
- Service Catalog
- Workflow
- Provider scope
- KPI definition
- AI model/version
- Dataset policy
- Pricing/Funding
- Geography

روش رسمی Change Control هنوز باید تعریف شود.

## 16. Exit Evidence Package

پیش از Scale Gate، باید یک Evidence Package قابل Review وجود داشته باشد که حداقل شامل:

- Scope اجراشده
- تغییرات نسبت به Baseline
- KPI results
- Quality findings
- Satisfaction findings
- Financial findings
- Workforce findings
- Provider findings
- Data governance findings
- AI findings
- Dataset lifecycle findings
- Risks/incidents
- Open issues
- Recommendation

باشد.

قالب نهایی این Package هنوز تعیین نشده است.

## 17. Explicit Non-Decisions

BC-011 موارد زیر را تصویب نمی‌کند:

- محل پایلوت
- تعداد سالمندان
- تعداد سالمندیاران
- مدت پایلوت
- بودجه
- Service Catalog پایلوت
- KPI Targetها
- Go/No-Go Threshold
- AI quality threshold
- Dataset cadence
- Training cadence
- Model promotion rule
- Decision owner نهایی
- Conditional Go conditions

## 18. Open Decisions Required to Accept BC-011

1. Pilot geography
2. Pilot population
3. Pilot size
4. Pilot duration
5. Service Catalog
6. Provider scope
7. Operational workflow
8. Role/authority matrix
9. AI use cases
10. Dataset eligibility/pipeline policy
11. KPI catalog
12. KPI targets/thresholds
13. Budget/funding
14. Incident severity model
15. Go/Conditional-Go/No-Go rules
16. Scale Gate owner
17. Evidence Package format
18. Change-control rule

## 19. Downstream Constraints

تا پیش از Accepted شدن BC-011:

- Technical نباید Pilot Size یا Duration را فرض کند.
- Backlog نباید Scope پایلوت را بدون Business approval تثبیت کند.
- Deployment plan نباید AI را از نسخه پایلوت حذف کند.
- Dataset automation باید جزء Day-one readiness باشد.
- Dashboard نباید Go/No-Go را خودکار اعلام کند.
- توسعه شبکه نباید بدون Scale Gate مصوب آغاز شود.
