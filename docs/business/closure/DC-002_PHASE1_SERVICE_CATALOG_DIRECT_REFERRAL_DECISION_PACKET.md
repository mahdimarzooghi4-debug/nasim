# DC-002 — Phase-1 Service Catalog & Direct-vs-Referral Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + BC-002 + BC-008 + BC-018 + DC-001
- **Purpose:** بستن مرز سطح بالای Service Catalog فاز اول و تفکیک Direct Service از Referral-only بدون اختراع Service SKU، SLA، تعرفه یا اختیار تخصصی سالمندیار.

> این سند **Decision Register نیست** و هیچ تصمیمی را Accepted نمی‌کند. فقط تصمیم‌های دارای پشتوانه کافی و مواردی که نیازمند تصمیم مستقیم مالک محصول هستند را جدا می‌کند.

## 1. Why This Packet Is Blocking

Technical برای طراحی معتبر حداقل باید بداند:

- Service Domainهای فاز اول چیست
- چه چیزی وظیفه مستقیم سالمندیار است
- چه چیزی به Provider/شبکه تخصصی ارجاع می‌شود
- چه Service Itemهایی واقعاً در Pilot فعال‌اند
- چه چیزی خارج از Scope فاز اول است

بدون این مرز، API، Data Model، Workflow و UI ناچار به اختراع Service Type یا Permission می‌شوند.

## 2. Source-confirmed Service Architecture

طرح اولیه نسیم را یک شبکه خدماتی چندلایه تعریف می‌کند:

1. **شبکه سالمندیاری محله‌محور**
2. **شبکه سلامت**
3. **شبکه رفاه و خدمات مکمل**

اصل عملیاتی منبع:

`Service starts near the elder; specialized needs are referred to specialized layers.`

این ساختار، معماری Business سطح بالا است؛ نه Service Catalog اجرایی نهایی.

## 3. Source-confirmed Elder-care Worker Direct Scope

وظایف صریح سالمندیار:

- تشکیل و به‌روزرسانی پرونده اولیه
- ارتباط منظم با سالمند و خانواده
- شناسایی/پایش تغییرات جسمی، روانی و اجتماعی
- ثبت و گزارش نیاز
- ارجاع موارد نیازمند خدمت
- پیگیری ارائه خدمت
- پیگیری رضایت سالمند
- هماهنگی دریافت خدمات تخصصی

اینها مستقیم‌ترین Service/Operational Capabilities هستند که منبع برای سالمندیار تعیین می‌کند.

## 4. What the Source Does NOT Grant to Elder-care Workers

منبع سالمندیار را به‌عنوان:

- پزشک
- پرستار
- درمانگر
- ارائه‌دهنده مستقل خدمات تخصصی سلامت
- ارائه‌دهنده قطعی خدمت حقوقی
- ارائه‌دهنده قطعی توانبخشی تخصصی

تعریف نمی‌کند.

بنابراین هیچ صلاحیت تخصصی از عنوان «سالمندیار» استنتاج نمی‌شود.

## 5. Source-confirmed Health Service Families

در لایه سلامت، منبع این خانواده‌ها را ذکر می‌کند:

- ارزیابی سلامت
- خدمات پزشکی
- خدمات پرستاری
- مراقبت از بیماری‌های مزمن
- توانبخشی و مراقبت‌های تخصصی
- خدمات سلامت روان

منبع تصریح می‌کند سالمند بر اساس Need شناسایی‌شده **به خدمات سلامت ارجاع می‌شود** و این خدمات از طریق اتصال به ترنم و سایر ظرفیت‌های درمانی/مراقبتی ارائه می‌شوند.

## 6. Source-confirmed Welfare & Complementary Families

در لایه رفاه و خدمات مکمل، منبع این خانواده‌ها را ذکر می‌کند:

- خدمات رفاهی
- خدمات فرهنگی و اجتماعی
- خدمات حمایتی
- خدمات حقوقی
- خدمات توانبخشی
- سایر ظرفیت‌های موجود در اکوسیستم کارفرما و شرکای همکار

منبع Service Definition اجرایی هیچ‌کدام را تعیین نمی‌کند.

## 7. Service Family ≠ Active Pilot Service

اصل مهم:

`Source-listed Service Family ≠ automatically active Pilot Service Item`

وجود یک خانواده خدمت در Concept به معنی این نیست که همه Service Itemهای آن در روز اول Pilot فعال باشند.

برای Pilot باید Activation جداگانه تصویب شود.

## 8. Direct vs Referral-only Classification Rule

در سطح فعلی Evidence، پیشنهاد Business زیر قابل دفاع است:

### Direct Elder-care Worker Scope
- پرونده
- ارتباط
- پایش
- ثبت/گزارش Need
- هماهنگی
- Referral
- Follow-up
- Satisfaction follow-up

### Referral-only by Default
هر خدمت تخصصی که انجام آن به صلاحیت حرفه‌ای، تخصص، مجوز یا Provider تخصصی نیاز دارد.

اصل:

`Caregiver coordination role ≠ specialist service authority`

## 9. Proposed Decision Candidate — Three-layer Service Architecture

### Candidate D-0008

