import { afterEach, expect, it, vi } from "vitest";
import { ApiError } from "./api";
import {
  correctionAllowed, latestContactRevisions, submitCorrection, validateCorrection,
} from "./correctionCommands";
import type { ActorContext } from "./types";

const caseId = "ed1c5701-38df-422c-bff3-12a910e50ec3";
const assignmentId = "66d6dd5e-bd21-48c3-9589-2fc37e5b84f7";
const recordId = "fb561ab4-33e0-437e-a4c1-0c4325dbdd7c";
const key = "4c1726cf-65f7-424c-9b9a-e6ce67b37d22";
const actor = (grants: string[], who = "caregiver"): ActorContext => ({
  actor_id: who, actor_type: "HUMAN", capabilities: grants, correlation_id: "test",
});
const oldFetch = globalThis.fetch;
afterEach(() => { globalThis.fetch = oldFetch; vi.restoreAllMocks(); });
const common = {
  expected_current_assignment_id: assignmentId,
  correction_reason: "Explicit human correction",
};

it("only explicitly authorized humans may submit each correction", () => {
  expect(correctionAllowed(actor(["case.assignment.manage"], "supervisor"), "profile", "caregiver")).toBe(true);
  expect(correctionAllowed(actor(["case.read.oversight"], "supervisor"), "profile", "caregiver")).toBe(false);
  expect(correctionAllowed(actor(["case.contact.manage.assigned"]), "contact", "caregiver")).toBe(true);
  expect(correctionAllowed(actor(["case.monitor.assigned"]), "interaction", "caregiver")).toBe(true);
  expect(correctionAllowed(actor(["case.observe.assigned"]), "observation", "caregiver")).toBe(true);
  expect(correctionAllowed(actor(["case.observe.assigned"], "former"), "observation", "caregiver")).toBe(false);
  expect(correctionAllowed({
    ...actor(["case.assignment.manage"]), actor_type: "AI",
  }, "profile", "caregiver")).toBe(false);
});

it("calls exact approved immutable correction URLs and never forges identity", async () => {
  const spy = vi.fn().mockImplementation(() => Promise.resolve(
    new Response(JSON.stringify({ id: recordId }), {
      status: 201, headers: { "content-type": "application/json" },
    }),
  ));
  globalThis.fetch = spy;
  const profile = { ...common, expected_current_revision_id: recordId, elder_reference: "corrected-elder" };
  const contact = {
    ...common, expected_current_revision_id: recordId,
    contact_kind: "contact-type", contact_value: "contact-value",
  };
  const interaction = {
    ...common, expected_current_record_id: recordId,
    interaction_type: "CONTACT" as const, occurred_at: "2026-10-09T10:00:00Z", content: "corrected",
  };
  const observation = {
    ...common, expected_current_record_id: recordId,
    record_type: "NEED_CAPTURE" as const, occurred_at: "2026-10-09T10:00:00Z", content: "corrected need",
  };
  await submitCorrection("profile", caseId, null, profile, key);
  await submitCorrection("contact", caseId, recordId, contact, key);
  await submitCorrection("interaction", caseId, recordId, interaction, key);
  await submitCorrection("observation", caseId, recordId, observation, key);
  expect(spy.mock.calls.map(x => x[0])).toEqual([
    "/api/v1/cases/" + caseId + "/profile/corrections",
    "/api/v1/cases/" + caseId + "/contacts/" + recordId + "/corrections",
    "/api/v1/cases/" + caseId + "/interactions/" + recordId + "/corrections",
    "/api/v1/cases/" + caseId + "/observations/" + recordId + "/corrections",
  ]);
  for (const [, cfg] of spy.mock.calls) {
    const opts = cfg as RequestInit;
    expect(opts).toMatchObject({
      method: "POST", credentials: "same-origin", mode: "same-origin",
      redirect: "error", cache: "no-store",
    });
    expect(opts.headers).toEqual({
      Accept: "application/json", "Content-Type": "application/json", "Idempotency-Key": key,
    });
    expect(opts.headers).not.toHaveProperty("Authorization");
    expect(opts.headers).not.toHaveProperty("X-Actor-ID");
  }
  expect(JSON.parse(spy.mock.calls[0]?.[1]?.body as string)).toEqual(profile);
});

