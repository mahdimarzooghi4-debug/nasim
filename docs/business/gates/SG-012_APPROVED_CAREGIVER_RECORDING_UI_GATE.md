# SG-012 — Approved Caregiver Recording UI Gate

- Date: 2026-10-09
- Result: **FOUNDATION ONLY / Existing Backend Commands**, not new service or outcome policy.
- Source: accepted SG-001/T-001 TS-03 Case Observation/Interaction and SG-003/T-003 Referral recording; SG-008/T-008 Human Referral Follow-up; SG-011/T-011 trusted, fail-closed read-only web baseline.
- Depends on still-unmerged Draft PR #23 (HEAD 69867fe4760ef561bb17dcfd7b1b0cdc0a43af62); this is NOT authorization to merge.

## Scope

A real authenticated and explicitly authorized **current human caregiver** can submit the already-accepted immutable backend records for observed Need/Observation, CONTACT/MONITORING, descriptive Referral against an existing NEED_CAPTURE record, or descriptive human follow-up note against an existing Referral. A backend pre-existing permission and current assignment gate applies to every write; the UI makes no role assumptions and invents no write to Provider, Service, Outcome, consent, emergency or AI.

The operator explicitly sees/chooses event time; a human-provided reason is required for Referral and Follow-up. If the record's source is stale after correction or assignment changed, backend fails closed with 409. UI never repairs inferred source/currentness or guesses who owns a Case.

## Non-decisions

No Role→Permission mapping, IdP/provider, CSRF/session policy, Provider dispatch, approval, acceptance, completed service, resolved need, Outcome, Training eligibility, diagnosis, service cost, SLA or triage criterion is decided. A human descriptive Follow-up is not independent verification of a service. Signed operating authentication and privacy/consent policy remain open; without them the UI is deliberately inaccessible.

Authorized development flow: SG-012 → T-012 → PB-012 → Sprint 012 → Code/tests → exact-head Web+Backend CI → technical Code Review. D-0130 Hosted Stage unavailable; keep all PRs Draft/Open and do not merge/deploy without explicit instruction.
