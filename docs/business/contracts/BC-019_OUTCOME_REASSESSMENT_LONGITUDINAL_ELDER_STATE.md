# BC-019 — Outcome, Reassessment & Longitudinal Elder State

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-003 + BC-007 + BC-010 + BC-018
- **Depends on:** BC-003, BC-006, BC-007, BC-010, BC-012, BC-014, BC-016, BC-018

> این سند چارچوب کسب‌وکاری مشاهده تغییرات سالمند در طول زمان، Reassessment، Outcome و ارتباط آن با Learning را تعریف می‌کند. منبع اولیه Outcome State Machine، ابزار Reassessment، دوره زمانی، Baseline instrument، Causal Attribution یا Rule نهایی حل‌شدن Need را تعیین نکرده است؛ بنابراین این موارد در این سند اختراع نمی‌شوند.

## 1. Source-aligned Outcome Principle

طرح مبنا ارزیابی را فقط کنترل انجام فعالیت نمی‌داند و صریحاً بر سنجش اثر خدمات بر کیفیت زندگی سالمندان، رضایت ذی‌نفعان و سایر پیامدهای اجتماعی تأکید می‌کند.

بنابراین نسیم باید بتواند میان «انجام خدمت» و «تغییر مشاهده‌شده در وضعیت سالمند» تفکیک ایجاد کند.

اصل:

`Service Delivered ≠ Outcome Achieved`

## 2. Longitudinal Elder State

از آنجا که سالمندیار موظف به ارتباط مستمر، پایش وضعیت و شناسایی تغییرات جسمی، روانی و اجتماعی است، نسیم باید بتواند وضعیت سالمند را در طول زمان قابل مقایسه نگه دارد.

این مفهوم در سطح Business یعنی:

- وضعیت در یک زمان مشخص ثبت شود
- منشأ و زمان مشاهده مشخص باشد
- تغییرات نسبت به وضعیت قبلی قابل تشخیص باشند
- تاریخچه بازنویسی نشود
- داده جدید جای داده تاریخی را بی‌صدا نگیرد

مدل فنی State هنوز تعیین نشده است.

## 3. Observation ≠ State ≠ Outcome

برای جلوگیری از اختلاط مفاهیم، Business آینده باید حداقل این سه مفهوم را جدا نگه دارد:

- **Observation:** یک مشاهده/داده ثبت‌شده درباره سالمند
- **State:** تصویر معتبر وضعیت سالمند در یک زمان یا دوره
- **Outcome:** تغییر مشاهده‌شده نسبت به Baseline یا State قبلی

اصل:

`Observation ≠ Accepted State ≠ Outcome`

نام و Workflow دقیق «Accepted State» هنوز تصمیم نشده است و این عبارت فقط برای تفکیک مفهومی استفاده می‌شود.

## 4. Outcome ≠ Impact

همسو با BC-010:

- **Outcome:** تغییر مشاهده‌شده در سطح سالمند/نیاز/خدمت
- **Impact:** اثر وسیع‌تر یا بلندمدت‌تر در سطح فرد، شبکه یا جامعه

یک Outcome موردی نباید خودکار به Impact کلان نسبت داده شود.

## 5. Reassessment

طرح اولیه Reassessment رسمی تعریف نکرده است، اما ماهیت «پایش مستمر» و سنجش اثر ایجاب می‌کند که وضعیت سالمند در نقاط مناسب دوباره بررسی شود.

Reassessment آینده باید بتواند حداقل به این سؤالات پاسخ دهد:

- چه چیزی نسبت به قبل تغییر کرده است؟
- Need هنوز وجود دارد یا خیر؟
- آیا شدت/اولویت تغییر کرده است؟
- آیا Service/Referral دیگری لازم است؟
- آیا Outcome قابل مشاهده است؟
- آیا Follow-up بیشتری لازم است؟

## 6. Reassessment Trigger — Open

هنوز تصمیم نشده است Reassessment چه زمانی انجام شود.

Candidate triggerها:

