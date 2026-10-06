# BR-002 — Pilot-specific Decision Input Sheet

- **Status:** AWAITING PRODUCT OWNER INPUT
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** BR-001 + OPEN_QUESTIONS.md + DC-001…DC-015 + DA-001…DA-008
- **Purpose:** جمع‌آوری فقط مقادیر و انتخاب‌های واقعی Phase/Pilot که از Concept و اسناد موجود قابل استنتاج نیستند و برای Technical Entry باید توسط مالک محصول تعیین یا صریحاً Deferred شوند.

> این سند هیچ Candidate Decision از D-0006…D-0117 را Accepted نمی‌کند و جای DA-008 را نمی‌گیرد. پاسخ‌های این Sheet فقط پس از تأیید صریح مالک محصول به Decision Register یا Deferral Register تبدیل می‌شوند.

## 1. How to answer

برای هر مورد یکی از این پاسخ‌ها لازم است:

- **VALUE:** مقدار/انتخاب نهایی
- **POLICY:** قاعده نهایی
- **DEFER:** خارج از Scope پایلوت فعلی
- **NOT APPLICABLE:** در این Pilot کاربرد ندارد
- **NEEDS EVIDENCE:** تصمیم فقط بعد از دریافت سند/اطلاعات بیرونی

عبارت‌هایی مانند «بعداً»، «فعلاً معلوم نیست» یا خالی‌گذاشتن پاسخ، Deferral محسوب نمی‌شوند.

---

## 2. P1 — Pilot Geography

**Question:** پایلوت دقیقاً در کدام محدوده جغرافیایی اجرا می‌شود؟

**Input required:**
- Province:
- City/County:
- District/Neighborhood/Village:
- Urban / Rural / Mixed:
- Boundary notes:

**Current status:** INPUT REQUIRED

---

## 3. P2 — Pilot Population Size

**Question:** Scope عملیاتی پایلوت از نظر ظرفیت اولیه چیست؟

**Input required:**
- Elder count:
- Caregiver count:
- Supervisor count, if applicable:
- Minimum active Provider count:
- Elder-to-caregiver ratio, if fixed:

**Current status:** INPUT REQUIRED

---

## 4. P3 — Pilot Duration

**Question:** مدت رسمی Pilot چقدر است؟

**Input required:**
- Start condition/date:
- Duration:
- Review checkpoints:
- Extension authority:
- Maximum extension, if any:

**Current status:** INPUT REQUIRED

---

## 5. P4 — Enrollment Eligibility

**Question:** یک سالمند دقیقاً تحت چه شرایطی وارد Pilot می‌شود؟

**Input required:**
- Age definition:
- IKRF/support-status requirement:
- Residence requirement:
- minimum Need requirement, if any:
- consent/authorization prerequisite:
- prioritization rule:
- exclusion rule:
- waiting-list rule:

**Current status:** INPUT REQUIRED

---

## 6. P5 — Exit / Suspension

**Question:** سالمند چه زمانی از Pilot خارج، suspend یا منتقل می‌شود؟

**Input required:**
- voluntary withdrawal:
- support-status change:
- geography change:
- unreachable handling:
- legal/consent change:
- safety restriction:
- duplicate enrollment:
- death:
- transfer to another program:
- final closure authority:

**Current status:** INPUT REQUIRED

---

## 7. P6 — Active Phase-1 Service Catalog

**Question:** کدام Service Familyها در Pilot واقعاً فعال‌اند؟

### Health
Choose ACTIVE / DEFER:
- health assessment:
- medical:
- nursing:
- chronic-care:
- rehabilitation/specialist:
- mental health:

### Welfare / Complementary
Choose ACTIVE / DEFER:
- welfare:
- cultural/social:
- support:
- legal:
- rehabilitation:
- other partner services:

**Additional input required:**
- rehabilitation duplication resolution:
- Home Visit = Service Item or Mode of Operation:
- out-of-catalog handling:

**Current status:** INPUT REQUIRED

---

## 8. P7 — Pilot Role Inventory

**Question:** کدام Actor/Roleها در Pilot رسمی هستند؟

Choose IN SCOPE / OUT OF SCOPE:
- Elder
- Authorized Representative
- Family Contact
- Caregiver
- Senior Caregiver
- Neighborhood Supervisor
- Regional Supervisor
- Nasim Operations
- Quality/Audit
- Provider
- Employer/Sponsor
- Data Governance
- AI Governance
- Risk/Incident Owner
- Financial Approver
- Scale Gate Approver
- System Admin/Security

**Current status:** INPUT REQUIRED

---

## 9. P8 — Core Authority Matrix

برای هر Business Action، Final Authority را مشخص کنید:

| Action | Final authority |
|---|---|
| Case assignment | INPUT REQUIRED |
| Case reassignment | INPUT REQUIRED |
| Referral authorization | INPUT REQUIRED |
| Provider selection | INPUT REQUIRED |
| Provider activation | INPUT REQUIRED |
| Provider suspension | INPUT REQUIRED |
| Referral re-route | INPUT REQUIRED |
| Need Resolution | INPUT REQUIRED |
| Need Reopen | INPUT REQUIRED |
| Complaint closure | INPUT REQUIRED |
| Incident severity | INPUT REQUIRED |
| Incident closure | INPUT REQUIRED |
| Risk Acceptance | INPUT REQUIRED |
| Emergency operational decision | INPUT REQUIRED |
| Financial exception | INPUT REQUIRED |
| Model Promotion | INPUT REQUIRED |
| Model Rollback | INPUT REQUIRED |
| Scale GO/NO-GO | INPUT REQUIRED |
| Policy Production Activation | INPUT REQUIRED |

---

## 10. P9 — Authorized Representative

**Question:** نماینده مجاز سالمند چگونه تعریف و فعال می‌شود؟

**Input required:**
- eligibility/legal basis:
- verification:
- scope of authority:
- data access:
- consent authority:
- expiration/revocation:
- emergency handling:
- multiple representatives rule:

**Current status:** INPUT REQUIRED

---

## 11. P10 — Consent / Legal Basis by Purpose

برای هر Purpose، مبنا را مشخص کنید:

| Purpose | Consent / legal basis |
|---|---|
| Service enrollment | INPUT REQUIRED |
| operational data collection | INPUT REQUIRED |
| Provider data sharing | INPUT REQUIRED |
| Employer reporting | INPUT REQUIRED |
| AI Runtime assistance | INPUT REQUIRED |
| AI Training | INPUT REQUIRED |
| Research/Evaluation, if any | INPUT REQUIRED |
| Export/sharing outside Nasim | INPUT REQUIRED |

**Current status:** INPUT REQUIRED

---

## 12. P11 — Minimum Data Access Matrix

برای Pilot حداقل سطح دسترسی Actorهای زیر را تعیین کنید:

- Elder:
- Authorized Representative:
- Family Contact:
- Caregiver:
- Supervisor:
- Provider:
- Employer/Sponsor:
- Operations:
- Quality/Audit:
- AI Runtime:
- Dataset/Training Pipeline:
- Admin/Security:

**Rule:** role access باید Purpose-limited باشد؛ Technical نباید Access را از Job Title حدس بزند.

**Current status:** INPUT REQUIRED

---

## 13. P12 — Training-eligible Data Classes

**Question:** کدام دسته داده‌ها اصولاً می‌توانند Candidate Learning Data باشند؟

For each choose ELIGIBLE / EXCLUDED / CONDITIONAL:
- elder-entered data:
- caregiver observations:
- provider result:
- structured assessment:
- reassessment:
- satisfaction:
- complaints:
- incident data:
- communication transcript:
- AI interactions:
- official accepted state:
- recorded outcome:
- external-system data:
- employer data:
- financial data:

**Also required:**
- mandatory exclusions:
- required de-identification/pseudonymization:
- quality/verification prerequisite:
- Training Eligibility owner:

**Current status:** INPUT REQUIRED

---

## 14. P13 — AI Day-one Human Ownership

برای هر Use Case، Human Owner/Reviewer را مشخص کنید:

### Elder-facing
- service guidance:
- referral/service status explanation:
- reminders:
- need-expression assistance:
- record explanation:
- system-use help:
- human escalation:

### Caregiver-facing
- history summary:
- daily follow-up preparation:
- change flagging:
- draft notes/reports:
- suggested questions:
- catalog/process search:
- candidate referral path:
- open-task reminders:
- data inconsistency flag:

**Current status:** INPUT REQUIRED

---

## 15. P14 — AI Evaluation / Promotion / Rollback Governance

**Input required:**
- AI Governance owner:
- Evaluation approver:
- minimum Evaluation evidence:
- Promotion authority:
- Rollback authority:
- Production activation authority:
- unavailable/invalid AI fallback:
- AI Incident owner:
- model monitoring owner:
- interaction retention direction:

**Current status:** INPUT REQUIRED

---

## 16. P15 — Provider Scope

**Input required:**
- Provider Types in Pilot:
- minimum qualification:
- required documents/evidence:
- activation authority:
- Service-to-Provider mapping owner:
- Provider response rule:
- no-response handling:
- minimum Completion Evidence:
- re-route/fallback rule:
- suspension authority:
- Provider data-sharing fields:

**Current status:** INPUT REQUIRED

---

## 17. P16 — KPI / Pilot Success

**Input required:**
- Pilot KPI catalog:
- KPI business definition owner:
- KPI data source owner:
- Satisfaction method:
- AI quality evidence:
- Dataset lifecycle evidence:
- Risk/Incident evidence:
- Economic evidence:
- Pilot Success Criteria:
- GO / CONDITIONAL GO / NO-GO rule:
- Scale Gate owner:
- observation period:

**Note:** Numeric Target/Threshold may be explicitly Deferred only if evidence capture remains fully specified.

**Current status:** INPUT REQUIRED

---

## 18. P17 — Funding / Payment Scope

**Input required:**
- Pilot Sponsor:
- funding source:
- budget authority:
- direct elder payment = IN SCOPE / OUT OF SCOPE:
- Billing = IN SCOPE / OUT OF SCOPE:
- Provider Settlement = IN SCOPE / OUT OF SCOPE:
- Financial Approver:
- minimum cost categories to capture:
- Economic Unit for Pilot, if required now:

**Current status:** INPUT REQUIRED

---

## 19. P18 — Pilot Integration Inventory

For each Integration provide:
- system/partner
- MANDATORY / OPTIONAL / DEFERRED
- business purpose
- inbound / outbound / bidirectional
- data classes
- Source of Truth
- fallback
- owner

### Known source direction
- Tarannom

### Decision required
- Tarannom status for Pilot:
- Other mandatory systems:
- Optional systems:
- Explicitly deferred systems:

**Current status:** INPUT REQUIRED

---

## 20. P19 — Continuity / Outage Minimum Behavior

Classify each capability as CRITICAL / DEGRADABLE / DEFERRABLE:
- active elder/case access:
- open referrals:
- caregiver task visibility:
- communication:
- provider coordination:
- incident handling:
- AI Runtime:
- automatic Dataset generation:
- reporting:
- audit/lineage:

**Also required:**
- minimum manual/fallback operation:
- Continuity Mode activation authority:
- recovery reconciliation owner:
- whether RTO/RPO must be fixed before Technical Architecture:

**Current status:** INPUT REQUIRED

---

## 21. P20 — Emergency / Urgent Boundary

**Input required:**
- definition of Urgent:
- definition of Emergency:
- first operational actor:
- escalation destination:
- when normal Journey pauses:
- external emergency path:
- follow-up requirement:
- documentation requirement:
- whether 24/7 service is in scope:
- whether medical triage is in scope:

**Current status:** INPUT REQUIRED

---

## 22. P21 — Reassessment / Outcome

**Input required:**
- Reassessment definition:
- trigger(s):
- cadence:
- Baseline definition:
- Outcome taxonomy:
- accepted evidence sources:
- Need Resolution criterion:
- Reopen/Recurrence rule:
- Outcome reviewer:
- AI role in Outcome analysis:
- Outcome Training Eligibility:
- Training-label validation authority:

**Current status:** INPUT REQUIRED

---

## 23. P22 — Policy / Change Governance

**Input required:**
- Policy Owner model:
- Policy Approver model:
- Activation authority:
- scope levels:
- precedence rule:
- override authority:
- override expiry rule:
- conflict-resolution authority:
- emergency-change authority:
- Production Policy Activation authority:
- Separation-of-Duties requirement:

**Current status:** INPUT REQUIRED

---

## 24. P23 — Explicit Deferral Candidates

برای هر مورد یکی از ACCEPT DEFERRAL / KEEP OPEN را تعیین کنید:

- Provider ranking/scoring
- advanced Provider quality ranking
- non-safety numeric SLA
- long-term caregiver compensation formula
- long-term Provider tariff/settlement formula
- full-market Revenue Model
- mature Unit Economics / Break-even
- advanced employer reporting
- optional communication channels
- Voice Assistant
- advanced forecasting/predictive analytics
- non-Pilot integrations
- national-scale organization design
- advanced rollout strategies
- long-term concentration limits
- mature-scale workforce promotion thresholds
- non-critical report layouts
- advanced dashboard presentation

For each accepted Deferral also provide:
- owner:
- future gate:
- constraint:

**Current status:** INPUT REQUIRED

---

## 25. Minimum response strategy

مالک محصول لازم نیست همه P1…P23 را در یک پیام پاسخ دهد.

Recommended closure sequence:

1. P1…P6 — Pilot Scope + Services
2. P7…P11 — Roles + Authority + Data
3. P12…P14 — AI + Learning
4. P15…P18 — Provider + KPI + Funding + Integrations
5. P19…P22 — Continuity + Emergency + Outcome + Policy
6. P23 — Explicit Deferrals

پس از هر Batch، پاسخ‌های پذیرفته‌شده باید به Decision Register/Deferral Register منتقل و Blocker Matrix به‌روزرسانی شوند.

## 26. Gate status

تا وقتی پاسخ‌های Blocking این Sheet به Decisionهای Accepted یا Deferralهای صریح تبدیل نشده‌اند:

**Business → Technical: NOT READY**

و:

**BR-002: WAITING FOR PRODUCT OWNER INPUT**
