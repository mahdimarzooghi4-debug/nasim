import { afterEach, describe, expect, it, vi } from "vitest";
import { api, ApiError, canReadCases, canReadJourney, canReadProviderWorkspace } from "./api";
import type { ActorContext } from "./types";

const human = (capabilities: string[]): ActorContext => ({
  actor_id: "a-human", actor_type: "HUMAN", correlation_id: "unit-test", capabilities,
});
const originalFetch = globalThis.fetch;
afterEach(() => { globalThis.fetch = originalFetch; vi.restoreAllMocks(); });

describe("same-origin live API contract", () => {
  it("never adds an impersonation header or uses local example data", async () => {
    const spy = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ items: [], next_cursor: null }), {
        status: 200, headers: { "content-type": "application/json" },
      }),
    );
    globalThis.fetch = spy;
    expect(await api.cases()).toEqual({ items: [], next_cursor: null });
    expect(spy).toHaveBeenCalledWith("/api/v1/cases?limit=20", expect.objectContaining({
      method: "GET", credentials: "same-origin", mode: "same-origin",
      cache: "no-store", redirect: "error",
      headers: { Accept: "application/json" },
    }));
    const request = spy.mock.calls[0]?.[1] as RequestInit;
    expect(request.headers).not.toHaveProperty("Authorization");
    expect(request.headers).not.toHaveProperty("X-Actor-ID");
  });
  it("returns 401/403 without fallback or locally cached content", async () => {
    globalThis.fetch = vi.fn().mockResolvedValue(new Response(null, { status: 401 }));
    await expect(api.self()).rejects.toMatchObject({
      status: 401, code: "AUTHENTICATION_REQUIRED",
    });
    globalThis.fetch = vi.fn().mockResolvedValue(new Response(null, { status: 403 }));
    await expect(api.providers()).rejects.toMatchObject({
      status: 403, code: "ACCESS_DENIED",
    });
  });
  it("rejects non-JSON response instead of treating an HTML login page as API data", async () => {
    globalThis.fetch = vi.fn().mockResolvedValue(
      new Response("<html>Login</html>", { status: 200, headers: { "content-type": "text/html" } }),
    );
    await expect(api.cases()).rejects.toBeInstanceOf(ApiError);
  });
  it("keeps IDs and cursors URL encoded and never interpolates a remote origin", async () => {
    const spy = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({}), { status: 200, headers: { "content-type": "application/json" } }),
    );
    globalThis.fetch = spy;
    await api.journey("case/id", { referralId: "ref+id", observationCursor: "a+b==" });
    const path = spy.mock.calls[0]?.[0] as string;
    expect(path).toContain("/cases/case%2Fid/journey-workspace?");
    expect(path).toContain("referral_id=ref%2Bid");
    expect(path).toContain("observation_cursor=a%2Bb%3D%3D");
    expect(path).not.toContain("https:");
  });
  it("does not invent grants from the role name or actor type", () => {
    expect(canReadCases(human([]))).toBe(false);
    expect(canReadCases(human(["case.assignment.manage"]))).toBe(false);
    expect(canReadJourney(human(["case.read.assigned"]))).toBe(false);
    expect(canReadJourney(human([
      "case.read.assigned", "referral.read.assigned", "referral.follow_up.read.assigned",
    ]))).toBe(true);
    expect(canReadProviderWorkspace(human(["provider_candidate.read"]))).toBe(false);
    expect(canReadProviderWorkspace(human([
      "provider_candidate.read",
      "provider_qualification_evidence.read",
      "provider_qualification_review.read",
    ]))).toBe(true);
    expect(canReadCases({ ...human(["case.read.assigned"]), actor_type: "AI" })).toBe(false);
  });
});
