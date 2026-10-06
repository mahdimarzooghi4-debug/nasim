# BC-023 — Integration, External Systems & Interoperability Governance

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-007 + BC-008 + BC-013 + BC-014 + BC-021 + BC-022
- **Depends on:** BC-003, BC-005, BC-006, BC-007, BC-008, BC-012, BC-013, BC-014, BC-017, BC-020, BC-021, BC-022

> این سند چارچوب کسب‌وکاری Integration، تبادل داده و تعامل نسیم با سامانه‌ها و سازمان‌های بیرونی را تعریف می‌کند. طرح اولیه اتصال نسیم به ظرفیت‌های سلامت، رفاه و شرکای تخصصی را قطعی می‌داند، اما API، استاندارد تبادل، Sync Model، Master Data، قرارداد فنی، Protocol، Message Broker یا Vendor مشخصی را تعیین نمی‌کند؛ بنابراین هیچ معماری فنی یا Interface نهایی در این سند اختراع نمی‌شود.

## 1. Source-confirmed Integration Direction

طرح مبنا، نسیم را اپراتور شبکه‌ای می‌داند که ظرفیت‌های موجود در حوزه‌های:

- سلامت
- رفاه
- اشتغال
- خدمات اجتماعی
- خدمات تخصصی شرکا

را به یکدیگر متصل می‌کند.

همچنین در لایه سلامت، منبع صریحاً به اتصال نسیم به «ترنم» و سایر ظرفیت‌های درمانی و مراقبتی اشاره می‌کند.

بنابراین Integration با سامانه‌ها و سازمان‌های بیرونی بخشی از مدل عملیاتی نسیم است.

## 2. Integration ≠ Data Ownership

اتصال به یک سامانه خارجی به‌معنی انتقال مالکیت یا حاکمیت همه داده‌ها نیست.

اصل:

`Integration Access ≠ Data Ownership`

برای هر Integration باید بعداً مشخص شود:

- چه داده‌ای متعلق به کدام Actor/Organization است
- کدام داده Source of Record است
- چه کسی حق اصلاح دارد
- چه کسی فقط Read دارد
- چه داده‌ای مشتق می‌شود
- چه داده‌ای قابل نگهداری محلی است
- چه داده‌ای فقط موقتاً قابل استفاده است

## 3. Integration Domains — DRAFT FRAME

Candidate integration domains شامل:

- Employer systems
- Health-service systems
- Welfare-service systems
- Provider systems
- Identity/eligibility systems
- Communication services
- Payment/financial systems در صورت تصویب آینده
- Reporting/exchange interfaces
- Contract/partner systems
- Other public/private partner platforms

این فهرست به معنی وجود یا تصویب هیچ سامانه خاصی نیست، به‌جز مواردی که منبع صریحاً نام برده است.

## 4. Tarannom / Named Health Connection Boundary

طرح اولیه «ترنم» را به‌عنوان یکی از ظرفیت‌های سلامت که خدمات از طریق اتصال به آن و سایر ظرفیت‌های درمانی/مراقبتی ارائه می‌شوند، ذکر می‌کند.

BC-023 فقط وجود این جهت اتصال را ثبت می‌کند و درباره موارد زیر تصمیمی نمی‌گیرد:

- مالک/اپراتور فنی ترنم
- API availability
- Authentication method
- data schema
- service catalog alignment
- write-back
- real-time sync
- SLA
- legal data-sharing terms

این موارد باید با Evidence واقعی سامانه مقصد بررسی شوند.

## 5. Integration Purpose

هر Integration باید Purpose مشخص داشته باشد.

Candidate purposes:

- eligibility verification
- referral delivery
- provider/service discovery
- appointment/service coordination
- service-result retrieval
- identity verification
- status synchronization
- reporting
- quality evidence
- consent/authorization verification

هیچ Purpose نباید صرف اتصال فنی، خودکار به همه Purposeهای دیگر تعمیم داده شود.

## 6. Data-sharing Contract per Integration

برای هر Integration باید Business Contract مشخص کند:

- source organization/system
- destination organization/system
- purpose
- data classes
- direction
- trigger
- frequency/cadence
- legal/consent basis
- access scope
- retention
- correction responsibility
- audit
- error handling
- termination/offboarding

این Contract می‌تواند بعداً مبنای Technical Interface Contract شود.

## 7. Source of Truth / System of Record

برای هر Data Element باید مشخص شود System of Record کدام سامانه است.

Candidate cases:

- elder identity
- eligibility
- contact information
- need/referral
- provider status
- service result
- consent
- payment/settlement
- outcome

