# DA-008 — Consolidated Product Owner Decision Board

- **Status:** AWAITING PRODUCT OWNER DECISION
- **Stage:** Business — Decision Acceptance
- **Date:** 2026-10-06
- **Source basis:** DA-001…DA-007 + DC-001…DC-014 + D-0001…D-0005
- **Candidate decision range:** D-0006…D-0117
- **Candidate count:** 112
- **Purpose:** ایجاد یک Board واحد برای تصمیم مالک محصول روی همه Candidate Decisionهای Business، بدون Acceptance ضمنی.

> این سند Decision Register نیست. ایجاد این Board هیچ Candidate را Accepted نمی‌کند. مرجع رسمی Acceptance همچنان `docs/DECISIONS.md` است.

## 1. Current accepted baseline

در زمان ایجاد این Board فقط این تصمیم‌ها Accepted هستند:

- D-0001 — نام و مخفف نسیم
- D-0002 — GitHub repository به‌عنوان مرجع رسمی تصمیمات
- D-0003 — فرآیند مادر توسعه محصول
- D-0004 — AI داخلی نسیم
- D-0005 — AI از Day-one + Automatic Versioned Dataset Lifecycle

هیچ Decision از D-0006 تا D-0117 هنوز Accepted نیست.

## 2. Consolidated acceptance board

| Round | Decision range | Domain | Count | Recommendation | Product Owner status |
|---|---:|---|---:|---|---|
| DA-001 | D-0006…D-0010 | Pilot Scope + Service Boundary | 5 | ACCEPT | PENDING |
| DA-002 | D-0011…D-0020 | Roles + Journey + Safety | 10 | ACCEPT | PENDING |
| DA-003 | D-0021…D-0035 | Data + Consent + AI Learning Governance | 15 | ACCEPT | PENDING |
| DA-004 | D-0036…D-0050 | Provider + Quality + Pilot/Scale Governance | 15 | ACCEPT | PENDING |
| DA-005 | D-0051…D-0070 | Economics + Funding + Integration Governance | 20 | ACCEPT | PENDING |
| DA-006 | D-0071…D-0093 | Risk + Continuity + Workforce + Operations | 23 | ACCEPT | PENDING |
| DA-007 | D-0094…D-0117 | Outcome + Reassessment + Configuration/Change Governance | 24 | ACCEPT | PENDING |

**Total: 112 Candidate Decisions**

## 3. Consolidated invariant set

The 112 candidates collectively preserve these core Business invariants:

- Role ≠ Permission
- Caregiver ≠ Specialist Provider
- Family ≠ Automatically Authorized Representative
- System ≠ Independent Business Authority
- AI Suggestion ≠ Human Decision
- AI Output ≠ Official Record
- AI Inference ≠ Observed Fact
- Operationally Available ≠ Training Eligible
- AI Runtime Access ≠ Training Permission
- Dataset Automation ≠ Governance Automation
- Training/Evaluation Success ≠ Production Promotion
- Model Version ≠ AI Policy Version
- Service Completion ≠ Need Resolution
- Provider Result ≠ Final Elder Outcome
- Satisfaction ≠ Outcome
- Observed Change ≠ Proven Causal Effect
- Recorded Outcome ≠ Automatically Verified Training Label
- Reporting / AI Analysis ≠ Approved Decision
- Integration Access ≠ Data Ownership
- External Data Received ≠ Automatically Accepted Truth
- External Data Available ≠ Training Eligible
- Integration Failure ≠ Silent Data Loss
- Backup Exists ≠ Recovery Proven
- Alert ≠ Confirmed Incident
- Recovery Urgency ≠ Permission to Bypass Security
- Decision ≠ Configuration ≠ Runtime Execution
- Draft ≠ Accepted ≠ Active
- Approved ≠ Automatically Active
- New Policy ≠ Retroactive Silent Rewrite
- Automatic Dataset Generation ≠ Automatic Policy Change
- Model Improvement ≠ Authority to Change Policy
- Code Deployment ≠ Silent Business Policy Change
- Automatic Learning Pipeline ≠ Automatic Governance Evolution

## 4. What bulk acceptance would mean

اگر مالک محصول D-0006 تا D-0117 را همگی **ACCEPT** کند:

- این 112 Candidate از حالت Proposal خارج می‌شوند.
- متن Accepted آنها باید در `docs/DECISIONS.md` ثبت شود.
- DA-001…DA-007 از PENDING به ACCEPTED/RESOLVED به‌روزرسانی می‌شوند.
- Business invariants فوق به Baseline رسمی Product تبدیل می‌شوند.
- Technical هنوز بلافاصله READY نمی‌شود، چون چند مقدار و Policy اجرایی Pilot هنوز فاقد مقدار نهایی‌اند.

Bulk Acceptance به معنی پذیرفتن همه Recommendationها با همان Boundaryهای ثبت‌شده است؛ نه پذیرفتن Blockerهایی که هنوز در Candidateها صریحاً Open مانده‌اند.

