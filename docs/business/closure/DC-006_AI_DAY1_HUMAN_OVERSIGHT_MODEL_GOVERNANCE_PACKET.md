# DC-006 — AI Day-one Use Cases, Human Oversight & Model Governance Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** D-0004 + D-0005 + BC-004 + BC-006 + BC-013

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند. هدف، تبدیل جهت مصوب AI داخلی نسیم به مرزهای قابل تصمیم برای فاز اول است، بدون انتخاب مدل، الگوریتم، Runtime یا معماری Training.

> **Subsequent Decision Register reconciliation (2026-10-08):** Candidate decisions **D-0031…D-0035** are now individually **ACCEPTED** as bounded safety/Human Review/model governance principles in `docs/DECISIONS.md` on Draft PR #10. A **narrow, information-only first use case for both elders and caregivers** is selected separately as **D-0135**. This does **not** accept every candidate ability under D-0029/D-0030, nor does it establish published service content, real user authorization, Human Owner, Training Eligibility, precise fail-safe or AI model/technical configuration. The original candidate sections below preserve their historical proposal text; binding decisions live in the Decision Register. Hosted Stage remains UNAVAILABLE under D-0130.

## 1. Existing accepted direction

طبق D-0004 و D-0005:
- AI داخلی نسیم دستیار سالمند و سالمندیار است.
- AI از روز اول بهره‌برداری عملیاتی در محصول حضور دارد.
- Dataset Lifecycle از روز اول مستمر، خودکار و Versioned است.
- خودکار بودن Dataset به معنی Auto-Promotion مدل نیست.

## 2. Candidate D-0029 — Phase-1 elder AI use cases

Use Caseهای پیشنهادی فاز اول برای سالمند:
- راهنمایی درباره خدمات نسیم
- توضیح Journey و وضعیت Referral/Service
- یادآوری پیگیری‌ها و کارهای ثبت‌شده
- کمک به بیان Need به زبان ساده
- توضیح اطلاعات ثبت‌شده به زبان قابل فهم
- کمک در تعامل با سامانه
- هدایت به سالمندیار وقتی اقدام انسانی لازم است

**Assessment:** aligned with BC-006; recommended for product-owner acceptance.

## 3. Candidate D-0030 — Phase-1 caregiver AI use cases

Use Caseهای پیشنهادی فاز اول برای سالمندیار:
- خلاصه‌سازی سابقه و تعاملات
- آماده‌سازی Follow-upهای روزانه
- برجسته‌سازی تغییرات برای بررسی انسانی
- Draft گزارش/یادداشت
- پیشنهاد سؤال تکمیلی
- جست‌وجو در Service Catalog و فرآیندها
- پیشنهاد Candidate Referral Path برای Review
- یادآوری Task/Referral/Follow-up باز
- Flag کردن ناسازگاری یا نقص داده

**Assessment:** aligned with BC-006; recommended for product-owner acceptance.

## 4. Candidate D-0031 — Forbidden actions

تا Decision مستقل، AI نباید به‌صورت نهایی و مستقل:
- تشخیص پزشکی ثبت کند
- درمان تجویز کند
- Eligibility را تعیین کند
- Referral را نهایی کند
- Provider را الزام‌آور انتخاب کند
- هزینه/پرداخت را تصویب کند
- پرونده رسمی را تغییر دهد
- Incident/Emergency را نهایی کند
- Case/Need را ببندد
- Risk Acceptance یا Scale Gate را تصویب کند

**Assessment:** directly aligned with BC-004/BC-006; recommended for acceptance.

## 5. Candidate D-0032 — Human review for consequential outputs

هر خروجی AI که بتواند روی:
- Official Record
- Service Path
- Referral
- Need/Outcome
- Incident
- Financial action

اثر رسمی بگذارد، باید مسیر Human Review با امکان Accept / Reject / Edit داشته باشد.

`AI Output ≠ Official Record`

**Assessment:** recommended for acceptance.

## 6. Candidate D-0033 — Production model promotion is separately governed

Training success یا Evaluation pass به‌تنهایی اجازه جایگزینی Model فعال در Production نمی‌دهد.

`Training/Evaluation Success ≠ Production Promotion`

Promotion باید Decision حاکمیتی جداگانه و قابل Audit باشد.

**Assessment:** aligned with D-0005 and BC-013; recommended for acceptance.

## 7. Candidate D-0034 — Fail-safe and rollback principle

در نبود Model معتبر، خطای Runtime یا نبود داده کافی:
- AI نباید Decision رسمی جعل کند.
- Workflow انسانی باید تا حد ممکن مستقل از AI قابل ادامه باشد.
- وضعیت AI unavailable/invalid باید قابل مشاهده باشد.
- Rollback Model باید در طراحی آینده ممکن باشد، اما Authority و Trigger آن هنوز باز است.

**Assessment:** recommended for acceptance.

## 8. Candidate D-0035 — AI provenance and transparency

برای AI Outputهای واردشده به Workflow باید قابل ردیابی باشد:
- AI involvement
- model/version
- generation time
- relevant input/context version
- human reviewer
- accepted/rejected/edited result
- final official action

AI نباید خود را Human Actor نشان دهد.

**Assessment:** recommended for acceptance.

## 9. Model vs policy separation

`Model Version ≠ AI Policy Version`

تغییر Model نباید خودکار:
- Forbidden Actions
- Data Access
- Human Review
- Service Authority
را تغییر دهد.

این مرز با BC-024 همسو است.

## 10. Dataset lifecycle vs model lifecycle

دو چرخه باید جدا بمانند:

`Eligible Operational Data → Versioned Dataset`

و

`Dataset → Training → Evaluation → Promotion Decision → Production Model`

چرخه اول طبق D-0005 خودکار است؛ Promotion در چرخه دوم مستقل و Governance-controlled باقی می‌ماند.

## 11. AI governance decisions still blocking

1. Human Owner هر Use Case
2. AI Governance owner/body
3. exact Review/Approval rule per Use Case
4. AI Runtime Data Access
5. Training Eligibility واقعی
6. Evaluation policy
7. Evaluation evidence requirements
8. Model Promotion authority
9. Rollback authority
10. Model monitoring metrics
11. AI incident severity/handling
12. uncertainty/escalation behavior
13. exact fail-safe behavior
14. retention of AI interactions

## 12. Technical decisions intentionally deferred

این Packet انتخاب نمی‌کند:
- Model family/type
- LLM or non-LLM
- Training algorithm
- Fine-tuning method
- RAG/vector database
- Runtime topology
- hosting
- model serving technology
- training orchestration
- evaluation implementation

این موارد بعد از Business Gate در Technical تصمیم می‌شوند.

## 13. Gate effect

پذیرش D-0029 تا D-0035 بخش عمده مرز AI Day-one را روشن می‌کند، اما Technical Entry Gate تا تعیین Human Owners، Training Eligibility، Evaluation Policy و Promotion/Rollback Authority همچنان **NOT READY** می‌ماند.

## 14. Next closure packet

**DC-007 — Provider Model, Onboarding, Referral Acceptance & Service Evidence Decision Packet**
