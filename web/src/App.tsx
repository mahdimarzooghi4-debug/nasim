import { useEffect, useState } from "react";
import CareActions from "./CareActions";
import CaseCorrections from "./CaseCorrections";
import CaseHistory from "./CaseHistory";
import CaseCreate from "./CaseCreate";
import CaseOperations from "./CaseOperations";
import CaseProfileOperations from "./CaseProfileOperations";
import { mayManageCases } from "./caseCommands";
import ProviderIntake from "./ProviderIntake";
import { canRecordProvider } from "./providerCommands";
import type { ReactNode } from "react";
import {
  api, ApiError, canReadCases, canReadJourney, canReadProviders,
  canReadProviderWorkspace,
} from "./api";
import { errorMessage, formatDate, shortId } from "./format";
import type {
  ActorContext, CareJourneyWorkspaceView, CaseProfileView, Page,
  ProviderCandidateView, ProviderWorkspaceView,
} from "./types";

function Alert({ children }: { children: ReactNode }) {
  return <div role="alert" className="notice">{children}</div>;
}
function Empty({ text }: { text: string }) {
  return <p className="empty">{text}</p>;
}
function Pager({ next, back, onNext, onBack }: {
  next: boolean; back: boolean; onNext: () => void; onBack: () => void;
}) {
  return <div className="pager">
    <button type="button" disabled={!back} onClick={onBack}>صفحه قبل</button>
    <button type="button" disabled={!next} onClick={onNext}>صفحه بعد</button>
  </div>;
}
function Field({ label, children }: { label: string; children: ReactNode }) {
  return <div className="field"><span>{label}</span><strong>{children}</strong></div>;
}
function Status({ busy, error }: { busy: boolean; error: string | null }) {
  return <>
    {busy && <p role="status" className="muted">در حال دریافت اطلاعات مجاز…</p>}
    {error && <Alert>{error}</Alert>}
  </>;
}
type LostAccess = () => void;
const expired = (error: unknown) => error instanceof ApiError && error.status === 401;

