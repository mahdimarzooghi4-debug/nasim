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



## D-0134 — تفکیک سه‌مرحله‌ای مسئولیت Qualification Provider

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Provider Qualification / Human Accountability
- **وضعیت:** Accepted — only the three-function human-responsibility boundary described here
- **تصمیم:** در مسیر آینده Qualification Provider سه کارکرد پاسخ‌گوی انسانی از هم جدا می‌شوند:
  1. **سالمندیار (معرفی‌کننده / ارزیاب میدانی):** معرفی Provider، ثبت شواهد و ارزیابی میدانی و پیشنهاد برای بررسی؛ حق اعلام نتیجه نهایی Qualification را صرفاً به دلیل سالمندیار بودن ندارد.
  2. **بازبین واجد صلاحیت تخصصی:** بررسی شواهد، مدارک و معیارهای مصوب در حوزه تخصص مربوط و ثبت نظر قابل حسابرسی؛ شایستگی و انتصاب واقعی بازبین باید جداگانه تعریف و احراز شود.
  3. **مسئول دارای اختیار مصوب شبکه Provider نسیم:** صاحب تصمیم نهایی Qualification در دامنه مجوز مصوب و بر اساس شواهد و بررسی تخصصی؛ این عنوان توصیف کارکرد آینده است، نه اعلام وجود سمت سازمانی یا اعطای Permission به فرد مشخص.
- **تفکیک:** پیشنهاددهنده / ارزیاب میدانی نباید همان تصمیم‌گیر نهایی پرونده‌ای باشد که پیشنهاد می‌کند. مسئولیت بررسی تخصصی و مسئولیت تصمیم نهایی مستقل و قابل انتساب‌اند. حدود دقیق تفکیک اشخاص، assignment، جانشینی، تعارض منافع و maker-checker/approval matrix فراتر از همین تفکیک حداقلی هنوز OPEN هستند.
- **مرز حقوقی/فنی:** این تصمیم هیچ ActorRoleAssignment، RolePermissionGrant، شایستگی تخصصی پیش‌فرض، reviewer identity، approver identity، فهرست مدرک، معیار اعتبار، threshold، State Machine، حق دسترسی به پرونده سالمند یا امکان اجرای Qualification Decision ایجاد نمی‌کند. `Role Title ≠ Permission` و `ActorType ≠ Authority`.
- **Activation:** نتیجه Qualification حتی در صورت تصمیم انسانی معتبر، به‌تنهایی Approval سازمانی یا Operational Activation یا Provider Selection / Service Eligibility نیست. Activation authority، prerequisites، scope، effective date، suspension/deactivation/revocation جداگانه OPEN باقی می‌مانند.
- **تاریخچه:** هر تصمیم بعدی باید قابل ردیابی و غیرقابل بازنویسی بی‌صدا باشد؛ قواعد دقیق Evidence Pinning و Lifecycle هنوز OPEN هستند.
- **گیت:** تنها تقسیم مسئولیت در Business پذیرفته شده است؛ QD-01 و جزئیات QD-02 و QD-03…QD-07 از `DC-016` بسته نشده‌اند. SG-007، Technical، Backlog، Sprint و Code هنوز مجاز نیستند. D-0130 برقرار است.
- **منبع پذیرش:** تأیید صریح مالک محصول در گفت‌وگو نسبت به ساختار پیشنهادی سالمندیار → بازبین صلاحیت تخصصی → مسئول مجاز شبکه.

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




## D-0136 — مسئول تأیید و انتشار محتوای رسمی نسیم برای دستیار AI

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Authoritative Content Governance
- **وضعیت:** Accepted — content approval and publication responsibility only
- **تصمیم:** **مدیر عملیات نسیم** مسئول تأیید و انتشار محتوای رسمی نسیم است که به‌عنوان منبع پاسخ‌گویی دستیار AI در نخستین Use Case اطلاعاتی D-0135 به کار می‌رود. محتوای خدمات و رویه‌های عملیاتیِ مورد استفاده دستیار باید پیش از استفاده به‌عنوان منبع رسمی، از این مسیر تأیید و منتشر شده باشد.
- **مرز:** این تصمیم به‌تنهایی وجود محتوای مصوب/منتشرشده، Service Catalog معتبر، مخزن محتوا، نسخه محتوا، متن واقعی دستورالعمل، مجوز دسترسی، یا اصالت/صلاحیت حرفه‌ای محتوای تخصصی را اثبات نمی‌کند. اعتبار قانونی، پزشکی یا تخصصی محتوا و اینکه کدام بازبینی تخصصی لازم است در صورت اقتضای نوع محتوا جداگانه باید احراز شود؛ عنوان مدیر عملیات جانشین صلاحیت تخصصی یا مرجع قانونی نیست.
- **مسئولیت در برابر اختیار اجرایی:** این تصمیم صاحب مسئولیت Business برای تأیید/انتشار را مشخص می‌کند؛ هویت فرد منصوب، نگاشت Actor/Role/Permission، اعطای دسترسی فنی، نماینده/جانشین و گردش‌کار انتشار و ابطال هنوز باید جداگانه تعیین شوند. هیچ مجوز جدیدی در Backend ایجاد نشده است.
- **تفکیک داده:** انتشار محتوای رسمی، مجوز استفاده از داده شخصی سالمند یا سالمندیار در AI Runtime یا Training، Consent/Legal Basis، Training Eligibility یا انتقال خودکار محتوا به Dataset نیست؛ AI فقط از منابعی که واقعاً منتشر و برای مخاطب مربوط مجازند می‌تواند استفاده کند.
- **OPEN باقی‌مانده:** محل و مرجع نگهداری محتوای معتبر، اسناد/نسخه‌های واقعی و وضعیت انتشار، کنترل تاریخ اعتبار/اصلاح/بازپس‌گیری، دسترسی سالمند در برابر سالمندیار، Human Owner برای تعاملات و Escalation، Runtime Data Classes، قواعد Legal/Consent، Training Eligibility، Model/Evaluation/Promotion و زیرساخت.
- **گیت:** D-0136 فقط بخشی از AI-D2 در DC-017 را می‌بندد؛ SG/Technical/Backlog/Sprint/Code و Stage مجاز نشده‌اند. D-0130 برقرار است.
- **منبع پذیرش:** پاسخ صریح مالک محصول: «مسئول تأیید و انتشار محتوای رسمی نسیم: مدیر عملیات نسیم».




## D-0137 — دو منبع محتوای رسمی قابل بررسی برای دستیار AI نسیم

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Official Content Source Classes
- **وضعیت:** Accepted — content source categories only
- **تصمیم:** منابع محتوایی نخستین دستیار اطلاعاتی نسیم (D-0135) می‌توانند از **دو دسته** باشند: (۱) **اسناد رسمی موجود** و (۲) **محتوای جدیدی که در نسیم تأیید و منتشر می‌شود**. هر دو دسته تنها وقتی می‌توانند مبنای پاسخ رسمی قرار بگیرند که منبع مشخص، معتبر، واقعاً مورد تأیید و انتشار، و برای مخاطب مربوط مجاز باشند. مسئول تأیید/انتشار محتوای رسمی مورد استفاده دستیار طبق D-0136 **مدیر عملیات نسیم** است؛ این مسئولیت جایگزین احراز اعتبار منبع تخصصی/حقوقی نمی‌شود.
- **مرز شواهد:** این تصمیم وجود یا هویت هیچ سند رسمی موجود، نسخه، URL، محل نگهداری، وضعیت اعتبار، شیوه ورود سند، تاریخ انتشار یا امکان دسترسی را اثبات نمی‌کند. اسناد پیشنویس یا فاقد تأیید معتبر نباید صرف نام «رسمی» بدون بررسی به منبع پاسخ رسمی تبدیل شوند.
- **مرز حقوق دسترسی:** محتوای ویژه سالمندیار خودبه‌خود برای سالمند قابل انتشار نیست؛ scope و Access هر Audience باید جداگانه تعیین شود. استفاده از محتوای مرجع برای پاسخ‌گویی، مجوز استفاده از داده‌های عملیاتی/شخصی در AI Runtime یا مجوز Dataset/Training ایجاد نمی‌کند.
- **OPEN باقی‌مانده:** فهرست و مکان واقعی اسناد، Source of Truth، احراز اعتبار/نسخه و وضعیت انتشار، دامنه دسترسی هر مخاطب، سازوکار اصلاح/ابطال/حذف، احراز هویت مدیر عملیات و Permissionهای انتشار، بررسی تخصصی یا حقوقی در صورت اقتضا، Human Review و Fail-safe، Consent/Legal Basis، Training Eligibility و تمام انتخاب‌های فنی AI.
- **گیت:** فقط دسته‌های منابع Business پذیرفته شده‌اند؛ بخش «منبع و شواهد واقعی» از AI-D2 در DC-017 همچنان OPEN است. این تصمیم SG، Technical، Backlog، Sprint، Code، Integration، Dataset Builder، Hosted Stage یا Production را مجاز نمی‌کند؛ D-0130 پابرجاست.
- **منبع پذیرش:** پاسخ صریح مالک محصول: «منبع محتوای رسمی نسیم برای دستیار AI: اسناد رسمی موجود و محتوای جدید تأیید و منتشرشده در نسیم».




## D-0138 — اسناد رسمی موجود فعلاً بیرون از نسیم نگهداری می‌شوند و بعداً وارد سامانه خواهند شد

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Official Content Onboarding
- **وضعیت:** Accepted — current location category and future import intention only
- **تصمیم:** اسناد رسمی موجود که طبق D-0137 یکی از دو دسته منبع محتواییِ پیشنهادی دستیار اطلاعاتی نسیم هستند، **در وضعیت فعلی خارج از سامانه نسیم نگهداری می‌شوند** و قرار است **در آینده به نسیم وارد شوند**. محتوای جدید نیز طبق D-0137 پس از تأیید و انتشار معتبر در نسیم می‌تواند منبع پاسخ‌گویی شود.
- **مرز وجود و اعتبار:** این تصمیم نام، تعداد، مالک حقوقی/سازمانی، مسیر واقعی فایل‌ها، کیفیت، تاریخ اعتبار، نسخه، دسته‌بندی دسترسی، شیوه واردسازی یا زمان ورود را اعلام یا تأیید نمی‌کند. محل بیرونی نگهداری به‌تنهایی سندی را به «محتوای معتبر و منتشرشده برای AI» تبدیل نمی‌کند.
- **قاعده محافظتی:** ورود آتی اسناد به سامانه به‌معنای پذیرش خودکار محتوا، انتشار برای همه مخاطبان، دسترسی AI، صحت تخصصی یا مجوز AI Training/Dataset نیست. استفاده رسمی در دستیار D-0135 نیازمند شواهد منشأ، اعتبار، بررسی/تأیید و انتشار تحت مسئولیت مدیر عملیات نسیم (D-0136) و دسترسی مجاز همان مخاطب است؛ بررسی تخصصی/حقوقی در صورت نیاز مستقل خواهد بود.
- **OPEN باقی‌مانده:** فهرست و محل دقیق اسناد بیرونی، منبع صادرکننده، اصالت و اعتبار فعلی، مالک/مجری فرآیند ورود، قواعد پذیرش/نسخه‌بندی/لغو انتشار، نوع و سطح دسترسی سالمند و سالمندیار، احراز اختیار واقعی ناشر و بازبین تخصصی، Consent/Legal Basis، Human Review/Escalation، Training Eligibility، Evaluation/Promotion و انتخاب فنی مخزن/انتقال.
- **گیت:** فقط محل فعلی در سطح Business و قصد ورود آینده ثبت می‌شود؛ هیچ Integration، Upload Pipeline، Content Repository، AI Runtime، Dataset Builder، SG، Technical، Backlog، Sprint، Code، Stage یا Production مجاز نشده است. D-0130 همچنان برقرار است.
- **منبع پذیرش:** پاسخ صریح مالک محصول: «محل فعلی اسناد رسمی مورد استفاده AI نسیم: خارج از نسیم؛ بعداً وارد سامانه می‌شوند».




