# DC-011 — Risk, Continuity, Security & Operational Resilience Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-012 + BC-017 + BC-021 + BC-022
- **Purpose:** بستن مرزهای حداقلی Risk، Incident، Continuity، Backup/Recovery، Security و Operational Resilience بدون اختراع Severity، SLA، RTO/RPO، Authentication Technology یا DR Architecture.

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند. طرح اولیه Risk Management، امنیت اطلاعات، پایداری سامانه، حفاظت از داده، پشتیبان‌گیری، کنترل دسترسی و پایش امنیت را الزام کلان می‌دهد؛ اما مقادیر، Stateها، Thresholdها و معماری فنی را تعیین نمی‌کند.

## 1. Source-confirmed risk families

طرح مبنا پنج خانواده ریسک را مشخص می‌کند:

1. Strategic
2. Operational
3. Financial
4. Legal / Regulatory
5. Technology

Risk Management باید در طراحی، اجرا، توسعه و بهره‌برداری مستمر باشد.

## 2. Candidate D-0071 — Risk management is a continuous governance function

- **تصمیم پیشنهادی:** Risk Management در نسیم یک فعالیت مقطعی نیست و باید در تمام چرخه طراحی، Pilot، Production و توسعه شبکه جاری باشد.
- **Boundary:** Risk scoring، appetite و thresholdها هنوز جداگانه تعیین می‌شوند.

**Assessment:** source-supported; recommended for acceptance.

## 3. Risk, incident, escalation and emergency must remain distinct

این مفاهیم نباید یکی فرض شوند:

- **Risk:** احتمال رخداد نامطلوب
- **Incident:** رخداد واقعی نیازمند رسیدگی
- **Escalation:** انتقال موضوع به سطح مسئولیت بالاتر
- **Emergency:** وضعیت فوری مرتبط با ایمنی/سلامت

## 4. Candidate D-0072 — Risk/Incident/Escalation/Emergency are distinct concepts

- **تصمیم پیشنهادی:** Risk، Incident، Escalation و Emergency در نسیم مفاهیم مستقل‌اند و تبدیل یکی به دیگری فقط با Rule مصوب انجام می‌شود.

**Assessment:** recommended for acceptance.

## 5. Incident scope

حداقل Incident Domainهای قابل پشتیبانی در آینده:

- service/referral failure
- provider failure
- workforce operational issue
- quality failure
- complaint-related issue
- system outage
- security incident
- data/privacy incident
- AI incident
- Dataset pipeline incident
- governance/control failure
- financial/control incident

Taxonomy و Severity نهایی هنوز باز هستند.

## 6. Candidate D-0073 — AI and Dataset incidents are first-class incident domains

- **تصمیم پیشنهادی:** چون AI و Dataset Lifecycle از روز اول عملیاتی‌اند، AI Incident و Dataset Pipeline Incident نیز از روز اول باید در Incident Governance نسیم قابل ثبت و رسیدگی باشند.

**Assessment:** aligned with D-0005; recommended for acceptance.

## 7. Human authority for sensitive risk decisions

تا Decision صریح:
- AI می‌تواند Detect/Flag کند.
- Rule Engine می‌تواند Alert تولید کند.
- ولی Incident Closure، final Severity، Risk Acceptance، Provider Suspension و Emergency Decision نهایی باید Owner انسانی/حاکمیتی مصوب داشته باشند.

## 8. Candidate D-0074 — Automation does not own risk acceptance

- **تصمیم پیشنهادی:** Automation یا AI حق Risk Acceptance، Incident Closure یا تصمیم نهایی Governance را به‌صرف Detection/Scoring ندارد.

`Detection / Automation ≠ Governance Acceptance`

**Assessment:** recommended for acceptance.

## 9. Continuity is broader than uptime

Business Continuity باید حداقل این حوزه‌ها را پوشش دهد:

- elder-facing operations
- caregiver operations
- referral/provider coordination
- communications
- case/record access
- incident handling
- AI assistance
- automatic Dataset lifecycle
- audit/lineage
- governance visibility

## 10. Candidate D-0075 — Availability, continuity and recovery are distinct

