# BC-016 — Service Operations, Scheduling, Field Work & Case Management

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + BC-003 + BC-005 + BC-015 + D-0004 + D-0005
- **Depends on:** BC-002, BC-003, BC-005, BC-006, BC-012, BC-013, BC-015

> این سند چارچوب کسب‌وکاری عملیات روزمره سالمندیار، Case ownership، برنامه‌ریزی تماس/پیگیری، فعالیت میدانی و جانشینی را تعریف می‌کند. منبع اولیه Cadence، Visit Schedule، نسبت سالمند به سالمندیار، State Machine کارها یا قواعد تخصیص/جانشینی را تعیین نکرده است؛ بنابراین این موارد در این سند نهایی نمی‌شوند.

## 1. Operational Principle

طرح مبنا عملیات نسیم را بر این اصول قرار می‌دهد:

- محله‌محوری
- پاسخ‌گویی سریع
- خدمات یکپارچه
- ارجاع هوشمند
- ثبت کامل اطلاعات
- پایش مستمر کیفیت
- حفظ کرامت سالمند
- توسعه‌پذیری

این اصول باید در مدل عملیات روزانه قابل مشاهده باشند، اما هیچ SLA یا زمان پاسخ عددی در منبع تعیین نشده است.

## 2. Single Point of Contact

در مدل منبع، سالمند فقط با یک نقطه تماس مواجه است و سالمندیار نزدیک‌ترین حلقه ارتباطی او با شبکه است.

بنابراین Business Design آینده باید بتواند برای هر سالمند، مسئول عملیاتی ارتباط را مشخص کند.

اما هنوز تعیین نشده است:

- آیا دقیقاً یک سالمندیار Primary وجود دارد
- آیا Co-owner مجاز است
- سالمندیار جایگزین چگونه تعیین می‌شود
- تغییر مالک Case چگونه انجام می‌شود
- در مرخصی/غیبت چه اتفاقی می‌افتد
- آیا Supervisor می‌تواند موقتاً Case را در اختیار بگیرد

## 3. Case Concept — DRAFT FRAME

منبع واژه فنی «Case» را تعریف نکرده است، اما از پرونده سالمند، ارتباط مستمر، نیاز، ارجاع و پیگیری صحبت می‌کند.

برای طراحی آینده می‌توان مفهوم Case را به‌عنوان Container عملیاتی برای این موارد بررسی کرد:

- elder profile/context
- active needs
- follow-ups
- referrals
- service history
- assigned worker
- open operational tasks
- complaints/incidents مرتبط

این Frame به معنی تصویب Entity یا Data Model نهایی نیست.

## 4. Elder Assignment — Open Contract

شبکه سالمندیاران بر اساس پراکندگی جغرافیایی سالمندان سازمان‌دهی می‌شود.

برای Assignment آینده باید حداقل این عوامل بررسی شوند:

- geography
- worker availability
- workload
- continuity of relationship
- language/cultural fit در صورت نیاز
- service complexity
- supervisory boundary

هیچ الگوریتم، Score یا نسبت ظرفیت فعلاً مصوب نیست.

## 5. Assignment Authority

هنوز مشخص نشده است:

- چه کسی سالمند را به سالمندیار تخصیص می‌دهد
- چه کسی Reassignment را تأیید می‌کند
- سالمند حق درخواست تغییر سالمندیار دارد یا خیر
- خانواده چه نقشی دارد
- AI آیا می‌تواند فقط پیشنهاد دهد یا نقشی ندارد

تا تصمیم صریح، تخصیص نهایی نباید به AI واگذار شود.

## 6. Contact & Monitoring Cadence

منبع ارتباط منظم و پایش مستمر را قطعی می‌داند، اما Cadence را تعیین نمی‌کند.

باید در آینده برای هر Segment/Need مشخص شود:

- minimum contact expectation
- type of contact
- follow-up interval
- reassessment trigger
- missed-contact handling
- escalation after no-contact

هیچ برنامه روزانه/هفتگی/ماهانه در BC-016 تعیین نمی‌شود.

## 7. Contact Channels

طرح اولیه Channel مشخصی برای ارتباط با سالمند تعیین نکرده است.

بنابراین هنوز باز است که ارتباط از چه مسیرهایی انجام شود، مانند:

- تماس تلفنی
- مراجعه حضوری
- پیام‌رسان
- اپلیکیشن
- تماس ویدیویی
- ارتباط از طریق خانواده

هیچ Channel به‌عنوان الزامی یا پیش‌فرض نهایی تصویب نشده است.

## 8. Field Work Boundary

