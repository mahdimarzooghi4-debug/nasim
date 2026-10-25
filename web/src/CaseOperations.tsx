import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { api, ApiError } from "./api";
import {
  mayManageCases, mayRecordContact, newIntentKey, submitCaseAction,
} from "./caseCommands";
import type { ContactRecord } from "./caseCommands";
import { errorMessage, formatDate } from "./format";
import type { ActorContext, CaseProfileView } from "./types";

/** Actual Case assignment/contact management, no Case lifecycle or outcome decisions. */
export default function CaseOperations({
  actor, profile, onChanged, onAuthenticationLost,
}: {
  actor: ActorContext;
  profile: CaseProfileView;
  onChanged: () => void;
  onAuthenticationLost: () => void;
}) {
  const [caregiver, setCaregiver] = useState("");
  const [reason, setReason] = useState("");
  const [contactKind, setContactKind] = useState("");
  const [contactValue, setContactValue] = useState("");
  const [contacts, setContacts] = useState<ContactRecord[] | null>(null);
  const [contactsError, setContactsError] = useState<string | null>(null);
  const [revision, setRevision] = useState(0);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [accepted, setAccepted] = useState<string | null>(null);
  const [pending, setPending] = useState<{ signature: string; key: string } | null>(null);
  const manage = mayManageCases(actor);
  const contact = mayRecordContact(actor, profile.current_assignment.caregiver_actor_id);

  useEffect(() => {
    const controller = new AbortController();
    setContacts(null); setContactsError(null);
    api.contacts(profile.case.id, controller.signal).then(result => {
      if (!controller.signal.aborted) setContacts(result);
    }).catch(cause => {
      if (controller.signal.aborted) return;
      if (cause instanceof ApiError && cause.status === 401) onAuthenticationLost();
      else setContactsError(errorMessage(cause));
    });
    return () => controller.abort();
  }, [profile.case.id, revision, onAuthenticationLost]);

  if (!manage && !contact) return null;

  function edited() {
    setError(null); setAccepted(null); setPending(null);
  }

  async function send(kind: "reassign" | "contact", event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (busy) return;
    setError(null); setAccepted(null);
    const body = kind === "reassign"
      ? {
        expected_current_assignment_id: profile.current_assignment.id,
        caregiver_actor_id: caregiver.trim(),
        reason: reason.trim(),
      }
      : {
        expected_current_assignment_id: profile.current_assignment.id,
        contact_kind: contactKind.trim(),
        contact_value: contactValue.trim(),
      };
    const signature = JSON.stringify({ kind, caseId: profile.case.id, body });
    let intent = pending?.signature === signature ? pending : null;
    try {
      if (!intent) {
        intent = { signature, key: newIntentKey() };
        setPending(intent);
      }
      setBusy(true);
      const result = kind === "reassign"
        ? await submitCaseAction("reassign", profile.case.id, body as {
          expected_current_assignment_id: string; caregiver_actor_id: string; reason: string;
        }, intent.key)
        : await submitCaseAction("contact", profile.case.id, body as {
          expected_current_assignment_id: string; contact_kind: string; contact_value: string;
        }, intent.key);
      setPending(null);
      setCaregiver(""); setReason(""); setContactKind(""); setContactValue("");
      setAccepted(result.id);
      setRevision(x => x + 1);
      onChanged();
    } catch (cause) {
      if (cause instanceof ApiError && cause.status === 401) {
        setPending(null);
        onAuthenticationLost();
        return;
      }
      setError(cause instanceof ApiError && cause.status === 409
        ? "تخصیص فعلی تغییر کرده یا شناسه درخواست با محتوای دیگری استفاده شده است. ابتدا پرونده را از سرور تازه‌سازی کنید."
        : errorMessage(cause));
      // Stale assignment invalidates the previously displayed Case profile.
      if (cause instanceof ApiError && cause.status === 409) onChanged();
    } finally {
      setBusy(false);
    }
  }

  return <section aria-label="مدیریت پرونده و مخاطبان" className="stack">
    <div className="cards two-col">
      {manage && <section className="card">
        <h3>تغییر مسئول پرونده</h3>
        <p className="disclaimer">
          تغییر سالمندیار تنها با مجوز مدیریت، دلیل انسانی و شناسه دقیق تخصیص فعلی
          ثبت می‌شود؛ تخصیص قبلی قابل بازنویسی نیست.
        </p>
        <form className="record-form" onSubmit={event => { void send("reassign", event); }}>
          <label htmlFor="next-caregiver">شناسه سالمندیار جدید</label>
          <input id="next-caregiver" value={caregiver} maxLength={200} required
            disabled={busy} onChange={e => { edited(); setCaregiver(e.target.value); }} />
          <label htmlFor="assignment-reason">دلیل تغییر مسئول</label>
          <textarea id="assignment-reason" value={reason} required rows={2}
            disabled={busy} onChange={e => { edited(); setReason(e.target.value); }} />
          <button type="submit" disabled={busy || !caregiver.trim() || !reason.trim() ||
            caregiver.trim() === profile.current_assignment.caregiver_actor_id}>
            {busy ? "در حال ثبت…" : "ثبت تغییر مسئول"}
          </button>
        </form>
      </section>}
      {contact && <section className="card">
        <h3>ثبت اطلاعات تماس</h3>
        <p className="disclaimer">
          نوع تماس مطابق قرارداد فنی یک برچسب آزاد است؛ این ثبت به معنی برقراری
          ارتباط یا تأیید مالکیت شماره نیست.
        </p>
        <form className="record-form" onSubmit={event => { void send("contact", event); }}>
          <label htmlFor="contact-kind">نوع مرجع تماس</label>
          <input id="contact-kind" value={contactKind} maxLength={100} required
            disabled={busy} onChange={e => { edited(); setContactKind(e.target.value); }} />
          <label htmlFor="contact-value">مقدار تماس (اطلاعات حساس)</label>
          <input id="contact-value" value={contactValue} required
            disabled={busy} onChange={e => { edited(); setContactValue(e.target.value); }} />
          <button type="submit" disabled={busy || !contactKind.trim() || !contactValue.trim()}>
            {busy ? "در حال ثبت…" : "ثبت مرجع تماس"}
          </button>
        </form>
      </section>}
    </div>
    {error && <p role="alert" className="notice">{error}</p>}
    {accepted && <p role="status">
      سرور ثبت را پذیرفت. شناسه رکورد: <bdi>{accepted}</bdi>
    </p>}
    <section className="card">
      <h3>مرجع‌های تماس ثبت‌شده</h3>
      <p className="disclaimer">این سوابق فقط برای مشاهده‌کننده دارای مجوز از Backend خوانده می‌شوند.</p>
      {contactsError && <p role="alert" className="notice">{contactsError}</p>}
      {contacts && contacts.length === 0 && <p className="empty">مرجع تماسی ثبت نشده است.</p>}
      {contacts && <ul className="records">
        {contacts.map(item => <li key={item.id}>
          <strong>{item.contact_kind}</strong>
          <p className="record-content"><bdi>{item.contact_value}</bdi></p>
          <p className="meta">
            نسخه {item.revision_no} · {formatDate(item.recorded_at)} · <bdi>{item.recorded_by_actor_id}</bdi>
          </p>
        </li>)}
      </ul>}
    </section>
  </section>;
}
