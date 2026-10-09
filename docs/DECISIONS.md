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


## D-0154 — مالک محصول استفاده از ۸۴ نمونه مصنوعی تألیفی نسیم را به‌عنوان ورودی اولیه مجاز دانست

- **تاریخ:** 2026-10-09
- **حوزه:** Business / Initial Synthetic AI Data / Purpose-limited Admission
- **وضعیت:** Accepted — **اجازه استفاده از منبع مصنوعی اولیه؛ نه تأیید خودکار کیفیت یا اجرای Training**
- **منبع تصمیم:** پاسخ صریح مالک محصول به سؤال Dataset اولیه: «داده‌هایی که خود تو به عنوان دیتا ست اولیه آماده کردی مجاز است و بعد از آن به مرور زمان داده‌هایی که در نسیم تایید می‌شوند».
- **دامنه دقیق:** مجموعه ۵۲ + ۳۲ نمونه مصنوعیِ تألیفی موجود در PR #10، همراه با ۸ منبع داستانی و دو اصلاحیه پیشنهادیِ جداگانه. صرفاً برای ثبت ورودی مصنوعیِ آغازین و آماده‌سازی مسیر Dataset/Training/Evaluation تحت گیت‌های مستقل. این اجازه مجوز داده واقعی سالمندان یا ادعای رسمی بودن محتوای ساختگی نیست.
- **عدم تعمیم:** هر نمونه هنوز `AUTHOR_DRAFT_UNREVIEWED` است و برچسب تاریخی `training_permission/evaluation_permission=NOT_AUTHORIZED` در نسخه اصلی به‌صورت مخفیانه تغییر نمی‌کند. اظهار جدید مالک محصول باید به‌صورت سند تصمیم جداگانه پیوند شود؛ پیش از مصرف برای Training/Evaluation، بررسی واقعی کیفیت ۸۴ رکورد، جداسازی Training/Evaluation، سلامت منبع/نسخه و قبول Dataset باید مستقل ثبت شود. هیچ AI-authored signoff جای Human Review را نمی‌گیرد.
- **Technical scope:** ساخت یک inventory قابل بازتولید از Git blobهای پین‌شده مجاز است؛ «Dataset APPROVED» یا Training Run خودکار تا تکمیل گیت‌ها مجاز شمرده نمی‌شود.

## D-0155 — پذیرش تدریجی فقط داده‌های واقعاً تأییدشده در نسیم برای Dataset آینده

- **تاریخ:** 2026-10-09
- **حوزه:** Business / Real Operational Learning
- **وضعیت:** Accepted principle — per-source/per-purpose authorization details OPEN
- **تصمیم:** پس از بسته مصنوعی اولیه، فقط داده‌هایی که در نسیم واقعاً بررسی و برای Purpose مشخص تأیید می‌شوند می‌توانند به تدریج Candidate ساخت Dataset شوند. صرف ثبت Operational، Approval پرونده یا رویداد Outbox به‌تنهایی مجوز Training/Evaluation نیست.
- **الزام باقیمانده:** مالک حقوقی و حاکمیتی، مبنای مجاز/رضایت برای Training مستقل از خدمات، Data Classes، exclusions، اثر Withdrawal، حریم خصوصی، کالیبراسیون کیفیت، تفکیک household/lineage و هدف Evaluation در BC-007/Issue #12 هنوز باید با شواهد واقعی بسته شوند. هیچ default eligible=true ساخته نشود. D-0005 درباره ساخت خودکار Dataset از داده **واقعاً eligible** همچنان الزام است.

## D-0156 — Keycloak اولویت Identity است، نه انتخاب یا استقرار مصوب

