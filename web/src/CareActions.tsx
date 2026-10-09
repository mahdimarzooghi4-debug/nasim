import { useState } from "react";
import type { FormEvent } from "react";
import { ApiError } from "./api";
import { errorMessage } from "./format";
import {
  canRecord, makeIdempotencyKey, recordCareAction, toObservedUtc,
} from "./commands";
import type { InteractionKind, ObservationKind, RecordingKind } from "./commands";
import type { ActorContext, ObservationView } from "./types";

function currentLocalTime(): string {
  const now = new Date();
  return new Date(now.getTime() - now.getTimezoneOffset() * 60_000)
    .toISOString().slice(0, 16);
}

interface Props {
  actor: ActorContext;
  caseId: string;
  assignmentId: string;
  assignedActorId: string;
  observations: ObservationView[];
  selectedReferralId: string | null;
  onRecorded: () => void;
  onAuthenticationLost: () => void;
}

const KIND_LABELS: Record<RecordingKind, string> = {
  observation: "ثبت مشاهده یا نیاز",
  interaction: "ثبت تماس یا پایش",
  referral: "ثبت ارجاع بر اساس نیاز",
  follow_up: "ثبت پیگیری انسانی ارجاع",
};

export default function CareActions({
  actor, caseId, assignmentId, assignedActorId,
  observations, selectedReferralId, onRecorded, onAuthenticationLost,
}: Props) {
  const available = (["observation", "interaction", "referral", "follow_up"] as const)
    .filter(kind => canRecord(actor, kind, assignedActorId) &&
      (kind !== "follow_up" || selectedReferralId !== null));
  const [kind, setKind] = useState<RecordingKind>("observation");
  const [recordType, setRecordType] = useState<ObservationKind>("OBSERVATION");
  const [interactionType, setInteractionType] = useState<InteractionKind>("CONTACT");
  const [eventTime, setEventTime] = useState(currentLocalTime);
  const [content, setContent] = useState("");
  const [reason, setReason] = useState("");
  const [needId, setNeedId] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);
  const [pending, setPending] = useState<{ signature: string; key: string } | null>(null);
  const visibleKind = available.includes(kind) ? kind : available[0];
  const needChoices = observations.filter(x => x.record_type === "NEED_CAPTURE");

  if (!visibleKind) return null;

  function markEdited() {
    setError(null);
    setSuccess(false);
    // Mutating a submitted payload MUST get a distinct idempotency identity.
    setPending(null);
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (submitting || !visibleKind) return;
    setError(null);
    setSuccess(false);

    try {
      const body = visibleKind === "observation"
      ? {
        expected_current_assignment_id: assignmentId,
        record_type: recordType,
        occurred_at: toObservedUtc(eventTime),
        content: content.trim(),
      }
      : visibleKind === "interaction"
        ? {
          expected_current_assignment_id: assignmentId,
          interaction_type: interactionType,
          occurred_at: toObservedUtc(eventTime),
          content: content.trim(),
        }
        : visibleKind === "referral"
          ? {
            expected_current_assignment_id: assignmentId,
            source_need_observation_id: needId,
            reason: reason.trim(),
          }
          : {
            expected_current_assignment_id: assignmentId,
            note: content.trim(),
            reason: reason.trim(),
          };
      const signature = JSON.stringify({ kind: visibleKind, caseId, selectedReferralId, body });
      let next = pending?.signature === signature ? pending : null;
      // Key is kept for uncertain network result/retry; never silently create a duplicate.
      if (!next) {
        next = { signature, key: makeIdempotencyKey() };
        setPending(next);
      }
      setSubmitting(true);
      await recordCareAction(visibleKind, caseId, selectedReferralId, body, next.key);
      setPending(null);
      setContent("");
      setReason("");
      setNeedId("");
      setEventTime(currentLocalTime());
      setSuccess(true);
      onRecorded();
    } catch (cause) {
      if (cause instanceof ApiError && cause.status === 401) {
        setPending(null);
        onAuthenticationLost();
        return;
      }
      if (cause instanceof ApiError && cause.status === 409) {
        setError("تخصیص یا نسخه رکورد تغییر کرده است یا کلید درخواست با محتوای دیگری استفاده شده؛ بدون بررسی دوباره اطلاعات، درخواست تازه ثبت نکنید.");
      } else {
        setError(errorMessage(cause));
      }
    } finally {
      setSubmitting(false);
    }
  }

  return <section className="card" aria-label="ثبت عملیات انسانی">
    <div className="section-title">
      <div>
        <p className="eyebrow">فرم‌های موجود در قرارداد Backend</p>
        <h3>ثبت اقدام انسانی در پرونده</h3>
      </div>
      <span className="chip">نیازمند مجوز و تخصیص فعلی</span>
    </div>
    <p className="disclaimer">
      این ثبت‌ها گزارش انسانی هستند؛ اثبات انجام خدمت، تأیید ارائه‌دهنده، تصمیم پزشکی یا نتیجه نهایی نیستند.
    </p>
    <form onSubmit={event => { void submit(event); }} className="record-form">
      <label htmlFor="action-kind">نوع ثبت</label>
      <select id="action-kind" value={visibleKind} disabled={submitting}
        onChange={event => { markEdited(); setKind(event.target.value as RecordingKind); }}>
        {available.map(item => <option key={item} value={item}>{KIND_LABELS[item]}</option>)}
      </select>

      {visibleKind === "observation" && <>
        <label htmlFor="record-type">نوع رکورد</label>
        <select id="record-type" value={recordType} disabled={submitting}
          onChange={event => { markEdited(); setRecordType(event.target.value as ObservationKind); }}>
          <option value="OBSERVATION">مشاهده</option>
          <option value="NEED_CAPTURE">ثبت نیاز مشاهده‌شده</option>
        </select>
      </>}
      {visibleKind === "interaction" && <>
        <label htmlFor="interaction-type">نوع تعامل</label>
        <select id="interaction-type" value={interactionType} disabled={submitting}
          onChange={event => { markEdited(); setInteractionType(event.target.value as InteractionKind); }}>
          <option value="CONTACT">تماس</option>
          <option value="MONITORING">پایش</option>
        </select>
      </>}
      {(visibleKind === "observation" || visibleKind === "interaction") && <>
        <label htmlFor="occurred-at">زمان وقوع واقعی (قابل اصلاح پیش از ثبت)</label>
        <input id="occurred-at" type="datetime-local" required value={eventTime}
          disabled={submitting}
          onChange={event => { markEdited(); setEventTime(event.target.value); }} />
      </>}
      {visibleKind === "referral" && <>
        <label htmlFor="need-source">نیاز ثبت‌شده مبنای ارجاع</label>
        <select id="need-source" required disabled={submitting}
          value={needId} onChange={event => { markEdited(); setNeedId(event.target.value); }}>
          <option value="">انتخاب رکورد نیاز از صفحه فعلی</option>
          {needChoices.map(ob => <option key={ob.id} value={ob.id}>
            {ob.content.slice(0, 70)} — {ob.id.slice(0, 8)}
          </option>)}
        </select>
        <p className="meta">رکورد باید در لحظه ثبت همچنان معتبر باشد؛ Backend این شرط را کنترل می‌کند.</p>
      </>}
      {visibleKind !== "referral" && <>
        <label htmlFor="action-content">{visibleKind === "follow_up" ? "شرح پیگیری انسانی" : "شرح مشاهده یا اقدام"}</label>
        <textarea id="action-content" required minLength={1} value={content} rows={3}
          disabled={submitting}
          onChange={event => { markEdited(); setContent(event.target.value); }} />
      </>}
      {(visibleKind === "referral" || visibleKind === "follow_up") && <>
        <label htmlFor="action-reason">دلیل ثبت</label>
        <textarea id="action-reason" required minLength={1} value={reason} rows={2}
          disabled={submitting}
          onChange={event => { markEdited(); setReason(event.target.value); }} />
      </>}
      {visibleKind === "referral" && needChoices.length === 0 &&
        <p className="meta">برای ارجاع، ابتدا نیاز را ثبت کنید یا صفحه شامل رکورد نیاز را باز کنید.</p>}
      {visibleKind === "follow_up" && selectedReferralId &&
        <p className="meta">ارجاع منتخب: <bdi>{selectedReferralId}</bdi></p>}

      {error && <p role="alert" className="notice">{error}</p>}
      {success && <p role="status">رکورد پذیرفته و ثبت شد؛ داده‌ها دوباره از سرور خوانده می‌شوند.</p>}
      <button type="submit" disabled={submitting ||
        (visibleKind === "referral" && !needId) ||
        ((visibleKind === "follow_up" || visibleKind === "observation" ||
          visibleKind === "interaction") && !content.trim()) ||
        ((visibleKind === "follow_up" || visibleKind === "referral") && !reason.trim())}>
        {submitting ? "در حال ارسال…" : "ثبت در سامانه"}
      </button>
    </form>
  </section>;
}
