# BC-004 — Internal AI Assistant

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source:** Product-owner decision D-0004
- **Depends on:** BC-001, BC-002, BC-003

> این قابلیت در طرح‌نامه اولیه «شمیم» تعریف نشده بود و به‌عنوان توسعه جدید محصول «نسیم» اضافه شده است.

## 1. Product Intent

نسیم باید یک **هوش مصنوعی داخلی** داشته باشد که در کنار دو بازیگر اصلی شبکه به‌عنوان دستیار عمل کند:

- سالمند
- سالمندیار

این AI بخشی از خود نسیم است و هدف آن کمک به استفاده بهتر از داده‌ها، تعاملات و فرآیندهای تولیدشده در شبکه است.

## 2. Learning Intent

طبق تصمیم محصول، AI باید از داده‌های تولیدشده در نسیم برای **آموزش و بهبود خودکار** استفاده کند.

این تصمیم فقط «جهت محصول» را تثبیت می‌کند؛ جزئیات زیر هنوز تصمیم نشده‌اند:

- چه داده‌هایی مجاز به ورود به Training هستند
- داده خام یا Curated Data
- ناشناس‌سازی / شبه‌ناشناس‌سازی
- Consent
- Retention
- Training cadence
- Online / Offline training
- Evaluation
- Model versioning
- Promotion / rollback
- Monitoring
- Human approval gates

## 3. Assistant Role for Elder

AI باید بتواند به‌عنوان دستیار سالمند طراحی شود.

Capabilityهای دقیق هنوز تصویب نشده‌اند. موضوعات قابل طراحی در مراحل بعدی می‌تواند شامل تعامل، راهنمایی، یادآوری، توضیح خدمات و کمک به استفاده از شبکه باشد؛ اما هیچ‌کدام تا تصمیم مستقل، قابلیت قطعی محصول محسوب نمی‌شوند.

## 4. Assistant Role for Elder-Care Worker

AI باید در کنار سالمندیار نیز به‌عنوان دستیار عمل کند.

نوع دقیق کمک، داده‌های قابل استفاده، پیشنهادها، محدودیت‌ها و سطح اتکاپذیری هنوز باید در Business Contractهای بعدی مشخص شوند.

## 5. Authority Boundary

تصمیم D-0004 «دستیار» بودن AI را تصویب می‌کند، نه جایگزینی سالمندیار یا سایر نقش‌های انسانی را.

تا زمان تصمیم صریح بعدی، موارد زیر نباید فرض شوند:

- تشخیص پزشکی مستقل
- تصمیم درمانی مستقل
- تصمیم نهایی درباره Eligibility
- تصمیم نهایی درباره Referral
- انتخاب خودکار Provider به‌عنوان تصمیم الزام‌آور
- تأیید هزینه یا پرداخت
- تغییر مستقل پرونده رسمی سالمند
- اقدام اضطراری بدون فرآیند انسانی تعریف‌شده

## 6. Internal AI Boundary

واژه «داخلی» در این مرحله یک الزام محصولی است.

تعریف فنی دقیق آن — از جمله Runtime، مدل، زیرساخت، محل استقرار، Training Engine و وابستگی یا عدم وابستگی به سرویس‌های بیرونی — باید در مرحله Technical به‌صورت مستقل تصمیم‌گیری شود و از این سند قابل استنتاج نیست.

## 7. Data Governance Required

از آنجا که داده‌های نسیم شامل اطلاعات مرتبط با سالمندان و احتمالاً داده‌های سلامت و اجتماعی خواهد بود، قبل از عملیاتی شدن Training باید حداقل این قراردادها تعیین شوند:

- Data classification
- Training eligibility
- Consent / legal basis
- De-identification
- Access control
- Dataset lineage
- Audit trail
- Data retention/deletion
- Evaluation dataset
- Model release governance

## 8. Open Decisions Required to Accept BC-004

1. Use Cases دقیق AI برای سالمند
2. Use Cases دقیق AI برای سالمندیار
3. Forbidden Actions
4. Data classes مجاز برای Training
5. Consent و Privacy model
6. Curated vs direct-production learning
7. Training pipeline
8. Evaluation policy
9. Human review / approval gates
10. Model versioning and rollback
11. Runtime architecture
12. Monitoring and incident handling
13. توضیح‌پذیری و ثبت مبنای پیشنهاد
14. رفتار Fail-safe در نبود مدل یا خطای AI

## 9. Downstream Constraints

تا پیش از Accepted شدن BC-004:

- Technical نباید نوع مدل یا الگوریتم را انتخاب‌شده فرض کند.
- Code نباید داده Production را بدون قرارداد Data Governance وارد Training کند.
- UI نباید پیشنهاد AI را به‌عنوان تصمیم قطعی انسانی/پزشکی نمایش دهد.
- AI نباید جایگزین مسئولیت سالمندیار یا Provider تخصصی فرض شود.
- هیچ Training/Promotion path بدون Versioning، Evaluation و Governance نهایی تلقی نشود.
