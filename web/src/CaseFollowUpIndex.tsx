import { useEffect, useState } from "react";
import { api, ApiError, canReadJourney } from "./api";
import { errorMessage, formatDate, shortId } from "./format";
import type { ActorContext, FollowUpView, Page } from "./types";

/** Descriptive Case-wide record index, not an operational due/overdue inbox. */
export default function CaseFollowUpIndex({
  caseId, actor, onAuthenticationLost,
}: {
  caseId: string;
  actor: ActorContext;
  onAuthenticationLost: () => void;
}) {
  const [cursors, setCursors] = useState<(string | null)[]>([null]);
  const cursor = cursors[cursors.length - 1] ?? null;
  const [page, setPage] = useState<Page<FollowUpView> | null>(null);
  const [refresh, setRefresh] = useState(0);
  const [busy, setBusy] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const allowed = canReadJourney(actor);

  useEffect(() => {
    if (!allowed) {
      setPage(null);
      setBusy(false);
      return;
    }
    const controller = new AbortController();
    setPage(null); setError(null); setBusy(true);
    api.caseFollowUps(caseId, cursor, controller.signal).then(result => {
      if (!controller.signal.aborted) setPage(result);
    }).catch(cause => {
      if (controller.signal.aborted) return;
      if (cause instanceof ApiError && cause.status === 401) onAuthenticationLost();
      else setError(errorMessage(cause));
    }).finally(() => {
      if (!controller.signal.aborted) setBusy(false);
    });
    return () => controller.abort();
  }, [allowed, caseId, cursor, refresh, onAuthenticationLost]);

  if (!allowed) return null;

  return <section className="card" aria-label="نمای پیگیری‌های انسانی پرونده">
    <header className="section-title">
      <div>
        <p className="eyebrow">سوابق واقعی ثبت‌شده، بدون استنتاج وضعیت</p>
        <h3>پیگیری‌های همه ارجاع‌های این پرونده</h3>
      </div>
      <button type="button" className="subtle" onClick={() => {
        setCursors([null]);
        setRefresh(value => value + 1);
      }}>تازه‌سازی از ابتدا</button>
    </header>
    <p className="disclaimer">
      این نما فقط یادداشت‌های انسانیِ ارجاع را نشان می‌دهد و اثبات انجام خدمت،
      رضایت سالمند، نتیجه درمان یا فوریت اقدام نیست. دسترسی در هر درخواست مجدداً بررسی می‌شود.
    </p>
    {busy && <p role="status">در حال دریافت پیگیری‌های مجاز…</p>}
    {error && <p role="alert" className="notice">{error}</p>}
    {page && page.items.length === 0 && <p className="empty">در این صفحه پیگیری‌ای ثبت نشده است.</p>}
    {page && <ul className="records">{page.items.map(item => <li key={item.id}>
      <div className="meta">
        {formatDate(item.recorded_at)} · ارجاع <bdi>{shortId(item.referral_id)}</bdi>
        {" · "}ثبت‌کننده <bdi>{item.recorded_by_actor_id}</bdi>
      </div>
      <p className="record-content">{item.note}</p>
      <p className="meta">دلیل ثبت: {item.reason}</p>
    </li>)}</ul>}
    <div className="pager">
      <button type="button" disabled={busy || cursors.length <= 1} onClick={() =>
        setCursors(current => current.slice(0, -1))
      }>صفحه قبل</button>
      <button type="button" disabled={busy || !page?.next_cursor} onClick={() => {
        if (page?.next_cursor) setCursors(current => [...current, page.next_cursor]);
      }}>صفحه بعد</button>
    </div>
  </section>;
}
