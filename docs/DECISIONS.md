# NASIM Decision Register

این فایل مرجع رسمی ثبت تصمیمات پروژه «نسیم» است.

## روش ثبت تصمیم‌ها

از این تاریخ به بعد، تصمیم‌های تأییدشده پروژه در این مخزن ثبت می‌شوند. هر تصمیم جدید باید حداقل شامل تاریخ، حوزه، وضعیت، متن تصمیم و در صورت نیاز منطق یا اثر آن باشد. اگر تصمیمی تغییر کند، تصمیم قبلی حذف نمی‌شود؛ بلکه با وضعیت **Superseded** مشخص و تصمیم جایگزین ثبت می‌شود تا تاریخچه تصمیم‌گیری حفظ شود.

---

## D-0001 — نام و مخفف پروژه

- **تاریخ:** 2026-10-06
- **حوزه:** Product / Identity
- **وضعیت:** Accepted
- **تصمیم:** نام پروژه «نسیم» است.
- **عبارت کامل:** «نظام سالمند‌یاری محله‌محور»
- **یادداشت:** این نام جایگزین نام قبلی «شمیم» برای ادامه پروژه می‌شود.

## D-0002 — مخزن مرجع تصمیمات

- **تاریخ:** 2026-10-06
- **حوزه:** Governance
- **وضعیت:** Accepted
- **تصمیم:** مخزن `mahdimarzooghi4-debug/nasim` مرجع رسمی ثبت تصمیمات پروژه نسیم است.
- **قاعده:** از این پس تصمیمات تأییدشده پروژه باید در همین مخزن ثبت و نگهداری شوند.


## D-0003 — فرآیند مادر توسعه محصول

- **تاریخ:** 2026-10-06
- **حوزه:** Product / Delivery Governance
- **وضعیت:** Accepted
- **تصمیم:** توسعه نسیم بر اساس فرآیند مادر زیر انجام می‌شود:
  `Business → Technical → Scrum/Product Backlog → Sprint → Code → Code Review → Stage → QA/Testing → Release Approval → Production → Monitoring → Improvement`
- **قاعده:** عبور از هر مرحله به مرحله بعد باید بر مبنای خروجی مرحله قبل انجام شود و تصمیم‌های محصولی/فنی مصوب در همین مخزن ثبت شوند.


## D-0004 — هوش مصنوعی داخلی نسیم

- **تاریخ:** 2026-10-06
- **حوزه:** Product / AI
- **وضعیت:** Accepted
- **تصمیم:** نسیم باید دارای یک هوش مصنوعی داخلی باشد که در کنار «سالمند» و «سالمندیار» به‌عنوان دستیار عمل کند.
- **یادگیری:** این هوش مصنوعی باید از داده‌های تولیدشده در نسیم برای آموزش/بهبود خودکار استفاده کند.
- **مرز تصمیم فعلی:** مدل، الگوریتم، معماری Training، نوع داده مجاز، رضایت و حریم خصوصی، نحوه ارزیابی، Gate انتشار نسخه جدید، سطح اختیار دستیار و اینکه چه تصمیم‌هایی نیازمند تأیید انسان هستند هنوز تعیین نشده‌اند و نباید در Technical یا Code اختراع شوند.
- **منبع تصمیم:** تصمیم مستقیم مالک محصول؛ این قابلیت در طرح‌نامه اولیه «شمیم» تعریف نشده بود و یک توسعه جدید برای نسیم است.


## D-0005 — AI از روز اول و چرخه خودکار Dataset

- **تاریخ:** 2026-10-06
- **حوزه:** Product / AI / Learning
- **وضعیت:** Accepted
- **تصمیم:** هوش مصنوعی داخلی نسیم از **روز اول بهره‌برداری عملیاتی** جزئی از محصول است و قابلیت AI به فاز یا توسعه بعدی موکول نمی‌شود.
- **Dataset Lifecycle:** نسیم باید به‌صورت مستمر و خودکار، از داده‌های تولیدشده و مجاز، Datasetهای جدید/نسخه‌های جدید Dataset ایجاد و به‌روزرسانی کند تا چرخه یادگیری AI دائماً تغذیه شود.
- **قاعده:** ایجاد و Version شدن Dataset یک فرآیند خودکار و پیوسته است؛ انتخاب داده مجاز برای ورود به این چرخه همچنان تابع Data Governance و Training Eligibility مصوب است.
- **مرز:** خودکار بودن Dataset Lifecycle به معنی Auto-Promotion مدل به Production یا حذف Evaluation/Governance نیست؛ سیاست Training، Evaluation و Promotion باید جداگانه تعیین شود.


## D-0118 — بستن تصمیم‌ها در زمان نیاز، نه به‌صورت اجباری و یک‌جا

