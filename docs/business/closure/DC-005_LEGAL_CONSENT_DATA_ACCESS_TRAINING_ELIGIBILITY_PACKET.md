# DC-005 — Legal, Consent, Data Access & Training Eligibility Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-006 + BC-007 + BC-014 + BC-022

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند.

## Candidate decisions ready for acceptance

### D-0021 — Purpose-limited data use
هر Data Class فقط برای Purpose مصوب استفاده شود. Service Delivery، Reporting، AI Runtime و AI Training Purposeهای مستقل‌اند.

### D-0022 — Operational data is not automatically training data
`Operationally Available ≠ Training Eligible`

### D-0023 — Runtime access is separate from training permission
`AI Runtime Access ≠ Training Permission`

### D-0024 — Family is not automatically an authorized representative
صرف رابطه خانوادگی، Authority خودکار برای مشاهده پرونده، Consent یا تصمیم‌گیری از طرف سالمند ایجاد نمی‌کند.

### D-0025 — Provider access is service-purpose limited
`Provider Access ≠ Full Elder Record Access`

### D-0026 — Employer supervision does not imply unrestricted individual access
نقش نظارتی کارفرما به‌تنهایی مجوز دسترسی نامحدود به پرونده فردی سالمند ایجاد نمی‌کند.

### D-0027 — Dataset automation does not automate governance
Dataset Lifecycle می‌تواند مستمر و خودکار باشد، اما Training Eligibility Rule و تغییر آن باید تحت Governance مصوب باشد.

### D-0028 — Provenance must be preserved
منشأ داده باید میان Elder، Family، Caregiver، Provider، System، AI و Human-reviewed AI قابل تفکیک و در Audit/Dataset lineage حفظ شود.

## Consent domains still requiring closure

Consent یا مبنای مجاز پردازش باید حداقل برای این Purposeها جدا بررسی شود:
- ورود به خدمت
- جمع‌آوری/نگهداری داده
- اشتراک با Provider
- AI Assistance
- AI Training
- Research/Evaluation در صورت وجود

`Consent for one purpose ≠ permission for every purpose`

## Access decisions still blocking

برای Phase/Pilot باید مرز دسترسی این Actorها بسته شود:
- سالمند
- نماینده مجاز در صورت تعریف
- سالمندیار
- Supervisor
- Provider
- کارفرما
- Operations
- Quality/Audit
- AI Runtime
- Dataset/Training Pipeline
- Admin/Security

## Training Eligibility minimum contract

Rule آینده باید حداقل این ابعاد را داشته باشد:
- Data class
- Purpose
- eligibility condition
- exclusion
- consent/legal basis
- preparation if required
- quality requirement
- provenance
- Dataset version
- governance owner

Pipeline فقط Rule مصوب را اجرا می‌کند و حق تغییر خودکار آن را ندارد.

## AI record boundary

- AI output ≠ Official Record
- AI inference ≠ observed fact
- AI suggestion ≠ human decision
- AI-generated content ≠ automatically verified training label

## Retention / withdrawal still open

منبع مدت Retention یا اثر Withdrawal را تعیین نمی‌کند. اثر آنها بر عملیات، Provider Sharing، AI Runtime، Datasetهای آینده/موجود و Model Lineage باید جداگانه تصمیم‌گیری شود.

## Product-owner / Legal decisions still blocking

1. Consent/legal-basis model per purpose
2. Authorized Representative model
3. Data Access Matrix
4. Provider data-sharing fields
5. Employer reporting boundary
6. Elder self-access/correction boundary
7. AI Runtime Data Access per Use Case
8. Training-eligible Data Classes
9. Training exclusions/preparation
10. Training Eligibility owner
11. Retention/deletion policy
12. Withdrawal effects
13. Export/sharing rules
14. Legal Review owner/gate

## Gate effect

پذیرش D-0021 تا D-0028 مرزهای Data Governance و Learning را روشن می‌کند، اما Technical Entry Gate تا بسته‌شدن Consent/Legal Basis، Data Access Matrix و Training Eligibility واقعی Phase/Pilot همچنان **NOT READY** می‌ماند.
