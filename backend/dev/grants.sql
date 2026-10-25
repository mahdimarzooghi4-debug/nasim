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

-- Inert proposed AI Dataset manifest metadata is never exposed to serving runtime.
-- Neither read nor write access exists until a separately approved policy/worker.
REVOKE ALL ON learning_proposed_manifest, learning_proposed_source, learning_source_purpose_claim FROM nasim_app;
