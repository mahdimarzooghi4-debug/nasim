# BC-020 — Reporting, Management Intelligence & Decision Support

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-007 + BC-010 + BC-013 + BC-019
- **Depends on:** BC-005, BC-007, BC-009, BC-010, BC-011, BC-012, BC-013, BC-014, BC-015, BC-016, BC-018, BC-019

> این سند چارچوب کسب‌وکاری گزارش‌دهی، داشبوردها، تحلیل مدیریتی و Decision Support را تعریف می‌کند. منبع اولیه «گزارش‌های مدیریتی»، «تحلیل داده‌ها و تصمیم‌سازی» و «نظام ارزیابی» را قطعی می‌داند، اما Dashboard نهایی، KPI Formula، سطح دسترسی گزارش، Alert Rule، گزارش کارفرما یا نحوه استفاده AI در تصمیم‌سازی را تعیین نکرده است؛ بنابراین این موارد در این سند اختراع نمی‌شوند.

## 1. Source-confirmed Reporting Capability

طرح مبنا برای سامانه نسیم این قابلیت‌ها را صریحاً ذکر می‌کند:

- مدیریت اطلاعات سالمندان
- مدیریت فعالیت سالمندیاران
- ثبت خدمات
- مدیریت ارجاعات
- پایش کیفیت خدمات
- گزارش‌های مدیریتی
- تحلیل داده‌ها
- پشتیبانی از تصمیم‌سازی

بنابراین Reporting و Management Intelligence بخشی از Capability اصلی نسیم هستند، نه قابلیت جانبی پس از استقرار.

## 2. Reporting ≠ Decision

گزارش، Dashboard یا تحلیل نباید به‌خودی‌خود Decision نهایی تلقی شود.

اصل:

`Data → Metric/Report → Analysis → Human/Governed Decision`

مگر در آینده برای یک Rule محدود و مشخص Automation صریحاً تصویب شود.

## 3. Reporting Layers — DRAFT FRAME

برای نیازهای مختلف، Reporting آینده باید بتواند حداقل در این سطوح تفکیک شود:

### A. Operational
برای عملیات روزمره، مانند:
- workload
- open needs
- referrals
- follow-ups
- service delivery
- overdue work
- incidents

### B. Supervisory
برای مدیریت تیم/منطقه، مانند:
- worker workload
- unresolved cases
- quality findings
- escalations
- training/readiness
- provider issues

### C. Management
برای مدیریت شبکه، مانند:
- coverage
- quality
- satisfaction
- workforce
- provider network
- operational performance
- risk
- economic performance

### D. Executive / Governance
برای تصمیم‌های کلان، مانند:
- strategic KPIs
- scale readiness
- risk profile
- financial sustainability
- social/economic impact
- AI governance
- learning-system health

این تقسیم‌بندی Frame است و Role/Permission نهایی نیست.

## 4. Four Evaluation Views — Source-confirmed

همسو با طرح اولیه و BC-010، Management Intelligence باید بتواند چهار سطح ارزیابی را پوشش دهد:

- Operational
- Managerial
- Economic
- Social

گزارش‌دهی نباید فقط بر Volume یا Activity متمرکز باشد.

## 5. KPI Families — Source-confirmed

حداقل خانواده‌های KPI سطح بالا:

- کیفیت خدمات
- رضایت سالمندان و خانواده‌ها
- توسعه سرمایه انسانی
- پایداری اقتصادی و توسعه بازار

KPIهای دقیق، Formula، Target و Threshold هنوز در BC-010 باز هستند.

## 6. Metric Definition Contract

هر Metric/KPI آینده باید Business Definition قابل نسخه‌بندی داشته باشد.

حداقل اطلاعات مورد نیاز:

- metric name
- business definition
- numerator
- denominator
- inclusion rules
- exclusion rules
- source data
- aggregation level
- time window
- refresh cadence
- owner
- version
- target/threshold در صورت تصویب
- data-quality rule

Technical نباید Formula را از نام KPI حدس بزند.

## 7. Metric Versioning

اگر تعریف KPI تغییر کند، نتایج تاریخی نباید بی‌صدا با Formula جدید بازنویسی شوند.

