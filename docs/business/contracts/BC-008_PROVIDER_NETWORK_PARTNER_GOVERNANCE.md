# BC-008 — Provider Network, Partner Governance & Service Delivery Contract

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + BC-002 + BC-003 + BC-005 + BC-007
- **Depends on:** BC-002, BC-003, BC-005, BC-007

> این سند چارچوب کسب‌وکاری شبکه ارائه‌دهندگان و شرکای تخصصی نسیم را تعریف می‌کند. هیچ معیار پذیرش، SLA، تعرفه، مدل تسویه، سطح دسترسی داده یا مسئولیت حقوقی که در منبع اولیه تعیین نشده باشد، در این سند نهایی نمی‌شود.

## 1. Provider Network Principle

نسیم یک **اپراتور شبکه خدمات** است و الزاماً ارائه‌دهنده مستقیم همه خدمات تخصصی نیست.

نقش نسیم در سطح منبع اولیه شامل این موارد است:

- طراحی و راهبری شبکه
- ایجاد استانداردها
- توسعه سامانه
- مدیریت کیفیت
- مدیریت قراردادها و شرکای اجرایی
- هماهنگی میان ارائه‌دهندگان خدمت

ارائه خدمات تخصصی می‌تواند توسط شرکای تخصصی انجام شود.

## 2. Source-confirmed Provider Domains

طرح اولیه برای شرکای تخصصی حداقل این حوزه‌ها را پیش‌بینی کرده است:

- خدمات سلامت
- خدمات رفاهی
- خدمات توانبخشی
- خدمات فرهنگی و اجتماعی
- سایر خدمات تخصصی مورد نیاز شبکه

این فهرست Service Catalog نهایی نیست و فقط Domainهای سطح بالا را نشان می‌دهد.

## 3. Provider Role Boundary

Provider تخصصی برای اجرای خدمت تخصصی وارد زنجیره می‌شود.

تفکیک پایه:

- **سالمندیار:** پایش، شناسایی نیاز، ثبت، ارجاع و پیگیری
- **نسیم:** راهبری شبکه، هماهنگی، کیفیت، فناوری و قراردادها
- **Provider:** ارائه خدمت تخصصی در دامنه مصوب

تا تصمیم صریح بعدی، سالمندیار و Provider یک نقش فرض نمی‌شوند.

## 4. Provider Registry — DRAFT BUSINESS NEED

برای مدیریت شبکه در مقیاس، نسیم در آینده نیازمند یک مرجع ثبت و مدیریت Providerها خواهد بود.

این نیاز کسب‌وکاری باید بتواند حداقل این موضوعات را پوشش دهد:

- هویت و نوع Provider
- حوزه/خانواده خدمت
- محدوده جغرافیایی خدمت
- وضعیت همکاری
- ظرفیت اعلام‌شده
- مدارک یا صلاحیت‌های لازم در صورت نیاز
- قرارداد مرتبط
- اطلاعات تماس عملیاتی
- کیفیت و عملکرد
- وضعیت فعال/غیرفعال بودن

ساختار فنی Registry و فیلدهای نهایی هنوز تصمیم نشده‌اند.

## 5. Provider Onboarding — Open Contract

منبع اولیه وجود شرکای تخصصی و مدیریت قراردادها را تأیید می‌کند، اما معیار پذیرش شریک را تعیین نمی‌کند.

برای Onboarding آینده باید حداقل این موارد تصمیم‌گیری شوند:

- معیار صلاحیت
- مدارک لازم
- بررسی اولیه
- نوع قرارداد
- Service coverage
- تعهدات کیفیت
- الزامات داده و محرمانگی
- آموزش یا آشنایی با فرآیند نسیم
- شرایط فعال‌سازی
- دوره بازبینی
- شرایط تعلیق یا خاتمه

تا زمان تصمیم نهایی، هیچ Provider Type نباید فقط با ثبت نام، «مجاز به خدمت» تلقی شود.

## 6. Referral-to-Provider Boundary

Referral به Provider فقط زمانی معنا دارد که:

