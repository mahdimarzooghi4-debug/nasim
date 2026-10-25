import { useEffect, useState } from "react";
import { api, ApiError, canManageCareRoutines, canReadCareRoutines } from "./api";
import { errorMessage } from "./format";
import CareRoutineEvents from "./CareRoutineEvents";
import type { ActorContext, CareRoutineView } from "./types";

const expired = (error: unknown) => error instanceof ApiError && error.status === 401;
const weekdays = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یکشنبه"];

function scheduleText(routine: CareRoutineView): string {
  const { cadence, weekdays: days, local_time: time, timezone } = routine.schedule;
  const frequency = cadence === "DAILY"
    ? "هر روز"
    : days.map(day => weekdays[day] ?? "روز نامشخص").join("، ");
  return `${frequency} · ساعت ${time.slice(0, 5)} · ${timezone}`;
}

export default function CareRoutines({ caseId, actor, assignmentId, assignedActorId, onLost }: {
  caseId: string;
  actor: ActorContext;
  assignmentId: string;
  assignedActorId: string;
  onLost: () => void;
}) {
  const [routines, setRoutines] = useState<CareRoutineView[] | null>(null);
  const [busy, setBusy] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const allowed = canReadCareRoutines(actor);

  useEffect(() => {
    const controller = new AbortController();
    setRoutines(null);
    setError(null);
    if (!allowed) {
      setBusy(false);
      return () => controller.abort();
    }
    setBusy(true);
    api.careRoutines(caseId, controller.signal).then(result => {
      if (!controller.signal.aborted) setRoutines(result);
    }).catch(reason => {
      if (controller.signal.aborted) return;
      if (expired(reason)) onLost();
      else setError(errorMessage(reason));
    }).finally(() => {
      if (!controller.signal.aborted) setBusy(false);
    });
    return () => controller.abort();
  }, [caseId, allowed, onLost]);

  return <section className="card" aria-label="برنامه‌های روزانه مراقبت">
    <header className="section-title">
      <div><p className="eyebrow">برنامه‌های ثبت‌شده</p><h3>روال روزانه</h3></div>
    </header>
    <p className="disclaimer">
      یادآوری اپ، انجام‌شدن کار را ثابت نمی‌کند. فقط ثبت صریح سالمندیار وضعیت انجام را نشان می‌دهد.
    </p>
    {!allowed && <p className="empty">مجوز مشاهده برنامه‌های مراقبت برای این حساب موجود نیست.</p>}
    {busy && allowed && <p role="status" className="muted">در حال دریافت برنامه‌های مجاز…</p>}
    {error && <div role="alert" className="notice">{error}</div>}
    {routines && routines.length === 0 && (
      <p className="empty">برنامهٔ فعالی برای نمایش ثبت نشده است.</p>
    )}
    {routines && routines.length > 0 && <ul className="records">
      {routines.map(routine => {
        const reminder = routine.routine_type === "APP_REMINDER";
        return <li key={routine.id}>
          <div className="section-title">
            <strong>{routine.title}</strong>
            <span className="chip">{reminder ? "یادآوری اپ" : "کار سالمندیار"}</span>
          </div>
          <p className="meta">{scheduleText(routine)}</p>
          <CareRoutineEvents
            caseId={caseId}
            routine={routine}
            actor={actor}
            assignmentId={assignmentId}
            assignedActorId={assignedActorId}
            onLost={onLost}
          />
          <p className="meta">
            {reminder
              ? "این برنامه برای یادآوری توسط اپ تعریف شده؛ ارسال اعلان از این نما قابل تأیید نیست."
              : "این برنامه به اقدام انسانی نیاز دارد؛ نبودِ ثبت، انجام‌شدن یا انجام‌نشدن را مشخص نمی‌کند."}
          </p>
        </li>;
      })}
    </ul>}
  </section>;
}
