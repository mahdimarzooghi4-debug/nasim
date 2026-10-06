# BC-018 — Service Catalog Definition, Need Taxonomy & Referral Eligibility

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + BC-002 + BC-003 + BC-008 + D-0004 + D-0005
- **Depends on:** BC-001, BC-002, BC-003, BC-005, BC-006, BC-007, BC-008, BC-012, BC-014, BC-016, BC-017

> این سند چارچوب کسب‌وکاری تبدیل «نیاز سالمند» به «خدمت قابل ارائه/ارجاع» را تعریف می‌کند. منبع اولیه Service SKU، Need Taxonomy، Severity، Priority، Eligibility Rule، Referral Rule یا Catalog Versioning نهایی را تعیین نکرده است؛ بنابراین این موارد در این سند اختراع نمی‌شوند.

## 1. Core Distinction: Need ≠ Service

در نسیم باید میان «نیاز» و «خدمت» تفکیک روشن وجود داشته باشد.

- **Need:** مسئله/نیاز شناسایی‌شده درباره سالمند
- **Service:** پاسخ عملیاتی تعریف‌شده‌ای که ممکن است برای پاسخ به یک Need مناسب باشد
- **Referral:** اتصال یک Need واجد شرایط به Service/Provider مناسب طبق Rule مصوب

اصل:

`Need ≠ Service ≠ Referral`

ثبت یک Need به‌تنهایی به معنی ایجاد خودکار Referral یا الزام به ارائه یک Service خاص نیست.

## 2. Source-confirmed Need Domains

طرح اولیه Need Taxonomy رسمی ارائه نمی‌کند، اما در پایش سالمند به تغییرات این حوزه‌ها اشاره می‌کند:

- جسمی
- روانی
- اجتماعی

همچنین درخواست‌ها می‌توانند بر اساس نوع نیاز به این لایه‌های سطح بالا هدایت شوند:

- سلامت
- رفاه و خدمات مکمل
- سایر خدمات موجود در شبکه

این موارد فقط Domainهای سطح بالا هستند، نه Taxonomy نهایی.

## 3. Source-confirmed Service Families

خدمات سلامت ذکرشده در طرح مبنا:

- ارزیابی سلامت
- خدمات پزشکی و پرستاری
- مراقبت از بیماری‌های مزمن
- توانبخشی و مراقبت‌های تخصصی
- سلامت روان

خدمات رفاهی/مکمل ذکرشده:

- رفاهی
- فرهنگی و اجتماعی
- حمایتی
- حقوقی
- توانبخشی
- سایر ظرفیت‌های اکوسیستم و شرکا

تا زمانی که Service Definition تصویب نشده باشد، اینها Service Family هستند و نه الزاماً Service Item قابل درخواست.

## 4. Need Record — DRAFT BUSINESS FRAME

برای اینکه یک Need قابل ارزیابی باشد، Business آینده باید تعیین کند چه اطلاعاتی حداقل لازم است.

Candidate dimensions:

- Need identifier
- Need category
- Description
- Source / who identified it
- Date/time
- Related observations
- Elder-stated concern
- Evidence
- Priority/urgency در صورت تعریف
- Current status
- Related service/referral
- Human reviewer/owner

اینها Data Model نهایی نیستند.

## 5. Need Source / Provenance

Need می‌تواند در آینده از منابع متفاوتی مطرح شود، مانند:

- سالمند
- خانواده/نماینده مجاز
- سالمندیار
- Provider
- سامانه
- AI suggestion

اما منشأ Need باید قابل تشخیص باشد.

اصل:

`AI-suggested Need ≠ Human-confirmed Need`

تا تصمیم صریح، AI نمی‌تواند Need رسمی را بدون مسیر Human Review نهایی ثبت کند.

## 6. Need Taxonomy — DRAFT STRUCTURE

Taxonomy آینده باید بتواند در صورت نیاز چند سطح داشته باشد:

`Need Domain → Need Category → Need Type`

اما تعداد سطوح، نام Categoryها و Codeها هنوز تصمیم نشده‌اند.

Taxonomy باید Versionable باشد تا تغییر دسته‌بندی در آینده داده تاریخی را مخدوش نکند.

## 7. Need Taxonomy Versioning

برای هر Need ثبت‌شده باید در آینده بتوان مشخص کرد:

- taxonomy version
- need code
- label at time of recording
- effective date
- superseded mapping در صورت تغییر

تغییر Taxonomy نباید تاریخچه Needهای قبلی را بی‌صدا بازنویسی کند.

## 8. Priority / Severity Boundary

منبع اولیه Severity یا Priority نهایی تعریف نکرده است.

این دو مفهوم نیز نباید بدون تصمیم یکی فرض شوند:

- **Priority:** ترتیب/اهمیت رسیدگی عملیاتی
- **Severity:** شدت وضعیت یا پیامد

ممکن است در آینده ارتباط داشته باشند، اما Rule نهایی باید Business-approved باشد.

## 9. Service Catalog Item — Required Business Fields

برای هر Service Item آینده حداقل باید این ابعاد قابل تعریف باشند:

