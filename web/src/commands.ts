/** Existing approved TS-03/Referral writes only. No new lifecycle or provider actions. */
import { ApiError } from "./api";
import type { ActorContext, FollowUpView, ObservationView, ReferralView } from "./types";

export type RecordingKind = "observation" | "interaction" | "referral" | "follow_up";
export type ObservationKind = "OBSERVATION" | "NEED_CAPTURE";
export type InteractionKind = "CONTACT" | "MONITORING";

export interface ObservationCommand {
  expected_current_assignment_id: string;
  record_type: ObservationKind;
  occurred_at: string;
  content: string;
}
export interface InteractionCommand {
  expected_current_assignment_id: string;
  interaction_type: InteractionKind;
  occurred_at: string;
  content: string;
}
export interface ReferralCommand {
  expected_current_assignment_id: string;
  source_need_observation_id: string;
  reason: string;
}
export interface FollowUpCommand {
  expected_current_assignment_id: string;
  note: string;
  reason: string;
}
export interface InteractionRecorded {
  id: string;
  case_id: string;
  interaction_type: InteractionKind;
  occurred_at: string;
  content: string;
}
export type RecordingResponse = ObservationView | InteractionRecorded | ReferralView | FollowUpView;

const capabilityByKind: Record<RecordingKind, string> = {
  observation: "case.observe.assigned",
  interaction: "case.monitor.assigned",
  referral: "referral.create.assigned",
  follow_up: "referral.follow_up.record.assigned",
};

export function canRecord(
  actor: ActorContext,
  kind: RecordingKind,
  assignedActorId: string,
): boolean {
  // UI hiding is advisory; every POST requires server-side assignment and capability checks.
  return actor.actor_type === "HUMAN" &&
    actor.actor_id === assignedActorId &&
    actor.capabilities.includes(capabilityByKind[kind]);
}

export function makeIdempotencyKey(): string {
  if (typeof crypto === "undefined" || typeof crypto.randomUUID !== "function") {
    // Never downgrade to a predictable/randomness-free mutation identity.
    throw new ApiError(0, "SECURE_RANDOM_UNAVAILABLE");
  }
  return crypto.randomUUID();
}

export function toObservedUtc(localDateTime: string): string {
  const date = new Date(localDateTime);
  if (!localDateTime.trim() || !Number.isFinite(date.getTime())) {
    throw new ApiError(422, "INVALID_EVENT_TIME");
  }
  return date.toISOString();
}

type KindBody = {
  observation: ObservationCommand;
  interaction: InteractionCommand;
  referral: ReferralCommand;
  follow_up: FollowUpCommand;
};

function assertUuid(value: string): void {
  if (!/^[a-f\d]{8}-[a-f\d]{4}-[1-8][a-f\d]{3}-[89ab][a-f\d]{3}-[a-f\d]{12}$/i.test(value)) {
    throw new ApiError(422, "INVALID_RECORD_REFERENCE");
  }
}

function validateText(value: string): void {
  if (!value.trim()) throw new ApiError(422, "REQUIRED_RECORD_TEXT");
}
function validatePayload(kind: RecordingKind, body: KindBody[RecordingKind]): void {
  assertUuid(body.expected_current_assignment_id);
  if (kind === "observation") {
    const c = body as ObservationCommand;
    if (!["OBSERVATION", "NEED_CAPTURE"].includes(c.record_type)) {
      throw new ApiError(422, "INVALID_RECORD_TYPE");
    }
    validateText(c.content);
    toObservedUtc(c.occurred_at);
  } else if (kind === "interaction") {
    const c = body as InteractionCommand;
    if (!["CONTACT", "MONITORING"].includes(c.interaction_type)) {
      throw new ApiError(422, "INVALID_RECORD_TYPE");
    }
    validateText(c.content);
    toObservedUtc(c.occurred_at);
  } else if (kind === "referral") {
    const c = body as ReferralCommand;
    assertUuid(c.source_need_observation_id);
    validateText(c.reason);
  } else {
    const c = body as FollowUpCommand;
    validateText(c.note);
    validateText(c.reason);
  }
}

export async function recordCareAction<K extends RecordingKind>(
  kind: K,
  caseId: string,
  referralId: string | null,
  body: KindBody[K],
  key: string,
  signal?: AbortSignal,
): Promise<RecordingResponse> {
  // URLs are assembled only from the finite, reviewed mutation route map.
  assertUuid(caseId);
  assertUuid(body.expected_current_assignment_id);
  validatePayload(kind, body);
  if (!/^[0-9a-f-]{36}$/i.test(key)) {
    throw new ApiError(422, "INVALID_IDEMPOTENCY_KEY");
  }
  if (kind === "follow_up") {
    if (!referralId) throw new ApiError(422, "REFERRAL_SELECTION_REQUIRED");
    assertUuid(referralId);
  }
  const prefix = "/api/v1/cases/" + encodeURIComponent(caseId);
  const path = kind === "observation" ? prefix + "/observations"
    : kind === "interaction" ? prefix + "/interactions"
      : kind === "referral" ? prefix + "/referrals"
        : "/api/v1/referrals/" + encodeURIComponent(referralId!) + "/follow-up-records";
  let response: Response;
  try {
    response = await fetch(path, {
      method: "POST", mode: "same-origin", credentials: "same-origin",
      redirect: "error", cache: "no-store", signal,
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "Idempotency-Key": key,
      },
      body: JSON.stringify(body),
    });
  } catch (error) {
    if (signal?.aborted) throw error;
    throw new ApiError(0, "NETWORK_UNAVAILABLE");
  }
  if (!response.ok) {
    const code = response.status === 401 ? "AUTHENTICATION_REQUIRED"
      : response.status === 403 ? "ACCESS_DENIED"
        : response.status === 409 ? "CONFLICT"
          : response.status === 422 ? "VALIDATION_ERROR"
            : response.status === 404 ? "NOT_FOUND" : "REQUEST_FAILED";
    throw new ApiError(response.status, code);
  }
  if (response.status !== 201 || !(response.headers.get("content-type") ?? "").includes("application/json")) {
    throw new ApiError(502, "INVALID_API_RESPONSE");
  }
  try { return (await response.json()) as RecordingResponse; }
  catch { throw new ApiError(502, "INVALID_API_RESPONSE"); }
}