## D-0139 — مدیر عملیات نسیم مسئول جمع‌آوری و ورود اسناد رسمی موجود است

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Official Content Collection & Import Accountability
- **وضعیت:** Accepted — Business responsibility assignment only
- **تصمیم:** مسئولیت کسب‌وکاری **جمع‌آوری و واردکردن اسناد رسمی موجود از خارج نسیم به سامانه نسیم** به **مدیر عملیات نسیم** سپرده می‌شود. این مسئولیت علاوه بر مسئولیت **تأیید و انتشار محتوای رسمی** طبق D-0136 است؛ جمع‌آوری/ورود و تأیید/انتشار همچنان دو اقدام مفهومی و قابل تفکیک‌اند، حتی وقتی Owner هر دو یک عنوان سازمانی باشد.
- **مرز عملیاتی:** تصمیم فعلی هیچ عملیات ورود سند، محل ذخیره، فهرست سند، زمان‌بندی، فناوری واردسازی، Data Model، API یا فرآیند فنی را اجرا یا تصویب نمی‌کند؛ تخصیص واقعی شخص/اکانت، اعطای Permission، تفویض اجرا، و قواعد بازبینی سند مستقل از این تصمیم هستند.
- **مرز اعتماد و انتشار:** ورود سند به نسیم به‌تنهایی آن را معتبر، به‌روز، رسمیِ منتشرشده یا مجاز برای پاسخ AI نمی‌کند. پیش از استفاده باید منشأ و اعتبار سند، انتشار با مسئولیت مدیر عملیات طبق D-0136، سطح دسترسی مخاطب و در موارد مقتضی بررسی تخصصی/حقوقی احراز شود. یکسان بودن مسئول ورود و انتشار، الزام به اعتبارسنجی مستقل موردنیاز برای اسناد تخصصی را حذف نمی‌کند.
- **مرز AI و Dataset:** این مسئولیت مجوز AI Runtime بر داده‌های شخصی، دسترسی عمومی سالمندان به رویه‌های داخلی سالمندیاران، یا Training Eligibility / Dataset نیست؛ این‌ها تصمیم‌های جدا هستند.
- **OPEN باقی‌مانده:** محل و اسامی واقعی اسناد بیرونی، مالک/مرجع صادرکننده، اصالت/نسخه/انقضا، قواعد intake/اعتبارسنجی/تأیید/اصلاح/ابطال، actor و مجوزهای واقعی، مخاطبان مجاز، Human Review و fail-safe، رضایت/مبنای قانونی داده، Training Eligibility، مدل/Training/Evaluation و زیرساخت.
- **گیت:** فقط مسئول Business روشن شده است. SG، Technical، Backlog، Sprint، Code، Stage، QA، Release و Production فعال نشده‌اند. D-0130 برقرار است.
- **منبع پذیرش:** پاسخ صریح مالک محصول: «مسئول جمع‌آوری و واردکردن اسناد رسمی موجود به نسیم: مدیر عملیات نسیم».




## D-0140 — تفکیک دو سطح مخاطب برای محتوای رسمی دستیار AI نسیم

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Official Content Audience Access
- **وضعیت:** Accepted — two-level content audience boundary only
- **تصمیم:** محتوای رسمیِ مورد استفاده دستیار اطلاعاتی نسیم (D-0135) بر اساس **مخاطب مجاز** به دو سطح Business تقسیم می‌شود:
  1. **عمومی (راهنمای قابل ارائه به سالمند و سالمندیار):** محتوای تأیید و منتشرشده‌ای که هر دو گروه مخاطب می‌توانند از آن برای دریافت راهنمایی اطلاعاتی استفاده کنند.
  2. **داخلی (رویه و دستورالعمل کارکنان):** محتوای تأیید و منتشرشده‌ای که فقط برای **سالمندیار یا سایر کارکنان دارای اختیار دسترسی مصوب** مجاز است؛ دستیار سالمند نباید به این محتوا دسترسی پیدا کند یا آن را در پاسخ افشا کند.
- **دقت معنایی:** واژه «عمومی» در این تصمیم به معنای **مجاز بودن نمایش به دو گروه سالمند و سالمندیار** است؛ به‌خودی‌خود به معنای Public Internet، دسترسی بی‌نیاز از احراز هویت، مجوز بازنشر بیرون از نسیم یا دسترسی هر شخص ثالث نیست.
- **مرز مجوز واقعی:** این تصمیم تنها سطح‌بندی Business محتوا را می‌پذیرد، نه فهرست اسناد طبقه‌بندی‌شده، Permission Registry، ActorRoleAssignment، RolePermissionGrant، User Access Matrix، انتشار واقعی یا راه‌حل فنی اعمال دسترسی. داخلی بودن به معنای دسترسی آزاد **همه** سالمندیاران یا کارکنان به **همه** رویه‌های داخلی نیست؛ دامنه دقیق مجاز باید تعیین شود.
- **مرز اعتبار محتوا:** پیش‌نیاز اعتبار منشأ، احراز صحت/نسخه، کنترل تخصصی یا حقوقی موردنیاز، تأیید و انتشار طبق D-0136، و جمع‌آوری/ورود طبق D-0139 مستقل از سطح مخاطب‌اند. واردکردن سند یا ثبت سطح مخاطب به‌تنهایی انتشار یا استفاده معتبر AI ایجاد نمی‌کند.
- **مرز داده/AI:** طبقه‌بندی محتوای راهنما هیچ حق دسترسی به اطلاعات شخصی سالمند/پرونده و هیچ مجوز Training Eligibility/Dataset/Retention برای محتوای رسمی یا AI Interaction ایجاد نمی‌کند.
- **OPEN باقی‌مانده:** مرجع مسئول طبقه‌بندی اولیه و تغییر سطح، قواعد رسیدگی به تعارض/بازطبقه‌بندی، اسناد و نسخه‌های واقعی، هویت/تأیید Actorهای کارکنان، گرانت‌های سطح دسترسی، الزامات احراز هویت، قواعد نمایش/withdrawal و fail-safe، Consent/Legal Basis و Training Eligibility.
- **گیت:** این پذیرش Business به‌تنهایی Technical Entry یا Code را مجاز نمی‌کند و D-0130 همچنان برقرار است.
- **منبع پذیرش:** تأیید صریح مالک محصول برای پیشنهاد تفکیک «عمومی: راهنمای مجاز برای سالمند و سالمندیار» و «داخلی: دستورالعمل صرفاً برای سالمندیار یا سایر کارکنان دارای مجوز».




## D-0141 — مسئول طبقه‌بندی و بازطبقه‌بندی محتوای رسمی دستیار AI

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Official Content Audience Classification
- **وضعیت:** Accepted — Business accountability for audience-level classification only
- **تصمیم:** **مدیر عملیات نسیم** مسئول **تعیین و تغییر سطح مخاطبِ عمومی/داخلی** برای اسناد و محتوای رسمی مورد استفاده دستیار اطلاعاتی نسیم است. دو سطح طبق D-0140 عبارت‌اند از «عمومی»، یعنی محتوای قابل ارائه به سالمند و سالمندیارِ مجاز در نسیم، و «داخلی»، یعنی فقط محتوای قابل ارائه به سالمندیار یا کارکنانی که اختیار دسترسی مصوب دارند.
- **مرز حقوقی/تخصصی:** اختیار تعیین برچسب توسط مدیر عملیات، حق لغو محرمانگی یا افشای اطلاعات پزشکی/شخصی/حقوقی دارای محدودیت قانونی یا تخصصی نیست. هر بازطبقه‌بندی به سطح گسترده‌تر باید همچنان با الزامات واقعی حقوقی، تخصصی، منشأ، اعتبار و مجوز انتشار و مخاطب سازگار باشد؛ فهرست قواعد و مراجع احراز این الزامات هنوز OPEN است.
- **تفکیک عملیات:** مسئولیت جمع‌آوری/ورود اسناد (D-0139)، بررسی اعتبار، تعیین/تغییر سطح مخاطب (این تصمیم)، تأیید و انتشار (D-0136) و مجوز دسترسی Runtime/Training اقدامات متفاوت هستند، حتی اگر مسئول برخی اقدامات یک عنوان سازمانی باشد. تغییر سطح، به‌خودی‌خود محتوای جدید را منتشر یا برای AI فعال نمی‌کند.
- **مرز فنی:** این تصمیم وجود شخص منصوب و authenticated، Role، Permission، Access Matrix، versioned classification record یا پیاده‌سازی UI/API را اثبات نمی‌کند؛ هیچ دسترسی فنی یا blanket staff access ایجاد نمی‌کند. عمومی بودن به معنای انتشار آزاد در اینترنت نیست و داخلی بودن به معنای دسترسی همه کارکنان نیست.
- **OPEN باقی‌مانده:** فهرست واقعی اسناد و سطح هر کدام، مدارک اعتبار/منشأ، کنترل‌های قانونی و تخصصی هنگام کاهش محرمانگی، احراز هویت مدیر عملیات/اختیارات اعطاشده، قواعد تغییر و Audit/اعتراض، نگهداری نسخه‌های قبلی، توقف دسترسی به محتوای باطل/منقضی، رفتار AI در نبود/تعارض منابع، Human Owner و Escalation، Consent/Legal Basis، Training Eligibility و تصمیم‌های فنی AI.
- **گیت:** این پذیرش صرفاً مسئولیت Business طبقه‌بندی را روشن می‌کند. SG/Technical/Backlog/Sprint/Code یا Stage به‌خودی‌خود مجاز نمی‌شوند؛ D-0130 برقرار است.
- **منبع پذیرش:** پاسخ صریح مالک محصول «ببله» به سؤال اینکه مدیر عملیات نسیم مسئول تعیین و تغییر سطح عمومی/داخلی اسناد باشد، با حفظ محدودیت‌های قانونی و تخصصی.




## D-0142 — سیاست رفتار ایمن دستیار AI هنگام نبود یا تعارض اطلاعات رسمی

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Official Information Fail-safe
- **وضعیت:** Accepted — bounded informational-response policy
- **تصمیم:** در نخستین Use Case راهنمای اطلاعاتی دستیار AI برای سالمند و سالمندیار (D-0135)، اگر برای پاسخ موضوع مورد درخواست **منبع رسمی معتبر، جاری، منتشرشده و مجاز برای مخاطب وجود نداشته باشد**، یا منابع مربوط **منقضی، نامعتبر یا متعارض باشند**، دستیار موظف است:
  1. **پاسخ قطعی یا حدسی ارائه نکند** و اطلاعات/قواعد یا منبع رسمی جعل نکند.
  2. **صریح و قابل فهم اعلام کند** که اطلاعات تأییدشده کافی نیست، اعتبار لازم را ندارد یا منابع با یکدیگر تعارض دارند، متناسب با وضعیت واقعی احرازشده.
  3. **کاربر را برای پیگیری به مسئول انسانی مرتبط راهنمایی کند**؛ هویت، کانال، مالک پیگیری و زمان‌بندی Escalation باید در قرارداد Business جداگانه پذیرفته شوند و فعلاً از عنوان «مسئول انسانی مرتبط» اختیار یا مقصد عملیاتی مشخصی استنتاج نمی‌شود.
  4. **تا رفع اشکال، اطلاعات نامعتبر/منقضی/متعارض را به‌عنوان پاسخ رسمی منتشر نکند**؛ صرف وجود سند واردشده یا برچسب «عمومی»/«داخلی» معیار صحت/تازگی نیست.
- **دامنه:** این تصمیم بر پاسخ‌گویی اطلاعاتیِ D-0135 و منابع رسمی تحت D-0136…D-0141 اعمال می‌شود و اصل محافظتی D-0034 را در همین دامنه مشخص‌تر می‌کند.
- **مرز:** اگر تنها منبعِ موجود خارج از دامنه مجوز کاربر است، دستیار حق افشای محتوای آن یا حتی تأیید وجود/جزئیات محرمانه آن را ندارد؛ باید پاسخ امن متناسب با مجوز بدهد. این تصمیم هیچ قواعد جدید پزشکی، تشخیص/اقدام اورژانسی، انتخاب Provider، تغییر پرونده یا حق دسترسی ایجاد نمی‌کند.
- **OPEN باقی‌مانده:** سازوکار احراز اعتبار/تازگی و حل تعارض منابع، نسخه و انتشار معتبر هر سند، تعریف و کانال «مسئول انسانی مرتبط» برای هر مخاطب/موضوع، ثبت Incident/Escalation و SLA، متن دقیق پیام‌ها، نحوه رسیدگی به درخواست‌های حساس و فوریت، Runtime Data Access/Consent و Training Eligibility؛ هیچ state machine، threshold، الگوریتم یا مسیر فنی از این سیاست قابل استنتاج نیست.
- **گیت:** ثبت این سیاست به‌تنهایی SG/Technical/Backlog/Sprint/Code را مجاز نمی‌کند؛ Stage همچنان طبق D-0130 UNAVAILABLE است.
- **منبع پذیرش:** موافقت صریح مالک محصول با **کل سیاست چهارمرحله‌ای** پیشنهادی درباره ندادن پاسخ حدسی، اعلام کمبود/تعارض اطلاعات، راهنمایی برای پیگیری انسانی و عدم ارائه اطلاعات نامعتبر به‌عنوان پاسخ رسمی.




