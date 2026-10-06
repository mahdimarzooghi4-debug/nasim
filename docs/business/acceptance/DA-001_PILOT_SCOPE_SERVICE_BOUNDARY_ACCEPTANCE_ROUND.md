# DA-001 — Product Owner Decision Acceptance Round: Pilot Scope + Service Boundary

- **Status:** AWAITING PRODUCT OWNER DECISION
- **Stage:** Business — Decision Acceptance
- **Date:** 2026-10-06
- **Source basis:** DC-001 + DC-002 + D-0004 + D-0005
- **Decision range:** D-0006…D-0010
- **Purpose:** ارائه پنج Candidate Decision نخست به مالک محصول برای Accept / Modify / Reject / Defer، بدون Acceptance ضمنی.

> این سند Decision Register نیست. تا زمانی که مالک محصول تصمیم صریح ندهد، هیچ‌یک از D-0006 تا D-0010 Accepted محسوب نمی‌شوند و `docs/DECISIONS.md` تغییر نمی‌کند.

## 1. Review Rule

برای هر Candidate یکی از Outcomeهای زیر لازم است:

- **ACCEPT**
- **ACCEPT WITH MODIFICATION**
- **REJECT**
- **DEFER FOR CURRENT PILOT**
- **MERGE WITH ANOTHER DECISION**

Recommendation فقط پیشنهاد است و جای تصمیم مالک محصول را نمی‌گیرد.

---

## 2. D-0006 — Phase-1 Target Population

### Proposed decision

- **حوزه:** Business / Phase-1 Scope
- **تصمیم:** جامعه هدف فاز اول نسیم، سالمندان تحت حمایت کمیته امداد امام خمینی (ره) است.
- **Boundary:** این تصمیم سن دقیق، Eligibility جزئی، اولویت‌بندی، شهر/استان پایلوت یا تعداد افراد را تعیین نمی‌کند.
- **Expansion:** ورود سایر سالمندان یا کارفرمایان به فازهای بعدی و Gate مستقل موکول می‌شود.

### Recommendation

**ACCEPT**

### Reason

این تصمیم مستقیماً توسط Concept مبنا پشتیبانی می‌شود و چیزی درباره Geography، Count یا Eligibility جزئی اختراع نمی‌کند.

### Product Owner Decision

**PENDING**

---

## 3. D-0007 — Pilot Purpose

### Proposed decision

- **حوزه:** Business / Pilot
- **تصمیم:** پایلوت نسیم یک Pilot عملیاتی واقعی برای اعتبارسنجی مدل سالمندیاری، Journey/Referral، Provider Network، کیفیت، سامانه، AI داخلی Day-one، Dataset Lifecycle و شواهد اقتصادی/حاکمیتی است؛ Demo نرم‌افزار محسوب نمی‌شود.
- **Gate:** توسعه جغرافیایی/شبکه‌ای پس از Pilot فقط با Scale Gate مجاز است.

### Recommendation

**ACCEPT**

### Reason

جهت پایلوت از طرح مبنا می‌آید و AI Day-one / Dataset Lifecycle نیز قبلاً در D-0005 Accepted شده‌اند.

### Product Owner Decision

**PENDING**

---

## 4. D-0008 — Three-layer Service Architecture

### Proposed decision

- **حوزه:** Business / Service Model
- **تصمیم:** مدل خدمت نسیم بر سه لایه «سالمندیاری محله‌محور»، «سلامت» و «رفاه و خدمات مکمل» استوار است.
- **Role:** سالمندیار نقطه ورود و هماهنگ‌کننده Journey است و نیازهای تخصصی به لایه/Provider تخصصی ارجاع می‌شوند.
- **Boundary:** این تصمیم Service SKU، Provider Type، SLA، Pricing یا Pilot activation هر خدمت را تعیین نمی‌کند.

### Recommendation

**ACCEPT**

### Reason

سه‌لایه بودن مدل و ارجاع نیازهای تخصصی مستقیماً از Concept مبنا قابل استناد است.

### Product Owner Decision

**PENDING**

---

## 5. D-0009 — Elder-care Worker Direct Service Boundary

### Proposed decision

