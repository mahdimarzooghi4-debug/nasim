import { afterEach, expect, it, vi } from "vitest";
import { readCaseHistory, mayReadCaseHistory } from "./caseHistory";
import type { ActorContext } from "./types";

const caseId = "ed1c5701-38df-422c-bff3-12a910e50ec3";
const originalFetch = globalThis.fetch;
const human = (capabilities: string[]): ActorContext => ({
  actor_id: "caregiver", actor_type: "HUMAN", capabilities, correlation_id: "test",
});
afterEach(() => { globalThis.fetch = originalFetch; vi.restoreAllMocks(); });

it("hides history for missing case.read and AI, never infers Manager grant", () => {
  expect(mayReadCaseHistory(human(["case.assignment.manage"]))).toBe(false);
  expect(mayReadCaseHistory(human(["case.read.assigned"]))).toBe(true);
  expect(mayReadCaseHistory(human(["case.read.oversight"]))).toBe(true);
  expect(mayReadCaseHistory({
    ...human(["case.read.oversight"]), actor_type: "AI",
  })).toBe(false);
});

it("reads four exact scoped routes without custom headers or unbounded query", async () => {
  const spy = vi.fn().mockImplementation(() => Promise.resolve(
    new Response(JSON.stringify({ items: [], next_cursor: null }), {
      status: 200, headers: { "content-type": "application/json" },
    }),
  ));
  globalThis.fetch = spy;
  expect((await readCaseHistory("timeline", caseId, "a+b==")).kind).toBe("timeline");
  expect((await readCaseHistory("interactions", caseId, null)).kind).toBe("interactions");
  expect((await readCaseHistory("observations", caseId, "c+d==")).kind).toBe("observations");
  expect(spy.mock.calls.map(x => x[0])).toEqual([
    "/api/v1/cases/" + caseId + "/timeline?cursor=a%2Bb%3D%3D&limit=20",
    "/api/v1/cases/" + caseId + "/interactions?limit=20",
    "/api/v1/cases/" + caseId + "/observations?cursor=c%2Bd%3D%3D&limit=20",
  ]);
  for (const call of spy.mock.calls) {
    const request = call[1] as RequestInit;
    expect(request).toMatchObject({
      method: "GET", credentials: "same-origin", cache: "no-store", redirect: "error",
    });
    expect(request.headers).toEqual({ Accept: "application/json" });
    expect(request.headers).not.toHaveProperty("X-Actor-ID");
  }
});

it("assignment history uses only existing Case authorization, never Referral endpoint", async () => {
  const spy = vi.fn().mockResolvedValue(new Response(JSON.stringify([
    { id: "assignment-a" }, { id: "assignment-b" },
  ]), { status: 200, headers: { "content-type": "application/json" } }));
  globalThis.fetch = spy;
  const page = await readCaseHistory("assignments", caseId, null);
  expect(page.kind).toBe("assignments");
  expect(page.items).toHaveLength(2);
  expect(page.next_cursor).toBeNull();
  expect(spy.mock.calls[0]?.[0]).toBe("/api/v1/cases/" + caseId + "/assignments");
});

it("does not fall back to cached or sample Case history on 401/403", async () => {
  const fetcher = vi.fn()
    .mockResolvedValueOnce(new Response("private name", { status: 401 }))
    .mockResolvedValueOnce(new Response("private name", { status: 403 }));
  globalThis.fetch = fetcher;
  await expect(readCaseHistory("timeline", caseId, null))
    .rejects.toMatchObject({ status: 401, code: "AUTHENTICATION_REQUIRED" });
  await expect(readCaseHistory("timeline", caseId, null))
    .rejects.toMatchObject({ status: 403, code: "ACCESS_DENIED" });
  expect(fetcher).toHaveBeenCalledTimes(2);
});
