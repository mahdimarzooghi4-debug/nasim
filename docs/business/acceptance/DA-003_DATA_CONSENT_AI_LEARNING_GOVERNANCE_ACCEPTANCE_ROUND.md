# DA-003 — Product Owner Decision Acceptance Round: Data + Consent + AI Learning Governance

- **Status:** AWAITING PRODUCT OWNER DECISION
- **Stage:** Business — Decision Acceptance
- **Date:** 2026-10-06
- **Source basis:** DC-005 + DC-006 + D-0004 + D-0005
- **Decision range:** D-0021…D-0035
- **Purpose:** ارائه Candidate Decisionهای Data Governance، Consent/Access Boundary، Training Eligibility، AI Day-one، Human Oversight و Model Governance برای Accept / Modify / Reject / Defer، بدون Acceptance ضمنی.

> این سند Decision Register نیست. تا زمانی که مالک محصول تصمیم صریح ندهد، هیچ‌یک از D-0021 تا D-0035 Accepted محسوب نمی‌شوند و `docs/DECISIONS.md` تغییر نمی‌کند.

## 1. Review Rule

برای هر Candidate یکی از Outcomeهای زیر لازم است:

- **ACCEPT**
- **ACCEPT WITH MODIFICATION**
- **REJECT**
- **DEFER FOR CURRENT PILOT**
- **MERGE WITH ANOTHER DECISION**

Recommendation فقط پیشنهاد است.

---

## 2. D-0021 — Purpose-limited Data Use

### Proposed decision

هر Data Class فقط برای Purpose مصوب استفاده می‌شود. حداقل این Purposeها مستقل‌اند:

- Service Delivery
- Reporting
- AI Runtime
- AI Training

Consent/Permission یک Purpose به‌تنهایی مجوز Purpose دیگر نیست.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 3. D-0022 — Operational Data Is Not Automatically Training Data

### Proposed decision

وجود داده در عملیات Production به‌تنهایی مجوز ورود آن به Learning/Training را ایجاد نمی‌کند.

`Operationally Available ≠ Training Eligible`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 4. D-0023 — Runtime Access Is Separate from Training Permission

### Proposed decision

مجاز بودن AI برای استفاده از داده در Runtime به معنی مجاز بودن همان داده برای Training نیست.

`AI Runtime Access ≠ Training Permission`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 5. D-0024 — Family Is Not Automatically an Authorized Representative

### Proposed decision

صرف رابطه خانوادگی، Authority خودکار برای مشاهده پرونده، Consent یا تصمیم‌گیری از طرف سالمند ایجاد نمی‌کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 6. D-0025 — Provider Access Is Purpose-limited

### Proposed decision

Provider فقط به داده‌ای دسترسی دارد که برای Purpose خدمت مصوب لازم است.

`Provider Access ≠ Full Elder Record Access`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 7. D-0026 — Employer Supervision Does Not Mean Full Individual Access

### Proposed decision

نقش نظارتی کارفرما به‌تنهایی مجوز دسترسی نامحدود به پرونده فردی سالمند ایجاد نمی‌کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 8. D-0027 — Dataset Automation Does Not Automate Governance

### Proposed decision

Dataset Lifecycle می‌تواند طبق D-0005 مستمر و خودکار باشد، اما Training Eligibility Rule، Exclusion Rule و تغییر آنها باید تحت Governance مصوب باقی بمانند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 9. D-0028 — Provenance Must Be Preserved

### Proposed decision

منشأ داده باید میان Elder، Family/Representative، Caregiver، Provider، System، AI و Human-reviewed AI قابل تفکیک باشد و در Audit/Dataset Lineage حفظ شود.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 10. D-0029 — Phase-1 Elder AI Use Cases

### Proposed decision

Use Caseهای فاز اول AI برای سالمند:

- راهنمایی درباره خدمات نسیم
- توضیح Journey و وضعیت Referral/Service
- یادآوری پیگیری‌ها و کارهای ثبت‌شده
- کمک به بیان Need به زبان ساده
- توضیح اطلاعات ثبت‌شده به زبان قابل فهم
- کمک در تعامل با سامانه
- هدایت سالمند به سالمندیار در موارد نیازمند اقدام انسانی

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 11. D-0030 — Phase-1 Caregiver AI Use Cases

### Proposed decision

Use Caseهای فاز اول AI برای سالمندیار:

- خلاصه‌سازی سابقه و تعاملات
- آماده‌سازی Follow-upهای روزانه
- برجسته‌سازی تغییرات برای بررسی انسانی
- Draft گزارش/یادداشت
- پیشنهاد سؤال تکمیلی
- جست‌وجو در Service Catalog و فرآیندها
- پیشنهاد Candidate Referral Path برای Review
- Reminder برای Task/Referral/Follow-up باز
- Flag کردن ناسازگاری یا نقص داده

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 12. D-0031 — AI Forbidden Actions

### Proposed decision

AI نباید به‌صورت نهایی و مستقل:

- تشخیص پزشکی ثبت کند
- درمان تجویز کند
- Eligibility نهایی تعیین کند
- Referral نهایی کند
- Provider را الزام‌آور انتخاب کند
- هزینه/پرداخت را تصویب کند
- Official Record را تغییر دهد
- Incident/Emergency را نهایی کند
- Case/Need را ببندد
- Risk Acceptance یا Scale Gate را تصویب کند

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 13. D-0032 — Human Review for Consequential AI Outputs