نسیم نباید بدون Rule مصوب خود را Master همه داده‌های بیرونی فرض کند.

## 8. Data Provenance

هر داده ورودی از بیرون باید Provenance خود را حفظ کند.

حداقل باید در آینده قابل تشخیص باشد:

- source system/organization
- source record/reference
- time received
- version/change indicator در صورت وجود
- processing/transformation
- verification status
- destination usage

Provenance برای Audit، Quality و AI Learning حیاتی است.

## 9. External Data ≠ Trusted Fact by Default

داده‌ای که از Integration دریافت می‌شود ممکن است:

- معتبر باشد
- ناقص باشد
- قدیمی باشد
- متعارض باشد
- نیازمند Human Review باشد

اصل:

`External Data Received ≠ Automatically Accepted Truth`

Rule پذیرش/تطبیق داده باید برای هر Domain تعیین شود.

## 10. Data Reconciliation

اگر داده نسیم و سامانه بیرونی با هم ناسازگار باشند، باید Rule آینده مشخص کند:

- کدام Source اولویت دارد
- چه کسی Review می‌کند
- آیا داده Merge می‌شود
- آیا Conflict ثبت می‌شود
- آیا عملیات متوقف می‌شود
- چگونه Audit حفظ می‌شود

Technical نباید Last-write-wins را بدون Business Decision پیش‌فرض قرار دهد.

## 11. Sync Model — Open

برای هر Integration باید بعداً تعیین شود:

- real-time
- near-real-time
- scheduled batch
- manual exchange
- event-driven
- on-demand

هیچ Sync Model نهایی در BC-023 تصویب نمی‌شود.

## 12. One-way vs Two-way Exchange

هر Integration باید جهت تبادل مشخص داشته باشد:

- inbound only
- outbound only
- bidirectional

دوطرفه بودن نباید بدون Contract صریح فرض شود.

## 13. Referral Integration

اگر Referral به Provider/System خارجی ارسال شود باید Business آینده مشخص کند:

- چه داده‌ای ارسال می‌شود
- چه زمانی Referral معتبر است
- چه acknowledgment لازم است
- چه statusهایی از خارج قابل قبول‌اند
- چه کسی status را نهایی می‌کند
- عدم پاسخ چگونه مدیریت می‌شود
- duplicate referral چگونه جلوگیری می‌شود
- cancellation/re-route چگونه انجام می‌شود

State Machine هنوز در BC-003 باز است.

## 14. External Service Result

Provider/System خارجی ممکن است Result یا Completion Evidence برگرداند.

اصل:

`External Service Result ≠ Final Need Resolution`

Result باید Provenance داشته باشد و ممکن است برای Outcome/Reassessment نیازمند Human Review یا Follow-up باشد.

## 15. Identity / Eligibility Integration Boundary

اگر در آینده برای هویت یا Eligibility از سامانه بیرونی استفاده شود باید مشخص شود:

- چه Attributeهایی قابل اعتمادند
- Verification cadence چیست
- stale data چگونه مدیریت می‌شود
- mismatch چه اثری دارد
- outage چه fallbackی دارد
- manual override authority چیست

هیچ External Identity Source در BC-023 تصویب نمی‌شود.

## 16. Provider Registry Synchronization

اگر Provider Registry با Registry بیرونی Sync شود، باید مشخص شود:

- کدام سیستم مالک status است
- credential/qualification source چیست
- active/inactive status از کجا می‌آید
- local review لازم است یا خیر
- suspension در یک سیستم چه اثری بر دیگری دارد

نسیم نباید صرف external active status، Provider را خودکار Operationally Approved فرض کند مگر Rule مصوب وجود داشته باشد.

## 17. Integration Security

همسو با BC-022، Integration باید تحت Access Governance باشد.

برای هر Integration باید در آینده مشخص شود:

- system identity
- authentication
- authorization
- least privilege
- data scope
- credential ownership
- rotation/revocation
- audit
- monitoring

هیچ API Key، OAuth، mTLS یا Protocol خاصی در Business تصویب نمی‌شود.

## 18. Organization Boundary

هر سازمان شریک باید از نظر Access Boundary مستقل تلقی شود.

اصل:

`Partner membership ≠ cross-organization unrestricted access`

Data Sharing باید به Organization، Service، Purpose و Contract مرتبط باشد.

## 19. Tenant / Organization Context — Business Need

اگر چند کارفرما، Provider یا سازمان هم‌زمان در نسیم فعالیت کنند، Technical آینده باید بتواند مرز Organization Context را حفظ کند.

