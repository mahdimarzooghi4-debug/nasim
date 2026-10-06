# DA-004 — Product Owner Decision Acceptance Round: Provider + Quality + Pilot/Scale Governance

- **Status:** AWAITING PRODUCT OWNER DECISION
- **Stage:** Business — Decision Acceptance
- **Date:** 2026-10-06
- **Source basis:** DC-007 + DC-008
- **Decision range:** D-0036…D-0050
- **Purpose:** ارائه Candidate Decisionهای Provider Governance، Quality/KPI و Pilot/Scale Gate برای Accept / Modify / Reject / Defer، بدون Acceptance ضمنی.

> این سند Decision Register نیست. تا زمانی که مالک محصول تصمیم صریح ندهد، هیچ‌یک از D-0036 تا D-0050 Accepted محسوب نمی‌شوند و `docs/DECISIONS.md` تغییر نمی‌کند.

## 1. Review Rule

برای هر Candidate یکی از Outcomeهای زیر لازم است:

- **ACCEPT**
- **ACCEPT WITH MODIFICATION**
- **REJECT**
- **DEFER FOR CURRENT PILOT**
- **MERGE WITH ANOTHER DECISION**

Recommendation فقط پیشنهاد است.

---

## 2. D-0036 — Provider Is a Distinct Specialist Role

### Proposed decision

Provider تخصصی Actor مستقل از سالمندیار و اپراتور نسیم است و فقط در دامنه Service/Contract مصوب خدمت تخصصی ارائه می‌کند.

Provider به‌صرف عضویت در شبکه، Full Case Authority یا Full Elder Record Access ندارد.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 3. D-0037 — Provider Requires Explicit Activation

### Proposed decision

ثبت Provider در Registry به‌تنهایی به معنی مجاز بودن ارائه خدمت نیست؛ Provider باید قبل از استفاده عملیاتی طبق Rule مصوب بررسی و فعال شود.

`Registry Entry ≠ Operational Activation`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 4. D-0038 — Provider Eligibility Does Not Equal Selection

### Proposed decision

واجد شرایط بودن Provider برای یک Service، به‌تنهایی Provider Selection نهایی ایجاد نمی‌کند.

`Provider Eligibility ≠ Provider Selection`

Selection Rule و نقش سالمند، سالمندیار، Supervisor یا AI جداگانه تصویب می‌شوند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 5. D-0039 — Provider Referral Response Must Be Explicit and Auditable

### Proposed decision

اگر Referral به Provider ارسال می‌شود، پاسخ Provider و وضعیت پذیرش/عدم پذیرش باید به‌صورت قابل ردیابی و Audit ثبت شود.

State names، SLA و rejection taxonomy هنوز جداگانه تعیین می‌شوند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 6. D-0040 — Provider Result Is Not Final Elder Outcome

### Proposed decision

Provider می‌تواند Service Result یا Completion Evidence ثبت کند، اما این داده به‌تنهایی Outcome نهایی سالمند یا Need Resolution را تعیین نمی‌کند.

`Provider Result ≠ Final Elder Outcome`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 7. D-0041 — Provider Failure Must Not Silently Close Referral

### Proposed decision

عدم پاسخ، رد، عدم ظرفیت یا Service Failure از Provider نباید Referral را به‌طور بی‌صدا موفق/بسته تلقی کند؛ وضعیت باید قابل مشاهده و وارد مسیر مصوب بعدی شود.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 8. D-0042 — Provider Ranking Is Not a Default Decision Mechanism

### Proposed decision

تا زمان تصویب Rule جداگانه، Ranking یا Score Provider نباید به‌صورت خودکار Provider Selection، Suspension یا Contract Decision ایجاد کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 9. D-0043 — Evaluation Must Remain Multi-dimensional

### Proposed decision

ارزیابی نسیم باید حداقل چهار سطح زیر را پوشش دهد:

- Operational
- Managerial
- Economic
- Social

Success نباید صرفاً با Activity Count یا Coverage سنجیده شود.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 10. D-0044 — KPI Framework Uses Four Core Families

### Proposed decision

KPI Framework نسیم حداقل بر چهار خانواده زیر بنا می‌شود:

- کیفیت خدمات
- رضایت سالمندان و خانواده‌ها
- توسعه سرمایه انسانی
- پایداری اقتصادی و توسعه بازار

KPI Definition، Formula، Target و Threshold هر خانواده جداگانه تعیین می‌شود.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 11. D-0045 — Coverage Alone Does Not Justify Scale

### Proposed decision

گسترش شبکه فقط با افزایش Coverage توجیه نمی‌شود و باید Evidence کیفیت، رضایت ذی‌نفعان و آمادگی عملیاتی نیز وجود داشته باشد.

`Coverage Growth ≠ Scale Readiness`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 12. D-0046 — Pilot Success Is Evidence-based and Multi-domain

### Proposed decision

