# BX-011 — Integration, External Dependency & Source-of-Truth Map

- **Status:** ACTIVE EXPLORATION BASELINE
- **Stage:** Business — Exploration
- **Date:** 2026-10-07
- **Source basis:** BC-023 + BC-021 + DC-010 + BR-004 + BX-010
- **Purpose:** ترسیم Integrationها، External Dependencyها، Source-of-Truth، Reconciliation، External-data Provenance و Fallback در سطح Business؛ بدون تعیین API، Protocol، Schema، Sync Technology یا Mandatory Integration.

> این سند هیچ Integration را برای Pilot اجباری اعلام نمی‌کند. حتی «ترنم» در این مرحله یک جهت Source-confirmed است، نه Technical Contract یا Mandatory Pilot Dependency.

## 1. Core boundaries

- Integration Access ≠ Data Ownership
- External Data Received ≠ Automatically Accepted Truth
- External Data Available ≠ Training Eligible
- External Service Result ≠ Final Need Resolution
- Integration Failure ≠ Silent Data Loss
- Technical Connectivity ≠ Business Authority
- Newer Arrival Time ≠ Business Truth
- Partner Membership ≠ Unrestricted Cross-Organization Access
- External Active Status ≠ Automatic NASIM Operational Approval

## 2. Integration-domain frame

Candidate domains:
- Employer systems
- Health systems
- Welfare systems
- Provider systems
- Identity / Eligibility systems
- Communication services
- Reporting/exchange systems
- Contract/partner systems
- Financial systems only if financial capability is later approved
- Other public/private partner platforms

وجود در این فهرست به معنی وجود واقعی یا الزام Pilot نیست.

## 3. Integration inventory concept

برای هر Integration آینده باید حداقل بتوان این Business Context را ثبت کرد:
- partner/system
- business purpose
- direction
- data classes
- owner
- organization boundary
- source-of-truth responsibility
- legal/data-sharing basis
- operational dependency
- outage effect
- fallback requirement
- interface/business contract version
- effective period

ساختار فنی Registry بعداً تعیین می‌شود.

## 4. Tarannom boundary

طرح مبنا «ترنم» را در لایه سلامت به‌عنوان یکی از جهت‌های اتصال ذکر می‌کند.

در این مرحله فقط این نتیجه معتبر است: Tarannom = Source-confirmed integration direction.

اما این موارد OPEN هستند:
- آیا برای Pilot الزامی است
- API availability
- authentication
- data schema
- write-back
- sync model
- SLA
- legal/data-sharing contract
- source-of-truth scope

Trigger: قبل از Health Integration Design باید Requirement واقعی ترنم با Evidence سامانه مقصد مشخص شود.

## 5. Integration direction

برای هر Integration باید Business direction مشخص شود: inbound، outbound یا bidirectional.
Bidirectional exchange نباید پیش‌فرض باشد.

REST، events، batch، broker، protocol و transport در مرحله Technical انتخاب می‌شوند.

## 6. Purpose limitation

هر Integration فقط برای Purpose مصوب استفاده می‌شود. Candidate purposes شامل identity/eligibility verification، referral delivery، provider/service discovery، appointment/service coordination، service-result retrieval، status synchronization، quality/reporting evidence و consent/authorization verification است.

یک Purpose اجازه همه Purposeهای دیگر را ایجاد نمی‌کند.

## 7. Source of Truth / System of Record

برای Data Elementهای مهم باید قبل از تبادل دوطرفه مشخص شود کدام System/Organization مرجع است. Candidate domains شامل identity، eligibility، contact data، Need/Referral، Provider status، Service Result، Consent، financial data در صورت ورود به Scope و Outcome است.

نسیم نباید خود را Master همه داده‌های بیرونی فرض کند.

## 8. Source-of-truth patterns

برای هر Data Domain ممکن است آینده یکی از این روابط وجود داشته باشد:
- External system authoritative
- NASIM authoritative
- Joint/derived with reconciliation
- External evidence only, human acceptance required

اینها State نهایی نیستند؛ فقط الگوهای تحلیلی‌اند.

## 9. External-data provenance

هر داده خارجی باید Source خود را حفظ کند: source organization/system، source reference، source timestamp/version، received time، transformation، verification/review status، destination use و correction/supersession history.

Aggregation یا AI processing نباید Source را محو کند.

## 10. External data trust

External data ممکن است معتبر، ناقص، stale، متعارض یا نیازمند Human Review باشد.
External Data Received ≠ Accepted State.
Rule پذیرش باید per Domain بسته شود.

## 11. Reconciliation

وقتی local و external data تعارض دارند، Business باید بعداً precedence، reviewer، conflict recording، correction authority، workflow impact، audit و امکان Merge را تعیین کند.

Last-write-wins نباید بدون Business Decision پیش‌فرض شود.

## 12. Late / stale / out-of-order data

Future Rule باید source timestamp semantics، stale handling، correction handling، replay handling و conflict with newer accepted local state را روشن کند.
Arrival time به‌تنهایی Truth Priority ایجاد نمی‌کند.

## 13. Referral integration

اگر Referral به Provider/System بیرونی منتقل شود، Business Contract آینده باید minimum outbound data، valid referral preconditions، acknowledgment semantics، accepted external responses/statuses، rejection/no-response handling، cancellation/re-route، duplicate protection requirement و final authority over NASIM referral state را مشخص کند.

هیچ State Machine در BX-011 تعریف نمی‌شود.

## 14. External service result

