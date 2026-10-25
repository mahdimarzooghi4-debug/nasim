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
    case "CONFLICT": return "رکورد یا تخصیص تغییر کرده است؛ اطلاعات را بازبینی کنید.";
    case "INVALID_EVENT_TIME": return "زمان وقوع معتبر نیست.";
    case "INVALID_RECORD_REFERENCE": return "شناسه رکورد معتبر نیست.";
    case "REQUIRED_RECORD_TEXT": return "شرح یا دلیل ثبت نمی‌تواند خالی باشد.";
    case "REFERRAL_SELECTION_REQUIRED": return "ابتدا ارجاع موردنظر را انتخاب کنید.";
    case "SECURE_RANDOM_UNAVAILABLE": return "مرورگر امکان ایجاد شناسه امن درخواست را ندارد.";
    case "NETWORK_UNAVAILABLE": return "ارتباط امن با سرویس برقرار نشد.";
    default: return "دریافت اطلاعات ممکن نشد. دوباره تلاش کنید.";
  }
}