- **حوزه:** Business / Service Model
- **تصمیم پیشنهادی:** مدل خدمت نسیم بر سه لایه «سالمندیاری محله‌محور»، «سلامت» و «رفاه و خدمات مکمل» استوار است. سالمندیار نقطه ورود و هماهنگ‌کننده Journey است و نیازهای تخصصی به لایه/Provider تخصصی ارجاع می‌شوند.
- **Boundary:** این تصمیم Service SKU، Provider Type، SLA، Pricing یا Pilot activation هر خدمت را تعیین نمی‌کند.

### Assessment

**Source-supported and recommended for acceptance.**

## 10. Proposed Decision Candidate — Elder-care Worker Service Boundary

### Candidate D-0009

- **حوزه:** Business / Service Boundary
- **تصمیم پیشنهادی:** دامنه مستقیم سالمندیار در فاز اول شامل ارتباط، پایش، تشکیل/به‌روزرسانی پرونده، ثبت و گزارش Need، هماهنگی، Referral، Follow-up و پیگیری رضایت است.
- **قاعده:** خدمات تخصصی سلامت، درمان، پرستاری، توانبخشی تخصصی، سلامت روان، حقوقی و سایر خدمات نیازمند صلاحیت تخصصی، تا زمانی که Contract جداگانه‌ای خلاف آن را تصویب نکرده باشد، **Direct Service سالمندیار محسوب نمی‌شوند**.
- **Boundary:** این تصمیم مشخص نمی‌کند کدام Provider Type مجاز به هر خدمت است.

### Assessment

**Source-supported and recommended for acceptance.**

## 11. Proposed Decision Candidate — Specialist Services Are Network-delivered

### Candidate D-0010

- **حوزه:** Business / Provider Model
- **تصمیم پیشنهادی:** نسیم در فاز اول به‌عنوان اپراتور شبکه، الزاماً ارائه‌دهنده مستقیم خدمات تخصصی نیست. خدمات تخصصی می‌توانند توسط Providerهای تخصصی/ظرفیت‌های شبکه ارائه شوند و نسیم مسئول هماهنگی، Referral، Quality و Follow-up است.
- **Boundary:** این تصمیم نوع قرارداد، Provider onboarding، SLA، تعرفه یا Settlement را تعیین نمی‌کند.

### Assessment

**Source-supported and recommended for acceptance.**

## 12. Phase-1 Catalog Structure — Recommended Frame

برای Catalog اجرایی فاز اول، ساختار پیشنهادی:

### A. Elder-care Operations
- case/profile setup
- regular contact
- monitoring
- need registration
- referral coordination
- follow-up
- satisfaction follow-up

### B. Health Referral Families
- health assessment
- medical
- nursing
- chronic-care
- rehabilitation/specialist care
- mental health

### C. Welfare / Complementary Referral Families
- welfare
- cultural/social
- support
- legal
- rehabilitation
- other approved partner services

این Frame از منبع مشتق می‌شود، اما هنوز Catalog فعال Pilot نیست.

## 13. Decisions Still Required for Actual Pilot Catalog

برای تبدیل Frame به Catalog فعال باید برای هر Service Item مشخص شود:

- Service Name
- Business Definition
- Target Need
- Direct / Referral-only
- Provider Type
- Preconditions
- Required Data
- Consent/Authorization
- Referral Entry Rule
- Completion Evidence
- Quality Criteria
- Availability/Geography
- Funding/Pricing if relevant
- Escalation
- Effective Version

بدون این اطلاعات، Service Item نباید در UI به‌عنوان «خدمت قابل سفارش/اجرا» قطعی نمایش داده شود.

## 14. Health Catalog — Blocking Decisions

برای فاز اول باید مالک محصول تعیین کند کدام‌یک از خانواده‌های زیر واقعاً **فعال** هستند:

- ارزیابی سلامت
- پزشکی
- پرستاری
- بیماری مزمن
- توانبخشی/تخصصی
- سلامت روان

منبع همه را به‌عنوان Service Family نام می‌برد ولی Pilot activation همه آنها را تضمین نمی‌کند.

## 15. Welfare Catalog — Blocking Decisions

همین تصمیم برای این خانواده‌ها لازم است:

- رفاهی
- فرهنگی و اجتماعی
- حمایتی
- حقوقی
- توانبخشی
- سایر خدمات Partner

عبارت «سایر ظرفیت‌ها» نباید به Catalog باز و نامحدود تبدیل شود.

## 16. Rehabilitation Duplication

«توانبخشی» هم در Health و هم در Welfare/Complementary در متن منبع ظاهر می‌شود.

این موضوع نباید بی‌صدا Merge یا Duplicate شود.

قبل از Technical باید تعیین شود:

- یک Service Family مشترک است
- دو Domain متفاوت با Definition متفاوت است
- یا در فاز اول فقط یکی فعال است

### Current status

**BLOCKING — SOURCE DOES NOT RECONCILE THE DUPLICATION**

## 17. Health Assessment Boundary

منبع «ارزیابی سلامت» را Service Family سلامت می‌داند.

اما مشخص نمی‌کند:

