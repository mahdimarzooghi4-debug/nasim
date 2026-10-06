# BC-006 — AI Use Cases, Human Oversight & Learning Boundary

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source:** Product-owner decision D-0004
- **Depends on:** BC-003, BC-004, BC-005

> این سند محدوده کسب‌وکاری هوش مصنوعی نسیم را برای دو مخاطب اصلی — سالمند و سالمندیار — روشن می‌کند. هر قابلیت یا اختیار که در D-0004 صریحاً تصویب نشده، تا زمان تصمیم مستقل نهایی تلقی نمی‌شود.

## 1. Product Role

هوش مصنوعی نسیم یک **دستیار داخلی** است که در کنار سالمند و سالمندیار عمل می‌کند.

اصل پایه:

`AI assists; humans remain accountable.`

AI می‌تواند اطلاعات را تحلیل کند، محتوا یا پیشنهاد تولید کند و انجام کار را تسهیل کند؛ اما تا زمان تصمیم صریح، صاحب اختیار نهایی در تصمیم‌های رسمی، تخصصی، درمانی، مالی یا حقوقی نیست.

## 2. Candidate Use Cases for Elder — DRAFT

Use Caseهای زیر برای طراحی Business آینده ثبت می‌شوند و هنوز Final/Accepted نیستند:

- پاسخ‌گویی و راهنمایی درباره خدمات نسیم
- کمک به درک فرآیند ارجاع و وضعیت خدمت
- یادآوری تعاملات، پیگیری‌ها یا برنامه‌های ثبت‌شده
- کمک به ثبت یا بیان نیاز به زبان ساده
- توضیح اطلاعات ثبت‌شده به شکل قابل فهم برای سالمند
- کمک در تعامل با سامانه برای سالمندانی که سواد دیجیتال پایین‌تری دارند
- هدایت سالمند به تماس با سالمندیار در مواردی که نیاز به اقدام انسانی وجود دارد

### Boundary

AI سالمند تا تصمیم بعدی نباید به‌عنوان مرجع تشخیص پزشکی، توصیه درمان قطعی، اورژانس، تأیید مالی یا تصمیم‌گیر Referral معرفی شود.

## 3. Candidate Use Cases for Elder-Care Worker — DRAFT

Use Caseهای زیر برای طراحی Business آینده ثبت می‌شوند و هنوز Final/Accepted نیستند:

- خلاصه‌سازی سابقه و تعاملات مرتبط با سالمند
- کمک به آماده‌سازی پیگیری‌های روزانه
- برجسته‌سازی تغییرات یا داده‌های قابل توجه برای بررسی انسانی
- کمک به تهیه متن گزارش یا یادداشت
- پیشنهاد پرسش‌های تکمیلی برای پیگیری وضعیت
- کمک به جست‌وجو در Service Catalog و فرآیندهای نسیم
- پیشنهاد مسیرهای احتمالی ارجاع برای بررسی سالمندیار
- یادآوری کارهای باز، ارجاعات و پیگیری‌ها
- کمک به کشف ناسازگاری یا نقص داده برای اصلاح انسانی

### Boundary

پیشنهاد AI معادل تصمیم سالمندیار، سرپرست، Provider یا نسیم نیست.

## 4. Human Oversight

در هر Use Case که خروجی AI بتواند بر خدمت واقعی، پرونده رسمی یا مسیر سالمند اثر بگذارد، Business Contract آینده باید این موارد را مشخص کند:

- Human Owner
- نوع Review
- Approval requirement
- امکان Reject / Edit
- ثبت هویت تصمیم‌گیر انسانی
- ثبت نسخه AI و ورودی‌های مؤثر
- نحوه Escalation در عدم اطمینان یا تعارض

تا آن زمان AI فقط نقش پیشنهادی/کمکی دارد.

## 5. Formal Record Boundary

AI نباید صرفاً با تولید یک پاسخ، حقیقت رسمی پرونده را تغییر دهد.

تفکیک مفهومی باید حفظ شود:

`AI Output ≠ Official Record`

برای تبدیل خروجی AI به داده رسمی، باید یک مسیر مصوب وجود داشته باشد که مسئول انسانی، Rule مصوب یا فرآیند معتبر آن را ثبت/تأیید کند.

## 6. Learning Goal

جهت محصول D-0004 این است که AI از داده‌های تولیدشده در نسیم برای آموزش و بهبود خودکار استفاده کند.

این هدف به معنی مجاز بودن استفاده مستقیم از هر داده Production نیست.

پیش از Training واقعی باید مشخص شود:

- چه Eventها و Data Classهایی Training-eligible هستند
- چه داده‌ای نیازمند پاک‌سازی یا De-identification است
- چه داده‌ای به دلیل حساسیت نباید وارد Dataset شود
- چه داده‌ای نیازمند Consent یا مبنای قانونی دیگر است
- چه کیفیتی برای ورود به Dataset لازم است
- چه کسی Dataset را تأیید می‌کند

