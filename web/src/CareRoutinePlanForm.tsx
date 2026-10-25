import { useState } from "react";
import type { FormEvent } from "react";
import { ApiError } from "./api";
import { errorMessage } from "./format";
import {
  createCareRoutine, makeCareRoutineIdempotencyKey,
} from "./careRoutineCommands";
import type { CreateCareRoutineCommand } from "./careRoutineCommands";
import type { CareRoutineView } from "./types";

const WEEKDAYS = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه", "شنبه", "یکشنبه"];

export default function CareRoutinePlanForm({
  caseId, assignmentId, routine, onCancel, onSaved, onLost,
}: {
  caseId: string;
  assignmentId: string;
  routine: CareRoutineView | null;
  onCancel: () => void;
  onSaved: (active: boolean) => void;
  onLost: () => void;
}) {
  const [title, setTitle] = useState(routine?.title ?? "");
  const [routineType, setRoutineType] = useState<"" | "APP_REMINDER" | "CAREGIVER_TASK">(
    routine?.routine_type ?? "",
  );
  const [cadence, setCadence] = useState<"" | "DAILY" | "WEEKLY">(
    routine?.schedule.cadence ?? "",
  );
  const [weekdays, setWeekdays] = useState<number[]>(routine?.schedule.weekdays ?? []);
  const [localTime, setLocalTime] = useState(routine?.schedule.local_time.slice(0, 5) ?? "");
  const [timezone, setTimezone] = useState(routine?.schedule.timezone ?? "");
  const [active, setActive] = useState(routine?.active ?? true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [pending, setPending] = useState<{ signature: string; key: string } | null>(null);

  function edited() {
    setPending(null);
    setError(null);
  }

  function timezoneHint() {
    try {
      const guessed = Intl.DateTimeFormat().resolvedOptions().timeZone;
      if (guessed) { setTimezone(guessed); edited(); }
    } catch {
      setError("منطقهٔ زمانی دستگاه قابل تشخیص نیست؛ نام IANA را وارد کنید.");
    }
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (saving) return;
    if (!routineType || !cadence || !title.trim() || !localTime || !timezone.trim()) {
      setError("عنوان، نوع برنامه، تکرار، ساعت محلی و منطقهٔ زمانی را کامل کنید.");
      return;
    }
    if (cadence === "WEEKLY" && weekdays.length === 0) {
      setError("برای برنامهٔ هفتگی دست‌کم یک روز انتخاب کنید.");
      return;
    }
    if (!/^([01]\d|2[0-3]):[0-5]\d$/.test(localTime)) {
      setError("ساعت محلی معتبر نیست.");
      return;
    }
    try { new Intl.DateTimeFormat("en", { timeZone: timezone.trim() }); }
    catch {
      setError("منطقهٔ زمانی باید نام معتبر IANA باشد، مانند Asia/Tehran.");
      return;
    }
    if (cadence === "DAILY" && weekdays.length > 0) {
      setError("برای برنامهٔ روزانه روزهای هفته را پاک کنید.");
      return;
    }
    const command: CreateCareRoutineCommand = {
      expected_current_assignment_id: assignmentId,
      routine_type: routineType,
      title: title.trim(),
      schedule: {
        timezone: timezone.trim(),
        local_time: localTime,
        cadence,
        weekdays: cadence === "WEEKLY" ? [...weekdays].sort((a, b) => a - b) : [],
      },
      active,
      supersedes_routine_id: routine?.id ?? null,
    };
    const signature = JSON.stringify(command);
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
      await createCareRoutine(caseId, command, request.key);
      setPending(null);
      onSaved(active);
    } catch (cause) {
      if (cause instanceof ApiError && cause.status === 401) {
        setPending(null);
        onLost();
      } else {
        if (cause instanceof ApiError && cause.status > 0 && cause.status < 500) {
          setPending(null);
        }
        setError(cause instanceof ApiError && cause.status === 409
          ? "تخصیص یا نسخهٔ برنامه تغییر کرده؛ فهرست را تازه کنید و دوباره بررسی کنید."
          : cause instanceof ApiError && cause.status === 422
            ? "اطلاعات با قرارداد برنامهٔ مراقبت سازگار نیست."
            : errorMessage(cause));
      }
    } finally {
      setSaving(false);
    }
  }

  return <section className="card" aria-label={routine ? "نسخهٔ جدید برنامهٔ مراقبت" : "برنامهٔ جدید مراقبت"}>
    <h4>{routine ? "ثبت نسخهٔ جدید برنامه" : "افزودن برنامهٔ مراقبت"}</h4>
    {routine && <p className="disclaimer">نسخهٔ قبلی حفظ می‌شود؛ این فرم یک نسخهٔ جانشین ثبت می‌کند.</p>}
    <form className="record-form" onSubmit={event => { void submit(event); }}>
      <label htmlFor="routine-title">عنوان برنامه</label>
      <input id="routine-title" required maxLength={240} value={title} disabled={saving}
        onChange={event => { edited(); setTitle(event.target.value); }} />

      <label htmlFor="routine-kind">نوع برنامه</label>
      <select id="routine-kind" required value={routineType} disabled={saving || Boolean(routine)}
        onChange={event => { edited(); setRoutineType(event.target.value as typeof routineType); }}>
        <option value="">انتخاب کنید</option>
        <option value="APP_REMINDER">یادآوری اپ</option>
        <option value="CAREGIVER_TASK">کار سالمندیار</option>
      </select>

      <label htmlFor="routine-cadence">تکرار</label>
      <select id="routine-cadence" required value={cadence} disabled={saving}
        onChange={event => {
          edited();
          const next = event.target.value as typeof cadence;
          setCadence(next);
          if (next !== "WEEKLY") setWeekdays([]);
        }}>
        <option value="">انتخاب کنید</option>
        <option value="DAILY">هر روز</option>
        <option value="WEEKLY">روزهای مشخص هفته</option>
      </select>

      {cadence === "WEEKLY" && <fieldset>
        <legend>روزهای هفته</legend>
        <div className="routine-weekdays">
          {WEEKDAYS.map((day, index) => <label key={index}>
            <input type="checkbox" checked={weekdays.includes(index)} disabled={saving}
              onChange={event => {
                edited();
                setWeekdays(current => event.target.checked
                  ? [...current, index].sort((a, b) => a - b)
                  : current.filter(value => value !== index));
              }} />
            {day}
          </label>)}
        </div>
      </fieldset>}

      <label htmlFor="routine-local-time">ساعت محلی</label>
      <input id="routine-local-time" type="time" required value={localTime} disabled={saving}
        onChange={event => { edited(); setLocalTime(event.target.value); }} />

      <label htmlFor="routine-timezone">منطقهٔ زمانی محل زندگی سالمند (IANA)</label>
      <div className="section-title">
        <input id="routine-timezone" type="text" required maxLength={100} value={timezone}
          placeholder="مثال: Asia/Tehran" disabled={saving}
          onChange={event => { edited(); setTimezone(event.target.value); }} />
        <button type="button" className="subtle" disabled={saving} onClick={timezoneHint}>
          پیشنهاد از دستگاه
        </button>
      </div>

      <label className="check-row">
        <input type="checkbox" checked={active} disabled={saving}
          onChange={event => { edited(); setActive(event.target.checked); }} />
        این نسخه فعال باشد
      </label>
      {error && <div role="alert" className="notice">{error}</div>}
      <div className="section-title">
        <button type="submit" disabled={saving}>{saving ? "در حال ثبت…" : routine ? "ثبت نسخهٔ جدید" : "ثبت برنامه"}</button>
        <button type="button" className="subtle" disabled={saving} onClick={onCancel}>انصراف</button>
      </div>
    </form>
  </section>;
}
