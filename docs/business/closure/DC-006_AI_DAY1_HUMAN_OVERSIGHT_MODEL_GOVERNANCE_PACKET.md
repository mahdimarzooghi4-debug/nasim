# DC-006 — AI Day-one Use Cases, Human Oversight & Model Governance Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** D-0004 + D-0005 + BC-004 + BC-006 + BC-013

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند. هدف، تبدیل جهت مصوب AI داخلی نسیم به مرزهای قابل تصمیم برای فاز اول است، بدون انتخاب مدل، الگوریتم، Runtime یا معماری Training.

> **Current decision reconciliation (2026-10-08; unmerged Draft PR #10):** D-0031…D-0035 safety/Human Review/model-governance principles are **ACCEPTED**. The first **information-only** elder/caregiver use case D-0135; official source classes/import/publish/classification responsibilities D-0136…D-0141; four-part safe source failure D-0142; and bounded, conditional human follow-up/organizational direction D-0143…D-0146 are accepted **only within their stated Business limits**. **D-0147 explicitly DEFERS only final model/version selection** pending an evidence-based benchmark; it does **not** delay mandatory real Day-one AI or governed automatic Dataset production under D-0004/D-0005. Actual published documents, legal/identity grants, support appointments, Training Eligibility, model evaluation/deployment evidence remain **OPEN**. The original D-0029/D-0030 and D-0031…D-0035 candidate sections below are historical proposal text, not fresh unapproved demands or the binding register. For operative status, use `docs/DECISIONS.md`, [DC-017](DC-017_AI_DAY_ONE_BOUNDED_USE_CASE_DECISION_PACKET.md), [DC-018](DC-018_AI_DAY_ONE_INTEGRATED_PRE_TECHNICAL_READINESS.md), and [DC-019](DC-019_AI_SOURCE_USE_AND_TRAINING_ELIGIBILITY_EVIDENCE_MATRIX.md). Hosted Stage remains UNAVAILABLE under D-0130.

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

## 11. Historical decision-question inventory (current statuses reconciled below)

> The original questions below are retained as a historical inventory. Do **not** interpret every line as wholly OPEN: D-0142 now settles the bounded informational-source safe-response policy, and D-0143…D-0146 partly settle elder follow-up and conditional support functions. Actual human contacts, lawful access and incident/urgency handling are still OPEN.

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

## 12. Historical technical non-selections — current status differentiated

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

این موارد در این سند انتخاب نشده‌اند. **فقط انتخاب نهایی مدل/نسخه** تحت D-0147 به گیت ارزیابی/Technical Selection آینده صریحاً **DEFERRED** شده است؛ الگوریتم، Runtime، استقرار، ظرفیت و سایر انتخاب‌های فنی صرفاً **NOT SELECTED / OPEN** هستند، نه اینکه همه رسماً Deferred شده باشند. Day-one AI و ساخت خودکار Dataset نسخه‌دارِ داده مجاز طبق D-0004/D-0005 پابرجا هستند و هیچ مدل فرضی/Placeholder آن را محقق نمی‌کند.

## 13. Gate effect

**CURRENT GATE: NOT READY FOR AI TECHNICAL ENTRY.** D-0029/D-0030 شامل فهرست قابلیت‌های نامزد هستند، **نه Use Caseهای پذیرفته‌شده همگانی**. فقط D-0135 و حدود قبول‌شده D-0031…D-0035، D-0136…D-0146 برقرارند؛ مدل نهایی طبق D-0147 به‌طور محدود Deferred است. نبود مدارک واقعی نشر محتوا، مجوز و Purpose داده، Owner/Channel انسانی، Training Eligibility، Evaluation و Promotion Authority مانع گیت AI است. CI موفق، اسناد آمادگی، یا انتخاب نام مدل هیچ‌کدام مجوز Technical/Code/Stage نیست.

## 14. Successor packages and independence

Historical follow-on **DC-007 — Provider Model/Onboarding/Referral** is independent of AI and does not close its authority or data-use questions.

The current AI Business trail is [DC-017](DC-017_AI_DAY_ONE_BOUNDED_USE_CASE_DECISION_PACKET.md) → [DC-018](DC-018_AI_DAY_ONE_INTEGRATED_PRE_TECHNICAL_READINESS.md) → [DC-019](DC-019_AI_SOURCE_USE_AND_TRAINING_ELIGIBILITY_EVIDENCE_MATRIX.md). These are preparation/evidence documents, **not** an approved Technical Contract, Dataset Policy, user access grant or runnable AI. Avoid another repetitive decision micro-question; request actual documents, legal/purpose evidence and authorization only when the affected gate needs them.
