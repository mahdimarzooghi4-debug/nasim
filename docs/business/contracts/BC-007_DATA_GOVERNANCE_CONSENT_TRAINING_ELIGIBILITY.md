# BC-007 — Data Governance, Consent & Training Eligibility

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + تصمیم D-0004 + BC-006
- **Depends on:** BC-001, BC-003, BC-004, BC-005, BC-006

> این سند چارچوب کسب‌وکاری داده در نسیم را تعریف می‌کند. طبقه‌بندی حقوقی نهایی، مبنای قانونی پردازش، Retention Period، Consent UX و جزئیات فنی Security هنوز تصمیم نشده‌اند.

## 1. Data Governance Objective

نسیم یک نظام داده‌محور است و سامانه آن برای مدیریت اطلاعات سالمندان، فعالیت سالمندیاران، خدمات، ارجاعات، کیفیت، گزارش و تحلیل داده طراحی می‌شود.

با اضافه شدن هوش مصنوعی داخلی، داده دو مصرف متفاوت پیدا می‌کند:

1. **Operational Use** — برای ارائه و مدیریت خدمت
2. **Learning Use** — برای آموزش، ارزیابی و بهبود AI

این دو مصرف نباید به‌صورت پیش‌فرض یکی فرض شوند.

## 2. Source-confirmed Operational Data Domains

بر اساس طرح اولیه، حداقل حوزه‌های داده عملیاتی شامل موارد زیر هستند:

- اطلاعات سالمند
- پرونده اولیه سالمند
- ارتباطات و پیگیری‌های سالمندیار
- تغییرات جسمی
- تغییرات روانی
- تغییرات اجتماعی
- نیازهای ثبت‌شده
- ارجاعات
- خدمات ارائه‌شده
- وضعیت پیگیری خدمت
- رضایت سالمند
- فعالیت سالمندیار
- داده‌های کیفیت خدمات
- داده‌های گزارش و ارزیابی
- داده‌های عملکرد شبکه

این فهرست Data Schema نهایی نیست.

## 3. Additional AI-related Data Domains

برای AI ممکن است در آینده داده‌های دیگری تولید شود، از جمله:

- AI prompt/input
- AI output
- پیشنهاد AI
- پذیرش/رد/ویرایش پیشنهاد توسط انسان
- AI model/version identifier
- Evaluation result
- Training dataset membership
- Training/evaluation lineage

وجود این حوزه‌ها به معنی تصویب ذخیره دائمی همه آنها نیست.

## 4. Data Classification — DRAFT FRAME

برای ادامه طراحی، داده‌ها باید حداقل از این ابعاد قابل طبقه‌بندی باشند:

### A. Identity & Contact
اطلاعات هویتی و تماس.

### B. Health-related
اطلاعات جسمی، روانی، مراقبتی و سایر داده‌های مرتبط با سلامت.

### C. Social & Family
اطلاعات خانوادگی، اجتماعی، تنهایی، حمایت و شرایط زندگی.

### D. Service & Referral
نیاز، ارجاع، Provider، خدمت، پیگیری و نتیجه خدمت.

### E. Workforce
فعالیت، آموزش، ارزیابی و عملکرد سالمندیار و سایر نیروها.

### F. Operational & Quality
کیفیت، SLA در صورت تصویب آینده، شکایت، رضایت و عملکرد شبکه.

### G. AI Interaction
ورودی، خروجی و بازخورد مرتبط با AI.

### H. Governance & Audit
Consent، Access، Approval، Change History و Audit Trail.

این طبقه‌بندی فقط Frame کسب‌وکاری است و سطح حساسیت یا ضوابط قانونی هر کلاس هنوز باید تعیین شود.

## 5. Purpose Limitation

هر Data Class باید Purpose مشخص داشته باشد.

حداقل Purposeهای آینده:

- ارائه خدمت
- پیگیری خدمت
- مدیریت شبکه
- کنترل کیفیت
- گزارش مدیریتی
- ارزیابی اثر
- آموزش نیروی انسانی
- AI assistance
- AI training
- AI evaluation

مجوز استفاده از داده برای یک Purpose نباید خودکار به همه Purposeهای دیگر تعمیم داده شود.

