import { expect, it } from "vitest";
import { renderToStaticMarkup } from "react-dom/server";
import CaseHistory from "./CaseHistory";
import type { ActorContext } from "./types";

const actor = (capabilities: string[], type: ActorContext["actor_type"] = "HUMAN"):
ActorContext => ({
  actor_id: "caregiver", actor_type: type, capabilities, correlation_id: "unit-test",
});
const base = {
  caseId: "ed1c5701-38df-422c-bff3-12a910e50ec3",
  onAuthenticationLost: () => {},
};

it("renders no Case audit screen without existing Case read permission", () => {
  const html = renderToStaticMarkup(<CaseHistory {...base} actor={actor(["case.assignment.manage"])} />);
  expect(html).not.toContain("تاریخچه و منشأ تغییرات پرونده");
  expect(html).not.toContain("ثبت اقدامات و تغییرات");
});
it("never renders audit screen for AI even if incorrectly granted a Case read", () => {
  const html = renderToStaticMarkup(<CaseHistory
    {...base} actor={actor(["case.read.oversight"], "AI")} />);
  expect(html).not.toContain("تاریخچه و منشأ تغییرات پرونده");
});
it("gives explicitly entitled human a read-only, non-Outcome history view", () => {
  const html = renderToStaticMarkup(<CaseHistory
    {...base} actor={actor(["case.read.assigned"])} />);
  expect(html).toContain("تاریخچه و منشأ تغییرات پرونده");
  expect(html).toContain("تاریخچه تخصیص سالمندیار");
  expect(html).toContain("نسخه‌های مشاهدات و نیازها");
  expect(html).not.toContain('type="submit"');
});
