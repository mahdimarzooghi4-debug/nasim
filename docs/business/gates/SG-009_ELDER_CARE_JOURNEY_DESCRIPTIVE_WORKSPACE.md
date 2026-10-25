# SG-009 — Elder Care Journey Descriptive Read Workspace

- Date: 2026-10-09
- Status: **READ-ONLY FOUNDATION / TECHNICAL COMPOSITION GATE**, not service completion or an approved new Business Policy.
- Source: accepted TS-03 Case/Need scope (D-0119…D-0125, SG-001/T-001), bounded Referral record foundation (SG-003/T-003), human follow-up foundation (SG-008/T-008), shared TS-05 capability-based identity model (SG-002/T-002).
- Integration prerequisite: Draft PR #20 `522c9498d58cb4e4debd0df7e3ea90305c27b1b3`. This is not merged into main.

## Narrow derived behavior

Compose **existing module-owned read contracts** for one Case: CaseProfileView, a bounded independently paginated Case Observation history, bounded Referral records and, optionally, a bounded history of human notes against one explicitly selected Referral belonging to the Case. This is purely the data needed to *inspect* the already-recorded chain; there are no new writes or new state machines.

Require the intersection of each context's existing read permissions, checked again by each owner:
- `case.read.assigned` OR `case.read.oversight`;
- `referral.read.assigned` OR `referral.read.oversight`;
- `referral.follow_up.read.assigned` OR `referral.follow_up.read.oversight`.
No actor/role gains any permission from this composition. AI remains denied. Read must fail as a whole when a required context denies access, with no partial response.

## Exclusions and facts this view does not claim

This view is **not** an immutable cross-service snapshot. Its owner contexts are queried individually; it must not imply current need sufficiency, reviewed truth, final eligibility, signed Provider qualification, service availability, provider selection, accepted referral, scheduling, completed service, satisfaction, Outcome, Reassessment, or AI training eligibility. A Referral ID outside the requested Case must not expose follow-up records. Current assignment is checked on the owner service reads. Zero records is not zero need. No inferred Dashboard KPI or task queue.

Provider activation, triage, resolution, SLA, real consent/legal basis, retention, external sharing, and source-of-truth integrations remain contextual OPEN decisions. This descriptive composition does not accept any such decision.

Gate route: SG-009 → T-009 → PB-009 → Sprint 009 → tests/code → Draft PR → exact-head CI → technical Code Review. D-0130 Hosted Stage unavailable. No Merge, Ready for Review, Production, or independent human approval is implied.