## 6. Training Eligibility Principle — DRAFT

اصل پیشنهادی BC-007:

`Operationally Available ≠ Training Eligible`

وجود یک داده در Production به‌تنهایی برای ورود آن به Training Dataset کافی نیست.

هر داده برای Training باید از یک Rule صریح عبور کند که حداقل این موارد را مشخص کند:

- Data class
- Purpose
- Eligibility condition
- Required preparation
- Consent / legal basis
- Exclusion rule
- Quality requirement
- Dataset version
- Approval / governance owner

## 7. Candidate Training Eligibility States — DRAFT

برای طراحی بعدی، هر Data Item یا Data Class می‌تواند از منظر Training یکی از وضعیت‌های زیر داشته باشد:

- **NOT_ASSESSED**
- **INELIGIBLE**
- **ELIGIBLE_WITH_PREPARATION**
- **ELIGIBLE**
- **EXCLUDED**

این Stateها فقط Vocabulary پیشنهادی هستند و State Machine فنی نهایی نیستند.

## 8. Data Preparation / Curation

BC-006 مسیر زیر را به‌عنوان چارچوب Draft معرفی کرده است:

`Production Data → Eligible Data → Prepared/Curated Dataset → Training → Evaluation → Approved Model Version → Production`

در BC-007، «Prepared/Curated» به معنی این است که قبل از Training باید فرآیندی برای حداقل موارد زیر قابل تعریف باشد:

- حذف داده نامعتبر
- کنترل کیفیت
- حذف یا کاهش داده‌های غیرضروری
- De-identification در صورت نیاز
- Label/annotation در صورت نیاز
- جلوگیری از ورود داده‌هایی که نباید در Dataset باشند
- ثبت Dataset version و lineage

روش دقیق این عملیات هنوز تصمیم نشده است.

## 9. Consent & Legal Basis — Open Contract

منبع اولیه فقط بر حفاظت از اطلاعات سالمندان و رعایت قوانین تأکید می‌کند و مدل Consent را تعیین نکرده است.

بنابراین هنوز باید جداگانه مشخص شود:

- Consent برای ثبت داده چگونه است
- Consent برای اشتراک داده با Provider چگونه است
- Consent یا مبنای قانونی AI assistance چیست
- Consent یا مبنای قانونی Training چیست
- Withdrawal چگونه عمل می‌کند
- اثر Withdrawal بر داده‌های قبلی و Datasetهای ساخته‌شده چیست
- در صورت وجود نماینده مجاز، Authority او چگونه احراز می‌شود

BC-007 هیچ مدل حقوقی را از پیش فرض نمی‌کند.

## 10. Minimum Access Principle — DRAFT

دسترسی هر Actor باید به داده مورد نیاز نقش و Purpose محدود شود.

این اصل به معنی RBAC نهایی نیست، اما Technical آینده باید بتواند حداقل میان این حوزه‌ها تفکیک ایجاد کند:

- سالمند
- نماینده مجاز در صورت تعریف
- سالمندیار
- سطوح سرپرستی
- Provider
- کارفرما
- عملیات نسیم
- کنترل کیفیت
- AI runtime
- Training pipeline
- Audit / governance

سطح دقیق دسترسی هنوز در BC-005 و قراردادهای بعدی تعیین می‌شود.

## 11. AI Runtime Data vs Training Data

داده‌ای که AI برای پاسخ در لحظه مجاز به مشاهده آن است، لزوماً مجاز به ورود به Training نیست.

تفکیک باید حفظ شود:

`Runtime Access ≠ Training Permission`

مثلاً ممکن است یک داده برای کمک به سالمندیار در یک Case قابل استفاده باشد، ولی برای Dataset آموزشی مجاز نباشد. تعیین مصادیق بعداً انجام می‌شود.

## 12. Human-generated vs AI-generated Data

نسیم باید بتواند میان حداقل این منشأها تمایز قائل شود:

- Elder-provided
- Family-provided
- Elder-care-worker recorded
- Provider-provided
- System-generated
- AI-generated
- Human-reviewed AI output

