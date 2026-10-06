# BC-017 — Communications, Notifications & Elder Interaction Model

- **Status:** DRAFT
- **Stage:** Business
- **Date:** 2026-10-06
- **Source basis:** طرح‌نامه اولیه «شمیم» + D-0004 + D-0005 + BC-003 + BC-005 + BC-014 + BC-016
- **Depends on:** BC-003, BC-005, BC-006, BC-007, BC-012, BC-014, BC-016

> این سند چارچوب کسب‌وکاری ارتباط با سالمند، خانواده، سالمندیار و سایر بازیگران، Notificationها، Reminderها و تعامل AI را تعریف می‌کند. منبع اولیه کانال ارتباطی، ساعات تماس، قالب پیام، Notification Policy، Voice Channel یا Messaging Platform مشخصی تعیین نکرده است؛ بنابراین این موارد در این سند نهایی نمی‌شوند.

## 1. Communication Principle

طرح مبنا دو اصل قطعی دارد:

- سالمندیار باید ارتباط منظم با سالمند و خانواده داشته باشد.
- سالمند در شبکه باید با یک نقطه تماس مواجه باشد.

بنابراین Communication در نسیم یک قابلیت جانبی نیست؛ بخشی از خود مدل خدمت است.

## 2. Single Contact Experience

نسیم باید تجربه‌ای ایجاد کند که سالمند برای پیگیری نیاز خود میان واحدهای متعدد سردرگم نشود.

در سطح Business:

- سالمندیار نزدیک‌ترین نقطه تماس سالمند با شبکه است.
- ارتباط درباره نیاز، ارجاع و پیگیری باید قابل هماهنگی باشد.
- در صورت حضور Provider یا واحد دیگر، تجربه سالمند نباید به چند مسیر متعارض تبدیل شود.

اما هنوز مشخص نشده است که «یک نقطه تماس» دقیقاً به معنی یک شخص ثابت، یک شماره، یک Inbox یا یک کانال سازمانی باشد.

## 3. Communication Actors

ارتباطات آینده ممکن است میان این Actorها رخ دهند:

- سالمند
- خانواده / همراه
- نماینده مجاز در صورت تعریف
- سالمندیار
- سطوح سرپرستی
- اپراتور نسیم
- Provider
- سامانه نسیم
- AI داخلی نسیم

هر ارتباط باید در حدود Role، Purpose و Data Access مصوب انجام شود.

## 4. Contact Channels — Open

طرح اولیه Channel نهایی تعیین نکرده است.

Candidate channelها برای تصمیم آینده می‌توانند شامل این موارد باشند:

- تماس تلفنی
- تماس حضوری
- پیام متنی
- اپلیکیشن
- پیام‌رسان
- تماس صوتی درون سامانه
- تماس تصویری
- Notification درون برنامه
- ارتباط از طریق خانواده یا نماینده مجاز

هیچ‌یک از این Channelها در BC-017 به‌عنوان الزامی یا نهایی تصویب نمی‌شوند.

## 5. Channel Suitability

انتخاب Channel آینده باید با شرایط سالمند سازگار باشد.

Business Design باید بتواند عواملی مانند اینها را در نظر بگیرد:

- توانایی استفاده از فناوری
- ترجیح سالمند
- دسترس‌پذیری
- محدودیت شنوایی/بینایی
- سواد دیجیتال
- محرمانگی
- فوریت
- نوع پیام
- کیفیت اتصال

قواعد دقیق Accessibility هنوز تصمیم نشده‌اند.

## 6. Communication Purpose Taxonomy — DRAFT

برای جلوگیری از اختلاط پیام‌ها، ارتباطات می‌توانند در آینده بر اساس Purpose تفکیک شوند:

- onboarding
- routine contact
- monitoring
- need clarification
- referral update
- appointment/service update
- follow-up
- satisfaction
- complaint
- incident/escalation
- reminder
- education/guidance
- AI interaction
- consent/privacy communication
- administrative notice

این Taxonomy نهایی نیست.

## 7. Notification vs Conversation

نسیم باید میان این دو مفهوم تمایز داشته باشد:

- **Notification:** اطلاع‌رسانی یک‌طرفه یا Event-driven
- **Conversation:** تعامل دوطرفه که ممکن است پاسخ، Context و Follow-up داشته باشد

Technical نباید این دو را یک Entity یا Workflow واحد فرض کند مگر Business Contract بعدی چنین تصمیمی بگیرد.

## 8. Reminder Model — DRAFT FRAME

Reminder ممکن است برای موضوعاتی مانند این لازم شود:

- تماس برنامه‌ریزی‌شده
- Follow-up
- Appointment
- Referral update
- Reassessment
- رضایت
- Training
- Task due
- Consent renewal در صورت وجود

اما هنوز تصمیم نشده است:

