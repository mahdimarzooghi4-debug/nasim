import { expect, it } from "vitest";
import { renderToStaticMarkup } from "react-dom/server";
import CaseFollowUpIndex from "./CaseFollowUpIndex";
import type { ActorContext } from "./types";

const actor = (capabilities: string[], actor_type: ActorContext["actor_type"] = "HUMAN"): ActorContext => ({
  actor_id: "synthetic-actor", actor_type, correlation_id: "test", capabilities,
});
const reads = ["case.read.assigned", "referral.read.assigned", "referral.follow_up.read.assigned"];
const render = (who: ActorContext) => renderToStaticMarkup(
  <CaseFollowUpIndex caseId="synthetic-id" actor={who} onAuthenticationLost={() => {}} />,
);

it("does not show a sensitive Case-wide pane without every independent read capability", () => {
  for (const capability of reads) {
    expect(render(actor(reads.filter(value => value !== capability)))).toBe("");
  }
  expect(render(actor(reads, "AI"))).toBe("");
});

it("describes a read-only human record list, never a verified outcome or priority", () => {
  const html = render(actor(reads));
  expect(html).toContain("پیگیری‌های همه ارجاع‌های این پرونده");
  expect(html).toContain("در حال دریافت پیگیری‌های مجاز");
  expect(html).not.toContain("میزان موفقیت");
  expect(html).not.toContain("ثبت نتیجه");
  expect(html).not.toContain("اولویت فوری");
});
