# DC-021 — Elder-Originated Request for Human Review: Decision Packet

- **Status:** DRAFT / OPEN decisions — not an accepted Business, API or lifecycle contract
- **Date:** 2026-10-09
- **Purpose:** Link the approved D-0172 elder service + internal AI experience and UX-003 draft/human handoff to the professional caregiver experience, while **not inventing** user identity, commands, statuses, triage rules or provider authority.
- **Scope:** Proposed self-originated elder request for human attention, not authoritative `NEED_CAPTURE`, `Referral`, Order, Payment, Provider booking, Emergency Service or verified Outcome.
- **Basis:** D-0004/0005, D-0170/0171/0172, BC-003/004/005/006/007/014/016/017/018/022, UX-003, TS-03/TS-05.

## A. Verified current repository boundary (not proposed)

1. The Python FastAPI Backend already has a **capability-scoped current-assignment Case index**, `GET /api/v1/cases`, backed by `AssignedCaseIndex`. Its output holds `CaseView`, latest `ProfileView` including `elder_reference`, and `current_assignment`; it contains **no request queue, priority, SLA, elder-facing request lifecycle or inferred status**. Only the already-authorized assigned user/oversight actor can read according to server rules.
2. Server-owned professional HUMAN commands already include:
   - `POST /api/v1/cases/{case_id}/observations` — `record_type=OBSERVATION|NEED_CAPTURE`, explicit `occurred_at`, `content`, `expected_current_assignment_id`. Existing authority: `case.observe.assigned` and validated current caregiver assignment.
   - `POST /api/v1/cases/{case_id}/interactions` — `interaction_type=CONTACT|MONITORING` plus exact assignment and human recording controls.
   - `POST /api/v1/cases/{case_id}/referrals` — requires an already recorded current `NEED_CAPTURE`, with independently authorized descriptive human Referral (NOT Provider dispatch).
   - `POST /api/v1/referrals/{referral_id}/follow-up-records` — separately authorized human note, **not** proven service/Outcome.
3. Write boundaries use server-authoritative identity/permissions, current assignment verification, immutable/auditable records, idempotency keys, re-read after accepted 201, and fail closed on 401/403/409.
4. There is **no verified elder self-service request creation API, case-to-elder identity grant, caregiver request-inbox API, actionable intake lifecycle, notification dispatch or Production AI runtime**. The React operational web interface is Draft; React Native professional mobile is not yet implemented. Figma does not establish these contracts.

## B. Proposed conceptual boundary — decision required

`ELDER EXPRESSION / AI-ASSISTED DRAFT → EXPLICIT ELDER REVIEW AND INTENT → [future authenticated elder-request intake, if approved] → [future authorized human inbox/view] → HUMAN CASE REVIEW → existing authorized HUMAN Need/Referral commands where applicable`

- The self-originated **request** is not the official `NEED_CAPTURE` observation, Referral, service entitlement, case status or confirmed emergency. AI-generated text remains a **draft with provenance**, not human assertion.
- The current Case index is **not** a request queue. Reusing Case records or observations to impersonate elder-submitted tasks is forbidden.
- The owner of review/handoff, whether the elder can submit directly without an active Case/assigned caregiver, and what to do with multi-household/family/caregiver reassignment are **OPEN**. No implicit route, fallback assignee or automatic assignment.
- Who may originate a request must be independently authorized by authoritative source-linked identity. A child acting via family mode is not the elder and not an automatic authorized representative; D-0170 affects only who may pay **if and when purchase flow is separately implemented**.
- The actor who authored a draft, the actual elder confirmer, any family assistant and the human reviewing professional should remain distinct for audit. AI may not masquerade as one of these principals.

## C. Decision matrix — must be explicitly closed BEFORE API or operational UI

| Blocking item | Decisions required | Why it matters |
|---|---|---|
| Elder identity and Case binding | Identity proofing, Case ownership/membership source, multiple Cases, Consent/purpose, revocation | No family/elder data access by guess |
| Intake command eligibility | Who can submit, exactly what the request means, minimum permitted data, source/confirmation, privacy | Avoid creating a new formal Need by accident |
| Data & provenance | User text vs AI suggestions, draft edits, original source, time/model version, minimization, retention | Prevent AI-generated record becoming official silently |
| Review owner | Authorized caregiver or operations role, reassignment and unreachable caregiver, conflict rules | Prevent fabricated queue owner |
| Lifecycle / statuses | Which durable states exist (if any), transition authority, cancellation/change, acknowledgment/visibility | No default `PENDING/ACCEPTED/COMPLETED` vocabulary |
| Handoff delivery | Queue/read API only after source-of-truth, ACLs, deduplication, routing, idempotency, concurrency | No false message-delivered claim |
| Human disposition | Exact actions and review outcome, whether re-recording `NEED_CAPTURE` permitted, correction/audit rules | Enforce current server-owned Case commands |
| Elder status read | Exact read permissions, what status is proven and human-visible, no optimistic success | Avoid exposing or inventing real workflow |
| Safety / escalation | Emergency route, human availability, nonresponse, capacity, contact windows | AI is not an emergency service |
| Security and privacy | 401/403/409, stale assignment and consent, tenant constraints, anti-spam, accessibility, deletion/audit | Fail closed and preserve attribution |
| AI governance | Model availability, contextual data rights, uncertainty, forbidden actions, human approval and provenance | AI assists only, cannot commit a Need or Referral |
| Service/finance boundaries | Catalog, provider qualification/selection, payment and support-organization disclosure | No invented booking, pricing, money or data access |

## D. Candidate UX contract (for design only)

1. Elder can **draft** or revise a human-facing request with optional internal AI assistance, keeping a clear AI-generated label.
2. Before any future submission, present human-readable review, explicit user intent, no medical/financial certainty and verified authority.
3. If a Business-authorized intake command becomes available, the Backend must perform independent permissions, source/case, purpose/consent, stale-state and idempotency checks. The UI must not infer success before a real accepted response.
4. Professional caregiver sees only genuinely authorized, real Backend work items **if a later approved read model exists**, otherwise the UI shows an accurate unavailable/empty state.
5. The caregiver may use existing authorized `RecordObservation/NEED_CAPTURE` after their *own* human verification; this must **not** silently turn an AI draft into a Case record. The professional review outcome for the proposed request awaits an explicit contract.
6. Data for elder and family mobile follow-up must come from separately authorized authoritative read models. No fictional request status or automatic disclosure.
7. In AI unavailability, a separately approved human channel must remain possible. No synthetic AI fallback, case mutation, fake contact delivery or arbitrary emergency promise.

## E. Non-implementation / approval gates

- Do not add an HTTP route, table, enum/status machine, task queue, notification, role grant, backend handler, mobile mutation, service availability, medical triage or purchase action from this packet.
- Business owner/Operations Manager must close the above policy and authority decisions before Technical contract → backlog/Sprint → code/test → Code Review, followed by Stage/QA gates when infrastructure exists.
- D-0130: Hosted Stage remains unavailable. No merge/Ready/Stage/Production without explicit instruction and appropriate independent review.