- بعد از ارائه خدمت
- بعد از تکمیل Referral
- در Follow-up
- در Cadence دوره‌ای
- پس از Incident
- در صورت تغییر مهم مشاهده‌شده
- به درخواست سالمند/سالمندیار
- پیش از Need Closure

هیچ Trigger نهایی در BC-019 تصویب نمی‌شود.

## 7. Baseline Requirement

برای سنجش تغییر، باید Baseline قابل اتکا وجود داشته باشد.

Baseline آینده می‌تواند به:

- initial assessment
- prior reassessment
- prior accepted observation/state
- need-specific baseline

متصل باشد.

اما ابزار، فرم، Scale و اعتبار Baseline هنوز تعیین نشده‌اند.

## 8. Reassessment Versioning

اگر Assessment/Reassessment Definition در آینده تغییر کند، داده‌های تاریخی نباید با تعریف جدید بازتفسیر یا overwrite شوند.

برای هر Reassessment باید در آینده بتوان مشخص کرد:

- definition/version
- date/time
- actor/source
- related need/service/referral
- inputs/evidence
- resulting observations
- review status

این الزام برای مقایسه معتبر و Learning ضروری است.

## 9. Need Lifecycle Link

همسو با BC-018:

`Service Completion ≠ Need Resolution`

پس از Service Completion ممکن است:

- Need همچنان باز باشد
- Need کاهش یافته باشد
- Need بدون تغییر باشد
- Need تشدید شده باشد
- Need حل شده باشد
- Need نیازمند Reassessment بیشتر باشد

این Outcomeها فقط Frame مفهومی‌اند و State Machine نهایی نیستند.

## 10. Need Resolution — Open Contract

برای هر Need Type باید در آینده تعیین شود:

- چه چیزی Resolution محسوب می‌شود
- چه Evidence لازم است
- چه کسی Resolution را تأیید می‌کند
- آیا Reassessment لازم است
- آیا رضایت سالمند شرط است
- آیا Need می‌تواند Reopen شود
- چه زمانی Need «مزمن/مستمر» تلقی می‌شود

هیچ Rule نهایی در این سند تصویب نمی‌شود.

## 11. Referral Closure vs Need Resolution

این مفاهیم باید جدا بمانند:

- **Referral Closure:** چرخه یک ارجاع پایان یافته است
- **Service Completion:** Provider اعلام/اثبات کرده خدمت انجام شده
- **Need Resolution:** وضعیت Need بر اساس Rule مصوب تعیین شده
- **Outcome Observation:** تغییر پس از مداخله/خدمت مشاهده شده

Technical نباید یکی را به‌صورت خودکار از دیگری نتیجه بگیرد.

## 12. Outcome Evidence

Outcome باید به Evidence قابل ردیابی متصل باشد.

Candidate evidence sources:

- elder report
- caregiver observation
- provider result
- structured reassessment
- satisfaction feedback
- system-generated operational data
- other authorized source

اما اعتبار هر نوع Evidence باید جداگانه تعیین شود.

## 13. Provenance

برای هر Outcome/Observation باید منشأ قابل تشخیص باشد:

- Elder-provided
- Family-provided
- Elder-care-worker recorded
- Provider-provided
- System-generated
- AI-generated suggestion
- Human-reviewed AI output

Provenance نباید در مسیر Aggregation یا Dataset generation حذف شود.

## 14. Causality Boundary

دیدن تغییر پس از یک Service به معنی اثبات علت بودن آن Service نیست.

اصل:

`Observed Change ≠ Proven Causal Effect`

اگر در آینده ادعای Causal Impact لازم باشد، Methodology جداگانه باید تصویب شود.

BC-019 هیچ Causal Attribution خودکاری ایجاد نمی‌کند.

## 15. Outcome Dimensions — Source-aligned Frame

طرح اولیه بر بهبود کیفیت زندگی سالمند و اثرات اجتماعی تأکید دارد.

برای Outcome Model آینده می‌توان حداقل این حوزه‌ها را بررسی کرد:

- physical condition
- psychological condition
- social condition
- access to services
- service continuity
- elder satisfaction
- perceived quality of life
- unresolved need burden

اینها فقط Dimensionهای قابل بررسی هستند و Instrument نهایی محسوب نمی‌شوند.

## 16. Satisfaction ≠ Outcome

رضایت سالمند یکی از داده‌های مهم است، اما نباید معادل Outcome کلی فرض شود.

ممکن است:

- خدمت انجام شده باشد ولی Outcome مطلوب نباشد
- سالمند راضی باشد ولی Need همچنان باقی باشد
- Outcome بهتر شده باشد ولی رضایت پایین باشد

بنابراین Satisfaction باید مستقل ثبت و تحلیل شود.

## 17. Provider Result ≠ Outcome

Provider می‌تواند نتیجه/گزارش خدمت خود را ثبت کند، اما:

`Provider Result ≠ Final Elder Outcome`

Outcome نهایی ممکن است نیازمند Follow-up یا Reassessment مستقل باشد.

## 18. AI Role in Reassessment — Day-one Boundary

AI داخلی از روز اول می‌تواند در Use Caseهای مصوب در این حوزه‌ها کمک کند:

- خلاصه‌سازی Observations
- مقایسه داده جدید با سابقه
- برجسته‌سازی تغییرات
- پیشنهاد سؤال Reassessment
- پیشنهاد موارد نیازمند Human Review
- کمک به توضیح روند برای سالمندیار

اما تا تصمیم صریح:

- AI Reassessment رسمی را نهایی نمی‌کند
- AI Outcome رسمی را به‌تنهایی تعیین نمی‌کند
- AI Need Resolution نهایی نمی‌کند
- AI Causal Claim ایجاد نمی‌کند
- AI پرونده رسمی را بدون مسیر معتبر تغییر نمی‌دهد

## 19. Human Review of AI Outcome Analysis

اگر AI در Outcome Analysis استفاده شود، باید قابل ثبت باشد:

- model/version
- relevant input versions
- AI output
- human reviewer
- accepted/rejected/edited result
- final official action
- time

این Trace برای Audit، Evaluation و Learning لازم است.

## 20. AI-generated Observation Boundary

خروجی AI به‌تنهایی Observation معتبر از وضعیت واقعی سالمند نیست.

اصل:

`AI inference ≠ observed fact`

اگر AI از داده‌ها احتمال یا تغییر احتمالی را استنباط کند، تا زمانی که Rule مصوب و Human/Source Verification وجود نداشته باشد، آن استنباط نباید به‌عنوان واقعیت رسمی سالمند ثبت شود.

## 21. Outcome Dataset Link

Outcome و Reassessment از مهم‌ترین منابع بالقوه Learning هستند، زیرا می‌توانند رابطه میان:

`Need → Service/Referral → Delivery → Follow-up → Observed Outcome`

را قابل تحلیل کنند.

اما طبق D-0005:

- فقط داده واجد Training Eligibility وارد Dataset می‌شود
- Dataset generation خودکار و مستمر است
- Dataset باید Versioned و دارای Lineage باشد
- Source/Definition Version باید حفظ شود

## 22. Outcome Learning Signal ≠ Ground Truth by Default

هر Outcome ثبت‌شده لزوماً Label نهایی و بی‌خطا برای Training نیست.

قبل از استفاده به‌عنوان Training Signal باید Rule مشخص کند:

- آیا Outcome verified است
- چه Sourceهایی معتبرند
- چه Review لازم است
- چه Data Quality شرط است
- آیا Attribution لازم است یا خیر

اصل:

`Recorded Outcome ≠ automatically verified training label`

## 23. Dataset Version Alignment

اگر Dataset از Reassessment/Outcome استفاده کند، باید حداقل این نسخه‌ها قابل ردیابی باشند:

- assessment/reassessment definition version
- need taxonomy version
- service catalog version
- relevant AI/model version در صورت نقش AI
- dataset version

این کار از آلودگی معنایی داده تاریخی جلوگیری می‌کند.