برای هر گزارش/نقطه زمانی باید بتوان مشخص کرد:

- metric version
- data period
- source snapshot/version
- calculation time
- relevant taxonomy/catalog versions در صورت نیاز

## 8. Operational Reports

Candidate operational views ممکن است شامل این موارد باشند:

- سالمندان فعال
- Needهای باز
- Referralهای باز
- Follow-upهای موعددار/انجام‌نشده
- Service delivery activity
- Satisfaction pending
- Incident/escalation
- Workload
- Provider availability/capacity در صورت تعریف

اینها Candidate هستند و KPI یا Dashboard نهایی محسوب نمی‌شوند.

## 9. Workforce Reporting

همسو با BC-015، گزارش‌های سرمایه انسانی ممکن است حوزه‌های زیر را پوشش دهند:

- activation/readiness
- training completion
- workload
- follow-up quality
- satisfaction evidence
- data-quality evidence
- incident history
- progression/career data

اما هیچ Ranking یا Composite Score نهایی تصویب نشده است.

## 10. Provider Reporting

همسو با BC-008، گزارش Provider ممکن است ابعادی مانند این داشته باشد:

- referral volume
- response
- completion
- availability/capacity
- quality
- satisfaction
- complaints/incidents
- data completeness

Provider ranking یا «بهترین Provider» بدون Rule مصوب مجاز نیست.

## 11. Elder-level View vs Aggregate Reporting

Business باید میان این دو تفکیک کند:

- **Case-level / Elder-level reporting**
- **Aggregate management reporting**

هر Actor نباید صرفاً به دلیل دسترسی به Aggregate Report، حق Drill-down به پرونده فردی داشته باشد.

اصل:

`Aggregate visibility ≠ individual-record access`

## 12. Employer Reporting Boundary

کارفرما طبق منبع نقش نظارتی دارد، اما سطح گزارش‌دهی او هنوز مشخص نشده است.

باید تصمیم شود:

- چه گزارش‌هایی دریافت می‌کند
- چه سطحی از Aggregation
- آیا Drill-down مجاز است
- آیا داده فردی نمایش داده می‌شود
- چه داده‌ای Mask/Exclude می‌شود
- گزارش با چه Cadence ارائه می‌شود
- چه Evidence برای نظارت کافی است

تا آن زمان، کارفرما دسترسی پیش‌فرض به پرونده فردی ندارد.

## 13. Data Minimization in Reporting

گزارش باید فقط داده لازم برای Purpose خود را نمایش دهد.

مثلاً گزارش مدیریتی شبکه لزوماً نباید اطلاعات هویتی سالمند را نمایش دهد.

قواعد Masking، Aggregation و Suppression هنوز باید در Data/Legal Contract نهایی شوند.

## 14. Longitudinal Reporting

همسو با BC-019، Reporting باید بتواند تغییر را در طول زمان نمایش دهد بدون اینکه تاریخچه را overwrite کند.

Candidate views:

- trend of needs
- referral/service history
- reassessment trend
- observed outcomes
- satisfaction trend
- quality trend

اما Interpretation خودکار اثر علّی مجاز نیست.

## 15. Outcome Reporting Boundary

اصل:

`Observed Outcome ≠ Proven Impact ≠ Proven Causality`

Dashboard نباید صرف هم‌زمانی Service و تغییر Outcome، Service را علت قطعی تغییر معرفی کند.

اگر Causal Analysis نیاز باشد، Methodology جداگانه لازم است.

## 16. Data Quality Visibility

از آنجا که تصمیم مدیریتی بر داده متکی است، گزارش باید در آینده بتواند کیفیت داده را نیز قابل مشاهده کند.

Candidate dimensions:

- completeness
- timeliness
- provenance
- consistency
- missingness
- review status
- definition/version coverage

این موارد بدون Threshold مصوب نباید به Pass/Fail قطعی تبدیل شوند.

## 17. Reporting Freshness

هر گزارش باید در آینده مشخص کند داده آن مربوط به چه زمان یا Snapshotی است.

