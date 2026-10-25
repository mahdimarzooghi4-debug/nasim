import { afterEach, expect, it, vi } from "vitest";
import { ApiError } from "./api";
import { canRecordProvider, postProviderIntake } from "./providerCommands";
import type { ActorContext } from "./types";

const candidateId = "c67a619c-b562-40c9-b494-09d8064aee71";
const key = "648f3e52-c231-4ff6-bde2-5d15357f0c39";
const human = (capabilities: string[]): ActorContext => ({
  actor_id: "authenticated-human",
  actor_type: "HUMAN",
  capabilities,
  correlation_id: "test",
});
const oldFetch = globalThis.fetch;
afterEach(() => { globalThis.fetch = oldFetch; vi.restoreAllMocks(); });

it("requires explicit Provider intake capability and does not allow AI", () => {
  expect(canRecordProvider(human(["provider_candidate.read"]), "candidate")).toBe(false);
  expect(canRecordProvider(human(["provider_candidate.register"]), "candidate")).toBe(true);
  expect(canRecordProvider(human(["provider_qualification_review.request"]), "review_request")).toBe(true);
  expect(canRecordProvider(human(["provider_qualification_evidence.record"]), "evidence")).toBe(true);
  expect(canRecordProvider({ ...human(["provider_candidate.register"]), actor_type: "AI" }, "candidate")).toBe(false);
});

it("uses only preexisting registration/evidence/request APIs without actor headers", async () => {
  const spy = vi.fn().mockImplementation(() => Promise.resolve(
    new Response(JSON.stringify({ id: candidateId }), {
      status: 201, headers: { "content-type": "application/json" },
    }),
  ));
  globalThis.fetch = spy;
  await postProviderIntake("candidate", null, {
    display_name: "Applicant Name", reason: "Applicant submitted",
  }, key);
  await postProviderIntake("evidence", candidateId, {
    evidence_label: "Submitted document",
    evidence_reference: "opaque-reference",
    reason: "Descriptive only",
  }, key);
  await postProviderIntake("review_request", candidateId, {
    reason: "Human requests review, not approval",
  }, key);
  expect(spy.mock.calls.map(x => x[0])).toEqual([
    "/api/v1/provider-candidates",
    "/api/v1/provider-candidates/" + candidateId + "/qualification-evidence",
    "/api/v1/provider-candidates/" + candidateId + "/qualification-review-requests",
  ]);
  for (const call of spy.mock.calls) {
    const opt = call[1] as RequestInit;
    expect(opt.method).toBe("POST");
    expect(opt.mode).toBe("same-origin");
    expect(opt.credentials).toBe("same-origin");
    expect(opt.cache).toBe("no-store");
    expect(opt.headers).toEqual({
      Accept: "application/json",
      "Content-Type": "application/json",
      "Idempotency-Key": key,
    });
    expect(opt.headers).not.toHaveProperty("X-Actor-ID");
  }
});

it("rejects absent candidate ID and empty technical evidence without a network request", async () => {
  const spy = vi.fn();
  globalThis.fetch = spy;
  await expect(postProviderIntake("evidence", null, {
    evidence_label: "label", evidence_reference: "ref", reason: "human",
  }, key)).rejects.toMatchObject({ status: 422 });
  await expect(postProviderIntake("candidate", null, {
    display_name: " ", reason: "human",
  }, key)).rejects.toMatchObject({ code: "REQUIRED_RECORD_TEXT" });
  await expect(postProviderIntake("review_request", candidateId, {
    reason: " ",
  }, key)).rejects.toMatchObject({ code: "REQUIRED_RECORD_TEXT" });
  expect(spy).not.toHaveBeenCalled();
});

it("does not treat 401/403/409/HTML as an accepted provider decision or echo raw errors", async () => {
  const spy = vi.fn()
    .mockResolvedValueOnce(new Response("raw sensitive text", { status: 401 }))
    .mockResolvedValueOnce(new Response("raw sensitive text", { status: 403 }))
    .mockResolvedValueOnce(new Response("raw sensitive text", { status: 409 }))
    .mockResolvedValueOnce(new Response("<html>login</html>", {
      status: 201, headers: { "content-type": "text/html" },
    }));
  globalThis.fetch = spy;
  for (const [status, code] of [
    [401, "AUTHENTICATION_REQUIRED"],
    [403, "ACCESS_DENIED"],
    [409, "CONFLICT"],
    [502, "INVALID_API_RESPONSE"],
  ] as const) {
    await expect(postProviderIntake("candidate", null, {
      display_name: "Candidate",
      reason: "Human reason",
    }, key)).rejects.toMatchObject({ status, code });
  }
  expect(spy).toHaveBeenCalledTimes(4);
});