BC-023 مدل Multi-tenancy فنی را تعیین نمی‌کند، اما Business Boundary باید مانع نشت داده بین سازمان‌های نامرتبط شود.

## 20. Integration Audit

برای تبادل‌های مهم باید در آینده قابل ردیابی باشد:

- source
- destination
- operation
- data category
- reference/correlation
- time
- status
- retries
- actor/process
- consent/authority context
- error/result

Audit باید Human/System/Integration Process را از هم تفکیک کند.

## 21. Integration Failure

Candidate failure modes:

- destination unavailable
- authentication failure
- timeout
- malformed data
- schema mismatch
- duplicate event
- delayed event
- stale data
- partial update
- rejected request
- inconsistent status

Severity و Retry/Recovery Rule هنوز باید تعیین شوند.

## 22. Failure ≠ Silent Data Loss

اصل:

`Integration Failure ≠ Silent Data Loss`

اگر تبادل ناموفق باشد، سیستم باید در آینده بتواند Failure را ثبت، قابل مشاهده و قابل پیگیری نگه دارد.

Technical Details در مرحله Technical تعیین می‌شود.

## 23. Idempotency / Duplicate Protection — Business Requirement

برای عملیات حساس مانند:

- Referral creation
- Service result
- consent update
- payment event در صورت وجود
- dataset-related import

باید از تکرار ناخواسته اثر کسب‌وکاری جلوگیری شود.

روش فنی Idempotency در Technical تعیین می‌شود.

## 24. Ordering / Late Data

داده بیرونی ممکن است با تأخیر یا خارج از ترتیب برسد.

Business آینده باید تعیین کند:

- timestamp/source precedence
- stale-event handling
- correction handling
- replay handling
- conflict with newer local data

نباید صرف زمان دریافت، داده قدیمی جای داده جدید را بگیرد.

## 25. Schema / Contract Versioning

External Interface باید Versionable باشد.

در آینده باید مشخص شود:

- interface version
- effective date
- backward compatibility
- migration period
- deprecation
- contract owner
- change approval

Technical نباید Integration Contract را Hard-code و بدون Versioning طراحی کند.

## 26. External Change Management

تغییر در سامانه شریک ممکن است عملیات نسیم را تحت تأثیر قرار دهد.

برای تغییرات Integration باید آینده پاسخ داشته باشد:

- notification process
- compatibility review
- testing
- approval
- rollout
- rollback
- incident handling

هیچ Change SLA فعلاً تصویب نشده است.

## 27. Integration Testing

پیش از Production، Integration باید Evidence قابل اتکا داشته باشد.

Candidate test domains:

- authentication/access
- valid request/response
- invalid data
- duplicate handling
- timeout/retry
- permission boundary
- privacy/data minimization
- reconciliation
- audit
- outage/recovery

Test suite فنی بعداً تعیین می‌شود.

## 28. External Dependency Continuity

همسو با BC-021، Availability نسیم ممکن است به سیستم بیرونی وابسته باشد.

برای هر Dependency باید بعداً مشخص شود:

- criticality
- outage effect
- fallback
- queue/retry
- manual process
- recovery reconciliation
- stakeholder notification

هیچ Vendor SLA یا Fallback Architecture در BC-023 تصویب نمی‌شود.

## 29. Data Minimization for Integrations

نسیم نباید بیش از Data لازم برای Purpose مصوب ارسال یا دریافت کند.

اصل:

`Integration convenience ≠ permission for broad data exchange`

برای هر Interface باید Data Fields و Purpose به‌صورت صریح تصویب شوند.

## 30. Consent / Legal Basis

هر تبادل داده باید با BC-014 همسو باشد.

برای هر Integration باید در آینده روشن شود:

- legal basis / consent
- authorized recipient
- purpose
- retention
- onward sharing
- withdrawal impact
- incident notification

وجود Contract فنی جای Legal/Data-sharing Contract را نمی‌گیرد.

## 31. AI Access to External Data

AI داخلی ممکن است در Use Caseهای آینده به External Data دسترسی داشته باشد، اما این دسترسی باید صریحاً تصویب شود.

برای هر Use Case باید مشخص شود:

- external source
- data classes
- runtime purpose
- freshness
- trust/verification
- sensitive-data rule
- human-review boundary
- audit

AI نباید به‌صرف وجود Integration به همه داده‌های بیرونی دسترسی داشته باشد.

## 32. External Data and Training Eligibility

اصل:

`External Data Available ≠ Training Eligible`

حتی اگر داده از Provider یا سامانه بیرونی برای عملیات مجاز باشد، ورود آن به Dataset AI نیازمند Training Eligibility Rule جداگانه است.

