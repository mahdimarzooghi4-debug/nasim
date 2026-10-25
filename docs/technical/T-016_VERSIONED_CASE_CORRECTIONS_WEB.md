# T-016 — Append-Only Case Corrections UI / Exact TS-03 Contracts

Status: **Existing backend correction contract wiring only.** The four POST APIs and immutable persistence already exist; no Backend schema migration or new Role grant.

- `POST /api/v1/cases/{case_id}/profile/corrections`: `expected_current_assignment_id`, `expected_current_revision_id`, `elder_reference`, `correction_reason`; `case.assignment.manage`; returns ProfileView (201).
- `POST /api/v1/cases/{case_id}/contacts/{logical_contact_id}/corrections`: `expected_current_assignment_id`, `expected_current_revision_id`, `contact_kind`, `contact_value`, `correction_reason`; `case.contact.manage.assigned`; returns ContactView (201).
- `POST /api/v1/cases/{case_id}/interactions/{interaction_id}/corrections`: `expected_current_assignment_id`, `expected_current_record_id`, `interaction_type`, `occurred_at`, `content`, `correction_reason`; `case.monitor.assigned`; 201 InteractionView.
- `POST /api/v1/cases/{case_id}/observations/{observation_id}/corrections`: `expected_current_assignment_id`, `expected_current_record_id`, `record_type`, `occurred_at`, `content`, `correction_reason`; `case.observe.assigned`; 201 ObservationView.

Reads: existing authorized Profile, existing Contacts history, bounded `GET /api/v1/cases/{id}/interactions|observations?cursor&limit=20`. Contacts are grouped by logical_contact_id and latest revision_no for form selection; Backend **still** validates current version atomically. Interaction/Observation lists are bounded recorded history; records may have later successors not on the page; never claim their currentness. UI makes no unbounded data source queries or cross-context joins.

Security: Browser identity is **not implemented** under Sprint 015 deny-only boundary. Mutations use existing same-origin JSON 201 response and crypto UUID Idempotency-Key reused only for *identical* payload after uncertain failure, rotated on edit/success. 401 closes protected UI; 403/409 fail closed; 409 triggers authoritative refresh/human review. Never silently choose a new expected version, auto-retry with new key, edit DB history in place, or infer eligibility from corrected data. No localStorage, HTML injection, token or custom Actor header.

Testing: TypeScript strict, four exact URL/body/header and negative 401/403/409/time/currentness cases, SSR role/assignee denial, contact logical revision selection, independent bounded reads, Web CI and inherited full Backend CI on exact final SHA. Browser E2E with approved identity, Origin+CSRF, independent QA and hosted Stage are blocked.
