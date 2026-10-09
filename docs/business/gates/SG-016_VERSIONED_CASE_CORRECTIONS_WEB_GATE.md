# SG-016 — Human Versioned Case Corrections in Operational Web

Date: 2026-10-09. **FOUNDATION ONLY**, derived from the accepted TS-03 immutable correction contracts in SG-001/T-001 and the governed read and human write gates SG-009–SG-014. Source Draft PR #27 HEAD `21d16a8868e0e1a8aedc1513d3913ade745989ed` is unmerged.

## Admitted scope

Expose the **already implemented** backend versioned correction commands in a guarded human web workspace: Case Profile reference, Contact revision, Interaction (CONTACT/MONITORING), Observation (OBSERVATION/NEED_CAPTURE). Corrections append a new record, never overwrite/delete original history. Every correction requires human-entered reason and the server-read exact expected assignment and record/revision ID, plus an explicit existing capability. Backend remains authoritative about allowed principal, current assignment, currentness/supersession, conflict and event/audit effects.

A Profile correction is allowed only under existing `case.assignment.manage`. Other corrections require the current assigned HUMAN and each existing record capability (`case.contact.manage.assigned`, `case.monitor.assigned`, `case.observe.assigned`). A Case read grant by itself is not correction authority. An old, corrected or off-page source may be presented as historical; the server must fail closed on stale expected version (409), never auto-rewrite history or infer an acceptable current revision.

Do not infer that correcting a NEED_CAPTURE retroactively closes, reopens or verifies past Referral/Outcome, recalculates eligibility, grants Provider authority, or makes evidence training-eligible. Event occurrence time is a user-visible field, not synthesized by AI; data correction is not external verification or a medical judgment.

Open blockers stay OPEN: real IdP/server session and Origin+CSRF, real consent/legal basis, referral service lifecycle, Outcome, AI dataset eligibility and production activation. No vendor, actor matrix, eligibility rule, calculation or status invented.

Gate: SG-016→T-016→PB-016→Sprint 016→TypeScript/SSR tests→exact-head Web+Backend CI→technical review. D-0130 Stage unavailable; all PRs Draft/Open, no Merge/Ready/QA/Release/Production without explicit instruction.
