# BC-014 — Legal, Privacy, Consent & Elder Rights

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + BC-005 + BC-007 + BC-012 + BC-013 + D-0004 + D-0005
- **Depends on:** BC-003, BC-005, BC-006, BC-007, BC-008, BC-012, BC-013

> این سند فقط چارچوب کسب‌وکاری حقوق سالمند، محرمانگی، رضایت، نمایندگی، اشتراک داده و الزامات حقوقی/حاکمیتی را مشخص می‌کند. متن رضایت‌نامه، مبنای قانونی پردازش، دوره نگهداری داده، حقوق قابل استناد قانونی و الزامات مقرراتی نهایی هنوز باید با بررسی حقوقی مستقل تعیین شوند و در این سند اختراع نمی‌شوند.

## 1. Source-confirmed Legal Direction

طرح مبنا بر این موارد تأکید دارد:

- رعایت قوانین و مقررات در تنظیم قراردادها و فرآیندهای همکاری
- حفاظت از اطلاعات سالمندان
- کنترل دسترسی
- پشتیبان‌گیری
- پایش امنیت
- مدیریت ریسک حقوقی و فناوری

منبع، مدل حقوقی تفصیلی برای Consent، نمایندگی، Retention، Data Sharing یا AI Training تعریف نکرده است.

## 2. Elder-centered Rights Principle

با توجه به سالمندمحور بودن نسیم، Business Design آینده باید حقوق و اختیارات سالمند را به‌صورت صریح تعریف کند.

حداقل حوزه‌هایی که باید تصمیم‌گیری شوند:

- اطلاع از اینکه چه داده‌ای جمع‌آوری می‌شود
- اطلاع از Purpose استفاده از داده
- اطلاع از اینکه چه Actorهایی به داده دسترسی دارند
- اطلاع از استفاده AI در تعامل یا تصمیم‌سازی کمکی
- امکان اعتراض/شکایت
- امکان اصلاح اطلاعات نادرست طبق Rule مصوب
- تعیین حدود نمایندگی خانواده
- تعیین نحوه رضایت یا مبنای قانونی پردازش
- تعیین شرایط اشتراک داده با Provider

این فهرست Frame کسب‌وکاری است و به معنی ادعای وجود حق قانونی مشخص در یک حوزه قضایی خاص نیست.

## 3. Consent Domains

برای ادامه طراحی، Consent باید حداقل در این حوزه‌ها جداگانه بررسی شود:

### A. Service Consent
رضایت/مبنای لازم برای ورود سالمند به خدمت یا فرآیند.

### B. Data Collection
رضایت/مبنای لازم برای ثبت اطلاعات سالمند.

### C. Provider Data Sharing
رضایت/مبنای لازم برای اشتراک داده با Provider.

### D. AI Assistance
رضایت/اطلاع‌رسانی لازم برای استفاده از AI در تعامل با سالمند یا سالمندیار.

### E. AI Training
رضایت یا مبنای قانونی لازم برای ورود داده واجد شرایط به Training Dataset.

### F. Research / Evaluation
هرگونه استفاده پژوهشی یا ارزیابی خارج از Purpose عملیاتی اصلی، در صورت مطرح شدن آینده.

هیچ‌یک از این حوزه‌ها در حال حاضر دارای متن Consent یا Rule نهایی نیستند.

## 4. Consent ≠ Universal Permission

اصل مهم:

`Consent for one purpose ≠ permission for every purpose`

مثلاً اجازه ثبت داده برای ارائه خدمت نباید خودکار به معنای مجوز استفاده از همان داده برای Training AI فرض شود.

Purpose Limitation از BC-007 باید در مدل Consent نیز رعایت شود.

## 5. Family / Representative Boundary

منبع اولیه ارتباط سالمندیار با «سالمند و خانواده» را قطعی می‌داند، اما خانواده را نماینده رسمی سالمند تعریف نمی‌کند.

بنابراین تا تصمیم بعدی:

- Family ≠ Authorized Representative
- حضور خانواده ≠ رضایت قانونی برای دسترسی به پرونده
- رابطه خانوادگی ≠ اختیار تصمیم‌گیری از طرف سالمند
- دسترسی خانواده به داده باید Contract صریح داشته باشد

باید در آینده تعریف شود:

- چه کسی می‌تواند نماینده مجاز باشد
- نمایندگی چگونه اثبات می‌شود
- دامنه اختیار نماینده چیست
- آیا اختیار داده با اختیار خدمت یکی است یا خیر
- نمایندگی چه زمانی خاتمه می‌یابد
- تعارض نظر سالمند و نماینده چگونه مدیریت می‌شود

