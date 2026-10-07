# BX-013 — Policy, Configuration & Change Governance Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** D-0002 + D-0003 + D-0004 + D-0005 + D-0118 + BC-024 + DC-014 + BR-004 + BX-012
- **Purpose:** تفکیک Decision، Policy، Configuration و Runtime Execution و ترسیم Versioning، Effective Dating، Scope، Override، Activation، Rollback و Change Governance در سطح Business؛ بدون ساخت Policy Engine، API، Schema یا Activation Implementation.

> این سند Candidate Decisionهای D-0105…D-0117 را Accepted نمی‌کند. آنها فقط به‌عنوان Candidate Governance Invariant بررسی می‌شوند.

## 1. Core separation

- Business Decision ≠ Policy / Configuration
- Policy / Configuration ≠ Runtime Execution
- Draft ≠ Accepted ≠ Active
- Approved ≠ Automatically Active
- New Policy ≠ Retroactive Silent Rewrite
- Code Deployment ≠ Silent Business Policy Change
- Automatic Dataset Generation ≠ Automatic Policy Change
- Model Improvement ≠ Authority to Change Policy
- Automatic Learning Pipeline ≠ Automatic Governance Evolution

## 2. Business Decision

Business Decision یک انتخاب مصوب Product/Governance است که باید در Decision Register مرجع ثبت شود.

Draft Contract، Exploration Artifact یا Runtime Configuration به‌تنهایی Accepted Decision نیست.

## 3. Policy

Policy بیان نسخه‌دار یک Rule کسب‌وکاری/حاکمیتی است که برای Scope و زمان مشخص قابل اعمال می‌شود.

Future Policy باید بتواند حداقل این ابعاد را داشته باشد:
- identifier/domain
- version
- owner
- approver
- scope
- status
- effective-from / effective-to where applicable
- rationale/evidence
- related Decision
- supersession/change history

Data Model فنی بعداً تعیین می‌شود.

## 4. Configuration

Configuration مقدار یا تنظیمی است که یک Policy/Rule مصوب را برای Scope مشخص operationalize می‌کند.

وجود Configuration به‌تنهایی Approval ایجاد نمی‌کند.

Configured ≠ Approved ≠ Active.

## 5. Runtime Execution

Runtime Execution اجرای Policy/Configuration فعال روی Context واقعی است.

Future audit should be able to trace:
Runtime Result → Active Policy Version → Scope → Input Context → Actor/Process → Time.

## 6. Status lifecycle — conceptual

Vocabulary مفهومی:
- DRAFT
- ACCEPTED / APPROVED
- ACTIVE / EFFECTIVE
- SUPERSEDED / RETIRED

این Vocabulary هنوز State Machine نهایی نیست.

OPEN:
- exact statuses
- who may move between statuses
- separation of duties
- activation authority
- rollback authority

## 7. Effective dating

Policy ممکن است Approved باشد ولی هنوز Active نشده باشد.

Policy می‌تواند در آینده:
- برای تاریخ آینده فعال شود
- فقط برای Pilot فعال شود
- فقط برای Organization/Geography/Scope مشخص فعال شود
- در زمان مشخص نسخه قبلی را supersede کند

Approved now ≠ Effective immediately.

## 8. Historical integrity

Recordهای مهم باید بتوانند به Policy Version مؤثر در زمان خود متصل بمانند.

Candidate examples:
- Need Taxonomy Version
- Service Catalog Version
- Eligibility Rule Version
- KPI Definition Version
- Consent / Access Policy Version
- AI Policy Version
- Training Eligibility Version
- Integration Contract Version

New Policy نباید معنای Historical Record را بی‌صدا عوض کند.

## 9. Policy domains

Candidate governance domains:
- enrollment / eligibility
- Need Taxonomy
- Service Catalog
- Need-to-Service mapping
- Referral eligibility
- Provider qualification / mapping
- Consent / privacy
- Data classification / access
- Training Eligibility
- Dataset preparation / curation
- AI use cases
- AI guardrails / Human Review
- KPI / reporting definitions
- Incident / risk rules
- Workforce / training requirements
- Communication / notification
- Integration contracts
- Continuity / recovery governance
- Security / access governance

