# BR-003 — Pilot Scope + Services Decision Batch

- **Status:** OPEN — PARKED UNTIL CONTEXT REQUIRES DECISION
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** BR-002 P1…P6 + DC-001 + DC-002
- **Scope:** P1…P6 only
- **Purpose:** بستن نخستین Batch از Blockerهای واقعی پایلوت، بدون اختراع Geography، Count، Duration، Eligibility یا Service Activation.

> این سند هیچ Candidate Decision از D-0006…D-0010 را Accepted نمی‌کند و هیچ مقدار باز را از روی حدس پر نمی‌کند. طبق D-0118، P1…P6 تا زمانی که Context واقعی تصمیم یا Gate مربوطه به آنها نیاز نداشته باشد OPEN می‌مانند و پاسخ فوری مالک محصول الزامی نیست.

## 1. Source-supported facts already available

این موارد از Concept/Closure قبلی قابل استنادند و نیاز به Input جدید ندارند:

- مدل نسیم محله‌محور است و قابلیت توسعه به روستاها را دارد.
- جامعه هدف اولیه در Concept، سالمندان تحت حمایت کمیته امداد امام خمینی (ره) است.
- Pilot باید قبل از توسعه شبکه، عملیات واقعی را اعتبارسنجی کند.
- معماری خدمت سه‌لایه است: سالمندیاری محله‌محور، سلامت، رفاه و خدمات مکمل.
- سالمندیار نقطه ورود، پایش، ثبت Need، هماهنگی، Referral و Follow-up است.
- خدمات تخصصی به‌صورت پیش‌فرض Direct Service سالمندیار نیستند.
- Service Family مندرج در Concept الزاماً Active Pilot Service نیست.
- AI Day-one و Automatic Versioned Dataset Lifecycle طبق D-0004/D-0005 بخشی از Pilot target product هستند.

## 2. P1 — Pilot Geography

### Source boundary
Concept هیچ Province/City/Neighborhood مشخصی تعیین نمی‌کند.

### Product Owner input required
- Province:
- City/County:
- District/Neighborhood/Village:
- Urban / Rural / Mixed:
- Boundary notes:

### Decision rule
تا زمان تعیین این موارد، Geography باید **UNRESOLVED** بماند و Technical نباید Location Scope فرض کند.

### Status
**BLOCKING**

---

## 3. P2 — Pilot Population Size

### Source boundary
Concept هیچ عددی برای تعداد سالمندان، سالمندیاران، Supervisorها یا Providerها ارائه نمی‌کند.

### Product Owner input required
- Elder count:
- Caregiver count:
- Supervisor count, if applicable:
- Minimum active Provider count:
- Elder-to-caregiver ratio, if fixed:

### Decision rule
هیچ عددی نباید از Benchmark عمومی یا حدس اجرایی وارد Business Baseline شود.

### Status
**BLOCKING**

---

## 4. P3 — Pilot Duration

### Source boundary
Concept Pilot را مرحله پیش از توسعه شبکه می‌داند، اما مدت آن را تعیین نمی‌کند.

### Product Owner input required
- Start condition/date:
- Duration:
- Review checkpoints:
- Extension authority:
- Maximum extension, if any:

### Decision rule
اگر Duration هنوز نباید بسته شود، باید صریحاً **DEFER** شود و Gate آینده/Owner مشخص باشد؛ Unknown قابل قبول نیست.

### Status
**BLOCKING**

---

## 5. P4 — Enrollment Eligibility

### Source-supported minimum
- تعلق به جامعه هدف فاز اول، یعنی سالمند تحت حمایت کارفرمای اولیه.

### Product Owner input required
- Age definition:
- support-status requirement:
- residence requirement:
- minimum Need requirement, if any:
- consent/authorization prerequisite:
- prioritization rule:
- exclusion rule:
- waiting-list rule:

### Important separation
دو مفهوم باید جدا بمانند:
- **Population Eligibility**
- **Pilot Enrollment Eligibility**

### Status
**BLOCKING**

---

## 6. P5 — Exit / Suspension

