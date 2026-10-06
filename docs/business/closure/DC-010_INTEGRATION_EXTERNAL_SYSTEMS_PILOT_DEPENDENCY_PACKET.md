# DC-010 — Integration, External Systems & Pilot Dependency Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + BC-008 + BC-021 + BC-023
- **Purpose:** بستن مرزهای Integration، External Data Trust، Source of Truth، Pilot Dependency و Failure/Fallback بدون اختراع API، Protocol، Sync Technology یا Vendor Contract.

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند. طرح اولیه اتصال نسیم به ظرفیت‌های بیرونی را جزء مدل شبکه می‌داند و در حوزه سلامت نام «ترنم» را صریحاً ذکر می‌کند، اما Interface، API، Data Contract، SLA یا روش فنی Integration را تعیین نمی‌کند.

## 1. Source-confirmed integration direction

طرح مبنا نسیم را برای کنار هم قرار دادن ظرفیت‌های:
- مددکاری و حمایت
- اشتغال
- سلامت
- خدمات اجتماعی
- شرکای تخصصی

طراحی می‌کند.

در لایه سلامت نیز صریحاً بیان می‌شود که خدمات از طریق اتصال به **ترنم** و سایر ظرفیت‌های درمانی/مراقبتی ارائه خواهند شد.

بنابراین Integration با سازمان‌ها/سامانه‌های بیرونی بخشی از Business Model است، ولی فهرست اجرایی Integrationهای Pilot هنوز تعیین نشده است.

## 2. Candidate D-0061 — External integration is a governed business capability

- **تصمیم پیشنهادی:** Integration با سامانه‌ها/سازمان‌های بیرونی فقط برای Purpose مصوب و در چارچوب Data, Access, Legal و Operational Governance انجام می‌شود.
- **Boundary:** اتصال فنی به‌تنهایی Data Access یا Business Authority گسترده ایجاد نمی‌کند.

**Assessment:** source-aligned; recommended for acceptance.

## 3. Candidate D-0062 — Tarannom is a source-confirmed integration direction, not a technical contract

- **تصمیم پیشنهادی:** «ترنم» یک جهت اتصال Source-confirmed در لایه سلامت است، اما API، Auth، Data Schema، Write-back، Sync Model، SLA و Legal Data-sharing آن تا دریافت Evidence واقعی از سامانه مقصد باز می‌ماند.

**Assessment:** directly source-supported; recommended for acceptance.

## 4. Pilot integration inventory — blocking

پیش از Technical باید برای Pilot مشخص شود هر Integration در یکی از این وضعیت‌هاست:

- **MANDATORY FOR PILOT**
- **OPTIONAL FOR PILOT**
- **EXPLICITLY DEFERRED**

برای هر مورد باید حداقل مشخص باشد:
- partner/system
- business purpose
- direction
- required data classes
- operational dependency
- legal/data-sharing requirement
- outage effect
- owner

Unknown بودن Integration نباید به‌صورت ضمنی Mandatory یا Deferred فرض شود.

## 5. Candidate D-0063 — Integration access does not transfer data ownership

- **تصمیم پیشنهادی:** دسترسی Integration به داده، مالکیت یا حاکمیت داده را به‌صورت خودکار منتقل نمی‌کند.

`Integration Access ≠ Data Ownership`

برای هر Data Element باید Source/Owner و Correction Authority مشخص باشد.

**Assessment:** recommended for acceptance.

## 6. Source of Truth / System of Record — blocking

برای Data Elementهای مهم Pilot باید مشخص شود Source of Record چیست، از جمله در صورت استفاده:
- identity
- eligibility
- contact
- provider status
- referral status
- service result
- consent
- payment/settlement
- outcome

نسیم نباید خود را Master همه داده‌های بیرونی فرض کند.

## 7. Candidate D-0064 — External data is not automatically trusted fact

- **تصمیم پیشنهادی:** داده دریافت‌شده از سامانه بیرونی تا زمانی که Rule پذیرش/تطبیق آن مشخص نباشد، به‌صورت خودکار حقیقت رسمی نسیم محسوب نمی‌شود.

