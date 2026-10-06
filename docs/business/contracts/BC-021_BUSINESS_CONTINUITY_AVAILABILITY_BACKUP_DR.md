# BC-021 — Business Continuity, Availability, Backup & Disaster Recovery

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-007 + BC-012 + BC-020
- **Depends on:** BC-006, BC-007, BC-012, BC-013, BC-014, BC-016, BC-017, BC-020

> این سند چارچوب کسب‌وکاری تداوم خدمت، پایداری سامانه، پشتیبان‌گیری، بازیابی و رفتار نسیم هنگام اختلال را تعریف می‌کند. منبع اولیه «پایداری سامانه‌ها»، «پشتیبان‌گیری مستمر»، «کنترل دسترسی» و «پایش امنیت» را الزام کلان می‌داند، اما RTO، RPO، معماری Failover، تعداد نسخه Backup، Recovery Site، سطح Availability یا DR Runbook نهایی را تعیین نکرده است؛ بنابراین هیچ مقدار یا معماری فنی در این سند اختراع نمی‌شود.

## 1. Source-confirmed Continuity Direction

طرح اولیه وابستگی شبکه به سامانه‌های اطلاعاتی را یک ریسک فناوری می‌داند و برای کنترل آن بر این موارد تأکید می‌کند:

- پایداری سامانه‌ها
- امنیت اطلاعات
- حفاظت از داده‌های سالمندان
- پشتیبان‌گیری مستمر
- کنترل دسترسی
- پایش امنیت
- توسعه زیرساخت‌های فناوری

بنابراین Business Continuity برای نسیم یک نیاز اصلی بهره‌برداری است، نه قابلیت اختیاری.

## 2. Continuity Scope

تداوم نسیم فقط «روشن بودن وب‌سایت» نیست.

Business Continuity آینده باید بتواند حداقل این حوزه‌ها را پوشش دهد:

- Elder-facing operations
- Elder-care-worker operations
- Referral operations
- Provider coordination
- Communication/notification
- Case/record access
- Reporting/management visibility
- AI assistance
- Automatic Dataset lifecycle
- Audit/lineage
- Incident handling

میزان Criticality هر حوزه هنوز باید جداگانه تعیین شود.

## 3. Availability ≠ Continuity ≠ Recovery

این مفاهیم باید از هم تفکیک شوند:

- **Availability:** قابلیت دسترسی به سرویس در یک زمان مشخص
- **Continuity:** توان ادامه خدمت در شرایط اختلال
- **Recovery:** بازگرداندن سرویس/داده پس از اختلال
- **Disaster Recovery:** بازیابی پس از اختلال شدید یا گسترده

Technical نباید این چهار مفهوم را با یک KPI واحد جایگزین کند.

## 4. Service Criticality — Open Contract

Business آینده باید برای Capabilityهای اصلی نسیم سطح Criticality تعیین کند.

Candidate domains:

- access to elder record
- open needs/referrals
- incident/escalation
- caregiver task access
- provider coordination
- communications
- AI runtime
- dataset generation
- reporting
- admin/governance

هیچ Criticality Class یا Priority نهایی در BC-021 تصویب نمی‌شود.

## 5. Minimum Operations During Outage

برای هر Capability حیاتی باید در آینده مشخص شود که در زمان اختلال:

- چه کاری باید ادامه پیدا کند
- چه کاری می‌تواند موقتاً متوقف شود
- چه داده‌ای باید قابل دسترس باشد
- چه عملیات دستی/جایگزین مجاز است
- چه چیزی بعداً باید Reconcile شود
- چه کسی وضعیت Continuity را اعلام می‌کند

هیچ Manual Fallback نهایی در منبع تعریف نشده است.

## 6. System Outage Boundary

اختلال سامانه نباید باعث شود:

- نیاز یا Referral باز فراموش شود
- Incident حیاتی گم شود
- تاریخچه داده حذف شود
- اقدام انسانی بدون Audit قابل بازسازی باقی بماند
- AI تصمیم ساختگی جایگزین سیستم ازکارافتاده کند

روش فنی تحقق این قواعد در Technical تعیین می‌شود.

## 7. Backup Principle — Source-confirmed

منبع اولیه «پشتیبان‌گیری مستمر» را صریحاً یکی از کنترل‌های ریسک فناوری می‌داند.