### Proposed decision

هر خروجی AI که بتواند بر Official Record، Service Path، Referral، Need/Outcome، Incident یا Financial Action اثر رسمی بگذارد باید مسیر Human Review با امکان Accept / Reject / Edit داشته باشد.

`AI Output ≠ Official Record`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 14. D-0033 — Production Model Promotion Is Separately Governed

### Proposed decision

Training Success یا Evaluation Pass به‌تنهایی اجازه جایگزینی Model فعال Production را ایجاد نمی‌کند.

`Training/Evaluation Success ≠ Production Promotion`

Model Promotion باید Decision حاکمیتی مستقل و قابل Audit باشد.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 15. D-0034 — AI Fail-safe and Rollback Principle

### Proposed decision

در نبود Model معتبر، Runtime failure یا نبود داده کافی:

- AI نباید Decision رسمی جعل کند.
- Human workflow باید تا حد ممکن مستقل از AI ادامه‌پذیر باشد.
- AI unavailable/invalid باید قابل مشاهده باشد.
- Model rollback باید از نظر طراحی ممکن باشد.
- Authority و Trigger دقیق Rollback جداگانه تعیین می‌شوند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 16. D-0035 — AI Provenance and Transparency

### Proposed decision

برای AI Outputهای وارد Workflow باید حداقل قابل ردیابی باشد:

- AI involvement
- model/version
- generation time
- relevant input/context version
- human reviewer where required
- accepted/rejected/edited state
- final official action

AI نباید خود را Human Actor نشان دهد.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 17. What acceptance of D-0021…D-0035 would close

در صورت پذیرش این پانزده Candidate:

- Purposeهای Operational/Reporting/Runtime/Training از هم جدا می‌شوند.
- Production Data از Training Eligibility جدا می‌شود.
- Runtime Permission از Training Permission جدا می‌شود.
- Family/Provider/Employer access boundaries سطح بالا تثبیت می‌شوند.
- Data Provenance الزام می‌شود.
- Use Caseهای Day-one AI برای سالمند و سالمندیار تثبیت می‌شوند.
- Forbidden Actions AI تثبیت می‌شوند.
- Human Review برای خروجی‌های consequential تثبیت می‌شود.
- Auto-Promotion مدل ممنوع می‌ماند.
- Fail-safe/Rollback principle تثبیت می‌شود.
- AI Provenance/Transparency الزام می‌شود.

## 18. Blockers that remain even after acceptance

1. Consent/legal-basis model per Purpose
2. Authorized Representative workflow
3. final Data Access Matrix
4. Provider data-sharing fields
5. Employer reporting boundary
6. elder self-access/correction rights
7. AI Runtime Data Access per Use Case
8. Training-eligible Data Classes
9. Training exclusions/preparation rules
10. Training Eligibility owner
11. Retention/deletion policy
12. Withdrawal effects
13. Export/sharing policy
14. Legal Review owner/gate
15. Human Owner per AI Use Case
16. AI Governance owner/body
17. exact Human Review rule per Use Case
18. Evaluation Policy
19. Evaluation evidence
20. Model Promotion authority
21. Model Rollback authority
22. AI monitoring metrics
23. AI incident handling
24. uncertainty/escalation behavior
25. exact AI fail-safe behavior
26. retention of AI interactions

## 19. Technical decisions intentionally not decided here

این Round هیچ‌کدام از موارد زیر را انتخاب نمی‌کند:

- model family/type
- LLM vs non-LLM
- training algorithm
- fine-tuning method
- RAG/vector database
- runtime topology
- hosting
- model-serving technology
- training orchestration
- evaluation implementation

اینها پس از Business Gate و در Technical قابل تصمیم‌اند، مگر Product Decision آینده خلاف آن را تعیین کند.

## 20. Decision Register update rule

پس از تصمیم صریح مالک محصول:

- ACCEPT → در `docs/DECISIONS.md` ثبت می‌شود.
- ACCEPT WITH MODIFICATION → متن اصلاح‌شده ثبت می‌شود.
- REJECT → Accepted Decision ساخته نمی‌شود؛ نتیجه Review ثبت می‌شود.
- DEFER → Scope، Owner، Future Gate و Constraint لازم است.
- MERGE → ارتباط Candidate با Decision مقصد Traceable می‌شود.

## 21. Current dependency note

- DA-001 برای D-0006…D-0010 همچنان **PENDING** است.
- DA-002 برای D-0011…D-0020 همچنان **PENDING** است.
- ایجاد DA-003 به معنی Acceptance ضمنی هیچ Round قبلی نیست.

## 22. Recommended Product Owner response

برای پذیرش Recommendation فعلی:

`D-0021 تا D-0035 همگی ACCEPT`

یا هر Decision جداگانه با Outcome/Modification اعلام شود.

## 23. Gate status

تا زمان تصمیم صریح مالک محصول:

**Business → Technical: NOT READY**

و:

**Decision Acceptance Round DA-003: WAITING FOR PRODUCT OWNER**