## D-0143 — سالمندیار مسئول، نخستین مرجع پیگیری انسانی سالمند در پاسخ نامطمئن دستیار AI

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Elder Human Follow-up
- **وضعیت:** Accepted — first human follow-up function for elder only
- **تصمیم:** در نخستین Use Case اطلاعاتی سالمند (D-0135)، هرگاه پاسخ معتبر طبق سیاست D-0142 ممکن نباشد و نیاز به پیگیری انسانی وجود داشته باشد، **نخستین مرجع پیگیری انسانی برای سالمند، سالمندیار مسئول همان سالمند** است. راهنمایی سالمند به پیگیری انسانی در این محدوده با ساختار مالک/مخاطب اصلی Case در D-0121 سازگار است.
- **دامنه محدود:** انتخاب سالمندیار مسئول به‌عنوان *مقصد اولیه Business*، خودش اثبات نمی‌کند سالمندیار مشخصی در سیستم واقعاً منصوب/فعال است یا کاربر به پرونده و مسیر تماس او دسترسی دارد. AI نباید مالک Case را حدس بزند یا بدون قرارداد مستقل به Case/Assignment/PII دسترسی بگیرد. اگر سالمندیار مسئول موجود یا قابل دسترس نباشد، مسیر جایگزین همچنان **OPEN** است و نباید به‌صورت ساختگی تعیین شود.
- **حد اختیار:** سالمندیار فقط در دامنه اختیارات انسانی مصوبش پیگیری می‌کند. هیچ اختیار جدید تشخیص/درمان، رسیدگی اضطراری، تصمیم Provider/Referral، تغییر پرونده، انتشار محتوای رسمی یا تأیید پاسخ AI با این تصمیم ایجاد نمی‌شود؛ موارد خارج از اختیار سالمندیار باید طبق مسیر ارجاع بالادستیِ هنوز OPEN رسیدگی شوند.
- **مرزهای اجرایی OPEN:** کانال تماس/ارجاع و نحوه احراز مخاطب، ایجاد Human Work Item یا Ticket، مالکیت و SLA پیگیری، اعلان‌ها، privacy-safe disclosure، نبود/تعویض/عدم دسترس‌پذیری سالمندیار، مسیر ارجاع مجدد/ارجاع به مقام بالاتر، پاسخ به پرسش‌های **سالمندیار** درباره AI، incident/emergency escalation و دسترسی‌های واقعی Runtime همگی نیازمند تصمیم‌های مستقل هستند.
- **مرز حفاظت از داده:** Business destination نه Role/Permission assignment است، نه consent/legal basis برای داده‌های شخصی، نه صلاحیت AI برای مشاهده Case و نه training eligibility.
- **گیت:** این پذیرش فقط بخشی از AI-D3/AI-D5 در DC-017 را می‌بندد؛ Technical/Backlog/Sprint/Code، Hosted Stage یا Production را مجاز نمی‌کند. D-0130 برقرار است.
- **منبع پذیرش:** پاسخ صریح مالک محصول «بله» به پیشنهاد «سالمندیار مسئول همان سالمند نخستین مرجع پیگیری انسانی باشد؛ موارد خارج از اختیار سالمندیار با تصمیم جداگانه تعیین شوند».




## D-0144 — نقش آتی پشتیبانی نسیم به‌عنوان مرجع جایگزین پیگیری سالمند

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Elder Human Follow-up Fallback
- **وضعیت:** Accepted — conditional future Business destination only, pending formal role definition
- **تصمیم:** در مسیر پیگیری انسانی سالمند تحت D-0142 و D-0143، اگر سالمندیار مسئول همان سالمند **تعیین نشده یا در دسترس نباشد**، مرجع جایگزینِ موردنظر مالک محصول **«مسئول پاسخ‌گویی یا پشتیبانی نسیم» است، اما فقط پس از تعریف رسمی این نقش و تعیین اختیار معتبر آن**. تا زمانی که نقش و صاحب اختیار آن به‌صورت مصوب تعریف و از نظر اجرایی قابل دسترس نشده‌اند، این تصمیم به معنای وجود مرجع پشتیبانی فعال یا امکان ارجاع واقعی نیست.
- **مرز نقش و اختیار:** عنوان «مسئول پاسخ‌گویی یا پشتیبانی نسیم» فعلاً یک **کارکرد سازمانی آینده** است؛ تعریف وظایف، مرجع انتصاب/اعطای اختیار، صلاحیت، قلمرو پاسخ‌گویی، فرد/واحد منصوب، جانشین، وضعیت دسترسی و مجوزهای واقعی همه **OPEN** هستند. صرف ActorType یا Role Title به شخصی اختیار رسیدگی، مشاهده پرونده یا دسترسی به داده‌ها نمی‌دهد.
- **مرز اجرای ارجاع:** ارتباط با مسئول پشتیبانی فقط پس از وجود مرجع واقعی، احراز اختیار و راه ارتباطی معتبر طبق قرارداد جداگانه امکان‌پذیر است؛ AI نباید فرد، شماره تماس، کانال، سامانه Ticket، SLA یا موفقیت ارجاع را جعل کند. اگر این نقش هنوز تعریف/فعال نشده یا قابل دسترس نیست، رفتار جایگزین بعدی و فرآیند انسانی موقت همچنان **OPEN** می‌مانند؛ پاسخ نامعتبر نباید جایگزین شود.
- **مرز تصمیم تخصصی:** این fallback اختیارات تشخیص/درمان، تصمیم Provider/Referral، امور مالی، اقدامات اضطراری، تغییر پرونده یا تأیید مستقل محتوای رسمی را به نقش پشتیبانی نمی‌دهد. مسیر ارجاع موضوعات خارج از اختیار، حساس یا فوریتی جداگانه باید مشخص شود.
- **مرز AI و داده:** نقش مقصد، دسترسی AI به Case/Assignment/PII، مجوز انتقال اطلاعات خصوصی به پشتیبانی، AI Training Eligibility، Dataset/Retention یا مجوز فنی ایجاد نمی‌کند. قواعد احراز هویت، حداقل‌سازی داده و مبنای قانونی/Consent همچنان OPEN است.
- **گیت:** فقط مقصد جایگزینِ **مشروط به تعریف نقش** در Business پذیرفته شده؛ هیچ SG/Technical/Backlog/Sprint/Code، Integration، Stage/QA/Release/Production مجاز نشده است؛ D-0130 برقرار است.
- **منبع پذیرش:** پاسخ صریح مالک محصول: «مرجع جایگزین پیگیری سالمند در نبود یا عدم دسترسی به سالمندیار مسئول: مسئول پاسخ‌گویی یا پشتیبانی نسیم پس از تعریف این نقش».




## D-0145 — مدیر عملیات، مرجع پیشنهادی تعریف و تصویب نقش پشتیبانی با شرط احراز اختیار سازمانی

- **تاریخ:** 2026-10-08
- **حوزه:** Business / AI Day-one / Support Function Establishment Authority
- **وضعیت:** Accepted — conditional Business designation only; proof of formal organizational authority OPEN
- **تصمیم:** مالک محصول موافقت کرد که **مدیر عملیات نسیم** مرجع تعریف و تصویب نقش آتی «مسئول پاسخ‌گویی یا پشتیبانی نسیم» باشد، **مشروط به اینکه اختیار سازمانی معتبر برای تعریف و تصویب این نقش را داشته باشد**. این پذیرش، مرجع مسئولِ مدنظر برای پیشبرد تعریف نقش را در سطح Business مشخص می‌کند و به‌معنای اثبات اعطا یا وجود آن اختیار نیست.
- **تفکیک دقیق:** انتخاب مدیر عملیات به‌عنوان مسئول Business برای پیشنهاد/تعریف و تصویب مشروطِ نقش ≠ احراز اختیار قانونی/سازمانی وی ≠ تعریف‌شدن واقعی نقش ≠ انتصاب مسئول پشتیبانی ≠ فعال‌شدن مسیر جایگزین D-0144. پیش از هر اثر سازمانی یا فنی، مرجع واقعی اعطای اختیار و سند یا تصمیم معتبر آن، حدود اختیار و شیوه تعیین/انتصاب مسئول این نقش باید جداگانه پذیرفته و احراز شوند.
- **مرز وظایف:** این تصمیم شرح وظایف پشتیبانی، سطح ارجاع، امکان مشاهده پرونده، کانال پاسخ‌گویی، الزامات آموزش/صلاحیت، SLA، جانشینی، مسیر موقتِ نبود سالمندیار یا وظیفه حل مسأله تخصصی/درمانی را تصویب نمی‌کند.
- **مرز سیستم و AI:** صرف عنوان مدیر عملیات یا پشتیبانی Actor/Role/Permission نمی‌سازد؛ اعطای اختیار فنی، دسترسی AI به Case یا داده شخصی، تبادل داده با واحد پشتیبانی، Training Eligibility و Dataset به مجوزهای جداگانه نیاز دارد. AI نباید وجود پشتیبانی فعال یا امکان ارجاع موفق را ادعا کند.
- **OPEN باقی‌مانده:** هویت مرجع اعطای اختیار به مدیر عملیات و مبنای معتبر آن، انتصاب و دامنه اختیار مدیر عملیات، قرارداد رسمی نقش پشتیبانی و مسئول واقعی آن، مسیر تماس/پیگیری و SLA، راه‌حل موقت تا ایجاد نقش، مرجع انسانی سالمندیار، مسیرهای فوریتی و استقلال تصمیم‌های Data/AI Governance.
- **گیت:** پذیرش مشروط D-0145 به‌تنهایی ایجاد نقش یا SG/Technical/Backlog/Sprint/Code/Stage/QA/Release/Production را مجاز نمی‌کند؛ D-0130 برقرار است.
- **منبع پذیرش:** پاسخ صریح مالک محصول «بله» به پیشنهاد «مدیر عملیات نسیم مرجع تعریف و تصویب نقش مسئول پاسخ‌گویی یا پشتیبانی باشد، مشروط به داشتن اختیار سازمانی لازم».




## D-0146 — مدیرعامل نسیم، مرجع مدنظر برای اعطای اختیار تعریف نقش پشتیبانی به مدیر عملیات

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Organizational Authority / Future Support Function
- **وضعیت:** Accepted — organizational design direction; actual legal/organizational proof and grant remain OPEN
- **تصمیم:** در ساختار سازمانی مدنظر نسیم، **مدیرعامل نسیم** مرجع اعطای اختیار به **مدیر عملیات نسیم** برای تعریف و تصویب نقش آتی «مسئول پاسخ‌گویی یا پشتیبانی نسیم» است؛ **مشروط به اینکه مدیرعامل واقعاً طبق ساختار و اسناد سازمانی معتبر، اختیار اعطای این حق را داشته باشد**. این تصمیم D-0145 را از جهت مرجع صادرکننده موردنظر تکمیل می‌کند.
- **مرز واقعیت نهادی:** این پاسخ نه اثبات وجود شخصیت حقوقی/سمت یا فرد منصوب مدیرعامل است، نه تأیید اساسنامه/مصوبه/صلاحیت وی، نه مستند تفویض صادرشده، نه واگذاری قطعی اختیار به مدیر عملیات. برای اثر واقعی باید مشروعیت اختیار مدیرعامل، تصمیم/تفویض معتبر، دامنه و محدودیت‌ها و مسئول منصوب به‌طور جداگانه احراز شوند.
- **مرز اجرا:** D-0146 نقش پشتیبانی D-0144 را ایجاد، منصوب، فعال یا پاسخ‌گو نمی‌کند و مسیر fallback را عملیاتی نمی‌سازد؛ Role/Permission، دسترسی به پرونده، کانال تماس، SLA، استفاده از داده در AI Runtime/Training و تصمیم‌های تخصصی/پزشکی/مالی همچنان تابع مجوز مستقل‌اند.
- **تفکیک با Provider:** اختیار مربوط به **تعریف نقش پشتیبانی** است؛ این تصمیم درباره مرجع اعطای اختیار **Qualification Provider** در DC-016/PR #9 یا Activation هیچ فرض یا پذیرشی ایجاد نمی‌کند.
- **تصمیم‌های باز:** مدارک و حدود اختیار واقعی مدیرعامل و تفویض به مدیر عملیات؛ قرارداد نقش پشتیبانی، انتصاب و دسترسی؛ مسیر موقت در نبود سالمندیار و پشتیبانی؛ مسیر پیگیری انسانی سالمندیار؛ Data Governance و Training Eligibility.
- **رویکرد پیشبرد:** سؤال‌های خردِ بدون اثر بر گیت از کاربر تکرار نشوند؛ تصمیم‌های قابل استنتاج از اسناد طبق D-0118/D-0124 در بسته‌های منطقی پیش بروند و فقط برای انتخاب‌های مادیِ غیرقابل استنتاج یا نیازمند اثبات حقوقی/نهادی واقعی، تأیید/شواهد مشخص خواسته شود. این بند تصمیم‌های OPEN را ACCEPTED یا DEFERRED نمی‌کند.
- **گیت:** هیچ Technical/Backlog/Sprint/Code یا Stage/QA/Release/Production با این تصمیم مجاز نمی‌شود؛ D-0130 پابرجاست.
- **منبع پذیرش:** موافقت صریح مالک محصول «بله» با پیشنهاد مدیرعامل نسیم به‌عنوان مرجع اعطای اختیار، همراه با بازخورد «به نظرم این سوالات ریز لازم نیست».




