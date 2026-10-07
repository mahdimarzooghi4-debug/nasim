# BR-004 — Contextual Open Decision Register

- **Status:** ACTIVE
- **Stage:** Business — Contextual Decision Governance
- **Date:** 2026-10-06
- **Source basis:** D-0118 + BR-001 + BR-002 + BR-003 + BC-025 + BX-015 + BX-016

این سند تصمیم‌های باز را نگه می‌دارد تا فقط زمانی بسته شوند که Context واقعی کار به آنها نیاز داشته باشد.

## Governing rule

`OPEN ≠ DEFERRED ≠ ACCEPTED`

طبق D-0118، تصمیم باز نباید زودتر از نیاز واقعی بسته شود و Technical/Backlog/Code نیز حق حدس‌زدن آن را ندارند.

## Statuses

- **OPEN:** تصمیم هنوز لازم نشده یا Evidence کافی ندارد.
- **CONTEXT TRIGGERED:** کار جاری اکنون واقعاً به این تصمیم وابسته شده است.
- **ACCEPTED:** تصمیم صریح ثبت شده است.
- **DEFERRED:** صریحاً از Scope جاری خارج شده و Owner/Future Gate/Constraint دارد.
- **SUPERSEDED:** با تصمیم جدید جایگزین شده است.

## Open decision groups and triggers

### Pilot Scope
- Geography — وقتی Pilot location واقعی انتخاب شود.
- Population size — وقتی capacity/staffing/budget sizing لازم شود.
- Duration — هنگام Pilot Plan.
- Enrollment eligibility — قبل از Enrollment workflow.
- Exit/suspension — قبل از Case lifecycle freeze.
- Active Service Catalog — قبل از Service/Referral contract freeze.

### Roles & Authority
- Role inventory — قبل از Identity/Authorization design.
- Case assignment/reassignment — قبل از Case Ownership workflow.
- Referral authorization — قبل از Referral mutation contract.
- Provider selection — قبل از Provider Matching workflow.
- Incident/Risk authority — قبل از Incident workflow.
- Emergency ownership — قبل از Safety-critical workflow.

### Data / Legal / Access
- Consent/legal basis — قبل از جمع‌آوری یا اشتراک واقعی داده.
- Authorized Representative — قبل از representative access.
- Data Access Matrix — قبل از authorization implementation.
- Provider sharing boundary — قبل از Provider integration.
- Retention/deletion — قبل از Production data lifecycle freeze.
- Export/sharing — قبل از export capability.

### AI / Learning
- Final elder/caregiver AI use cases — قبل از AI UX/API contract freeze.
- Forbidden actions — قبل از AI runtime contract freeze.
- Human Owner/Review — قبل از consequential AI workflow.
- Training-eligible Data Classes / exclusions — قبل از Dataset Builder.
- Evaluation governance — قبل از Model Evaluation workflow.
- Promotion/Rollback authority — قبل از Production model lifecycle.
- AI fail-safe — قبل از runtime availability contract.

### Provider
- Provider Types — قبل از Provider Registry schema freeze.
- Qualification/activation — قبل از Provider Activation workflow.
- Service-to-Provider mapping — قبل از Referral routing.
- Response semantics — قبل از Provider response workflow.
- Completion Evidence — قبل از Service Completion contract.
- Re-routing/suspension — قبل از Provider failure governance.

### KPI / Economics / Scale
- KPI catalog — قبل از measurement contract freeze.
- KPI thresholds — فقط وقتی automation/gate به عدد نیاز دارد.
- Pilot Success Criteria / Scale Gate owner — قبل از Pilot launch/exit.
- Sponsor/Payor/Billing/Settlement — قبل از financial capability.
- Economic Unit — قبل از Unit Economics reporting.

### Integration / Continuity
- Integration Inventory — قبل از external integration design.
- Tarannom requirement — قبل از health integration design.
- Source of Truth — قبل از bidirectional exchange.
- Fallback — قبل از mandatory external dependency.
- Critical capabilities / minimum outage operation — قبل از continuity architecture freeze.
- RTO/RPO — فقط اگر architecture sizing به عدد نیاز پیدا کند.

### Outcome / Policy
- Reassessment definition/cadence — قبل از reassessment workflow.
- Baseline / Need Resolution — قبل از Outcome/Need closure contract.
- Outcome evidence validity / Training Eligibility — قبل از formal Outcome learning path.
- Policy Owner/Approver — قبل از Policy activation workflow.
- Scope/precedence/override — قبل از multi-scope policy resolution.
- Production Policy Activation authority — قبل از Production policy promotion.

## Allowed work while decisions remain OPEN

مجاز:
- Business exploration
- domain vocabulary clarification
- dependency mapping
- non-binding Technical exploration
- architecture option comparison
- test/risk exploration
- backlog discovery items that are not implementation-ready

غیرمجاز:
- architecture freeze بر پایه Business guess
- implementation-ready contract وابسته به Policy باز
- production code با Eligibility/Authority/Access فرضی
- hard-coded threshold بدون Accepted Decision
- implicit acceptance of Draft/Candidate decisions

## Context-trigger procedure

وقتی Work Item به Decision باز وابسته شد:
1. همان Decision به **CONTEXT TRIGGERED** تغییر می‌کند.
2. فقط همان Decision یا کوچک‌ترین مجموعه وابسته مطرح می‌شود.
3. پاسخ در Decision Register یا Deferral Register ثبت می‌شود.
4. Work Item ادامه می‌یابد.
5. Decisionهای نامرتبط OPEN می‌مانند.

`Just-in-time Decision Closure > Forced Up-front Decision Closure`

## Current state

- Stage: **Business — Technical Entry Preparation**
- Accepted: D-0001…D-0005 + D-0118 + D-0119 + D-0120 + D-0121 + D-0122
- D-0006…D-0117: هنوز Accepted نشده‌اند.
- BR-003 P1…P6: **OPEN / PARKED**
- BX-001…BX-015: Exploration / Technical-entry candidate mapping completed.
- Selected Technical Slice: **TS-03 — Core Case / Journey Foundation**
- Global Business → Technical Gate: **NOT PASSED**
- TS-03 Q1 Case Entry Boundary: **RESOLVED — starts after Enrollment (D-0119)**
- TS-03 Q2 Early Journey Scope: **RESOLVED — Contact → Case/Profile → Monitoring → Observation / Need capture (D-0120)**
- TS-03 Q3 Case Operational Owner / Assignment: **RESOLVED — caregiver primary owner/contact; authorized supervisory/operations assignment; reassignment reason + audit (D-0121)**
- TS-03 Q4 Minimum Case/Profile Data Classes: **RESOLVED — six bounded Data Classes; medical/provider/outcome/AI-training data excluded from current slice (D-0122)**
- Next TS-03 question: **Q5 — Correction / History**
- کار غیرالزام‌آور Documentation/Gate Preparation می‌تواند ادامه یابد.

## Current next path

از BX-015 برای انتخاب صریح یک Technical Slice محدود استفاده می‌شود. فقط پس از Selection:
1. کوچک‌ترین Decision Set وابسته به همان Slice به **CONTEXT TRIGGERED** می‌رود.
2. همان مجموعه Accept/Modify/Reject/Explicitly Defer می‌شود.
3. Slice Gate Evidence ساخته می‌شود.
4. Technical فقط در صورت Pass شدن همان Slice Gate آغاز می‌شود.

تا قبل از Selection، هیچ Decision نامرتبط نباید به‌اجبار بسته شود.