باید مشخص شود:

- data ownership/licensing
- consent/legal basis
- provenance
- quality
- allowed training purpose
- exclusion
- retention
- dataset lineage

## 33. External AI Services — Boundary

D-0004 فقط AI داخلی نسیم را الزام می‌کند.

BC-023 هیچ سرویس AI خارجی، API مدل بیرونی یا Vendor AI را تصویب نمی‌کند.

اگر در آینده استفاده از سرویس بیرونی مطرح شود، باید Decision مستقل درباره:

- data transfer
- privacy
- security
- legal basis
- model/runtime governance
- availability
- vendor risk

ثبت شود.

## 34. Dataset Pipeline Imports

اگر داده بیرونی در آینده منبع Dataset شود، Pipeline باید:

- source identity را حفظ کند
- source version/time را ثبت کند
- eligibility را جداگانه اجرا کند
- transformation/curation را ثبت کند
- duplicate/replay را کنترل کند
- lineage را حفظ کند

Import مستقیم به Training Dataset بدون Eligibility/Curation مجاز نیست.

## 35. Integration Registry — DRAFT BUSINESS NEED

برای مدیریت مقیاس، نسیم باید بتواند Registry از Integrationها داشته باشد.

Candidate fields:

- integration ID/name
- partner/system
- business purpose
- data direction
- data classes
- owner
- legal/data-sharing contract reference
- interface version
- environment/status
- criticality
- monitoring/incident contact
- effective dates

ساختار فنی Registry بعداً تعیین می‌شود.

## 36. Ownership & Accountability

برای هر Integration باید Owner انسانی/سازمانی مشخص باشد.

حداقل Ownership domains:

- business owner
- data owner
- technical owner
- security reviewer
- legal/privacy reviewer
- operational support owner

وجود این Functionها به معنی ایجاد Unit/Committee جدید نیست.

## 37. Decommissioning

پایان Integration باید Governance داشته باشد.

باید تعیین شود:

- stop date
- pending messages/data
- access revocation
- credential revocation
- retained data
- delete/archive
- audit preservation
- impact on active referrals/services
- replacement/fallback

قطع یک Interface نباید History عملیاتی را پاک کند.

## 38. Reporting & Monitoring

همسو با BC-020، Integration Governance Reporting آینده می‌تواند شامل:

- integration health
- failure/retry
- data freshness
- reconciliation backlog
- security events
- contract/version status
- unresolved incidents

باشد.

هیچ KPI یا Threshold نهایی تصویب نشده است.

## 39. Explicit Non-Decisions

BC-023 موارد زیر را تصویب نمی‌کند:

- API style
- REST/GraphQL/gRPC
- message broker
- event bus
- integration platform
- ESB/iPaaS
- FHIR/HL7 یا هر استاندارد تخصصی دیگر
- sync cadence
- retry count
- timeout
- schema
- endpoint
- OAuth/mTLS/API key
- master-data technology
- external identity provider
- payment integration
- external AI API
- data residency
- vendor SLA
- automatic conflict resolution

## 40. Open Decisions Required to Accept BC-023

1. Integration inventory
2. Partner/system inventory
3. Business purpose per integration
4. Data-sharing contract per integration
5. Source-of-truth matrix
6. Data provenance requirements
7. Reconciliation rules
8. Sync model per integration
9. One-way/two-way direction
10. Referral integration contract
11. Service-result contract
12. Identity/eligibility integration decision
13. Provider Registry synchronization
14. Security/authentication requirements
15. Organization/tenant boundaries
16. Failure/retry/replay policy
17. Idempotency requirements
18. Schema/interface versioning
19. External change-management process
20. Integration testing gate
21. Continuity/fallback rules
22. Consent/legal basis per exchange
23. AI external-data access rules
24. External-data training eligibility
25. Integration Registry ownership
26. Decommissioning policy

## 41. Downstream Constraints

تا پیش از Accepted شدن BC-023:

- Technical نباید API، Protocol یا Integration Platform نهایی را اختراع کند.
- دریافت داده بیرونی نباید به‌معنی پذیرفتن خودکار آن به‌عنوان حقیقت رسمی باشد.
- Last-write-wins نباید Conflict Rule پیش‌فرض باشد.
- Provider/System خارجی نباید Full-record Access پیش‌فرض داشته باشد.
- External Data نباید بدون Training Eligibility وارد Dataset شود.
- AI نباید به‌صورت پیش‌فرض به همه داده‌های Integration دسترسی داشته باشد.
- هر Integration باید قابلیت Versioning، Audit، Failure Visibility و Organization Boundary داشته باشد.
