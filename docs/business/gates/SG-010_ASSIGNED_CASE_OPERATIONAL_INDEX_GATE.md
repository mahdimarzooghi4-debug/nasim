# SG-010 — Assigned Case Operational Index Gate

Date: 2026-10-09. Result: **FOUNDATION ONLY / Existing TS-03 Read Contract Extension**.

Sources: SG-001 / T-001 / PB-001 (Case/Profile and current assignment), SG-002 / T-002 (Role Title != Permission, explicit read capability), PR #21 Sprint 009 (descriptive journey workspace). This gate adds no new business power or policy.

The authorized human caregiver needs to *find* currently assigned Cases before opening the already-authorized Case Journey. A read-only, bounded, keyset-paginated index of preexisting Cases is admitted as technical composition. Explicit `case.read.assigned` means **only** the actor's current Case assignments; explicit `case.read.oversight` permits the existing bounded oversight read. A Role title, mere assignment or `case.assignment.manage` alone never grants read. AI remains denied even with capabilities. The output contains existing Case/Profile/current Assignment views only, not new sensitive data classes, status, priority, due dates, KPI, Need severity, Referral dispatch, Provider activation, Outcome, or automatically inferred work.

The index does not resolve identity-provider decisions, cross-role access rights, onboarding/enrollment validity, Family/Provider access, Provider status, close/resolution, medical judgment, SLA or consent. All remain OPEN as defined in BR-004. Only current-assignment rows are accessible; reassignment revokes old caregiver visibility on subsequent reads. No free-form global user filter, no impersonation and no new role grants.

Order: Business SG-010 → Technical T-010 → Backlog PB-010 → Sprint 010 → contracts/tests/code → Draft PR → exact-head full CI → technical Code Review. Hosted Stage remains unavailable under D-0130. PRs #14–#21 remain Draft/Open; no merge, Ready for Review, or Production without explicit owner instruction.