- **تصمیم پیشنهادی:** Availability، Continuity، Recovery و Disaster Recovery چهار مفهوم متفاوت‌اند و نباید با یک KPI یا یک State جایگزین شوند.

**Assessment:** aligned with BC-021; recommended for acceptance.

## 11. Criticality — still blocking

برای Capabilityهای Pilot باید Business تعیین کند:
- critical
- degradable
- deferrable

Candidate critical domains:
- access to active elder/case information
- open referrals
- incidents/escalations
- caregiver task visibility
- communication
- provider coordination
- audit-critical actions

AI Runtime و Dataset generation ممکن است Criticality متفاوت داشته باشند؛ این موضوع هنوز باید تصمیم شود.

## 12. Minimum operation during outage — still blocking

برای هر Capability حیاتی باید مشخص شود:
- چه کاری ادامه پیدا کند
- چه کاری می‌تواند متوقف شود
- چه manual/fallback process مجاز است
- چه داده‌ای باید بعداً reconcile شود
- چه کسی Continuity Mode را اعلام/ببندد

Technical نباید Manual Fallback اختراع کند.

## 13. Candidate D-0076 — Outage must not silently lose operational obligations

- **تصمیم پیشنهادی:** اختلال سامانه نباید باعث فراموش‌شدن Need، Referral، Incident، Task یا اقدام انسانی شود؛ هر اقدام fallback باید بعداً قابل Reconciliation و Audit باشد.

**Assessment:** recommended for acceptance.

## 14. Backup and recovery

منبع «پشتیبان‌گیری مستمر» را الزام کلان می‌دهد.

اما هنوز باید تعیین شود:
- backup scope
- cadence
- retention
- access
- restore verification
- failure handling
- recovery priority
- RTO/RPO

## 15. Candidate D-0077 — Backup is not proof of recoverability

- **تصمیم پیشنهادی:** وجود Backup به‌تنهایی Recovery Readiness را اثبات نمی‌کند؛ Recovery باید با Evidence/Restore Verification قابل اثبات باشد.

`Backup Exists ≠ Recovery Proven`

**Assessment:** recommended for acceptance.

## 16. Security source boundary

منبع صریحاً این موارد را الزام می‌کند:
- information security
- elder-data protection
- access control
- security monitoring

اما هیچ IdP، MFA، RBAC/ABAC، encryption algorithm یا SIEM در Business تصویب نشده است.

## 17. Candidate D-0078 — Security must survive degraded/recovery mode

- **تصمیم پیشنهادی:** Continuity یا Recovery urgency نباید به‌صورت پیش‌فرض Security Governance، Access Control یا Auditability را دور بزند.

`Recovery Urgency ≠ Permission to Bypass Security`

**Assessment:** aligned with BC-021/BC-022; recommended for acceptance.

## 18. Security and access during emergency

اگر Break-glass یا Emergency Access در آینده تصویب شود، باید حداقل:
- trigger
- eligible actor
- scope
- duration
- reason
- logging
- post-review
- expiry

داشته باشد.

هیچ Break-glass mechanism در این Packet تصویب نمی‌شود.

## 19. Candidate D-0079 — Privileged and emergency actions require attribution

- **تصمیم پیشنهادی:** Actionهای حساس، Recovery، Emergency Access، Restore و Security Override باید به Actor/Process مشخص، Authority و Audit قابل انتساب باشند.

**Assessment:** recommended for acceptance.

## 20. Monitoring and alerts

Monitoring آینده باید بتواند حداقل این حوزه‌ها را قابل مشاهده کند:
- availability/outage
- integration failure
- failed/suspicious access
- sensitive export/access
- AI runtime failure
- Dataset pipeline failure
- backup/restore failure
- unresolved incidents

اما:

`Alert ≠ Confirmed Incident`

Alert نیازمند Rule Review/Classification است.

## 21. Candidate D-0080 — Monitoring alert is not itself a confirmed incident

- **تصمیم پیشنهادی:** Alertهای فنی/امنیتی/AI به‌تنهایی Incident نهایی محسوب نمی‌شوند؛ Incident status باید طبق Rule مصوب تعیین شود.

**Assessment:** recommended for acceptance.