- Service ID
- Service Name
- Service Family
- Business Description
- Target Need(s)
- Direct / Referral-only
- Eligible Provider Type
- Preconditions
- Eligibility Rules
- Required Data
- Required Consent/Authorization
- Geographic Availability
- Capacity dependency
- Request/Referral Entry Rule
- Completion Evidence
- Quality Criteria
- SLA در صورت تصویب
- Pricing/Funding در صورت تصویب
- Escalation rule
- Effective version/status

هیچ مقدار این فیلدها در BC-018 نهایی نمی‌شود.

## 10. Direct vs Referral-only Boundary

برای هر Service باید مشخص شود:

- آیا نسیم/سالمندیار آن را مستقیماً ارائه می‌کند
- یا فقط به Provider تخصصی Referral می‌دهد
- یا مدل دیگری دارد که بعداً تصویب شود

تا زمان تصمیم صریح، خدمات تخصصی سلامت/پرستاری/درمانی نباید Direct Service سالمندیار فرض شوند.

## 11. Need-to-Service Mapping

برای هر Need Type آینده باید بتوان مشخص کرد:

- چه Serviceهایی Candidate پاسخ هستند
- چه Serviceهایی مجاز نیستند
- چه Preconditions لازم‌اند
- آیا چند Service ممکن است مناسب باشند
- آیا هیچ Service فعلی مناسب نیست

اصل:

`Need classification does not automatically select one provider or one service.`

## 12. Referral Eligibility

Referral فقط وقتی باید قابل ایجاد باشد که Business Rule لازم را پاس کرده باشد.

Eligibility Rule آینده می‌تواند ابعادی مانند این داشته باشد:

- Need type
- Service eligibility
- elder eligibility
- consent/authorization
- required evidence
- provider/service availability
- geography
- funding authorization در صورت نیاز
- prior steps/preconditions

اما هیچ Rule نهایی در این سند تعریف نمی‌شود.

## 13. Eligibility Result — DRAFT FRAME

برای تحلیل Business ممکن است Outcomeهای Eligibility به شکل مفهومی شامل این موارد باشند:

- eligible
- not eligible
- needs more information
- needs human review
- out of catalog

این Vocabulary نهایی نیست و State Machine محسوب نمی‌شود.

## 14. Out-of-Catalog Need

ممکن است Need معتبر باشد اما هیچ Service مصوب فعلی برای آن وجود نداشته باشد.

نسیم باید بتواند میان این دو حالت فرق بگذارد:

- Need نامعتبر/تأییدنشده
- Need معتبر ولی خارج از Service Catalog

نبود Service نباید باعث حذف یا جعل Need شود.

## 15. Multiple Needs / Multiple Services

یک سالمند ممکن است هم‌زمان چند Need داشته باشد و یک Need نیز ممکن است بیش از یک Service مرتبط داشته باشد.

Technical نباید رابطه Need ↔ Service را به‌طور پیش‌فرض one-to-one فرض کند.

Multiplicity نهایی در Technical پس از Business Contract تعیین می‌شود.

## 16. Service Eligibility ≠ Provider Eligibility

حتی اگر سالمند برای یک Service واجد شرایط باشد، هنوز باید Provider مناسب و مجاز جداگانه تعیین شود.

تفکیک:

`Need Eligibility → Service Eligibility → Provider Eligibility/Availability`

این مراحل نباید بدون Business Decision در یک Rule مبهم ادغام شوند.

## 17. Provider Mapping

همسو با BC-008، هر Service باید در آینده بتواند به Provider Typeهای مجاز Mapping شود.

اما هنوز تصمیم نشده است:

- Provider Type نهایی
- Credential rules
- ranking
- selection
- capacity rule
- geography rule
- fallback/re-routing

## 18. Service Catalog Status & Lifecycle — DRAFT

Catalog آینده باید بتواند نسخه و وضعیت داشته باشد.

Candidate concepts:

- Draft
- Active
- Suspended
- Retired

اینها فقط Frame هستند و State Machine نهایی نیستند.

Service قدیمی نباید صرفاً با حذف از Catalog باعث نامعتبر شدن تاریخچه Referralهای قبلی شود.

## 19. Catalog Change Governance

تغییر Service Catalog باید Governance داشته باشد، به‌خصوص وقتی روی این موارد اثر دارد:

- Referral eligibility
- Provider mapping
- Pricing/funding
- Data requirements
- Consent
- Quality criteria
- AI suggestions
- Training data interpretation

Owner و Approval Rule این تغییرات هنوز در BC-013 باز است.

## 20. Effective-dated Rules

برای جلوگیری از تغییر معنای داده تاریخی، Ruleهای زیر باید در آینده Versionable/Effective-dated باشند:

- Need Taxonomy
- Service Definition
- Eligibility Rule
- Provider Eligibility Mapping
- Completion Criteria
- Quality Criteria

Technical باید امکان این رفتار را فراهم کند، اما نسخه‌بندی دقیق بعداً طراحی می‌شود.

## 21. Referral Creation Boundary

Referral نباید فقط از انتخاب یک Service در UI ساخته شود.

