# DC-007 — Provider Model, Onboarding, Referral Acceptance & Service Evidence Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + BC-003 + BC-008 + BC-018 + BC-023
- **Purpose:** بستن مرزهای Provider Model، Onboarding، Referral Acceptance، Capacity، Service Evidence و Failure Handling بدون اختراع SLA، Tariff، Ranking یا Contract Template.

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند. منبع اولیه وجود شرکای تخصصی، نقش اپراتوری نسیم و ارجاع به ظرفیت‌های سلامت/رفاه را تأیید می‌کند، اما معیار پذیرش Provider، SLA، Settlement، State Machine یا Provider Selection Rule را تعیین نمی‌کند.

## 1. Source-confirmed Provider model

طرح مبنا این مرز را روشن می‌کند:
- نسیم الزاماً ارائه‌دهنده مستقیم همه خدمات تخصصی نیست.
- نسیم شبکه، استانداردها، فناوری، کیفیت، قراردادها و هماهنگی را مدیریت می‌کند.
- خدمات تخصصی توسط شرکای تخصصی/ظرفیت‌های شبکه ارائه می‌شوند.
- حوزه‌های Source-confirmed شامل سلامت، رفاه، توانبخشی، فرهنگی/اجتماعی و سایر خدمات تخصصی مورد نیاز شبکه است.

## 2. Candidate D-0036 — Provider is a distinct specialist role

- **تصمیم پیشنهادی:** Provider تخصصی یک Actor مستقل از سالمندیار و اپراتور نسیم است و فقط در دامنه Service/Contract مصوب خدمت تخصصی ارائه می‌کند.
- **Boundary:** Provider به‌صرف عضویت در شبکه، Full Case Authority یا Full Elder Record Access ندارد.

**Assessment:** source-supported; recommended for acceptance.

## 3. Candidate D-0037 — Provider must be explicitly activated

- **تصمیم پیشنهادی:** ثبت Provider در Registry به‌تنهایی به معنی مجاز بودن ارائه خدمت نیست؛ Provider باید قبل از استفاده عملیاتی طبق Rule مصوب بررسی و فعال شود.
- **Boundary:** Qualification، مدارک، Reviewer، Approver و Activation Workflow هنوز باید تعیین شوند.

**Assessment:** governance-derived; recommended for acceptance.

## 4. Provider Registry — minimum business need

Registry آینده باید حداقل بتواند این ابعاد را نگه دارد:
- Provider identity/type
- Service family/item
- geographic coverage
- status
- contract reference
- qualification/evidence where relevant
- operational contact
- capacity declaration if used
- quality/performance evidence
- activation/suspension/end status

این موارد Data Model فنی نهایی نیستند.

## 5. Onboarding decisions still blocking

برای Phase/Pilot باید تعیین شود:
- Provider types required
- qualification/credential rules
- required evidence/documents
- review owner
- approval/activation owner
- contract prerequisite
- confidentiality/data-sharing terms
- service coverage
- geography
- quality commitments
- suspension/end conditions

## 6. Referral-to-Provider preconditions

حداقل این موارد باید قبل از Referral به Provider برقرار باشند:
- Need معتبر در مسیر Business وجود داشته باشد.
- Service مناسب مشخص باشد.
- Provider برای همان Service مجاز باشد.
- Data/Consent/Authorization لازم برقرار باشد.
- Provider در Scope جغرافیایی/عملیاتی مجاز باشد.

این Preconditions هنوز به معنی Provider selection خودکار نیستند.

## 7. Candidate D-0038 — Provider selection is not implied by eligibility

- **تصمیم پیشنهادی:** واجد شرایط بودن Provider برای یک Service، به‌تنهایی Provider Selection نهایی ایجاد نمی‌کند.

`Provider Eligibility ≠ Provider Selection`

- **Boundary:** Rule انتخاب Provider، نقش سالمند، سالمندیار، Supervisor یا AI هنوز باید جداگانه تصویب شود.

**Assessment:** recommended for acceptance.

## 8. Referral acceptance / rejection — still blocking

Business باید تعیین کند:
- آیا Provider Referral را می‌پذیرد یا رد می‌کند
- response evidence چیست
- rejection reason required است یا خیر
- timeout/no-response چه اثری دارد
- referral چه زمانی معتبر/committed می‌شود
- آیا re-route لازم است
- چه Actorی re-route را انجام می‌دهد

هیچ SLA عددی در منبع وجود ندارد.

## 9. Candidate D-0039 — Provider response must be explicit and auditable

- **تصمیم پیشنهادی:** اگر Referral به Provider ارسال می‌شود، پاسخ Provider و وضعیت پذیرش/عدم پذیرش باید به‌صورت قابل ردیابی و Audit ثبت شود.
- **Boundary:** State names، SLA و rejection taxonomy هنوز باز هستند.

**Assessment:** recommended for acceptance.

## 10. Capacity — business boundary

Capacity مفهوم لازم برای جلوگیری از Referral غیرقابل انجام است، اما مدل آن هنوز باز است.

ممکن است در آینده بر اساس:
- Service
- geography
- time window
- staff/resource
- temporary stop
تعریف شود.

هیچ Capacity Formula یا Threshold در این Packet تصویب نمی‌شود.

## 11. Service delivery evidence

برای هر Service باید مشخص شود:
- چه چیزی Completion محسوب می‌شود
- چه Evidence لازم است
- چه Actorی آن را ثبت می‌کند
- چه Actorی در صورت نیاز Verify می‌کند
- date/time
- result/exception
- linkage to Referral

Provider declaration به‌تنهایی نباید خودکار Need Resolution ایجاد کند.