## D-0147 — تعویق انتخاب مدل نهایی هوش مصنوعی نسیم تا وجود شواهد ارزیابی

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Internal AI / Model-selection timing
- **وضعیت:** Deferred — **فقط انتخاب مدل نهایی/نسخه و پیکربندی مدل**؛ نه تعویق AI یا Dataset روز اول
- **تصمیم:** مالک محصول تأیید کرد که **اکنون برای انتخاب مدل مشخص هوش مصنوعی نسیم زود است**. هیچ خانواده، نام، نسخه، مدل منتخب، الگوریتم Training/Fine-tuning، معماری Runtime، Provider، سخت‌افزار یا Model Promotion از این گفتگو تصویب نمی‌شود. مدل‌های احتمالی فقط می‌توانند *گزینه تحقیقاتی* باشند.
- **دامنه تعویق و Owner:** انتخاب مدل/نسخه برای نخستین Use Case مصوب D-0135 تحت مسئولیت تصمیم‌گیری **مالک محصول** در گیت آینده **Model Benchmark / Technical Selection**، بر مبنای شواهد ارزیابی واقعی و مجوزهای مربوط. طراحی معیارهای ارزیابی و آماده‌سازی منابع مجاز در Business می‌تواند اکنون ادامه یابد.
- **شرط بازگشایی:** نخست محتوای رسمی معتبر، نسخه‌دار و مجاز برای مخاطب (D-0136…D-0142)، سناریوهای مقایسه‌ای قابل تکرار و قواعد دسترسی/ارزیابی مربوط روشن شوند. مدل‌ها سپس بر اساس کیفیت فارسی، پاسخ ایمن برای سالمند، وفاداری به منبع، عدم افشای محتوای داخلی، رفتار در کمبود/تعارض اطلاعات و عملکرد روی زیرساخت واقعی نسیم مقایسه شوند. نه Threshold و نه برنده‌ای از پیش تعیین نشده است.
- **الزام مستقل محفوظ:** D-0004/D-0005 **همچنان الزام‌آورند**: دستیار AI واقعی برای سالمند و سالمندیار و چرخه مستمر خودکار Dataset نسخه‌دار فقط از داده واقعاً Training-eligible، از **روز اول بهره‌برداری عملیاتی** لازم‌اند. تعویق انتخاب مدل مجوز عرضه محصول بدون AI واقعی یا جایگزینی آن با Demo/Placeholder نیست.
- **مرزهای حاکمیت:** Runtime Data Access با Training Eligibility یکی نیست؛ استفاده از اسناد رسمی برای پاسخ مجوز Training نیست. Training/Evaluation Success به‌تنهایی Production Promotion ایجاد نمی‌کند؛ انتخاب نهایی نیازمند تصمیم معتبر انسانی و گیت مستقل است. داده‌ها، نام مدل‌های نامزد، منابع خارجی و محدودیت‌های قانونی نباید فرضی ثبت شوند.
- **گیت:** این Deferred فقط انتخاب مدل نهایی را برای موعد مشخص‌شده کنار می‌گذارد؛ **AI Technical Entry، Backlog، Sprint، Code، Stage، QA، Release و Production را مجاز نمی‌کند**؛ D-0130 پابرجاست.
- **منبع پذیرش:** پاسخ صریح مالک محصول: «موافقم پس فعلا زود است»، درباره زمان انتخاب مدل هوش مصنوعی نسیم.




