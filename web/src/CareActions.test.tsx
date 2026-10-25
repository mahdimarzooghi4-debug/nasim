import { expect, it } from "vitest";
import { renderToStaticMarkup } from "react-dom/server";
import CareActions from "./CareActions";
import type { ActorContext } from "./types";

const human: ActorContext = {
  actor_id: "assigned",
  actor_type: "HUMAN",
  capabilities: [
    "case.observe.assigned",
    "referral.create.assigned",
    "referral.follow_up.record.assigned",
  ],
  correlation_id: "test",
};
const props = {
  actor: human,
  caseId: "a12d2334-3a0d-43ea-9e9a-1f6e89de3377",
  assignmentId: "bc9cd439-baf6-46fa-9257-18923b9e1b07",
  assignedActorId: "assigned",
  observations: [],
  selectedReferralId: null,
  onRecorded: () => {},
  onAuthenticationLost: () => {},
};

it("does not show write forms when actor has only read permissions", () => {
  const markup = renderToStaticMarkup(
    <CareActions {...props} actor={{ ...human, capabilities: ["case.read.assigned"] }} />,
  );
  expect(markup).not.toContain("ثبت اقدام انسانی در پرونده");
  expect(markup).not.toContain('type="submit"');
});

it("shows only explicitly enabled human recording commands", () => {
  const markup = renderToStaticMarkup(<CareActions {...props} />);
  expect(markup).toContain("ثبت مشاهده یا نیاز");
  expect(markup).toContain("ثبت ارجاع بر اساس نیاز");
  expect(markup).not.toContain("ثبت پیگیری انسانی ارجاع");
  expect(markup).toContain("زمان وقوع واقعی");
  expect(markup).not.toContain("تأیید صلاحیت ارائه‌دهنده");
});

it("cannot write as a different assignee or as AI despite grants", () => {
  const other = renderToStaticMarkup(<CareActions {...props} assignedActorId="someone-else" />);
  const ai = renderToStaticMarkup(
    <CareActions {...props} actor={{ ...human, actor_type: "AI" }} />,
  );
  expect(other).not.toContain("ثبت اقدام انسانی");
  expect(ai).not.toContain("ثبت اقدام انسانی");
});