- **تاریخ:** 2026-10-06
- **حوزه:** Product / Decision Governance
- **وضعیت:** Accepted
- **تصمیم:** تصمیم‌های Business که هنوز زمان یا Context لازم برای تعیین آنها نرسیده است، به‌صورت **OPEN** باقی می‌مانند و فقط زمانی بسته می‌شوند که در جریان واقعی طراحی، پایلوت یا Gate مربوطه نیاز به تصمیم آنها ایجاد شود؛ مالک محصول مجبور به پاسخ‌دادن دسته‌ای و پیشاپیش به همه Open Questionها نیست.
- **قاعده:** `OPEN ≠ DEFERRED ≠ ACCEPTED`. باز ماندن یک تصمیم به معنی Deferred شدن یا پذیرفته‌شدن آن نیست.
- **عدم اختراع:** تا زمانی که تصمیمی OPEN است، Technical، Backlog و Code حق ندارند مقدار یا Policy آن را حدس بزنند.
- **Gate:** هنگام عبور از هر Gate، فقط Blockerهای لازم برای همان Gate باید Accepted یا صریحاً Deferred شده باشند.
- **اثر:** BR-002/BR-003 و Input Sheetهای مشابه به‌عنوان مرجع Open Decisionها حفظ می‌شوند، اما نباید روند کار را با اجبار به پاسخ فوری متوقف کنند.

## D-0119 — TS-03 از بعد از Enrollment آغاز می‌شود

- **تاریخ:** 2026-10-07
- **حوزه:** Product / TS-03 Core Case / Journey Scope
- **وضعیت:** Accepted
- **تصمیم:** در Technical Slice اول، **TS-03 — Core Case / Journey Foundation** از **بعد از Enrollment** آغاز می‌شود. Case/Profile در این Slice فقط برای سالمندی طراحی می‌شود که قبلاً توسط یک فرآیند Business بالادستی وارد/پذیرفته شده است.
- **مرز:** Enrollment Eligibility، قواعد پذیرش، سن، وضعیت حمایتی، اولویت‌بندی، Waiting List و سایر Ruleهای Enrollment در Scope فعلی TS-03 نیستند و همچنان OPEN می‌مانند تا Context مربوط به Enrollment آنها را Trigger کند.
- **قاعده عدم‌اختراع:** TS-03 نباید Eligibility را اجرا، بازتعریف یا از روی Case creation استنتاج کند؛ وجود Case در این Slice فقط نشان می‌دهد upstream enrollment قبلاً انجام شده است.
- **اثر بر Candidateها:** D-0006 به‌علت این تصمیم برای Gate فعلی TS-03 دیگر Blocker نیست و Accepted/Deferred نمی‌شود؛ وضعیت Candidate آن بدون تغییر باقی می‌ماند.
- **منبع تصمیم:** انتخاب صریح Product Owner در SGP-001، Q1 = Option A.

## D-0120 — مرز Journey اولیه TS-03

- **تاریخ:** 2026-10-07
- **حوزه:** Product / TS-03 Core Case / Journey Scope
- **وضعیت:** Accepted
- **تصمیم:** در TS-03، Journey اولیه به این Scope محدود می‌شود:
  `Contact → Case/Profile → Monitoring → Observation / Need capture`
- **خارج از Scope فعلی TS-03:** Referral، Service Delivery، Follow-up، Satisfaction، Reassessment، Need Resolution و Outcome.
- **قاعده:** خارج‌بودن این مراحل از TS-03 به معنی حذف یا Deferred شدن آنها در محصول نیست؛ فقط Technical Slice اول آنها را طراحی نمی‌کند.
- **اثر بر Candidateها:** D-0017 برای Gate فعلی TS-03 فقط به‌عنوان Source/Reference باقی می‌ماند و با این تصمیم به‌طور کامل Accepted نمی‌شود؛ بخش بعدی Journey همچنان OPEN است تا Slice مربوطه آن را Trigger کند.
- **منبع تصمیم:** تأیید صریح Product Owner در SGP-001، Q2.

## D-0121 — مالک عملیاتی Case و قاعده Assignment در TS-03

- **تاریخ:** 2026-10-07
- **حوزه:** Product / TS-03 Case Ownership
- **وضعیت:** Accepted
- **تصمیم:** در TS-03، **سالمندیار Primary Operational Case Owner / Contact** است.
- **Assignment:** تخصیص اولیه سالمندیار و هرگونه Reassignment/Substitution باید توسط یک **نقش بالادستی/عملیاتیِ مجاز** انجام شود؛ Self-assignment یا تغییر مالکیت صرفاً از روی عنوان شغلی فرض نمی‌شود.
- **Audit:** هر Reassignment/Substitution باید حداقل دارای **Reason + Actor + Time + Audit Trail** باشد.
- **مرز اختیار:** این تصمیم Business responsibility را مشخص می‌کند و به‌خودی‌خود Permission Model یا RBAC نمی‌سازد. نگاشت دقیق «نقش بالادستی مجاز» به Role/Permission مشخص همچنان OPEN است و در Context Identity/Authorization بسته می‌شود.
- **قاعده:** `Case Ownership ≠ Authorization` و `Role Title ≠ Permission`.
- **منبع تصمیم:** تأیید صریح Product Owner در SGP-001، Q3.