`External Data Received ≠ Automatically Accepted Truth`

**Assessment:** recommended for acceptance.

## 8. Reconciliation — blocking

در تعارض داده محلی و بیرونی باید مشخص شود:
- source precedence
- human review where required
- conflict recording
- correction ownership
- effect on ongoing workflow
- audit

Technical نباید **last-write-wins** را Default Business Rule فرض کند.

## 9. Candidate D-0065 — No implicit last-write-wins

- **تصمیم پیشنهادی:** Conflict بین داده نسیم و داده بیرونی باید با Rule مصوب per Domain حل شود و صرف جدیدتر بودن زمان دریافت، اولویت Business ایجاد نمی‌کند.

**Assessment:** recommended for acceptance.

## 10. Integration direction and cadence — technical/business split

Business باید برای هر Integration مشخص کند:
- inbound / outbound / bidirectional
- business trigger/purpose
- freshness requirement
- whether delayed data is acceptable

اما انتخاب:
- REST / GraphQL / gRPC
- event bus / broker
- batch technology
- protocol
- integration platform

Technical Decision است.

## 11. Referral integration — blocking

اگر Referral به سامانه/Provider بیرونی ارسال شود باید مشخص شود:
- minimum outbound data
- acknowledgment semantics
- accepted external statuses
- rejection/no-response handling
- cancellation/re-route rule
- duplicate protection requirement
- final authority over Referral state

State Machine نهایی همچنان به Journey Closure وابسته است.

## 12. Candidate D-0066 — External service result is not final need resolution

- **تصمیم پیشنهادی:** Result یا Completion Evidence برگشتی از سامانه/Provider خارجی می‌تواند Evidence خدمت باشد، اما به‌تنهایی Need Resolution یا Final Outcome سالمند نیست.

`External Service Result ≠ Final Need Resolution`

**Assessment:** aligned with BC-019/BC-023; recommended for acceptance.

## 13. Integration failure and visibility

Integration Failure می‌تواند شامل:
- destination unavailable
- authentication failure
- timeout
- invalid/malformed data
- schema mismatch
- duplicate/replay
- delayed/stale data
- partial update
- rejected request
- inconsistent status

Severity و Retry Count فنی هنوز تعیین نشده‌اند.

## 14. Candidate D-0067 — Integration failure must not be silent

- **تصمیم پیشنهادی:** Failure در تبادل بیرونی نباید باعث Silent Data Loss یا نمایش موفقیت کاذب شود؛ Failure باید قابل مشاهده، پیگیری و Audit باشد.

`Integration Failure ≠ Silent Data Loss`

**Assessment:** recommended for acceptance.

## 15. Pilot dependency / fallback — blocking

برای هر Integration اجباری Pilot باید تعیین شود:
- criticality
- outage impact
- minimum degraded operation
- manual/fallback business path if any
- reconciliation after recovery
- notification responsibility

Fallback Architecture در Technical تعیین می‌شود؛ ولی وجود یا عدم وجود Business Fallback باید پیش از آن روشن باشد.

## 16. Candidate D-0068 — Pilot-critical dependencies need explicit fallback policy

- **تصمیم پیشنهادی:** هر External Dependency که برای Pilot «Mandatory» است باید Business Continuity/Fallback Rule صریح داشته باشد یا به‌عنوان Single Point of Operational Failure آگاهانه و با Risk Acceptance ثبت شود.

**Assessment:** aligned with BC-021; recommended for acceptance.

## 17. Data minimization and organization boundary

هر Integration باید فقط Data لازم برای Purpose مصوب را مبادله کند.

`Integration convenience ≠ permission for broad data exchange`

همچنین عضویت یک Partner در شبکه به معنی دسترسی بین‌سازمانی نامحدود نیست.

## 18. AI access to external data

وجود Integration به‌خودی‌خود مجوز دسترسی AI به داده بیرونی ایجاد نمی‌کند.

برای هر AI Use Case باید جداگانه مشخص شود:
- external source
- data classes
- runtime purpose
- freshness/trust
- human-review boundary
- audit

## 19. Candidate D-0069 — External data availability does not create training eligibility

