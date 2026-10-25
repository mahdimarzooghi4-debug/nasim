# SG-008 — Referral Follow-up Record Foundation Business Gate

- Date: 2026-10-09
- Result: **FOUNDATION ONLY** for recording an accountable human note against an already recorded Referral.
- Basis: D-0118 / D-0124 / D-0012 / D-0013 / D-0014 / D-0015 / D-0021 / D-0028, SG-003 and BC-003 §§2,6,9; BC-016 §24.
- This local Slice gate does **not** promote draft BC-003/BC-016 to accepted contracts.

## Explicit narrowly admitted behavior

The assigned, explicitly authorized **human** Caregiver may append an immutable descriptive record of a follow-up attempt/activity to an existing Referral. Record is only an actor-attested note, not proof of communication, Provider service, clinical judgement, complaint resolution or improved elder condition. Same Referral may have many such records. The system captures actual database recording time and trustworthy actor/type/correlation metadata. All accepted writes preserve audit/outbox/idempotency atomically and the raw note does not appear in the outbox/AI learning data.

Reading notes requires a separate explicitly granted read capability and current assignment, or a separate read oversight capability. Provider, Elder, Family and AI receive no implicit access. ActorType/title alone never conveys authority. There is no final organization Role→Permission mapping; technical vocabulary is seeded **without grants**.

## OPEN — explicitly not decided

Follow-up cadence/owner by phase, SLA, response/non-response classification, contact channel, satisfaction scale, evidence trust and corroboration, escalation, emergency path, cancellation/closure, Provider selection or Provider response, Service completion, Need Resolution, Outcome, Consent and external sharing remain **OPEN**. These records cannot advance Referral status or authorize Provider activation/selection.

## Gate sequence

SG-008 → T-008 → PB-008 → Sprint 008 → Code → Code Review (Draft PR).

Hosted Stage remains unavailable per D-0130. Do not mark Ready for Review, merge or deploy without separate explicit instruction.
