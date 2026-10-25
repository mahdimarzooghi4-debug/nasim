# نسیم

**نسیم = نظام سالمند‌یاری محله‌محور**

این مخزن مرجع رسمی مستندات، تصمیمات و توسعه محصول نسیم است.

## وضعیت فعلی

تا commit ادغام `5760f21ae3af0ff1616d4fc4be4a059f0b8b9178` در 2026-10-25، Sprint 025 و تکمیل‌های وب روال مراقبت (PRهای #51 تا #54: مشاهده برنامه، ثبت رویداد انسانی، و مدیریت برنامه برای مراقبِ منتسب) در `main` هستند. Backend و Web CI روی HEAD دقیق PR #54 (`af0b64dbc80e5d87d7b363ec497c1ab69e9d84b5`) موفق شدند؛ CI شامل smoke کانتینری Stage-like است و آمادگی Hosted Stage یا بهره‌برداری را تأیید نمی‌کند.

- Hosted Stage هنوز طبق D-0130 در دسترس نیست؛ پذیرش Stage، QA مبتنی بر Stage، Release و Production انجام نشده‌اند.
- دامنه عملیاتی اولین Phase/Pilot هنوز باید مشخص و به تصمیم ثبت‌شده تبدیل شود.
- معماری OIDC با Keycloak در D-0169 انتخاب شده، اما سرویس واقعی پیکربندی یا متصل نشده است.
- D-0135 استفاده اطلاعاتی، فقط‌خواندنی و مبتنی بر منبع تأییدشده را برای سالمند و مراقب به‌عنوان جهت اولین مورد AI ثبت می‌کند. محتوای رسمی منتشرشده و مجاز هنوز باید با شواهد واقعی تأمین شود.
- تصمیم‌های مجزای دسترسی داده و مجازبودن استفاده برای Training همچنان نیازمند شواهد و تأیید واقعی‌اند.

مبنای اولیه کسب‌وکار، طرح‌نامه «شبکه سالمندیاری شمیم» است. تغییر نام به «نسیم» به‌خودی‌خود مفاد کسب‌وکار را عوض نمی‌کند؛ تغییر محتوایی باید به‌عنوان تصمیم مستقل ثبت شود.

## فرآیند توسعه

`Business → Technical → Scrum/Product Backlog → Sprint → Code → Code Review → exact-head CI → Hosted Stage → QA/Testing → Release Approval → Production → Monitoring → Improvement`

هر مرحله گیت مستقل دارد. CI یا smoke test کانتینر جای Hosted Stage، QA، تأیید Release یا Production را نمی‌گیرد.

## مستندات

- [Decision Register](docs/DECISIONS.md)
- [Business Concept Baseline](docs/business/CONCEPT_BASELINE.md)
- [Business Open Questions](docs/business/OPEN_QUESTIONS.md)
- [Pre-Stage Readiness Register](docs/business/PRE_STAGE_COMPLETION_READINESS_REGISTER.md)
- [Product Process](docs/PRODUCT_PROCESS.md)

## Backend

توسعه Backend تا Sprint 025 در `main` ادغام شده است. جزئیات محدوده پیاده‌شده، اجرای محلی، migrationها و محدودیت‌های فعلی در [Backend README](backend/README.md) آمده است. برنامه‌ریزی یا ادغام کد به‌تنهایی به معنی فعال‌شدن سرویس بیرونی یا تأیید محیط Stage نیست.