- **حوزه:** Business / Service Boundary
- **تصمیم:** دامنه مستقیم سالمندیار در فاز اول شامل ارتباط، پایش، تشکیل/به‌روزرسانی پرونده، ثبت و گزارش Need، هماهنگی، Referral، Follow-up و پیگیری رضایت است.
- **Rule:** خدمات تخصصی سلامت، درمان، پرستاری، توانبخشی تخصصی، سلامت روان، حقوقی و سایر خدمات نیازمند صلاحیت تخصصی، تا زمانی که Contract جداگانه‌ای خلاف آن را تصویب نکرده باشد، Direct Service سالمندیار محسوب نمی‌شوند.
- **Boundary:** Provider Type مجاز برای هر خدمت هنوز جداگانه تعیین می‌شود.

### Recommendation

**ACCEPT**

### Reason

این تصمیم از نقش Source-confirmed سالمندیار فراتر نمی‌رود و از اعطای صلاحیت تخصصی بدون Evidence جلوگیری می‌کند.

### Product Owner Decision

**PENDING**

---

## 6. D-0010 — Specialist Services Are Network-delivered

### Proposed decision

- **حوزه:** Business / Provider Model
- **تصمیم:** نسیم در فاز اول به‌عنوان اپراتور شبکه، الزاماً ارائه‌دهنده مستقیم همه خدمات تخصصی نیست.
- **Delivery:** خدمات تخصصی می‌توانند توسط Providerهای تخصصی/ظرفیت‌های شبکه ارائه شوند.
- **Nasim responsibility:** هماهنگی، Referral، Quality و Follow-up.
- **Boundary:** نوع قرارداد، Provider onboarding، SLA، تعرفه و Settlement در این تصمیم تعیین نمی‌شوند.

### Recommendation

**ACCEPT**

### Reason

این تصمیم با نقش Source-confirmed اپراتور و شرکای تخصصی همسو است.

### Product Owner Decision

**PENDING**

---

## 7. What acceptance of D-0006…D-0010 would close

اگر هر پنج Decision پذیرفته شوند:

- جامعه هدف سطح بالا برای فاز اول تثبیت می‌شود.
- ماهیت Pilot به‌عنوان عملیات واقعی تثبیت می‌شود.
- معماری سه‌لایه Service Model تثبیت می‌شود.
- مرز Direct سالمندیار تثبیت می‌شود.
- مرز Operator / Specialist Provider تثبیت می‌شود.

این Acceptance هنوز Technical Entry Gate را Pass نمی‌کند.

## 8. Blockers that remain even after acceptance

حتی در صورت پذیرش هر پنج Decision، این موارد همچنان باز می‌مانند:

1. Pilot geography
2. Pilot elder count
3. Caregiver count / ratio
4. Pilot duration
5. exact enrollment eligibility
6. exit/suspension rules
7. Pilot Sponsor/Payor detail
8. active Health Service Families
9. active Welfare/Complementary Service Families
10. Service Item definitions
11. rehabilitation duplication resolution
12. Provider Type per Service
13. Need-to-Service mapping
14. Service eligibility
15. Completion evidence
16. Home Visit classification
17. Emergency service boundary

## 9. Decision Register update rule

پس از تصمیم صریح مالک محصول:

- ACCEPT → تصمیم با Status = Accepted در `docs/DECISIONS.md` ثبت می‌شود.
- ACCEPT WITH MODIFICATION → متن اصلاح‌شده ثبت می‌شود.
- REJECT → Candidate وارد Decision Register به‌عنوان Accepted نمی‌شود؛ در Acceptance Record نتیجه ثبت می‌شود.
- DEFER → Deferral باید Scope، Owner، future Gate و Constraint داشته باشد.
- MERGE → Candidate با Decision مقصد Traceable می‌شود.

## 10. Recommended Product Owner response

برای پذیرش Recommendation فعلی، پاسخ صریح می‌تواند این باشد:

`D-0006 تا D-0010 همگی ACCEPT`

یا هر Decision جداگانه با Outcome/Modification اعلام شود.

## 11. Gate status

تا زمان پاسخ مالک محصول:

**Business → Technical: NOT READY**

و:

**Decision Acceptance Round DA-001: WAITING FOR PRODUCT OWNER**