Backup Policy آینده باید حداقل برای این موارد تصمیم داشته باشد:

- چه Data/Artifactهایی Backup می‌شوند
- Cadence
- Retention
- Encryption/security
- Access
- Restore verification
- Off-site / isolated copy در صورت نیاز
- Backup failure handling

هیچ عدد یا فناوری در BC-021 تصویب نمی‌شود.

## 8. Backup ≠ Recovery

اصل:

`Backup Exists ≠ Recovery Proven`

وجود Backup به‌تنهایی به معنی امکان بازیابی معتبر نیست.

Business آینده باید Recovery Evidence و دوره آزمون Restore را تعریف کند.

## 9. Recovery Objectives — Open

در آینده باید برای Capabilityهای حیاتی این اهداف تعیین شوند:

- **RTO** — حداکثر زمان قابل قبول برای بازگردانی
- **RPO** — حداکثر میزان قابل قبول از دست رفتن داده زمانی
- recovery priority
- dependency order

هیچ مقدار RTO/RPO در طرح اولیه وجود ندارد.

## 10. Data Integrity During Recovery

Recovery نباید فقط «بالا آمدن سیستم» باشد.

باید بتوان بعد از بازیابی بررسی کرد:

- data completeness
- consistency
- provenance
- audit continuity
- version integrity
- access-control integrity
- open workflow continuity
- dataset/model lineage continuity

Rule و Evidence نهایی هنوز باز هستند.

## 11. Longitudinal Record Protection

همسو با BC-019، تاریخچه وضعیت سالمند نباید بی‌صدا از دست برود یا overwrite شود.

در Recovery باید توان حفظ/بازسازی این موارد وجود داشته باشد:

- observation history
- need/referral history
- service history
- reassessment/outcome history
- corrections
- audit events

روش فنی در Technical تعیین می‌شود.

## 12. AI Day-one Continuity

بر اساس D-0005، AI از روز اول بخشی از محصول است؛ بنابراین Availability/Failure آن نیز باید از روز اول در Continuity Plan دیده شود.

Business آینده باید مشخص کند در صورت:

- AI unavailable
- model runtime failure
- model artifact unavailable
- invalid model/version
- AI dependency failure

چه رفتار عملیاتی مجاز است.

## 13. AI Fail-safe During Outage

اصل:

`AI unavailable ≠ permission to fabricate AI output`

در نبود AI معتبر:

- سیستم نباید پاسخ ساختگی به نام AI تولید کند
- تصمیم رسمی نباید جعل شود
- Human Workflow باید در صورت امکان ادامه یابد
- وضعیت عدم دسترس‌پذیری باید قابل مشاهده باشد

Fallback دقیق هنوز باید تعیین شود.

## 14. AI Graceful Degradation — DRAFT FRAME

برای Use Caseهای AI باید در آینده مشخص شود:

- آیا عملیات بدون AI قابل ادامه است
- چه قابلیت‌هایی Degrade می‌شوند
- چه Taskهایی به Human-only تبدیل می‌شوند
- چه تعاملاتی موقتاً غیرفعال می‌شوند
- چگونه بعداً Reconcile می‌شوند

این موارد هنوز Decision نهایی نیستند.

## 15. Dataset Lifecycle Continuity

با توجه به D-0005، Pipeline ساخت Dataset نیز از روز اول باید در Continuity Scope باشد.

در صورت اختلال باید آینده بتواند تشخیص دهد:

- کدام Source Window پردازش شده
- کدام Eventها پردازش نشده
- آخرین Dataset Version معتبر چیست
- آیا Build ناقص ایجاد شده
- آیا Lineage کامل است
- آیا Retry باعث Duplicate شده است یا خیر

جزئیات فنی Idempotency/Replay در Technical تعیین می‌شوند.

## 16. Dataset Failure ≠ Operational Data Loss

خرابی Pipeline Dataset نباید باعث حذف یا تغییر داده عملیاتی منبع شود.

اصل:

`Learning Pipeline Failure ≠ Operational Record Mutation`

مسیر Learning باید از Record اصلی قابل تفکیک و بازیابی باشد.

## 17. Dataset Recovery Boundary

در بازیابی چرخه Learning باید بتوان:

- آخرین Dataset معتبر را شناسایی کرد
- Dataset ناقص/خراب را جدا کرد
- Source lineage را بازسازی کرد
- duplicate inclusion را تشخیص داد
- version history را حفظ کرد
- Training/Evaluation linkage را بررسی کرد

Threshold یا Recovery Automation نهایی هنوز تصمیم نشده است.

## 18. Model Artifact Continuity

اگر Model Version در Production فعال است، Continuity آینده باید بتواند مشخص کند:

- active model version
- approved artifact reference
- configuration/version linkage
- rollback candidate در صورت تصویب
- last-known-good status
- deployment/promotion evidence

BC-021 نوع Artifact Store یا Model Registry فنی را تعیین نمی‌کند.

## 19. Model Rollback Boundary

Rollback با Backup Restore یکی نیست.

- **Backup Restore:** بازیابی داده/سیستم
- **Model Rollback:** بازگرداندن نسخه AI به نسخه قبلی مصوب

Rollback Rule و Authority همچنان در AI Governance باز است.

## 20. Communications During Major Outage

همسو با BC-017، باید برای اختلال گسترده در آینده تعیین شود:

- چه Actorهایی مطلع می‌شوند
- سالمند/سالمندیار چه پیامی می‌گیرند
- Providerها چگونه مطلع می‌شوند
- کارفرما چه زمانی مطلع می‌شود
- چه Channel جایگزینی معتبر است

هیچ Notification SLA یا Channel اضطراری در BC-021 تصویب نمی‌شود.

## 21. Manual / Offline Fallback — Open

فعالیت میدانی ممکن است در شرایط عدم اتصال یا خرابی سامانه ادامه داشته باشد، اما طرح اولیه Offline Mode نهایی تعریف نکرده است.

اگر Manual/Offline Fallback در آینده تصویب شود، باید حداقل مشخص کند:

- چه عملیات‌هایی مجازند
- چه داده‌ای می‌تواند موقتاً خارج از سیستم ثبت شود
- چه کسی مجاز است
- امنیت و محرمانگی چگونه حفظ می‌شود
- چه زمانی Data Re-entry انجام می‌شود
- Conflict resolution چگونه است
- Audit چگونه بازسازی می‌شود

## 22. Reconciliation After Recovery

پس از بازیابی، سیستم باید بتواند در آینده وضعیت عملیات انجام‌شده در زمان اختلال را Reconcile کند.

Candidate domains:

- contacts
- tasks
- referrals
- service updates
- incidents
- consent/authorization changes
- AI interactions
- dataset events

Rule نهایی Conflict Resolution هنوز باید تصمیم شود.

## 23. Security Continuity

پایداری نباید با دورزدن Security به‌دست آید.

در شرایط اختلال، اصول زیر باید حفظ شوند:

- access control
- least privilege
- confidentiality
- auditability
- incident logging
- credential protection

Emergency access یا Break-glass Rule هنوز تصمیم نشده است.

## 24. Backup Access Boundary

Backup نباید به‌دلیل ماهیت پشتیبان، از Data Governance خارج فرض شود.

Backupها نیز باید تحت قواعد:

- access
- retention
- confidentiality
- deletion/legal hold
- audit
- restore authorization

قرار گیرند.

## 25. Third-party / Provider Dependency

نسیم ممکن است برای ارائه خدمت به Providerها و سایر زیرساخت‌ها وابسته باشد.

Business Continuity آینده باید برای Failure وابستگی‌های بیرونی نیز پاسخ داشته باشد:

- provider unavailable
- communication provider unavailable
- infrastructure dependency outage
- external integration failure در صورت وجود

اما هیچ Vendor یا External Architecture در Business تعیین نمی‌شود.

## 26. Dependency Mapping — DRAFT BUSINESS NEED

برای هر Capability حیاتی باید در آینده Dependency Map وجود داشته باشد.

Candidate dependency types:

- people
- process
- system
- data
- AI/model
- dataset pipeline
- provider
- communication channel
- infrastructure

این Map تکنیکی نهایی نیست، بلکه نیاز Business برای Continuity Planning است.

## 27. Continuity Incident Governance

اختلال جدی باید با BC-012 همسو باشد.

باید بعداً مشخص شود:

- چه زمانی Outage تبدیل به Incident می‌شود
- Severity چگونه تعیین می‌شود
- Owner کیست
- Escalation چیست
- Communication چیست
- Closure Evidence چیست
- Post-incident review چگونه انجام می‌شود

## 28. Recovery Decision Authority

برای تصمیم‌های Recovery باید Owner مشخص شود، از جمله:

- declare incident
- activate continuity procedure
- restore backup
- switch/failover در صورت وجود
- suspend capability
- resume production
- accept residual risk

این Decision Rights در BC-013 باید نهایی شوند.

## 29. Disaster Recovery Exercise

طرح اولیه آزمون DR را صریحاً تعریف نمی‌کند، اما اگر Recovery باید قابل اتکا باشد، Business آینده باید Evidence of Rehearsal را تعیین کند.

موضوعات باز:

- exercise cadence
- scope
- participants
- restore test
- failover test در صورت وجود
- evidence
- remediation
- approval

هیچ Cadence یا Success Threshold در BC-021 تصویب نمی‌شود.

## 30. Recovery Evidence Package — DRAFT

پس از Incident یا Exercise، Evidence آینده می‌تواند شامل:

- incident/exercise scope
- affected capabilities
- start/end times
- data loss assessment
- restore evidence
- integrity checks
- unresolved issues
- AI/model status
- dataset lineage status
- security findings
- remediation
- approval to resume

باشد.

قالب نهایی هنوز تصمیم نشده است.

## 31. Reporting & Monitoring Link

همسو با BC-020، Management Reporting باید در آینده بتواند وضعیت Continuity را نمایش دهد.

Candidate dimensions:

- service availability
- backup health
- restore test status
- unresolved continuity incidents
- AI availability
- dataset pipeline continuity
- last recovery exercise

هیچ KPI/Threshold نهایی تصویب نشده است.

## 32. Recovery Does Not Equal Success

بازگشت سرویس به Online به‌تنهایی پایان Recovery نیست.

برای Closure باید در آینده بررسی شود:

- integrity
- completeness
- security
- workflow continuity
- AI/model validity
- dataset lineage validity
- stakeholder communication
- residual risks

## 33. Continuous Improvement

نتایج Outage، Recovery و DR Exercise باید بتوانند ورودی Improvement باشند:

- architecture improvement
- process change
- training update
- backup policy change
- incident rule change
- AI fallback improvement
- dataset pipeline improvement
- monitoring improvement

Change Approval همچنان باید Governance مصوب داشته باشد.

## 34. Explicit Non-Decisions

BC-021 موارد زیر را تصویب نمی‌کند:

- Availability درصدی
- RTO
- RPO
- Backup cadence
- Backup retention
- Backup technology
- Cloud/on-prem architecture
- Active-active / active-passive
- failover topology
- DR site
- offline mode
- emergency access rule
- restore authority
- DR exercise cadence
- AI fallback implementation
- model rollback threshold
- dataset replay implementation
- communication SLA during outage

## 35. Open Decisions Required to Accept BC-021

1. Service criticality classification
2. Continuity scope per capability
3. Minimum operations during outage
4. RTO/RPO
5. Backup scope/cadence/retention
6. Restore verification policy
7. Recovery integrity checks
8. AI outage/fallback policy
9. Dataset recovery/replay policy
10. Model artifact continuity
11. Model rollback authority/rule
12. Manual/offline fallback
13. Reconciliation/conflict rule
14. Outage communication policy
15. Security/break-glass policy
16. Dependency map ownership
17. Continuity incident thresholds
18. Recovery decision authority
19. DR exercise policy
20. Recovery evidence/closure rule

## 36. Downstream Constraints

تا پیش از Accepted شدن BC-021:

- Technical نباید RTO/RPO یا Availability Target اختراع کند.
- Backup وجودش نباید معادل Recovery اثبات‌شده تلقی شود.
- Recovery نباید Data Governance یا Access Control را دور بزند.
- AI failure نباید باعث جعل خروجی یا تصمیم شود.
- Dataset pipeline failure نباید Operational Record را تغییر دهد.
- Dataset/Model Version و Lineage باید در Recovery قابل حفظ/بررسی باشند.
- Resume Production باید از Recovery Evidence و Authority مصوب تبعیت کند.
