import type {
  ActorContext, CareJourneyWorkspaceView, CaseProfileView, Page,
  ProviderCandidateView, ProviderWorkspaceView,
} from "./types";

export class ApiError extends Error {
  constructor(readonly status: number, readonly code: string) {
    super(code);
    this.name = "ApiError";
  }
}

function assertLocalApiPath(path: string): void {
  // Never call an untrusted remote origin with operational Case data.
  if (!path.startsWith("/api/v1/") || path.includes("//") || path.includes("#")) {
    throw new Error("INVALID_API_PATH");
  }
}

async function getJson<T>(path: string, signal?: AbortSignal): Promise<T> {
  assertLocalApiPath(path);
  let response: Response;
  try {
    response = await fetch(path, {
      method: "GET",
      credentials: "same-origin",
      mode: "same-origin",
      cache: "no-store",
      redirect: "error",
      headers: { Accept: "application/json" },
      signal,
    });
  } catch (error) {
    if (signal?.aborted) throw error;
    throw new ApiError(0, "NETWORK_UNAVAILABLE");
  }
  if (!response.ok) {
    // Never render raw backend error messages or submitted data.
    throw new ApiError(response.status, response.status === 401
      ? "AUTHENTICATION_REQUIRED" : response.status === 403
        ? "ACCESS_DENIED" : response.status === 404
          ? "NOT_FOUND" : "REQUEST_FAILED");
  }
  const contentType = response.headers.get("content-type") ?? "";
  if (!contentType.includes("application/json")) {
    throw new ApiError(502, "INVALID_API_RESPONSE");
  }
  try { return (await response.json()) as T; }
  catch { throw new ApiError(502, "INVALID_API_RESPONSE"); }
}

function params(fields: Record<string, string | number | null | undefined>): string {
  const query = new URLSearchParams();
  for (const [key, value] of Object.entries(fields)) {
    if (value !== null && value !== undefined) query.set(key, String(value));
  }
  const encoded = query.toString();
  return encoded ? "?" + encoded : "";
}

const id = (value: string) => encodeURIComponent(value);

export const api = {
  self: (signal?: AbortSignal) => getJson<ActorContext>("/api/v1/authorization/self", signal),
  cases: (cursor?: string | null, signal?: AbortSignal) =>
    getJson<Page<CaseProfileView>>("/api/v1/cases" + params({ cursor, limit: 20 }), signal),
  journey: (
    caseId: string, opts: {
      referralId?: string | null;
      observationCursor?: string | null;
      referralCursor?: string | null;
      followUpCursor?: string | null;
    } = {}, signal?: AbortSignal
  ) => getJson<CareJourneyWorkspaceView>(
    "/api/v1/cases/" + id(caseId) + "/journey-workspace" + params({
      referral_id: opts.referralId, observation_cursor: opts.observationCursor,
      referral_cursor: opts.referralCursor, follow_up_cursor: opts.followUpCursor, limit: 20,
    }), signal),
  providers: (cursor?: string | null, signal?: AbortSignal) =>
    getJson<Page<ProviderCandidateView>>(
      "/api/v1/provider-candidates" + params({ cursor, limit: 20 }), signal),
  providerWorkspace: (
    candidateId: string, signal?: AbortSignal,
    options: { evidenceCursor?: string | null; requestCursor?: string | null } = {},
  ) => getJson<ProviderWorkspaceView>(
    "/api/v1/provider-candidates/" + id(candidateId) +
      "/qualification-review-workspace" + params({
        evidence_cursor: options.evidenceCursor, request_cursor: options.requestCursor, limit: 20,
      }),
    signal),
};

export const canReadCases = (actor: ActorContext) =>
  actor.actor_type !== "AI" && actor.capabilities.some(c =>
    c === "case.read.assigned" || c === "case.read.oversight");

export const canReadJourney = (actor: ActorContext) =>
  canReadCases(actor) &&
  actor.capabilities.some(c => c === "referral.read.assigned" || c === "referral.read.oversight") &&
  actor.capabilities.some(c =>
    c === "referral.follow_up.read.assigned" || c === "referral.follow_up.read.oversight");

export const canReadProviders = (actor: ActorContext) =>
  actor.actor_type !== "AI" && actor.capabilities.includes("provider_candidate.read");

export const canReadProviderWorkspace = (actor: ActorContext) =>
  canReadProviders(actor) &&
  actor.capabilities.includes("provider_qualification_evidence.read") &&
  actor.capabilities.includes("provider_qualification_review.read");
