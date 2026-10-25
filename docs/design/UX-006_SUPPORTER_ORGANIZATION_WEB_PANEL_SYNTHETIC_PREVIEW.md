# UX-006 — Supporter Organization Web Panel: Synthetic Aggregate Preview

**Status:** Figma editable design proposal, not live reporting, permission approval, operational service, finance or Production delivery.
**Date:** 2026-10-09
**Baseline:** D-0171 (React/TypeScript organization panels), D-0173 (approved emerald/coral UI palette); BC-005/009/013/020/022 (organizational, reporting, funding, identity and privacy boundaries).
**Design:** https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=47-2

**Product direction update (D-0174):** The Product Owner has explicitly added organization-side person registration, authorized per-person support-status visibility and governed financial injection as required product capabilities. The exact identity linkage, status fields, permission grants, funds destination and payment mechanics are **not yet contracted or implemented**. The earlier aggregate-only screens in this document remain a design subset; see [UX-007](UX-007_SUPPORTER_PEOPLE_STATUS_FUNDING_PROTOTYPES.md) and [DC-022](../business/closure/DC-022_SUPPORTER_BENEFICIARIES_STATUS_FUNDING_PACKET.md) for the new concept and open decisions.

## Purpose and audience boundary

This is a **proposed supportive-organization** dashboard. The existing Business documents describe a separate `employer` role and potential funding/oversight; they **do not finalize** a new supporter-org actor's exact authority or grant it the employer's capabilities by default. Formal Actor/tenant contracts, organization relationship to Nasim, reporting purposes, minimum aggregate group size and approval matrix remain OPEN.

Keep supporter organization, employer, Nasim operator/admin, professional caregiver and elder independently identifiable and authorized. Organization identity, title or design sample does not grant access to elder Cases, household identity, financial actions, data export or AI Training data.

## Editable Figma screens

| Screen | Node | Presentation and boundary |
|---|---|---|
| **S01 — Overview** | [47:8](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=47-8) | Three aggregate-style cards and editable bar chart. Values **28, 3, 5** are fixture-design values only. **Not** official KPIs, network volumes or authorized supporter reports. |
| **S02 — Sample reports** | [47:92](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=47-92) | Five purely fictitious periods and a 3-row category table. No formal KPI, KPI formula, individual drilldown, export, outcome claim or online data. |
| **S03 — Collaboration areas** | [47:190](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=47-190) | Concept cards for neighborhood elder support, health referral and welfare/cultural/community support; these are families/topics, not active services. No budget, price, amount, transfer, allocation, service-level agreement or payment UI. |
| **S04 — Access & boundaries** | [48:14](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=48-14) | Fictional organization identity, boundary matrix and explicit unavailable reporting/finance actions. Not an actual permissions inventory, RBAC grant or Keycloak integration. |

The sidebar contains reusable editable Figma component variants with 4 routes: «نمای کلی»، «گزارش نمونه»، «حوزه‌های حمایت»، «دسترسی و مجوزها». A visual prototype is not a functional routed React app.

## Fixture reference — synthetic only

- Example organization: **مؤسسه سپیدار**, fixture identity `ORG-DEMO-01`. Invented name; no real organization.
- Fictional sample category data: محله‌محور **14**, سلامت **8**, رفاه و اجتماع **6**; sum **28**.
- Fictional visualization across five generic, **undated** periods: **4 + 5 + 7 + 5 + 7 = 28**.
- All "counts" are authored presentation fixtures, **not production data, actual supporter funding, accepted Cases, served elders, referrals, budgets, KPI metrics or trustworthy trends**.
- No elder names, personal information, or payment claims appear on these screens; no `case.read.oversight` or `case.read.assigned` capability is inferred for supporter organizations.
- Future React implementation may use fixtures **only in explicitly labeled design/dev preview contexts** isolated from Production Backend; no fake data after a denied/failed/missing authorized response.

## Design-system use

Emerald `#005543` remains base, coral `#A94E43` is a contrasting accent for a small number of highlights, coral-soft `#FCECE7` for selected navigation and illustrative areas, coral-ink `#702D26` for text on coral-soft. Vazirmatn Persian RTL typography; editable vector bar charts, variable-bound swatches and sidebar navigation.

## Required Business/Technical gates before real support panel development

1. Define whether "supporter organization" is an employer, partner, funding entity, or independently scoped organizational role; **do not merge these types without an approved contract**.
2. Specify reporting purpose, authorized organizational tenancy, actor identity, actual source of truth, permitted report classes, aggregation/minimum cohort rules and privacy/suppression behavior.
3. Adopt versioned definitions, formulas, dates and provenance for any KPI or chart. Charts must never treat unverified co-occurrence as causality.
4. Approve report drill-down, extraction/export and sharing permissions independently and explicitly; default to no personal elder data.
5. Agree budgets, funding flows, financial sign-off and settlement policies through separate owner-approved Business contracts; do not infer amounts or financial powers.
6. Connect real Keycloak/security sessions and trusted backend authorization; 401/403/409 and lack of data must fail closed rather than render fictional metrics.
7. Perform accessibility, responsive web, contrast, Persian RTL, independent code review, CI, hosted Stage, QA and release approval according to the parent process.

**Release note:** Four Figma prototypes are completed; supporter panel frontend implementation, backend read models, financial/organizational integrations, real Stage and Production are **not** completed. PR stays Draft/Open; do not merge or deploy without the user's explicit instruction.
