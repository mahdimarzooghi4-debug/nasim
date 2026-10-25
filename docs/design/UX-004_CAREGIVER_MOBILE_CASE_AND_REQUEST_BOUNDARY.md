# UX-004 — Caregiver Mobile Professional Workbench: Authorized Casework versus Future Elder Request Intake

- **Status:** Editable Figma prototype / design evidence. Not operational approval.
- **Date:** 2026-10-09
- **Figma page:** https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=27-2
- **Decision packet:** [DC-021](../business/closure/DC-021_ELDER_REQUEST_HUMAN_REVIEW_DECISION_PACKET.md)
- **Related:** UX-003, D-0171/0172 and T-012.

## 1. Five editable React Native-target caregiver screens

| Design | Node | Contract boundary |
|---|---|---|
| **C01 — Current assigned Cases** | [27:51](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=27-51) | Mirrors existing guarded `GET /api/v1/cases` fields only; `ELDER-DEMO-*` sample values are fictitious, no "priority"/review inbox interpretation. |
| **C02 — Current Case workspace** | [27:109](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=27-109) | Existing authorized observations, recorded Needs, Referrals and Follow-ups are **records** not verified service outcomes. |
| **C03 — HUMAN `NEED_CAPTURE` form specimen** | [27:180](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=27-180) | Existing server command requires exact current-assignment and scoped capability; mobile form is NOT connected. No automatic mutation or falsely prefilled occurred_at. |
| **C04 — Elder-originated human-review request intake** | [27:234](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=27-234) | **Future conceptual flow only**. No request creation command, queue, assigned task list, status enum or delivery guarantee exists. Does not fabricate work items. |
| **C05 — Professional caregiver AI guidance** | [27:294](https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=27-294) | Draft-only assistance; AI cannot record Need, diagnose, choose Provider, commit Referral or confirm payment/outcome. Not connected to a Production model. |

## 2. Navigation & design quality

- Consistent 4-destination RTL bottom navigation **پرونده‌ها · ثبت · پیگیری · دستیار** as editable component sets `Caregiver Nav / cases`, `/ record`, `/ follow`, `/ ai`.
- Shared Nasim emerald/olive UI token palette and `Vazirmatn` typography, editable Figma vectors/text, 52px primary visual targets, separate header for *caregiver's own identity*.
- The professional app is separate from elder/family dual-mode app; both use shared Python/FastAPI Backend, but never share credentials, permissions or inferred case relationships.
- All placeholders are explicit. Missing real data is represented as missing/unavailable, not green/safe/approved/handled.
- Figma screens have no interactive API/production AI and are not real accessibility/QA acceptance; evaluate native scaling, talkback and older-adult experience later.

## 3. Trace to existing technical contracts

- **Read existing only:** `GET /api/v1/cases`, Case read/journey workspace and related independent record reads, gated by `case.read.assigned` / `case.read.oversight` and separate referral capabilities.
- **Human write already present on Backend:** `POST /api/v1/cases/{case_id}/observations` with `record_type=NEED_CAPTURE|OBSERVATION`, explicit `occurred_at` and `expected_current_assignment_id`. UI is non-operational mock; 201 must trigger fresh read, 401/403/409 must fail closed in a future mobile implementation.
- **Not existing:** receiving requests from elder mobile, sending notices to professional mobile, queue/assignment/status of requests, and accessible elder read receipt. These await DC-021 acceptance and separate Technical contracts.

**Release rule:** No claimed PSP, AI runtime, identity integration, Stage admission, merge or Production deployment. This page documents design, not shipped software.
