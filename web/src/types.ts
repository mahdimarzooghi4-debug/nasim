/** Strictly existing read models from Nasim's FastAPI OpenAPI contracts. */

export type ActorType = "HUMAN" | "SYSTEM" | "AI" | "AUTOMATION";
export interface ActorContext {
  actor_id: string;
  actor_type: ActorType;
  capabilities: string[];
  correlation_id: string;
}
export interface Page<T> { items: T[]; next_cursor: string | null }
export interface CaseView {
  id: string; upstream_enrollment_ref: string; created_at: string;
  created_by_actor_id: string; created_by_actor_type: ActorType;
}
export interface ProfileView {
  id: string; case_id: string; revision_no: number; elder_reference: string;
  supersedes_revision_id: string | null; correction_reason: string | null;
  recorded_at: string; recorded_by_actor_id: string; recorded_by_actor_type: ActorType;
}
export interface AssignmentView {
  id: string; case_id: string; caregiver_actor_id: string; started_at: string;
  ended_at: string | null; assigned_by_actor_id: string;
  assigned_by_actor_type: ActorType; reason: string;
}
export interface CaseProfileView {
  case: CaseView; profile: ProfileView; current_assignment: AssignmentView;
}
export interface ObservationView {
  id: string; case_id: string; record_type: "OBSERVATION" | "NEED_CAPTURE";
  occurred_at: string; content: string; recorded_at: string;
  recorded_by_actor_id: string; recorded_by_actor_type: ActorType;
  supersedes_observation_id: string | null; correction_reason: string | null;
}
export interface ReferralView {
  id: string; case_id: string; source_need_observation_id: string;
  created_at: string; created_by_actor_id: string; created_by_actor_type: ActorType;
  reason: string; correlation_id: string;
}
export interface FollowUpView {
  id: string; referral_id: string; recorded_at: string;
  recorded_by_actor_id: string; recorded_by_actor_type: ActorType;
  note: string; reason: string; correlation_id: string;
}
export interface CareJourneyWorkspaceView {
  case: CaseProfileView;
  observations: Page<ObservationView>;
  referrals: Page<ReferralView>;
  selected_referral: ReferralView | null;
  follow_ups: Page<FollowUpView> | null;
}
export interface ProviderCandidateView {
  id: string; display_name: string; registered_at: string;
  registered_by_actor_id: string; registered_by_actor_type: ActorType;
  reason: string; correlation_id: string;
}
export interface ProviderEvidenceView {
  id: string; provider_candidate_id: string; evidence_label: string;
  evidence_reference: string; recorded_at: string; recorded_by_actor_id: string;
  recorded_by_actor_type: ActorType; reason: string; correlation_id: string;
}
export interface ProviderReviewRequestView {
  id: string; provider_candidate_id: string; requested_at: string;
  requested_by_actor_id: string; requested_by_actor_type: ActorType;
  reason: string; correlation_id: string;
}
export interface ProviderWorkspaceView {
  candidate: ProviderCandidateView;
  evidence: Page<ProviderEvidenceView>;
  review_requests: Page<ProviderReviewRequestView>;
}