- **تصمیم پیشنهادی:** داده بیرونی حتی اگر برای عملیات مجاز باشد، فقط با Training Eligibility Rule مستقل می‌تواند وارد Dataset شود.

`External Data Available ≠ Training Eligible`

**Assessment:** aligned with D-0005; recommended for acceptance.

## 20. External AI services

D-0004 فقط وجود AI داخلی نسیم را الزام می‌کند. هیچ External AI Service یا Vendor AI در Business فعلی تصویب نشده است.

اگر در آینده استفاده از External AI مطرح شود، نیازمند Product Decision مستقل درباره Data Transfer، Privacy، Security، Runtime Governance و Vendor Risk خواهد بود.

## 21. Versioning and change management

Integration Contract باید قابل Versioning باشد تا تغییر در:
- purpose
- fields
- direction
- schema/interface contract
- external status semantics
- source of truth
- consent/legal basis
- deprecation

قابل ردیابی باشد.

## 22. Candidate D-0070 — Integration contracts must be versioned

- **تصمیم پیشنهادی:** Integrationهای رسمی باید Business/Interface Contract versioned و effective-dated داشته باشند؛ تغییر Partner Interface نباید Business Meaning را بی‌صدا تغییر دهد.

**Assessment:** aligned with BC-023/BC-024; recommended for acceptance.

## 23. Integration test gate

برای Integration اجباری Production/Pilot باید قبل از فعال‌سازی Evidence کافی وجود داشته باشد، حداقل در حوزه:
- access/security boundary
- valid/invalid exchange
- duplicate/replay protection
- failure visibility
- reconciliation
- privacy/data minimization
- audit
- outage/recovery behavior

Test implementation در Technical/QA تعیین می‌شود.

## 24. Integration ownership

هر Integration باید حداقل Ownerهای روشن داشته باشد:
- business owner
- data owner
- technical owner
- security reviewer
- legal/privacy reviewer
- operational support owner

وجود این Functionها به معنی الزام به Committee جدا نیست.

## 25. Decommissioning

پایان Integration باید بدون حذف History عملیاتی انجام شود و برای موارد زیر Rule داشته باشد:
- stop date
- pending data/messages
- access/credential revocation
- retained data
- open referrals/services
- replacement/fallback
- audit preservation

## 26. Candidates ready for acceptance

- **D-0061:** Integration یک capability governed با Purpose مصوب است.
- **D-0062:** Tarannom جهت اتصال Source-confirmed است، نه Technical Contract.
- **D-0063:** Integration Access ≠ Data Ownership.
- **D-0064:** External Data Received ≠ Automatically Accepted Truth.
- **D-0065:** No implicit last-write-wins.
- **D-0066:** External Service Result ≠ Final Need Resolution.
- **D-0067:** Integration Failure ≠ Silent Data Loss.
- **D-0068:** Pilot-critical external dependencies require fallback/risk-acceptance rule.
- **D-0069:** External Data Available ≠ Training Eligible.
- **D-0070:** Integration Contracts must be versioned/effective-dated.

## 27. Product-owner decisions still blocking

1. Pilot Integration Inventory
2. Mandatory / Optional / Deferred classification
3. Tarannom operational requirement for Pilot
4. Business purpose per Integration
5. Source-of-Truth matrix
6. Data-sharing fields per Integration
7. legal/consent basis per exchange
8. reconciliation rules
9. Referral integration semantics
10. Service-result acceptance rules
11. Identity/eligibility integration decision
12. Provider Registry synchronization decision
13. organization boundary
14. failure/fallback business rules
15. external dependency criticality
16. Integration ownership
17. AI access to external data
18. external-data Training Eligibility
19. decommissioning policy

## 28. Gate effect

پذیرش D-0061 تا D-0070 مرز Integration Governance را روشن می‌کند، اما Technical Entry Gate تا تعیین **Pilot Integration Inventory، Source of Truth، Data-sharing Contract و Fallback برای Dependencyهای اجباری** همچنان **NOT READY** می‌ماند.

## 29. Next closure packet

**DC-011 — Risk, Continuity, Security & Operational Resilience Decision Packet**
