# BC-022 — Security, Identity, Access Control & Audit Governance

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-005 + BC-007 + BC-012 + BC-013 + BC-014 + BC-021
- **Depends on:** BC-005, BC-006, BC-007, BC-008, BC-012, BC-013, BC-014, BC-017, BC-020, BC-021

> این سند چارچوب کسب‌وکاری Identity، Authentication، Authorization، Least Privilege، Access Governance، Audit و Security Monitoring در نسیم را تعریف می‌کند. منبع اولیه «کنترل دسترسی»، «حفاظت از اطلاعات سالمندان»، «امنیت اطلاعات» و «پایش امنیت» را الزام کلان می‌داند، اما نوع IAM، MFA، Session Policy، RBAC/ABAC، رمزنگاری، Identity Provider یا معماری فنی امنیت را مشخص نکرده است؛ بنابراین هیچ فناوری یا Policy عددی در این سند اختراع نمی‌شود.

## 1. Source-confirmed Security Direction

طرح مبنا وابستگی شبکه به سامانه‌های اطلاعاتی را یک ریسک فناوری می‌داند و بر این موارد تأکید می‌کند:

- امنیت اطلاعات
- حفاظت از داده سالمندان
- کنترل دسترسی
- پایش امنیت
- پایداری سامانه
- پشتیبان‌گیری

بنابراین Security و Access Control جزء الزامات پایه بهره‌برداری نسیم هستند.

## 2. Identity ≠ Role ≠ Permission

سه مفهوم باید مستقل باقی بمانند:

- **Identity:** چه شخص/سامانه‌ای در حال تعامل است
- **Role:** جایگاه یا نقش سازمانی/عملیاتی
- **Permission:** چه اقدام یا داده‌ای برای آن Identity مجاز است

اصل:

`Job Title ≠ Permission`

وجود عنوان «سالمندیار»، «مدیر» یا «Provider» نباید خودکار به دسترسی کامل منجر شود.

## 3. Human Identity Domains

نسیم در آینده باید بتواند Identityهای انسانی حداقل این Actorها را از هم تفکیک کند:

- سالمند
- خانواده / همراه
- نماینده مجاز در صورت تعریف
- سالمندیار
- سالمندیار ارشد
- سطوح سرپرستی
- کارکنان عملیاتی نسیم
- Quality/Audit
- مدیران
- Provider personnel
- کارفرما
- Admin/Governance roles

Role inventory نهایی هنوز تصمیم نشده است.

## 4. Non-human Identity Domains

در کنار انسان‌ها، سامانه آینده ممکن است Identityهای غیرانسانی داشته باشد، مانند:

- application/service identity
- integration identity
- automation process
- AI runtime
- dataset pipeline
- training/evaluation process
- monitoring/backup process

وجود این Candidateها به معنی انتخاب معماری Service Account یا Credential Type مشخص نیست.

## 5. Authentication — Open Contract

Business باید در آینده مشخص کند برای هر Actor چه سطحی از احراز هویت لازم است.

موضوعات باز:

- login method
- password/passwordless
- OTP
- MFA
- device trust
- identity proofing
- provider/staff onboarding verification
- elder identity verification
- representative verification
- session duration
- re-authentication
- recovery/reset process

BC-022 هیچ روش Authentication را تصویب نمی‌کند.

## 6. Authorization Principle

هر Identity فقط باید به Action و Data لازم برای Purpose مصوب دسترسی داشته باشد.

اصل:

`Authenticated ≠ Authorized for everything`

و:

`Role membership ≠ universal data access`

Authorization باید از Authentication جدا طراحی شود.

## 7. Least Privilege

اصل کسب‌وکاری:

هر Actor باید حداقل سطح دسترسی لازم برای انجام مسئولیت مصوب را داشته باشد.

این اصل باید برای:

- data
- workflow actions
- reports
- exports
- approvals
- admin functions
- AI runtime
- training pipeline

قابل اعمال باشد.

جزئیات فنی Least Privilege در Technical تعیین می‌شود.

## 8. Purpose-bound Access

همسو با BC-007 و BC-014، دسترسی باید علاوه بر Role، با Purpose نیز سازگار باشد.

مثلاً ممکن است Actor برای یک Case مجاز به مشاهده داده‌ای باشد، ولی برای:

- گزارش مدیریتی
- اشتراک با Provider
- Training AI
- Export
- Audit

همان مجوز را نداشته باشد.

اصل:

`Operational Access ≠ Training Access ≠ Reporting Access ≠ Export Permission`

## 9. Elder Access Boundary

باید در آینده تعیین شود سالمند چه دسترسی‌ای به داده و عملیات خود دارد، از جمله:

