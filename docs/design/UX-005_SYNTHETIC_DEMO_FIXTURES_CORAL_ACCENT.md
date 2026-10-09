# UX-005 — Cohesive Synthetic Demo Fixtures and Coral Contrast for Nasim Mobile

**Status:** Figma design iteration / proposed visual accent; **not** a live app, authorized elder record, official case workflow or accepted commercial catalogue.
**Date:** 2026-10-09
**Requested by Product Owner:** Fill mobile app mockups with realistic **fake data** and introduce a color contrasting with overused green.
**Basis:** D-0170 (child pays using own account when real purchase is built; elder credit deferred), D-0171 (React Native/TypeScript mobile), D-0172 (integrated elder services and AI UX), UX-003 and UX-004, BC-002/003/006/014/022.

## 1. Figma source and treatment

Changes were made **in place** in the existing editable Figma file. Frames, vectors, components, variables and text are editable; screenshots are not substituted for layouts.

- [Design system accent specimen](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=35-12)
- [Elder + family screens](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=21-2) — Home, Service Families, Assistant, Follow-up, Family Companion
- [AI draft + human handoff](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=25-2) — Sample chat, elder review, pre-submit handoff and AI-unavailable safe state
- [Professional caregiver app](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=27-2) — assigned Cases, Case workspace, human recording form specimen, future elder request-preview, caregiver AI guidance

## 2. Fixture identities (fictional, not derived from operational data)

| Entity | Display | Reference | Reality claim |
|---|---|---|---|
| Elder A | مهتاب نیک‌رفتار, ۷۴ سال | `NSM-DEMO-101` | **FICTIONAL** |
| Elder B | هما بهاروند, ۶۹ سال | `NSM-DEMO-102` | **FICTIONAL** |
| Caregiver | سارا مهرآیین | `caregiver-demo` | **FICTIONAL** |
| Family companion / elder A's child | نیما نیک‌رفتار | Demo family account | **FICTIONAL** |
| Example conversation | مهتاب درباره حضور در فعالیت اجتماعی محله صحبت می‌کند | No authoritative Request ID | **FICTIONAL** |
| AI response | پیشنهادی برای بیان خواسته، قابل بازبینی سالمند | Not an accepted Need | **FICTIONAL** |
| Example caregiver observation | مهتاب در یک گفت‌وگوی فرضی تمایل به فعالیت محلی را بیان کرد | No persisted event | **FICTIONAL** |
| Follow-up depiction | Example narrative of an elder→AI draft→possible human review | No backend queue status | **FICTIONAL** |

Demo names, ages, IDs, note texts and simulated sequence must never be copied into Production databases, audits, telemetry, learning datasets, authenticated user data or real care cases.

## 3. New contrast tokens (design proposal)

Existing deep emerald `#005543` remains core Nasim branding. Add a **warm coral accent** with deliberate, limited usage:

| Token | Hex | Intended use |
|---|---|---|
| `primitive/coral` / `color/accent` | `#A94E43` | Rare, important CTA / one dominant highlight |
| `primitive/coral-soft` / `color/accent-soft` | `#FCECE7` | Selected navigation, sample card background, low-emphasis contrast |
| `primitive/coral-ink` / `color/accent-ink` | `#702D26` | Readable labels on coral-soft |
| `color/brand` | `#005543` | Core identity and secondary actions |

Calculated sRGB contrast (reference only, **not** a substitute for mobile accessibility QA): white on `#A94E43` ~**5.44:1**, `#702D26` on `#FCECE7` ~**8.74:1**. Color must not be the only indicator of a status, and coral must not be mistaken for an emergency alert.

Updated editable navigation master components for both elder/family app and professional caregiver app: selected item uses `color/accent-soft` with `color/accent-ink` label. Some important actions use coral + white for visual rhythm while other UI remains emerald, cloud-white and muted neutral.

**Palette status:** proposed design iteration pending user's visual feedback, not a separate final corporate brand-identity decision.

## 4. Demo architecture constraint for React Native implementation

1. If implementation later needs fixtures, use an explicitly labelled Development/Storybook/Design Preview data source isolated from real API clients, credentials and persistent stores. **Never** show a fabricated Case/Request/Payment as a fallback to an HTTP 401/403/409/500, missing consent or unavailable internal AI.
2. Keep the authoritative contracts for current assigned Cases and professional HUMAN actions unchanged. `GET /api/v1/cases` is **not** an elder-request inbox. A proposed request preview is a storyboard only, not an existing API, queue or durable status.
3. No real service SKU, approved Provider, price/checkout, PSP, financial transaction, elder-credit spending, medical decision, actual notification delivery, AI runtime response or service outcome is represented.
4. Family self-funded purchase remains a scoped, future-enabled Business choice (D-0170); no assertion that payment flows have been implemented.
5. Preserve visual explicit `نمونه / ساختگی / دمو` labels; strip sample names and fixtures from Production builds and real user-visible case data. Do not infer household relationships, access rights, official Needs, Referrals, training eligibility or AI authority from Figma.
6. Before mobile release: implement real identity, approved Case linkage, scoped capability and legal-purpose checks, genuine empty/unavailable states, approved request-intake contracts, accessibility and end-to-end QA.

## 5. Visual review and non-release boundary

The screens were inspected using Figma screenshots, several overflowing content sections were shortened/reflowed, and a coral CTA with initially insufficient label contrast was corrected to white. The design is **not** a tested React Native app; no API, CI implementation, Stage, payment or Production deployment has been claimed.

PR stays Draft/Open; code and design must be reviewed under the existing parent process before implementation or release.