## 6. Capacity / Decision Support Boundary

نسیم با سالمندانی با شرایط متنوع جسمی، روانی و اجتماعی سروکار خواهد داشت، اما طرح اولیه مدل Capacity Assessment حقوقی یا بالینی تعیین نکرده است.

بنابراین BC-014 هیچ Rule درباره فقدان اهلیت، قیمومت، Guardian، Proxy یا تصمیم جایگزین تصویب نمی‌کند.

این موضوع نیازمند بررسی حقوقی/تخصصی مستقل است.

## 7. Privacy by Purpose

هر Actor فقط باید در حد Purpose مصوب به داده دسترسی داشته باشد.

Business آینده باید به‌صورت مستقل مرز دسترسی این Actorها را تعیین کند:

- سالمند
- نماینده مجاز
- سالمندیار
- سطوح سرپرستی
- Provider
- کارفرما
- عملیات نسیم
- Quality/Audit
- AI runtime
- Dataset pipeline
- Training/Evaluation process

اصل پایه:

`Need for service ≠ right to full record`

## 8. Employer Reporting Boundary

کارفرما در منبع نقش نظارتی دارد، اما این نقش به‌صورت خودکار به معنی دسترسی به پرونده کامل فردی سالمند نیست.

باید در آینده مشخص شود:

- کارفرما چه گزارش‌هایی دریافت می‌کند
- گزارش‌ها فردی یا تجمیعی هستند
- چه داده‌ای Mask/Aggregate می‌شود
- چه داده‌ای اصلاً نباید در اختیار کارفرما قرار گیرد
- استثناهای قانونی/قراردادی چه هستند

## 9. Provider Data-sharing Boundary

همسو با BC-008:

Provider باید فقط داده‌ای را دریافت کند که برای ارائه خدمت مصوب لازم است.

باید برای هر Service مشخص شود:

- Data needed
- Purpose
- Sharing trigger
- Sharing duration
- Recipient
- Further-sharing restriction
- Return/result data
- Retention expectation
- Auditability

هیچ Provider نباید صرف عضویت در شبکه به پرونده کامل دسترسی داشته باشد.

## 10. AI Transparency

چون AI از روز اول در نسیم حضور دارد، Business آینده باید تعیین کند که سالمند و سالمندیار چگونه از حضور AI مطلع می‌شوند.

حداقل باید بتوان میان این موارد تمایز قائل شد:

- پاسخ/پیشنهاد تولیدشده توسط AI
- اطلاعات ثبت‌شده توسط انسان
- تصمیم تأییدشده توسط انسان
- اقدام خودکار سامانه

UI/UX دقیق در Technical/Product Design تعیین می‌شود.

## 11. AI Output Boundary

اصل:

`AI Output ≠ Human Decision ≠ Official Record`

مگر آنکه Contract مصوب صریحاً مسیر تبدیل آن را تعریف کند.

AI نباید هویت تصمیم‌گیر انسانی را جعل کند یا خروجی خود را به‌عنوان تأیید انسانی ثبت کند.

## 12. Training Data Legal Boundary

D-0005 ساخت مستمر و خودکار Dataset را تصویب کرده است، اما این خودکارسازی فقط برای داده‌ای مجاز است که از قواعد Legal/Data Governance عبور کرده باشد.

قبل از ورود یک Data Class به Training باید حداقل مشخص شود:

- Purpose
- legal basis / consent requirement
- eligibility
- de-identification requirement
- exclusion rules
- retention
- withdrawal impact
- dataset lineage
- governance owner

## 13. Withdrawal — Open Contract

اگر مدل آینده اجازه Withdrawal از Consent را بدهد، باید اثر آن روشن شود.

موضوعات باز:

- اثر بر Operational Data
- اثر بر Provider-shared data
- اثر بر AI runtime access
- اثر بر Datasetهای آینده
- اثر بر Datasetهای قبلی
- اثر بر Modelهای قبلاً آموزش‌دیده
- زمان اثرگذاری
- محدودیت‌های حقوقی/عملیاتی

BC-014 هیچ نتیجه حقوقی خودکاری برای Withdrawal تعیین نمی‌کند.

## 14. Retention & Deletion

Retention و Deletion باید برای هر Data Class و Purpose جداگانه تعیین شوند.

موضوعات نیازمند تصمیم:

- active retention
- archive period
- deletion trigger
- legal hold
- backup retention
- audit retention
- effect on Dataset lineage
- effect on model lineage

هیچ بازه زمانی در منبع اولیه مشخص نشده است.

## 15. Confidentiality

