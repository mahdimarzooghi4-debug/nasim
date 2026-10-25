# Sprint 025 — Daily care routines backend foundation

- **Status:** Merged into `main` via PR #46; subsequent full Backend and Web CI passed on PR #52 exact HEAD.
- **Source:** D-0178 and T-027.

## Delivered scope
- Added append-only routine-plan and routine-event records with migration 0010_care_routines.
- Added assigned-caregiver API to create/list plans and record/list explicit occurrence events.
- Required explicit local time, IANA timezone, cadence, and weekly weekdays; no notification or no-response behavior is inferred.
- Added idempotency, audit, outbox metadata, current-assignment checks and capability checks.
- Added source-specific technical and backlog contracts.

## Review boundaries
- Elder self-access, family access, push/SMS channels, scheduler, missed-response routing and role grants remain outside this slice.
- Automated CI is the exact-head validation gate; no Hosted Stage or release is claimed.
