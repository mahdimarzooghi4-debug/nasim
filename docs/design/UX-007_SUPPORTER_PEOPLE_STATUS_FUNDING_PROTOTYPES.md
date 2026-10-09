# UX-007 — Supporter People, Individual Status and Funding Draft Screens

**Status:** Editable Figma prototype, supporter capabilities accepted in D-0174 and **individual earmarked credit** destination selected in D-0175; real finance, accounts, rights, spending, APIs and code not implemented.
**Date:** 2026-10-09
**Figma design page:** https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=49-2
**Business contract:** [DC-022](../business/closure/DC-022_SUPPORTER_BENEFICIARIES_STATUS_FUNDING_PACKET.md)

## Four new Figma screens

| Page | Figma node | Fictional UI and boundary |
|---|---|---|
| **S05 — People under support** | [49:8](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=49-8) | Roster of three **fictional** individuals, sample relation labels; no real enrollment or Case link. |
| **S06 — Add a person** | [49:82](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=49-82) | Filled visual identity/relationship form; save disabled, no consent/identity proof asserted, no API called. |
| **S07 — Person support status** | [49:159](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=49-159) | Fictional status snapshot/story; NOT a Case workflow, real patient state or authorized per-person reporting. |
| **S08 — Funding / money injection concept** | [49:238](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=49-238) | **Selected business destination (D-0175): per-person earmarked credit**; fictional target **مهتاب نیک‌رفتار / NSM-DEMO-101** with illustrative **12,000,000 IRR**. General organization-wide funding pool is explicitly unselected. Still non-executable, with no real PSP, legal wallet/account, authoritative balance, ledger, spendability or money movement. |

**Fixture scenario:** Fictional supporter **مؤسسه سپیدار / ORG-DEMO-01**. Fictional roster: **مهتاب نیک‌رفتار / NSM-DEMO-101**; **هما بهاروند / NSM-DEMO-102**; **داریوش شمس / NSM-DEMO-103**. **پروین درخشان / NSM-DEMO-NEW** is a fictional form example. These must never be ingested into Production or AI Training, nor used as real personally identifying records.

Approved UI palette D-0173: emerald `#005543`, warm coral `#A94E43`, soft coral `#FCECE7`, dark coral ink `#702D26`. Screens are editable Persian RTL layers/components/variables, not flattened images.

### Navigation

All four existing supporter web screens from UX-006 and these four new screens now show the **same eight-section visual navigation**:

`نمای کلی` → `افراد تحت حمایت` → `تعریف فرد` → `وضعیت حمایت` → `تأمین مالی` → `گزارش نمونه` → `حوزه‌های حمایت` → `دسترسی و مجوزها`.

Navigation is Figma mockup, not functional app routing or active permissions.

### Implementation controls

- Separately authorize supporter organization, user, person relationships, source-specific permission and legal purpose. Sponsor registering a person is **not** equivalent to changing the elder's Case or adding health data.
- A supporter individual-status read model must explicitly select allowed **support-oriented** fields, never reuse a full Case workspace or overshared export.
- The target funding model is now per-person earmarked credit (D-0175). Financial flows still need accepted funding/account/journal/PSP/settlement and provenance contracts; no invented balance, default success, silent allocation, spending from elder credit, automatic AI funding or real transaction. A child cannot use elder credit via D-0175; D-0170 remains unchanged.
- All fictitious data only under isolated development/design preview. Missing real API/auth/consent/AI results fail safely with honest empty/unavailable states; never substitute fabricated success.
- Prototype review is not testing, code completion, hosted Stage, or release authorization.
