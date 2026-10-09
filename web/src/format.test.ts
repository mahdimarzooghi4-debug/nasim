import { expect, it } from "vitest";
import { errorMessage, shortId } from "./format";
import { ApiError } from "./api";

it("renders only generic safe errors", () => {
  expect(errorMessage(new ApiError(403, "ACCESS_DENIED"))).toContain("مجوز");
  expect(errorMessage(new ApiError(401, "AUTHENTICATION_REQUIRED"))).toContain("هویت");
  expect(errorMessage(new Error("sensitive elder info"))).not.toContain("sensitive");
});
it("shortens opaque IDs for display only", () => {
  expect(shortId("f20e664a-aaaa-bbbb")).toBe("f20e664a");
});
