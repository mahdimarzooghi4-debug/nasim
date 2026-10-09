# UX-002 — تجربه یکپارچه سالمند، خدمات و دستیار نسیم (ناوبری حرفه‌ای)

**Status:** Approved UX direction from D-0172; Figma mock, not live product.
**Applies to:** elder-facing React Native client and matching family mode (D-0170 / D-0171).

## Navigation (RTL, four persistent destinations)
1. **خانه:** نقطه شروع آرام و واضح، تماس/ارتباط انسانی و مسیر ورود به درخواست کمک، نمایش محتوای مجاز.
2. **خدمات:** Service Family-level education and proposal/request path; no claim that specialist services are active, priced or directly purchasable.
3. **دستیار نسیم:** AI conversations contextualized to service support, simple text prompts and explicit "AI suggestion, not official record" boundary. Voice is exploratory, not a committed active feature.
4. **پیگیری:** approved/read-only status and case/referral information only after real authorization; honest unavailable/empty states, no fictional status.

**Account & permissions** in the page header; each mode is an experience, not an entitlement.

## Target flow
Elder expression (or authorized family input) → AI may explain/help draft → authorized human verifies and explicitly records official need where supported → human-supervised referral to approved professional network when contract permits → human follow-up, status shown only from authoritative backend.

No AI autonomous clinical decision, priority, provider selection, financial approval, record mutation, or service completion.

## Design requirements
- Unified emerald / olive Nasim identity; Vazirmatn Persian with strong contrast and scalable font size.
- Tappable navigation targets and CTA >=44 px in design draft, text hierarchy and clear icon+label pairs, no icon-only required interaction.
- One obvious primary action per screen; avoid dense dashboards for elders.
- Visible identity/authority boundaries; never present mock data, fake "successful payment", active model, real calls or service availability.
- Allow later usability testing with actual elderly users and accessibility QA; no claim of production WCAG conformance without evidence.

## Scope exclusions and unresolved contracts
- Full operational Service Catalog, service booking, direct order, Provider activation, SLA, pricing/PSP, voice channel, medical triage, consent details, permission mapping and family authority are not established here.
- D-0170: family purchase with child's own account *when commercial flow is actually built*; elder credit remains DEFERRED.
- Figma design is editable UX evidence only; backend remains the source of truth for roles, capabilities and records.