- چه کسی انجام می‌دهد
- ابزار چیست
- Clinical vs non-clinical
- آیا سالمندیار فقط Observation دارد یا Assessment تخصصی
- چه Evidence لازم است

بنابراین سالمندیار نباید به‌طور پیش‌فرض مجری «ارزیابی سلامت تخصصی» فرض شود.

## 18. Home Visit — Not Source-confirmed as a Service

فعالیت میدانی سالمندیار در منبع وجود دارد، اما «Home Visit» به‌عنوان Service Item مستقل و قطعی تعریف نشده است.

پس:

- Field activity ممکن است وجود داشته باشد
- Home Visit Service SKU هنوز تصمیم نشده است

## 19. Emergency Service — Not Source-confirmed

منبع فقط آموزش مدیریت شرایط اضطراری را برای سالمندیار ذکر می‌کند.

هیچ‌کدام از این موارد هنوز مصوب نیست:

- 24/7 response
- medical triage
- ambulance coordination contract
- emergency SLA
- emergency provider service

Emergency باید جداگانه در Closure Journey/Safety بسته شود.

## 20. Other Common Services — Explicitly Not Inferred

از Concept نباید این خدمات را خودکار وارد Scope کرد:

- حمل‌ونقل
- تهیه/تحویل دارو
- تغذیه/غذا
- نظافت منزل
- خرید روزانه
- خدمات مالی
- پرداخت نقدی توسط سالمندیار
- تجهیزات پزشکی در منزل

اگر لازم باشند باید Product Decision مستقل بگیرند.

## 21. Provider Type Is Still Open

حتی برای Service Familyهای Source-confirmed، Provider Type دقیق هنوز مشخص نیست.

مثلاً منبع نمی‌گوید:

- ارزیابی سلامت حتماً توسط چه حرفه‌ای انجام شود
- توانبخشی توسط چه نوع Providerی ارائه شود
- خدمات حمایتی توسط چه Organization Typeی انجام شود

این موارد باید در Provider Closure بسته شوند.

## 22. Need-to-Service Mapping Still Open

Service Familyهای منبع Need Taxonomy نهایی نمی‌سازند.

اصل:

`Need identified ≠ automatic service selection`

برای هر Service باید Mapping و Eligibility مصوب وجود داشته باشد.

## 23. AI Boundary in Service Catalog

AI داخلی می‌تواند در Use Case مصوب:

- Service Catalog را برای سالمندیار توضیح دهد
- Candidate Service Family پیشنهاد دهد
- داده ناقص را Flag کند

اما تا Decision بعدی:

- Service را نهایی انتخاب نمی‌کند
- Referral را نهایی ایجاد نمی‌کند
- Provider را نهایی انتخاب نمی‌کند
- Service Eligibility نهایی صادر نمی‌کند

## 24. Catalog Versioning

طبق BC-018/BC-024، Catalog فعال فاز اول باید Versioned باشد.

حداقل باید قابل تشخیص باشد:

- Catalog version
- effective date
- active/inactive service
- changed definition
- old referral linkage
- Need-to-Service mapping version

## 25. Decisions That Can Be Accepted Now Without Inventing Facts

سه Candidate از DC-002 دارای پشتوانه کافی‌اند:

### D-0008 پیشنهادی
**Three-layer Service Architecture**

### D-0009 پیشنهادی
**Caregiver direct boundary = پرونده/ارتباط/پایش/ثبت/Referral/Follow-up؛ خدمات تخصصی Direct نیستند مگر تصمیم جداگانه**

### D-0010 پیشنهادی
**Nasim = network operator; specialist services may be delivered by specialist Providers/network capacities**

هیچ‌یک Service SKU، Pricing یا Pilot activation همه Service Familyها را اختراع نمی‌کند.

## 26. Product-owner Decisions Still Blocking

این موارد هنوز نیازمند تصمیم مستقیم هستند:

1. کدام Health Service Familyها در Pilot فعال‌اند
2. کدام Welfare/Complementary Familyها در Pilot فعال‌اند
3. Definition هر Service Item
4. Rehabilitation duplication resolution
5. Provider Type هر Service
6. Need-to-Service mapping
7. Eligibility per Service
8. Completion evidence
9. Out-of-catalog handling
10. Emergency service boundary
11. آیا Home Visit Service Item است یا فقط Mode of Operation
12. هر Service جدید خارج از متن منبع

## 27. Gate Effect

اگر D-0008 تا D-0010 پذیرفته شوند:

- مرز نقش سالمندیار برای Technical بسیار روشن‌تر می‌شود
- BC-002 بخشی از Blocking خود را می‌بندد
- BC-008 مرز Operator/Provider را تثبیت می‌کند
- اما Technical Entry Gate همچنان **NOT READY** است چون Catalog فعال Pilot و Service Definitions هنوز بسته نشده‌اند.

## 28. Next Closure Packet

گام بعد:

**DC-003 — Roles, Authority & Human Decision Rights Packet**

هدف: تعیین مرز اختیار سالمند، سالمندیار، Supervisor، Provider، کارفرما، سامانه و AI و آماده‌کردن Decisionهای قابل پذیرش برای Decision Register.
