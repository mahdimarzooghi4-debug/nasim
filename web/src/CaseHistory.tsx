import { useEffect, useState } from "react";
import { ApiError } from "./api";
import { mayReadCaseHistory, readCaseHistory } from "./caseHistory";
import type { HistoryKind, HistoryPage } from "./caseHistory";
import { errorMessage, formatDate } from "./format";
import type { ActorContext } from "./types";

const labels: Record<HistoryKind, string> = {
  timeline: "ثبت اقدامات و تغییرات",
  assignments: "تاریخچه تخصیص سالمندیار",
  interactions: "نسخه‌های تماس و پایش",
  observations: "نسخه‌های مشاهدات و نیازها",
};

const kinds: HistoryKind[] = ["timeline", "assignments", "interactions", "observations"];
const smallId = (value: string) => value.slice(0, 8);

export default function CaseHistory({
  caseId, actor, onAuthenticationLost,
}: {
  caseId: string;
  actor: ActorContext;
  onAuthenticationLost: () => void;
}) {
  const [kind, setKind] = useState<HistoryKind>("timeline");
  const [cursors, setCursors] = useState<Record<HistoryKind, (string | null)[]>>({
    timeline: [null], assignments: [null], interactions: [null], observations: [null],
  });
  const stack = cursors[kind];
  const cursor = stack[stack.length - 1] ?? null;
  const [page, setPage] = useState<HistoryPage | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [revision, setRevision] = useState(0);
  const allowed = mayReadCaseHistory(actor);

  useEffect(() => {
    if (!allowed) return;
    const controller = new AbortController();
    setPage(null); setError(null); setLoading(true);
    readCaseHistory(kind, caseId, cursor, controller.signal).then(result => {
      if (!controller.signal.aborted) setPage(result);
    }).catch(cause => {
      if (controller.signal.aborted) return;
      if (cause instanceof ApiError && cause.status === 401) onAuthenticationLost();
      else setError(errorMessage(cause));
    }).finally(() => {
      if (!controller.signal.aborted) setLoading(false);
    });
    return () => controller.abort();
  }, [allowed, kind, caseId, cursor, revision, onAuthenticationLost]);

  if (!allowed) return null;

  function nextPage() {
    if (!page?.next_cursor) return;
    const next = page.next_cursor;
    setCursors(prev => ({ ...prev, [kind]: [...prev[kind], next] }));
  }
  function previousPage() {
    setCursors(prev => ({
      ...prev, [kind]: prev[kind].length <= 1 ? [null] : prev[kind].slice(0, -1),
    }));
  }

  return <section className="card" aria-label="سوابق قابل ممیزی پرونده">
    <header className="section-title">
      <div>
        <p className="eyebrow">صرفاً رکوردهای ثبت‌شده در نسیم</p>
        <h3>تاریخچه و منشأ تغییرات پرونده</h3>
      </div>
      <button className="subtle" type="button" onClick={() => setRevision(v => v + 1)}>
        بازخوانی از سرور
      </button>
    </header>
    <p className="disclaimer">
      این نمایش، سابقه فنی ثبت‌ها و اصلاحات را گزارش می‌کند؛ تأیید انجام خدمت،
      نتیجه درمان، وضعیت ارجاع یا صلاحیت Provider نیست. صفحه‌های مختلف یک تصویر
      تاریخی منجمد و یکپارچه ندارند؛ دسترسی و نسخه‌ها در هر درخواست دوباره سنجیده می‌شوند.
    </p>
    <div className="history-tabs" role="group" aria-label="دسته سابقه">
      {kinds.map(value => <button type="button" key={value}
        className={kind === value ? "active" : "subtle"} aria-pressed={kind === value}
        onClick={() => setKind(value)}>{labels[value]}</button>)}
    </div>
    {loading && <p role="status" className="muted">در حال دریافت سوابق مجاز از Backend…</p>}
    {error && <p role="alert" className="notice">{error}</p>}
    {page && page.kind === kind && <>
      {page.items.length === 0 && <p className="empty">در این صفحه رکوردی ثبت نشده است.</p>}
      <ol className="records history-records">
        {page.kind === "timeline" && page.items.map(item => <li key={item.id}>
          <div className="meta">{formatDate(item.timestamp)} · <bdi>{item.actor_id}</bdi> ({item.actor_type})</div>
          <strong dir="ltr">{item.action}</strong>
          <p className="meta">نوع منبع: <bdi>{item.resource_type}</bdi> · شناسه: <bdi>{smallId(item.resource_id)}</bdi></p>
          {item.before_reference && <p className="meta">
            شناسه نسخه پیشین: <bdi>{item.before_reference}</bdi>
          </p>}
          <p className="meta">شناسه رکورد بعدی/ثبت‌شده: <bdi>{item.after_reference}</bdi></p>
          {item.reason && <p className="record-content">دلیل ثبت‌شده: {item.reason}</p>}
          <p className="meta">Correlation: <bdi>{item.correlation_id}</bdi></p>
        </li>)}
        {page.kind === "assignments" && page.items.map(item => <li key={item.id}>
          <div className="meta">تخصیص: <bdi>{smallId(item.id)}</bdi></div>
          <strong>سالمندیار: <bdi>{item.caregiver_actor_id}</bdi></strong>
          <p className="meta">شروع: {formatDate(item.started_at)}</p>
          <p className="meta">{item.ended_at ? "پایان: " + formatDate(item.ended_at) : "پایان ثبت نشده است"}</p>
          <p className="meta">ثبت‌کننده: <bdi>{item.assigned_by_actor_id}</bdi></p>
          <p className="record-content">دلیل: {item.reason}</p>
        </li>)}
        {page.kind === "interactions" && page.items.map(item => <li key={item.id}>
          <div className="meta">ثبت: {formatDate(item.recorded_at)} · وقوع: {formatDate(item.occurred_at)}</div>
          <strong>{item.interaction_type}</strong>
          <p className="record-content">{item.content}</p>
          <p className="meta">شناسه نسخه: <bdi>{item.id}</bdi></p>
          {item.supersedes_interaction_id && <p className="meta">
            اصلاح بر اساس: <bdi>{item.supersedes_interaction_id}</bdi>
          </p>}
          {item.correction_reason && <p className="record-content">دلیل اصلاح: {item.correction_reason}</p>}
          <p className="meta">ثبت‌کننده: <bdi>{item.recorded_by_actor_id}</bdi></p>
        </li>)}
        {page.kind === "observations" && page.items.map(item => <li key={item.id}>
          <div className="meta">ثبت: {formatDate(item.recorded_at)} · وقوع: {formatDate(item.occurred_at)}</div>
          <strong>{item.record_type === "NEED_CAPTURE" ? "نیاز ثبت‌شده" : "مشاهده"}</strong>
          <p className="record-content">{item.content}</p>
          <p className="meta">شناسه نسخه: <bdi>{item.id}</bdi></p>
          {item.supersedes_observation_id && <p className="meta">
            اصلاح بر اساس: <bdi>{item.supersedes_observation_id}</bdi>
          </p>}
          {item.correction_reason && <p className="record-content">دلیل اصلاح: {item.correction_reason}</p>}
          <p className="meta">ثبت‌کننده: <bdi>{item.recorded_by_actor_id}</bdi></p>
        </li>)}
      </ol>
      {kind !== "assignments" && <div className="pager">
        <button type="button" disabled={stack.length <= 1} onClick={previousPage}>صفحه قبل</button>
        <button type="button" disabled={!page.next_cursor} onClick={nextPage}>صفحه بعد</button>
      </div>}
    </>}
  </section>;
}