function CaseJourney({ caseId, actor, back, onLost }: {
  caseId: string; actor: ActorContext; back: () => void; onLost: LostAccess;
}) {
  const [selected, setSelected] = useState<string | null>(null);
  const [obsCursor, setObsCursor] = useState<string | null>(null);
  const [refCursor, setRefCursor] = useState<string | null>(null);
  const [followCursor, setFollowCursor] = useState<string | null>(null);
  const [view, setView] = useState<CareJourneyWorkspaceView | null>(null);
  const [revision, setRevision] = useState(0);
  const [busy, setBusy] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();
    setView(null);
    setBusy(true);
    setError(null);
    api.journey(caseId, {
      referralId: selected, observationCursor: obsCursor,
      referralCursor: refCursor, followUpCursor: followCursor,
    }, controller.signal).then(data => {
      if (!controller.signal.aborted) setView(data);
    }).catch(e => {
      if (controller.signal.aborted) return;
      if (expired(e)) onLost();
      else setError(errorMessage(e));
    }).finally(() => { if (!controller.signal.aborted) setBusy(false); });
    return () => controller.abort();
  }, [caseId, selected, obsCursor, refCursor, followCursor, revision, onLost]);

  function selectReferral(next: string | null) {
    setSelected(next);
    setFollowCursor(null);
  }

  return <section aria-label="جزئیات پرونده">
    <button className="subtle" type="button" onClick={back}>بازگشت به پرونده‌ها</button>
    <Status busy={busy} error={error} />
    {error && <button type="button" onClick={() => {
      setObsCursor(null); setRefCursor(null); setFollowCursor(null);
    }}>بارگذاری مجدد</button>}
    {view && <div className="stack">
      <header className="section-title">
        <div><p className="eyebrow">پرونده ثبت‌شده</p>
          <h2>نمای سفر سالمند</h2></div>
        <span className="chip">صرفاً سوابق ثبت‌شده</span>
      </header>
      <div className="cards two-col">
        <article className="card">
          <h3>اطلاعات پرونده</h3>
          <Field label="شناسه پرونده"><code dir="ltr">{view.case.case.id}</code></Field>
          <Field label="شناسه سالمند"><span dir="auto">{view.case.profile.elder_reference}</span></Field>
          <Field label="آخرین اصلاح پروفایل">نسخه {view.case.profile.revision_no}</Field>
          <Field label="تاریخ ایجاد">{formatDate(view.case.case.created_at)}</Field>
        </article>
        <article className="card">
          <h3>مسئول ثبت‌شده</h3>
          <Field label="شناسه سالمندیار"><span dir="ltr">{view.case.current_assignment.caregiver_actor_id}</span></Field>
          <Field label="شروع تخصیص">{formatDate(view.case.current_assignment.started_at)}</Field>
          <Field label="منشأ ورود"><span dir="auto">{view.case.case.upstream_enrollment_ref}</span></Field>
        </article>
      </div>
      <div className="cards two-col">
        <section className="card" aria-label="مشاهدات ثبت‌شده">
          <h3>مشاهدات و نیازهای ثبت‌شده</h3>
          {view.observations.items.length === 0 && <Empty text="مشاهده‌ای در این صفحه ثبت نشده است." />}
          <ul className="records">
            {view.observations.items.map(item => <li key={item.id}>
              <div className="meta">{item.record_type === "NEED_CAPTURE" ? "ثبت نیاز" : "مشاهده"}
                {" · "}{formatDate(item.recorded_at)}</div>
              <p className="record-content">{item.content}</p>
              <span className="meta">ثبت‌کننده: <bdi>{item.recorded_by_actor_id}</bdi></span>
            </li>)}
          </ul>
          <button type="button" disabled={!view.observations.next_cursor}
            onClick={() => setObsCursor(view.observations.next_cursor)}>صفحه بعد مشاهدات</button>
          {obsCursor && <button className="subtle" type="button" onClick={() => setObsCursor(null)}>شروع مشاهدات</button>}
        </section>
        <section className="card" aria-label="ارجاعات ثبت‌شده">
          <h3>ارجاع‌های ثبت‌شده</h3>
          {view.referrals.items.length === 0 && <Empty text="ارجاعی در این صفحه ثبت نشده است." />}
          <ul className="records">
            {view.referrals.items.map(item => <li key={item.id}>
              <div className="meta">{formatDate(item.created_at)} · <bdi>{shortId(item.id)}</bdi></div>
              <p className="record-content">{item.reason}</p>
              <button type="button" aria-pressed={selected === item.id}
                onClick={() => selectReferral(item.id)}>مشاهده پیگیری‌های این ارجاع</button>
            </li>)}
          </ul>
          <button type="button" disabled={!view.referrals.next_cursor}
            onClick={() => setRefCursor(view.referrals.next_cursor)}>صفحه بعد ارجاعات</button>
          {refCursor && <button className="subtle" type="button" onClick={() => setRefCursor(null)}>شروع ارجاعات</button>}
        </section>
      </div>
      <CaseOperations
        actor={actor}
        profile={view.case}
        onAuthenticationLost={onLost}
        onChanged={() => setRevision(value => value + 1)}
      />
      <CaseCorrections
        actor={actor} profile={view.case}
        onAuthenticationLost={onLost}
        onChanged={() => setRevision(value => value + 1)}
      />
      <CaseHistory caseId={caseId} actor={actor} onAuthenticationLost={onLost} />
      <CareActions
        actor={actor}
        caseId={caseId}
        assignmentId={view.case.current_assignment.id}
        assignedActorId={view.case.current_assignment.caregiver_actor_id}
        observations={view.observations.items}
        selectedReferralId={selected}
        onAuthenticationLost={onLost}
        onRecorded={() => {
          // Re-read authoritative state, including a fresh assignment on the server.
          setObsCursor(null); setRefCursor(null); setFollowCursor(null);
          setRevision(value => value + 1);
        }}
      />
      {view.selected_referral && view.follow_ups && <section className="card">
        <div className="section-title">
          <h3>پیگیری‌های انسانیِ ارجاع <bdi>{shortId(view.selected_referral.id)}</bdi></h3>
          <button type="button" onClick={() => selectReferral(null)}>بستن جزئیات</button>
        </div>
        <p className="disclaimer">این یادداشت‌ها اثبات انجام خدمت یا نتیجه سلامت سالمند نیستند.</p>
        {view.follow_ups.items.length === 0 && <Empty text="هنوز پیگیری‌ای برای این ارجاع ثبت نشده است." />}
        <ul className="records">
          {view.follow_ups.items.map(item => <li key={item.id}>
            <div className="meta">{formatDate(item.recorded_at)} · <bdi>{item.recorded_by_actor_id}</bdi></div>
            <p className="record-content">{item.note}</p>
            <div className="meta">دلیل ثبت: {item.reason}</div>
          </li>)}
        </ul>
        <button type="button" disabled={!view.follow_ups.next_cursor}
          onClick={() => setFollowCursor(view.follow_ups?.next_cursor ?? null)}>صفحه بعد پیگیری‌ها</button>
        {followCursor && <button className="subtle" type="button" onClick={() => setFollowCursor(null)}>شروع پیگیری‌ها</button>}
      </section>}
    </div>}
  </section>;
}