- نیاز معتبر در مسیر Business ثبت شده باشد؛
- Service Family یا Service Item مناسب مشخص باشد؛
- Provider مجاز برای آن خدمت وجود داشته باشد؛
- شرایط ارجاع مصوب رعایت شده باشد.

اما هنوز تعیین نشده است:

- چه کسی Provider را انتخاب می‌کند
- آیا سالمند حق انتخاب دارد
- آیا سالمندیار پیشنهاد می‌دهد یا تصمیم می‌گیرد
- آیا AI صرفاً پیشنهاد می‌دهد یا اصلاً در انتخاب نقش دارد
- آیا Provider می‌تواند Referral را رد کند
- در نبود ظرفیت چه می‌شود
- Re-routing چگونه انجام می‌شود

## 7. Provider Capacity — DRAFT CONCEPT

برای جلوگیری از ارجاع غیرقابل انجام، شبکه در آینده باید بتواند مفهوم Capacity را مدیریت کند.

موضوعات باز:

- واحد ظرفیت
- ظرفیت روزانه/هفتگی/ماهانه
- ظرفیت جغرافیایی
- ظرفیت بر اساس Service
- مهلت پاسخ به Referral
- ظرفیت اضطراری
- توقف موقت پذیرش

هیچ مدل عددی یا SLA در این مرحله تصویب نشده است.

## 8. Service Delivery Evidence

نسیم برای پیگیری خدمت باید بتواند تشخیص دهد که Provider چه خدمتی را انجام داده یا اعلام کرده است.

در آینده برای هر Service باید حداقل مشخص شود:

- Completion criteria
- Evidence type
- Who records it
- Who verifies it
- Date/time
- Outcome/Result fields در صورت نیاز
- Exception / failed-delivery reason

منبع اولیه Completion Evidence را تعریف نکرده است.

## 9. Quality Governance

منبع اولیه تأکید می‌کند که توسعه شبکه نباید به کاهش کیفیت منجر شود و کنترل کیفیت، ممیزی دوره‌ای، آموزش بازآموزی و پایش داده از ابزارهای حفظ کیفیت هستند.

در شبکه Providerها، مدل کیفیت آینده باید بتواند حداقل این حوزه‌ها را پوشش دهد:

- کیفیت ارائه خدمت
- رضایت سالمند
- زمان پاسخ
- رعایت استانداردها
- شکایت و رخداد
- تکرار خطا
- نیاز به بازآموزی
- تعلیق یا بازبینی همکاری

Thresholdها و Scoreهای عددی هنوز تصمیم نشده‌اند.

## 10. Provider Performance

برای هر Provider باید در آینده امکان مشاهده عملکرد در چارچوب مصوب وجود داشته باشد، اما KPI نهایی هنوز باز است.

Candidate dimensions برای تصمیم‌گیری بعدی:

- Referral response
- Service completion
- Timeliness
- Complaint rate
- Satisfaction
- Quality review result
- Data completeness
- Rework / repeat service

این موارد صرفاً ابعاد طراحی هستند، نه KPIهای مصوب.

## 11. Data-sharing Boundary

Provider فقط باید به داده‌ای دسترسی داشته باشد که برای Purpose خدمت مجاز است.

اصل کسب‌وکاری:

`Provider Access ≠ Full Elder Record Access`

سطح دقیق داده قابل اشتراک باید در Data Access Matrix و Contract آینده تعیین شود.

همچنین داده‌ای که Provider در مسیر خدمت ثبت می‌کند، از منظر:

- Provenance
- Official record status
- Training eligibility
- Retention
- Audit

باید از قواعد BC-007 تبعیت کند.

## 12. Provider-generated Data

داده‌ای که Provider تولید می‌کند باید از سایر منشأها قابل تفکیک باشد.

حداقل Provenance مورد نیاز در آینده:

- Provider identity
- Service/referral context
- Time
- Recording actor
- Data category
- Verification/review status در صورت نیاز

وجود داده Provider به معنی مجاز بودن آن برای Training AI نیست.

## 13. Complaint & Incident Boundary