## 12. Candidate D-0040 — Provider result is not final elder outcome

- **تصمیم پیشنهادی:** Provider می‌تواند Service Result/Completion Evidence ثبت کند، اما این داده به‌تنهایی Outcome نهایی سالمند یا Need Resolution را تعیین نمی‌کند.

`Provider Result ≠ Final Elder Outcome`

**Assessment:** aligned with BC-019/BC-023; recommended for acceptance.

## 13. Data-sharing boundary

Provider فقط باید Data لازم برای Purpose همان Service/Referral را دریافت کند.

`Provider Access ≠ Full Elder Record Access`

Data fields، retention، onward sharing و write-back scope باید per Service/Contract تعیین شوند.

## 14. Provider-generated data and provenance

هر داده‌ای که Provider ثبت می‌کند باید قابل انتساب باشد به:
- Provider
- human recording actor where relevant
- Referral/Service context
- time
- source
- verification status if required

وجود Provider-generated data به‌خودی‌خود Training Eligibility ایجاد نمی‌کند.

## 15. Provider failure / no-capacity path

در صورت:
- no response
- rejection
- no capacity
- service failure
- quality issue
- provider unavailable

باید Business Rule آینده مشخص کند:
- retry/re-route
- escalation
- elder notification
- referral status effect
- incident creation
- alternate provider
- closure evidence

## 16. Candidate D-0041 — Provider failure must not silently close the referral

- **تصمیم پیشنهادی:** عدم پاسخ، رد، عدم ظرفیت یا Service Failure از Provider نباید Referral را به‌طور بی‌صدا موفق/بسته تلقی کند؛ وضعیت باید قابل مشاهده و نیازمند مسیر مصوب بعدی باشد.

**Assessment:** recommended for acceptance.

## 17. Provider suspension / termination — still blocking

برای تعلیق یا خاتمه همکاری باید تعیین شود:
- trigger
- authority
- effect on open Referrals
- reassignment/re-routing
- data access revocation
- communication
- contract effect
- audit

AI یا Score به‌تنهایی نباید Provider را تعلیق کند مگر Decision صریح آینده.

## 18. Quality governance

Source direction:
- توسعه شبکه نباید کیفیت را کاهش دهد.
- کنترل کیفیت، ممیزی و پایش داده ضروری‌اند.

برای Provider آینده می‌توان ابعادی مانند:
- completion
- timeliness
- complaint
- satisfaction
- quality review
- data completeness
را سنجید؛ اما هیچ KPI/Score/Ranking نهایی در این Packet تصویب نمی‌شود.

## 19. Candidate D-0042 — Provider ranking is not a default decision mechanism

- **تصمیم پیشنهادی:** تا زمان تصویب Rule جداگانه، Ranking یا Score Provider نباید به‌صورت خودکار Provider Selection، Suspension یا Contract Decision ایجاد کند.

**Assessment:** recommended for acceptance.

## 20. Financial boundary

منبع Provider Financial Model را نهایی نمی‌کند.

این موارد هنوز باز هستند:
- price/tariff
- fee/commission
- reimbursement
- invoice
- settlement
- co-pay
- penalty
- payment authorization

Technical نباید Billing/Settlement را از Referral lifecycle حدس بزند.

## 21. Integration boundary

اگر Referral یا Service Result با سیستم Provider تبادل شود:
- interface version
- source of truth
- acknowledgment
- retries
- reconciliation
- organization boundary
- security
- data minimization
باید در Integration Contract جدا تعیین شود.

`External Service Result ≠ automatically accepted final truth`

## 22. AI boundary in provider network

AI می‌تواند فقط در Use Case مصوب:
- Provider options را برای Review خلاصه کند
- ظرفیت/اطلاعات را نمایش دهد
- مشکلات داده یا تناقض را Flag کند

اما تا Decision صریح:
- Provider را الزام‌آور انتخاب نمی‌کند
- Provider را فعال/تعلیق نمی‌کند
- Quality approval نهایی نمی‌دهد
- Contract decision نمی‌گیرد

## 23. Candidates ready for acceptance

- **D-0036:** Provider نقش تخصصی مستقل است.
- **D-0037:** Registry entry ≠ operational activation.
- **D-0038:** Provider Eligibility ≠ Provider Selection.
- **D-0039:** Provider response به Referral باید explicit/auditable باشد.
- **D-0040:** Provider Result ≠ Final Elder Outcome.
- **D-0041:** Provider failure/no-response نباید Referral را بی‌صدا ببندد.
- **D-0042:** Ranking/Score به‌طور پیش‌فرض تصمیم خودکار ایجاد نمی‌کند.

## 24. Product-owner decisions still blocking

1. Provider types for Pilot
2. onboarding/qualification rules
3. activation authority
4. Registry required fields
5. Service-to-Provider mapping
6. Referral acceptance/rejection rules
7. Provider Selection rule
8. Elder choice rule
9. Capacity model
10. Completion Evidence
11. Quality standards
12. Provider KPI framework
13. complaint/incident handling
14. suspension/termination authority
15. re-routing/fallback rule
16. provider data-sharing fields
17. financial/settlement model
18. integration requirements
19. AI role in provider recommendation

## 25. Gate effect

پذیرش D-0036 تا D-0042 مرز Provider Model را روشن می‌کند، اما Technical Entry Gate تا تعیین Provider Types فاز، Onboarding/Activation، Selection، Acceptance/Rejection و Completion Evidence واقعی همچنان **NOT READY** می‌ماند.

## 26. Next closure packet

**DC-008 — Quality, KPI, Pilot Success & Scale Gate Decision Packet**