منبع، «آمادگی فعالیت میدانی» را برای سالمندیار ضروری می‌داند و شبکه را محله‌محور تعریف می‌کند.

اما نوع و فراوانی فعالیت میدانی را تعیین نمی‌کند.

بنابراین هنوز تصمیم نشده است:

- بازدید منزل الزامی است یا خیر
- Visit cadence
- Geographic radius
- Travel policy
- Lone-worker safety
- check-in/check-out
- transportation responsibility
- expense reimbursement

## 9. Daily Work Planning — DRAFT FRAME

برای عملیات مقیاس‌پذیر، سامانه آینده باید بتواند Work Queue یا Task Planning را پشتیبانی کند.

Candidate task sources:

- planned contact
- follow-up
- referral follow-up
- satisfaction follow-up
- reassessment
- supervisor request
- complaint/incident follow-up
- training requirement
- data correction

اینها Candidate هستند و Task taxonomy نهایی نیستند.

## 10. Task Lifecycle — NOT FINAL

برای تحلیل Business ممکن است Taskها وضعیت‌هایی مانند:

`Planned → Due → In Progress → Done / Deferred / Escalated`

داشته باشند.

این فقط مثال برای نیاز عملیاتی است و State Machine نهایی محسوب نمی‌شود.

## 11. Missed / Uncompleted Work

برای کار برنامه‌ریزی‌شده‌ای که انجام نمی‌شود باید Rule آینده تعیین شود.

نمونه وضعیت‌ها:

- elder unavailable
- worker unavailable
- provider dependency
- connectivity issue
- consent/authorization blocker
- operational overload
- safety concern

هنوز مشخص نیست چه چیزی Deferred، Escalated یا Failed محسوب می‌شود.

## 12. Reassignment & Continuity

از آنجا که سالمندیار نقطه تماس اصلی است، Reassignment نباید باعث از دست رفتن Context شود.

در طراحی آینده باید مشخص شود:

- handover evidence
- open needs
- active referrals
- unresolved complaints/incidents
- upcoming tasks
- recent observations
- permissions/access transfer

Workflow نهایی Handover هنوز تعیین نشده است.

## 13. Absence & Substitution

برای مواردی مانند:

- مرخصی
- بیماری
- قطع همکاری
- جابه‌جایی منطقه
- تعلیق
- overload

باید Substitute/Backup rule وجود داشته باشد.

اما BC-016 تعیین نمی‌کند چه Actor یا سطحی جانشین می‌شود.

## 14. Supervisor Operational Role — DRAFT FRAME

سطوح سرپرستی در منبع وجود دارند، اما اختیار دقیق آنها مشخص نیست.

در عملیات آینده ممکن است نیاز باشد Supervisor بتواند:

- workload را مشاهده کند
- Caseهای بدون Owner را ببیند
- backlog و overdue work را ببیند
- Reassignment پیشنهاد/تأیید کند
- Escalation را بررسی کند
- quality issue را دنبال کند

اینها Candidate capability هستند و Decision Right نهایی نیستند.

## 15. Scheduling vs Clinical Scheduling

برنامه‌ریزی کار سالمندیار با Scheduling خدمات تخصصی Provider یکی نیست.

تفکیک:

- **Worker Schedule:** برنامه فعالیت سالمندیار
- **Service Appointment:** زمان ارائه خدمت توسط Provider
- **Referral Timeline:** زمان‌بندی چرخه ارجاع

این سه نباید در Technical به‌صورت یک مفهوم واحد فرض شوند.

## 16. Service Appointment Boundary

طرح اولیه وجود خدمات تخصصی را قطعی می‌داند ولی Scheduling آنها را تعریف نمی‌کند.

هنوز باز است:

- چه کسی وقت Provider را رزرو می‌کند
- سالمند انتخاب زمان دارد یا خیر
- سالمندیار فقط هماهنگ می‌کند یا رزرو می‌کند
- Cancellation/Reschedule چگونه است
- Reminder چگونه ارسال می‌شود

## 17. Operational Documentation

منبع «ثبت کامل اطلاعات» و ثبت نیازها/خدمات/ارجاعات را اصل می‌داند.

برای هر فعالیت عملیاتی آینده باید مشخص شود:

- چه چیزی باید ثبت شود
- چه کسی ثبت می‌کند
- چه زمانی
- چه Evidence لازم است
- چه داده‌ای Official Record است
- چه چیزی Draft است

AI-generated content به‌صورت پیش‌فرض Official Record نیست.

## 18. AI in Daily Operations — Day-one

