import { useState } from "react";
import type { FormEvent } from "react";
import { ApiError } from "./api";
import { errorMessage } from "./format";
import {
  canRecordProvider, makeIdempotencyKey, postProviderIntake,
} from "./providerCommands";
import type { ProviderIntakeKind } from "./providerCommands";
import type { ActorContext } from "./types";

const labels: Record<ProviderIntakeKind, string> = {
  candidate: "ثبت اولیه Candidate",
  evidence: "ثبت شواهد ارائه‌شده",
  review_request: "ثبت درخواست بررسی",
};

export default function ProviderIntake({
  actor, candidateId, onSaved, onAuthenticationLost,
}: {
  actor: ActorContext;
  candidateId: string | null;
  onSaved: (newCandidateId: string | null) => void;
  onAuthenticationLost: () => void;
}) {
  const available = (["candidate", "evidence", "review_request"] as const).filter(kind =>
    canRecordProvider(actor, kind) && (kind === "candidate" ? candidateId === null : !!candidateId));
  const [kind, setKind] = useState<ProviderIntakeKind>(candidateId ? "evidence" : "candidate");
  const [displayName, setDisplayName] = useState("");
  const [evidenceLabel, setEvidenceLabel] = useState("");
  const [evidenceReference, setEvidenceReference] = useState("");
  const [reason, setReason] = useState("");
  const [pending, setPending] = useState<{ payload: string; key: string } | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);
  const active = available.includes(kind) ? kind : available[0];

  if (!active) return null;

  function changed() {
    setError(null);
    setSuccess(false);
    setPending(null);
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (busy || !active) return;
    setError(null); setSuccess(false);
    const body = active === "candidate"
      ? { display_name: displayName.trim(), reason: reason.trim() }
      : active === "evidence"
        ? {
          evidence_label: evidenceLabel.trim(),
          evidence_reference: evidenceReference.trim(),
          reason: reason.trim(),
        }
        : { reason: reason.trim() };
    const payload = JSON.stringify({ active, candidateId, body });
    let intent = pending?.payload === payload ? pending : null;
    try {
      if (!intent) {
        intent = { payload, key: makeIdempotencyKey() };
        setPending(intent);
      }
      setBusy(true);
      const result = await postProviderIntake(active, candidateId, body, intent.key);
      setPending(null);
      setDisplayName(""); setEvidenceLabel(""); setEvidenceReference(""); setReason("");
      setSuccess(true);
      onSaved(active === "candidate" ? result.id : null);
    } catch (e) {
      if (e instanceof ApiError && e.status === 401) {
        setPending(null);
        onAuthenticationLost();
        return;
      }
      setError(e instanceof ApiError && e.status === 409
        ? "این درخواست قبلاً با محتوای متفاوت پذیرفته شده یا داده‌ها تغییر کرده‌اند؛ ابتدا سوابق واقعی را بررسی کنید."
        : errorMessage(e));
    } finally {
      setBusy(false);
    }
  }

  return <section className="card" aria-label="ثبت مقدماتی Provider">
    <header className="section-title">
      <h3>ثبت مستندات مقدماتی Provider</h3>
      <span className="chip">فاقد حکم صلاحیت</span>
    </header>
    <p className="disclaimer">
      ثبت Candidate، مدرک یا درخواست بررسی به معنی تأیید، فعال‌سازی، انتخاب یا اعزام ارائه‌دهنده نیست.
    </p>
    <form className="record-form" onSubmit={e => { void submit(e); }}>
      <label htmlFor="provider-kind">نوع ثبت</label>
      <select id="provider-kind" disabled={busy} value={active}
        onChange={e => { changed(); setKind(e.target.value as ProviderIntakeKind); }}>
        {available.map(item => <option key={item} value={item}>{labels[item]}</option>)}
      </select>
      {active === "candidate" && <>
        <label htmlFor="provider-name">نام معرفی‌شده Candidate</label>
        <input id="provider-name" required disabled={busy} value={displayName}
          onChange={e => { changed(); setDisplayName(e.target.value); }} />
      </>}
      {active === "evidence" && <>
        <label htmlFor="provider-evidence-label">عنوان مدرک ارائه‌شده</label>
        <input id="provider-evidence-label" required disabled={busy} value={evidenceLabel}
          onChange={e => { changed(); setEvidenceLabel(e.target.value); }} />
        <label htmlFor="provider-evidence-ref">مرجع ثبت‌شده مدرک (شناسه، نه فایل آپلودشده)</label>
        <input id="provider-evidence-ref" required disabled={busy} value={evidenceReference}
          onChange={e => { changed(); setEvidenceReference(e.target.value); }} />
      </>}
      <label htmlFor="provider-reason">دلیل ثبت</label>
      <textarea id="provider-reason" rows={2} required disabled={busy} value={reason}
        onChange={e => { changed(); setReason(e.target.value); }} />
      {candidateId && <p className="meta">شناسه Candidate منتخب: <bdi>{candidateId}</bdi></p>}
      {error && <p role="alert" className="notice">{error}</p>}
      {success && <p role="status">رکورد پذیرفته شد؛ اطلاعات از سرور بازخوانی می‌شوند.</p>}
      <button type="submit" disabled={busy || !reason.trim() ||
        (active === "candidate" && !displayName.trim()) ||
        (active === "evidence" && (!evidenceLabel.trim() || !evidenceReference.trim()))}>
        {busy ? "در حال ثبت…" : "ثبت مقدماتی"}
      </button>
    </form>
  </section>;
}
