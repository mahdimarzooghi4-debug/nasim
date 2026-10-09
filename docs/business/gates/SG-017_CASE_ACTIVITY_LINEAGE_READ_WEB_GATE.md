# SG-017 — Case Activity / Revision Lineage Read Web Gate

Date 2026-10-09. Status: **FOUNDATION ONLY / existing approved Casework reads**, not a new case outcome, Referral status or formal audit approval. Source: SG-001/T-001 TS-03 immutable case events and read models; SG-010/T-010 authorized Case index; SG-011/T-011 real same-origin web foundation; SG-014/T-014 management reads; SG-016/T-016 immutable corrections. Underlying still-unmerged Draft PR #28 HEAD `f5575e9b644faf0158a0cfd555db11473a3d7f08`.

Purpose: make the original Casework technical audit trail inspectable by already-authorized human Case readers, including recorded action and actor, before/after resource IDs, correlation/reason, historical assignment start/end and correction-chain references for Interaction and Observation. A Casework timeline is bounded to **Casework AuditEntry actions only**, not a comprehensive Provider, Referral, payment, clinical or verified Outcome event log.

Permissions are not inferred: only existing `case.read.assigned` on the *currently assigned human* or `case.read.oversight` can see this view. AI cannot read it. A manager's `case.assignment.manage` write grant **does not become Case read**. The Backend rechecks all permissions and current assignment on every page fetch. No fictitious statuses, deadlines, action recommendations, eligibility, Provider rating, outcome metrics or AI interpretation.

The temporal view is a succession of individual paginated reads; it is not a frozen full-history snapshot and can change as additional records are entered. The assignment list is existing full read, not an invented paginated contract. Event IDs are opaque technical references, not adjudicated facts. Raw Case reason text is shown only behind Case read authorization and never sent to external analytics or Training.

Delivery: SG-017 → T-017 → PB-017 → Sprint 017 → typed API / UI → TS/SSR contract tests → same-SHA Web+Backend CI → AI-assisted nonapproving code review. D-0130 Stage unavailable and real browser identity / Origin+CSRF remains unconfigured; keep PRs Draft/Open and no Merge/Production without explicit owner instruction.