این Provenance برای کیفیت داده، Audit و Training Eligibility اهمیت دارد.

## 13. Official Record Boundary

همسو با BC-006:

`AI Output ≠ Official Record`

تا زمانی که مسیر معتبر ثبت/تأیید وجود نداشته باشد، خروجی AI نباید به‌صورت خودکار به حقیقت رسمی پرونده تبدیل شود.

همچنین AI-generated content نباید صرفاً به دلیل قرار گرفتن در پرونده، خودکار Training-eligible شود.

## 14. Training Exclusion Categories — NOT YET FINAL

دسته‌های زیر باید قبل از هر Training Policy بررسی ویژه شوند:

- داده هویتی مستقیم
- داده تماس
- اطلاعات سلامت
- اطلاعات سلامت روان
- اطلاعات خانوادگی
- اطلاعات حمایتی و اقتصادی
- متن آزاد
- اسناد یا فایل‌های بارگذاری‌شده
- داده Provider
- شکایت و اختلاف
- اطلاعات امنیتی و دسترسی

این فهرست به معنی ممنوعیت قطعی یا مجاز بودن هیچ موردی نیست؛ فقط نشان می‌دهد Rule صریح لازم است.

## 15. Retention & Deletion

برای هر Data Class باید در آینده تعیین شود:

- Retention period
- Archive rule
- Deletion rule
- Legal hold در صورت نیاز
- Backup retention
- اثر حذف داده بر Dataset
- اثر حذف داده بر Model lineage

طرح اولیه عدد یا بازه زمانی مشخصی ارائه نمی‌کند.

## 16. Data Quality

از آنجا که AI و ارزیابی شبکه به داده وابسته‌اند، Training Dataset نباید صرفاً از «داده موجود» ساخته شود.

Quality gateهای آینده ممکن است ابعادی مانند موارد زیر داشته باشند:

- Completeness
- Validity
- Provenance
- Consistency
- Timeliness
- Review status

Threshold عددی هیچ‌کدام هنوز تصمیم نشده است.

## 17. Audit & Lineage

برای Data Governance باید امکان ردیابی این زنجیره در آینده وجود داشته باشد:

`Source Record → Eligibility Decision → Preparation/Curation → Dataset Version → Training Run → Evaluation → Model Version → Production Promotion`

در هر مرحله باید Actor/Process و زمان قابل شناسایی باشد. شکل فنی Audit Trail در Technical تعیین خواهد شد.

## 18. Explicit Non-Decisions

BC-007 موارد زیر را تصویب نمی‌کند:

- نوع Database
- Data Lake / Warehouse architecture
- Encryption technology
- Retention duration
- Consent text
- Legal basis نهایی
- De-identification algorithm
- Training on raw Production data
- Online continual learning
- Automatic dataset inclusion
- Automatic model promotion
- استفاده از تمام داده‌های سلامت برای Training
- دسترسی کارفرما به پرونده فردی
- دسترسی کامل Provider به پرونده
- انتقال داده به سرویس AI خارجی

## 19. Open Decisions Required to Accept BC-007

1. Data inventory نهایی
2. Sensitivity classification
3. Purpose matrix
4. Consent/legal basis matrix
5. Data access matrix
6. Training eligibility rules
7. Exclusion rules
8. Curation/preparation policy
9. De-identification policy
10. Dataset approval ownership
11. Retention/deletion policy
12. Withdrawal handling
13. Provider data-sharing contract
14. Employer reporting boundary
15. AI runtime access boundary
16. Training pipeline access boundary
17. Audit/lineage requirements
18. Data incident governance

## 20. Downstream Constraints

تا پیش از Accepted شدن BC-007:

- Technical نباید همه Production data را Training-eligible فرض کند.
- Runtime access نباید معادل Training permission پیاده‌سازی شود.
- هیچ Actor نباید صرف عنوان نقش به همه داده‌ها دسترسی داشته باشد.
- Dataset باید Versionable و قابل ردیابی طراحی شود.
- Data provenance نباید حذف شود.
- AI-generated data باید از Human-recorded data قابل تمایز باشد.
- مدل Consent، Retention و Deletion نباید در Code حدس زده شود.