it("fails before network for missing exact versions, correction reasons and time", () => {
  const spy = vi.fn(); globalThis.fetch = spy;
  expect(() => validateCorrection("profile", caseId, null, {
    ...common, correction_reason: " ", expected_current_revision_id: recordId,
    elder_reference: "valid",
  }, key)).toThrow(ApiError);
  expect(() => validateCorrection("contact", caseId, recordId, {
    ...common, expected_current_revision_id: "fake",
    contact_kind: "type", contact_value: "value",
  }, key)).toThrow(ApiError);
  expect(() => validateCorrection("observation", caseId, recordId, {
    ...common, expected_current_record_id: recordId,
    record_type: "OBSERVATION", occurred_at: "invalid", content: "text",
  }, key)).toThrow(ApiError);
  expect(() => validateCorrection("interaction", caseId, null, {
    ...common, expected_current_record_id: recordId,
    interaction_type: "MONITORING", occurred_at: "2026-10-09T10:00:00Z", content: "text",
  }, key)).toThrow(ApiError);
  expect(spy).not.toHaveBeenCalled();
});

it("does not leak private server error content or treat 409 as a write", async () => {
  globalThis.fetch = vi.fn()
    .mockResolvedValueOnce(new Response("sensitive elder name", { status: 401 }))
    .mockResolvedValueOnce(new Response("sensitive elder name", { status: 403 }))
    .mockResolvedValueOnce(new Response("sensitive elder name", { status: 409 }))
    .mockResolvedValueOnce(new Response("<html>invalid</html>", {
      status: 201, headers: { "content-type": "text/html" },
    }));
  const body = { ...common, expected_current_revision_id: recordId, elder_reference: "corrected" };
  for (const [status, code] of [
    [401, "AUTHENTICATION_REQUIRED"], [403, "ACCESS_DENIED"],
    [409, "CONFLICT"], [502, "INVALID_API_RESPONSE"],
  ] as const) {
    await expect(submitCorrection("profile", caseId, null, body, key))
      .rejects.toMatchObject({ status, code });
  }
});

it("only latest Contact revision per logical identifier is selectable", () => {
  const base = {
    id: recordId, case_id: caseId, logical_contact_id: recordId,
    revision_no: 1, contact_kind: "type", contact_value: "old", recorded_at: "2026-10-09T09:00:00Z",
    recorded_by_actor_id: "actor", recorded_by_actor_type: "HUMAN",
    supersedes_revision_id: null, correction_reason: null,
  };
  const other = {
    ...base, id: "98620ac1-5c76-4bd0-9c46-bd7b2659ba0f",
    logical_contact_id: "61895637-273f-4bd5-97a9-fcd3203b933e",
  };
  const rows = latestContactRevisions([
    { ...base, revision_no: 2, id: "758ad1d1-af5d-4c61-82ab-c359139b7a09", contact_value: "new" },
    other, base,
  ]);
  expect(rows.length).toBe(2);
  expect(rows.find(row => row.logical_contact_id === recordId)?.contact_value).toBe("new");
});

it("reads real bounded interaction and observation APIs", async () => {
  const { api } = await import("./api");
  const mock = vi.fn().mockImplementation(() => Promise.resolve(
    new Response(JSON.stringify({ items: [], next_cursor: null }), {
      status: 200, headers: { "content-type": "application/json" },
    }),
  ));
  globalThis.fetch = mock;
  await api.interactions(caseId, "a+b=");
  await api.observations(caseId, "c+d=");
  expect(mock.mock.calls.map(x => x[0])).toEqual([
    "/api/v1/cases/" + caseId + "/interactions?cursor=a%2Bb%3D&limit=20",
    "/api/v1/cases/" + caseId + "/observations?cursor=c%2Bd%3D&limit=20",
  ]);
});
