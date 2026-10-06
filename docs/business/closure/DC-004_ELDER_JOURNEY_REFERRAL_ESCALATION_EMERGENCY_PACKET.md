# DC-004 — Elder Journey, Referral Authority, Escalation & Emergency Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + BC-003 + BC-012 + BC-016 + BC-019
- **Purpose:** آماده‌سازی تصمیم‌های Journey، Referral، Follow-up، Escalation و Emergency بدون اختراع State Machine، SLA یا Triage تخصصی.

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند.

## 1. Source-confirmed Journey

منبع این جهت را مشخص می‌کند:

- سالمند یک نقطه تماس دارد.
- درخواست ابتدا توسط سالمندیار ثبت و ارزیابی اولیه می‌شود.
- سپس بر اساس نوع Need به شبکه سلامت، رفاه یا سایر خدمات ارجاع می‌شود.
- سالمندیار ارائه خدمت و رضایت سالمند را پیگیری می‌کند.

نمای سطح بالا:

`ارتباط → پرونده → پایش → Need → ثبت/ارزیابی اولیه → Referral → Service → Follow-up → Satisfaction → ادامه پایش`

این Flow، State Machine فنی نهایی نیست.

## 2. Candidate D-0016 — Single Point of Contact

- **تصمیم پیشنهادی:** سالمند در Journey نسیم باید یک نقطه تماس نزدیک و قابل پیگیری داشته باشد و سالمندیار رابط اصلی هماهنگی با شبکه است.
- **Boundary:** جانشینی یا تغییر Case Owner هنوز Rule مستقل می‌خواهد.

**Assessment:** Source-supported; recommended for acceptance.

## 3. Candidate D-0017 — High-level Journey

- **تصمیم پیشنهادی:** Journey پایه نسیم شامل ارتباط اولیه، تشکیل/به‌روزرسانی پرونده، پایش، شناسایی و ثبت Need، ارزیابی اولیه، Referral در صورت نیاز، ارائه Service، Follow-up، دریافت Satisfaction و ادامه پایش است.
- **Boundary:** Stateها، SLAها، Priorityها و Approvalها هنوز تعیین نشده‌اند.

**Assessment:** Source-supported; recommended for acceptance.

## 4. Referral Trigger — Minimum Source Boundary

حداقل شرط قابل استناد برای Referral:

- Need شناسایی شده باشد؛ و
- پاسخ به آن Need نیازمند اتصال به Service/Layer تخصصی باشد.

اما منبع مشخص نمی‌کند:
- Referral چه کسی نهایی می‌کند
- آیا برخی Referralها Approval می‌خواهند
- Provider چگونه انتخاب می‌شود
- Consent در چه نقطه‌ای لازم است
- Financial approval چگونه انجام می‌شود

این موارد **Blocking** هستند.

## 5. Referral Lifecycle — Still Open

منبع وجود Referral را قطعی می‌کند ولی State Machine را مشخص نمی‌کند.

نمونه‌هایی مانند Pending، Accepted، Rejected، Scheduled، Completed یا Cancelled فقط Candidate هستند و نباید پیش از Business Decision نهایی Hard-code شوند.

## 6. Candidate D-0018 — Follow-up Is Core

- **تصمیم پیشنهادی:** Follow-up ارائه خدمت و Satisfaction جزء مسئولیت‌های پایه سالمندیار و Journey رسمی نسیم است.
- **Boundary:** Cadence، SLA، Evidence و Escalation Trigger هنوز باز هستند.

**Assessment:** Source-supported; recommended for acceptance.

## 7. Service Completion vs Need Resolution

همسو با BC-019 باید این مفاهیم جدا بمانند:

- Service Completion
- Referral Closure
- Need Resolution
- Observed Outcome

اصل:

`Service Completion ≠ Referral Closure ≠ Need Resolution ≠ Outcome`

## 8. Candidate D-0019 — No Automatic Need Closure

- **تصمیم پیشنهادی:** Completion خدمت به‌تنهایی Need را حل‌شده تلقی نمی‌کند و Referral Closure نیز به‌تنهایی Need Resolution نیست.
- **Boundary:** Resolution/Reopen Rule و Evidence لازم هنوز جداگانه تعیین می‌شوند.

**Assessment:** Governance-derived; recommended for acceptance.

## 9. Reassessment — Still Open

منبع Reassessment رسمی تعریف نمی‌کند. Candidate triggerها:
- بعد از Service
- بعد از Referral Completion
- در Follow-up
- پس از تغییر مهم
- پس از Incident
- پیش از Need Closure