Business آینده باید تعهد محرمانگی را برای همه Actorهایی که به داده دسترسی دارند قابل اعمال کند، از جمله:

- سالمندیار
- کارکنان نسیم
- Provider
- پیمانکار فناوری
- نقش‌های Quality/Audit
- تیم AI/Data

نوع قرارداد، متن تعهد و ضمانت اجرا هنوز تعیین نشده‌اند.

## 16. Complaint & Rights Request

طرح اولیه رضایت و مدیریت کیفیت را مطرح می‌کند، اما Rights-request Workflow مشخصی ندارد.

برای آینده باید تصمیم شود چگونه سالمند یا نماینده مجاز بتواند حداقل این موارد را مطرح کند:

- شکایت
- اعتراض به خدمت
- اعتراض به ثبت داده
- درخواست اصلاح
- پرسش درباره دسترسی/اشتراک داده
- اعتراض به استفاده AI
- درخواست بررسی انسانی

نوع حقوق قابل اعمال باید با بررسی حقوقی نهایی شود.

## 17. Notice & Information Duties — DRAFT FRAME

برای هر پردازش مهم، Business آینده باید مشخص کند چه اطلاعاتی باید به سالمند ارائه شود.

Candidate items:

- چه داده‌ای
- برای چه Purpose
- توسط چه Actor
- برای چه مدتی
- با چه Recipientهایی
- آیا AI درگیر است
- آیا داده ممکن است وارد Training شود
- مسیر سؤال/شکایت چیست

اینها Frame طراحی هستند، نه متن حقوقی نهایی.

## 18. Data Breach / Privacy Incident

همسو با BC-012، رخدادهای Privacy/Data باید Incident مستقل داشته باشند.

نمونه حوزه‌ها:

- unauthorized access
- unauthorized disclosure
- incorrect recipient
- excessive access
- wrong-purpose processing
- invalid dataset inclusion
- lost provenance
- compromised credentials

Notification، severity و regulatory reporting هنوز باید تعیین شوند.

## 19. Children/Guardianship Assumptions Prohibited

صرف سالمند بودن کاربر نباید باعث شود سیستم به‌صورت پیش‌فرض:

- او را فاقد اختیار فرض کند
- خانواده را صاحب اختیار فرض کند
- نماینده قانونی ایجاد کند
- دسترسی خانواده را فعال کند

هر استثنا باید Rule و مبنای صریح داشته باشد.

## 20. Legal Review Gate

پیش از Production باید موضوعات زیر از منظر حقوقی/مقرراتی Review شوند:

- Terms / agreements
- Consent model
- Data-sharing contracts
- Provider contracts
- Privacy notice
- Retention/deletion
- Complaint process
- AI transparency
- Training-data legal basis
- Incident notification
- cross-organization data access

این الزام به معنی تعیین مشاور، نهاد یا حوزه قضایی خاص نیست.

## 21. Explicit Non-Decisions

BC-014 موارد زیر را تصویب نمی‌کند:

- قانون حاکم نهایی
- حوزه قضایی
- متن Consent
- Privacy Policy نهایی
- Retention period
- حق حذف مطلق
- حق دسترسی مطلق
- Guardian/Proxy rule
- سن یا Capacity rule
- Cross-border data transfer
- Data residency
- Provider confidentiality template
- Employer access level
- AI training legal basis
- Regulatory reporting deadlines
- جریمه یا مسئولیت مدنی خاص

## 22. Open Decisions Required to Accept BC-014

1. Governing legal/regulatory framework
2. Elder rights catalog
3. Consent model
4. Authorized representative model
5. Capacity/guardianship handling
6. Privacy notice
7. Data access matrix
8. Employer reporting boundary
9. Provider data-sharing contract
10. AI transparency requirements
11. AI training legal basis
12. Withdrawal handling
13. Retention/deletion policy
14. Confidentiality obligations
15. Complaint/rights-request workflow
16. Data incident notification rules
17. Legal review owner
18. Legal approval gate before Production

## 23. Downstream Constraints

تا پیش از Accepted شدن BC-014:

- Technical نباید Consent flow نهایی را اختراع کند.
- خانواده نباید به‌صورت پیش‌فرض نماینده مجاز باشد.
- Provider و کارفرما نباید دسترسی کامل پیش‌فرض داشته باشند.
- AI runtime access و Training permission باید جدا بمانند.
- Dataset automation فقط باید داده‌ای را وارد کند که قواعد حقوقی/Data Governance آن را مجاز کرده‌اند.
- UI نباید حقوق یا تعهدات قانونی‌ای را نمایش دهد که Business/Legal تصویب نکرده است.