## 5. What bulk acceptance would NOT decide

حتی با ACCEPT همه 112 Candidate، این دسته‌ها همچنان نیازمند تصمیم صریح Phase/Pilot هستند:

### Pilot Scope
- Geography
- elder count
- caregiver count/ratio
- duration
- detailed enrollment eligibility
- exit/suspension rules
- active Service Items

### Operational Authority
- final Authority Matrix
- referral authorization
- provider selection
- incident/risk owner
- emergency ownership
- assignment/reassignment
- delegation/substitution

### Legal / Data
- Consent/legal basis per Purpose
- Authorized Representative workflow
- final Data Access Matrix
- retention/deletion
- export/sharing
- Training-eligible Data Classes

### AI / Learning
- Human Owner per AI Use Case
- exact review rules
- Evaluation Policy
- Model Promotion authority
- Model Rollback authority
- monitoring thresholds
- Training Eligibility details
- Label validation rules

### Provider
- Pilot Provider Types
- qualification/onboarding
- activation authority
- selection rule
- response semantics
- Completion Evidence
- suspension/re-routing

### KPI / Scale
- exact KPI catalog
- metric definitions
- target/threshold where required
- Pilot Success Criteria
- Scale Gate owner
- GO / CONDITIONAL GO / NO-GO rules

### Economics
- Pilot Sponsor
- Payor per Service
- direct elder payment scope
- Billing/Settlement scope
- Provider Settlement
- Unit Economics
- Financial Approval Matrix

### Integration / Continuity
- Pilot Integration Inventory
- Mandatory / Optional / Deferred classification
- Tarannom Pilot requirement
- Source-of-Truth matrix
- fallback rules
- critical capabilities
- minimum outage operation
- RTO/RPO where architecture requires values

### Configuration Governance
- Policy owner/approver matrix
- activation authority
- scope/precedence
- override details
- emergency-change path
- Production activation authority

## 6. Allowed Product Owner actions on this board

مالک محصول می‌تواند:

### Option A — Bulk accept all recommendations

`D-0006 تا D-0117 همگی ACCEPT`

Result:
- همه 112 Candidate با متن فعلی Accepted می‌شوند.
- Decision Register باید در Commit مستقل به‌روزرسانی شود.
- سپس یک Remaining Business Blocker Register ساخته می‌شود.

### Option B — Accept all except named decisions

Format:

`D-0006 تا D-0117 ACCEPT؛ به‌جز D-XXXX و D-YYYY که MODIFY/REJECT/DEFER شوند`

### Option C — Decide per acceptance round

Examples:

`DA-001 ACCEPT`

`DA-002 ACCEPT WITH MODIFICATION: ...`

### Option D — Decide individual decisions

Example:

`D-0031 ACCEPT، D-0032 MODIFY: ...`

## 7. Recommendation

چون تمام 112 Candidate قبلاً در DC-001…DC-014 با Boundaryهای عدم‌اختراع بررسی شده‌اند و در DA-001…DA-007 Recommendation = ACCEPT گرفته‌اند، Recommendation تجمیعی این Board:

**ACCEPT D-0006…D-0117 AS CURRENTLY WRITTEN**

این Recommendation فقط درباره Candidateهای آماده است و هیچ مقدار Open/Blocking را اختراع یا تصویب نمی‌کند.

## 8. Decision Register mutation rule

فقط پس از پیام صریح مالک محصول:

1. Accepted Decisionها در `docs/DECISIONS.md` ثبت می‌شوند.
2. هر Decision با Date، Domain، Status، Decision Text و Boundary ثبت می‌شود.
3. Acceptance Roundهای مربوطه به وضعیت resolved تغییر می‌کنند.
4. Blockerهای باقی‌مانده از Candidateهای Accepted حذف نمی‌شوند؛ به Remaining Business Blocker Register منتقل می‌شوند.
5. Technical Entry Gate دوباره ارزیابی می‌شود.

## 9. Current consolidated status

- Accepted: D-0001…D-0005
- Pending candidates: D-0006…D-0117
- Pending candidate count: 112
- Acceptance rounds prepared: DA-001…DA-007
- Consolidated board: DA-008
- Business → Technical Gate: **NOT READY**
- Reason: Product Owner Acceptance + remaining Pilot-specific Business values are still open.

## 10. Next step after Product Owner acceptance

پس از Acceptance این Board:

**BR-001 — Remaining Business Blocker Register & Pilot-specific Decision Closure**

این Artifact فقط Blockerهای واقعی باقی‌مانده را جمع می‌کند و آنها را به:
- MUST DECIDE BEFORE TECHNICAL
- EXPLICITLY DEFER FOR PILOT
- TECHNICAL DECISION
- LATER DELIVERY/OPERATIONS

طبقه‌بندی خواهد کرد.