وجود در این فهرست به معنی Accepted شدن هیچ Rule نیست.

## 10. Scope model — OPEN

Future Policy Scope may need to distinguish:
- global
- organization
- geography
- pilot
- service
- provider
- role/function
- AI use case

اما مدل نهایی Scope هنوز OPEN است.

### Trigger
قبل از multi-scope Policy Resolution یا Technical policy-store design.

## 11. Inheritance / precedence — OPEN

وقتی چند Policy هم‌زمان قابل اعمال‌اند، Business باید precedence را تعیین کند.

Examples:
- global vs organization
- organization vs pilot
- service vs provider
- old active version vs new effective version
- privacy restriction vs operational convenience
- AI policy vs data-access policy

Technical نباید precedence را اختراع کند.

## 12. Override

اگر Override در آینده مجاز شود، باید حداقل این Context را داشته باشد:
- scope
- actor
- reason
- duration/expiry
- target policy/version
- audit
- review/approval where required

Unlimited / invisible override نباید به‌عنوان Default فرض شود.

Exact override authority remains OPEN.

## 13. Policy conflict

Policy Conflict نیازمند Rule صریح است.

Future resolution may require:
- precedence
- explicit rejection
- Human Review
- temporary hold
- higher-order governance decision

هیچ conflict-resolution algorithm اینجا تعیین نمی‌شود.

## 14. Change proposal

تغییر Policy مهم باید قبل از Activation قابل بررسی باشد از منظر:
- elder safety
- operations
- workforce/provider
- legal/privacy
- data/security
- integration
- KPI/reporting
- AI/Dataset
- continuity/recovery
- economics

Depth of impact assessment remains OPEN.

## 15. Change classification — OPEN

Business آینده ممکن است نیاز داشته باشد Changeها را به کلاس‌هایی مانند:
- routine
- consequential
- high-risk
- emergency

تقسیم کند.

این Classification هنوز تصمیم نشده و هیچ SLA/Approval chain برای آن تعریف نمی‌شود.

## 16. Activation

Activation یعنی Policy/Configuration مصوب برای Scope مشخص وارد Runtime شود.

Future activation should be able to preserve:
- approved version
- scope
- effective time
- activating authority
- environment
- audit evidence

### Core boundary
Accepted ≠ Automatically Active.

## 17. Rollout

برای Change حساس، آینده ممکن است rollout محدود لازم داشته باشد.

Candidate dimensions:
- scope
- start time
- observation window
- rollback readiness
- evidence

اما rollout rule نهایی OPEN است.

## 18. Rollback

Rollback باید از Historical Rewrite جدا باشد.

Future rollback should consider:
- previous valid version
- effective time
- impacted records
- reconciliation
- reporting impact
- Dataset/AI impact
- audit

Rollback authority و exact trigger OPEN هستند.

## 19. Restatement / migration

برخی Policy Changeها ممکن است نیازمند Migration/Restatement باشند؛ اما historical meaning نباید silently change.

Future rule باید روشن کند:
- which records remain under old version
- which future actions use new version
- whether derived reports are restated
- whether Dataset versions are regenerated or remain immutable

هیچ default migration policy تعیین نمی‌شود.

## 20. AI policy boundary

AI Policy باید از Model Version جدا بماند.

AI Policy may govern:
- use case
- allowed data
- output type
- guardrails
- Human Review
- fail-safe
- provenance

Changing Model Version نباید این Policyها را خودکار تغییر دهد.

## 21. Dataset / learning policy boundary

Training Eligibility و Curation Rule باید Versionable باشند.

Automatic Dataset Generation فقط Rule مصوب را اجرا می‌کند.

Dataset pipeline حق ندارد:
- eligibility را توسعه دهد
- consent/access rule را تغییر دهد
- guardrail را تغییر دهد
- policy activation انجام دهد
- model promotion authority بسازد

## 22. Model promotion boundary

Model Promotion یک Governance action مستقل از Training/Evaluation است.

