# DC-013 — Outcome, Reassessment, Longitudinal State & Learning Signal Decision Packet

- **Status:** DRAFT DECISION PACKET
- **Stage:** Business — Decision Closure
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-006 + BC-007 + BC-010 + BC-019
- **Purpose:** بستن مرزهای Outcome، Reassessment، Longitudinal Elder State و Learning Signal بدون اختراع Instrument، Score، Cadence، Need State Machine یا Causal Method.

> این سند Decision Register نیست و هیچ تصمیمی را Accepted نمی‌کند. طرح اولیه پایش مستمر وضعیت سالمند، شناسایی تغییرات جسمی/روانی/اجتماعی، پیگیری خدمت و سنجش اثر بر کیفیت زندگی را پشتیبانی می‌کند؛ اما Reassessment رسمی، Outcome taxonomy، Baseline instrument، Need-resolution rule یا Causal Attribution را تعیین نمی‌کند.

## 1. Source-confirmed outcome direction

منبع دو جهت را هم‌زمان تثبیت می‌کند:

- سالمندیار باید وضعیت سالمند را به‌صورت مستمر پایش و تغییرات جسمی، روانی و اجتماعی را شناسایی کند.
- ارزیابی نسیم فقط کنترل اجرای فعالیت نیست و باید اثر خدمات بر کیفیت زندگی، رضایت و آثار اجتماعی/اقتصادی را نیز بررسی کند.

پس نسیم باید بتواند میان «خدمت انجام‌شده» و «تغییر مشاهده‌شده» تفاوت بگذارد.

## 2. Candidate D-0094 — Service delivery is not outcome achievement

- **تصمیم پیشنهادی:** انجام Service یا Completion آن به‌تنهایی Outcome مطلوب یا Need Resolution را اثبات نمی‌کند.

`Service Delivered ≠ Outcome Achieved`

**Assessment:** source-aligned; recommended for acceptance.

## 3. Longitudinal elder state

برای مقایسه وضعیت سالمند در طول زمان، Business باید بتواند ثبت کند:
- چه چیزی مشاهده شده
- چه زمانی
- توسط چه Source/Actorی
- نسبت آن با وضعیت قبلی چیست
- آیا داده بعداً تصحیح شده است یا خیر

مدل فنی State هنوز Technical Decision است.

## 4. Candidate D-0095 — Elder history must remain longitudinal

- **تصمیم پیشنهادی:** وضعیت سالمند باید در طول زمان با حفظ تاریخچه قابل مقایسه باشد و داده جدید نباید تاریخچه قبلی را بی‌صدا overwrite کند.

**Assessment:** derived from continuous monitoring and evaluation; recommended for acceptance.

## 5. Observation, accepted state and outcome are distinct

برای جلوگیری از اختلاط مفهوم‌ها:

- **Observation:** داده/مشاهده ثبت‌شده
- **Accepted State:** تصویری از وضعیت که طبق Rule معتبر پذیرفته شده
- **Outcome:** تغییر مشاهده‌شده نسبت به Baseline/State قبلی

عبارت Accepted State در این Packet فقط یک مفهوم Business برای تفکیک است؛ نام و Workflow نهایی آن هنوز تصمیم نشده است.

## 6. Candidate D-0096 — Observation is not automatically official state or outcome

- **تصمیم پیشنهادی:** Observation ثبت‌شده به‌تنهایی وضعیت رسمی یا Outcome نهایی ایجاد نمی‌کند.

`Observation ≠ Accepted State ≠ Outcome`

**Assessment:** recommended for acceptance.

## 7. Reassessment requirement

منبع Instrument یا Cadence رسمی Reassessment نمی‌دهد، اما «پایش مستمر» و «سنجش اثر» نیاز به ارزیابی مجدد را ایجاد می‌کنند.

Reassessment آینده باید بتواند حداقل پاسخ دهد:
- چه چیزی تغییر کرده است؟
- Need هنوز وجود دارد؟
- Severity/Priority تغییر کرده؟
- Follow-up یا Service دیگری لازم است؟
- Outcome قابل مشاهده است؟
- آیا Need قابل Resolution است؟

## 8. Candidate D-0097 — Reassessment definition must be versioned

- **تصمیم پیشنهادی:** هر Assessment/Reassessment باید به Definition Version خودش متصل باشد و تغییر Definition نباید داده تاریخی را با معنای جدید بازنویسی کند.

**Assessment:** governance-derived; recommended for acceptance.