## D-0122 — حداقل Data Classهای Case/Profile در TS-03

- **تاریخ:** 2026-10-07
- **حوزه:** Product / TS-03 Case/Profile Data Boundary
- **وضعیت:** Accepted
- **تصمیم:** حداقل Data Classهای موردنیاز TS-03 به این شش گروه محدود می‌شوند:
  1. Elder identity/reference
  2. Contact information
  3. Case administrative context
  4. Interaction / Monitoring record
  5. Observation / Need capture
  6. Caregiver assignment / history
- **خارج از Scope فعلی TS-03:** Medical dataset، Provider data، Outcome data و AI-training fields.
- **مرز:** این تصمیم فقط Data Classهای Business را مشخص می‌کند؛ Field-level schema، validation، storage model، identifiers و technical relationships هنوز Technical Decision هستند.
- **داده و AI:** خارج‌بودن AI-training fields از TS-03 به معنی تصمیم درباره Training Eligibility این Data Classها نیست؛ Training Eligibility همچنان OPEN است.
- **دسترسی:** این تصمیم هیچ Access Permission ایجاد نمی‌کند؛ Access Boundary جداگانه در Q6 بسته می‌شود.
- **منبع تصمیم:** تأیید صریح Product Owner در SGP-001، Q4.

## D-0123 — حداقل Access Boundary برای TS-03

- **تاریخ:** 2026-10-07
- **حوزه:** Product / TS-03 Data Access Boundary
- **وضعیت:** Accepted
- **تصمیم:** در TS-03، دسترسی به Case/Profile فقط به Actorهایی محدود می‌شود که برای اجرای Scope همین Slice نیاز عملیاتی مستقیم دارند.
- **سالمندیار:** فقط سالمندیار Assign‌شده به Case می‌تواند به داده‌های TS-03 موردنیاز برای Contact، Monitoring و Observation/Need capture دسترسی داشته باشد.
- **نقش بالادستی/عملیاتی مجاز:** فقط به میزانی که برای Assignment/Reassignment و نظارت عملیاتی لازم است دسترسی دارد.
- **خارج از Scope فعلی TS-03:** Elder self-access، Family/Representative access، Provider access، Employer access و AI access.
- **قاعده:** وجود داده در Case به‌خودی‌خود هیچ Access Right ایجاد نمی‌کند؛ `Data Existence ≠ Access Permission`.
- **مرز:** این تصمیم فقط Business access boundary را تعیین می‌کند. RBAC/ABAC model، permission identifiers، policy enforcement و authentication/authorization implementation در Technical تعیین می‌شوند.
- **اثر:** Access برای Actorهای خارج از Scope رد یا Deferred نشده است؛ فقط در TS-03 تعریف نمی‌شود و در Context مربوطه OPEN می‌ماند.
- **منبع تصمیم:** تأیید صریح Product Owner در SGP-001، Q6.

## D-0124 — اختیار تسریع تصمیم‌گیری تا مرز Code

- **تاریخ:** 2026-10-07
- **حوزه:** Product / Delivery Governance
- **وضعیت:** Accepted
- **تصمیم:** برای تسریع ادامه کار، مالک محصول با گزینه‌های پیشنهادی دستیار در تصمیم‌های باقی‌مانده تا رسیدن به مرز **Code** موافق است و لازم نیست برای هر انتخاب کم‌ریسک و مستند، تأیید جداگانه تکرار شود.
- **شرط:** این اختیار فقط زمانی معتبر است که تصمیم از اسناد پروژه، Decisionهای Accepted و Scope جاری قابل استنتاج/طراحی باشد و Fact، Policy، عدد، اختیار حقوقی، داده بیرونی، Credential یا تعهد نهادیِ نامعلوم اختراع نشود.
- **Gate:** هیچ Gate حذف نمی‌شود؛ Business → Technical → Backlog → Sprint همچنان باید به ترتیب ثبت شوند.
- **توقف اجباری:** اگر تصمیم به داده بیرونی/حقوقی/نهادی واقعی نیاز داشته باشد یا چند گزینه اثر تجاری/حقوقی materially متفاوت داشته باشند و Evidence کافی وجود نداشته باشد، موضوع OPEN می‌ماند.
- **Code boundary:** طبق توافق قبلی، قبل از ورود به Code باید صریحاً به مالک محصول اعلام شود که ادامه در Codex انجام شود.
- **منبع تصمیم:** پیام صریح مالک محصول: «من با همه تصمیمات تو موافقم زودتر کار تموم کن».

## D-0125 — Correction / History در TS-03

