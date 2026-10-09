/** Existing TS-03 Case creation, reassignment and contact registration only. */

import { ApiError } from "./api";
import type { ActorContext, AssignmentView, CaseProfileView } from "./types";

export interface CreateCaseInput {
  upstream_enrollment_ref: string;
  elder_reference: string;
  initial_caregiver_actor_id: string;
}
export interface ReassignCaseInput {
  expected_current_assignment_id: string;
  caregiver_actor_id: string;
  reason: string;
}
export interface CreateContactInput {
  expected_current_assignment_id: string;
  contact_kind: string;
  contact_value: string;
}
export interface ContactRecord {
  id: string;
  case_id: string;
  logical_contact_id: string;
  revision_no: number;
  contact_kind: string;
  contact_value: string;
  recorded_at: string;
  recorded_by_actor_id: string;
  recorded_by_actor_type: string;
  supersedes_revision_id: string | null;
  correction_reason: string | null;
}

const uuid = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
export function validId(value: string): boolean { return uuid.test(value); }

export function mayManageCases(actor: ActorContext): boolean {
  return actor.actor_type === "HUMAN" &&
    actor.capabilities.includes("case.assignment.manage");
}
export function mayRecordContact(actor: ActorContext, currentCaregiver: string): boolean {
  return actor.actor_type === "HUMAN" &&
    actor.actor_id === currentCaregiver &&
    actor.capabilities.includes("case.contact.manage.assigned");
}

export function newIntentKey(): string {
  if (typeof globalThis.crypto?.randomUUID !== "function") {
    throw new ApiError(0, "SECURE_RANDOM_UNAVAILABLE");
  }
  return globalThis.crypto.randomUUID();
}

type CaseAction = "create" | "reassign" | "contact";
type Payloads = {
  create: CreateCaseInput;
  reassign: ReassignCaseInput;
  contact: CreateContactInput;
};
type Results = {
  create: CaseProfileView;
  reassign: AssignmentView;
  contact: ContactRecord;
};

function checkText(value: string, max: number): void {
  if (!value.trim() || value.length > max) {
    throw new ApiError(422, "REQUIRED_RECORD_TEXT");
  }
}
export function verifyCasePayload<K extends CaseAction>(
  kind: K, caseId: string | null, payload: Payloads[K], key: string,
): void {
  if (!uuid.test(key)) throw new ApiError(422, "INVALID_IDEMPOTENCY_KEY");
  if (kind !== "create" && (!caseId || !uuid.test(caseId))) {
    throw new ApiError(422, "INVALID_RECORD_REFERENCE");
  }
  if (kind === "create") {
    const input = payload as CreateCaseInput;
    checkText(input.upstream_enrollment_ref, 200);
    checkText(input.elder_reference, 200);
    checkText(input.initial_caregiver_actor_id, 200);
  } else if (kind === "reassign") {
    const input = payload as ReassignCaseInput;
    if (!uuid.test(input.expected_current_assignment_id)) {
      throw new ApiError(422, "INVALID_RECORD_REFERENCE");
    }
    checkText(input.caregiver_actor_id, 200);
    checkText(input.reason, 10000);
  } else {
    const input = payload as CreateContactInput;
    if (!uuid.test(input.expected_current_assignment_id)) {
      throw new ApiError(422, "INVALID_RECORD_REFERENCE");
    }
    checkText(input.contact_kind, 100);
    checkText(input.contact_value, 10000);
  }
}

export async function submitCaseAction<K extends CaseAction>(
  kind: K, caseId: string | null, payload: Payloads[K], key: string,
  signal?: AbortSignal,
): Promise<Results[K]> {
  verifyCasePayload(kind, caseId, payload, key);
  const base = "/api/v1/cases";
  const path = kind === "create" ? base
    : base + "/" + encodeURIComponent(caseId!) +
      (kind === "reassign" ? "/reassignments" : "/contacts");

  let response: Response;
  try {
    response = await fetch(path, {
      method: "POST",
      mode: "same-origin",
      credentials: "same-origin",
      redirect: "error",
      cache: "no-store",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "Idempotency-Key": key,
      },
      signal,
      body: JSON.stringify(payload),
    });
  } catch (error) {
    if (signal?.aborted) throw error;
    throw new ApiError(0, "NETWORK_UNAVAILABLE");
  }
  if (!response.ok) {
    throw new ApiError(response.status,
      response.status === 401 ? "AUTHENTICATION_REQUIRED"
        : response.status === 403 ? "ACCESS_DENIED"
          : response.status === 404 ? "NOT_FOUND"
            : response.status === 409 ? "CONFLICT"
              : response.status === 422 ? "VALIDATION_ERROR" : "REQUEST_FAILED");
  }
  if (response.status !== 201 ||
    !(response.headers.get("content-type") ?? "").includes("application/json")) {
    throw new ApiError(502, "INVALID_API_RESPONSE");
  }
  try { return await response.json() as Results[K]; }
  catch { throw new ApiError(502, "INVALID_API_RESPONSE"); }
}