هیچ Trigger نهایی در این Packet پذیرفته نمی‌شود.

## 10. Escalation — Still Open

برای Escalation باید بعداً مشخص شود:
- trigger
- initiating actor
- destination
- effect on open Referral
- notification
- closure evidence

Escalation با Complaint، Incident و Emergency یکی نیست.

## 11. Emergency — Source Boundary

منبع فقط تصریح می‌کند سالمندیار پیش از شروع فعالیت باید آموزش «مدیریت شرایط اضطراری» ببیند.

منبع درباره مسیر عملیاتی Emergency، Triage تخصصی، تعهد 24/7، SLA یا Service اضطراری مستقیم تصمیمی نمی‌دهد.

## 12. Candidate D-0020 — Emergency Boundary

- **تصمیم پیشنهادی:** آموزش مدیریت شرایط اضطراری برای سالمندیار لازم است؛ اما تا تصویب Contract مستقل، این الزام به معنی تعهد 24/7، Triage تخصصی یا ارائه مستقیم Service اضطراری توسط سالمندیار/نسیم نیست.
- **Rule:** Technical نباید از آموزش اضطراری، Workflow یا SLA اختراع کند.

**Assessment:** Source-supported boundary; recommended for acceptance.

## 13. Urgent/Emergency Definitions — Blocking

Business هنوز باید تعیین کند:
- Urgent چیست
- Emergency چیست
- چه Actorی تشخیص عملیاتی اولیه می‌دهد
- چه زمانی Journey عادی متوقف/تغییر می‌کند
- چه مسیر بیرونی یا داخلی استفاده می‌شود
- چه Follow-upی لازم است

## 14. Provider Failure — Blocking

در صورت عدم پذیرش، عدم پاسخ، نبود ظرفیت، تأخیر یا Service failure باید Rule جداگانه برای:
- Re-route
- Approval
- Notification
- Escalation/Incident
وجود داشته باشد.

## 15. Unreachable Elder — Blocking

در صورت عدم دسترسی به سالمند باید بعداً تعیین شود:
- تعداد/روش تلاش
- Channel
- Escalation
- نقش Family/Representative
- شرایط بستن Task/Referral

هیچ مقدار عددی در منبع وجود ندارد.

## 16. Case Ownership During Absence — Blocking

Single Point of Contact باید در غیبت یا تعویض سالمندیار حفظ شود. Rule آینده باید جانشینی، Handover، Access و Audit را مشخص کند.

## 17. Satisfaction Boundary

رضایت سالمند در منبع قطعی است، اما روش سنجش، Scale، زمان و اثر آن بر Complaint/Closure تعیین نشده است.

همچنین:

`Satisfaction ≠ Outcome`

## 18. AI in Journey

AI در Use Caseهای مصوب می‌تواند توضیح، Summary، Flag و پیشنهاد سؤال/Service Family ارائه دهد.

اما تا Decision صریح:
- Need نهایی نمی‌کند
- Severity/Emergency نهایی نمی‌کند
- Referral نهایی نمی‌کند
- Provider نهایی انتخاب نمی‌کند
- Need را نمی‌بندد

## 19. Candidates Ready for Acceptance

- **D-0016:** Single Point of Contact
- **D-0017:** High-level Elder Journey
- **D-0018:** Follow-up/Satisfaction as core caregiver duty
- **D-0019:** Completion/Closure/Resolution/Outcome are distinct
- **D-0020:** Emergency training required; no inferred 24/7/Triage/direct emergency service

## 20. Product-owner Decisions Still Blocking

1. Referral authorization
2. Provider selection authority
3. Referral lifecycle states
4. Acceptance/rejection/cancellation rules
5. Referral closure criteria
6. Need resolution/reopen rule
7. Reassessment triggers/cadence
8. Escalation trigger/owner/path
9. Complaint path
10. Urgent definition
11. Emergency definition/path
12. Provider failure/re-routing
13. Unreachable elder handling
14. Substitute/Case ownership
15. Satisfaction method
16. SLA/response expectations
17. Consent requirement before Referral

## 21. Gate Effect

پذیرش D-0016 تا D-0020 مرز Journey و Safety را روشن‌تر می‌کند، اما Technical Entry Gate همچنان **NOT READY** می‌ماند تا Referral Authority، Lifecycle و Emergency Path حداقلی بسته شوند.

## 22. Next Closure Packet

**DC-005 — Legal, Consent, Data Access & Training Eligibility Decision Packet**