- **تاریخ:** 2026-10-09
- **حوزه:** Business / Authentication / Browser
- **وضعیت:** Preference accepted / technical provisioning OPEN
- **تصمیم:** سرویس هویت هنوز انتخاب نشده؛ `Keycloak` گزینه اولویت‌دار بررسی فنی و انتخاب آینده است. تا زمانی که انتخاب، محیط، OIDC issuer/client، policy نشست، role mapping و شواهد صحت استقرار مشخص نشده‌اند، browser session fail-closed باقی می‌ماند. هیچ login، token، secret یا production identity جعلی تولید نشود.

## D-0157 — مسئول تصمیم انسانی Provider و انتخاب مقصد ارجاع: مدیر عملیات نسیم

- **تاریخ:** 2026-10-09
- **حوزه:** Business / Provider Qualification, Activation & Human Referral Destination
- **وضعیت:** Accepted at organizational decision-owner level
- **تصمیم:** سمت سازمانی «مدیر عملیات نسیم» مرجع انسانی تصمیم نهایی تأیید صلاحیت Provider، فعال‌سازی عملیاتی Provider و انتخاب Provider مقصد ارجاع است؛ این پاسخ به پرسش صریح این سه حوزه داده شد.
- **محدودیت:** این سمت به معنی هویت شخص، احراز هویت، انتصاب رسمی، قابلیت فنی از پیش Provisionشده، معیار بررسی مدارک، نوع Provider، مجوز قرارداد، پوشش خدمت، ظرفیت، رضایت اشتراک اطلاعات، Service Completion Evidence، Reassessment Rule، یا اختیار پزشکی نیست. Ruleهای عملیاتی و تمایز Reviewer/Approver هنوز باید به‌طور مستقل تصویب شوند. هیچ Candidate صرفاً به‌علت وجود این نقش Active نمی‌شود؛ AI حق انتخاب نهایی ندارد.

## D-0158 — منشأ بسته محتوایی نسیم همان بسته تألیفی PR #10 است

- **تاریخ:** 2026-10-09
- **حوزه:** Business / Official Content Reference / AI Day-one
- **وضعیت:** Product-owner source identification accepted; publication evidence and independent per-record review OPEN
- **تصمیم:** مالک محصول مجموعه محتوای اولیه را «همونی هست که خودت تهیه کردی» معرفی کرد. مرجع فعلیِ نسخه‌دار GitHub، فایل‌های PR #10 در SHA `faf33342497ec23f7c0969930ce808787e476be6` است. گزارش قبلی مالک محصول مبنی بر تأیید/تحویل و انتشار توسط مدیر عملیات در D-0152/0153 (هنوز روی PR #10 unmerged) تکراراً سؤال نشود.
- **مرز:** داده‌های داستانی، اسناد Draft یا AI-generated به صرف گفته فوق سند رسمی خدمت واقعی نمی‌شوند. محل/نسخه واقعی نشر، مخاطب مجاز و ارزیابی ۸۴ نمونه توسط بازبین انسانی مستقل هنوز در Issues #11 و #13 نیازمند شواهد جداگانه‌اند. بازبینی مستقل از سوی مؤلفِ هوش مصنوعی ادعا نشود.

## D-0159 — مجوز مشروط مالک محصول برای ادغام PRهای آماده

- **تاریخ:** 2026-10-09
- **حوزه:** Delivery Governance / Integration
- **وضعیت:** Accepted conditional authorization, NOT automatic merge of every open PR
- **تصمیم:** مالک محصول به پیشنهاد «ادغام پس از تطبیق کامل تغییرات، بازبینی مستقل و CI سبز، به ترتیب وابستگی» پاسخ مثبت داد.
- **گیت لازم:** بازسازی تاریخچه و جلوگیری از double-apply برای PRهای واگرا، بازبینی مستقل واقعی در سطح لازم، CI سبز دقیق HEAD و ترتیب صحیح وابستگی. COMMENT مؤلف/عامل خودکار معادل independent human approval نیست. اگر گیتی کامل نیست، PR همان Draft/Open باقی بماند؛ نباید آن را به صرف این Yes ادغام یا Ready کرد. Stage/QA/Release/Production همچنان زیر D-0130 مستقل‌اند.
- **هماهنگی شاخه:** D-0134…D-0153 فعلاً در PR #10 unmerged هستند؛ هنگام ادغام باید تاریخچه canonical `docs/DECISIONS.md` با آن شاخه تطبیق شود و هیچ تصمیم پذیرفته‌شده‌ای overwrite نشود.