## 7. Learning Boundary — DRAFT Principle

چرخه یادگیری آینده باید میان این مفاهیم تفکیک قائل شود:

`Production Data → Eligible Data → Prepared/Curated Dataset → Training → Evaluation → Approved Model Version → Production`

این زنجیره در این مرحله فقط یک **چارچوب حاکمیتی پیشنهادی برای جلوگیری از یادگیری کنترل‌نشده** است؛ نوع Training، الگوریتم، مدل و Gateهای دقیق هنوز تصمیم نشده‌اند.

## 8. No Silent Self-Promotion

عبارت «بهبود خودکار» در D-0004 به معنی مجاز بودن ارتقای خودکار و بدون کنترل مدل در Production نیست.

تا زمان تصمیم صریح:

- Training و Production Runtime از نظر Governance یکی فرض نمی‌شوند.
- خروجی Training نباید خودکار جایگزین نسخه فعال شود.
- Model Version باید قابل شناسایی باشد.
- Evaluation و Promotion policy باید جداگانه تعریف شود.
- Rollback باید در Technical قابل طراحی باشد.

## 9. Data Lineage & Audit

برای هر Dataset یا Model Version آینده باید قابلیت ردیابی مفهومی زیر وجود داشته باشد:

- Source data period
- Data eligibility rule
- Dataset version
- Training run/version
- Evaluation evidence
- Model version
- Promotion event

جزئیات فنی این ردیابی در مرحله Technical تعیین می‌شود.

## 10. Sensitive Domains

نسیم با داده‌های بالقوه حساس سالمندان سروکار دارد. بنابراین AI Contract آینده باید برای حداقل این حوزه‌ها قواعد صریح داشته باشد:

- سلامت جسمی
- سلامت روان
- وضعیت اجتماعی
- اطلاعات خانوادگی
- اطلاعات حمایتی
- اطلاعات تماس و هویتی
- داده‌های عملکرد سالمندیار
- داده‌های Provider و خدمت

وجود این دسته‌ها به معنی مجاز بودن همه آنها برای Training نیست.

## 11. Fail-safe Principle

در نبود مدل معتبر، خطای AI، عدم اطمینان، یا نبود داده کافی، سیستم نباید تصمیم رسمی را جعل کند.

رفتار دقیق Fail-safe هنوز باید تعیین شود؛ اما اصل Business این است که **عدم توانایی AI نباید به تصمیم ساختگی یا تغییر خودکار پرونده منجر شود.**

## 12. Explainability / Provenance

برای پیشنهادهای AI که وارد فرآیند کاری سالمندیار می‌شوند، باید در طراحی آینده امکان تشخیص این موارد وجود داشته باشد:

- اینکه خروجی توسط AI تولید شده
- نسخه AI
- زمان تولید
- Actor انسانی که آن را پذیرفته/رد/ویرایش کرده
- ارتباط آن با داده‌های مجاز ورودی

سطح Explainability فنی هنوز باز است.

## 13. Explicit Non-Decisions

BC-006 موارد زیر را تصویب نمی‌کند:

- نوع مدل
- LLM بودن یا نبودن
- الگوریتم Training
- Online Learning
- Fine-tuning method
- Vector DB یا RAG
- Cloud یا On-prem deployment
- استفاده از سرویس AI بیرونی
- Training مستقیم روی تمام داده‌های Production
- Auto-promotion
- Medical diagnosis
- Autonomous referral
- Autonomous provider selection
- Autonomous case closure
- Autonomous financial approval

## 14. Open Decisions Required to Accept BC-006

1. فهرست نهایی Use Caseهای سالمند
2. فهرست نهایی Use Caseهای سالمندیار
3. Forbidden Actions
4. Human Owner هر Use Case
5. Review/Approval rules
6. Official-record conversion rule
7. Data classification
8. Training eligibility
9. Consent/legal basis
10. Curation/preparation rules
11. Evaluation policy
12. Model promotion policy
13. Rollback policy
14. Fail-safe behavior
15. Incident handling
16. Monitoring metrics
17. Retention/deletion
18. Explainability/provenance requirements

## 15. Downstream Constraints

تا پیش از Accepted شدن BC-006:

- Technical نباید مدل، الگوریتم یا Training method را قطعی فرض کند.
- Production data نباید بدون Data Governance وارد Training path شود.
- خروجی AI نباید مستقیماً Official Record شود.
- مدل جدید نباید بدون Promotion policy جایگزین مدل فعال شود.
- UI باید بتواند AI output را از Human decision متمایز کند.
- Audit design باید منشأ AI output و پذیرش/رد انسانی را قابل ردیابی کند.