- **تاریخ:** 2026-10-07
- **حوزه:** Product / TS-03 Record Integrity
- **وضعیت:** Accepted
- **تصمیم:** هیچ Correction در Case/Profile/Interaction/Observation نباید مقدار قبلی را به‌صورت Silent Overwrite حذف کند.
- **History:** مقدار/نسخه قبلی باید قابل ردیابی باقی بماند.
- **Correction metadata:** هر Correction باید حداقل Actor + Time + Reason را ثبت کند.
- **Provenance:** هر Provenance/Evidence link مرتبط باید در زنجیره اصلاح حفظ شود.
- **مرز فنی:** روش دقیق پیاده‌سازی مانند append-only revision، temporal model یا history table یک Technical Decision است.
- **منبع تصمیم:** پیشنهاد ثبت‌شده در SGP-001 Q5، پذیرفته‌شده تحت D-0124.

## D-0126 — Deferral محدودِ Named Role Mapping برای Assignment

- **تاریخ:** 2026-10-07
- **حوزه:** Product / TS-03 → TS-05 Boundary
- **وضعیت:** Accepted
- **تصمیم:** نگاشت دقیق «نقش بالادستی/عملیاتی مجاز» برای Assignment/Reassignment به یک Role/Permission نام‌گذاری‌شده، از TS-03 خارج و به **TS-05 — Identity / Role / Authorization Foundation** منتقل می‌شود.
- **Owner:** Product Owner.
- **Future Gate:** TS-05 Slice Gate.
- **Constraint for TS-03:** Technical فقط می‌تواند یک capability/authorization predicate انتزاعی برای Assignment/Reassignment طراحی کند و حق ندارد عنوان شغلی مشخصی را به‌عنوان Permission نهایی Hard-code کند.
- **اثر:** TS-03 می‌تواند با Business authority class تعریف‌شده در D-0121 جلو برود، بدون اینکه RBAC نهایی اختراع شود.

## D-0012 — Caregiver Base Responsibility Boundary

- **تاریخ:** 2026-10-07
- **حوزه:** Product / Roles & Authority
- **وضعیت:** Accepted
- **تصمیم:** دامنه پایه سالمندیار شامل ارتباط، پایش، ثبت، هماهنگی، Referral و Follow-up است.
- **مرز:** از این مسئولیت‌ها اختیار تخصصی پزشکی/درمانی، اختیار مالی، Provider activation یا Eligibility نهایی استنتاج نمی‌شود.
- **منبع:** DC-003؛ Source-supported boundary؛ پذیرفته‌شده تحت D-0124.

## D-0013 — Role Title Does Not Create Permission

- **تاریخ:** 2026-10-07
- **حوزه:** Product / Roles & Authority
- **وضعیت:** Accepted
- **تصمیم:** عنوان شغلی یا جایگاه در مسیر رشد، به‌تنهایی Permission یا Approval Right ایجاد نمی‌کند.
- **قاعده:** Authority هر سطح باید در Authority Matrix مستقل تصویب شود.
- **منبع:** DC-003؛ governance-safe boundary؛ پذیرفته‌شده تحت D-0124.

## D-0014 — System Is Not Independent Business Authority

- **تاریخ:** 2026-10-07
- **حوزه:** Product / System Authority
- **وضعیت:** Accepted
- **تصمیم:** سامانه قواعد مصوب را اجرا و ثبت می‌کند و به‌صرف خودکار بودن Workflow، صاحب مستقل Business Decision Right نمی‌شود.
- **منبع:** DC-003؛ پذیرفته‌شده تحت D-0124.

## D-0015 — Human / System / AI / Automation Traceability

- **تاریخ:** 2026-10-07
- **حوزه:** Product / Audit & AI Governance
- **وضعیت:** Accepted
- **تصمیم:** Actionهای مهم نسیم باید از نظر منشأ Human / System / AI / Automation قابل تفکیک و Audit باشند.
- **قاعده:** AI suggestion، System execution و Human decision نباید به‌صورت یک Actor مبهم ثبت شوند.
- **منبع:** DC-003؛ همسو با D-0004/D-0005؛ پذیرفته‌شده تحت D-0124.

## D-0021 — Purpose-Limited Data Use

- **تاریخ:** 2026-10-07
- **حوزه:** Product / Data Governance
- **وضعیت:** Accepted
- **تصمیم:** هر Data Class فقط برای Purpose مصوب استفاده می‌شود.
- **قاعده:** Service Delivery، Reporting، AI Runtime و AI Training Purposeهای مستقل‌اند و مجوز یکی، مجوز دیگری نیست.
- **منبع:** DC-005؛ پذیرفته‌شده تحت D-0124.

## D-0028 — Provenance Must Be Preserved

- **تاریخ:** 2026-10-07
- **حوزه:** Product / Data Governance / Audit
- **وضعیت:** Accepted
- **تصمیم:** منشأ داده باید میان Elder، Family، Caregiver، Provider، System، AI و Human-reviewed AI قابل تفکیک و در Audit/Dataset lineage حفظ شود.
- **مرز:** این تصمیم به‌خودی‌خود Access یا Training Eligibility ایجاد نمی‌کند.
- **منبع:** DC-005؛ پذیرفته‌شده تحت D-0124.

## D-0127 — ورود TS-03 به مرحله Technical

