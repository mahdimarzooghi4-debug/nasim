import { afterEach, describe, expect, it, vi } from "vitest";
import { ApiError } from "./api";
import {
  canRecord, makeIdempotencyKey, recordCareAction, toObservedUtc,
} from "./commands";
import type { ActorContext } from "./types";

const caseId = "a12d2334-3a0d-43ea-9e9a-1f6e89de3377";
const assignmentId = "bc9cd439-baf6-46fa-9257-18923b9e1b07";
const needId = "d8815e0a-9dd7-4468-ae0a-0c012a47f739";
const referralId = "f589a69e-23de-47c4-b754-9d3f52a79528";
const key = "908a77b5-49d7-427f-ad5e-1b97f282ca22";
const originalFetch = globalThis.fetch;
afterEach(() => { globalThis.fetch = originalFetch; vi.restoreAllMocks(); });

const human = (capabilities: string[], actor_id = "assigned") : ActorContext => ({
  actor_id, actor_type: "HUMAN", correlation_id: "tests", capabilities,
});

describe("approved operational recording contracts", () => {
  it("does not infer mutation authority from a read grant, role or different actor", () => {
    expect(canRecord(human(["case.read.assigned"]), "observation", "assigned")).toBe(false);
    expect(canRecord(human(["case.observe.assigned"]), "observation", "assigned")).toBe(true);
    expect(canRecord(human(["case.observe.assigned"], "other"), "observation", "assigned")).toBe(false);
    expect(canRecord({ ...human(["referral.create.assigned"]), actor_type: "AI" }, "referral", "assigned")).toBe(false);
    expect(canRecord(human(["referral.follow_up.record.assigned"]), "follow_up", "assigned")).toBe(true);
    expect(canRecord(human(["case.monitor.assigned"]), "interaction", "assigned")).toBe(true);
  });

  it("uses a secure idempotency UUID and a user-visible timestamp", () => {
    expect(makeIdempotencyKey()).toMatch(/^[a-f\d-]{36}$/);
    expect(toObservedUtc("2026-10-09T10:30")).toContain("T");
    expect(() => toObservedUtc("")).toThrowError(ApiError);
  });

  it("writes the exact observation contract with no actor spoofing headers", async () => {
    const spy = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ id: needId }), {
        status: 201, headers: { "content-type": "application/json" },
      }),
    );
    globalThis.fetch = spy;
    const body = {
      expected_current_assignment_id: assignmentId,
      record_type: "NEED_CAPTURE" as const,
      occurred_at: "2026-10-09T10:30:00Z",
      content: "A real human-recorded need",
    };
    const result = await recordCareAction("observation", caseId, null, body, key);
    expect(result).toHaveProperty("id", needId);
    const [path, opts] = spy.mock.calls[0] as [string, RequestInit];
    expect(path).toBe("/api/v1/cases/" + caseId + "/observations");
    expect(opts.method).toBe("POST");
    expect(opts.credentials).toBe("same-origin");
    expect(opts.redirect).toBe("error");
    expect(opts.headers).toEqual({
      Accept: "application/json",
      "Content-Type": "application/json",
      "Idempotency-Key": key,
    });
    expect(opts.headers).not.toHaveProperty("X-Actor-ID");
    expect(opts.headers).not.toHaveProperty("Authorization");
    expect(JSON.parse(opts.body as string)).toEqual(body);
  });

  it("uses distinct reviewed routes for Contact/Monitoring, Referral and Follow-up", async () => {
    const spy = vi.fn().mockImplementation(() => Promise.resolve(
      new Response(JSON.stringify({ id: needId }), {
        status: 201, headers: { "content-type": "application/json" },
      }),
    ));
    globalThis.fetch = spy;
    await recordCareAction("interaction", caseId, null, {
      expected_current_assignment_id: assignmentId,
      interaction_type: "CONTACT",
      occurred_at: "2026-10-09T13:10:00+04:00",
      content: "Human call record",
    }, key);
    await recordCareAction("referral", caseId, null, {
      expected_current_assignment_id: assignmentId,
      source_need_observation_id: needId,
      reason: "Recorded Need only",
    }, key);
    await recordCareAction("follow_up", caseId, referralId, {
      expected_current_assignment_id: assignmentId,
      note: "Attempted contact",
      reason: "No outcome claim",
    }, key);
    expect(spy.mock.calls.map(call => call[0])).toEqual([
      "/api/v1/cases/" + caseId + "/interactions",
      "/api/v1/cases/" + caseId + "/referrals",
      "/api/v1/referrals/" + referralId + "/follow-up-records",
    ]);
  });

  it("fails before fetch on missing/invalid immutable source and empty data", async () => {
    const spy = vi.fn();
    globalThis.fetch = spy;
    await expect(recordCareAction("referral", caseId, null, {
      expected_current_assignment_id: assignmentId,
      source_need_observation_id: "bad",
      reason: "valid",
    }, key)).rejects.toMatchObject({ status: 422 });
    await expect(recordCareAction("follow_up", caseId, null, {
      expected_current_assignment_id: assignmentId,
      note: "human note",
      reason: "reason",
    }, key)).rejects.toMatchObject({ code: "REFERRAL_SELECTION_REQUIRED" });
    await expect(recordCareAction("observation", caseId, null, {
      expected_current_assignment_id: assignmentId,
      record_type: "OBSERVATION",
      occurred_at: "invalid",
      content: "observed",
    }, key)).rejects.toMatchObject({ code: "INVALID_EVENT_TIME" });
    await expect(recordCareAction("observation", caseId, null, {
      expected_current_assignment_id: assignmentId,
      record_type: "OBSERVATION",
      occurred_at: "2026-10-09T10:00:00Z",
      content: "   ",
    }, key)).rejects.toMatchObject({ code: "REQUIRED_RECORD_TEXT" });
    expect(spy).not.toHaveBeenCalled();
  });

  it("does not leak server error text, retry automatically, or treat 409 as success", async () => {
    const spy = vi.fn()
      .mockResolvedValueOnce(new Response("elder personal notes", { status: 409 }))
      .mockResolvedValueOnce(new Response(null, { status: 401 }))
      .mockResolvedValueOnce(new Response("<html>proxy</html>", {
        status: 201, headers: { "content-type": "text/html" },
      }));
    globalThis.fetch = spy;
    const body = {
      expected_current_assignment_id: assignmentId,
      source_need_observation_id: needId, reason: "Real human reason",
    };
    await expect(recordCareAction("referral", caseId, null, body, key))
      .rejects.toMatchObject({ status: 409, code: "CONFLICT" });
    await expect(recordCareAction("referral", caseId, null, body, key))
      .rejects.toMatchObject({ status: 401, code: "AUTHENTICATION_REQUIRED" });
    await expect(recordCareAction("referral", caseId, null, body, key))
      .rejects.toMatchObject({ status: 502, code: "INVALID_API_RESPONSE" });
    expect(spy).toHaveBeenCalledTimes(3);
  });
});