- چه Reminderهایی الزامی‌اند
- Recipient کیست
- چه زمانی ارسال می‌شوند
- چندبار تکرار می‌شوند
- Opt-out چگونه است
- Failure delivery چه اثری دارد

## 9. Elder-facing Communication

ارتباط با سالمند باید با اصل حفظ کرامت سالمند سازگار باشد.

در طراحی آینده باید مشخص شود:

- چه نوع پیام‌هایی مستقیم به سالمند ارسال می‌شوند
- زبان و لحن چگونه تنظیم می‌شود
- اطلاعات حساس چگونه بیان می‌شود
- آیا پیام‌های سیستمی نیازمند Human Review هستند
- چه زمانی سالمند باید به سالمندیار ارجاع داده شود
- در چه شرایطی AI پاسخ می‌دهد

هیچ Content Policy نهایی در منبع وجود ندارد.

## 10. Family Communication Boundary

منبع ارتباط منظم سالمندیار با خانواده را ذکر می‌کند، اما BC-014 روشن می‌کند که خانواده به‌صورت پیش‌فرض نماینده مجاز نیست.

بنابراین:

- Family contact ≠ full-data access
- Family contact ≠ decision authority
- Family notification ≠ legal consent

باید در آینده تعیین شود چه اطلاعاتی، در چه شرایطی، برای کدام عضو خانواده و بر اساس چه مجوزی قابل اشتراک است.

## 11. Provider Communication Boundary

Provider ممکن است برای اجرای خدمت نیازمند ارتباط باشد، اما Channel و Scope این ارتباط هنوز تعیین نشده است.

باید مشخص شود:

- Provider مستقیماً با سالمند تماس می‌گیرد یا از مسیر نسیم
- چه داده‌ای در پیام/تماس قابل استفاده است
- چه ارتباطی باید ثبت شود
- Appointment updates چگونه منتقل می‌شوند
- Failure/no-response چگونه Escalate می‌شود

## 12. Human vs System-generated Communication

نسیم باید در آینده بتواند منشأ ارتباط را تفکیک کند:

- Human-authored
- System-generated
- AI-generated
- AI-drafted + Human-approved

این تفکیک برای Transparency، Audit و Dataset Governance لازم است.

## 13. Day-one AI Interaction

بر اساس D-0004 و D-0005، AI از روز اول بخشی از تجربه نسیم است.

AI می‌تواند در Use Caseهای مصوب برای سالمند یا سالمندیار به‌صورت تعاملی استفاده شود.

Candidate elder-facing interactions:

- راهنمایی درباره نسیم
- توضیح وضعیت خدمت
- کمک به بیان نیاز
- یادآوری
- پاسخ به پرسش‌های ساده درباره فرآیند

Candidate elder-care-worker interactions:

- خلاصه‌سازی
- آماده‌سازی Draft
- Reminder
- جست‌وجوی فرآیند/خدمت
- پیشنهاد Follow-up

این Use Caseها فقط در صورت تصویب Business نهایی قابل اجرا هستند.

## 14. AI Identity & Transparency

در تعامل مستقیم با سالمند یا سالمندیار باید امکان تشخیص اینکه پاسخ توسط AI تولید شده وجود داشته باشد.

اصل:

`AI must not impersonate a human actor.`

AI نباید خود را سالمندیار، پزشک، Provider یا تصمیم‌گیر انسانی معرفی کند.

UI/Voice wording دقیق هنوز تصمیم نشده است.

## 15. AI Conversation Boundary

AI تا تصمیم صریح نباید از طریق Conversation:

- تشخیص پزشکی نهایی بدهد
- دستور درمان الزام‌آور بدهد
- Referral نهایی کند
- Provider نهایی انتخاب کند
- هزینه یا پرداخت را تأیید کند
- Consent حقوقی را جعل کند
- Emergency response نهایی را جایگزین انسان کند

Conversation باید با Authority Boundaryهای BC-006 همسو بماند.

## 16. Voice / Conversational Accessibility — Open

برای سالمندان، Voice Interaction ممکن است مفید باشد؛ اما طرح اولیه Voice Assistant را تعریف نکرده است.

موضوعات باز:

- voice input
- voice output
- speech-to-text
- text-to-speech
- Persian dialect handling
- accessibility modes
- noisy environment handling
- consent for recording
- retention of audio
- identity verification in voice interaction

هیچ‌یک در BC-017 تصویب نشده‌اند.

## 17. Communication Logging

برای ارتباطات مهم باید بعداً مشخص شود چه چیزی ثبت می‌شود.

Candidate metadata:

- actor/source
- recipient
- time
- channel
- purpose
- related case/referral/task
- delivery status
- response status
- AI involvement
- consent basis if relevant

محتوای کامل همه تماس‌ها الزاماً نباید ذخیره شود؛ این موضوع نیازمند تصمیم Privacy/Retention است.

## 18. Message Content vs Official Record

یک پیام یا Conversation به‌خودی‌خود Official Record نیست.

