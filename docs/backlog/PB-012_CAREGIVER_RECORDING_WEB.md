# PB-012 — Caregiver Recording Workflows

Status: Implementation backlog for **existing approved record commands only**.

- WEB-C12-1 P0: explicitly authorized current human Case caregiver may record OBSERVATION/NEED_CAPTURE with chosen timestamp and entered content.
- WEB-C12-2 P0: explicit CONTACT/MONITORING human interaction records, no communication delivery claim.
- WEB-C12-3 P0: human-only descriptive Referral from a selected recorded NEED_CAPTURE (Backend enforces lineage/currentness); no Provider selection or dispatch.
- WEB-C12-4 P0: human-only Referral follow-up note/reason bound to selected Referral, not outcome.
- WEB-C12-5 P0: browser-safe same-origin POST, crypto idempotency tied to identical request, fail-closed 401/403/409, no optimistic state, fresh read on success.
- WEB-C12-6 P0: unit/SSR contract tests + Web and inherited full Backend CI, technical review and Draft PR.
- WEB-C12-7 P1: document remaining real browser authentication, CSRF, external service and hosted Stage blockers without inventing them.

No final Role→Capability matrix, IdP choice, Provider activation, Service confirmation, outcome/reassessment, AI learning/training, external SMS, data-sharing/consent, Figma approval, Stage, release or Production.