مفاهیم لازم:

- data period
- last refresh
- event-time vs processing-time در صورت نیاز
- late-arriving data handling
- correction handling

Cadence نهایی هنوز تصمیم نشده است.

## 18. Correction & Restatement

اگر داده منبع تصحیح شود یا KPI Definition تغییر کند، Business آینده باید مشخص کند:

- گزارش تاریخی Restate می‌شود یا خیر
- نسخه قبلی حفظ می‌شود یا خیر
- دلیل تغییر ثبت می‌شود یا خیر
- چه Actorهایی مطلع می‌شوند

Technical نباید Historical Reporting را silent overwrite کند.

## 19. Alerts ≠ Reports

Alert یک Trigger عملیاتی/مدیریتی است و با Report فرق دارد.

Candidate alert domains:

- overdue follow-up
- capacity problem
- quality issue
- incident
- missing data
- AI incident
- dataset pipeline failure
- KPI threshold breach در صورت تعریف

Alert Rule و Threshold هیچ‌کدام در BC-020 تصویب نمی‌شوند.

## 20. Decision Support

طرح اولیه «تحلیل داده‌ها و تصمیم‌سازی» را قابلیت سامانه می‌داند.

Decision Support می‌تواند شامل:

- جمع‌بندی Evidence
- مقایسه وضعیت با دوره قبل
- نمایش روند
- برجسته‌سازی Exception
- تحلیل سناریو در صورت تعریف
- آماده‌سازی شواهد برای Review

باشد.

اما سامانه نباید بدون Rule مصوب Decision Right انسانی را تصاحب کند.

## 21. Day-one AI in Management Intelligence

بر اساس D-0004 و D-0005، AI از روز اول می‌تواند در Use Caseهای مصوب به Decision Support کمک کند.

Candidate uses:

- خلاصه‌سازی گزارش
- توضیح KPI
- کشف الگو/Exception برای بررسی
- پاسخ به سؤال مدیریتی بر پایه داده مجاز
- مقایسه دوره‌ها
- Draft کردن Management Brief
- برجسته‌سازی Data Quality issue
- خلاصه‌سازی Incident/Risk evidence

اینها Use Case نهایی نیستند.

## 22. AI Analysis ≠ Official Management Decision

اصل:

`AI Analysis ≠ Approved Decision`

AI نباید:

- GO/NO-GO را نهایی کند
- Risk Acceptance را نهایی کند
- Provider suspension را نهایی کند
- Model Promotion را نهایی کند
- KPI Definition را تغییر دهد
- Budget/Pricing را نهایی کند

مگر تصمیم صریح آینده خلاف آن را برای یک Use Case محدود مشخص کند.

## 23. AI Provenance in Reports

اگر Report یا Brief از AI استفاده کند باید در آینده امکان ردیابی این موارد وجود داشته باشد:

- AI involvement
- model/version
- data scope/snapshot
- generation time
- human reviewer در صورت نیاز
- accepted/edited/rejected status

AI-generated narrative نباید با Raw Metric یا Human-approved conclusion مخلوط شود.

## 24. AI Hallucination / Unsupported Claim Boundary

AI نباید در گزارش مدیریتی عدد، KPI، Trend یا علت را بدون داده پشتیبان تولید کند.

هر Claim داده‌ای باید بتواند به Source Evidence یا Metric Definition قابل ردیابی متصل شود.

در نبود داده کافی، AI باید عدم کفایت شواهد را نشان دهد، نه اینکه عدد یا نتیجه اختراع کند.

## 25. Reporting Access Control

Business آینده باید تعیین کند چه Roleهایی به چه Reportهایی دسترسی دارند.

حداقل ابعاد تصمیم:

- report type
- aggregation level
- geography
- organization
- individual drill-down
- sensitive dimensions
- export permission
- sharing permission

RBAC نهایی هنوز در BC-013/BC-014 باز است.

## 26. Export & External Sharing

منبع اولیه Export یا Sharing Format تعریف نکرده است.

اگر در آینده گزارش قابل Export باشد، باید Rule تعیین شود برای:

- format
- data masking
- watermark/classification در صورت نیاز
- recipient
- expiration/access
- audit
- onward sharing

هیچ Export Policy نهایی تصویب نشده است.

## 27. Reporting for Pilot & Scale Gate

همسو با BC-011، Reporting باید بتواند Evidence Package پایلوت و Scale Gate را پشتیبانی کند.

Candidate evidence domains:

- operations
- quality
- satisfaction
- workforce
- providers
- economics
- data governance
- AI quality
- dataset lifecycle
- risk/incidents

Dashboard نباید جای Evidence Package و Decision Record را بگیرد.

## 28. AI & Dataset Lifecycle Reporting

چون Datasetها به‌صورت خودکار و مستمر نسخه‌بندی می‌شوند، Governance Reporting باید بتواند حداقل این موارد را در آینده نشان دهد:

- dataset version
- source period/window
- eligibility-rule version
- curation/preparation status
- lineage completeness
- training/evaluation linkage
- model/version linkage
- pipeline incidents

اعداد/Thresholdهای سلامت Pipeline هنوز تصمیم نشده‌اند.

## 29. Model Monitoring Reporting

برای AI داخلی، Management/Governance Reporting باید بتواند در آینده ابعادی مانند این را پوشش دهد:

- active model/version
- availability
- use-case usage
- human accept/reject/edit
- incidents
- evaluation evidence
- rollback events
- dataset/model lineage

این فهرست Dashboard نهایی نیست.

## 30. Learning Loop Feedback

طرح اولیه بر «یادگیری سازمانی» تأکید دارد و D-0005 نیز Learning AI را مستمر کرده است.

بنابراین Reporting باید بتواند دو Loop متفاوت را پشتیبانی کند:

1. **Organizational Learning**
   - evaluation
   - feedback
   - operational analysis
   - process/service improvement

2. **AI Learning**
   - eligible data
   - versioned datasets
   - training/evaluation
   - governed model lifecycle

این دو Loop مرتبط‌اند اما یکی نیستند.

## 31. Report Definition Governance

هر Report رسمی آینده باید حداقل Owner و Purpose مشخص داشته باشد.

Candidate fields:

- report name
- purpose
- audience
- source metrics
- filters
- aggregation
- refresh cadence
- access rule
- export rule
- version
- owner
- approver

ساختار نهایی هنوز تصمیم نشده است.

## 32. Explicit Non-Decisions

BC-020 موارد زیر را تصویب نمی‌کند:

- Dashboard UI نهایی
- BI tool
- Data warehouse/lake
- KPI Formula
- KPI Target
- Alert Threshold
- Employer drill-down access
- Export format
- Report cadence
- Ranking formula
- Predictive model
- Forecasting method
- Automated management decision
- AI autonomous decision
- AI-generated causal explanation
- AI-based provider/worker ranking

## 33. Open Decisions Required to Accept BC-020

1. Report catalog
2. Audience/role matrix
3. Employer reporting boundary
4. KPI/metric definitions
5. Metric versioning policy
6. Dashboard hierarchy
7. Drill-down rules
8. Data-minimization/masking rules
9. Report refresh cadence
10. Correction/restatement policy
11. Alert catalog
12. Alert thresholds
13. Export/sharing policy
14. Pilot/scale evidence reports
15. AI decision-support use cases
16. AI provenance requirements
17. AI-report human-review rules
18. Dataset/AI governance reports
19. Management intelligence ownership
20. Report-definition approval process

## 34. Downstream Constraints

تا پیش از Accepted شدن BC-020:

- Technical نباید BI Tool یا Data Platform نهایی را از Business Contract استنتاج کند.
- Dashboard نباید KPI Formula یا Target اختراعی داشته باشد.
- Employer نباید Drill-down فردی پیش‌فرض داشته باشد.
- AI-generated insight نباید به‌عنوان Decision یا Fact بدون Evidence نمایش داده شود.
- Historical reports/metrics باید قابلیت Versioning/Restatement کنترل‌شده داشته باشند.
- Dataset/Model Reporting باید Lineage را حفظ کند.
- Reporting و Decision Rights باید جدا بمانند.
