# PB-013 — Provider Candidate Intake Web

Status: Implementation backlog for **existing accepted descriptive Provider Registry writes** only.

- PV-013-01 P0: registered human operations staff with `provider_candidate.register` may record new Candidate name and reason.
- PV-013-02 P0: selected Candidate, exact `provider_qualification_evidence.record` may append submitted evidence label/opaque reference/reason.
- PV-013-03 P0: selected Candidate, exact `provider_qualification_review.request` may append descriptive request reason.
- PV-013-04 P0: no privilege escalation from write grants to directory read or qualification approval; no automatic AI, Provider choice, service/capacity/status derivation.
- PV-013-05 P0: crypto idempotency, same-origin security, fail-closed 401/403/404/409, re-read after accepted 201, no raw server message exposure.
- PV-013-06 P0: Web contract/SSR tests, exact-head Web and complete Backend CI, nonapproving technical review, Draft PR only.

Blocked out of scope: real IdP/Origin-CSRF/session policy, encrypted document storage and scanner, legal sharing, qualification criteria, reviewer authority, Provider activation/dispatch, Outcome, AI Training, external integrations, Stage/QA/Release/Production. No invented Role or Actor grants.
