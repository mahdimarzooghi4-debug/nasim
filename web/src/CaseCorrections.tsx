import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { api, ApiError } from "./api";
import { newIntentKey } from "./caseCommands";
import { toObservedUtc } from "./commands";
import {
  correctionAllowed, latestContactRevisions, submitCorrection,
} from "./correctionCommands";
import type { CorrectionKind, InteractionRecorded } from "./correctionCommands";
import { errorMessage, formatDate, shortId } from "./format";
import type { ActorContext, CaseProfileView, ObservationView, Page } from "./types";
import type { ContactRecord } from "./caseCommands";

const labels: Record<CorrectionKind, string> = {
  profile: "اصلاح مرجع پروفایل",
  contact: "اصلاح مرجع تماس",
  interaction: "اصلاح تماس یا پایش ثبت‌شده",
  observation: "اصلاح مشاهده یا نیاز ثبت‌شده",
};
function localTime(iso: string): string {
  const date = new Date(iso);
  if (!Number.isFinite(date.getTime())) return "";
  return new Date(date.getTime() - date.getTimezoneOffset() * 60_000).toISOString().slice(0, 16);
}

/** Human corrections are append-only new revisions, never UPDATE/DELETE. */
export default function CaseCorrections({
  actor, profile, onChanged, onAuthenticationLost,
}: {
  actor: ActorContext;
  profile: CaseProfileView;
  onChanged: () => void;
  onAuthenticationLost: () => void;
}) {
  const kinds = (["profile", "contact", "interaction", "observation"] as const)
    .filter(kind => correctionAllowed(
      actor, kind, profile.current_assignment.caregiver_actor_id,
    ));
  const [kind, setKind] = useState<CorrectionKind>("profile");
  const active = kinds.includes(kind) ? kind : kinds[0];
  const [records, setRecords] = useState<(ContactRecord | InteractionRecorded | ObservationView)[]>([]);
  const [nextCursor, setNextCursor] = useState<string | null>(null);
  const [cursor, setCursor] = useState<string | null>(null);
  const [chosenId, setChosenId] = useState("");
  const [content, setContent] = useState(profile.profile.elder_reference);
  const [recordType, setRecordType] = useState("OBSERVATION");
  const [occurredAt, setOccurredAt] = useState("");
  const [reason, setReason] = useState("");
  const [loading, setLoading] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);
  const [pending, setPending] = useState<{ signature: string; key: string } | null>(null);
  const [revision, setRevision] = useState(0);

  useEffect(() => {
    if (!active || active === "profile") return;
    const controller = new AbortController();
    setLoading(true); setError(null); setRecords([]); setNextCursor(null);
    const promise: Promise<{
      items: (ContactRecord | InteractionRecorded | ObservationView)[];
      next_cursor: string | null;
    }> = active === "contact"
      ? api.contacts(profile.case.id, controller.signal).then(items => ({
        items: latestContactRevisions(items), next_cursor: null,
      }))
      : active === "interaction"
        ? api.interactions(profile.case.id, cursor, controller.signal)
        : api.observations(profile.case.id, cursor, controller.signal);
    promise.then(page => {
      if (!controller.signal.aborted) {
        setRecords(page.items); setNextCursor(page.next_cursor);
      }
    }).catch(cause => {
      if (controller.signal.aborted) return;
      if (cause instanceof ApiError && cause.status === 401) onAuthenticationLost();
      else setError(errorMessage(cause));
    }).finally(() => {
      if (!controller.signal.aborted) setLoading(false);
    });
    return () => controller.abort();
  }, [active, profile.case.id, cursor, revision, onAuthenticationLost]);

  if (!active) return null;
  const selected = records.find(item => item.id === chosenId);
  const targetId = active === "contact" && selected && "logical_contact_id" in selected
    ? selected.logical_contact_id : selected?.id ?? null;

  function resetIntent() {
    setError(null); setSuccess(false); setPending(null);
  }
  function selectKind(value: CorrectionKind) {
    resetIntent(); setKind(value); setCursor(null); setChosenId("");
    setContent(value === "profile" ? profile.profile.elder_reference : "");
    setRecordType(value === "interaction" ? "CONTACT" : "OBSERVATION");
    setOccurredAt(""); setReason("");
  }
  function selectRecord(id: string) {
    resetIntent(); setChosenId(id); setReason("");
    const item = records.find(row => row.id === id);
    if (!item) { setContent(""); setOccurredAt(""); return; }
    if ("contact_value" in item) {
      setContent(item.contact_value); setRecordType(item.contact_kind); setOccurredAt("");
    } else if ("interaction_type" in item) {
      setContent(item.content); setRecordType(item.interaction_type);
      setOccurredAt(localTime(item.occurred_at));
    } else {
      setContent(item.content); setRecordType(item.record_type);
      setOccurredAt(localTime(item.occurred_at));
    }
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!active || submitting || (active !== "profile" && !selected)) return;
    setError(null); setSuccess(false);
    try {
      const common = {
        expected_current_assignment_id: profile.current_assignment.id,
        correction_reason: reason.trim(),
      };
      const body = active === "profile"
        ? {
          ...common, expected_current_revision_id: profile.profile.id,
          elder_reference: content.trim(),
        }
        : active === "contact" && selected
          ? {
            ...common, expected_current_revision_id: selected.id,
            contact_kind: recordType.trim(), contact_value: content.trim(),
          }
          : active === "interaction" && selected
            ? {
              ...common, expected_current_record_id: selected.id,
              interaction_type: recordType as "CONTACT" | "MONITORING",
              occurred_at: toObservedUtc(occurredAt), content: content.trim(),
            }
            : {
              ...common, expected_current_record_id: selected!.id,
              record_type: recordType as "OBSERVATION" | "NEED_CAPTURE",
              occurred_at: toObservedUtc(occurredAt), content: content.trim(),
            };
      const signature = JSON.stringify({ active, caseId: profile.case.id, targetId, body });
      let intent = pending?.signature === signature ? pending : null;
      if (!intent) {
        intent = { signature, key: newIntentKey() };
        setPending(intent);
      }
      setSubmitting(true);
      if (active === "profile") {
        await submitCorrection("profile", profile.case.id, null, body as {
          expected_current_assignment_id: string; correction_reason: string;
          expected_current_revision_id: string; elder_reference: string;
        }, intent.key);
      } else if (active === "contact") {
        await submitCorrection("contact", profile.case.id, targetId, body as {
          expected_current_assignment_id: string; correction_reason: string;
          expected_current_revision_id: string; contact_kind: string; contact_value: string;
        }, intent.key);
      } else if (active === "interaction") {
        await submitCorrection("interaction", profile.case.id, targetId, body as {
          expected_current_assignment_id: string; correction_reason: string;
          expected_current_record_id: string; interaction_type: "CONTACT" | "MONITORING";
          occurred_at: string; content: string;
        }, intent.key);
      } else {
        await submitCorrection("observation", profile.case.id, targetId, body as {
          expected_current_assignment_id: string; correction_reason: string;
          expected_current_record_id: string; record_type: "OBSERVATION" | "NEED_CAPTURE";
          occurred_at: string; content: string;
        }, intent.key);
      }
      setPending(null); setReason(""); setChosenId(""); setSuccess(true);
      setCursor(null); setRevision(value => value + 1);
      onChanged();
    } catch (cause) {
      if (cause instanceof ApiError && cause.status === 401) {
        setPending(null); onAuthenticationLost(); return;
      }
      if (cause instanceof ApiError && cause.status === 409) {
        setError("نسخه رکورد یا تخصیص تغییر کرده است. اصلاح تازه‌ای ثبت نشد؛ ابتدا سوابق جدید را بخوانید.");
        onChanged();
      } else {
        setError(errorMessage(cause));
      }
    } finally {
      setSubmitting(false);
    }
  }

  return <section className="card" aria-label="اصلاح نسخه‌دار پرونده">
    <header className="section-title">
      <h3>اصلاح نسخه‌دار سوابق انسانی</h3>
      <span className="chip">ثبت نسخه جدید، بدون حذف سابقه</span>
    </header>
    <p className="disclaimer">
      اصلاح فقط با دلیل انسانی و شناسه نسخه مورد انتظار انجام می‌شود.
      ممکن است رکورد انتخاب‌شده بعد از دریافت این صفحه تغییر کرده باشد؛ Backend آن را کنترل می‌کند.
      اصلاح نیاز، به معنی تغییر خودکار ارجاع‌های گذشته یا نتیجه خدمت نیست.
    </p>
    <form className="record-form" onSubmit={e => { void submit(e); }}>
      <label htmlFor="correction-kind">نوع اصلاح</label>
      <select id="correction-kind" value={active} disabled={submitting}
        onChange={e => selectKind(e.target.value as CorrectionKind)}>
        {kinds.map(value => <option key={value} value={value}>{labels[value]}</option>)}
      </select>
      {active !== "profile" && <>
        <label htmlFor="correction-target">رکورد قابل مشاهده برای اصلاح</label>
        <select id="correction-target" value={chosenId} required disabled={submitting || loading}
          onChange={e => selectRecord(e.target.value)}>
          <option value="">رکورد را انتخاب کنید</option>
          {records.map(row => <option key={row.id} value={row.id}>
            {shortId(row.id)} · {"recorded_at" in row ? formatDate(row.recorded_at) : ""}
          </option>)}
        </select>
        {loading && <p role="status">در حال دریافت سوابق از Backend…</p>}
        {nextCursor && <button type="button" className="subtle" disabled={submitting}
          onClick={() => { resetIntent(); setChosenId(""); setCursor(nextCursor); }}>
          صفحه بعد رکوردها
        </button>}
        {cursor && <button type="button" className="subtle" disabled={submitting}
          onClick={() => { resetIntent(); setChosenId(""); setCursor(null); }}>
          صفحه نخست رکوردها
        </button>}
      </>}
      {(active === "contact") && <>
        <label htmlFor="correction-contact-kind">برچسب نوع تماس اصلاح‌شده</label>
        <input id="correction-contact-kind" value={recordType} disabled={submitting} required
          onChange={e => { resetIntent(); setRecordType(e.target.value); }} />
      </>}
      {(active === "interaction" || active === "observation") && <>
        <label htmlFor="correction-record-type">نوع رکورد</label>
        <select id="correction-record-type" value={recordType} disabled={submitting}
          onChange={e => { resetIntent(); setRecordType(e.target.value); }}>
          {(active === "interaction" ? ["CONTACT", "MONITORING"] : ["OBSERVATION", "NEED_CAPTURE"])
            .map(t => <option value={t} key={t}>{t}</option>)}
        </select>
        <label htmlFor="correction-occurred">زمان واقعی وقوع</label>
        <input id="correction-occurred" type="datetime-local" required disabled={submitting}
          value={occurredAt} onChange={e => { resetIntent(); setOccurredAt(e.target.value); }} />
      </>}
      <label htmlFor="correction-content">{active === "profile" ? "شناسه مرجع سالمند" : "محتوای اصلاح‌شده"}</label>
      <textarea id="correction-content" required rows={2} value={content} disabled={submitting}
        onChange={e => { resetIntent(); setContent(e.target.value); }} />
      <label htmlFor="correction-reason">دلیل اصلاح (اجباری)</label>
      <textarea id="correction-reason" required rows={2} value={reason} disabled={submitting}
        onChange={e => { resetIntent(); setReason(e.target.value); }} />
      {error && <p role="alert" className="notice">{error}</p>}
      {success && <p role="status">نسخه اصلاحی پذیرفته شد؛ سوابق از سرور بازخوانی می‌شوند.</p>}
      <button type="submit" disabled={submitting || !content.trim() || !reason.trim() ||
        (active !== "profile" && !chosenId) ||
        ((active === "interaction" || active === "observation") && !occurredAt)}>
        {submitting ? "در حال ثبت…" : "ثبت نسخه اصلاحی"}
      </button>
    </form>
  </section>;
}