External Service Result ≠ Final Need Resolution ≠ Final Elder Outcome.
داده بیرونی فقط Evidence است تا وقتی Rule معتبر آن را در Follow-up/Reassessment/Outcome استفاده کند.

## 15. Identity / eligibility boundary

اگر External Identity یا Eligibility در آینده استفاده شود، trusted attributes، verification freshness، stale-data behavior، mismatch behavior، outage fallback و manual review/override authority باید مشخص شود.

هیچ External Identity Provider فعلاً تصویب نشده است.

## 16. Provider registry synchronization

External credential/status باید Source خود را حفظ کند و local operational approval ممکن است جدا باشد.
External Provider Status ≠ Automatic NASIM Activation.

## 17. Organization boundary

هر Partner/Employer/Provider Organization باید Boundary مستقل داشته باشد. Data Sharing آینده باید به organization، contract، purpose، service/context و exact data scope متصل باشد.

Technical multi-tenancy later؛ Business boundary اکنون باید روشن بماند.

## 18. External dependency map

برای هر Capability حیاتی باید Dependencyهای بیرونی مانند Provider، communication service، health/welfare system، external identity/eligibility، infrastructure dependency و financial service در صورت تصویب قابل شناسایی باشند.

برای هر Dependency باید criticality، outage impact، minimum operation، fallback need، reconciliation after recovery و notification responsibility بعداً تصمیم شود.

## 19. Mandatory / optional / deferred status

وقتی Pilot واقعی طراحی می‌شود، هر Integration باید یکی از وضعیت‌های Mandatory for Pilot، Optional for Pilot یا Explicitly Deferred را به‌صورت صریح بگیرد.

Unknown ≠ Mandatory ≠ Deferred.
طبق D-0118 این تصمیم فقط در Context Pilot بسته می‌شود.

## 20. Fallback boundary

برای Dependencyهای Mandatory باید Business مشخص کند manual path exists or not، degraded service allowed or not، which obligations continue، which actions pause، who owns fallback و what must later be reconciled.

Fallback Architecture در Technical تعیین می‌شود.

## 21. Integration failure

Candidate failure classes: destination unavailable، authentication failure، timeout، malformed data، schema mismatch، duplicate/replay، delayed/stale data، partial update، rejected request و inconsistent status.

Failure باید visible/auditable باشد؛ Success کاذب نباید نمایش داده شود.

## 22. Duplicate / replay business effect

برای عملیات حساس مانند Referral creation، Service Result، Consent update، financial event در صورت ورود به Scope و Dataset import باید از اثر تکراری کسب‌وکاری جلوگیری شود.

روش فنی Idempotency بعداً تعیین می‌شود.

## 23. Integration versioning

Business/Interface Contract باید Versionable باشد. Purpose، data fields/classes، direction، status semantics، source-of-truth rule، consent/legal basis، effective date و deprecation باید قابل Versioning باشند.

Partner Interface Change نباید Business Meaning را بی‌صدا تغییر دهد.

## 24. External-data AI runtime boundary

وجود Integration به AI حق دسترسی خودکار نمی‌دهد. برای هر AI Use Case باید external source، allowed data class، runtime purpose، freshness/trust، human-review boundary و audit جداگانه تعیین شود.

Integration Exists ≠ AI Access.

## 25. External-data learning boundary

حتی اگر External Data برای Operations مجاز باشد، Training نیازمند Rule مستقل درباره ownership/licensing، consent/legal basis، provenance، quality، allowed training purpose، exclusions، retention و lineage است.

External Operational Use ≠ Training Permission.

## 26. External AI boundary

Business فعلی فقط AI داخلی نسیم را الزام می‌کند. هیچ External AI API/Vendor Service در این Exploration تصویب نمی‌شود.

## 27. Continuity relationship

برای Dependency مهم باید بتوان مشخص کرد چه Capability متاثر می‌شود، چه کار انسانی باید ادامه یابد، چه داده‌ای queue/reconcile می‌شود، چه چیزی بعداً repair/replay می‌شود و چه Evidence برای Recovery لازم است.

External Dependency Outage ≠ Permission to Bypass Security/Data Governance.

## 28. Integration audit spine

Future audit should reconstruct: Business Purpose → Source → Destination → Data Class → Contract Version → Exchange Time → Result/Failure → Retry/Reconciliation → Final Operational Effect.

در صورت AI use، AI Policy Version، Model Version، external-data context و Human Review نیز باید قابل ردیابی باشند.

## 29. Decision triggers

- Integration inventory: before external integration design
- Tarannom requirement: before health integration design
- Mandatory/optional/deferred status: during Pilot planning
- Source of Truth: before bidirectional exchange
- Data-sharing fields: before interface contract
- Reconciliation rules: before two-way synchronization
- Referral integration semantics: before external referral flow
- External status acceptance: before local state can change from external data
- Fallback: before mandatory dependency
- Organization boundary: before partner access
- External AI runtime access: before AI uses external data
- External-data Training Eligibility: before external data enters Dataset
- Decommissioning rule: before production dependency lifecycle

## 30. Explicit non-decisions

BX-011 does not define API style، protocol، schema، endpoint، authentication technology، sync cadence، retry count، timeout، message broker، integration platform، healthcare interoperability standard، external identity provider، payment integration، external AI vendor، vendor SLA، master-data technology یا mandatory Pilot integrations.

## 31. Next artifact

**BX-012 — Risk, Safety, Continuity & Recovery Scenario Map**

## 32. Current stage

- Stage: Business
- Integration/External Dependency exploration: ACTIVE
- Business → Technical: NOT READY
- Code: NOT STARTED
- Codex handoff: NOT YET TRIGGERED