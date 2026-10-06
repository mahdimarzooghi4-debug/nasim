# DA-006 — Product Owner Decision Acceptance Round: Risk + Continuity + Workforce + Operations

- **Status:** AWAITING PRODUCT OWNER DECISION
- **Stage:** Business — Decision Acceptance
- **Date:** 2026-10-06
- **Source basis:** DC-011 + DC-012
- **Decision range:** D-0071…D-0093
- **Purpose:** ارائه Candidate Decisionهای Risk/Incident، Continuity/Security، Workforce Readiness، Scheduling، Communication و Case Operations برای Accept / Modify / Reject / Defer، بدون Acceptance ضمنی.

> این سند Decision Register نیست. تا زمانی که مالک محصول تصمیم صریح ندهد، هیچ‌یک از D-0071 تا D-0093 Accepted محسوب نمی‌شوند و `docs/DECISIONS.md` تغییر نمی‌کند.

## 1. Review Rule

برای هر Candidate یکی از Outcomeهای زیر لازم است:

- **ACCEPT**
- **ACCEPT WITH MODIFICATION**
- **REJECT**
- **DEFER FOR CURRENT PILOT**
- **MERGE WITH ANOTHER DECISION**

Recommendation فقط پیشنهاد است.

---

## 2. D-0071 — Risk Management Is Continuous

### Proposed decision

Risk Management در نسیم یک فعالیت مقطعی نیست و باید در تمام چرخه طراحی، Pilot، Production و توسعه شبکه جاری باشد.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 3. D-0072 — Risk / Incident / Escalation / Emergency Are Distinct

### Proposed decision

Risk، Incident، Escalation و Emergency مفاهیم مستقل‌اند و تبدیل یکی به دیگری فقط طبق Rule مصوب انجام می‌شود.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 4. D-0073 — AI and Dataset Incidents Are First-class Domains

### Proposed decision

چون AI و Dataset Lifecycle از روز اول عملیاتی‌اند، AI Incident و Dataset Pipeline Incident نیز باید از روز اول در Incident Governance قابل ثبت، پیگیری و رسیدگی باشند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 5. D-0074 — Automation Does Not Own Risk Acceptance

### Proposed decision

Automation یا AI صرفاً با Detection/Scoring حق Risk Acceptance، Incident Closure یا تصمیم نهایی Governance را ندارد.

`Detection / Automation ≠ Governance Acceptance`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 6. D-0075 — Availability / Continuity / Recovery / DR Are Distinct

### Proposed decision

Availability، Continuity، Recovery و Disaster Recovery مفاهیم متفاوت‌اند و نباید با یک KPI یا State واحد جایگزین شوند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 7. D-0076 — Outage Must Not Silently Lose Operational Obligations

### Proposed decision

اختلال سامانه نباید باعث فراموش‌شدن Need، Referral، Incident، Task یا اقدام انسانی شود؛ هر اقدام Fallback باید بعداً قابل Reconciliation و Audit باشد.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 8. D-0077 — Backup Exists Does Not Mean Recovery Proven

### Proposed decision

وجود Backup به‌تنهایی Recovery Readiness را اثبات نمی‌کند؛ Recovery باید با Restore Verification / Evidence قابل اثبات باشد.

`Backup Exists ≠ Recovery Proven`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 9. D-0078 — Recovery Urgency Does Not Bypass Security

### Proposed decision

Continuity یا Recovery urgency نباید Security Governance، Access Control یا Auditability را به‌صورت پیش‌فرض دور بزند.

`Recovery Urgency ≠ Permission to Bypass Security`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 10. D-0079 — Privileged / Recovery / Emergency Actions Require Attribution

### Proposed decision

Actionهای حساس، Recovery، Emergency Access، Restore و Security Override باید به Actor/Process مشخص، Authority و Audit قابل انتساب باشند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 11. D-0080 — Alert Is Not a Confirmed Incident

### Proposed decision

Alertهای فنی، امنیتی یا AI به‌تنهایی Incident نهایی محسوب نمی‌شوند؛ Incident Status باید طبق Rule مصوب تعیین شود.

