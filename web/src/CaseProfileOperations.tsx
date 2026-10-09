import { useEffect, useState } from "react";
import { api, ApiError } from "./api";
import CaseOperations from "./CaseOperations";
import CaseCorrections from "./CaseCorrections";
import { errorMessage, formatDate } from "./format";
import type { ActorContext, CaseProfileView } from "./types";

/** A Case profile view for authorized readers without Referral/Follow-up access. */
export default function CaseProfileOperations({
  caseId, actor, back, onAuthenticationLost,
}: {
  caseId: string;
  actor: ActorContext;
  back: () => void;
  onAuthenticationLost: () => void;
}) {
  const [profile, setProfile] = useState<CaseProfileView | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(true);
  const [revision, setRevision] = useState(0);

  useEffect(() => {
    const controller = new AbortController();
    setProfile(null); setError(null); setBusy(true);
    api.caseProfile(caseId, controller.signal).then(value => {
      if (!controller.signal.aborted) setProfile(value);
    }).catch(cause => {
      if (controller.signal.aborted) return;
      if (cause instanceof ApiError && cause.status === 401) onAuthenticationLost();
      else setError(errorMessage(cause));
    }).finally(() => {
      if (!controller.signal.aborted) setBusy(false);
    });
    return () => controller.abort();
  }, [caseId, revision, onAuthenticationLost]);

  return <section aria-label="پروفایل و عملیات پرونده">
    <button className="subtle" type="button" onClick={back}>بازگشت به پرونده‌ها</button>
    {busy && <p role="status">در حال خواندن آخرین تخصیص از سرور…</p>}
    {error && <p role="alert" className="notice">{error}</p>}
    {profile && <div className="stack">
      <article className="card">
        <h2>پرونده ثبت‌شده</h2>
        <p className="meta">شناسه: <bdi>{profile.case.id}</bdi></p>
        <p>مرجع سالمند: <bdi>{profile.profile.elder_reference}</bdi></p>
        <p>نسخه پروفایل: {profile.profile.revision_no}</p>
        <p>سالمندیار فعلی: <bdi>{profile.current_assignment.caregiver_actor_id}</bdi></p>
        <p className="meta">زمان تخصیص: {formatDate(profile.current_assignment.started_at)}</p>
        <p className="disclaimer">این نما دسترسی به ارجاع، پیگیری یا نتیجه خدمت اعطا نمی‌کند.</p>
      </article>
      <CaseOperations
        actor={actor} profile={profile}
        onChanged={() => setRevision(value => value + 1)}
        onAuthenticationLost={onAuthenticationLost}
      />
      <CaseCorrections
        actor={actor} profile={profile}
        onChanged={() => setRevision(value => value + 1)}
        onAuthenticationLost={onAuthenticationLost}
      />
    </div>}
  </section>;
}