## D-0160 — بازبینی موردبه‌مورد هر ۸۴ نمونه اولیه به‌دست مدیر عملیات، طبق گزارش مالک محصول

- **تاریخ:** 2026-10-09
- **حوزه:** Business / Synthetic Initial AI Data / Human Quality Review
- **وضعیت:** **Product-owner attestation accepted — review completion REPORTED; item-level review evidence and results NOT YET RECONCILED**
- **تصمیم/اظهار:** در پاسخ به سؤال مشخص «آیا مدیر عملیات نسیم شخصاً بررسی تک‌تک ۸۴ نمونه اولیه را انجام داده است؟»، مالک محصول تصریح کرد: «خودش انجام داده». این یک اظهار جدید درباره *انجام* بازبینی انسانیِ مستقل از مؤلف AI است و نباید به وضعیت «بازبینی اصلاً انجام نشده» تقلیل داده شود.
- **حد اثبات:** این پاسخ به‌تنهایی فهرست ۸۴ نتیجه ACCEPT/REWRITE/REJECT، نسخه دقیق هر نمونه در زمان بررسی، نتیجه دو اصلاحیه پیشنهادی v0.3، زمان/مرجع ثبت بررسی یا مجوز حرفه‌ای موارد سلامت/ایمنی را ارائه نکرده است. هیچ رکورد مشخصی به‌صورت خودکار ACCEPT نمی‌شود؛ منبع نسخه‌دار PR #10/PR #34 و برچسب‌های تاریخی آن تغییر نمی‌کنند.
- **اقدام فنی مجاز:** ابزار offline فقط صحت پوشش و تطابق نسخه/شناسه شواهد انسانی را بررسی کند، بدون تولید امضای جعلی یا ادعای تأیید مستقل مبتنی بر AI و بدون ساخت Dataset/Training Run. Issue #13 برای **تطبیق شواهد بازبینی گزارش‌شده** باز بماند، نه برای درخواست مجددِ اصل بازبینی.

## D-0161 — مدیر عملیات نسیم مرجع سازمانیِ تأیید Training Eligibility است

- **تاریخ:** 2026-10-09
- **حوزه:** Business / AI Training Data Governance / Decision Rights
- **وضعیت:** **Accepted organizational authority; no blanket source approval**
- **تصمیم:** در پاسخ به پرسش «آیا اختیار تأیید استفاده از داده برای آموزش AI نیز با مدیر عملیات نسیم است، یا باید مرجع حاکمیتی جداگانه آن را تصویب کند؟» مالک محصول پاسخ مثبت «بله» داد. در چارچوب همان سؤال، «مدیر عملیات نسیم» مرجع سازمانی تصمیم **Training Eligibility** است.
- **حد اختیار:** احراز هویت فرد منصوب، مجوز قانونی/رضایت معتبر حسب نوع داده و Purpose، قواعد حذف/Withdrawal، Data Class، Curation، برچسب تأییدشده و جداسازی Training/Evaluation همچنان لازم است و صرف سمت سازمانی آنها را اثبات نمی‌کند. تأیید داده برای عملیات پرونده به‌تنهایی Training Eligibility نمی‌آورد. این تصمیم مجوز کلی برای داده واقعی سالمندان یا Training خودکار نیست.
- **مرز:** قواعد داده واقعی باید در BC-007 و Issue #12 با شواهد منبع و قانون مصوب شوند. AI یا System نمی‌تواند جای مدیر عملیات تأیید کند؛ Real Dataset Builder فقط منابع واقعاً مجاز را بگیرد. Promotion مدل همچنان Human-controlled است.