## 9. Reassessment trigger — blocking

Candidate triggerها:
- بعد از Service
- بعد از Referral completion
- در Follow-up
- دوره‌ای
- پس از Incident
- پس از تغییر مهم
- به درخواست سالمند/سالمندیار
- پیش از Need Closure

هیچ Trigger یا Cadence نهایی در منبع وجود ندارد.

## 10. Baseline — blocking

برای سنجش تغییر، Baseline لازم است؛ اما منبع تعیین نمی‌کند:
- Baseline اولیه چیست
- چه Instrumentی استفاده شود
- چه Sourceهایی معتبرند
- چه زمانی Baseline refresh شود
- Need-specific یا whole-person باشد

Technical نباید Scale یا Form اختراع کند.

## 11. Candidate D-0098 — Outcome requires traceable evidence

- **تصمیم پیشنهادی:** Outcome رسمی باید به Evidence و Provenance قابل ردیابی متصل باشد؛ Source و زمان Observation نباید از Outcome جدا شوند.

**Assessment:** recommended for acceptance.

## 12. Evidence sources — not equal by default

Candidate sources:
- elder report
- authorized family/representative input
- caregiver observation
- provider result
- structured reassessment
- satisfaction feedback
- system-generated operational evidence
- AI-assisted analysis after human review

Business هنوز باید اعتبار و Review requirement هر Source را تعیین کند.

## 13. Provider result and satisfaction boundaries

دو اصل باید حفظ شوند:

`Provider Result ≠ Final Elder Outcome`

`Satisfaction ≠ Outcome`

Provider Completion و رضایت هر دو Evidence مهم‌اند، اما هیچ‌کدام به‌تنهایی Outcome کلی یا Need Resolution را تعیین نمی‌کنند.

## 14. Candidate D-0099 — Need resolution is separate from referral closure

- **تصمیم پیشنهادی:** Referral Closure، Service Completion، Need Resolution و Outcome Observation باید جداگانه قابل ثبت و Governance باشند.

**Assessment:** aligned with BC-019/DC-004; recommended for acceptance.

## 15. Need resolution — blocking

برای هر Need Type باید بعداً تعیین شود:
- Resolution criterion
- required evidence
- authority
- reassessment requirement
- role of elder feedback
- reopen rule
- recurrence handling
- chronic/ongoing need handling

هیچ State Machine نهایی تصویب نمی‌شود.

## 16. Outcome versus impact

- Outcome = تغییر مشاهده‌شده در سطح سالمند/Need/Service
- Impact = اثر گسترده‌تر یا بلندمدت‌تر در سطح فرد/شبکه/جامعه

## 17. Candidate D-0100 — Observed change is not causal proof

- **تصمیم پیشنهادی:** مشاهده تغییر پس از Service به معنی اثبات رابطه علّی Service با آن تغییر نیست.

`Observed Change ≠ Proven Causal Effect`

ادعای Causal Impact نیازمند Methodology مستقل است.

**Assessment:** recommended for acceptance.

## 18. AI role in reassessment/outcome

AI Day-one در Use Case مصوب می‌تواند:
- Observations را خلاصه کند
- داده جدید را با سابقه مقایسه کند
- تغییرات را Flag کند
- سؤال Reassessment پیشنهاد دهد
- موارد نیازمند Human Review را برجسته کند

اما تا Decision صریح:
- Reassessment رسمی را نهایی نمی‌کند
- Outcome رسمی را نهایی نمی‌کند
- Need را Resolve/Close نمی‌کند
- Causal Claim رسمی تولید نمی‌کند
- Observation جدید از واقعیت را اختراع نمی‌کند

## 19. Candidate D-0101 — AI inference is not observed fact

- **تصمیم پیشنهادی:** استنباط AI درباره وضعیت سالمند، بدون Source Verification/Rule معتبر، Observation رسمی محسوب نمی‌شود.

`AI Inference ≠ Observed Fact`

**Assessment:** aligned with BC-006/BC-019; recommended for acceptance.

## 20. Human review of AI outcome analysis

اگر AI در Outcome/Reassessment Analysis نقش داشته باشد، باید قابل ردیابی باشد:
- model/version
- input/context versions
- AI output
- reviewer
- accept/reject/edit
- final official action
- time

## 21. Learning signal boundary

Outcome/Reassessment می‌توانند منبع Learning Signal باشند چون زنجیره زیر را قابل تحلیل می‌کنند:

`Need → Referral/Service → Delivery → Follow-up → Observed Outcome`