Success پایلوت باید بر Evidence چندبعدی در این حوزه‌ها استوار باشد:

- operations
- quality
- satisfaction
- workforce
- provider
- technology
- data
- economics
- governance
- risk/incidents
- AI
- Dataset Lifecycle

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 13. D-0047 — AI and Dataset Lifecycle Are Part of Pilot Readiness

### Proposed decision

چون AI و Dataset Lifecycle از روز اول جزء محصول‌اند، Pilot Readiness باید Use Caseهای مصوب AI، Human Review، AI quality/incidents، Dataset versioning و lineage را نیز ارزیابی کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 14. D-0048 — KPI Definitions Are Versioned Business Rules

### Proposed decision

KPI Definitionها باید Versioned و قابل Audit باشند و تغییر Formula، Scope یا Target نباید تاریخچه را بی‌صدا بازنویسی کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 15. D-0049 — Scale Gate Is a Human Governance Decision

### Proposed decision

Scale Gate یک تصمیم حاکمیتی انسانی است. Dashboard، AI یا Rule Engine می‌تواند Evidence و Analysis ارائه کند، اما GO / CONDITIONAL GO / NO-GO را به‌صورت مستقل نهایی نمی‌کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 16. D-0050 — Decision Support Is Not Decision Authority

### Proposed decision

Reporting، Dashboard و AI Management Analysis برای Decision Support هستند و خودشان Decision Right ایجاد نمی‌کنند.

`Reporting / AI Analysis ≠ Approved Decision`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 17. What acceptance of D-0036…D-0050 would close

در صورت پذیرش این پانزده Candidate:

- Provider از Caregiver/Operator جدا تثبیت می‌شود.
- Registry از Activation جدا می‌شود.
- Eligibility از Selection جدا می‌شود.
- Provider response و failure باید auditable باشند.
- Provider Result از Elder Outcome جدا می‌شود.
- Ranking/Score از Decision Authority جدا می‌شود.
- ارزیابی چندبعدی و چهار خانواده KPI تثبیت می‌شوند.
- Coverage به‌تنهایی مجوز Scale نمی‌دهد.
- Pilot باید Evidence چنددامنه تولید کند.
- AI/Dataset lifecycle داخل Pilot Readiness می‌مانند.
- KPIها Versioned می‌شوند.
- Scale Gate تصمیم انسانی می‌ماند.
- Reporting/AI analysis از Decision Right جدا می‌شوند.

## 18. Blockers that remain even after acceptance

### Provider
1. Provider types for Pilot
2. onboarding/qualification minimum
3. activation authority
4. Provider Registry required fields
5. Service-to-Provider mapping
6. Referral acceptance/rejection rules
7. Provider Selection rule
8. Elder choice rule
9. Capacity model
10. Completion Evidence
11. Provider quality standards
12. Provider KPI framework
13. complaint/incident handling
14. suspension/termination authority
15. re-routing/fallback
16. provider data-sharing fields
17. financial/settlement model
18. Pilot provider integrations
19. exact AI role in provider recommendation

### Quality / Pilot / Scale
20. final Pilot KPI catalog
21. Business definition/source per KPI
22. KPI owner/reviewer
23. Target/Threshold where required
24. Satisfaction method
25. Quality Audit process
26. Caregiver evaluation model
27. Provider quality model
28. AI quality metrics/thresholds
29. Dataset lifecycle readiness criteria
30. Pilot Success criteria
31. GO / CONDITIONAL GO / NO-GO rules
32. Scale Gate owner
33. remediation/conditional-go process
34. observation period
35. Evidence Package format
36. correction/restatement policy

## 19. Decision Register update rule

پس از تصمیم صریح مالک محصول:

- ACCEPT → در `docs/DECISIONS.md` ثبت می‌شود.
- ACCEPT WITH MODIFICATION → متن اصلاح‌شده ثبت می‌شود.
- REJECT → Accepted Decision ساخته نمی‌شود؛ نتیجه Review ثبت می‌شود.
- DEFER → Scope، Owner، Future Gate و Constraint لازم است.
- MERGE → ارتباط Candidate با Decision مقصد Traceable می‌شود.

## 20. Current dependency note

- DA-001 برای D-0006…D-0010 همچنان **PENDING** است.
- DA-002 برای D-0011…D-0020 همچنان **PENDING** است.
- DA-003 برای D-0021…D-0035 همچنان **PENDING** است.
- ایجاد DA-004 به معنی Acceptance ضمنی هیچ Round قبلی نیست.

## 21. Recommended Product Owner response

برای پذیرش Recommendation فعلی:

`D-0036 تا D-0050 همگی ACCEPT`

یا هر Decision جداگانه با Outcome/Modification اعلام شود.

## 22. Gate status

تا زمان تصمیم صریح مالک محصول:

**Business → Technical: NOT READY**

و:

**Decision Acceptance Round DA-004: WAITING FOR PRODUCT OWNER**
