import type { ApiError } from "./api";

const display = new Intl.DateTimeFormat("fa-IR", {
  year: "numeric", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit",
});

export function formatDate(value: string): string {
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? "تاریخ نامعتبر" : display.format(date);
}
export function shortId(value: string): string { return value.slice(0, 8) }
export function errorMessage(error: unknown): string {
  if (error instanceof Error && error.name === "AbortError") return "";
  const known = error as ApiError;
  switch (known?.code) {
    case "AUTHENTICATION_REQUIRED": return "ورود تأییدشده در دسترس نیست. اتصال هویت واقعی لازم است.";
    case "ACCESS_DENIED": return "برای مشاهده این اطلاعات مجوز لازم را ندارید.";
    case "NOT_FOUND": return "این رکورد پیدا نشد یا دیگر قابل مشاهده نیست.";
    case "NETWORK_UNAVAILABLE": return "ارتباط امن با سرویس برقرار نشد.";
    default: return "دریافت اطلاعات ممکن نشد. دوباره تلاش کنید.";
  }
}