## 22. Communications during disruption — blocking

برای اختلال‌های مهم باید مشخص شود:
- چه Actorهایی مطلع شوند
- سالمند چگونه مطلع شود
- Provider چگونه مطلع شود
- چه Channelهایی قابل استفاده‌اند
- failed notification چه اثری دارد
- چه چیزی باید ثبت شود

BC-017 Channel یا Cadence نهایی تعیین نمی‌کند.

## 23. External dependency resilience

برای External Dependencyهای Mandatory Pilot باید:
- outage effect
- fallback
- recovery reconciliation
- operational notification
- owner

مشخص باشد.

این موضوع با DC-010 پیوند مستقیم دارد.

## 24. Risk/incident evidence in Scale Gate

Risk/Incident Evidence باید جزء Pilot/Scale Review باشد.

اما:
- وجود یک Incident لزوماً No-Go نیست.
- نبود Incident ثبت‌شده نیز ایمنی را اثبات نمی‌کند.

Gate-blocking severity/conditions و Risk Acceptance authority هنوز باید تعیین شوند.

## 25. Candidate D-0081 — Risk evidence is mandatory for scale decisions

- **تصمیم پیشنهادی:** تصمیم Scale باید Risk/Incident Evidence را به‌عنوان ورودی رسمی بررسی کند و نمی‌تواند صرفاً بر Coverage، KPI یا Revenue تکیه کند.

**Assessment:** aligned with BC-010/BC-011; recommended for acceptance.

## 26. Post-incident improvement

Incident/Risk Finding باید در صورت نیاز قابل اتصال باشد به:
- process change
- service-standard change
- training update
- provider remediation
- product change
- security control change
- data rule change
- AI guardrail/model action
- monitoring improvement

خود Incident به‌صورت خودکار Policy را تغییر نمی‌دهد.

## 27. Candidate D-0082 — Incident does not automatically change policy

- **تصمیم پیشنهادی:** Incident می‌تواند Change Proposal ایجاد کند، اما تغییر Policy/Rule/Guardrail باید از Change Governance مصوب عبور کند.

`Incident Finding ≠ Automatic Policy Change`

**Assessment:** aligned with BC-024; recommended for acceptance.

## 28. Product-owner decisions still blocking

1. final Risk taxonomy
2. Incident taxonomy
3. Severity model
4. Risk Acceptance authority
5. Incident owner/closure authority
6. Escalation Matrix
7. Emergency workflow
8. gate-blocking incident rules
9. Pilot capability criticality
10. minimum outage operations
11. fallback/manual-operation rules
12. RTO/RPO
13. backup scope/cadence/retention
14. restore-test expectations
15. Break-glass decision
16. privileged/recovery authority
17. security notification rules
18. continuity communication rules
19. AI fail-safe/availability boundary
20. Dataset-pipeline failure/recovery boundary
21. post-incident change workflow

## 29. Candidates ready for acceptance

- **D-0071:** Risk management is continuous.
- **D-0072:** Risk / Incident / Escalation / Emergency are distinct.
- **D-0073:** AI + Dataset incidents are first-class domains.
- **D-0074:** Automation does not own Risk Acceptance.
- **D-0075:** Availability / Continuity / Recovery / DR are distinct.
- **D-0076:** Outage must not silently lose obligations.
- **D-0077:** Backup Exists ≠ Recovery Proven.
- **D-0078:** Recovery urgency does not bypass security.
- **D-0079:** Privileged/recovery/emergency actions require attribution/audit.
- **D-0080:** Alert ≠ Confirmed Incident.
- **D-0081:** Risk/Incident evidence is required for Scale decisions.
- **D-0082:** Incident Finding ≠ Automatic Policy Change.

## 30. Gate effect

پذیرش D-0071 تا D-0082 چارچوب Resilience را روشن می‌کند، اما Technical Entry Gate تا تعیین Criticality، Emergency/Incident Authority، حداقل Continuity Behavior و Security/Recovery Business Requirements همچنان **NOT READY** می‌ماند.

## 31. Next closure packet

**DC-012 — Workforce, Scheduling, Communication & Case Operations Decision Packet**