- مشاهده پرونده
- مشاهده Needها
- مشاهده Referralها
- مشاهده Service history
- مشاهده Outcome/Reassessment
- اصلاح/اعتراض
- Consent/preferences
- AI interaction history
- audit/access history در صورت تصویب

هیچ سطح دسترسی نهایی در منبع تعیین نشده است.

## 10. Family / Representative Access

همسو با BC-014:

`Family ≠ Authorized Representative`

بنابراین خانواده تا زمان اثبات/تعریف Authority نباید دسترسی خودکار به پرونده سالمند داشته باشد.

در آینده باید مشخص شود:

- چه کسی Authorized Representative است
- Scope اختیار چیست
- مدت اعتبار چیست
- revocation چگونه است
- دسترسی به چه Data Classهایی مجاز است
- چه اقدام‌هایی می‌تواند انجام دهد

## 11. Elder-care-worker Access

سالمندیار برای انجام وظایف خود به بخشی از داده و Workflow نیاز دارد.

اما دسترسی او نباید از مسئولیت‌های مصوب فراتر رود.

باید در آینده تعیین شود:

- access to assigned elders
- cross-case access
- geographic access
- sensitive data access
- referral/service data
- outcome/reassessment
- complaint/incident
- export
- correction/edit rights

BC-022 هیچ Full-record Access پیش‌فرض ایجاد نمی‌کند.

## 12. Supervisor Access

سطوح سرپرستی ممکن است برای Oversight به داده بیشتری نیاز داشته باشند، اما Title نباید دسترسی مطلق ایجاد کند.

Candidate access dimensions:

- team
- geography
- workload
- case summary
- quality
- incidents
- performance
- reassignment
- approvals

مرز Drill-down و Data Sensitivity هنوز باز است.

## 13. Provider Access

همسو با BC-008:

`Provider Access ≠ Full Elder Record Access`

Provider فقط باید داده لازم برای Service/Referral مصوب را ببیند.

باید در آینده برای هر Service/Provider Type تعیین شود:

- required data
- permitted actions
- write-back/result fields
- duration of access
- revocation
- onward sharing
- audit

## 14. Employer Access

نقش نظارتی کارفرما به معنی دسترسی فردی نامحدود نیست.

همسو با BC-020:

`Aggregate visibility ≠ individual-record access`

Employer Access باید با Reporting Boundary، Data Minimization و Purpose مصوب تعیین شود.

## 15. Admin Access Is Not Unlimited by Default

Admin بودن نباید به معنی دسترسی نامحدود به همه داده‌های سالمندان باشد.

Business آینده باید بین این Capabilityها تفکیک کند:

- system administration
- user/identity administration
- business configuration
- data access
- audit access
- security administration
- AI/model administration

Segregation of Duties باید بعداً تعیین شود.

## 16. AI Runtime Access Boundary

AI داخلی برای Use Case مصوب ممکن است به بخشی از Context سالمند یا عملیات نیاز داشته باشد.

اصل:

`AI can access only data required for the approved use case.`

AI Runtime نباید به دلیل «داخلی بودن» دسترسی نامحدود داشته باشد.

باید برای هر Use Case تعیین شود:

- required data classes
- time/context scope
- purpose
- sensitive-data restrictions
- human-review requirement
- logging/audit
- training separation

## 17. AI Runtime Access ≠ Training Permission

اصل تثبیت‌شده BC-007:

`Runtime Access ≠ Training Permission`

داده‌ای که AI برای پاسخ لحظه‌ای مجاز به استفاده از آن است، خودکار Training-eligible نیست.

این جداسازی باید در Access Governance قابل اعمال باشد.

## 18. Dataset / Training Pipeline Access

Pipeline Learning فقط باید به داده‌ای دسترسی داشته باشد که Training Eligibility Rule مصوب آن را مجاز کرده است.

باید در آینده مشخص شود:

- source scope
- eligible classes
- excluded classes
- de-identification/preparation
- access owner
- execution identity
- audit trail
- dataset write permission
- lineage write permission

Pipeline نباید Rule Eligibility را خودش تغییر دهد.

## 19. Model / AI Governance Access

Actionهای حساس AI باید Access Control مستقل داشته باشند، مانند:

- register model/version
- attach evaluation evidence
- change AI policy/guardrail
- promote model
- rollback model
- change training eligibility
- alter dataset lineage

Owner و Approval Rule هنوز در BC-013 باز است.

## 20. Authentication of Automated Processes

هر Process غیرانسانی که Action رسمی انجام می‌دهد باید در آینده قابل شناسایی باشد.

Audit باید بتواند تفاوت میان:

- human action
- system action
- scheduled automation
- AI action/suggestion
- dataset pipeline action

را نشان دهد.

روش Credential فنی هنوز تصمیم نشده است.

## 21. Delegation & Acting-on-behalf-of