- **تاریخ:** 2026-10-07
- **حوزه:** Delivery Governance / TS-03
- **وضعیت:** Accepted
- **تصمیم:** بر اساس SG-001، Slice **TS-03 — Core Case / Journey Foundation** با نتیجه **READY FOR THIS SLICE WITH EXPLICIT DEFERRAL** وارد مرحله **Technical** می‌شود.
- **Deferral:** Named supervisory Role/Permission mapping مطابق D-0126 به TS-05 منتقل شده است.
- **مرز:** این تصمیم فقط TS-03 را وارد Technical می‌کند؛ Global Business → Technical Gate برای Sliceهای دیگر Pass نشده است.
- **قاعده:** هیچ Code تا تکمیل Technical، Product Backlog و Sprint برای TS-03 آغاز نمی‌شود.

## D-0128 — پذیرش Technical Baseline و ورود TS-03 به Product Backlog

- **تاریخ:** 2026-10-07
- **حوزه:** Technical / Delivery Governance / TS-03
- **وضعیت:** Accepted
- **تصمیم:** Technical Baseline ثبت‌شده در `T-001_TS03_CORE_CASE_JOURNEY_TECHNICAL_BASELINE.md` برای TS-03 پذیرفته شد و بر اساس TG-001، این Slice وارد مرحله **Scrum/Product Backlog** می‌شود.
- **معماری:** modular monolith، backend-first.
- **Stack:** Python 3.12، FastAPI، PostgreSQL، async SQLAlchemy، Alembic، Pydantic؛ Pytest/Ruff/Pyright برای quality.
- **Integrity:** correctionها با append-only superseding revision؛ audit و outbox transactional.
- **Authorization:** ActorContext + capability checks؛ named Role mapping مطابق D-0126 در TS-05.
- **مرز:** هیچ Referral/Provider/Outcome/AI/Enrollment/Emergency behavior وارد TS-03 نمی‌شود.
- **منبع:** T-001 + TG-001؛ پذیرفته‌شده تحت D-0124.

## D-0129 — پذیرش Sprint 001 و ورود TS-03 به Code

- **تاریخ:** 2026-10-07
- **حوزه:** Delivery Governance / TS-03
- **وضعیت:** Accepted
- **تصمیم:** Product Backlog PB-001 و Sprint Plan ثبت‌شده در `SPRINT-001_TS03_CORE_CASE_JOURNEY_FOUNDATION.md` پذیرفته شدند و TS-03 مجاز است وارد مرحله **Code** شود.
- **Code scope:** فقط BL-001…BL-012 در محدوده TS-03.
- **مرز:** هیچ Enrollment/Referral/Provider/Outcome/AI/Emergency/Named-RBAC behavior نباید در Code این Sprint اضافه شود.
- **Quality:** Code Review، Stage، QA و Release همچنان Gateهای مستقل بعدی هستند.
- **Codex handoff:** طبق قاعده پروژه، اجرای Code باید در Codex انجام شود؛ این Chat در مرز Code متوقف می‌شود.
- **منبع:** T-001 + TG-001 + PB-001 + SPRINT-001؛ پذیرفته‌شده تحت D-0124.

## D-0130 — محیط Stage فعلاً وجود ندارد

- **تاریخ:** 2026-10-07
- **حوزه:** Delivery Governance / Environment
- **وضعیت:** Accepted
- **تصمیم:** در وضعیت فعلی پروژه نسیم، محیط **Stage** provision نشده و قابل استفاده نیست.
- **اثر:** پس از Merge و Code Review، نمی‌توان Stage Admission، Stage validation یا Stage-based QA را Pass‌شده تلقی کرد.
- **فرآیند مادر:** D-0003 تغییر نمی‌کند و Stage از فرآیند حذف نشده است؛ فقط محیط Stage در حال حاضر **UNAVAILABLE** است.
- **قاعده:** نبود Stage به معنی عبور خودکار از Stage Gate نیست. QA/Release/Production نباید بر مبنای Stage فرضی یا ساختگی ادعا شوند.
- **مسیر بعدی:** یا باید Stage Environment به‌صورت واقعی ساخته و Gate آن اجرا شود، یا مالک محصول بعداً یک تغییر صریح در فرآیند/Scope تصویب کند.
- **منبع تصمیم:** اعلام صریح مالک محصول: «الان استیج نداریم».



## D-0036 — Provider نقش تخصصی مستقل است

- **تاریخ:** 2026-10-07
- **حوزه:** Business / Provider Network
- **وضعیت:** Accepted
- **تصمیم:** Provider تخصصی Actor مستقلی از سالمندیار و اپراتور نسیم است و فقط در دامنه Service/Contract مصوب می‌تواند خدمت تخصصی ارائه کند.
- **مرز:** عضویت یا ثبت Provider در شبکه به‌خودی‌خود Full Case Authority یا Full Elder Record Access ایجاد نمی‌کند.
- **منبع:** DC-007؛ source-supported؛ پذیرفته‌شده تحت D-0124.

## D-0037 — Registry Entry ≠ Operational Activation