اما Outcome ثبت‌شده به‌طور خودکار Label معتبر Training نیست.

## 22. Candidate D-0102 — Recorded outcome is not automatically a verified training label

- **تصمیم پیشنهادی:** Outcome یا Reassessment فقط در صورت عبور از Training Eligibility، Quality/Verification و Labeling Rule مصوب می‌تواند به Learning Signal/Training Label تبدیل شود.

`Recorded Outcome ≠ Automatically Verified Training Label`

**Assessment:** aligned with D-0005/BC-007; recommended for acceptance.

## 23. Candidate D-0103 — Learning lineage must preserve definition versions

- **تصمیم پیشنهادی:** اگر Outcome/Reassessment وارد Dataset شود، Lineage باید حداقل نسخه‌های Assessment/Reassessment Definition، Need Taxonomy، Service Catalog، Dataset و در صورت نقش AI، Model Version مرتبط را حفظ کند.

**Assessment:** recommended for acceptance.

## 24. Automatic dataset lifecycle boundary

طبق D-0005:

`Eligible Outcome/Reassessment Evidence → Automatic Versioned Dataset Lifecycle`

اما:
- Eligibility Rule خودکار تغییر نمی‌کند.
- Recorded Outcome خودکار Ground Truth نیست.
- Dataset generation خودکار است، نه Governance acceptance.
- Model Promotion همچنان جدا است.

## 25. Correction and historical integrity

اگر Observation/State اشتباه تصحیح شود، باید بتوان تشخیص داد:
- value before
- value after
- actor
- reason
- time
- effect on later Outcome
- effect on Dataset lineage

## 26. Candidate D-0104 — Corrections must preserve history

- **تصمیم پیشنهادی:** تصحیح داده سالمند نباید تاریخچه را حذف کند؛ تغییر باید با علت، Actor و اثر احتمالی بر Outcome/Dataset قابل ردیابی باشد.

**Assessment:** recommended for acceptance.

## 27. Reopen / recurrence — blocking

Business باید مشخص کند:
- Reopen همان Need است یا Need جدید
- recurrence چگونه تشخیص داده می‌شود
- Baseline جدید چیست
- ارتباط با Referral/Service قبلی چگونه حفظ می‌شود

هیچ Rule منبعی وجود ندارد.

## 28. Outcome dimensions — source-aligned, not final taxonomy

حوزه‌های قابل بررسی:
- physical condition
- psychological condition
- social condition
- access to services
- service continuity
- elder satisfaction
- perceived quality of life
- unresolved need burden

اینها Instrument یا Score نهایی نیستند.

## 29. Candidates ready for acceptance

- **D-0094:** Service Delivered ≠ Outcome Achieved.
- **D-0095:** Elder history must remain longitudinal.
- **D-0096:** Observation ≠ Accepted State ≠ Outcome.
- **D-0097:** Reassessment definitions must be versioned.
- **D-0098:** Outcome requires traceable evidence/provenance.
- **D-0099:** Referral Closure / Service Completion / Need Resolution / Outcome are distinct.
- **D-0100:** Observed Change ≠ Proven Causal Effect.
- **D-0101:** AI Inference ≠ Observed Fact.
- **D-0102:** Recorded Outcome ≠ Automatically Verified Training Label.
- **D-0103:** Learning lineage preserves definition versions.
- **D-0104:** Corrections preserve history.

## 30. Product-owner decisions still blocking

1. Observation model
2. official elder-state/acceptance model
3. Reassessment definition
4. Reassessment trigger/cadence
5. Baseline rule
6. Outcome taxonomy
7. Outcome evidence validity rules
8. Need Resolution criteria
9. Need reopen/recurrence rule
10. Satisfaction/outcome relationship
11. Provider-result/outcome verification
12. Causality/attribution policy
13. AI Human Review rule for Outcome Analysis
14. Outcome Training Eligibility
15. Training-label validation rule
16. correction/restatement effects on Dataset
17. Longitudinal timeline requirements
18. Outcome owner/reviewer

## 31. Gate effect

پذیرش D-0094 تا D-0104 مرز مفهومی Outcome/Learning را روشن می‌کند، اما Technical Entry Gate تا تعیین **Reassessment Contract، Baseline، Need Resolution Rule و Outcome Training Eligibility واقعی** همچنان **NOT READY** می‌ماند.

## 32. Next closure packet

**DC-014 — Business Configuration, Policy Versioning & Change Control Decision Packet**