### Source boundary
Concept هیچ Exit/Suspension lifecycle فردی تعریف نمی‌کند.

### Product Owner input required
برای هر مورد یکی از POLICY / DEFER / NOT APPLICABLE:
- voluntary withdrawal
- support-status change
- geography change
- unreachable elder
- legal/consent change
- safety restriction
- duplicate enrollment
- death
- transfer to another program

Also:
- final closure authority:

### Decision rule
Technical نباید از Workflow یا Statusها Exit Rule استنتاج کند.

### Status
**BLOCKING**

---

## 7. P6 — Active Phase-1 Service Catalog

### Source-supported Health families
- health assessment
- medical
- nursing
- chronic-care
- rehabilitation/specialist
- mental health

### Source-supported Welfare / Complementary families
- welfare
- cultural/social
- support
- legal
- rehabilitation
- other approved partner services

### Product Owner activation input

برای هر مورد فقط یکی از این‌ها:
- **ACTIVE**
- **DEFER FOR PILOT**
- **NOT APPLICABLE**

#### Health
- health assessment:
- medical:
- nursing:
- chronic-care:
- rehabilitation/specialist:
- mental health:

#### Welfare / Complementary
- welfare:
- cultural/social:
- support:
- legal:
- rehabilitation:
- other approved partner services:

### Additional decisions required

#### Rehabilitation duplication
Choose one:
- one shared Service Family
- two different Domains with different definitions
- only one active in Pilot
- another explicit rule

#### Home Visit
Choose one:
- Service Item
- Mode of Operation
- DEFER

#### Out-of-catalog handling
Choose one:
- reject/no service
- manual review
- temporary exception with approval
- another explicit policy

### Status
**BLOCKING**

---

## 8. What this Batch will produce after Product Owner input

پس از پاسخ صریح P1…P6، فقط همان پاسخ‌ها به تصمیم‌های Business جدید تبدیل می‌شوند و در صورت تأیید:

- Pilot Geography Baseline
- Pilot Capacity Baseline
- Pilot Duration Baseline
- Enrollment Eligibility Baseline
- Exit/Suspension Baseline
- Active Phase-1 Service Catalog Baseline

ساخته خواهند شد.

هیچ پاسخ دیگری از P7…P23 از این Batch استنتاج نمی‌شود.

## 9. Acceptance dependency

D-0006…D-0010 همچنان در DA-001 **PENDING** هستند.

پاسخ P1…P6:
- DA-001 را خودکار Accept نمی‌کند.
- Accepted Candidateهای DA-001 را جایگزین نمی‌کند.
- فقط Blockerهای مقداری/اجرایی Pilot را می‌بندد.

## 10. Response format when the decision context arrives

مالک محصول می‌تواند فقط این قالب کوتاه را پر کند:

```
P1:
Province =
City/County =
District/Neighborhood/Village =
Urban/Rural/Mixed =
Boundary notes =

P2:
Elder count =
Caregiver count =
Supervisor count =
Minimum active Provider count =
Ratio =

P3:
Start =
Duration =
Checkpoints =
Extension authority =
Max extension =

P4:
Age =
Support status =
Residence =
Minimum Need =
Consent prerequisite =
Prioritization =
Exclusions =
Waiting list =

P5:
Withdrawal =
Support-status change =
Geography change =
Unreachable =
Consent/legal change =
Safety restriction =
Duplicate =
Death =
Transfer =
Closure authority =

P6:
Health assessment =
Medical =
Nursing =
Chronic-care =
Rehab/specialist =
Mental health =
Welfare =
Cultural/social =
Support =
Legal =
Rehabilitation =
Other partner services =
Rehab duplication =
Home Visit =
Out-of-catalog =
```

## 11. Current status under D-0118

P1…P6 در وضعیت **OPEN** نگهداری می‌شوند و پاسخ فوری لازم نیست.

این وضعیت به معنی ACCEPT یا DEFER نیست. Technical نیز تا زمان بسته‌شدن هر موردی که واقعاً برای Gate لازم شود، حق حدس‌زدن آن را ندارد.

**BR-003: OPEN / PARKED**