- **تاریخ:** 2026-10-07
- **حوزه:** Business / Provider Governance
- **وضعیت:** Accepted
- **تصمیم:** ثبت Provider در Registry به‌تنهایی به معنی مجاز بودن ارائه خدمت یا استفاده عملیاتی در Referral نیست.
- **مرز:** Qualification، مدارک، Reviewer/Approver، Activation Workflow و Service eligibility همچنان OPEN هستند.
- **منبع:** DC-007؛ governance-safe boundary؛ پذیرفته‌شده تحت D-0124.

## D-0038 — Provider Eligibility ≠ Provider Selection

- **تاریخ:** 2026-10-07
- **حوزه:** Business / Referral / Provider
- **وضعیت:** Accepted
- **تصمیم:** واجد شرایط بودن Provider برای یک Service، به‌تنهایی Provider Selection نهایی ایجاد نمی‌کند.
- **مرز:** Rule انتخاب Provider و نقش Elder/Caregiver/Supervisor/AI در انتخاب همچنان OPEN است.
- **منبع:** DC-007؛ پذیرفته‌شده تحت D-0124.

## D-0039 — Provider Response باید صریح و قابل Audit باشد

- **تاریخ:** 2026-10-07
- **حوزه:** Business / Referral Response
- **وضعیت:** Accepted
- **تصمیم:** هرگاه در Slice آینده Referral واقعاً به Provider ارسال شود، پاسخ Provider و پذیرش/عدم پذیرش باید صریح و قابل ردیابی باشد.
- **مرز:** State names، SLA، timeout و rejection taxonomy همچنان OPEN هستند.
- **منبع:** DC-007؛ پذیرفته‌شده تحت D-0124.

## D-0040 — Provider Result ≠ Final Elder Outcome

- **تاریخ:** 2026-10-07
- **حوزه:** Business / Provider / Outcome
- **وضعیت:** Accepted
- **تصمیم:** Provider می‌تواند در آینده Service Result/Completion Evidence ثبت کند، اما این داده به‌تنهایی Outcome نهایی سالمند یا Need Resolution را تعیین نمی‌کند.
- **منبع:** DC-007؛ پذیرفته‌شده تحت D-0124.

## D-0041 — Provider Failure نباید Referral را بی‌صدا ببندد

- **تاریخ:** 2026-10-07
- **حوزه:** Business / Referral Failure
- **وضعیت:** Accepted
- **تصمیم:** عدم پاسخ، رد، عدم ظرفیت یا Service Failure از Provider نباید Referral را به‌صورت ضمنی موفق/بسته تلقی کند.
- **مرز:** Retry، reroute، escalation، notification و closure behavior همچنان OPEN هستند.
- **منبع:** DC-007؛ پذیرفته‌شده تحت D-0124.

## D-0042 — Provider Ranking تصمیم پیش‌فرض ایجاد نمی‌کند

- **تاریخ:** 2026-10-07
- **حوزه:** Business / Provider Governance
- **وضعیت:** Accepted
- **تصمیم:** تا زمان تصویب Rule جداگانه، Ranking یا Score Provider نباید به‌صورت خودکار Provider Selection، Suspension یا Contract Decision ایجاد کند.
- **منبع:** DC-007؛ پذیرفته‌شده تحت D-0124.

## D-0131 — Sprint 004 فقط Provider Candidate Registry Foundation است

- **تاریخ:** 2026-10-07
- **حوزه:** Delivery Governance / Provider Foundation
- **وضعیت:** Accepted
- **تصمیم:** Slice بعدی به یک **Provider Candidate Registry Foundation** پیش‌عملیاتی محدود می‌شود؛ ثبت یک Candidate فقط هویت/Provenance ثبت‌شده را ایجاد می‌کند و هیچ Activation، Eligibility، Service mapping، Referral destination، Capacity، Contract authority یا Data Access ایجاد نمی‌کند.
- **قاعده:** Candidate Registry عمداً قبل از TS-06 عملیاتی قرار می‌گیرد و نباید به‌عنوان عبور از TS-06 Provider Network Gate تلقی شود.
- **OPEN باقی می‌ماند:** Provider Types فاز/Pilot، Qualification/Onboarding، Activation Authority، Service-to-Provider mapping، Provider Selection، Referral Acceptance/Rejection، Capacity، Completion Evidence، Provider Data Access، Suspension/Termination، Financial/Settlement و Integration.
- **منبع:** BC-008 + DC-007 + D-0036…D-0042؛ پذیرفته‌شده تحت D-0124.


## D-0132 — Sprint 005 فقط Provider Qualification Evidence Foundation است

