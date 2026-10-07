-- Run as migration owner in each local database after migrations.
GRANT CONNECT ON DATABASE nasim_dev TO nasim_app;
GRANT CONNECT ON DATABASE nasim_test TO nasim_app;
GRANT USAGE ON SCHEMA public TO nasim_app;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO nasim_app;
GRANT INSERT ON elder_case, case_profile_revision, contact_point_revision,
  case_assignment, case_interaction, case_observation, audit_entry,
  outbox_event, idempotency_record, referral_record,
  provider_candidate_record, provider_qualification_evidence_record,
  provider_qualification_review_request_record TO nasim_app;
GRANT UPDATE (ended_at) ON case_assignment TO nasim_app;
-- SELECT FOR UPDATE requires an UPDATE privilege; immutable trigger forbids actual changes.
GRANT UPDATE (id) ON elder_case TO nasim_app;
