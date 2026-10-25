# NASIM Product Development Process

فرآیند مادر توسعه نسیم:

`Business → Technical → Scrum/Product Backlog → Sprint → Code → Code Review → exact-head CI → Stage → QA/Testing → Release Approval → Production → Monitoring → Improvement`

## وضعیت فعلی

تصمیم‌های کسب‌وکاری و تعیین دامنهٔ Phase/Pilot همچنان در جریان‌اند. پیاده‌سازی Backend تا Sprint 025 و تکمیل وبِ مشاهده و ثبت برنامه‌های روزانه در `main` ادغام شده‌اند؛ Backend و Web CI روی HEAD دقیق PR #52 موفق بوده‌اند. Hosted Stage طبق D-0130 هنوز در دسترس نیست؛ بنابراین Stage، QA مبتنی بر Stage، Release و Production انجام‌شده تلقی نمی‌شوند.

## قواعد

- تصمیم‌های تأییدشده در `docs/DECISIONS.md` ثبت می‌شوند.
- موضوع تعیین‌نشده نباید در Technical Design یا Code حدس زده شود.
- Technical و Code برای هر قابلیت باید بر Business decisions و Slice Gateهای لازم تکیه کنند؛ تکمیل یک شاخهٔ فنی به معنی بسته‌شدن همهٔ پرسش‌های Business نیست.
- Backlog باید از Business و Technical مصوب مشتق شود.
- CI، آزمون محلی یا smoke test کانتینر جای Stage و QA محیطی را نمی‌گیرد.
- Production فقط پس از Stage، QA/Testing و Release Approval انجام می‌شود.
- Monitoring و Improvement چرخه پس از انتشار را می‌بندند.

## خروجی‌های لازم برای دامنهٔ اولیه

- Problem و Scope و جامعه هدف
- Actors و مسئولیت‌ها
- Value Proposition
- Service Model و Service Catalog مربوط به پایلوت
- Operating Model و Referral Journey
- Governance، حدود اختیار و داده‌های قابل دسترس
- KPI Framework و معیارهای عبور/توقف پایلوت
- مدت، محدودهٔ جغرافیایی و مالک تصمیم عبور از پایلوت
- Business Risks و Constraints

مبنای اولیه در `docs/business/CONCEPT_BASELINE.md` و سؤال‌های باز context-triggered در `docs/business/OPEN_QUESTIONS.md` است. پاسخ‌های پذیرفته‌شده باید در Decision Register ثبت شوند؛ تا آن زمان موارد باز، فرض قطعی فنی یا کسب‌وکاری محسوب نمی‌شوند.
