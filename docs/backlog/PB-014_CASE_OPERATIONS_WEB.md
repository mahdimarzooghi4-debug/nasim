# PB-014 — Case Operations Web

Only existing TS-03 human command surfaces, authorized by SG-014/T-014:

- WEB-014-01 P0: assignment manager creates a Case from caller-supplied upstream enrollment and elder reference, with initial caregiver and idempotent 201; no Enrollment validation claim.
- WEB-014-02 P0: manager reassigns a Case with required reason, expected exact current assignment UUID, stale conflict fail-closed and new authoritative server read.
- WEB-014-03 P0: current caregiver with exact contact permission records bounded contact kind/value; no invented catalog, contact validation or delivery effect.
- WEB-014-04 P0: users with only Case read but without Referral read see Case-only profile and contact workspace; assignment manager without read may create without enumerating cases.
- WEB-014-05 P0: no custom actor headers, secure same-origin request/Idempotency-Key, no runtime mocks, 401/403/409 handling, no optimistic business status; TS, Web tests + full Backend CI and technical Code Review.
- WEB-014-06 P0: keep prior PRs Draft/Open, no merge, Stage or Production; document external IdP, CSRF/session, Enrollment source and privacy blockers.

No Case lifecycle closure, emergency, Provider/Referral decision, medical eligibility, Outcome, AI Training, real contact delivery, named Role grant or platform deployment.
