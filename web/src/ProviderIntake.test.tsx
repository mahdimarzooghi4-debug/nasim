import { expect, it } from "vitest";
import { renderToStaticMarkup } from "react-dom/server";
import ProviderIntake from "./ProviderIntake";
import type { ActorContext } from "./types";

const actor: ActorContext = {
  actor_id: "reviewer",
  actor_type: "HUMAN",
  capabilities: ["provider_candidate.register", "provider_qualification_evidence.record", "provider_qualification_review.request"],
  correlation_id: "test",
};
const props = {
  actor,
  candidateId: null,
  onSaved: () => {},
  onAuthenticationLost: () => {},
};
it("no permission or AI never sees Provider intake action", () => {
  expect(renderToStaticMarkup(
    <ProviderIntake {...props} actor={{ ...actor, capabilities: [] }} />,
  )).not.toContain("ثبت مقدماتی Provider");
  expect(renderToStaticMarkup(
    <ProviderIntake {...props} actor={{ ...actor, actor_type: "AI" }} />,
  )).not.toContain("ثبت مقدماتی Provider");
});
it("candidate registration is descriptive and not a qualification decision", () => {
  const output = renderToStaticMarkup(<ProviderIntake {...props} />);
  expect(output).toContain("نام معرفی‌شده Candidate");
  expect(output).toContain("ثبت اولیه Candidate");
  expect(output).not.toContain("تأیید صلاحیت");
});
it("an existing Candidate uses its scoped evidence/request inputs, never global mutations", () => {
  const output = renderToStaticMarkup(
    <ProviderIntake {...props} candidateId="c67a619c-b562-40c9-b494-09d8064aee71" />,
  );
  expect(output).toContain("شواهد ارائه‌شده");
  expect(output).toContain("مرجع ثبت‌شده مدرک");
  expect(output).not.toContain("ثبت اولیه Candidate");
});
