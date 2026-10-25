import { ApiError } from "./api";

export type CareRoutineEventStatus = "DONE" | "NOT_DONE" | "SKIPPED";

export interface RecordCareRoutineEventCommand {
  expected_current_assignment_id: string;
  occurrence_date: string;
  status: CareRoutineEventStatus;
  occurred_at: string;
}

export interface RecordedCareRoutineEvent {
  id: string;
  case_id: string;
  routine_id: string;
  occurrence_date: string;
  status: CareRoutineEventStatus;
  occurred_at: string;
  recorded_at: string;
  recorded_by_actor_id: string;
  recorded_by_actor_type: string;
  correlation_id: string;
}

function assertUuid(value: string): void {
  if (!/^[a-f\d]{8}-[a-f\d]{4}-[1-8][a-f\d]{3}-[89ab][a-f\d]{3}-[a-f\d]{12}$/i.test(value)) {
    throw new ApiError(422, "INVALID_RECORD_REFERENCE");
  }
}

export function makeCareRoutineIdempotencyKey(): string {
  if (typeof crypto === "undefined" || typeof crypto.randomUUID !== "function") {
    throw new ApiError(0, "SECURE_RANDOM_UNAVAILABLE");
  }
  return crypto.randomUUID();
}

export async function recordCareRoutineEvent(
  caseId: string,
  routineId: string,
  command: RecordCareRoutineEventCommand,
  key: string,
): Promise<RecordedCareRoutineEvent> {
  assertUuid(caseId);
  assertUuid(routineId);
  assertUuid(command.expected_current_assignment_id);
  if (!/^[0-9a-f-]{36}$/i.test(key)) {
    throw new ApiError(422, "INVALID_IDEMPOTENCY_KEY");
  }
  if (!/^\d{4}-\d{2}-\d{2}$/.test(command.occurrence_date) ||
      !Number.isFinite(Date.parse(command.occurred_at)) ||
      !["DONE", "NOT_DONE", "SKIPPED"].includes(command.status)) {
    throw new ApiError(422, "INVALID_EVENT");
  }
  let response: Response;
  try {
    response = await fetch(
      "/api/v1/cases/" + encodeURIComponent(caseId) +
        "/care-routines/" + encodeURIComponent(routineId) + "/events",
      {
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
        body: JSON.stringify(command),
      },
    );
  } catch {
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
  if (response.status !== 201 ||
      !(response.headers.get("content-type") ?? "").includes("application/json")) {
    throw new ApiError(502, "INVALID_API_RESPONSE");
  }
  try { return (await response.json()) as RecordedCareRoutineEvent; }
  catch { throw new ApiError(502, "INVALID_API_RESPONSE"); }
}

export interface CreateCareRoutineCommand {
  expected_current_assignment_id: string;
  routine_type: "APP_REMINDER" | "CAREGIVER_TASK";
  title: string;
  schedule: {
    timezone: string;
    local_time: string;
    cadence: "DAILY" | "WEEKLY";
    weekdays: number[];
  };
  active: boolean;
  supersedes_routine_id: string | null;
}

export async function createCareRoutine(
  caseId: string,
  command: CreateCareRoutineCommand,
  key: string,
): Promise<import("./types").CareRoutineView> {
  assertUuid(caseId);
  assertUuid(command.expected_current_assignment_id);
  if (command.supersedes_routine_id) assertUuid(command.supersedes_routine_id);
  if (!/^[0-9a-f-]{36}$/i.test(key)) {
    throw new ApiError(422, "INVALID_IDEMPOTENCY_KEY");
  }
  let response: Response;
  try {
    response = await fetch(
      "/api/v1/cases/" + encodeURIComponent(caseId) + "/care-routines",
      {
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
        body: JSON.stringify(command),
      },
    );
  } catch {
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
  if (response.status !== 201 ||
      !(response.headers.get("content-type") ?? "").includes("application/json")) {
    throw new ApiError(502, "INVALID_API_RESPONSE");
  }
  try { return (await response.json()) as import("./types").CareRoutineView; }
  catch { throw new ApiError(502, "INVALID_API_RESPONSE"); }
}
