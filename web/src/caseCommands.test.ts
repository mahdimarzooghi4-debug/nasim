import { afterEach, expect, it, vi } from "vitest";
import { ApiError } from "./api";
import {
  mayManageCases, mayRecordContact, newIntentKey, submitCaseAction, verifyCasePayload,
} from "./caseCommands";
import type { ActorContext } from "./types";

const caseId = "ed1c5701-38df-422c-bff3-12a910e50ec3";
const assignmentId = "66d6dd5e-bd21-48c3-9589-2fc37e5b84f7";
const key = "4c1726cf-65f7-424c-9b9a-e6ce67b37d22";
const actor = (caps: string[], name = "human"): ActorContext => ({
  actor_id: name, actor_type: "HUMAN", capabilities: caps, correlation_id: "tests",
});
const originalFetch = globalThis.fetch;
afterEach(() => { globalThis.fetch = originalFetch; vi.restoreAllMocks(); });

it("does not infer authority from assignment, Case read, Role or AI actor", () => {
  expect(mayManageCases(actor(["case.read.oversight"]))).toBe(false);
  expect(mayManageCases(actor(["case.assignment.manage"]))).toBe(true);
  expect(mayRecordContact(actor(["case.contact.manage.assigned"]), "someone-else")).toBe(false);
  expect(mayRecordContact(actor(["case.read.assigned"]), "human")).toBe(false);
  expect(mayRecordContact(actor(["case.contact.manage.assigned"]), "human")).toBe(true);
  expect(mayManageCases({
    ...actor(["case.assignment.manage"]), actor_type: "AI",
  })).toBe(false);
});

it("requires secure UUID idempotency identity, not predictable generation", () => {
  expect(newIntentKey()).toMatch(/^[0-9a-f-]{36}$/i);
});

it("POSTs exactly the existing three TS-03 commands and only same-origin credentials", async () => {
  const mock = vi.fn().mockImplementation(() => Promise.resolve(
    new Response(JSON.stringify({ id: caseId, case: { id: caseId } }), {
      status: 201, headers: { "content-type": "application/json" },
    }),
  ));
  globalThis.fetch = mock;
  await submitCaseAction("create", null, {
    upstream_enrollment_ref: "supplied-authoritative-external-ref",
    elder_reference: "opaque-elder",
    initial_caregiver_actor_id: "human",
  }, key);
  await submitCaseAction("reassign", caseId, {
    expected_current_assignment_id: assignmentId,
    caregiver_actor_id: "next-human",
    reason: "Human management decision",
  }, key);
  await submitCaseAction("contact", caseId, {
    expected_current_assignment_id: assignmentId,
    contact_kind: "human-entered-kind",
    contact_value: "human-entered-value",
  }, key);
  expect(mock.mock.calls.map(call => call[0])).toEqual([
    "/api/v1/cases",
    "/api/v1/cases/" + caseId + "/reassignments",
    "/api/v1/cases/" + caseId + "/contacts",
  ]);
  for (const [, options] of mock.mock.calls) {
    const request = options as RequestInit;
    expect(request.method).toBe("POST");
    expect(request.mode).toBe("same-origin");
    expect(request.credentials).toBe("same-origin");
    expect(request.redirect).toBe("error");
    expect(request.headers).toEqual({
      Accept: "application/json",
      "Content-Type": "application/json",
      "Idempotency-Key": key,
    });
    expect(request.headers).not.toHaveProperty("Authorization");
    expect(request.headers).not.toHaveProperty("X-Actor-ID");
  }
});

it("forbids missing source IDs or fake defaults before any network request", () => {
  const spy = vi.fn();
  globalThis.fetch = spy;
  expect(() => verifyCasePayload("create", null, {
    upstream_enrollment_ref: "", elder_reference: "elder", initial_caregiver_actor_id: "human",
  }, key)).toThrow(ApiError);
  expect(() => verifyCasePayload("reassign", caseId, {
    expected_current_assignment_id: "fake", caregiver_actor_id: "next", reason: "reason",
  }, key)).toThrow(ApiError);
  expect(() => verifyCasePayload("contact", caseId, {
    expected_current_assignment_id: assignmentId, contact_kind: " ", contact_value: "value",
  }, key)).toThrow(ApiError);
  expect(() => verifyCasePayload("contact", null, {
    expected_current_assignment_id: assignmentId, contact_kind: "note", contact_value: "value",
  }, key)).toThrow(ApiError);
  expect(spy).not.toHaveBeenCalled();
});

it("requires exact 201 JSON and safely handles access/stale-conflict errors", async () => {
  const mock = vi.fn()
    .mockResolvedValueOnce(new Response("private data", { status: 401 }))
    .mockResolvedValueOnce(new Response("private data", { status: 403 }))
    .mockResolvedValueOnce(new Response("private data", { status: 409 }))
    .mockResolvedValueOnce(new Response("<html>not JSON</html>", {
      status: 201, headers: { "content-type": "text/html" },
    }));
  globalThis.fetch = mock;
  const body = {
    expected_current_assignment_id: assignmentId,
    caregiver_actor_id: "new-human",
    reason: "Human reassignment",
  };
  for (const [status, code] of [
    [401, "AUTHENTICATION_REQUIRED"],
    [403, "ACCESS_DENIED"],
    [409, "CONFLICT"],
    [502, "INVALID_API_RESPONSE"],
  ] as const) {
    await expect(submitCaseAction("reassign", caseId, body, key))
      .rejects.toMatchObject({ status, code });
  }
  expect(mock).toHaveBeenCalledTimes(4);
});

it("reads current profile and contact records only on protected server routes", async () => {
  const { api } = await import("./api");
  const mock = vi.fn().mockImplementation(() => Promise.resolve(
    new Response(JSON.stringify([]), {
      status: 200, headers: { "content-type": "application/json" },
    }),
  ));
  globalThis.fetch = mock;
  await api.caseProfile(caseId);
  await api.contacts(caseId);
  expect(mock.mock.calls.map(call => call[0])).toEqual([
    "/api/v1/cases/" + caseId,
    "/api/v1/cases/" + caseId + "/contacts",
  ]);
  expect(mock.mock.calls[0]?.[1]).toMatchObject({
    method: "GET", credentials: "same-origin", cache: "no-store",
  });
});