function CaseIndex({ actor, onLost }: { actor: ActorContext; onLost: LostAccess }) {
  const [cursor, setCursor] = useState<string | null>(null);
  const [history, setHistory] = useState<(string | null)[]>([]);
  const [data, setData] = useState<Page<CaseProfileView> | null>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [busy, setBusy] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [revision, setRevision] = useState(0);

  useEffect(() => {
    const controller = new AbortController();
    setBusy(true); setError(null); setData(null);
    if (!canReadCases(actor)) {
      setBusy(false);
      return () => controller.abort();
    }
    api.cases(cursor, controller.signal).then(next => {
      if (!controller.signal.aborted) setData(next);
    }).catch(e => {
      if (controller.signal.aborted) return;
      if (expired(e)) onLost();
      else setError(errorMessage(e));
    }).finally(() => { if (!controller.signal.aborted) setBusy(false); });
    return () => controller.abort();
  }, [cursor, revision, actor, onLost]);

  if (selected) {
    return canReadJourney(actor)
      ? <CaseJourney
        caseId={selected} actor={actor} onLost={onLost} back={() => setSelected(null)}
      />
      : <CaseProfileOperations
        caseId={selected} actor={actor} onAuthenticationLost={onLost}
        back={() => { setSelected(null); setRevision(value => value + 1); }}
      />;
  }

  return <section>
    <header className="section-title">
      <div><p className="eyebrow">دسترسی از روی تخصیص فعلی</p><h2>پرونده‌های قابل مشاهده</h2></div>
      <button type="button" className="subtle" onClick={() => setRevision(v => v + 1)}>به‌روزرسانی</button>
    </header>
    <p className="disclaimer">فهرست تنها پرونده‌های مجاز در لحظه درخواست را نشان می‌دهد؛ فاقد اولویت، وضعیت خدمت یا ارزیابی خودکار است.</p>
    <CaseCreate
      actor={actor} onAuthenticationLost={onLost}
      onAccepted={() => { setCursor(null); setHistory([]); setRevision(value => value + 1); }}
    />
    {!canReadCases(actor) && <Alert>مجوز خواندن فهرست پرونده‌ها موجود نیست؛ تنها عملیات مدیریتیِ مجاز در دسترس است.</Alert>}
    <Status busy={busy && canReadCases(actor)} error={error} />
    {data && <>
      {data.items.length === 0 && <Empty text="پرونده‌ای با این مجوز و تخصیص فعلی در این صفحه پیدا نشد." />}
      <div className="cards">
        {data.items.map(item => <article className="card case-card" key={item.case.id}>
          <div><h3><span dir="auto">{item.profile.elder_reference}</span></h3>
            <p className="meta">شناسه: <bdi>{shortId(item.case.id)}</bdi> · ایجاد: {formatDate(item.case.created_at)}</p>
            <p className="meta">سالمندیار فعلی: <bdi>{item.current_assignment.caregiver_actor_id}</bdi></p></div>
          <button type="button" onClick={() => setSelected(item.case.id)}
            aria-label={"مشاهده جزئیات مجاز پرونده " + item.profile.elder_reference}>
            مشاهده جزئیات مجاز
          </button>
        </article>)}
      </div>
      <Pager next={!!data.next_cursor} back={history.length > 0}
        onNext={() => {
          if (!data.next_cursor) return;
          setHistory(h => [...h, cursor]); setCursor(data.next_cursor);
        }} onBack={() => {
          if (!history.length) return;
          setCursor(history[history.length - 1] ?? null); setHistory(h => h.slice(0, -1));
        }} />
    </>}
  </section>;
}

