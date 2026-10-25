# T-027 — Daily care routine backend foundation

**Source need:** accepted product boundary D-0178. This Technical Slice adds the assigned-caregiver API foundation for recurring routine plans and explicit human occurrence records.

## Contract
- APP_REMINDER means the app is expected to remind; CAREGIVER_TASK means an assigned caregiver action is required. The API preserves the distinction.
- A plan stores local time, an explicit IANA time zone, cadence (DAILY or WEEKLY), and applicable weekdays. No timezone, clock time, channel, or schedule is silently defaulted.
- A plan is immutable. A change or deactivation is represented by a successor plan; the prior version remains auditable.
- A human assigned caregiver can record one explicit DONE, NOT_DONE, or SKIPPED event for a plan/date. A missing event is not interpreted as completion, failure, or emergency.
- Mutations use idempotency keys and write the plan/event, audit entry, outbox metadata, and idempotency response in one transaction. Free-text title and schedule are excluded from the outbox.
- care_routine.*.assigned capabilities are required. This slice does not seed a role grant or infer authority from job titles.

## Explicit boundary
No notification transport/worker, due-instance generation, missed-response escalation, elder self-authentication/access, family access, or care/medical recommendation is implemented. Current Keycloak and Hosted Stage gates still apply. The caregiver-facing assigned-case API is not a claim that the elder mobile client is ready.