طرح اولیه بر کیفیت، رضایت و مدیریت ریسک تأکید دارد، اما Workflow شکایت Provider را تعریف نمی‌کند.

برای Contract آینده باید تعیین شود:

- چه کسی شکایت را ثبت می‌کند
- چه کسی رسیدگی می‌کند
- Provider چه مهلتی برای پاسخ دارد
- چه زمانی Escalation رخ می‌دهد
- چه زمانی Provider تعلیق می‌شود
- Case-specific remedy چیست
- آیا Referralهای باز منتقل می‌شوند

## 14. Financial Boundary

منبع اولیه می‌گوید نسیم قراردادها و شرکای اجرایی را مدیریت می‌کند، اما مدل مالی رابطه با Provider را تعریف نکرده است.

هنوز تصمیم نشده است:

- Pricing
- Tariff
- Fee
- Commission
- Reimbursement
- Settlement cycle
- Invoice model
- Co-payment
- Insurance claim
- Penalty/credit
- Payment authorization

هیچ‌یک نباید از Service Name یا Provider Type استنتاج شوند.

## 15. Contract Lifecycle — DRAFT FRAME

برای هر Provider Contract در آینده باید بتوان حداقل این مراحل مفهومی را مدیریت کرد:

`Candidate → Reviewed → Contracted → Activated → Monitored → Suspended/Ended`

این فقط Frame برای تحلیل Business است و State Machine نهایی محسوب نمی‌شود.

## 16. Network Resilience

از آنجا که منبع اولیه ریسک ناهماهنگی شرکا و ضعف نظام ارجاع را مطرح می‌کند، طراحی آینده باید بتواند برای موارد زیر پاسخ داشته باشد:

- Provider unavailable
- Capacity exhausted
- Service failure
- Repeated quality issue
- Contract suspension
- Geographic gap
- Referral rerouting

روش دقیق مدیریت این وضعیت‌ها هنوز تصمیم نشده است.

## 17. AI Boundary in Provider Network

با توجه به D-0004 و BC-006:

- AI می‌تواند در آینده برای تحلیل یا پیشنهاد به سالمندیار کمک کند.
- AI تا تصمیم صریح، Provider را به‌صورت الزام‌آور انتخاب نمی‌کند.
- AI نباید Provider را فعال/تعلیق کند.
- AI نباید کیفیت Provider را به‌صورت نهایی تأیید کند.
- AI-generated recommendation باید از Human Decision قابل تفکیک باشد.

## 18. Explicit Non-Decisions

BC-008 موارد زیر را تصویب نمی‌کند:

- Provider selection algorithm
- Provider ranking
- Auto-routing
- SLA عددی
- Tariff
- Settlement model
- Contract template
- Licensing criteria
- Scoring formula
- Penalty formula
- Geographic allocation rule
- Exclusive provider model
- Provider access to full elder record
- AI-based autonomous provider selection

## 19. Open Decisions Required to Accept BC-008

1. Provider types
2. Onboarding criteria
3. Qualification/credential rules
4. Provider Registry fields
5. Service-to-provider eligibility mapping
6. Referral acceptance/rejection rules
7. Provider selection rule
8. Elder choice rule
9. Capacity model
10. Completion evidence
11. Quality standards
12. Provider KPI framework
13. Complaint/incident workflow
14. Suspension/termination policy
15. Data-sharing contract
16. Financial/settlement model
17. Re-routing/fallback policy
18. AI role in provider recommendation

## 20. Downstream Constraints

تا پیش از Accepted شدن BC-008:

- Technical نباید Provider ranking یا auto-routing اختراع کند.
- Provider Registry نباید وضعیت «مجاز» را بدون Business rule قطعی کند.
- UI نباید Provider را «بهترین» یا «پیشنهاد قطعی» نشان دهد مگر Rule مصوب وجود داشته باشد.
- Provider نباید به‌صورت پیش‌فرض به پرونده کامل سالمند دسترسی داشته باشد.
- Billing/Settlement نباید از Referral lifecycle حدس زده شود.
- AI نباید Provider selection نهایی یا Contract activation انجام دهد.