function ProviderDetail({ id, actor, back, onLost }: {
  id: string; actor: ActorContext; back: () => void; onLost: LostAccess;
}) {
  const [data, setData] = useState<ProviderWorkspaceView | null>(null);
  const [evidenceCursor, setEvidenceCursor] = useState<string | null>(null);
  const [requestCursor, setRequestCursor] = useState<string | null>(null);
  const [revision, setRevision] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(true);

  useEffect(() => {
    const controller = new AbortController();
    setData(null); setError(null); setBusy(true);
    api.providerWorkspace(id, controller.signal, {
      evidenceCursor, requestCursor,
    }).then(next => {
      if (!controller.signal.aborted) setData(next);
    }).catch(e => {
      if (controller.signal.aborted) return;
      if (expired(e)) onLost();
      else setError(errorMessage(e));
    }).finally(() => { if (!controller.signal.aborted) setBusy(false); });
    return () => controller.abort();
  }, [id, evidenceCursor, requestCursor, revision, onLost]);

  return <section>
    <button type="button" className="subtle" onClick={back}>بازگشت به Candidateها</button>
    <Status busy={busy} error={error} />
    {data && <div className="stack">
      <header className="section-title"><div>
        <p className="eyebrow">ثبت اولیه ـ فاقد تصمیم صلاحیت</p>
        <h2>{data.candidate.display_name}</h2>
      </div><span className="chip">Candidate</span></header>
      <p className="disclaimer">مدارک ارائه‌شده و درخواست بررسی، معادل تأیید صلاحیت یا فعال‌سازی ارائه‌دهنده نیستند.</p>
      <ProviderIntake actor={actor} candidateId={id}
        onAuthenticationLost={onLost}
        onSaved={() => {
          setEvidenceCursor(null); setRequestCursor(null);
          setRevision(value => value + 1);
        }}
      />
      <div className="cards two-col">
        <section className="card"><h3>شواهد ارائه‌شده</h3>
          {data.evidence.items.length === 0 && <Empty text="سندی ثبت نشده است." />}
          <ul className="records">{data.evidence.items.map(x => <li key={x.id}>
            <strong>{x.evidence_label}</strong>
            <p className="record-content" dir="auto">{x.evidence_reference}</p>
            <p className="meta">{x.reason} · {formatDate(x.recorded_at)}</p>
          </li>)}</ul>
          <button type="button" disabled={!data.evidence.next_cursor}
            onClick={() => setEvidenceCursor(data.evidence.next_cursor)}>صفحه بعد اسناد</button>
          {evidenceCursor && <button className="subtle" type="button"
            onClick={() => setEvidenceCursor(null)}>شروع اسناد</button>}
        </section>
        <section className="card"><h3>درخواست‌های بررسی</h3>
          {data.review_requests.items.length === 0 && <Empty text="درخواست بررسی ثبت نشده است." />}
          <ul className="records">{data.review_requests.items.map(x => <li key={x.id}>
            <p className="record-content">{x.reason}</p>
            <p className="meta">{formatDate(x.requested_at)} · <bdi>{x.requested_by_actor_id}</bdi></p>
          </li>)}</ul>
          <button type="button" disabled={!data.review_requests.next_cursor}
            onClick={() => setRequestCursor(data.review_requests.next_cursor)}>صفحه بعد درخواست‌ها</button>
          {requestCursor && <button className="subtle" type="button"
            onClick={() => setRequestCursor(null)}>شروع درخواست‌ها</button>}
        </section>
      </div>
    </div>}
  </section>;
}

