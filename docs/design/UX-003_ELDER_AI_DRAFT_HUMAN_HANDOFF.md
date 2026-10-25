# UX-003 — Nasim Elder AI-assisted Need Expression and Human Handoff

**Status:** Figma editable proposal, NOT an accepted operational workflow or an AI use-case approval.
**Date:** 2026-10-09
**Basis:** D-0004/0005 (Day-one internal AI and controlled Dataset), D-0172 (integrated services + AI elder UX), BC-003 (human need/referral), BC-004/006 (AI assist only), BC-007 (training eligibility), BC-014/022 (privacy and authority).
**Design link:** https://www.figma.com/design/i61F2sxmja12zxmMS1jZNR/Nasim?node-id=25-2

## 1. Editable Figma evidence (four screens)

| Screen | Figma node | Safe prototype purpose |
|---|---|---|
| A01 — Conversation illustration | `25:3` | Elder expresses a sample non-medical social concern. AI illustrative reply helps articulate a need; no clinical/eligibility determination or real conversation. |
| A02 — Proposed text review | `25:76` | A text draft is distinguishable from the official record; elder must be able to review/correct before any formal attempt. Editable text fields are visual specimens, not active data inputs. |
| A03 — Human handoff preview | `25:144` | States owner roles: elder explicit intention → server identity/authorization/consent check → authorized professional elder-care worker human review → official handling under accepted contracts. **No request has been sent.** |
| A04 — Internal AI unavailable | `25:214` | Fail-closed assistant; no fabricated AI response, official status or contact action. Future human contact route must work independently of AI, after integration. |

All screens retain the approved four-icon-and-label navigation via reusable Figma components `Nav / home`, `Nav / services`, `Nav / ai`, and `Nav / follow`, with current AI tab selected. Screens are editable frames/text/vectors, not flattened screenshots.

## 2. Conceptual interaction sequence — not an active API

`Elder expression → optional internal AI explanatory text/draft → elder reviews and intentionally requests human attention → Backend validates identity/permissions/consent and accepts only a contract-valid command → authorized elder-care worker handles/reviews → separately authorized official record/referral/follow-up → independently authorized read model for elder.`

- `AI output != official Need`, `AI output != Referral`, `UI sample != sent command`.
- Keep source/actor, timestamps, AI involvement/model-version provenance and human review separately attributable once the contracts exist; never invent real payload or command endpoints from Figma.
- Do not turn social/mental distress into a diagnosis, score, severity, urgency, priority or clinical intervention. An emergency path remains an explicit policy dependency.
- AI must not select providers, commit financial actions or consume elder credit; D-0170 family-payer boundary remains unchanged.
- Real Operational data must never flow into automatic Training without independent purpose-specific eligibility; automatic Dataset versioning and human-governed model promotion remain distinct.

## 3. UX and accessibility acceptance candidates

- Clearly mark the actor speaking, explicitly label AI responses and visual examples.
- Prominent elder-readable labels, high contrast, predictable four-destination bottom navigation, >=44 px primary tap targets, and one main action per screen.
- Make draft review/correction and deliberate confirmation separate from submission success, with clear error/no-access/network/AI-unavailable and no-data states.
- Avoid exposing a fake human response, fake message delivery, fictional Case state, or non-existent active AI.
- Final target sizes/accessibility acceptance require usability tests with elders and native app QA.

## 4. Open contracts before implementing real behavior

1. Elder mobile identity, case relationship, consent and exact capabilities; family authority separately.
2. Input data schema, validation, responsible actor, review owner and whether a self-service elder "request for human review" command is admitted to the domain.
3. Human review queue semantics and durable statuses, retry/idempotency, conflict and error states.
4. Authorized read model for what the elder may see as confirmation and follow-up; no optimistic fabricated status.
5. Internal inference runtime, specific safe AI prompts/policies, provenance, evaluation and model unavailability behavior.
6. Non-AI human-contact path, urgency/emergency communication policy, notification channel, audit/privacy/retention controls.

**Gate:** Do not infer accepted service catalog, real AI runtime, final workflow, payment PSP, provider dispatch, or production deployment from this design. Draft PR and Stage/Production restrictions remain in force.