## 24. Continuous Learning Loop

جهت محصول D-0005 اجازه می‌دهد که با تولید Outcomeهای جدید و واجد شرایط، Datasetهای جدید خودکار ساخته شوند.

نمای مفهومی:

`Operational Data → Reassessment/Outcome Evidence → Eligibility/Curation → Versioned Dataset → Training/Evaluation`

این Loop مستمر است، اما Model Promotion همچنان تصمیم جداگانه و حاکمیتی باقی می‌ماند.

## 25. Quality & Impact Link

Outcomeهای معتبر می‌توانند در آینده ورودی:

- Service quality evaluation
- Provider evaluation
- workforce learning
- pilot evaluation
- impact measurement
- service catalog improvement
- AI evaluation

باشند.

ولی Formula و Weighting هیچ‌کدام در BC-019 تصویب نمی‌شوند.

## 26. Longitudinal Timeline

نسیم باید در آینده بتواند Timeline سالمند را بدون از دست دادن تاریخچه نگه دارد.

Candidate event types:

- observation
- need creation/change
- referral
- service delivery
- follow-up
- reassessment
- outcome
- complaint/incident
- AI suggestion/human review

اینها Entity یا Event Schema نهایی نیستند.

## 27. Correction vs Historical Integrity

اگر داده اشتباه تصحیح شود، باید در آینده مشخص باشد:

- مقدار قبلی چه بوده
- چه کسی تغییر داده
- چرا تغییر داده
- مقدار جدید چیست
- آیا Outcome قبلی تحت تأثیر قرار می‌گیرد
- آیا Datasetهای قبلی تحت تأثیر قرار می‌گیرند

تاریخچه نباید بی‌صدا overwrite شود.

## 28. Reopen / Recurrence

Need ممکن است پس از Resolution دوباره ظاهر شود یا وضعیت جدیدی ایجاد شود.

Business آینده باید مشخص کند:

- Reopen همان Need است یا Need جدید
- recurrence چگونه ثبت می‌شود
- Baseline جدید چیست
- ارتباط با Service/Referral قبلی چگونه حفظ می‌شود

هیچ Rule نهایی فعلاً وجود ندارد.

## 29. Explicit Non-Decisions

BC-019 موارد زیر را تصویب نمی‌کند:

- Outcome taxonomy نهایی
- Reassessment instrument
- Reassessment cadence
- Baseline scale
- Need resolution states
- Outcome score
- Clinical outcome definition
- Quality-of-life instrument
- Causal attribution method
- Automatic outcome determination
- AI autonomous reassessment
- AI autonomous need closure
- Training-label validation rule
- Outcome-based provider ranking formula
- Outcome-based worker ranking formula

## 30. Open Decisions Required to Accept BC-019

1. Observation model
2. Elder-state model
3. Reassessment definition
4. Reassessment triggers/cadence
5. Baseline rule
6. Reassessment versioning
7. Outcome taxonomy
8. Outcome evidence rules
9. Need resolution criteria
10. Reopen/recurrence rule
11. Referral closure vs Need resolution rule
12. Satisfaction/outcome relationship
13. Provider result/outcome relationship
14. Causality/attribution policy
15. AI role in reassessment/outcome analysis
16. Human-review rule for AI output
17. Outcome training-eligibility rules
18. Training-label validation rule
19. Longitudinal timeline requirements
20. Correction/history policy

## 31. Downstream Constraints

تا پیش از Accepted شدن BC-019:

- Technical نباید Service Completion را Outcome یا Need Resolution فرض کند.
- Backend نباید Outcome State Machine نهایی اختراع کند.
- Reassessment Definition باید Versionable طراحی شود.
- تاریخچه وضعیت سالمند نباید overwrite شود.
- AI inference نباید به‌صورت خودکار واقعیت رسمی سالمند شود.
- Datasetهای خودکار باید Source/Definition Version و Lineage را حفظ کنند.
- Outcome نباید بدون Methodology مصوب به Causal Impact تبدیل شود.