function ProviderIndex({ actor, onLost }: { actor: ActorContext; onLost: LostAccess }) {
  const [cursor, setCursor] = useState<string | null>(null);
  const [revision, setRevision] = useState(0);
  const [history, setHistory] = useState<(string | null)[]>([]);
  const [data, setData] = useState<Page<ProviderCandidateView> | null>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(true);

  useEffect(() => {
    const controller = new AbortController();
    setBusy(true); setData(null); setError(null);
    if (!canReadProviders(actor)) {
      setBusy(false);
      return () => controller.abort();
    }
    api.providers(cursor, controller.signal).then(next => {
      if (!controller.signal.aborted) setData(next);
    }).catch(e => {
      if (controller.signal.aborted) return;
      if (expired(e)) onLost();
      else setError(errorMessage(e));
    }).finally(() => { if (!controller.signal.aborted) setBusy(false); });
    return () => controller.abort();
  }, [cursor, revision, actor, onLost]);

  if (selected) {
    return canReadProviderWorkspace(actor)
      ? <ProviderDetail id={selected} actor={actor} back={() => setSelected(null)} onLost={onLost} />
      : <section className="card">
        <button type="button" onClick={() => setSelected(null)}>بازگشت</button>
        <Alert>برای مشاهده شواهد و درخواست‌های بررسی باید هر سه مجوز خواندن Provider موجود باشند.</Alert>
      </section>;
  }
  return <section>
    <header className="section-title"><div>
      <p className="eyebrow">ثبت‌های اولیه</p><h2>Provider Candidateها</h2>
    </div></header>
    <p className="disclaimer">فهرست Candidateها هیچ نشانه‌ای از تأیید، ظرفیت یا آمادگی ارائه خدمت نیست.</p>
    <ProviderIntake
      actor={actor}
      candidateId={null}
      onAuthenticationLost={onLost}
      onSaved={newCandidateId => {
        setCursor(null); setHistory([]);
        setRevision(value => value + 1);
        if (newCandidateId && canReadProviderWorkspace(actor)) setSelected(newCandidateId);
      }}
    />
    {!canReadProviders(actor) && <Alert>مجوز مشاهده Candidateها موجود نیست؛ فقط ثبت مجاز است.</Alert>}
    <Status busy={busy} error={error} />
    {data && <>
      {data.items.length === 0 && <Empty text="Candidate قابل مشاهده‌ای در این صفحه وجود ندارد." />}
      <div className="cards">
        {data.items.map(item => <article className="card case-card" key={item.id}>
          <div><h3>{item.display_name}</h3>
            <p className="meta">ثبت: {formatDate(item.registered_at)} · <bdi>{shortId(item.id)}</bdi></p>
          </div>
          <button type="button" disabled={!canReadProviderWorkspace(actor)}
            onClick={() => setSelected(item.id)}>مشاهده مدارک و درخواست‌ها</button>
        </article>)}
      </div>
      <Pager next={!!data.next_cursor} back={history.length > 0}
        onNext={() => {
          if (!data.next_cursor) return;
          setHistory(h => [...h, cursor]); setCursor(data.next_cursor);
        }} onBack={() => {
          if (!history.length) return;
          setCursor(history[history.length - 1] ?? null); setHistory(h => h.slice(0, -1));
        }} />
    </>}
  </section>;
}

