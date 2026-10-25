# PB-025 — Daily care routines: assigned-caregiver backend foundation

**Status:** Implemented in Sprint 025 and present in `main`; full Backend and Web CI passed on follow-on PR #52 exact HEAD.
**Source:** D-0178.

## Scope
- Store immutable, versioned daily/weekly plans with explicit timezone and local time.
- Keep app reminders distinct from caregiver-required tasks.
- Read current plans for the assigned case caregiver.
- Record and read explicit human occurrence events: DONE / NOT_DONE / SKIPPED.
- Preserve audit, idempotency, outbox metadata, and same-case history lineage.
- Fail closed if actor lacks the named care-routine capability or is no longer assigned.

## Not included
No notifications, scheduling worker, auto-generated outcome on no response, elder/family access, medical advice, or role grants. Those require the relevant business and identity decisions.
