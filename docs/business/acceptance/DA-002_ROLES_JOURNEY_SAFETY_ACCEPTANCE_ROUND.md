# DA-002 — Product Owner Decision Acceptance Round: Roles + Journey + Safety

- **Status:** AWAITING PRODUCT OWNER DECISION
- **Stage:** Business — Decision Acceptance
- **Date:** 2026-10-06
- **Source basis:** DC-003 + DC-004 + D-0004 + D-0005
- **Decision range:** D-0011…D-0020
- **Purpose:** ارائه Candidate Decisionهای Roles، Authority، Journey، Follow-up و Emergency Boundary برای Accept / Modify / Reject / Defer، بدون Acceptance ضمنی.

> این سند Decision Register نیست. تا زمانی که مالک محصول تصمیم صریح ندهد، هیچ‌یک از D-0011 تا D-0020 Accepted محسوب نمی‌شوند و `docs/DECISIONS.md` تغییر نمی‌کند.

## 1. Review Rule

برای هر Candidate یکی از Outcomeهای زیر لازم است:

- **ACCEPT**
- **ACCEPT WITH MODIFICATION**
- **REJECT**
- **DEFER FOR CURRENT PILOT**
- **MERGE WITH ANOTHER DECISION**

Recommendation فقط پیشنهاد است.

---

## 2. D-0011 — Employer / Operator / Provider Separation

### Proposed decision

سه نقش «کارفرما»، «اپراتور نسیم» و «Provider تخصصی» متمایز هستند و هیچ‌کدام به‌صورت پیش‌فرض اختیار نقش دیگر را ندارد.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 3. D-0012 — Caregiver Authority Boundary

### Proposed decision

دامنه پایه سالمندیار شامل ارتباط، پایش، ثبت، هماهنگی، Referral و Follow-up است. از این مسئولیت‌ها اختیار تخصصی پزشکی/درمانی، اختیار مالی، Provider activation یا Eligibility نهایی استنتاج نمی‌شود.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 4. D-0013 — Job Title Does Not Create Permission

### Proposed decision

عنوان شغلی یا جایگاه در مسیر رشد، به‌تنهایی Permission یا Approval Right ایجاد نمی‌کند. Authority هر سطح باید در Authority Matrix مستقل تصویب شود.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 5. D-0014 — System Is Not an Independent Business Authority

### Proposed decision

سامانه نسیم قواعد مصوب را اجرا و ثبت می‌کند و صرف خودکار بودن Workflow به سامانه Business Decision Right مستقل نمی‌دهد.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 6. D-0015 — Human / System / AI / Automation Traceability

### Proposed decision

Actionهای مهم باید از نظر منشأ Human / System / AI / Automation قابل تفکیک و Audit باشند. AI suggestion، System execution و Human decision نباید به‌صورت Actor مبهم ثبت شوند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 7. D-0016 — Single Point of Contact

### Proposed decision

سالمند در Journey نسیم باید یک نقطه تماس نزدیک و قابل پیگیری داشته باشد و سالمندیار رابط اصلی هماهنگی با شبکه است.

### Boundary

جانشینی، Handover و Case-owner change هنوز Rule مستقل می‌خواهند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 8. D-0017 — High-level Elder Journey

### Proposed decision

Journey پایه نسیم:

`ارتباط اولیه → پرونده → پایش → Need → ثبت/ارزیابی اولیه → Referral در صورت نیاز → Service → Follow-up → Satisfaction → ادامه پایش`

### Boundary

Stateها، SLAها، Priorityها و Approvalها هنوز جداگانه تعیین می‌شوند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 9. D-0018 — Follow-up Is Core

### Proposed decision

Follow-up ارائه خدمت و Satisfaction جزء مسئولیت‌های پایه سالمندیار و Journey رسمی نسیم است.

### Boundary

Cadence، SLA، Evidence و Escalation Trigger هنوز باز هستند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 10. D-0019 — No Automatic Need Closure

### Proposed decision

Service Completion به‌تنهایی Need را حل‌شده تلقی نمی‌کند و Referral Closure نیز به‌تنهایی Need Resolution نیست.

`Service Completion ≠ Referral Closure ≠ Need Resolution ≠ Outcome`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 11. D-0020 — Emergency Boundary

### Proposed decision

آموزش مدیریت شرایط اضطراری برای سالمندیار لازم است؛ اما این الزام به‌تنهایی به معنی تعهد 24/7، Medical Triage یا ارائه مستقیم Service اضطراری توسط سالمندیار/نسیم نیست.

Technical نباید از آموزش اضطراری، Workflow یا SLA اختراع کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 12. What acceptance of D-0011…D-0020 would close

در صورت پذیرش این ده Candidate:

- تفکیک Actorهای اصلی تثبیت می‌شود.
- مرز پایه اختیار سالمندیار روشن می‌شود.
- Job Title از Permission جدا می‌شود.
- System/AI از Business Authority مستقل منع می‌شوند.
- Traceability تصمیم/اجرا تثبیت می‌شود.
- Single Point of Contact و Journey پایه تثبیت می‌شوند.
- Follow-up/Satisfaction به‌عنوان وظیفه Core تثبیت می‌شوند.
- Completion/Closure/Resolution/Outcome از هم جدا می‌شوند.
- Emergency Training از Emergency Service/24x7/Triage جدا می‌شود.

## 13. Blockers that remain even after acceptance

1. final Pilot role inventory
2. Elder decision rights
3. Authorized Representative model
4. Caregiver Authority Matrix
5. Supervisor Authority Matrix
6. Provider Decision Rights
7. Employer Decision Rights
8. Referral authorization
9. Provider selection authority
10. Referral lifecycle states
11. acceptance/rejection/cancellation
12. Referral closure criteria
13. Need resolution/reopen
14. Reassessment trigger/cadence
15. Escalation owner/path
16. Complaint owner/path
17. Urgent definition
18. Emergency definition/path
19. Provider failure/re-routing
20. Unreachable elder handling
21. substitute/case ownership
22. Satisfaction method
23. SLA/response expectations
24. Consent requirement before Referral
25. Incident/Risk authority
26. Delegation/Substitution and Separation of Duties

## 14. Decision Register update rule

پس از تصمیم صریح مالک محصول:
- ACCEPT → در `docs/DECISIONS.md` ثبت می‌شود.
- ACCEPT WITH MODIFICATION → متن اصلاح‌شده ثبت می‌شود.
- REJECT → فقط نتیجه Review ثبت می‌شود؛ Accepted Decision ساخته نمی‌شود.
- DEFER → Scope، Owner، Future Gate و Constraint لازم است.
- MERGE → ارتباط با Decision مقصد باید Traceable باشد.

## 15. Current dependency note

DA-001 برای D-0006…D-0010 همچنان **PENDING** است. ایجاد DA-002 به معنی Acceptance ضمنی DA-001 نیست.

## 16. Recommended Product Owner response

برای پذیرش Recommendation فعلی:

`D-0011 تا D-0020 همگی ACCEPT`

یا هر Decision جداگانه با Outcome/Modification اعلام شود.

## 17. Gate status

تا زمان تصمیم صریح مالک محصول:

**Business → Technical: NOT READY**

و:

**Decision Acceptance Round DA-002: WAITING FOR PRODUCT OWNER**