قبل از Referral باید Ruleهای مصوب مربوط به Need، Service، Authorization و Eligibility اعمال شده باشند.

اما هنوز مشخص نشده است:

- چه کسی Referral را ایجاد می‌کند
- چه کسی آن را Approve می‌کند
- چه Referralهایی Approval اضافه می‌خواهند
- آیا سالمندیار اختیار نهایی دارد
- چه زمانی Consent لازم است

## 22. Completion ≠ Need Resolution

اصل مهم:

`Service Completion ≠ Need Resolution`

ممکن است Provider یک Service را Completed اعلام کند، ولی Need سالمند همچنان ادامه داشته باشد.

Business آینده باید جداگانه تعیین کند:

- Service completion
- Referral closure
- Need resolution
- Need reopen/reassessment

Technical نباید این مفاهیم را یکی کند.

## 23. Outcome Link

برای ارزیابی اثر، باید در آینده بتوان بین این مفاهیم ارتباط برقرار کرد:

`Need → Service/Referral → Delivery → Follow-up → Observed Outcome`

اما Outcome Model و Attribution نهایی در Contract جداگانه باید تعیین شود.

## 24. AI Role in Need Classification — Day-one Boundary

چون AI از روز اول در نسیم حضور دارد، AI می‌تواند در Use Caseهای مصوب در این حوزه‌ها کمک کند:

- خلاصه‌سازی Observations
- پیشنهاد Need Category
- پیشنهاد سؤال تکمیلی
- پیشنهاد Candidate Service Family
- هشدار درباره داده ناقص/ناسازگار

اما تا تصمیم صریح:

- AI Need رسمی را نهایی نمی‌کند
- AI Priority/Severity نهایی تعیین نمی‌کند
- AI Referral Eligibility نهایی صادر نمی‌کند
- AI Provider را الزام‌آور انتخاب نمی‌کند
- AI Service Order نهایی ایجاد نمی‌کند

## 25. Human Review of AI Suggestions

اگر AI در Need/Service Mapping نقش پیشنهادی داشته باشد، باید امکان ثبت این موارد وجود داشته باشد:

- AI suggestion
- model/version
- rule/catalog/taxonomy version
- human accept/reject/edit
- final human/system action

این Provenance برای Audit و Learning ضروری است.

## 26. Dataset & Learning Link

تعاملات این حوزه می‌توانند منبع Learning Signal باشند، از جمله:

- AI category suggestion
- human correction
- final Need classification
- Service mapping
- Referral outcome
- completion/result
- follow-up outcome

اما طبق D-0005، فقط داده واجد Training Eligibility وارد Dataset خودکار می‌شود.

همچنین:

`Human correction ≠ automatically verified ground truth`

مگر Labeling/Validation Rule مصوب وجود داشته باشد.

## 27. Catalog and Dataset Version Alignment

اگر Dataset از داده Need/Service استفاده می‌کند، باید نسخه Taxonomy و Service Catalog مربوط به هر Record قابل ردیابی باشد.

در غیر این صورت تغییر نام یا تعریف Service/Need می‌تواند معنای Training Data را مخدوش کند.

## 28. Emergency Boundary

Need Taxonomy نباید به‌صورت ضمنی Medical Triage یا Emergency Protocol ایجاد کند.

Urgent/Emergency rules همچنان در BC-003 و BC-012 تصمیم باز هستند.

## 29. Explicit Non-Decisions

BC-018 موارد زیر را تصویب نمی‌کند:

- Need taxonomy نهایی
- Need codes
- Severity levels
- Priority levels
- Triage protocol
- Phase-1 Service Catalog نهایی
- Service SKUهای نهایی
- Direct-service list
- Eligibility formulas
- Automated eligibility
- Auto-referral
- Provider ranking/selection
- SLA
- Price/tariff
- Clinical protocol
- Emergency classification
- AI autonomous classification
- AI autonomous service ordering

## 30. Open Decisions Required to Accept BC-018

1. Need taxonomy
2. Need taxonomy versioning policy
3. Priority model
4. Severity model
5. Phase-1 Service Catalog
6. Service definitions
7. Direct vs Referral-only classification
8. Need-to-service mappings
9. Service eligibility rules
10. Required evidence/data
11. Consent/authorization requirements
12. Out-of-catalog handling
13. Provider-type mappings
14. Referral creation/approval rule
15. Completion criteria
16. Need resolution/reopen rule
17. Catalog lifecycle/versioning
18. Catalog change authority
19. AI role in classification/mapping
20. Human-review rule for AI suggestions

## 31. Downstream Constraints

تا پیش از Accepted شدن BC-018:

- Backend نباید Need Taxonomy یا Service SKU نهایی را Hard-code کند.
- UI نباید Need و Service را یک مفهوم نمایش دهد.
- Referral نباید فقط از انتخاب Service به‌طور خودکار قطعی شود.
- Service completion نباید Need resolution تلقی شود.
- Provider eligibility نباید از Service eligibility استنتاج شود.
- AI نباید Classification، Eligibility یا Referral را نهایی کند.
- Datasetهای Learning باید Taxonomy/Service Catalog Version مربوط به داده را حفظ کنند.
