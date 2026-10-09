/** Only approved Provider Registry intake writes, never qualification decisions. */
import { ApiError } from "./api";
import { makeIdempotencyKey } from "./commands";
import type {
  ActorContext, ProviderCandidateView, ProviderEvidenceView, ProviderReviewRequestView,
} from "./types";

export type ProviderIntakeKind = "candidate" | "evidence" | "review_request";
export type CandidateInput = { display_name: string; reason: string };
export type EvidenceInput = { evidence_label: string; evidence_reference: string; reason: string };
export type ReviewInput = { reason: string };
type InputByKind = {
  candidate: CandidateInput;
  evidence: EvidenceInput;
  review_request: ReviewInput;
};

const requiredCapability: Record<ProviderIntakeKind, string> = {
  candidate: "provider_candidate.register",
  evidence: "provider_qualification_evidence.record",
  review_request: "provider_qualification_review.request",
};

export function canRecordProvider(actor: ActorContext, kind: ProviderIntakeKind): boolean {
  return actor.actor_type === "HUMAN" && actor.capabilities.includes(requiredCapability[kind]);
}

export { makeIdempotencyKey };

function requireUuid(value: string): void {
  if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(value)) {
    throw new ApiError(422, "INVALID_RECORD_REFERENCE");
  }
}

export async function postProviderIntake<K extends ProviderIntakeKind>(
  kind: K,
  candidateId: string | null,
  body: InputByKind[K],
  key: string,
  signal?: AbortSignal,
): Promise<ProviderCandidateView | ProviderEvidenceView | ProviderReviewRequestView> {
  if (kind !== "candidate") {
    if (!candidateId) throw new ApiError(422, "INVALID_RECORD_REFERENCE");
    requireUuid(candidateId);
  }
  if (!/^[0-9a-f-]{36}$/i.test(key)) throw new ApiError(422, "INVALID_IDEMPOTENCY_KEY");
  if (!Object.values(body).every(x => typeof x === "string" && x.trim().length > 0)) {
    throw new ApiError(422, "REQUIRED_RECORD_TEXT");
  }
  const prefix = "/api/v1/provider-candidates";
  const path = kind === "candidate" ? prefix
    : prefix + "/" + encodeURIComponent(candidateId!) +
      (kind === "evidence" ? "/qualification-evidence" : "/qualification-review-requests");
  let response: Response;
  try {
    response = await fetch(path, {
      method: "POST",
      credentials: "same-origin", mode: "same-origin",
      redirect: "error", cache: "no-store", signal,
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "Idempotency-Key": key,
      },
      body: JSON.stringify(body),
    });
  } catch (e) {
    if (signal?.aborted) throw e;
    throw new ApiError(0, "NETWORK_UNAVAILABLE");
  }
  if (!response.ok) {
    throw new ApiError(response.status,
      response.status === 401 ? "AUTHENTICATION_REQUIRED"
        : response.status === 403 ? "ACCESS_DENIED"
          : response.status === 409 ? "CONFLICT"
            : response.status === 422 ? "VALIDATION_ERROR"
              : response.status === 404 ? "NOT_FOUND" : "REQUEST_FAILED");
  }
  if (response.status !== 201 ||
      !(response.headers.get("content-type") ?? "").includes("application/json")) {
    throw new ApiError(502, "INVALID_API_RESPONSE");
  }
  try { return await response.json() as ProviderCandidateView | ProviderEvidenceView | ProviderReviewRequestView; }
  catch { throw new ApiError(502, "INVALID_API_RESPONSE"); }
}
