/** Exactly the immutable correction contracts already implemented by TS-03. */
import { ApiError } from "./api";
import { toObservedUtc } from "./commands";
import type { ActorContext, ProfileView, ObservationView } from "./types";
import type { ContactRecord } from "./caseCommands";

export type CorrectionKind = "profile" | "contact" | "interaction" | "observation";
export type InteractionRecorded = {
  id: string; case_id: string; interaction_type: "CONTACT" | "MONITORING";
  occurred_at: string; content: string; recorded_at: string;
  recorded_by_actor_id: string; recorded_by_actor_type: string;
  supersedes_interaction_id: string | null; correction_reason: string | null;
};
type Common = {
  expected_current_assignment_id: string;
  correction_reason: string;
};
export type ProfileCorrection = Common & {
  expected_current_revision_id: string; elder_reference: string;
};
export type ContactCorrection = Common & {
  expected_current_revision_id: string; contact_kind: string; contact_value: string;
};
export type InteractionCorrection = Common & {
  expected_current_record_id: string;
  interaction_type: "CONTACT" | "MONITORING";
  occurred_at: string;
  content: string;
};
export type ObservationCorrection = Common & {
  expected_current_record_id: string;
  record_type: "OBSERVATION" | "NEED_CAPTURE";
  occurred_at: string;
  content: string;
};
export type CorrectionInputs = {
  profile: ProfileCorrection;
  contact: ContactCorrection;
  interaction: InteractionCorrection;
  observation: ObservationCorrection;
};
export type CorrectionResults = {
  profile: ProfileView;
  contact: ContactRecord;
  interaction: InteractionRecorded;
  observation: ObservationView;
};
const uuid = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
export function correctionAllowed(
  actor: ActorContext, kind: CorrectionKind, currentCaregiver: string,
): boolean {
  if (actor.actor_type !== "HUMAN") return false;
  if (kind === "profile") return actor.capabilities.includes("case.assignment.manage");
  const grant = kind === "contact" ? "case.contact.manage.assigned"
    : kind === "interaction" ? "case.monitor.assigned" : "case.observe.assigned";
  return actor.actor_id === currentCaregiver && actor.capabilities.includes(grant);
}

function nonEmpty(s: string, max: number): void {
  if (!s.trim() || s.length > max) throw new ApiError(422, "REQUIRED_RECORD_TEXT");
}
export function validateCorrection<K extends CorrectionKind>(
  kind: K, caseId: string, recordId: string | null,
  body: CorrectionInputs[K], key: string,
): void {
  if (!uuid.test(caseId) || !uuid.test(key) ||
      !uuid.test(body.expected_current_assignment_id)) {
    throw new ApiError(422, "INVALID_RECORD_REFERENCE");
  }
  nonEmpty(body.correction_reason, 10000);
  if (kind !== "profile" && (!recordId || !uuid.test(recordId))) {
    throw new ApiError(422, "INVALID_RECORD_REFERENCE");
  }
  if (kind === "profile") {
    const input = body as ProfileCorrection;
    if (!uuid.test(input.expected_current_revision_id)) {
      throw new ApiError(422, "INVALID_RECORD_REFERENCE");
    }
    nonEmpty(input.elder_reference, 200);
  } else if (kind === "contact") {
    const input = body as ContactCorrection;
    if (!uuid.test(input.expected_current_revision_id)) {
      throw new ApiError(422, "INVALID_RECORD_REFERENCE");
    }
    nonEmpty(input.contact_kind, 100); nonEmpty(input.contact_value, 10000);
  } else if (kind === "interaction") {
    const input = body as InteractionCorrection;
    if (!uuid.test(input.expected_current_record_id) ||
      !["CONTACT", "MONITORING"].includes(input.interaction_type)) {
      throw new ApiError(422, "INVALID_RECORD_REFERENCE");
    }
    nonEmpty(input.content, 10000);
    toObservedUtc(input.occurred_at);
  } else {
    const input = body as ObservationCorrection;
    if (!uuid.test(input.expected_current_record_id) ||
      !["OBSERVATION", "NEED_CAPTURE"].includes(input.record_type)) {
      throw new ApiError(422, "INVALID_RECORD_REFERENCE");
    }
    nonEmpty(input.content, 10000);
    toObservedUtc(input.occurred_at);
  }
}

export async function submitCorrection<K extends CorrectionKind>(
  kind: K, caseId: string, recordId: string | null,
  body: CorrectionInputs[K], key: string, signal?: AbortSignal,
): Promise<CorrectionResults[K]> {
  validateCorrection(kind, caseId, recordId, body, key);
  const prefix = "/api/v1/cases/" + encodeURIComponent(caseId);
  const route = kind === "profile" ? "/profile/corrections"
    : kind === "contact" ? "/contacts/" + encodeURIComponent(recordId!) + "/corrections"
      : kind === "interaction" ? "/interactions/" + encodeURIComponent(recordId!) + "/corrections"
        : "/observations/" + encodeURIComponent(recordId!) + "/corrections";
  let response: Response;
  try {
    response = await fetch(prefix + route, {
      method: "POST", credentials: "same-origin", mode: "same-origin",
      redirect: "error", cache: "no-store", signal,
      headers: {
        Accept: "application/json", "Content-Type": "application/json", "Idempotency-Key": key,
      },
      body: JSON.stringify(body),
    });
  } catch (error) {
    if (signal?.aborted) throw error;
    throw new ApiError(0, "NETWORK_UNAVAILABLE");
  }
  if (!response.ok) {
    throw new ApiError(response.status, response.status === 401 ? "AUTHENTICATION_REQUIRED"
      : response.status === 403 ? "ACCESS_DENIED"
        : response.status === 404 ? "NOT_FOUND"
          : response.status === 409 ? "CONFLICT"
            : response.status === 422 ? "VALIDATION_ERROR" : "REQUEST_FAILED");
  }
  if (response.status !== 201 ||
      !(response.headers.get("content-type") ?? "").includes("application/json")) {
    throw new ApiError(502, "INVALID_API_RESPONSE");
  }
  try { return await response.json() as CorrectionResults[K]; }
  catch { throw new ApiError(502, "INVALID_API_RESPONSE"); }
}

export function latestContactRevisions(records: ContactRecord[]): ContactRecord[] {
  // The API returns every immutable Contact revision. Display only the latest
  // revision per logical contact; the backend still checks exact currentness.
  const byLogicalId = new Map<string, ContactRecord>();
  for (const row of records) {
    const prior = byLogicalId.get(row.logical_contact_id);
    if (!prior || row.revision_no > prior.revision_no) byLogicalId.set(row.logical_contact_id, row);
  }
  return [...byLogicalId.values()];
}