Training/Evaluation Success ≠ Production Promotion.

Promotion/Rollback Authority در AI Governance همچنان OPEN است.

## 23. Code vs policy

Technical Configuration مثل timeout، replica count یا implementation detail لزوماً Business Policy نیست.

اما هر Code Change که Business Meaning را تغییر می‌دهد باید به Decision/Policy مرتبط قابل trace باشد.

Code Deployment نباید Business Policy را silently redefine کند.

## 24. Production activation

Production باید همان Policy Version مصوب برای همان Scope را اجرا کند.

Future evidence should be able to show:
- approved version
- active production version
- activation time
- actor/authority
- scope
- stage/production difference if any

Production Activation Authority هنوز OPEN است.

## 25. Emergency change — OPEN

Business آینده باید قبل از استفاده واقعی روشن کند:
- Emergency Change چیست
- چه Actorی مجاز است
- حداقل Approval چیست
- duration
- expiry
- post-review
- formalization or rollback

هیچ Break-glass Change Rule در BX-013 تصویب نمی‌شود.

## 26. Policy registry — business need

نسیم در آینده به یک Registry منطقی برای Policyها نیاز دارد که بتواند حداقل این موارد را نگه دارد:
- domain/id
- version
- status
- owner/approver
- scope
- effective dates
- dependencies
- supersession
- audit reference

Technology و Schema نهایی بعداً تعیین می‌شوند.

## 27. Decision-trigger matrix

- Policy status lifecycle: before Policy workflow freeze
- Owner/Approver Matrix: before policy approval workflow
- Activation Authority: before policy activation
- Scope model: before multi-scope policy storage/resolution
- Inheritance/Precedence: before policy conflict resolution
- Override policy: before any runtime override capability
- Change classification: before change workflow
- Impact-assessment depth: before consequential policy change
- Rollout rules: before limited-scope activation
- Rollback rules: before sensitive production activation
- Emergency-change path: before break-glass change capability
- Restatement/migration rules: before policy changes affect historical/derived data
- Production Activation Authority: before production policy promotion
- Separation of duties: before authorization/approval implementation

## 28. Explicit non-decisions

BX-013 does not define Policy Engine، database schema، API، enum/state machine، approval workflow implementation، precedence algorithm، scope hierarchy، override permissions، rollout percentage، emergency-change SLA، activation technology، feature-flag product، configuration service یا policy storage technology.

## 29. Cross-domain governance invariants

این تفکیک‌ها باید در Artifactهای بعدی حفظ شوند:
- Decision ≠ Configuration ≠ Runtime Execution
- Draft ≠ Accepted ≠ Active
- Approved ≠ Automatically Active
- New Policy ≠ Retroactive Silent Rewrite
- Runtime Result باید به Rule Version قابل ردیابی باشد
- Automatic Dataset Generation ≠ Automatic Policy Change
- Model Improvement ≠ Authority to Change Policy
- Configured ≠ Approved ≠ Active
- Override باید bounded/auditable باشد if allowed
- Sensitive Change نیازمند rollback consideration است
- Code Deployment ≠ Silent Business Policy Change
- Automatic Learning Pipeline ≠ Automatic Governance Evolution

اینها در BX-013 Exploration invariants هستند؛ Accepted Decision Register همچنان فقط D-0001…D-0005 و D-0118 را دارد.

## 30. Next artifact

**BX-014 — Cross-Domain Consistency & Contextual Decision Trigger Review**

Scope:
- مرور BX-001…BX-013
- کشف تناقض یا overlap بین Domainها
- یکپارچه‌سازی Decision Triggerها
- تفکیک exploration-safe work از context-triggered decisions
- شناسایی کوچک‌ترین مجموعه Blocker برای حرکت بعدی
- بدون Accept کردن D-0006…D-0117 و بدون عبور خودکار به Technical

## 31. Current stage

- Stage: Business
- Policy/Change Governance exploration: ACTIVE
- Business → Technical: NOT READY
- Code: NOT STARTED
- Codex handoff: NOT YET TRIGGERED