- **تاریخ:** 2026-10-07
- **حوزه:** Delivery Governance / Provider Qualification
- **وضعیت:** Accepted
- **تصمیم:** Slice بعدی فقط ثبت شواهد Qualification برای Provider Candidate را فراهم می‌کند؛ ثبت Evidence به معنی Qualified شدن، Approval، Activation، Service Eligibility یا Provider Selection نیست.
- **قاعده:** `Qualification Evidence ≠ Qualification Decision ≠ Activation`.
- **محدوده مجاز:** ثبت immutable و provenance-preserving یک Evidence Reference توصیفی برای Provider Candidate موجود، Audit/Outbox/Idempotency، و read-only inspection.
- **OPEN باقی می‌ماند:** Qualification criteria، mandatory documents، evidence validity/expiry، reviewer، approver، review cadence، qualification result vocabulary/state machine، contract prerequisite، activation authority/workflow/scope/effective date، Provider Type، Service mapping، geography eligibility، Capacity، Provider Selection، Referral response، Provider Data Access و Suspension/Termination.
- **ممنوع:** Technical یا Code نباید از وجود Evidence نتیجه Qualified/Approved/Active بسازد.
- **منبع:** BC-008 + DC-007 + BX-007 + D-0037 + D-0131؛ پذیرفته‌شده تحت D-0124.


## D-0133 — Sprint 006 فقط Provider Qualification Review Request Foundation است

- **تاریخ:** 2026-10-07
- **حوزه:** Delivery Governance / Provider Qualification Review
- **وضعیت:** Accepted
- **تصمیم:** Slice بعدی فقط امکان ثبت یک **Qualification Review Request** برای Provider Candidate موجود را فراهم می‌کند؛ ثبت Request به معنی Reviewed شدن، Qualification Decision، Approval، Activation یا Service Eligibility نیست.
- **قاعده:** `Review Request ≠ Review Decision ≠ Activation`.
- **محدوده مجاز:** ثبت immutable و provenance-preserving یک Review Request توصیفی برای Candidate موجود، Audit/Outbox/Idempotency، و read-only inspection.
- **Evidence boundary:** Evidenceهای ثبت‌شده تا زمان Request همچنان به‌صورت مستقل و append-only در Candidate قابل مشاهده‌اند؛ این Sprint هیچ Evidence Bundle policy، mandatory evidence rule یا qualification criteria اختراع نمی‌کند.
- **OPEN باقی می‌ماند:** reviewer identity/authority، approver authority، assignment، review SLA/cadence، qualification criteria، decision vocabulary/state machine، evidence sufficiency، evidence pinning policy، approval/activation authority، activation scope/effective date، Provider Type، Service mapping، geography eligibility، Capacity، Provider Selection، Referral response، Provider Data Access و Suspension/Termination.
- **ممنوع:** Technical یا Code نباید از وجود Review Request نتیجه Reviewed/Qualified/Approved/Active بسازد.
- **منبع:** BC-008 + DC-007 + BX-007 + D-0037 + D-0132؛ source-supported need for review with unresolved reviewer/approver details؛ پذیرفته‌شده تحت D-0124.


## D-0031 — منع تصمیم مستقل و الزام‌آور AI در امور حساس

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Internal AI / Decision Authority
- **وضعیت:** Accepted — bounded safety guardrail
- **تصمیم:** تا پذیرش تصمیم جداگانه و معتبر درباره هر Use Case، AI نسیم صرفاً دستیار است و حق ندارد به‌تنهایی تشخیص پزشکی رسمی ثبت کند، درمان تجویز کند، Eligibility یا Referral را نهایی کند، Provider را الزام‌آور انتخاب کند، هزینه/پرداخت را تصویب کند، پرونده رسمی یا Case/Need status را تغییر دهد، وضعیت Emergency/Incident را نهایی کند، یا Risk Acceptance/Scale Gate را تصویب کند.
- **مرز:** این منع، نه فهرست قطعی Use Caseهای عملیاتی است و نه اجازه ضمنی دسترسی به داده؛ هر تغییر نیازمند Decision صریح و گیت مستقل است.
- **منبع:** DC-006 Candidate D-0031 + BC-004 + BC-006 + D-0004/D-0014؛ انتخاب محافظه‌کارانه تحت D-0124.

## D-0032 — بازبینی انسانی برای خروجی اثرگذار AI

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI / Human Review
- **وضعیت:** Accepted — principle, not detailed authority matrix
- **تصمیم:** خروجی AI که قرار است بر Official Record، مسیر خدمت، Referral، Need/Outcome، Incident یا اقدام مالی اثر رسمی بگذارد، باید پیش از اثر رسمی از مسیر بازبینی انسانی با امکان Accept / Reject / Edit عبور کند؛ AI Output خودبه‌خود Official Record نیست.
- **مرز:** Reviewer مشخص، اختیار او، mapping مجوز، workflow دقیق، تریگرها و شواهد پذیرش برای هر Use Case همچنان OPEN است؛ هیچ Role Title یا ActorType اختیاری ایجاد نمی‌کند.
- **منبع:** DC-006 Candidate D-0032 + BC-006 + D-0004/D-0015؛ پذیرفته‌شده تحت D-0124.

