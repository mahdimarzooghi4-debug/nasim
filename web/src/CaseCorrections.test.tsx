import { expect, it } from "vitest";
import { renderToStaticMarkup } from "react-dom/server";
import CaseCorrections from "./CaseCorrections";
import type { ActorContext, CaseProfileView } from "./types";

const caseId = "ed1c5701-38df-422c-bff3-12a910e50ec3";
const actor = (caps: string[], actorId = "caregiver"): ActorContext => ({
  actor_id: actorId, actor_type: "HUMAN", capabilities: caps, correlation_id: "test",
});
const profile: CaseProfileView = {
  case: {
    id: caseId, upstream_enrollment_ref: "opaque",
    created_at: "2026-10-09T08:00:00Z",
    created_by_actor_id: "supervisor", created_by_actor_type: "HUMAN",
  },
  profile: {
    id: "6bb26d2c-83ab-4c53-9f3a-0d1e13dc3374", case_id: caseId,
    revision_no: 1, elder_reference: "elder", supersedes_revision_id: null,
    correction_reason: null, recorded_at: "2026-10-09T08:00:00Z",
    recorded_by_actor_id: "supervisor", recorded_by_actor_type: "HUMAN",
  },
  current_assignment: {
    id: "66d6dd5e-bd21-48c3-9589-2fc37e5b84f7",
    case_id: caseId, caregiver_actor_id: "caregiver",
    started_at: "2026-10-09T08:00:00Z", ended_at: null,
    assigned_by_actor_id: "supervisor", assigned_by_actor_type: "HUMAN",
    reason: "Initial assignment",
  },
};
const base = { profile, onChanged: () => {}, onAuthenticationLost: () => {} };

it("does not show correction form for read-only principals, AI or former caregivers", () => {
  for (const selected of [
    actor(["case.read.assigned"]),
    actor(["case.observe.assigned"], "former"),
    { ...actor(["case.assignment.manage"]), actor_type: "AI" as const },
  ]) {
    const html = renderToStaticMarkup(<CaseCorrections {...base} actor={selected} />);
    expect(html).not.toContain("اصلاح نسخه‌دار سوابق انسانی");
    expect(html).not.toContain("ثبت نسخه اصلاحی");
  }
});
it("shows manager profile correction only with existing authority", () => {
  const html = renderToStaticMarkup(<CaseCorrections
    {...base} actor={actor(["case.assignment.manage"], "supervisor")} />);
  expect(html).toContain("اصلاح مرجع پروفایل");
  expect(html).toContain("دلیل اصلاح (اجباری)");
  expect(html).not.toContain("اصلاح مشاهده یا نیاز ثبت‌شده");
});
it("shows human current caregiver's explicitly authorized record types", () => {
  const html = renderToStaticMarkup(<CaseCorrections
    {...base} actor={actor(["case.contact.manage.assigned", "case.observe.assigned"])} />);
  expect(html).toContain("اصلاح مرجع تماس");
  expect(html).toContain("اصلاح مشاهده یا نیاز ثبت‌شده");
  expect(html).not.toContain("اصلاح مرجع پروفایل");
  expect(html).not.toContain("اصلاح تماس یا پایش ثبت‌شده");
});