اگر Actor انسانی از طرف Actor دیگری عمل می‌کند، باید Business Rule مستقل وجود داشته باشد.

Candidate scenarios:

- supervisor substitution
- authorized representative
- temporary delegation
- operational coverage during absence
- emergency access

سیستم نباید Acting-on-behalf-of را با Login مشترک یا هویت جعلی حل کند.

## 22. Shared Accounts — Boundary

برای Auditability آینده، Action رسمی باید تا حد ممکن به Actor/Process قابل انتساب باشد.

استفاده از Shared Identity برای اقدام رسمی می‌تواند Attribution را مخدوش کند.

Policy نهایی Shared Account هنوز تصمیم نشده است، اما Technical نباید آن را پیش‌فرض طراحی کند.

## 23. Access Lifecycle

برای هر Identity/Access باید در آینده Lifecycle تعریف شود:

- request
- review
- grant
- change
- temporary elevation
- suspension
- revocation
- periodic review
- termination/offboarding

State Machine و SLA نهایی هنوز تعیین نشده‌اند.

## 24. Joiner / Mover / Leaver

تغییر وضعیت نیروی انسانی یا Provider باید روی Access اثر قابل کنترل داشته باشد.

نمونه:

- استخدام/فعال‌سازی
- تغییر نقش
- تغییر منطقه
- تعلیق
- پایان همکاری
- Provider contract end

هیچ Access نباید فقط به دلیل باقی‌ماندن Credential قدیمی ادامه یابد.

## 25. Access Review

Business آینده باید مشخص کند چه Accessهایی نیازمند Periodic Review هستند.

Candidate high-risk areas:

- admin
- sensitive elder data
- employer drill-down
- provider access
- AI runtime
- training pipeline
- exports
- model promotion
- risk/incident governance

Cadence و Reviewer هنوز باز هستند.

## 26. Privileged Access

Actionهای حساس باید در آینده بتوانند از دسترسی عادی تفکیک شوند.

Candidate privileged actions:

- user/access administration
- security configuration
- bulk export
- data correction override
- backup restore
- emergency access
- model promotion/rollback
- dataset eligibility policy change

هیچ PAM technology یا workflow نهایی در BC-022 تصویب نمی‌شود.

## 27. Break-glass / Emergency Access — Open

BC-021 نیاز به تصمیم Break-glass را باز گذاشته است.

اگر چنین سازوکاری تصویب شود باید حداقل مشخص کند:

- trigger
- eligible roles
- scope
- duration
- reason
- logging
- post-review
- automatic expiry
- incident linkage

هیچ Emergency Access فعلاً تصویب نشده است.

## 28. Audit Principle

برای Actionهای مهم باید بتوان پاسخ داد:

- چه کسی/چه Processی؟
- چه اقدامی؟
- روی چه Resource/Recordی؟
- چه زمانی؟
- از چه Contextی؟
- نتیجه چه بود؟
- چه چیزی تغییر کرد؟
- AI involvement وجود داشت یا خیر؟
- Approval/Delegation مرتبط چه بود؟

ساختار فنی Audit Log در Technical تعیین می‌شود.

## 29. Audit Scope — DRAFT

Candidate auditable domains:

- authentication events
- access grants/revocations
- record views در صورت نیاز
- record changes
- consent/representative changes
- referral/service decisions
- provider actions
- exports
- incident decisions
- governance approvals
- AI suggestions/human review
- dataset build/version
- training/evaluation
- model promotion/rollback
- backup/restore

سطح جزئیات و Retention هنوز تصمیم نشده‌اند.

## 30. Audit ≠ Operational Record

Audit Trail و Business Record یک چیز نیستند.

- Business Record وضعیت رسمی عملیات را نگه می‌دارد.
- Audit Trail تاریخچه Action/Access/Change را برای Accountability نگه می‌دارد.

Technical نباید Audit را به‌عنوان جایگزین Data Model عملیاتی استفاده کند.

## 31. Audit Integrity

Business آینده باید مشخص کند چه سطحی از حفاظت برای Audit لازم است تا تغییرات بدون ردپا باقی نمانند.

Candidate needs:

- append/history preservation
- restricted modification
- time/source traceability
- integrity verification
- retention
- export for review

Implementation فنی هنوز تصمیم نشده است.

## 32. Security Monitoring

منبع اولیه «پایش امنیت» را صریحاً ذکر می‌کند.

Security Monitoring آینده باید بتواند حداقل رخدادهای مرتبط با:

- failed/suspicious authentication
- unusual access
- unauthorized action
- privilege change
- sensitive export
- credential/security incident
- AI/data access violation
- dataset-pipeline policy violation
- backup/restore security events

را در Scope بررسی قرار دهد.

Detection Rule و Threshold هنوز باز هستند.

## 33. Security Alert ≠ Confirmed Incident

اصل:

`Security Alert ≠ Confirmed Security Incident`

Alert باید Review شود و طبق BC-012 ممکن است به Incident تبدیل شود.

AI یا Rule Engine نباید بدون Contract نهایی Incident را خودکار قطعی/بسته کند.

## 34. Data Export Governance

Export می‌تواند ریسک دسترسی را از محیط کنترل‌شده به بیرون منتقل کند.

برای هر Export آینده باید Rule تعیین شود:

- who can export
- what data
- purpose
- scope
- format
- masking
- recipient
- audit
- retention/expiry
- onward-sharing restriction

هیچ Export Permission پیش‌فرض تصویب نشده است.

## 35. Access to Backups

همسو با BC-021، Backup نیز تحت Access Governance است.

دسترسی Backup باید جدا از دسترسی عادی Production تعریف شود و Restore Action نیز نیازمند Authority و Audit مصوب است.

## 36. Security Incident Link

رخدادهایی مانند این باید با BC-012 پیوند داشته باشند:

- unauthorized access
- credential compromise
- excessive privilege
- unauthorized export
- identity misuse
- privilege escalation
- AI unauthorized data access
- training pipeline unauthorized data access
- audit integrity failure

Severity، Notification و Response Rule هنوز نهایی نشده‌اند.

## 37. Access and Privacy Requests

همسو با BC-014، در آینده ممکن است سالمند یا نماینده مجاز نیاز به پاسخ درباره Access/Sharing داشته باشد.

Business باید تعیین کند آیا و چگونه می‌توان گزارش کرد:

- چه Actorهایی دسترسی داشته‌اند
- چه Data Sharing رخ داده
- چه Exportهایی انجام شده
- چه Consent/Authority فعال بوده

حقوق نهایی وابسته به Legal Review است.

## 38. Security vs Continuity

Continuity نباید برای سرعت بازیابی Security را دور بزند.

اصل:

`Recovery urgency ≠ permission to bypass security governance`

هر استثنا باید Rule، Authority، Time Limit و Audit مشخص داشته باشد.

## 39. Security Training

نقش‌هایی که به داده حساس یا Actionهای حساس دسترسی دارند باید در آینده Training متناسب با مسئولیت داشته باشند.

Candidate domains:

- confidentiality
- credential safety
- phishing/social engineering awareness
- secure data handling
- incident reporting
- AI/data access boundaries
- export/share rules

Curriculum نهایی در BC-015/Technical بعدی تعیین می‌شود.

## 40. Security Reporting

همسو با BC-020، Governance Reporting آینده می‌تواند حوزه‌هایی مانند این را پوشش دهد:

- access-review status
- privileged-access activity
- unresolved security incidents
- authentication/security alerts
- export activity
- audit health
- AI/data access violations

هیچ KPI یا Threshold نهایی تصویب نشده است.

## 41. Explicit Non-Decisions

BC-022 موارد زیر را تصویب نمی‌کند:

- Identity Provider
- OIDC/SAML/LDAP
- Password policy
- MFA method
- session duration
- RBAC vs ABAC
- encryption algorithms
- key-management technology
- PAM product
- SIEM product
- audit storage technology
- log-retention duration
- record-view logging policy نهایی
- break-glass mechanism
- shared-account policy نهایی
- IP/device restrictions
- zero-trust architecture
- network-security architecture
- access-review cadence

## 42. Open Decisions Required to Accept BC-022

1. Identity inventory
2. Authentication policy per actor
3. Identity-proofing requirements
4. Authorization model
5. Data Access Matrix
6. Action/Approval Permission Matrix
7. Employer access boundary
8. Provider access boundary
9. Family/representative access
10. Elder self-access
11. AI runtime access policy
12. Dataset/training pipeline access policy
13. Privileged-access model
14. Delegation/acting-on-behalf-of policy
15. Joiner/Mover/Leaver policy
16. Access-review policy
17. Break-glass policy
18. Audit event catalog
19. Audit retention/integrity policy
20. Security monitoring/alert rules
21. Export governance
22. Security incident linkage
23. Backup/restore access authority
24. Security training requirements

## 43. Downstream Constraints

تا پیش از Accepted شدن BC-022:

- Technical نباید RBAC/ABAC، IdP یا Authentication Method نهایی را اختراع کند.
- Title نباید خودکار Permission شود.
- Provider، Family و Employer نباید Full-record Access پیش‌فرض داشته باشند.
- AI Runtime نباید دسترسی نامحدود به داده داشته باشد.
- Training Pipeline فقط باید به داده Training-eligible دسترسی داشته باشد.
- Privileged Action باید از Action عادی قابل تفکیک باشد.
- Human/System/AI/Automation actions باید در Audit قابل انتساب باشند.
- Recovery نباید Security Governance را دور بزند.