## D-0033 — جداسازی موفقیت Training/Evaluation از ارتقای مدل

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI / Model Governance
- **وضعیت:** Accepted — governance boundary
- **تصمیم:** Training success و Evaluation pass اجازه جایگزینی نسخه فعال AI Production را ایجاد نمی‌کنند؛ Promotion نیازمند تصمیم مستقل، صریح، قابل حسابرسی و دارای اختیار انسانی است.
- **مرز:** شخص/مرجع دارای اختیار Promotion، Evaluation policy، thresholds، نسخه‌بندی اجرایی و Rollback workflow همچنان OPEN هستند؛ Dataset automation طبق D-0005 مستقل باقی می‌ماند.
- **منبع:** DC-006 Candidate D-0033 + D-0005؛ پذیرفته‌شده تحت D-0124.

## D-0034 — رفتار ایمن AI در نبود مدل/داده و امکان Rollback

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI / Availability & Fail-safe
- **وضعیت:** Accepted — principle only
- **تصمیم:** در نبود Model معتبر، خطای AI Runtime یا Context ناکافی، AI نباید جواب ساختگی را به‌عنوان واقعیت یا Decision رسمی ارائه دهد؛ وضعیت نامعتبر/غیرقابل‌دسترسی باید آشکار باشد و فرایند انسانی، تا حد ممکن و بر پایه قرارداد مجاز خودش، مستقل از AI ادامه‌پذیر بماند. امکان Rollback نسخه مدل باید در طراحی آینده پیش‌بینی شود.
- **مرز:** متن پاسخ در خطا، incident owner، escalation، retry، fallback عملیاتی، مرجع/تریگر Rollback و SLO هنوز OPEN هستند؛ این تصمیم هیچ Provider/Clinical/Financial action را مجاز نمی‌کند.
- **منبع:** DC-006 Candidate D-0034 + D-0004/D-0005؛ پذیرفته‌شده تحت D-0124.

## D-0035 — منشأ و ردیابی خروجی‌های اثرگذار AI

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI / Provenance & Audit
- **وضعیت:** Accepted — traceability principle
- **تصمیم:** برای خروجی AI که به مسیر عملیاتی/بازبینی انسانی می‌رسد، هویت AI و نسخه Model، زمان تولید، نسخه Context/ورودی اثرگذار، تصمیم/تغییرات Reviewer انسانی (در صورت لزوم)، و action رسمی بعدی باید به‌صورت قابل انتساب و حسابرسی ردیابی شوند. AI نباید به‌عنوان Actor انسانی ثبت شود.
- **مرز:** ذخیره متن کامل، retention، data access، logging sanitization و Training Eligibility از این تصمیم استنتاج نمی‌شوند؛ باید مستقل تعیین شوند.
- **منبع:** DC-006 Candidate D-0035 + D-0015/D-0028؛ پذیرفته‌شده تحت D-0124.

## D-0135 — نخستین Use Case محدود AI برای سالمند و سالمندیار

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Minimal Scope
- **وضعیت:** Accepted — selection of a safe, bounded first use case only
- **تصمیم:** نخستین Use Case منتخب برای هر دو مخاطب D-0004، «**راهنمایی اطلاعاتی فقط بر اساس محتوای رسمیِ منتشرشده و مصوب نسیم**» است:
  - **سالمند:** توضیح ساده درباره خدمات و مراحل **واقعاً مصوب/منتشرشده** نسیم و چگونگی درخواست کمک انسانی.
  - **سالمندیار:** جست‌وجو/توضیح راهنماها و رویه‌های عملیاتی **واقعاً مصوب/منتشرشده و مجاز برای سالمندیار**.
- **Bounded scope:** read-only/informational؛ بدون دسترسی پیش‌فرض به پرونده شخصی، Case status، اطلاعات سلامت، Provider ranking/selection، Referral mutation، Clinical/Financial instruction یا تغییر Official Record؛ در نبود منبع معتبر یا مجوز دسترسی باید از جعل محتوا خودداری شود.
- **الزام مستقل:** این انتخاب کوچک، تعهد D-0005 برای **AI هر دو مخاطب و Dataset خودکارِ نسخه‌دار از داده مجاز** در روز اول را کاهش نمی‌دهد یا جایگزین نمی‌کند. AI conversation یا داده عملیاتی خودبه‌خود Training Eligible نیست.
- **OPEN و مانع گیت:** محتوای واقعاً مصوب، Content Owner/Publication Authority، نسخه منبع، Human Owner/Review، access/consent/legal basis، retention، پاسخ دقیق در نبود منبع، Data Classes مجاز AI Runtime و Training، Dataset Eligibility و Model/Training/Evaluation/Promotion governance. تا احراز این موارد هیچ AI Runtime/API یا Dataset Builder برای این Use Case مجاز نیست.
- **منبع:** DC-017 AI-U01 و DC-006 Candidate D-0029/D-0030 + BC-004/BC-006 + D-0004/D-0005/D-0021؛ انتخاب اولین Slice کم‌ریسک تحت D-0124. این تصمیم به معنای قبول همه Use Caseهای D-0029/D-0030 نیست.
