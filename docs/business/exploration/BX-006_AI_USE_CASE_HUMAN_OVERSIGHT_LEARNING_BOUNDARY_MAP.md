# BX-006 — AI Use-case, Human Oversight & Learning Boundary Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** D-0004 + D-0005 + D-0118 + BC-004 + BC-006 + BC-007 + DC-006 + BX-005

این سند مرز مفهومی AI داخلی نسیم را برای ادامه Business Exploration مشخص می‌کند و هیچ Candidate Decision را Accepted نمی‌کند.

## Accepted direction

- AI داخلی نسیم دستیار سالمند و سالمندیار است.
- AI از روز اول بهره‌برداری عملیاتی حضور دارد.
- Dataset Lifecycle از روز اول خودکار، مستمر و Versioned است.
- فقط داده واجد شرایط Governance می‌تواند وارد Dataset شود.
- Dataset automation به معنی Model auto-promotion نیست.

## Core boundaries

- AI Assistance ≠ Human Accountability
- AI Suggestion ≠ Human Decision
- AI Output ≠ Official Record
- AI Inference ≠ Observed Fact
- AI Runtime Access ≠ Training Permission
- Operational Data ≠ Training Eligible Data
- Training/Evaluation Success ≠ Production Promotion
- Model Version ≠ AI Policy Version

## Elder-facing candidate families

- راهنمای خدمات نسیم
- توضیح Journey و وضعیت ثبت‌شده
- یادآوری Follow-upهای ثبت‌شده
- کمک به بیان Need
- توضیح اطلاعات ثبت‌شده
- کمک در استفاده از سامانه
- هدایت به سالمندیار وقتی اقدام انسانی لازم است

این موارد Candidate هستند و Activation نهایی آنها هنوز OPEN است.

## Caregiver-facing candidate families

- خلاصه‌سازی سابقه
- آماده‌سازی Follow-up
- برجسته‌سازی تغییرات برای Review
- Draft یادداشت و گزارش
- پیشنهاد سؤال
- جست‌وجو در Service Catalog و فرآیندها
- پیشنهاد Candidate Referral Path
- یادآوری Task/Referral/Follow-up
- Flag کردن نقص یا ناسازگاری داده

Draft، Flag و Recommendation به‌تنهایی Official Record یا Human Decision نیستند.

## Human review boundary

هر خروجی AI که قرار است اثر رسمی بر پرونده، Need، Referral، Reassessment، Outcome یا سایر تصمیم‌های مهم بگذارد باید قبل از اثر رسمی وارد مسیر Human Review شود.

Conceptual pattern:

AI Output → Human Review → Accept / Reject / Edit → Official Human Action

Reviewer و Rule نهایی هنوز OPEN هستند.

## AI provenance

برای خروجی‌های واردشده به Workflow باید در آینده بتوان این موارد را ردیابی کرد:

- Use-case / AI Policy Version
- Model Version
- generation time
- relevant input/context versions
- AI output
- reviewer when applicable
- accept/reject/edit result
- final official action

AI نباید به‌عنوان Human Actor ثبت شود.

## Runtime-data boundary

برای هر AI Use Case باید جداگانه مشخص شود:

- intended user
- allowed Data Classes
- minimum necessary context
- prohibited Data Classes
- historical-context allowance
- output type
- Human Review rule
- provenance/logging rule

Approved AI Use Case به معنی دسترسی به همه داده‌های عملیاتی نیست.

## Learning boundary

Dataset path:

Operational Data → Training Eligibility → Eligible Data → Preparation/Curation → Dataset Version

Model path:

Dataset Version → Training → Evaluation → Candidate Model Version → Governance Decision → Production Model

چرخه Dataset می‌تواند خودکار باشد؛ Production Promotion مستقل می‌ماند.

## Candidate learning sources

منابع بالقوه می‌توانند شامل داده عملیاتی، Follow-up، Referral/Service evidence، Reassessment/Outcome، Satisfaction، Provider Result و Human Review روی AI باشند.

هیچ‌کدام ذاتاً Training-eligible نیستند.

Human Review Event نیز به‌تنهایی Verified Training Label محسوب نمی‌شود.

## Fail-safe concept

اگر Context کافی نباشد یا AI معتبر در دسترس نباشد، AI نباید Official Decision ایجاد کند.

Candidate safe behavior:
- اعلام insufficient context
- درخواست اطلاعات تکمیلی
- handoff به انسان
- نمایش unavailable/invalid
- خودداری از تغییر Official Record

رفتار دقیق هر Use Case هنوز OPEN است.

## Evaluation and promotion boundary

Evaluation Governance آینده باید Purpose، Dataset/Evidence Version، Metric Definition، Reviewer/Owner، Decision Criteria و Provenance را تعیین کند.

Training Success ≠ Evaluation Pass ≠ Production Promotion

Promotion و Rollback Authority هنوز OPEN هستند.

## Decision triggers

- final elder use cases: before elder-facing AI contract
- final caregiver use cases: before caregiver AI workflow
- Human Owner/Review: before consequential AI workflow
- Runtime Data Classes: before each AI use case
- Training Eligibility: before Dataset Builder
- Label Validation: before learning from operational outcomes/reviews
- Evaluation Policy: before model evaluation gate
- Promotion/Rollback Authority: before Production model lifecycle
- Fail-safe: before runtime availability contract

## Explicit non-decisions

این سند Model Family، Algorithm، Fine-tuning، RAG، Runtime Topology، Hosting، API، Prompt Format، Dataset Storage، Evaluation Threshold یا Access Matrix را تعیین نمی‌کند.

## Next artifact

**BX-007 — Provider Lifecycle, Referral Response & Service Evidence Map**

## Current stage

- Stage: Business
- AI boundary exploration: ACTIVE
- Business → Technical: NOT READY
- Code: NOT STARTED
- Codex handoff: NOT YET TRIGGERED
