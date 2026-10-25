import { expect, it } from "vitest";
import { renderToStaticMarkup } from "react-dom/server";
import CaseCreate from "./CaseCreate";
import CaseOperations from "./CaseOperations";
import type { ActorContext, CaseProfileView } from "./types";

const actor = (capabilities: string[], actor_id = "caregiver"): ActorContext => ({
  actor_id, actor_type: "HUMAN", correlation_id: "test", capabilities,
});
const profile: CaseProfileView = {
  case: {
    id: "ed1c5701-38df-422c-bff3-12a910e50ec3",
    upstream_enrollment_ref: "opaque",
    created_at: "2026-10-09T10:00:00Z",
    created_by_actor_id: "supervisor",
    created_by_actor_type: "HUMAN",
  },
  profile: {
    id: "b0dd9afc-2cc0-43fb-a6ee-31f6a8a7686a",
    case_id: "ed1c5701-38df-422c-bff3-12a910e50ec3",
    revision_no: 1, elder_reference: "opaque-elder",
    supersedes_revision_id: null, correction_reason: null,
    recorded_at: "2026-10-09T10:00:00Z",
    recorded_by_actor_id: "supervisor", recorded_by_actor_type: "HUMAN",
  },
  current_assignment: {
    id: "66d6dd5e-bd21-48c3-9589-2fc37e5b84f7",
    case_id: "ed1c5701-38df-422c-bff3-12a910e50ec3",
    caregiver_actor_id: "caregiver",
    started_at: "2026-10-09T10:00:00Z", ended_at: null,
    assigned_by_actor_id: "supervisor", assigned_by_actor_type: "HUMAN",
    reason: "INITIAL_ASSIGNMENT",
  },
};
const base = {
  profile,
  onChanged: () => {},
  onAuthenticationLost: () => {},
};

it("only the existing assignment management capability can create or reassign", () => {
  const denied = renderToStaticMarkup(
    <CaseCreate actor={actor(["case.read.oversight"])}
      onAccepted={() => {}} onAuthenticationLost={() => {}} />,
  );
  expect(denied).not.toContain("ثبت پرونده");
  const allowed = renderToStaticMarkup(
    <CaseCreate actor={actor(["case.assignment.manage"])}
      onAccepted={() => {}} onAuthenticationLost={() => {}} />,
  );
  expect(allowed).toContain("مرجع ثبت‌نام بالادستی");
  expect(allowed).toContain("شناسه سالمندیار اولیه");
  const manager = renderToStaticMarkup(
    <CaseOperations {...base} actor={actor(["case.assignment.manage"], "supervisor")} />,
  );
  expect(manager).toContain("تغییر مسئول پرونده");
  expect(manager).not.toContain("ثبت اطلاعات تماس");
});

it("contact management requires the actual current human assignee and grant", () => {
  const authorized = renderToStaticMarkup(
    <CaseOperations {...base} actor={actor(["case.contact.manage.assigned"])} />,
  );
  expect(authorized).toContain("ثبت اطلاعات تماس");
  expect(authorized).not.toContain("تغییر مسئول پرونده");
  const stale = renderToStaticMarkup(
    <CaseOperations {...base} actor={actor(["case.contact.manage.assigned"], "former-owner")} />,
  );
  expect(stale).not.toContain("ثبت اطلاعات تماس");
  const ai = renderToStaticMarkup(
    <CaseOperations {...base} actor={{
      ...actor(["case.contact.manage.assigned"]), actor_type: "AI",
    }} />,
  );
  expect(ai).not.toContain("ثبت اطلاعات تماس");
});
