import { expect, it } from "vitest";
import { renderToStaticMarkup } from "react-dom/server";
import App from "./App";

it("does not display operational Case or Provider data before server authentication", () => {
  const html = renderToStaticMarkup(<App />);
  expect(html).toContain("در حال بررسی دسترسی");
  expect(html).not.toContain("پرونده‌های قابل مشاهده");
  expect(html).not.toContain("Provider Candidateها");
  expect(html).not.toContain("ورود آزمایشی");
});