بر اساس D-0004 و D-0005، AI از روز اول در عملیات حضور دارد.

Candidate uses در عملیات روزمره، منوط به تصویب Use Case:

- خلاصه‌سازی کارهای باز
- یادآوری Follow-up
- پیشنهاد اولویت بررسی
- آماده‌سازی Draft note
- برجسته‌سازی تغییرات
- کمک به یافتن Service/Process

### Boundary

AI تا تصمیم صریح:
- Case را نهایی تخصیص نمی‌دهد
- Reassignment را نهایی نمی‌کند
- Referral را نهایی نمی‌کند
- Closure را نهایی نمی‌کند
- Emergency decision نهایی نمی‌گیرد

## 19. AI-generated Operational Signals

برای جلوگیری از اختلاط، باید بتوان این موارد را جدا نگه داشت:

- system-generated task
- human-created task
- AI-suggested task
- human-confirmed task

پیشنهاد AI نباید بدون Rule مصوب به تعهد رسمی عملیاتی تبدیل شود.

## 20. Automatic Dataset Link

داده‌های حاصل از عملیات روزانه می‌توانند طبق D-0005 منبع Datasetهای جدید باشند، اما فقط پس از اعمال Eligibility Rules.

نمونه منابع بالقوه:

- contact records
- follow-up outcomes
- human edits to AI drafts
- accepted/rejected suggestions
- service/referral outcomes
- satisfaction
- operational incidents

هیچ‌یک ذاتاً Training-eligible نیستند.

## 21. Workload & Capacity

مدل عملیات باید بتواند Workload را بسنجد، اما Unit نهایی مشخص نیست.

Candidate dimensions:

- assigned elders
- active needs
- open referrals
- due follow-ups
- field workload
- geographic spread
- complexity
- incident burden

Threshold یا Capacity Score هنوز تعیین نشده است.

## 22. Overload Handling

در صورت Overload باید Rule آینده برای این موارد وجود داشته باشد:

- reassignment
- workload balancing
- supervisor escalation
- temporary intake limit
- delayed noncritical work
- additional workforce activation

هیچ Rule یا Threshold فعلاً تصویب نشده است.

## 23. Offline / Low-connectivity Operations

طرح اولیه نیاز فنی Offline را تعیین نکرده است، اما فعالیت میدانی ممکن است در محیط‌های با اتصال محدود رخ دهد.

این موضوع باید در Technical بررسی شود، ولی BC-016 الزام قطعی Offline mode ایجاد نمی‌کند.

## 24. Operational Auditability

برای فعالیت‌های مهم باید در آینده مشخص باشد:

- actor
- action
- time
- related elder/case
- source
- previous/new state در صورت تغییر رسمی
- AI involvement در صورت وجود

ساختار Audit Log در Technical تعیین می‌شود.

## 25. Explicit Non-Decisions

BC-016 موارد زیر را تصویب نمی‌کند:

- Primary-worker rule نهایی
- elder-to-worker ratio
- visit frequency
- mandatory home visit
- working hours
- shift model
- 24/7 coverage
- contact channel
- task state machine
- automated prioritization
- automated assignment
- AI assignment
- supervisor span of control
- travel reimbursement
- provider appointment workflow
- offline requirement

## 26. Open Decisions Required to Accept BC-016

1. Case ownership model
2. Assignment rule
3. Reassignment authority
4. Contact cadence
5. Monitoring cadence
6. Contact channels
7. Field-visit policy
8. Daily task taxonomy
9. Task lifecycle
10. Missed-work handling
11. Absence/substitution rule
12. Handover rule
13. Supervisor operational authority
14. Appointment coordination rule
15. Operational documentation minimum
16. Workload/capacity model
17. Overload handling
18. AI role in daily operations
19. AI-suggested task confirmation rule
20. Offline/low-connectivity requirement

## 27. Downstream Constraints

تا پیش از Accepted شدن BC-016:

- Backend نباید Case/Task State Machine نهایی را اختراع کند.
- Scheduler نباید Cadence یا Visit Frequency را Hard-code کند.
- Assignment نباید خودکار یا AI-driven فرض شود.
- غیبت سالمندیار نباید باعث از دست رفتن Open Need/Referral/Task شود.
- UI باید Human Action را از AI Suggestion قابل تفکیک نگه دارد.
- Workload KPI نباید بدون Business definition به Capacity limit تبدیل شود.
- عملیات Day-one باید AI را در Use Caseهای مصوب پشتیبانی کند، اما AI نباید صاحب Case یا تصمیم‌گیر نهایی باشد.
