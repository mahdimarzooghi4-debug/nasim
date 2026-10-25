import { useState } from "react";
import type { FormEvent } from "react";
import { ApiError } from "./api";
import { mayManageCases, newIntentKey, submitCaseAction } from "./caseCommands";
import { errorMessage } from "./format";
import type { ActorContext } from "./types";

/** Creation records a supplied *upstream* reference; it never verifies Enrollment. */
export default function CaseCreate({
  actor, onAccepted, onAuthenticationLost,
}: {
  actor: ActorContext;
  onAccepted: () => void;
  onAuthenticationLost: () => void;
}) {
  const [enrollmentRef, setEnrollmentRef] = useState("");
  const [elderRef, setElderRef] = useState("");
  const [caregiver, setCaregiver] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [accepted, setAccepted] = useState<string | null>(null);
  const [pending, setPending] = useState<{ payload: string; key: string } | null>(null);

  if (!mayManageCases(actor)) return null;
  const changed = () => { setError(null); setAccepted(null); setPending(null); };

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (busy) return;
    setError(null);
    const body = {
      upstream_enrollment_ref: enrollmentRef.trim(),
      elder_reference: elderRef.trim(),
      initial_caregiver_actor_id: caregiver.trim(),
    };
    const signature = JSON.stringify(body);
    let intent = pending?.payload === signature ? pending : null;
    try {
      if (!intent) {
        intent = { payload: signature, key: newIntentKey() };
        setPending(intent);
      }
      setBusy(true);
      const result = await submitCaseAction("create", null, body, intent.key);
      setPending(null);
      setEnrollmentRef(""); setElderRef(""); setCaregiver("");
      setAccepted(result.case.id);
      onAccepted();
    } catch (cause) {
      if (cause instanceof ApiError && cause.status === 401) {
        setPending(null);
        onAuthenticationLost();
        return;
      }
      setError(cause instanceof ApiError && cause.status === 409
        ? "کلید قبلی برای داده متفاوت استفاده شده است. درخواست را بررسی کنید؛ ایجاد دوباره خودکار انجام نمی‌شود."
        : errorMessage(cause));
    } finally {
      setBusy(false);
    }
  }

  return <section className="card" aria-label="ثبت پرونده پس از ثبت‌نام">
    <header className="section-title">
      <h3>ایجاد پرونده با مرجع ثبت‌نام بالادستی</h3>
      <span className="chip">مجوز مدیریت تخصیص</span>
    </header>
    <p className="disclaimer">
      این فرم صحت ثبت‌نام، احراز شرایط سالمند یا مجوز قانونی اطلاعات ورودی را بررسی نمی‌کند.
      شناسه‌ها باید از فرآیند معتبر بالادستی ارائه شوند.
    </p>
    <form className="record-form" onSubmit={e => { void submit(e); }}>
      <label htmlFor="upstream-enrollment">مرجع ثبت‌نام بالادستی</label>
      <input id="upstream-enrollment" value={enrollmentRef} maxLength={200}
        disabled={busy} required onChange={e => { changed(); setEnrollmentRef(e.target.value); }} />
      <label htmlFor="elder-reference">شناسه مرجع سالمند</label>
      <input id="elder-reference" value={elderRef} maxLength={200}
        disabled={busy} required onChange={e => { changed(); setElderRef(e.target.value); }} />
      <label htmlFor="initial-caregiver">شناسه سالمندیار اولیه</label>
      <input id="initial-caregiver" value={caregiver} maxLength={200}
        disabled={busy} required onChange={e => { changed(); setCaregiver(e.target.value); }} />
      {error && <p className="notice" role="alert">{error}</p>}
      {accepted && <p role="status">
        ثبت با پاسخ قطعی سرور پذیرفته شد. شناسه پرونده: <bdi>{accepted}</bdi>
      </p>}
      <button type="submit" disabled={busy || !enrollmentRef.trim() || !elderRef.trim() || !caregiver.trim()}>
        {busy ? "در حال ثبت…" : "ثبت پرونده"}
      </button>
    </form>
  </section>;
}