## D-0148 — انتصاب و اختیار رسمی مدیر عملیات برای تأیید و انتشار محتوای آموزشی نسیم و محتوای AI

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Organizational Authority / Caregiver Training Content / AI Official Content
- **وضعیت:** **Accepted — تصریح مالک محصول درباره انتصاب واقعی و اختیار رسمی مدیر عملیات، محدود به محتوای مورد سؤال**
- **تصمیم:** مالک محصول در پاسخ به دو سؤال مشخص اعلام کرد که **مدیر عملیات نسیم رسماً منصوب شده است** («منصوب شده») و **هم‌اکنون اختیار رسمی تأیید و انتشار محتوای آموزش سالمندیار و محتوای آموزشی/رسمی مربوط به هوش مصنوعی نسیم را دارد** («دارد»). بنابراین، مرجع سازمانی نهاییِ تأیید/انتشار نسخه رسمی این دسته از محتوا **مدیر عملیات نسیم** است؛ برای اعطای همین اختیار محتوایی، تفویض جدیدی در آینده پیش‌فرض یا الزامی تلقی نمی‌شود. این پذیرش حدود مسئولیت D-0136، D-0139 و D-0141 را برای محتوای مرتبط روشن‌تر می‌کند.
- **نوع شاهد:** **اظهار و تأیید صریح مالک محصول** درباره واقعیت انتصاب و وجود اختیار است. نام شخص منصوب، حکم انتصاب یا سند حقوقی/اداری اختیار در این گفتگو ارائه یا در مخزن ضمیمه نشده‌اند؛ این فقدان پیوست **به معنی انکار تأیید مالک محصول نیست**، اما نباید از آن یک فایل امضا‌شده یا Role/Permission فنیِ از پیش برقرار نتیجه گرفت. هر جا بررسی مدارک سازمانی/حقوقی برای انتشار رسمی لازم باشد، اصالت و حدود آن باید از مسیر واقعی احراز شود، نه با ساخت مدرک.
- **گستره تأیید:** مسئولیت مدیر عملیات برای بازبینی محتوایی در محدوده اختیار خود، تصمیم نسخه‌به‌نسخه درباره **تأیید/عدم تأیید و انتشار رسمی** راهنماهای آموزش سالمندیار و محتوای اطلاعاتی AI نسیم. طبقه‌بندی مخاطب `عمومی` / `داخلی` طبق D-0140/D-0141 همچنان **برای هر سند/نسخه** باید واقعی و مستند انجام شود؛ این تصمیم سطح دسترسی هیچ فایلی را خودکار تعیین نمی‌کند.
- **حدود تخصصی و حقوقی:** اختیار نشر **جایگزین صلاحیت پزشک، متخصص مراقبت، بازبین حرفه‌ای آموزش، بررسی حقوق سالمند، حریم خصوصی یا اصالت منابع خارجی نیست**. مطالب تخصصی/فوریتی/حقوقی پیش از انتشارِ مرتبط باید به میزان لازم توسط مرجع واقعاً دارای صلاحیت مرور شوند. TR-001، TR-002، متن دانش پایه AI-BOOT و ۸۴ نمونه مصنوعی هنوز صرفاً **Draft و منتشرنشده** هستند؛ خود این تصمیم هیچ‌کدام را تأیید، طبقه‌بندی یا منتشر نمی‌کند.
- **مرز با Training مدل:** **موافقت با نشر محتوای آموزشی انسان یا منبع اطلاعاتی AI ≠ Training Eligibility ≠ حقوق استفاده از متن برای Model Training/Evaluation ≠ Dataset Approval**. مسئله حقوقی/کیفی داده‌های مورد استفاده برای آموزش مدل، بازبینی مستقل ۸۴ نمونه (Issue #13)، مجوز منابع عملیاتی (Issue #12) و خودکارسازی Dataset نسخه‌دار D-0005 مستقل باقی می‌مانند. مدیر عملیات با این تصمیم «مرجع خودکار تأیید Dataset/Model» نمی‌شود.
- **مرز اختیارات دیگر:** D-0148 **به نقش آتی پشتیبانی** D-0144…D-0146، Provider Qualification/Activation در PR #9، دسترسی واقعی کارکنان/سالمندان به داده، AI Actor Access، اختیار پزشکی/پرداخت/ارجاع، نظام گواهی حرفه‌ای سالمندیار یا انتصاب مربی، هیچ حق جدیدی اعطا نمی‌کند. نباید از اختیاری که برای **نشر محتوا** تأیید شده، اختیار **تعریف/انتصاب نقش پشتیبانی** یا Provider استنتاج شود.
- **شاهد مورد نیاز برای اجرای نشر واقعی:** نسخه و شناسه واقعی محتوا، تأیید صلاحیت/اصالت و بازبینی تخصصی/حقوقیِ مرتبط در صورت لزوم، تصمیم واقعی مدیر عملیات درباره همان نسخه، طبقه‌بندی مخاطب، تاریخ/دامنه اعتبار، مکان نشر و امکان اصلاح/withdrawal. وجود سمت و اختیار مسئول **به معنای انجام واقعی هیچ‌یک از این اقدامات نیست**.
- **گیت:** فقط **بلاکِ نامشخص‌بودن انتصاب و صاحب اختیار محتوایی در سطح Business با تأیید مالک محصول رفع شده است**؛ Issue #11 تا ارائه مدارک واقعی محتوا و انتشار باز است. D-0130 Hosted Stage UNAVAILABLE و گیت‌های Business → Technical → Backlog → Sprint → Code → Code Review → Stage → QA → Release → Production همچنان برقرارند؛ هیچ مجوز استقرار یا Merge داده نشده است.
- **منبع پذیرش:** پاسخ‌های صریح و متوالی مالک محصول به انتصاب مدیر عملیات («منصوب شده») و اختیار رسمی تأیید و انتشار محتوای آموزش سالمندیار/AI («دارد»).




## D-0149 — تأیید محتوایی نخستین سند آموزش سالمندیار TR-001، به‌صورت موردی

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Workforce Training / Content Approval
- **وضعیت:** **Accepted — تأیید محتوایی TR-001 به روایت صریح مالک محصول؛ نه انتشار یا تأیید تخصصی مستقل**
- **تصمیم:** مالک محصول پس از تأیید انتصاب و اختیار رسمی مدیر عملیات در D-0148، در پاسخ به پرسش درباره اینکه آیا مدیر عملیات اسناد اولیه را بررسی و تأیید کرده، گفت **«تایید هست»** و سپس خواست تأییدها **یکی‌یکی** ثبت شوند. در این گام **صرفاً TR-001 — راهنمای اولیه آموزش سالمندیار نسیم** به‌عنوان سندی که تأیید محتوایی مدیر عملیات آن **توسط مالک محصول اعلام شده** ثبت می‌شود؛ هیچ تأیید تازه‌ای درباره TR-002، AI-BOOT یا ۸۴ نمونه مستقل از این بند ثبت نمی‌شود.
- **نسخه هدف تأیید:** `docs/training/drafts/TR-001_CAREGIVER_FOUNDATION_ORIENTATION_FA.md`، محتوای Draft 0.1 موجود پیش از ثبت این تصمیم، **blob SHA = `ac8ac0b0c9b50019cb19138a48be70e1c00543f8`** در شاخه Draft PR #10. تغییرات بعدی محتوایی نیازمند بازبینی نسخه جدید هستند؛ تأیید این نسخه به فایل‌های دیگر سرایت نمی‌کند.
- **نوع شاهد و محدودیت:** شاهد در اختیار ما **تأیید شفاهی/گفت‌وگوییِ مالک محصول** درباره تأیید توسط مدیر عملیات است؛ نام فرد، امضای مدیر عملیات، صورت‌جلسه بازبینی و سند انتصاب در GitHub ارائه نشده‌اند. این بند ادعا نمی‌کند که خود دستیار بازبینی مستقلی انجام داده یا سند امضاشده دریافت کرده است.
- **گیت‌های مستقل همچنان باز:** تأیید محتوایی مدیر عملیات **به‌معنای انتشار رسمی، تعیین سطح مخاطب عمومی/داخلی، تأیید بالینی/حقوقی، تصویب دوره/مربی/آزمون یا گواهی صلاحیت سالمندیار نیست**. برای استفاده عملیاتی، مدارک تخصصی لازم، نسخه معتبر نهایی، تصمیم واقعی نشر، طبقه‌بندی مخاطب و مسیر اصلاح/withdrawal باید به‌صورت مستقل ثبت شوند.
- **مرز AI و داده:** این پذیرش TR-001 را به منبع رسمیِ پاسخ‌گویی AI، نمونه Training-eligible، Dataset نسخه‌دار، Human-reviewed Label یا مجوز Training/Evaluation مدل تبدیل نمی‌کند. Issue #11 برای نشر واقعی و Issue #12 برای Training Eligibility باز می‌مانند.
- **گیت تحویل:** فقط تصمیم محتوایی محدود به TR-001 ثبت شد؛ PR #10 همچنان Draft/Open است. هیچ Technical/Backlog/Sprint/Code، Stage، Release یا Production مجاز نشده است.
- **منبع:** تأیید مستقیم مالک محصول «تایید هست» و درخواست بعدی «یکی بگیر» برای پیشبرد موردبه‌مورد.




## D-0150 — تأیید محتوایی مستقل سند TR-002 راهنمای استفاده ایمن از AI نسیم

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Workforce AI Literacy / Content Approval
- **وضعیت:** **Accepted — تأیید محتوایی TR-002 بر مبنای اعلام مستقیم مالک محصول درباره مدیر عملیات؛ نه انتشار یا مجوز آموزش مدل**
- **تصمیم:** مالک محصول، در ادامه ثبت موردبه‌مورد تأییدها و در پاسخ به سؤال مشخص «آیا مدیر عملیات، محتوای TR-002 — آموزش استفاده ایمن از هوش مصنوعی نسیم را هم تأیید کرده است؟»، پاسخ صریح **«بله»** داد. بنابراین تأیید محتوایی **صرفاً TR-002** توسط مدیر عملیات منصوب و صاحب اختیار موضوع D-0148، بر پایه اعلام مالک محصول، به‌صورت مستقل پذیرفته و ثبت می‌شود.
- **نسخه محتوایی مورد تأیید:** `docs/training/drafts/TR-002_NASIM_AI_SAFE_USE_GUIDE_FA.md` در شاخه Draft PR #10، نسخه تألیفی 0.1 با **Git blob SHA `91d560c8973bbf1efe4e952885c58918d1541ddf`** پیش از افزودن نشان وضعیت. این ثبت به متن همان نسخه محدود است؛ هر اصلاح اساسی بعدی نیاز به بررسی نسخه تازه دارد.
- **جایگاه شاهد:** تأیید در این مکالمه از طرف **مالک محصول** نقل شده است؛ امضای مستقیم مدیر عملیات، صورت‌جلسه یا مدرک بازبینی تخصصی جداگانه دریافت نشده و نباید جعل یا ادعای وجود آن شود.
- **حدود تأیید:** این پذیرش مربوط به **کیفیت/محتوای آموزشی TR-002** است؛ نه تصمیم انتشار رسمی، تعیین گروه مجاز برای استفاده از هر بخش، صدور مجوز اجرای دوره، تعهد به وجود AI عملیاتی، تأیید صحت پزشکی/حقوقی مستقل، تأیید شماره تماس یا ایجاد مسیر ارجاع انسانی. کارت ساده ویژه سالمند که در TR-002 آمده، فقط بخشی از نسخه مورد بررسی است و بدون طبقه‌بندی مخاطب، مجوز و ثبت انتشار مستقل قابل نمایش رسمی نیست.
- **استقلال سایر محتوا و AI:** D-0149 درباره TR-001 جداگانه باقی می‌ماند. **AI-BOOT-001/002/003، ۸۴ نمونه مصنوعی و دو اصلاحیه v0.3 با این پاسخ تأیید نشده‌اند.** هیچ نسخه‌ای از AI-BOOT یا داده‌های مصنوعی از این تصمیم مجوز Model Training، Evaluation، Dataset Inclusion یا انتشار به‌عنوان منبع رسمی پاسخ AI نمی‌گیرد.
- **اقدامات باز:** واقعی‌کردن تصمیم **انتشار هر نسخه** با هویت/نسخه/طبقه‌بندی `عمومی/داخلی`، مدارک اعتبار محتوایی یا بازبینی تخصصی/حقوقی مرتبط و ثبت کانال انتشار و اصلاح/withdrawal؛ این موارد در Issue #11 باقی می‌مانند. Training Eligibility عملیاتی Issue #12 و بازبینی مستقل ۸۴ نمونه Issue #13 همچنان OPEN هستند.
- **گیت:** این تصمیم فقط Business Content Approval همین سند را ثبت می‌کند؛ PR #10 Draft/Open است و Technical/Backlog/Sprint/Code، Hosted Stage، QA، Release یا Production را مجاز نمی‌کند.
- **منبع پذیرش:** پاسخ صریح مالک محصول «بله» به سؤال نام‌برده درباره تأیید TR-002 توسط مدیر عملیات.




## D-0151 — تأیید محتوایی مستقل AI-BOOT-001 دانش پایه هوش مصنوعی نسیم

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Internal AI / Foundational Knowledge / Content Approval
- **وضعیت:** **Accepted — تأیید محتوایی AI-BOOT-001 به اعلام مستقیم مالک محصول درباره مدیر عملیات؛ نه انتشار، تأیید تخصصی مستقل یا Training Permission**
- **تصمیم:** در ادامه ثبت موردبه‌مورد اسناد، مالک محصول در پاسخ به سؤال صریح «آیا مدیر عملیات، محتوای AI-BOOT-001 — دانش پایه هوش مصنوعی نسیم را نیز بررسی و تأیید کرده است؟» گفت **«بله»**. بر این اساس تأیید محتوایی مدیر عملیاتِ منصوب و دارای اختیار رسمی طبق D-0148 برای **فقط همین سند AI-BOOT-001** ثبت می‌شود.
- **نسخه محتوایی مورد تأیید:** `docs/ai/initial-content/AI-BOOT-001_NASIM_FOUNDATIONAL_KNOWLEDGE_DRAFT_FA.md`، Author Draft 0.1 روی شاخه Draft PR #10، با Git blob SHA **`0615dd67a7e81b89434ea42dd3064cfe5d986609`** پیش از درج وضعیت تأیید. اصلاح محتوایی بعدی نیازمند تعیین و بررسی نسخه جدید است.
- **ماهیت شاهد:** تأییدِ موردی بر پایه **اظهار مستقیم مالک محصول** درباره تأیید مدیر عملیات است؛ امضا/صورت‌جلسه مستقل مدیر عملیات، گزارش بازبینی تخصصی و تأیید مستند منبع رسمی در GitHub ارائه نشده و نباید اختراع شوند.
- **تفکیک محتوا از انتشار:** این تأیید **محتوای دانش پایه پیشنهادی** را پوشش می‌دهد، اما هیچ بند سند را خودکار به منبع معتبرِ **منتشرشده و مجاز برای پاسخ رسمی دستیار AI** تبدیل نمی‌کند. صحت و اصالت منابع واقعی، دسته‌بندی مخاطب `عمومی` / `داخلی`، نسخه نشر معتبر، بازبینی حقوقی/تخصصی لازم، محدوده دسترسی و امکان withdrawal مستقل باقی می‌مانند (Issue #11).
- **مرز یادگیری و مدل:** تأیید دانش پایه **مجوز Training/Evaluation، Dataset Inclusion یا برچسب انسانیِ موردپذیرش برای ۸۴ نمونه ساختگی نیست**. AI-BOOT-002 و AI-BOOT-003، فایل‌های JSONL و دو اصلاحیه 0.3 در این گام تأیید نشده‌اند. Issue #12 (Training Eligibility) و Issue #13 (بازبینی مستقل ۸۴ نمونه) همچنان بازند. D-0005 چرخه خودکار Dataset از داده واقعیِ واجد شرایط در روز اول را مستقل لازم می‌داند و D-0147 تنها انتخاب مدل نهایی را به تعویق انداخته است.
- **حدود اختیار:** این تأیید دانش پایه به معنای تأیید تعرفه، خدمت فعال، شماره تماس، پروتکل پزشکی، اختیار Provider/Referral یا دسترسی به پرونده شخصی نیست؛ هیچ‌کدام از موارد مجهول نباید ساخته شوند. D-0149 و D-0150 تأییدهای مستقل TR-001 و TR-002 هستند و تغییر نمی‌کنند.
- **گیت تحویل:** PR #10 همچنان Draft/Open است؛ این تصمیم نه Technical/Backlog/Sprint/Code را باز می‌کند، نه Hosted Stage/QA/Release/Production، نه مدل یا Runtime فعال ایجاد می‌کند.
- **منبع پذیرش:** پاسخ صریح مالک محصول **«بله»** به پرسش مشخص تأیید AI-BOOT-001 توسط مدیر عملیات.




## D-0152 — تأیید محتوایی مجموعه آثار آموزشی تهیه‌شده برای سالمندیار و AI نسیم

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Content Governance / AI Day-one / Workforce Training
- **وضعیت:** **Accepted — تأیید محتوایی کل بسته تألیفی، فقط به تأیید گفت‌وگویی مالک محصول درباره مدیر عملیات؛ نه تأیید همه Gateهای پروژه**
- **تصمیم:** مالک محصول پس از تأیید مستقل TR-001 (D-0149)، TR-002 (D-0150) و AI-BOOT-001 (D-0151)، در پاسخ به درخواست تأیید AI-BOOT-002 اعلام کرد **«همه کارها تایید کرده»**. این جمله در بستر پرسش‌های متوالی درباره **بازبینی و تأیید محتوای بسته آموزش و AI توسط مدیر عملیات** بیان شده است. بنابراین در سطح Business، تأیید محتوایی مدیر عملیات برای **باقی‌مانده همین مجموعه تألیفی موجود** نیز با اظهار مالک محصول پذیرفته می‌شود: AI-BOOT-002، AI-BOOT-003، دو فایل JSONL حاوی مجموعاً **۸۴ نامزد نمونه فارسی**، **۸ مرجع کاملاً داستانی** و دو اصلاحیه پیشنهادی v0.3. تأییدهای TR-001، TR-002 و AI-BOOT-001 همچنان تابع شناسه/نسخه ثبت‌شده در D-0149…D-0151 هستند.
- **نسخه‌ها و محدوده تأیید محتوا:** نسخه فایل‌های زیر قبل از افزودن این تصمیم و پیش از درج هر نشان وضعیت، با Git blobهای زیر ثبت شده است. این‌ها محتوای موجود روی شاخه Draft PR #10 هستند و هر تغییر مؤثر محتوایی نیازمند کنترل نسخه و تصمیم تازه است.

| سند/داده تألیفی | Git blob SHA | ماهیت |
|---|---|---|
| `docs/ai/initial-content/AI-BOOT-002_BEHAVIOR_SEED_REVIEW_GUIDE_FA.md` | `35c83b8a045703e86449b63429aa8ca4f727e5a5` | بسته تدوین و تحویل مرور |
| `docs/ai/initial-content/AI-BOOT-003_INDEPENDENT_REVIEW_HANDOFF_FA.md` | `ff9ecb53936f70e623ef51382dc85f26bdec55bc` | بسته تدوین و تحویل مرور |
| `docs/ai/initial-content/nasim_synthetic_behavior_candidates_v0_1.jsonl` | `9495f38c53eeb30db2b07824fdcb2b70a9e3ff52` | متن/نمونه/اصلاحیه تألیفی؛ بدون مجوز Training یا پذیرش مستقلِ نمونه‌به‌نمونه |
| `docs/ai/initial-content/nasim_synthetic_grounded_positive_candidates_v0_2.jsonl` | `3f8af141213ad111a646be3ff6a2c4fad277511c` | متن/نمونه/اصلاحیه تألیفی؛ بدون مجوز Training یا پذیرش مستقلِ نمونه‌به‌نمونه |
| `docs/ai/initial-content/nasim_fictional_grounding_fixtures_v0_2.jsonl` | `ed7797926c674687ead88fa4dcac6f20adb9bfc3` | متن/نمونه/اصلاحیه تألیفی؛ بدون مجوز Training یا پذیرش مستقلِ نمونه‌به‌نمونه |
| `docs/ai/initial-content/nasim_authorial_quality_corrections_v0_3.jsonl` | `753e6fb9ae603d84e5b97c6ff8201af079b4cb19` | متن/نمونه/اصلاحیه تألیفی؛ بدون مجوز Training یا پذیرش مستقلِ نمونه‌به‌نمونه |

- **تفسیر محدود جمله «همه کارها»:** در این گفت‌وگو **«همه» فقط به بسته محتواییِ مورد سؤال** مربوط است؛ نه به کل Product Backlog، Provider Qualification، انتصاب پشتیبانی، مصوبات تخصصی/حقوقی، استقرار، یا مجوزهای مستقل. **تأیید بسته در سطح Business** به‌تنهایی گواهی بررسی موردبه‌مورد و مستقل ۸۴ پاسخ توسط بازبین واجد صلاحیت نیست؛ AI-BOOT-003 صرفاً **برنامه تحویل بررسی مستقل** بوده و ثبت تأیید خود آن، چک‌لیست‌های داخلی‌اش را به «انجام شده» تبدیل نمی‌کند. دو اصلاحیه v0.3 نیز **پیشنهاد** می‌مانند و خودکار روی دو پاسخ اعمال نمی‌شوند.
- **نوع شاهد:** اظهار مستقیم مالک محصول از تأیید مدیر عملیات؛ هویت و امضای مستقیم آن مدیر، صورت‌جلسه، نتیجه جزئی بررسی تک‌تک نمونه‌ها یا تصمیم بازبین مستقل در اختیار نیست. **اظهار مالک محصول را می‌پذیریم ولی شواهدِ ارائه‌نشده را جعل نمی‌کنیم**. سند/مسئول تخصصی واقعاً واجد صلاحیت برای موضوعات سلامت/حقوق/ایمنی اگر لازم باشد جداگانه باید تأیید کند.
- **انتشار هنوز مجزا است:** هیچ سند با این تصمیم خودکار **منتشرشده، دارای نسخه رسمی، دارای طبقه‌بندی مخاطب `عمومی` / `داخلی` یا منبع رسمی AI D-0135** نمی‌شود. اصالت منابع بیرونی، بررسی تخصصی لازم، تصمیم نشر نسخه‌ای توسط مدیر عملیات، کنترل دسترسی و اصلاح/withdrawal باید واقعاً ثبت شوند (Issue #11).
- **Training Dataset و کیفیت مستقل هنوز مجزا هستند:** تمام نمونه‌ها و اصلاحیه‌های JSONL همچنان `training_permission=NOT_AUTHORIZED` و `evaluation_permission=NOT_AUTHORIZED` می‌مانند. **هیچ برچسب انسانی مستقلِ موردبه‌مورد، مجوز قانونی Data Training، Dataset Version، Model Training/Evaluation یا Production Model** از این تأیید ساخته نمی‌شود. Issue #12 (Eligibility داده) و Issue #13 (بازبینی مستقل شواهد ۸۴ نمونه و دو اصلاحیه) همچنان باز هستند؛ الزام Dataset خودکارِ eligible-only روز اول در D-0005 تغییر نمی‌کند.
- **گیت:** این تصمیم فقط بسته تألیفی Business را از نظر **اعلام تأیید محتوایی مدیر عملیات** پوشش می‌دهد. PR #10 همچنان Draft/Open است؛ هیچ Merge، Technical/Backlog/Sprint/Code/Stage/QA/Release/Production یا تغییر Runtime مجاز نشده است؛ D-0130 Hosted Stage UNAVAILABLE پابرجاست.
- **منبع پذیرش:** پاسخ مستقیم مالک محصول «همه کارها تایید کرده» در ادامه پرسش‌های تأیید محتوایی مدیر عملیات نسیم.




## D-0153 — اعلام مالک محصول مبنی بر تکمیل انتشار رسمی محتوا توسط مدیر عملیات

- **تاریخ:** 2026-10-08
- **حوزه:** Business / Official Content Publication / AI Day-one / Workforce Training
- **وضعیت:** **Accepted — اظهارنظر مالک محصول درباره انجام انتشار توسط مدیر عملیات؛ صحت و دامنه شواهد انتشار هنوز نیازمند تطبیق است**
- **اظهار صریح:** پس از ثبت تأیید محتوایی کل بسته در D-0152، از مالک محصول پرسیده شد که آیا مدیر عملیات **انتشار رسمی اسناد آموزشی نسیم را نیز انجام داده است یا فقط محتوا را تأیید کرده است**. مالک محصول پاسخ داد: **«همه کار کرده»**. بنابراین از این پس **نباید صرفاً به‌دلیل نبود اظهار نظر، ادعا کرد مدیر عملیات هنوز اقدام انتشار را انجام نداده** یا سؤالِ اصلِ انجام انتشار را دوباره مطرح کرد. این تصمیم **گزارش مالک محصول درباره انجام اقدام انتشار** است، نه جعل سند انتشار.
- **دامنه در بستر گفتگو:** اعلام به **مجموعه محتوای آموزشی و بسته AI تهیه‌شده در PR #10** مربوط است که تأیید محتوایی آن در D-0149…D-0152 ثبت شده است. اما اینکه **دقیقاً کدام سند/بخش با چه نسخه و برای کدام مخاطب در چه مقصدی منتشر شده** در پاسخ ارائه نشده است؛ تا دریافت شواهد، هیچ JSONL داستانی، نسخه Draft یا دستورالعملی را به‌صورت خودکار «منبع رسمی قابل پاسخ‌گویی به سالمند و سالمندیار» نمی‌شناسیم.
- **جداسازی حقیقت گزارش‌شده از شاهد قابل بررسی:** `PUBLICATION_REPORTED_BY_PRODUCT_OWNER = YES`؛ `VERIFIED_PUBLICATION_EVIDENCE = PENDING` برای هر نسخه. لینک/مسیر نشر رسمی، شناسه و نسخه مؤثر، تاریخ اعتبار، رکورد موافقت و طبقه‌بندی `عمومی` / `داخلی`، دامنه دسترسی کارکنان برای محتوای داخلی و مدارک تخصصی/حقوقی لازم در این گفتگو داده نشده‌اند و نباید ساخته شوند.
- **معنای `عمومی` در D-0140:** محتوای اجازه‌داده‌شده برای سالمند و سالمندیار **در نسیم**، نه انتشار بی‌قید در اینترنت. انتشار رسمی سند به‌خودی‌خود مجوز دسترسی AI، کارکنان فاقد مجوز یا شخص ثالث به اطلاعات `داخلی` نمی‌دهد؛ اصالت و اعتبار محتوای تخصصی باید مستقل بررسی شوند.
- **اثر بر وضعیت قبلی اسناد:** عبارت‌های «منتشرنشده» در یادداشت‌های پیش از D-0153 بیانگر نبود **شاهد انتشار در آن زمان** بودند. این تصمیم وضعیت را با **گزارش بعدی مالک محصول** به‌روز می‌کند؛ تا شواهد سندبه‌سند احراز نشود، وضعیت فنی/ممیزیِ قابل استناد برای راه‌اندازی AI همچنان `PUBLICATION_UNVERIFIED` می‌ماند و هیچ فایل Draft به‌صورت خودکار تبدیل به نسخه عملیاتی نمی‌شود.
- **مورد عملی بعدی در Issue #11:** به‌جای پرسیدن مجددِ «آیا منتشر شده»، فقط **محل/لینک واقعی انتشار یا شناسه رکوردهای رسمی** را دریافت کنیم و بعد نسخه‌ها، حدود مخاطب، اعتبار، کنترل دسترسی و وضعیت withdrawal را با مدارک واقعی تطبیق دهیم. **Issue #11 تا احراز شواهد واقعاً نسخه‌دار باز می‌ماند.**
- **مرزهای قطعی:** این اظهارنظر **بازبینی مستقلِ موردبه‌مورد ۸۴ نمونه (Issue #13)، حقوق Training/Evaluation یا Training Eligibility (Issue #12)، Dataset واقعی/نسخه‌دار D-0005، انتخاب مدل D-0147 یا مجوز Production** نیست. مواد داستانی نمی‌توانند شواهد خدمت واقعی نسیم شوند؛ دو اصلاحیه تألیفی v0.3 نیز صرفاً به‌دلیل این جمله خودکار پذیرفته یا اعمال نمی‌شوند.
- **گیت:** PR #10 همچنان Draft/Open است. این تصمیم نه Merge/Stage/Release/Production، نه Technical/Backlog/Sprint/Code و نه Role/Permission یا مصرف Runtime را مجاز می‌کند. D-0130 (نبود Hosted Stage) باقی است.
- **منبع پذیرش:** پاسخ مستقیم مالک محصول **«همه کار کرده»** به پرسش مشخص درباره انجام انتشار رسمی توسط مدیر عملیات.

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



## D-0162 — تأیید محتوایی تمام ۸۴ نمونه مصنوعی توسط مدیر عملیات نسیم، بنا بر اظهار مالک محصول

- **تاریخ ثبت:** 2026-10-09
- **حوزه:** Business / AI Initial Synthetic Corpus / Human Review Outcome
- **وضعیت:** **Accepted owner-reported decision — 84/84 CONTENT ACCEPTED as reported; individual external evidence and exact reviewed-version matching not yet reconciled**
- **اظهار صریح:** پس از پذیرش گزارش انجام بازبینی شخصی در D-0160، در پاسخ به سؤال «آیا مدیر عملیات هر ۸۴ نمونه را تأیید کرده، یا در بررسی او نمونه‌هایی هم نیازمند اصلاح یا رد بوده‌اند؟» مالک محصول اعلام کرد: «همه تایید کرده».
- **معنا:** بنا بر اظهار مستقیم مالک محصول، نتیجه بررسی محتوایی مدیر عملیات برای *هر ۸۴ نمونه اصلی* **قبول محتوایی** بوده است؛ هیچ‌کدام به‌عنوان مورد ردشده یا نیازمند اصلاح گزارش نشده‌اند. موضوع نتیجه کلی و انجام بررسی دیگر سؤال باز نیست؛ درخواست دوباره همان تأیید ممنوع است.
- **نسخه و منشأ:** مجموعه مرجع همان ۵۲ نمونه v0.1 و ۳۲ نمونه v0.2 در PR #10 SHA `faf33342497ec23f7c0969930ce808787e476be6`، با blobهای پین‌شده D-0154/SG-022 است. *از پاسخ کوتاه مالک محصول نمی‌توان اثبات کرد که نسخه دقیق زمان بررسی انسانی همین blobها بوده است*؛ بنابراین گزارش ۸۴ قبول به IDها پیوند داده می‌شود، اما گواهی امضا/ساعت/نسخه انسانی جعل نمی‌شود.
- **دو اصلاحیه:** `NSIM-EDIT-001` و `NSIM-EDIT-002` خارج از خود مجموعه ۸۴ رکورد، پیشنهادهای تألیفی جایگزین‌اند. «همه» در پاسخ به سؤال مشخص درباره ۸۴ نمونه، به‌تنهایی مجوز اعمال خودکار یا نتیجه بررسی مستقل این دو اصلاحیه نیست. اصل فایل‌ها و برچسب‌های تاریخی تغییر نمی‌کنند.
- **اثر محصول:** ۸۴/۸۴ از منظر *گزارش مالک محصول از تصمیم مدیر عملیات* پذیرفته‌اند؛ ولی Content Acceptance ≠ lawful Training/Evaluation Eligibility ≠ reviewed exact source-version proof ≠ Approved Dataset ≠ Model Production Promotion. برای ساخت Dataset باید شواهد واقعی/نسخه‌ای، هدف تفکیک Training/Evaluation و گیت‌های مربوط جداگانه برقرار باشند. هیچ داده واقعی سالمندان از این تصمیم مجاز نمی‌شود.
- **اجرای محدود کد:** افزودن نمای offline و فقط‌خواندنی `owner-reported-acceptance` با ۸۴ شناسه/هش، بدون درج review timestamp یا سند جعلی و بدون امکان مصرف در AdmissionVerifier/Training، مجاز است. CI، Code Review و Gateهای مستقل همچنان لازم‌اند.



## D-0163 — مالک محصول، نسخه دقیق ۵۲+۳۲ نمونه مصنوعی اولیه را تأیید کرد
- **تاریخ:** 2026-10-09
- **وضعیت:** Accepted product-owner attestation
- **تصمیم:** مالک محصول در پاسخ به سؤال درباره تأیید دقیق ۵۲ نمونه v0.1 و ۳۲ نمونه v0.2 موجود در PR #10 پاسخ «بله» داد. این اظهار، ابهام دامنه نسخه **برای تصمیم مالک محصول** را برطرف می‌کند. Git blobهای اولیه و SHA `faf33342497ec23f7c0969930ce808787e476be6` ثابت‌اند.
- **مرز شواهد:** اظهارات مالک محصول به‌عنوان سند تصمیم Business کافی شمرده می‌شود (D-0165)؛ جعل امضای شخص مدیر عملیات، timestamp بازبینی یا سند حقوقی ممنوع است. اصل داده تغییر نکند.


## D-0164 — هر دو اصلاحیه تألیفی v0.3 با حفظ نسخه‌های قبل پذیرفته شدند
- **تاریخ:** 2026-10-09
- **وضعیت:** Accepted editorial authorization
- **تصمیم:** مالک محصول به اعمال هر دو اصلاحیه پاسخ «بله» داد: `NSIM-EDIT-001` جایگزینی متن پاسخ `NSIM-SYN-034` و `NSIM-EDIT-002` اصلاح سؤال `NSIM-SYN-GP-022`. منظور، ساخت نسخه جانشین جدید از این دو *در بسته مصنوعی مشتق* است؛ ویرایش اصل JSONL یا از بین بردن تاریخچه ممنوع است.
- **مرز:** این تصمیم تصدیق محتوایی دو اصلاحیه است، نه ادعای اینکه مدیر عملیات شخصاً اصلاحیه‌ها را در تاریخ معین امضا کرده. نسخه مشتق باید قبل/بعد و SHAهای اصل/جدید را حفظ کند.


## D-0165 — شهادت مالک محصول برای پذیرش Business بسته مصنوعی اولیه کفایت می‌کند
- **تاریخ:** 2026-10-09
- **وضعیت:** Accepted scoped evidence policy
- **تصمیم:** مالک محصول تصریح کرد «بله نظرمن کافی است». بنابراین برای **تصمیم محتوایی و مجوز استفاده از بسته مصنوعیِ تألیفی اولیه** اظهار مالک محصول، سند Business معتبر است؛ درخواست تکراری صورت‌جلسه/امضای جداگانه برای اصل تصمیم ضرورتی ندارد.
- **مرز:** این راهکار هرگز `authenticated human electronic signature`، Legal Basis برای داده واقعی، Consent، تأیید مستقل سلامت/ایمنی یا تأیید Production Dataset/Model تلقی نمی‌شود. گزارش مالک محصول با گواهی مستقیم فرد بازبین متفاوت بماند.


## D-0166 — اختیار طراحی تقسیم Training/Evaluation و Benchmark مدل داخلی واگذار شد
- **تاریخ:** 2026-10-09
- **وضعیت:** Accepted technical delegation, **not automatic Production model choice**
- **تصمیم:** مالک محصول اختیار انتخاب راهبرد فنی تقسیم‌بندی مستقل، طراحی آزمایش و Benchmark مدل‌های **داخلی** را واگذار کرد. در Synthetic Seed اولیه از split **group-disjoint** استفاده شود: گروه‌های رفتاری `category` و برای ۳۲ مثال مثبت، گروه‌های `source_fixture_id` یکپارچه در یک پارتیشن قرار گیرند؛ اصل ۸۴ نمونه بدون مورد تکراری پوشش داده شود. گروه‌های Evaluation اولیه بر اساس `source_authenticity`، `privacy`، `untrusted_document_instruction`، `outdated_content` و fixtures `NSIM-FIX-002`/`NSIM-FIX-006` تعیین می‌شوند. تقسیم، قرارداد فنی قابل تغییر/نسخه‌بندی است، نه قانون ثابت Business یا اثبات حذف semantic leakage/overlap واقعی سالمندان.
- **گیت:** Benchmarks باید dataset/version، baseline، مدل‌ها، quality/uncertainty، مجموعه مستقل ارزیابی، leakage و fairness/coverage را ثبت کنند. الگوریتم/مدل نهایی و thresholds پیش از شواهد انتخاب نشوند. External AI API و خودکارشدن Promotion ممنوع است.


## D-0167 — فقط بسته مصنوعی اولیه؛ داده واقعی پس از پذیرش موردی و مجوز قانونی
- **تاریخ:** 2026-10-09
- **وضعیت:** Accepted
- **تصمیم:** در آغاز فقط ۸۴ نمونه مصنوعی تألیفیِ نسخه‌دار، با دو اصلاحیه مصوب، وارد بسته آفلاین Training/Evaluation شوند. داده واقعی سالمندان/Provider/Case، حتی اگر برای عملیات پذیرفته شده باشد، **تا تعیین Purpose مستقل، مبنای قانونی/رضایت لازم، Data Class، کنترل حساسیت و تأیید واقعی مدیر عملیات برای Training** مجاز نیست. مانع BC-007 برای داده واقعی برقرار است.
- **مرز:** Dataset مصنوعی اولیه با مدل Production/Runtime یا محتوای رسمی خدمات نسیم یکسان نیست؛ ۸ منبع داستانی به واقعیت عملیاتی تبدیل نمی‌شوند.


## D-0168 — مأموریت تدوین پیش‌نویس معیارهای Provider برای تصویب مدیر عملیات
- **تاریخ:** 2026-10-09
- **وضعیت:** Accepted drafting authorization ONLY
- **تصمیم:** مالک محصول با تدوین معیارهای صلاحیت، مدارک، قرارداد، جغرافیا، خدمت، کیفیت، حفظ حریم خصوصی، فعال‌سازی/تعلیق، پاسخ/شواهد خدمت توسط دستیار موافقت کرد؛ مدیر عملیات نسیم طبق D-0157 تصمیم‌گیر انسانی است.
- **مرز:** محتوای پیشنهادی **پیشنهاد برای Approval** است؛ هیچ نوع Provider، امتیاز/آستانه، مدارک الزام‌آور، activation یا انتخاب مقصد در سیستم به‌صورت نهایی ایجاد نشود.


## D-0169 — Keycloak گزینه منتخب معماری هویت و طراحی Stage تصویب شد
- **تاریخ:** 2026-10-09
- **وضعیت:** Accepted architecture selection, Stage/IdP provisioning NOT DONE
- **تصمیم:** مالک محصول انتخاب `Keycloak` را از گزینه اولویت‌دار D-0156 به معماری منتخب OIDC هویت نسیم ارتقا داد و تهیه معماری Stage را تصویب کرد. کانال قابل‌اجرا می‌تواند Backend-for-Frontend با Authorization Code + PKCE S256 و نشست HttpOnly/Secure و CSRF protection باشد، مشروط به Technical/QA review.
- **مرز:** هیچ Keycloak realm/hostname/client/certificate/secret/Role mapper، ماشین/ارائه‌دهنده زیرساخت یا محیط Stage واقعی انتخاب/راه‌اندازی نشده است. کد مرورگر تا تکمیل پیکربندی و Trust Boundary همچنان `401 BROWSER_SESSION_NOT_CONFIGURED` می‌دهد. D-0130 همچنان `Stage UNAVAILABLE` است. موافقت طراحی Stage ≠ دستور Deploy Stage/Production.



## D-0170 — انتخاب صریح گزینه سوم برای خرید فرزند به نفع سالمند

- **تاریخ:** 2026-10-09
- **حوزه:** Business / Family Companion Mobile / Purchase and Payer Boundary
- **وضعیت:** **ACCEPTED — محدود به فاز فعلی؛ استفاده از اعتبار سالمند DEFERRED**
- **منشأ:** مالک محصول پس از مشاهده سه گزینه صریح، پاسخ پیشین «فرزند فقط با حساب خودش برای سالمند خرید می‌کند» را با عبارت «نه گزینه 3 ثبت کن» اصلاح کرد. **گزینه سوم دقیقاً این بود:** «فعلاً خرید با حساب فرزند؛ استفاده از اعتبار سالمند را به تصمیم بعدی موکول کنیم». این گزینه ملاک تصمیم جاری است و جایگزین برداشتِ ممنوعیت دائمی از پاسخ قبلی می‌شود.
- **تصمیم فعلی:** در طرح آتیِ خرید به نفع سالمند، **سفارش‌دهنده/پرداخت‌کننده = فرزند با هویت و حساب خود**؛ **دریافت‌کننده خدمت = سالمند**. حساب یا اعتبار مالی سالمند **در فاز فعلی منبع پرداخت نیست**. فعال‌کردن پرداخت از منابع سالمند یا نمایندگی مالی **نه مجاز فرض می‌شود و نه برای همیشه رد می‌شود**؛ قرارداد و تأیید جداگانه در آینده لازم دارد.
- **مرزبندی هویت و اختیار:** نسبت فرزندی، دسترسی به پرونده، اختیار مراقبت و مجوز اقدام مالی چهار مفهوم مستقل‌اند. فرزند صرفاً با ادعای نسبت خانوادگی یا انتخاب «حالت همراه خانواده» حق مشاهده همه داده‌ها یا اقدام از جانب سالمند ندارد. نقش مستقل سالمند/همراه خانواده در اپ موبایل دوحالته یک **جهت طراحی UI** است؛ grant و authorization فعلی ایجاد نمی‌کند.
- **مرزبندی مالی و پیاده‌سازی:** این تصمیم **مجوز واقعی برداشت وجه، PSP، بانک، کیف پول، credit/settlement، قیمت، محصول/کاتالوگ یا حکم حقوقی نمایندگی ایجاد نمی‌کند**. Purchase/Payment workflow هنوز نیازمند Business/Technical contracts، امنیت، ارزیابی حقوقی و ادغام بیرونی واقعی است؛ Figma فقط طرح پیشنهادی است و نباید دکمه «پرداخت انجام شد» یا تراکنش واقعی را القا کند.
- **قابل پیگیری:** هر زمان مالک محصول استفاده از اعتبار سالمند را خواست، آن تصمیم جدید باید به‌صورت جداگانه همراه با صلاحیت، رضایت/اختیار، Scope، محدودیت‌ها، لغو اختیار، ثبت رویداد و حفاظت از سالمند تصویب شود. تا آن زمان **Deferred/Unavailable** است.



## D-0171 — پشته فناوری هدف نسیم: Python/FastAPI + PostgreSQL + React/TypeScript + React Native/TypeScript

- **تاریخ:** 2026-10-09
- **حوزه:** Technical Architecture / Delivery Channels / Internal AI
- **وضعیت:** **ACCEPTED technology direction** — implementation/deployment status is independently gated
- **منشأ تصمیم:** پس از ارائه ارزیابی حفظ Backend پایتون و پیشنهاد `React Native + TypeScript` برای اپ‌های موبایل، مالک محصول پاسخ «موافقم» داد.
- **Backend مصوب برای ادامه:** `Python 3.12 + FastAPI` و `PostgreSQL`، با `SQLAlchemy async + asyncpg + Alembic`. توسعه موجود باید حفظ شود؛ بازنویسی Backend به زبان دیگر بدون Benchmark واقعی توجیه ندارد.
- **کانال وب:** `React + TypeScript + Vite` برای محیط‌های سازمان حمایتگر، مدیریت/ادمین و عملیات مجاز نسیم. پیاده‌سازی فعلی فقط بخش‌های واقعی Case/Provider در شاخه‌های Draft را پوشش می‌دهد و پنل کامل حمایتگر هنوز محصول آماده نیست.
- **کانال موبایل:** `React Native + TypeScript` به‌عنوان فناوری منتخب برای **اپ سالمند با دو حالت «سالمند / همراه خانواده»** و **اپ عملیاتی سالمندیار حرفه‌ای**؛ دو نقش خانوادگی و حرفه‌ای نباید مخلوط شوند. Android/iOS قابلیت فنی فریم‌ورک‌اند؛ سفارش استقرار/انتشار فروشگاهی یا ترتیب پلتفرم‌ها هنوز مصوب نشده است.
- **مرز هویت و دسترسی:** یک Backend و قراردادهای API مشترک، اما هویت مستقل، Permission/Consent و Scope مجزای هر Actor. اشتراک قراردادهای TypeScript به معنی اشتراک Credential یا دسترسی کامل بین کاربران نیست. `Keycloak` مطابق D-0169 گزینه منتخب معماری OIDC است، نه سامانه متصل و آماده اجرا.
- **AI:** داخلی/نسیم‌مالک و با یادگیری کنترل‌شده و تفکیک Dataset/Training/Evaluation؛ `Python` بستر مناسب توسعه AI است، اما مدل نهایی، آموزش عملیاتی، Worker/Queue، منابع GPU، پارامترها و Production Activation به‌صورت شواهد-محور تعیین می‌شوند. هیچ API مدل بیرونی یا تصمیم مالی/درمانی/ارجاع خودکار از این تصمیم استنباط نمی‌شود.
- **مرز خرید خانواده:** D-0170 بدون تغییر معتبر است: فرزند فعلاً با حساب خودش برای سالمند خرید می‌کند؛ استفاده از منابع/اعتبار سالمند `DEFERRED` و قرارداد تجارت/پرداخت و PSP هنوز ساخته یا مستقر نشده است.
- **وضعیت واقعی:** Backend و Web در PRهای Draft/Open و `main` مستقل قرار دارند؛ دو اپ `React Native` هنوز پیاده‌سازی نشده‌اند؛ Stage واقعی به دلیل نبود زیرساخت D-0130 unavailable است. پذیرش فناوری ≠ ادعای پایان کدنویسی، QA، اتصال Keycloak یا مجوز Merge/Stage/Production.
- **برنامه توسعه:** Business contract و Capability Matrix هر کانال → Technical API/Security contracts → Backlog/Sprint → Code/Review → CI → Stage/QA gates → Release؛ Design System و Figma مرجع UI می‌شوند، نه منبع داده عملیاتی.



## D-0172 — تجربه یکپارچه خدمات و AI در اپ سالمند با ناوبری حرفه‌ای

- **تاریخ:** 2026-10-09
- **حوزه:** Business / Elder Mobile Experience / Internal AI / Accessibility
- **وضعیت:** **ACCEPTED phase-1 UX direction** — service operations, permissions and AI use-case contracts still independently gated
- **منشأ:** مالک محصول به پیشنهاد جریان یکپارچه «بیان نیاز/درخواست کمک → همراهی دستیار AI → بررسی و اقدام انسانی سالمندیار → ارجاع مجاز و پیگیری» پاسخ «موافقم» داد و تصریح کرد اپ باید ناوبری و ظاهر حرفه‌ای داشته باشد.
- **دامنه تجربه سالمند در فاز اول:** دسترسی ساده به ارتباط با سالمندیار، بیان نیاز و درخواست بررسی، اطلاعات و پیگیری‌های مجاز، و دستیار داخلی نسیم برای توضیح خدمات، کمک در فهم/بیان درخواست و راهنمایی. AI باید در بستر همان تجربه خدمت باشد، نه چت‌بات نامرتبط با عملیات.
- **مرز خدمت تخصصی:** سلامت، پزشکی، پرستاری، توانبخشی، سلامت روان، رفاه و حمایت تخصصی در فاز اول به‌صورت Service Family/مسیر بررسی و ارجاع انسانی طراحی می‌شوند؛ این تصمیم SKU، Service Catalog فعال، سفارش مستقیم خدمت تخصصی، Provider Activation، SLA، قیمت یا ادعای انجام خدمت ایجاد نمی‌کند. ارجاع رسمی، Provider Selection، مراحل و تغییر پرونده فقط بر اساس Business/Technical Contract و اختیار انسانی مصوب است.
- **مرز AI:** AI داخلی مطابق D-0004/D-0005 از روز اول بهره‌برداری هدف است؛ راهنمایی و پیش‌نویس پیشنهادی مجاز به طراحی‌اند اما AI بدون مسیر مصوب Review نمی‌تواند Need رسمی، تشخیص/تجویز پزشکی، ارجاع قطعی، انتخاب Provider، تأیید پرداخت، پرونده رسمی یا Outcome را ایجاد/تغییر دهد. نبود داده/Model معتبر باید fail-safe و بدون حدس/تصمیم ساختگی باشد. Training Eligibility، Dataset و Human Promotion مستقل باقی می‌مانند.
- **ناوبری و هویت بصری:** اپ موبایل باید ناوبری ثابت، واضح، راست‌به‌چپ و قابل‌درک برای سالمندان و ظاهر منسجم و حرفه‌ای داشته باشد. برای طراحی اولیه، چهار مقصد «خانه، خدمات، دستیار نسیم، پیگیری» به‌عنوان ساختار UX پذیرفته شد؛ «حساب کاربری/مجوزها» از سربرگ قابل دسترسی باشد. خوانایی، اندازه مناسب اهداف لمسی، کنتراست، زبان ساده و حالت‌های مجوز/عدم‌دسترسی جزء الزامات هستند؛ اعداد دقیق WCAG/پیاده‌سازی نهایی باید در QA آزموده شوند.
- **حالت همراه خانواده:** تجربه دیداری مشترک، هویت و Capability جدا؛ D-0170 پابرجاست: خرید فاز فعلی با حساب خود فرزند، استفاده از اعتبار سالمند `DEFERRED`؛ خرید واقعی، PSP و دسترسی به پرونده سالمند تا قرارداد و اتصال معتبر فعال نیستند.
- **مرز تأیید:** پذیرش مسیر UX به‌معنی پیاده‌سازی AI Voice، Notification، تماس واقعی، سرویس سفارش، قیمت/پرداخت یا تأیید ضمنی Consent نیست. طرح‌های Figma صراحتاً Prototype و بدون داده یا پرداخت واقعی هستند؛ نسخه نهایی و دسترس‌پذیری قبل از Code/Release QA می‌شوند.



## D-0173 — تأیید پالت مبنای سبز زمردی و مرجانی گرم برای طراحی نسیم

- **تاریخ:** 2026-10-09
- **حوزه:** Brand UI / Mobile Design System / Accessibility
- **وضعیت:** **ACCEPTED design baseline** — قابل بازنگری با شواهد تست و تأیید مستقل؛ نه تأیید نهایی تمام صفحات یا Release
- **منشأ:** پس از نمایش نسخه پرشده با داده‌های ساختگی و معرفی رنگ مرجانی برای رفع یکنواختی سبز، مالک محصول پیشنهاد «همین ترکیب سبز زمردی و مرجانی را مبنای ادامه طراحی بگذاریم» را با پاسخ «باشه موافقم» تصویب کرد.
- **رنگ اصلی:** `#005543` (سبز زمردی) برای هویت بصری و سطوح کلیدی.
- **رنگ متضاد/تأکیدی:** `#A94E43` (مرجانی گرم) برای اقدام مهم و تأکید محدود، با متن سفید خوانا.
- **رنگ سطوح تأکیدی:** `#FCECE7` (مرجانی روشن)، با `#702D26` (متن تیره مرجانی) برای انتخاب ناوبری و سطوح نمونه.
- **قواعد تجربه:** رنگ مرجانی جایگزین سبز هویتی نمی‌شود؛ انتخاب فعال فقط با رنگ مشخص نشود (آیکون/متن نیز داشته باشد)، هشدار و خطا نباید صرفاً با مرجانی نمایش داده شوند. خوانایی متن و مقیاس‌پذیری برای سالمندان و آزمون واقعی Accessibility الزامی است.
- **مرز داده:** نام‌ها، سن‌ها، پرونده‌ها، گفت‌وگوها و درخواست‌های نمایشیِ UX-005 ساختگی‌اند؛ استفاده از آن‌ها در Production، دسترسی، پرداخت یا آموزش AI مجاز نیست.
- **مرز تصویب:** این تصمیم فقط Design System و جهت طراحی را تثبیت می‌کند، نه فعال‌بودن خدمات، AI، درخواست‌ها، پرداخت، تکمیل اپ React Native، Code Review، Stage/QA یا انتشار. هر بهینه‌سازی بر اساس تست کاربری و دسترس‌پذیری قابل طرح و تصمیم مستقل است.



## D-0174 — نقش عملیاتی سازمان حمایتگر: تعریف افراد، مشاهده وضعیت و تأمین مالی

- **تاریخ:** 2026-10-09
- **حوزه:** Business / Supporter Organizations / Beneficiary Administration / Support Status / Funding
- **وضعیت:** **ACCEPTED high-level capability direction**؛ Business/Technical contract، مجوزها، داده قابل‌اشتراک و جریان مالی **OPEN/NOT AUTHORIZED**
- **منشأ:** مالک محصول پس از مشاهده پنل صرفاً گزارشی حمایتگر تصریح کرد: «باید حمایتگر بتونه آدم تعریف کنه، وضعیتشون ببینه، پول تزریق کنه و...».
- **جهت محصول:** پنل سازمان حمایتگر فقط Reporting نیست. حداقل باید مسیرهای مدیریت/معرفی **افراد تحت حمایت**، مشاهده **وضعیت حمایتی مجاز آن‌ها**، **تأمین مالی/تزریق وجه** و گزارش گردش حمایت‌ها را پشتیبانی کند. این گزاره نیازمندی کسب‌وکاری است، نه اجازه اجرای خودکار یا دسترسی بدون شرط.
- **مرز هویت:** «تعریف فرد تحت حمایت در یک سازمان» **متفاوت است** با ایجاد هویت حقیقی، پرونده سالمند در نسیم، تخصیص سالمندیار، تشخیص، احراز رابطه، یا تبدیل خودکار فرد به ذی‌نفع دارای حق مصرف اعتبار. رابطه معتبر میان سازمان، شخص و پرونده نسیم و رضایت/مبنای حقوقی باید جداگانه تصویب شود.
- **مرز وضعیت:** سازمان تنها می‌تواند اطلاعات و **وضعیت‌های مشخصاً مجاز و متناسب با هدف حمایتی** را ببیند؛ دسترسی عمومی به جزئیات پزشکی، داده حساس سالمند، تماس خانوادگی، رویدادهای داخلی پرونده و داده AI ایجاد نمی‌شود. فهرست وضعیت‌ها، منبع معتبر، سطح تجمیع/فردی و قواعد اشتراک هنوز باز هستند.
- **مرز مالی:** تزریق وجه نیازمند تعیین **منبع، مقصد، ذی‌نفع، مالک حساب/اعتبار، واحد پول، روش پرداخت، زمان اثر، مصرف، مانده، بازگشت/ابطال، مالک تصویب و گزارش حسابرسی** است. این تصمیم ایجاد Wallet، تخصیص خودکار اعتبار به سالمند، انتقال پول یا امکان برداشت را مجاز نمی‌کند. PSP، دفتر مالی، تسویه، دستور پرداخت، موجودی و نرخ‌ها همچنان بدون قرارداد/اتصال‌اند.
- **هم‌زیستی با D-0170:** در خرید آتی از طرف فرزند، **فرزند با حساب خودش پرداخت می‌کند**؛ استفاده از اعتبار سالمند **DEFERRED** می‌ماند. سازوکار حمایت مالی سازمان با این قاعده یکسان فرض نمی‌شود و باید جداگانه تعریف شود.
- **حاکمیت:** ثبت، تغییر رابطه، تخصیص اعتبار، برگشت پول یا نمایش اطلاعات فردی نیازمند اختیار انسانی، مسیر احراز هویت، ثبت ممیزی و کنترل Tenant/Purpose/Consent است. AI نمی‌تواند مستقل پول منتقل کند، اعتبار تخصیص دهد، مجوز اعطا کند یا وضعیت قطعی اعلام کند.
- **Design:** چهار صفحه جدید Figma با داده‌های کاملاً ساختگی و اقدام‌های مالی/ثبت واقعیِ غیرفعال در `UX-007`. همه صفحات حمایتگر ناوبری هماهنگ دریافت کرده‌اند. طراحی نشانه فعال‌بودن Backend یا تأیید قرارداد مالی نیست.
- **تکمیل ضروری:** تعیین (۱) مقصود دقیق از «آدم» و مبنای رابطه، (۲) مقصد و مالکیت وجه در «تزریق پول»، (۳) واژگان وضعیت‌ها و مرز داده فردی، (۴) دامنه گزارش/تراکنش و نحوه نظارت، پیش از Technical/Sprint/Code.



## D-0175 — انتخاب اعتبار اختصاصی هر فرد به‌عنوان مدل تأمین مالی حمایتگر

- **تاریخ:** 2026-10-09
- **حوزه:** Supporter Funding / Beneficiary Earmarking / Business Decision
- **وضعیت:** **ACCEPTED funding-destination direction**؛ قواعد مالکیت حساب، اعتبار قابل مصرف، ثبت مالی، مجوز پرداخت، گردش پول و پیاده‌سازی **OPEN/DEFERRED**
- **منشأ تصمیم:** مالک محصول صریحاً از میان سه گزینه «اعتبار اختصاصی هر فرد»، «موجودی عمومی سازمان با تخصیص بعدی» و «هر دو»، گزینه نخست را انتخاب کرد: «برای نسیم روش اعتبار اختصاصی هر فرد را انتخاب می‌کنم.»
- **قاعده مصوب:** سازمان حمایتگر برای **یک فرد مشخص**، حمایت/اعتبار با تخصیص اختصاصی تعریف می‌کند؛ سیستم نباید به‌صورت پیش‌فرض همه مبالغ را در یک موجودی عمومیِ قابل تخصیص مجدد میان افراد ادغام کند. «موجودی عمومی سازمانی» و «مدل ترکیبی» در این انتخاب **مدل‌های مصوب فاز جاری نیستند**.
- **تفکیک ثبت و اعتبار:** «اختصاص اعتبار به فرد» به معنی انتقال مستقیم پول به حساب بانکی فرد، مالکیت حقوقی کیف پول، وجود موجودی قابل برداشت، امکان خرج‌کردن یا ایجاد خودکار پرونده نسیم نیست. تحقق حقوقی/حسابداری آن به قرارداد بعدی وابسته است.
- **دسترسی:** فقط سازمان و Actor مجاز، رابطه معتبر حمایتگر–فرد و مقدار مجاز حمایت را با رعایت Consent، Purpose، Tenant و Audit مشاهده/مدیریت می‌کنند. رابطه مالی مجوز مشاهده پرونده سالمندیاری یا اطلاعات سلامت نیست.
- **مرز D-0170:** فرزند در خریدهای آینده با **حساب خودش** پرداخت می‌کند؛ اجازه خرج‌کردن اعتبار سالمند از سوی فرزند همچنان **DEFERRED** است و با D-0175 فعال نمی‌شود.
- **مرز AI:** AI حق تخصیص خودکار مبلغ، تعیین استحقاق، فعال‌کردن اعتبار قابل مصرف، انتقال وجه یا تأیید مالی را ندارد.
- **بازمانده تصمیم‌ها:** (۱) منبع و مقصد واقعی وجه، (۲) مالکیت حقوقی پول/حساب/اعتبار، (۳) واحد پول و ثبت حسابداری، (۴) نحوه و محدودیت مصرف اعتبار فرد، (۵) تأیید انسانی و ضدتقلب/موجودی و برگشت، (۶) انتخاب ارائه‌دهنده پرداخت/بانک، (۷) انقضا، لغو، بازگشت و گزارش حسابرسی، (۸) اتصال شخص تحت حمایت به Elder/Case و اختیارات دقیق نهاد حمایتگر.
- **Figma:** نمونه S08 در `UX-007` به مدل اختصاصی فرد و مثال کاملاً ساختگی مهتاب نیک‌رفتار/NSM-DEMO-101 به ارزش فرضی ۱۲٬۰۰۰٬۰۰۰ ریال تغییر کرده؛ CTA انتقال/ثبت واقعی **غیرفعال** است.
- **گیت:** Business/Legal financial contract → Technical/security/accounting → Backlog/Sprint → Code/Review → Stage/QA/Release. هیچ انتقال وجه/Stage/Production و تغییر API/DB با این تصمیم انجام نشده است.

## D-0176 — هدف مشارکت‌کنندگان پایلوت اولیه نسیم

- **تاریخ:** 2026-10-25
- **حوزه:** Business / Pilot / Initial cohort
- **وضعیت:** Accepted — اندازه هدف مشارکت‌کنندگان؛ سایر مرزهای پایلوت OPEN
- **تصمیم:** هدف برنامه‌ریزی فاز/پایلوت اولیه، حضور **۱۰۰ سالمند و ۱۰۰ سالمندیار** است.
- **مرز تفسیر:** این عدد هدف تعداد دو گروه است؛ به‌تنهایی سقف ثبت‌نام، نسبت تخصیص یک‌به‌یک، تعداد پرونده فعال، شرایط ورود، روش رضایت/پذیرش، شهر یا محدوده جغرافیایی، مدت پایلوت، ترکیب خدمات، KPI، معیار توقف/عبور یا مجوز آغاز بهره‌برداری را تعیین نمی‌کند.
- **اثر:** برنامه‌ریزی ظرفیت و طراحی جریان‌های محصول می‌تواند با این اندازه هدف انجام شود. هر Workflow عملیاتی همچنان تابع دامنه و تصمیم‌های لازم خودش است؛ Stage/Release/Production نیز گیت مستقل دارند.
- **منبع:** دستور مستقیم مالک محصول: «در فاز اول می‌خوام ۱۰۰ سالمند و ۱۰۰ سالمندیار داشته باشیم».


## D-0177 — استفاده از منابع اینترنتی برای آماده‌سازی Seed اولیه AI

- **تاریخ:** 2026-10-25
- **حوزه:** Business / AI / Initial seed sources
- **وضعیت:** Accepted — اجازه جست‌وجو و آماده‌سازی نامزدها؛ پذیرش هر منبع و Training Run جداگانه gated است
- **تصمیم:** منابع معتبرِ در دسترس از اینترنت می‌توانند برای تهیه نامزدهای محتواییِ Seed اولیه AI نسیم بررسی و آماده‌سازی شوند.
- **شرط منبع‌به‌منبع:** دسترس‌پذیری عمومی در وب، به‌تنهایی مجوز استفاده برای آموزش نیست. پیش از ورود هر منبع به Dataset، اصالت و نسخه، مالک/ناشر، مجوزی که استفاده موردنظر برای آموزش AI، ترجمه/اقتباس لازم و کاربرد برنامه‌ریزی‌شده محصول را پوشش می‌دهد، الزامات انتساب، محدودیت‌های قلمرو/تجاری، و بازبینی محتوایی باید ثبت شود. محتوای دارای حق‌نشر یا مجوز مبهم تا اخذ مجوز معتبر کنار گذاشته می‌شود.
- **حاکمیت:** این تصمیم اجازه می‌دهد منبع و مجوز بررسی و نامزدهای مجاز آماده شوند؛ جایگزین تأیید منبع/Training Eligibility مرجع سازمانی D-0161، بررسی حرفه‌ای/حقوقی لازم، یا گیت مستقل Training/Evaluation/Promotion نیست. تا تأیید منبع، داده در وضعیت `CANDIDATE_NOT_AUTHORIZED` می‌ماند و Training Run آغاز نمی‌شود.
- **مرز داده:** این اختیار فقط درباره منابع اینترنتی برای Seed اولیه است؛ استفاده از داده‌های واقعی سالمند، سالمندیار، Case، Provider، گفت‌وگو یا سایر داده‌های تولیدشده در نسیم را مجاز نمی‌کند و الزام Dataset پیوسته و نسخه‌دار D-0005 از داده عملیاتیِ جداگانه و واقعاً مجاز را برآورده نمی‌کند.
- **منبع:** دستور مستقیم مالک محصول: «می‌تونی از داده‌های اینترنت برای آموزش اولیه استفاده کنی».