اصل:

`Message/Conversation ≠ Official Record`

اگر اطلاعاتی از Conversation باید وارد پرونده رسمی شود، مسیر ثبت/تأیید آن باید مستقل و قابل Audit باشد.

## 19. Notification Delivery State — DRAFT

برای عملیات آینده ممکن است نیاز باشد وضعیت Delivery قابل ثبت باشد، مانند:

- generated
- sent
- delivered
- failed
- acknowledged

این Stateها فقط Candidate هستند و State Machine نهایی نیستند.

## 20. Failed Contact Handling

اگر تماس یا Notification موفق نشود، باید Rule آینده تعیین کند:

- retry
- alternate channel
- worker follow-up
- family contact در صورت مجاز بودن
- supervisor escalation
- no-contact incident

Threshold و Cadence هنوز باز هستند.

## 21. Quiet Hours / Contact Windows — Open

طرح اولیه ساعات مجاز تماس یا Quiet Hours را تعریف نکرده است.

باید بعداً مشخص شود:

- تماس در چه بازه‌ای مجاز است
- Emergency exception چیست
- Reminderها در چه زمان‌هایی ارسال می‌شوند
- سالمند می‌تواند Preference زمانی ثبت کند یا خیر

Technical نباید زمان ثابت اختراع کند.

## 22. Consent & Communication Preferences

آینده باید بتواند Preference و Consent ارتباطی را از هم تفکیک کند.

مثلاً:

- preferred channel
- allowed channel
- allowed recipients
- marketing/non-service contact
- operational contact
- emergency contact
- family notifications

BC-017 هیچ Opt-in/Opt-out Rule نهایی تعیین نمی‌کند.

## 23. Sensitive Communication

برای پیام‌هایی که شامل داده حساس‌اند، Business آینده باید مشخص کند:

- چه Channelهایی مجازند
- چه اطلاعاتی Mask شود
- Identity verification لازم است یا خیر
- link-based access مجاز است یا خیر
- message retention چیست

جزئیات فنی و حقوقی باز است.

## 24. Communication Incident

مواردی مانند این می‌توانند در آینده Incident محسوب شوند:

- ارسال پیام به Recipient اشتباه
- افشای داده بیش از حد
- جعل هویت Actor
- Notification اشتباه
- AI output نامناسب
- Failed critical notification
- Unauthorized family disclosure

Severity و Response Rule در BC-012 باید نهایی شوند.

## 25. Dataset Link

تعاملات ارتباطی ممکن است داده جدید تولید کنند.

Candidate sources:

- AI conversations
- worker notes
- message responses
- acknowledged reminders
- satisfaction replies
- correction/feedback
- accepted/rejected AI drafts

اما هیچ Communication Data به‌صورت پیش‌فرض Training-eligible نیست.

D-0005 فقط برای داده‌ای اعمال می‌شود که Eligibility Rule مصوب را پاس کرده باشد.

## 26. Communication Analytics

در آینده ممکن است برای عملیات نیاز به تحلیل ارتباط باشد، مانند:

- contact success
- response rate
- failed delivery
- unresolved communication
- channel utilization
- follow-up completion

اما این Metrics نباید بدون Business Definition به KPI رسمی تبدیل شوند.

## 27. Explicit Non-Decisions

BC-017 موارد زیر را تصویب نمی‌کند:

- SMS provider
- messaging platform
- telephone infrastructure
- voice assistant
- call recording
- working/contact hours
- quiet hours
- notification cadence
- reminder frequency
- family notification rights
- Provider direct-contact rule
- mandatory app usage
- AI voice mode
- auto-escalation threshold
- message retention duration
- communication KPI targets

## 28. Open Decisions Required to Accept BC-017

1. Contact channel catalog
2. Channel eligibility rules
3. Elder communication preferences
4. Family communication permissions
5. Provider communication model
6. Notification taxonomy
7. Reminder rules
8. Delivery/failure handling
9. Contact windows / quiet hours
10. Sensitive-message rules
11. Communication logging policy
12. Message-to-record conversion rule
13. AI interaction use cases
14. AI transparency wording/UX
15. Voice interaction decision
16. Audio/communication retention
17. Communication incident rules
18. Communication analytics/KPI definitions

## 29. Downstream Constraints

تا پیش از Accepted شدن BC-017:

- Technical نباید Channel یا Vendor نهایی انتخاب کند.
- UI نباید خانواده را به‌عنوان Recipient مجاز پیش‌فرض فرض کند.
- Notification Scheduler نباید Cadence یا Quiet Hours را Hard-code کند.
- AI نباید خود را Actor انسانی معرفی کند.
- Conversation نباید خودکار Official Record شود.
- Communication data نباید بدون Eligibility Rule وارد Dataset شود.
- Day-one product باید امکان تعامل AI در Use Caseهای مصوب را در معماری Communication لحاظ کند.