function OperationalShell({ actor, onLost }: {
  actor: ActorContext; onLost: LostAccess;
}) {
  const cases = canReadCases(actor) || mayManageCases(actor);
  const providers = canReadProviders(actor) || canRecordProvider(actor, "candidate");
  const [tab, setTab] = useState<"cases" | "providers">(cases ? "cases" : "providers");
  return <div className="app-shell">
    <aside className="sidebar">
      <div className="brand"><div className="brand-mark" aria-hidden="true">ن</div>
        <div><strong>نسیم</strong><span>نظام سالمندیاری محله‌محور</span></div>
      </div>
      <p className="nav-label">محیط‌های خواندنی</p>
      <nav aria-label="بخش‌های عملیاتی" className="nav">
        {cases && <button type="button" className={tab === "cases" ? "active" : ""}
          aria-current={tab === "cases" ? "page" : undefined} onClick={() => setTab("cases")}>
          پرونده‌ها و تخصیص‌ها
        </button>}
        {providers && <button type="button" className={tab === "providers" ? "active" : ""}
          aria-current={tab === "providers" ? "page" : undefined} onClick={() => setTab("providers")}>
          ثبت‌ها و مدارک Provider
        </button>}
      </nav>
      <p className="sidebar-note">تغییر وضعیت رسمی، انتخاب Provider و نتیجه خدمت در این محیط فعال نیست.</p>
    </aside>
    <main className="content">
      <header className="topbar">
        <div><p className="eyebrow">محیط عملیاتی · ثبت انسانی و مشاهده مجاز</p>
          <h1>{tab === "cases" ? "پرونده‌ها و پیگیری‌ها" : "بررسی مقدماتی Provider"}</h1></div>
        <div className="identity" title="هویت برگرفته از API تأییدشده">
          <span>کاربر تأییدشده</span><bdi>{actor.actor_id}</bdi>
        </div>
      </header>
      {!cases && !providers && <Alert>برای دسترسی به هیچ‌یک از محیط‌های خواندنی مجوز صریح وجود ندارد.</Alert>}
      {tab === "cases" && cases && <CaseIndex actor={actor} onLost={onLost} />}
      {tab === "providers" && providers && <ProviderIndex actor={actor} onLost={onLost} />}
      <footer>ثبت‌های مجاز انسانی و مشاهده سوابق واقعی؛ بدون تفسیر خودکار یا تأیید خدمت · طراحی نهایی Figma بعداً تعیین می‌شود</footer>
    </main>
  </div>;
}

export default function App() {
  const [actor, setActor] = useState<ActorContext | null>(null);
  const [state, setState] = useState<"loading" | "ready" | "blocked" | "unavailable">("loading");
  const onLost: LostAccess = () => { setActor(null); setState("blocked"); };

  useEffect(() => {
    const controller = new AbortController();
    api.self(controller.signal).then(value => {
      if (controller.signal.aborted) return;
      // Server is the authority; no local role-to-capability inference.
      if (value.actor_type === "AI") { setState("blocked"); return; }
      setActor(value); setState("ready");
    }).catch(e => {
      if (controller.signal.aborted) return;
      setState(expired(e) ? "blocked" : "unavailable");
    });
    return () => controller.abort();
  }, []);
  if (state !== "ready" || !actor) {
    return <main className="gate" dir="rtl">
      <div className="gate-card">
        <div className="brand"><div className="brand-mark">ن</div><div><strong>نسیم</strong><span>محیط عملیاتی</span></div></div>
        <h1>{state === "loading" ? "در حال بررسی دسترسی" : state === "blocked"
          ? "دسترسی تأیید نشده است" : "سرویس در دسترس نیست"}</h1>
        <p>{state === "loading" ? "هویت و مجوزها از سرویس واقعی دریافت می‌شوند."
          : state === "blocked"
            ? "هیچ ورود آزمایشی یا مسیر دورزدن احراز هویت وجود ندارد. اتصال هویت سازمانیِ تأییدشده ضروری است."
            : "ارتباط با سرویس واقعی برقرار نشد. داده نمایشی یا اطلاعات ذخیره‌شده جایگزین نخواهد شد."}</p>
        {state !== "loading" && <button type="button" onClick={() => window.location.reload()}>
          تلاش مجدد
        </button>}
      </div>
    </main>;
  }
  return <OperationalShell actor={actor} onLost={onLost} />;
}