`Alert ≠ Confirmed Incident`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 12. D-0081 — Risk/Incident Evidence Is Required for Scale Decisions

### Proposed decision

Scale Decision باید Risk/Incident Evidence را به‌عنوان ورودی رسمی بررسی کند و نمی‌تواند صرفاً بر Coverage، KPI یا Revenue تکیه کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 13. D-0082 — Incident Finding Does Not Automatically Change Policy

### Proposed decision

Incident می‌تواند Change Proposal ایجاد کند، اما تغییر Policy، Rule یا Guardrail باید از Change Governance مصوب عبور کند.

`Incident Finding ≠ Automatic Policy Change`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 14. D-0083 — Human Capital Is a Core Operating Capability

### Proposed decision

سرمایه انسانی سالمندیاران یک Capability اصلی عملیات نسیم است و کیفیت خدمت، رضایت و مقیاس‌پذیری بدون Workforce Readiness معتبر تلقی نمی‌شود.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 15. D-0084 — Required Training Precedes Operational Activation

### Proposed decision

هیچ سالمندیار نباید پیش از طی آموزش‌های الزامی نسخه فعال، Operationally Active تلقی شود.

Pass Rule، Assessment، Certification و Approver جداگانه تعیین می‌شوند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 16. D-0085 — Day-one AI Requires Workforce AI-readiness

### Proposed decision

چون AI از روز اول جزء محصول است، آموزش سالمندیار قبل از Activation باید Boundaryهای AI، Human Review، Data/Privacy، Official Record و AI Incident Reporting را پوشش دهد.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 17. D-0086 — Training Content Must Be Versioned

### Proposed decision

محتوای آموزش عملیاتی باید Versioned و Effective-dated باشد تا مشخص باشد هر سالمندیار با کدام نسخه آموزش برای چه Scopeی آماده شده است.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 18. D-0087 — Volume Does Not Equal Workforce Performance

### Proposed decision

عملکرد سالمندیار نباید صرفاً بر اساس تعداد سالمندان یا فعالیت سنجیده شود؛ کیفیت پیگیری، رضایت، دقت داده، پاسخ‌گویی و یادگیری نیز جزء Evidence عملکردند.

`Volume ≠ Workforce Performance`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 19. D-0088 — Career Progression Does Not Auto-grant Authority

### Proposed decision

ارتقای شغلی یا Title جدید به‌تنهایی Permission، Data Access یا Approval Right ایجاد نمی‌کند؛ Authority Matrix باید مستقل باشد.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 20. D-0089 — Active Elder/Case Needs Explicit Operational Responsibility

### Proposed decision

برای هر سالمند/Case فعال باید مسئول عملیاتی ارتباط و پیگیری قابل تشخیص باشد؛ وضعیت بدون Owner یا با Owner مبهم نباید حالت عادی عملیات باشد.

Assignment Rule و Substitute Model جداگانه تعیین می‌شوند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 21. D-0090 — Scheduling/Cadence Is Business Policy, Not Technical Default

### Proposed decision

Cadence تماس، Follow-up، Visit، Reminder و Reassessment باید Policy مصوب و Versioned باشند؛ Technical نباید زمان پیش‌فرض اختراع کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 22. D-0091 — Communication Channel Must Fit Elder Suitability and Authorization

### Proposed decision

Channel ارتباط باید با دسترس‌پذیری، ترجیح/مجوز، محرمانگی و شرایط سالمند سازگار باشد و هیچ Channel واحدی به‌صورت پیش‌فرض برای همه سالمندان الزام‌آور نیست.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 23. D-0092 — AI Must Not Impersonate a Human Actor

### Proposed decision

در تعامل مستقیم، کاربر باید بتواند تشخیص دهد پاسخ AI-generated است؛ AI نباید خود را سالمندیار، Provider، پزشک یا Human Decision Maker معرفی کند.

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 24. D-0093 — Message / Conversation Is Not Automatically Official Record

### Proposed decision

تماس، پیام یا AI Conversation به‌خودی‌خود Official Record نیست و تبدیل آن به Record رسمی باید Rule و Actor معتبر داشته باشد.

`Message / Conversation ≠ Official Record`

### Recommendation

