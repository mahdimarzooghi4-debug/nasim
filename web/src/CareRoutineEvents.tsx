import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import type { ActorContext, CareRoutineEventView, CareRoutineView } from "./types";
import { api, ApiError } from "./api";
import { errorMessage, formatDate } from "./format";
import {
  makeCareRoutineIdempotencyKey, recordCareRoutineEvent,
} from "./careRoutineCommands";
import type {
  CareRoutineEventStatus, RecordCareRoutineEventCommand,
} from "./careRoutineCommands";

const STATUS_LABELS: Record<CareRoutineEventStatus, string> = {
  DONE: "انجام شد",
  NOT_DONE: "انجام نشد",
  SKIPPED: "صرف‌نظر شد",
};

function localDateTimeNow(): string {
  const now = new Date();
  return new Date(now.getTime() - now.getTimezoneOffset() * 60_000)
    .toISOString().slice(0, 16);
}

function dateInTimezone(instant: Date, timezone: string): string {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: timezone, year: "numeric", month: "2-digit", day: "2-digit",
  }).formatToParts(instant);
  const value = (type: string) => parts.find(part => part.type === type)?.value ?? "";
  return value("year") + "-" + value("month") + "-" + value("day");
}

const eventError = (cause: unknown) => {
  if (!(cause instanceof ApiError)) return errorMessage(cause);
  if (cause.status === 409) return "برای این تاریخ قبلاً ثبت انجام شده یا برنامه تغییر کرده است؛ ابتدا فهرست را تازه کنید.";
  if (cause.status === 422) return "زمان وقوع با روز یا برنامهٔ هفتگی سازگار نیست.";
  return errorMessage(cause);
};

export default function CareRoutineEvents({
  caseId, routine, actor, assignmentId, assignedActorId, onLost,
}: {
  caseId: string;
  routine: CareRoutineView;
  actor: ActorContext;
  assignmentId: string;
  assignedActorId: string;
  onLost: () => void;
}) {
  const canRead = actor.actor_type === "HUMAN" &&
    actor.actor_id === assignedActorId &&
    actor.capabilities.includes("care_routine.event.read.assigned");
  const canRecord = actor.actor_type === "HUMAN" &&
    actor.actor_id === assignedActorId &&
    actor.capabilities.includes("care_routine.event.record.assigned");
  const [events, setEvents] = useState<CareRoutineEventView[] | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [occurredAt, setOccurredAt] = useState(localDateTimeNow);
  const [status, setStatus] = useState<CareRoutineEventStatus>("DONE");
  const [saving, setSaving] = useState(false);
  const [revision, setRevision] = useState(0);
  const [pending, setPending] = useState<{ signature: string; key: string } | null>(null);

  useEffect(() => {
    const controller = new AbortController();
    if (!canRead) {
      setEvents(null);
      setBusy(false);
      return () => controller.abort();
    }
    setBusy(true);
    setError(null);
    api.careRoutineEvents(caseId, routine.id, controller.signal).then(result => {
      if (!controller.signal.aborted) setEvents(result);
    }).catch(cause => {
      if (controller.signal.aborted) return;
      if (cause instanceof ApiError && cause.status === 401) onLost();
      else setError(errorMessage(cause));
    }).finally(() => {
      if (!controller.signal.aborted) setBusy(false);
    });
    return () => controller.abort();
  }, [caseId, routine.id, canRead, revision, onLost]);

  function edited() {
    setError(null);
    setPending(null);
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!canRecord || saving) return;
    const instant = new Date(occurredAt);
    if (!occurredAt.trim() || !Number.isFinite(instant.getTime())) {
      setError("زمان وقوع را به‌درستی وارد کنید.");
      return;
    }
    const command: RecordCareRoutineEventCommand = {
      expected_current_assignment_id: assignmentId,
      occurrence_date: dateInTimezone(instant, routine.schedule.timezone),
      status,
      occurred_at: instant.toISOString(),
    };
    const signature = JSON.stringify({ caseId, routineId: routine.id, command });
    let request: { signature: string; key: string };
    try {
      request = pending?.signature === signature
        ? pending : { signature, key: makeCareRoutineIdempotencyKey() };
    } catch (cause) {
      setError(errorMessage(cause));
      return;
    }
    setPending(request);
    setSaving(true);
    setError(null);
    try {
      await recordCareRoutineEvent(caseId, routine.id, command, request.key);
      setPending(null);
      setOccurredAt(localDateTimeNow());
      setRevision(value => value + 1);
    } catch (cause) {
      if (cause instanceof ApiError && cause.status === 401) {
        setPending(null);
        onLost();
      } else {
        if (cause instanceof ApiError && cause.status > 0 && cause.status < 500) setPending(null);
        setError(eventError(cause));
      }
    } finally {
      setSaving(false);
    }
  }

  return <section className="card routine-events" aria-label={"ثبت‌های " + routine.title}>
    <h4>ثبت‌های سالمندیار</h4>
    {!canRead && <p className="muted">مجوز مشاهدهٔ ثبت‌های این برنامه برای این حساب موجود نیست.</p>}
    {canRead && busy && <p role="status" className="muted">در حال دریافت ثبت‌ها…</p>}
    {canRead && events?.length === 0 && (
      <p className="empty">هنوز ثبت صریحی برای این برنامه وجود ندارد؛ وضعیت انجام نامشخص است.</p>
    )}
    {canRead && events && events.length > 0 && <ul className="records">
      {events.map(item => <li key={item.id}>
        <strong>{STATUS_LABELS[item.status]}</strong>
        <p className="meta">زمان وقوع: {formatDate(item.occurred_at)} · روز برنامه: {item.occurrence_date}</p>
        <p className="meta">ثبت در {formatDate(item.recorded_at)} توسط <bdi>{item.recorded_by_actor_id}</bdi></p>
      </li>)}
    </ul>}
    {error && <div role="alert" className="notice">{error}</div>}
    {canRecord && <form className="record-form" onSubmit={event => { void submit(event); }}>
      <label htmlFor={"routine-event-time-" + routine.id}>زمان وقوع واقعی (به وقت دستگاه)</label>
      <input
        id={"routine-event-time-" + routine.id}
        type="datetime-local"
        required
        value={occurredAt}
        disabled={saving}
        onChange={event => { edited(); setOccurredAt(event.target.value); }}
      />
      <label htmlFor={"routine-event-status-" + routine.id}>وضعیت ثبت‌شده توسط سالمندیار</label>
      <select
        id={"routine-event-status-" + routine.id}
        value={status}
        disabled={saving}
        onChange={event => { edited(); setStatus(event.target.value as CareRoutineEventStatus); }}
      >
        <option value="DONE">انجام شد</option>
        <option value="NOT_DONE">انجام نشد</option>
        <option value="SKIPPED">صرف‌نظر شد</option>
      </select>
      <p className="disclaimer">این گزارش انسانی است و به‌تنهایی تأیید مستقلِ انجام کار یا نتیجهٔ مراقبتی نیست.</p>
      <button type="submit" disabled={saving}>{saving ? "در حال ثبت…" : "ثبت وضعیت"}</button>
    </form>}
  </section>;
}