**ACCEPT**

### Product Owner Decision

**PENDING**

---

## 25. What acceptance of D-0071…D-0093 would close

در صورت پذیرش این 23 Candidate:

- Risk Management به یک Function مستمر Governance تبدیل می‌شود.
- Risk/Incident/Escalation/Emergency از هم جدا می‌شوند.
- AI/Dataset incidents به‌عنوان Domain رسمی پذیرفته می‌شوند.
- Automation از Risk Acceptance و Incident Closure جدا می‌ماند.
- Continuity/Recovery/DR تفکیک می‌شوند.
- Outage اجازه Silent Loss نمی‌دهد.
- Backup از Proven Recovery جدا می‌شود.
- Security در Recovery حفظ می‌شود.
- Alert از Incident نهایی جدا می‌شود.
- Risk Evidence وارد Scale Gate می‌شود.
- Incident خودکار Policy را تغییر نمی‌دهد.
- Workforce Readiness، Training-before-Activation و AI-readiness تثبیت می‌شوند.
- Training Versioning و Performance multi-factor تثبیت می‌شوند.
- Career Title از Authority جدا می‌شود.
- Operational Owner برای Case/elder فعال لازم می‌شود.
- Scheduling به Business Policy تبدیل می‌شود.
- Communication بر اساس Elder Suitability/Authorization کنترل می‌شود.
- AI impersonation ممنوع می‌ماند.
- Message/Conversation از Official Record جدا می‌شود.

## 26. Blockers that remain even after acceptance

### Risk / Continuity / Security
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

### Workforce / Operations / Communication
22. recruitment criteria
23. screening/assessment
24. final training curriculum
25. readiness/pass rule
26. activation authority
27. continuous-training cadence
28. retraining triggers
29. performance KPI/thresholds
30. promotion criteria
31. capacity model / elder-to-worker ratio
32. assignment/reassignment authority
33. substitute/absence rule
34. contact/follow-up/visit cadence
35. field-work policy
36. communication channel catalog
37. elder preferences/permissions
38. family communication permissions
39. provider communication model
40. quiet hours/contact windows
41. failed-contact handling
42. communication logging/retention
43. workforce conduct/disciplinary process
44. compensation model

## 27. Technical decisions intentionally not decided here

این Round موارد زیر را انتخاب نمی‌کند:

- IdP / MFA technology
- RBAC vs ABAC implementation
- encryption algorithm
- SIEM
- backup technology
- DR topology
- RTO/RPO values
- scheduler technology
- notification vendor
- SMS/voice platform
- task engine
- workforce scoring algorithm

اینها فقط پس از روشن‌شدن Business Intent وارد Technical می‌شوند.

## 28. Decision Register update rule

پس از تصمیم صریح مالک محصول:

- ACCEPT → در `docs/DECISIONS.md` ثبت می‌شود.
- ACCEPT WITH MODIFICATION → متن اصلاح‌شده ثبت می‌شود.
- REJECT → Accepted Decision ساخته نمی‌شود؛ نتیجه Review ثبت می‌شود.
- DEFER → Scope، Owner، Future Gate و Constraint لازم است.
- MERGE → ارتباط Candidate با Decision مقصد Traceable می‌شود.

## 29. Current dependency note

- DA-001 برای D-0006…D-0010 همچنان **PENDING** است.
- DA-002 برای D-0011…D-0020 همچنان **PENDING** است.
- DA-003 برای D-0021…D-0035 همچنان **PENDING** است.
- DA-004 برای D-0036…D-0050 همچنان **PENDING** است.
- DA-005 برای D-0051…D-0070 همچنان **PENDING** است.
- ایجاد DA-006 به معنی Acceptance ضمنی هیچ Round قبلی نیست.

## 30. Recommended Product Owner response

برای پذیرش Recommendation فعلی:

`D-0071 تا D-0093 همگی ACCEPT`

یا هر Decision جداگانه با Outcome/Modification اعلام شود.

## 31. Gate status

تا زمان تصمیم صریح مالک محصول:

**Business → Technical: NOT READY**

و:

**Decision Acceptance Round DA-006: WAITING FOR PRODUCT OWNER**
