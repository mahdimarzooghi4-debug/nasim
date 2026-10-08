# DC-018 — Nasim Day-one AI: Integrated Business → Technical Readiness Work Package

- **Project:** نسیم — نظام سالمندیاری محله‌محور
- **Status:** **DRAFT / IMPLEMENTATION-NEUTRAL READINESS PACKAGE** — not an Accepted Decision, Slice Gate, Technical Baseline, Backlog or Sprint authorization
- **Prepared:** 2026-10-08
- **PR scope:** [Draft PR #10](https://github.com/mahdimarzooghi4-debug/nasim/pull/10), documentation only
- **Source of binding decisions:** `docs/DECISIONS.md` (D-0004/D-0005, D-0013…D-0015, D-0021/D-0028, D-0031…D-0035, D-0118/D-0124/D-0130, and D-0135…D-0146 on this **unmerged Draft branch**)
- **Reference packets:** `DC-005_LEGAL_CONSENT_DATA_ACCESS_TRAINING_ELIGIBILITY_PACKET.md`, `DC-006_AI_DAY1_HUMAN_OVERSIGHT_MODEL_GOVERNANCE_PACKET.md`, `DC-017_AI_DAY_ONE_BOUNDED_USE_CASE_DECISION_PACKET.md`, `BC-004_INTERNAL_AI_ASSISTANT.md`, `BC-006_AI_USE_CASES_HUMAN_OVERSIGHT_LEARNING.md`
- **Independent readiness reference:** [PR #8 — pre-Stage register](https://github.com/mahdimarzooghi4-debug/nasim/pull/8) (separate Draft branch; **not** included in `main` or this branch)
- **Independent Provider-governance reference:** [PR #9 — DC-016](https://github.com/mahdimarzooghi4-debug/nasim/pull/9) (separate Draft branch; **Provider Qualification authority is not decided by this AI packet**)

> **Disposition:** The selected first informational use case and several safety/authority *Business boundaries* are accepted, **but AI Day-one Technical Entry is NOT READY**. This packet converts existing decisions to consolidated work packages, verification questions and future acceptance-test candidates. It makes **no new Product Owner decisions** and must not turn an OPEN item into ACCEPTED/DEFERRED. `Business → Technical → Scrum/Product Backlog → Sprint → Code → Code Review → Stage → QA/Testing → Release Approval → Production → Monitoring → Improvement` remains mandatory.

## 1. Verified baseline and integrated scope

The last reviewed `main` baseline was `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`, with exact-main CI [#95 SUCCESS](https://github.com/mahdimarzooghi4-debug/nasim/actions/runs/37803350724). This does **not** prove AI exists or Hosted Stage passed: D-0130 states **Hosted Stage UNAVAILABLE**.

| Domain | Accepted Business boundary on Draft PR #10 | Not established |
|---|---|---|
| Day-one audience | Nasim-owned **internal AI** for both **elder and caregiver**, first operational day (D-0004/D-0005) | Implemented/integrated AI Runtime, usable UI, hosting/model/config |
| First AI interaction | Information-only, read-only guidance drawn exclusively from **actually validated, approved, published and audience-permitted** official content (D-0135) | Actual content corpus, deployed data access, additional AI features |
| Official content sources | Existing official documents **currently outside Nasim, intended for later import**, plus newly approved/published content in Nasim (D-0137/D-0138) | Document identities, locations, signatures, issuer/validity proof, real import/publication |
| Content authority | Operations Manager owns collection/import, audience classification/reclassification, approval/publication at the Business level (D-0136/D-0139/D-0141) | Named appointed human, identity/RBAC grants, specialist/legal content sufficiency |
| Audience classes | `عمومی`: approved for elder **and** caregiver inside Nasim, not necessarily anonymous Internet. `داخلی`: authorized caregiver/staff only (D-0140) | Per-document labels and authorization, staff-scope permission, anonymous access |
| Safe source failure | Never guess or state invalid/stale/conflicting material as official; accurately disclose insufficient/conflicting verified information and guide to appropriate human follow-up (D-0142) | Source validity evaluation, response wording, logging, emergency handling |
| Elder human handoff | First follow-up is that elder's **verified assigned caregiver** (D-0143). Future fallback is a **defined, authorized support/response officer** if no caregiver/none available (D-0144) | Actually assigned caregiver/contact, support role, interim fallback, channel/SLA |
| Support authority | Operations Manager is **conditionally** proposed to define/approve the future support role, with CEO as **intended** issuer of that authority only if actual organizational competence is evidenced (D-0145/D-0146) | Real CEO authority, legal/organization documentation, actual delegation/appointment |
| Training data and models | Versioned Dataset creation/update **automatically and continuously** from policy-eligible new operational data on first operational day; independent governed Training/Evaluation and **no model auto-promotion** (D-0005, D-0033) | Which classes/events may train, consent/legal basis, curation, evaluation, Promotion authority, model/technical stack |

**Excluded from the first bounded AI contract until separate acceptance:** clinical guidance, diagnosis, referral/provider selection, case or official record mutation, personal case summary/status, sensitive health processing, unauthorized staff document access, financial action and AI-driven organizational decisions. The larger D-0029/D-0030 candidate lists remain just candidates.

## 2. Consolidated preparation packages — do what is safely possible now

Each row below is an **analysis/drafting work package**, **not** a Technical/Code task or authorization. Packages may be researched in parallel within Business; they must not silently bypass their own entry gates.

| Package | Concrete preparation output | Independent prerequisite or blocker | Readiness |
|---|---|---|---|
| **A — Official Content Inventory & Provenance** | Draft inventory format: document ID/reference, issuing authority, title, actual external source location, version/date, authenticity/validity evidence, access classification, supersession/revocation, publication record and review evidence | **Actual external documents and issuer validity are unknown**; import is not publication | **PREPARATION READY; authoritative corpus OPEN** |
| **B — Content Publication & Audience Boundary** | Draft handoff checklist separating **collection → verification → classification → approval/publication → audience-specific access → withdrawal**; map Operations Manager's bounded responsibilities, and points requiring specialist/legal input | Exact human appointment/grants, publication state contract, documents and restricted categories **OPEN** | **PREPARATION READY; Technical entry NOT READY** |
| **C — Human Continuity for AI** | Decision-linked journey for elder: safe response → **verified assigned caregiver** → conditional support role only after real appointment; a table of unavailable/no-assignment/no-channel and caregiver-facing AI gaps | Support-role organizational authority evidence/appointment, human channels, privacy basis, caregiver-side contact, urgency handling **OPEN** | **PREPARATION READY; automatic/live handoff BLOCKED** |
| **D — AI Runtime Purpose & Fail-safe** | Data-minimization and negative-path matrix: no automatic Case/PII access, no unofficial source, fail closed on missing/stale/disputed/restricted content; keep AI/Human provenance separate | Real audience identity, actual content, authorized runtime purpose/legal basis, human reviewer/incident ownership **OPEN** | **PREPARATION READY; Runtime Technical entry NOT READY** |
| **E — Automatic Dataset Eligibility & Model Governance** | Separate policy-evidence worksheet for candidate eligible operational event classes, exclusions, consent/legal basis, provenance, preparation, approval owner, dataset/version lineage and retraction; distinguish build/evaluation/promotion | **NO accepted Training Eligibility policy**, real data/source/consent/retention or model release authority; no hard-coded model/threshold | **Governance preparation READY; Builder/Trainer/Evaluator NOT AUTHORIZED** |
| **F — Verification & Acceptance Evidence** | Draft source/content, human-continuity, privacy, data-exclusion and model-governance scenario inventory; explicitly label tests as **planned, not run** | No AI implementation; Stage unavailable; future tests depend on approved technical contract | **SCENARIO DRAFTING READY; QA/Stage claims FORBIDDEN** |

### 2.1 Content evidence worksheet (fields only; not verified items)

For every **real** document later presented by Operations Manager, collect: actual source and owner/issuer; file/document identifier; original reference and version/date; evidence of authenticity/current validity; required subject-matter/legal review; **عمومی/داخلی** audience and permitted sub-scope; classification decision and change trace; approval/publication decision and effective/withdrawal status; superseded version lineage; allowed assistant use. Leave unknown fields **UNKNOWN/OPEN**; never fill them with fabricated documents, hashes, dates, sample policies or defaults.

Publication eligibility and AI audience eligibility are **separate**. A document may be present in Nasim but not validated, not published or not authorized for that particular requester. No label grants Case-data access or AI Training rights.

### 2.2 Human follow-up worksheet (business routing, not implementation)

| Situation | Accepted Business direction | Remaining evidence before real handoff |
|---|---|---|
| Elder needs human review; assigned caregiver verified and reachable | That caregiver is first human follow-up (D-0143) | Legitimate lookup/identity authorization and a real channel |
| Elder has no verified assignee or assignee is unreachable | Future Nasim response/support function selected as **conditional** fallback (D-0144) | Formally defined and staffed support role, actual delegated power, channel, privacy grant |
| Support function not defined, not staffed or unreachable | **No operative fallback can be claimed** | Valid temporary operational plan and owner; OPEN |
| Caregiver using AI needs human follow-up | **No accepted destination yet** | Human owner/escalation Business decision; OPEN |
| Urgent, clinical, safety or sensitive issue | AI must not autonomously make a medical/organizational decision | Real authoritative incident/emergency handling and human assignment policy; OPEN |

**Organizational chain** for future support role: CEO is an **intended source of authority**, not proven; Operations Manager's approval power and support-officer appointment are **not evidence-backed yet**. Do not represent either office as an actual configured authorization grant. This chain has **no bearing on Provider Qualification** in PR #9.

### 2.3 Training eligibility worksheet (not an eligibility grant)

For a **proposed** data source/event only, request actual evidence for: originating service/workflow, data class, lawful purpose and use-specific consent/legal basis, minimum fields, exclusions/protected fields, provenance/verification or human review, preparation/de-identification requirements, correction/withdrawal consequences, version/lineage policy, retention/legal limits and accountable policy approval. Do not choose eligibility solely because a field or event exists in Case/Profile, Referral, content, AI chat or Provider activity.

The obligation to automatically produce **versioned** datasets from eligible new operations (D-0005) is **not optional and must not be silently deferred**. Equally, implementing a permissive Dataset Builder before eligible source policies are approved is not permitted. `eligible source → governed automatic Dataset Version` does not mean `Dataset Version → automatic Production Model`.

## 3. Candidate future acceptance scenarios — **not executed or authorized tests**

1. Elder AI request with **valid, actually published, elder-permitted** content produces only an informational answer linked to its verified source/version; it cannot mutate an official record.
2. Elder request whose only matching sources are **داخلی** must not leak their content or protected existence/details.
3. Caregiver request with an internal document but **no approved staff scope** receives no internal content.
4. Missing, expired, withdrawn or mutually conflicting official sources result in **no invented official answer**, clear uncertainty and safe human-follow-up guidance.
5. A newly imported but **unverified/unpublished** official-looking document never becomes authoritative merely by import.
6. Elder human follow-up may identify an **actually verified assigned caregiver** only using separately permitted identity/assignment data; otherwise there is no invented contact or case association.
7. The future support role must not be presented as operational until actual role contract, human assignment, authority and channel exist; otherwise an **OPEN interim fallback** must not be silently replaced.
8. No AI output is automatically a human decision or official Case/Referral/Provider state transition.
9. Dataset candidates with unknown or disallowed purpose/consent/eligibility cannot join an approved Training Dataset; automatic creation applies **only** when actual eligible-data policy permits it.
10. Later correction/withdrawal and model version changes preserve provenance and do not rewrite historical decisions; model Training/Evaluation alone cannot switch Production without explicit authority.

These are **test-design prompts**. Exact expected response text, authorization semantics, training filters, model behaviors, dataset timing and technical APIs **require accepted Business/Technical contracts**.

## 4. Stop/go: the smallest material blockers, batched

| Group | What must arrive before the affected Technical admission | Interim disposition |
|---|---|---|
| **B1 — Actual authoritative content** | Authentic documents or newly approved and published Nasim content, issuer/version and source-of-truth evidence, sufficient for the intended audience | **OPEN**; no source-dependent AI runtime authorized |
| **B2 — Real identity & legal access** | Real publisher/classifier appointments and grants, elder/caregiver authentication/authorization and the legal basis for the **specific** AI Runtime data exposure | **OPEN**; no invented access rights |
| **B3 — Human follow-up & support** | Real channel to assigned caregiver; if fallback is needed, actual organization/CEO delegation evidence, support role definition/appointment/access; caregiver AI owner and interim/urgent handling | **OPEN**; response policy can be documented but live handoff cannot be claimed |
| **B4 — Training and data governance** | Per-data-class/event Training Eligibility and consent/legal basis, exclusions, accountable reviewer, correction/withdrawal/retention rules, independent evaluation and explicit model promotion authority | **OPEN**; no Dataset Builder/Trainer admission |
| **B5 — Day-one implementation and hosting** | Separately approved model/runtime, actual model artifacts/resources, identity/integration/environment inputs and the agreed Phase/Pilot scope | **OPEN**; no selection of LLM, provider, algorithm, GPU, credential or deployment target from this packet |

No item in B1–B5 is declared **DEFERRED** here. Scope-sensitive items may be dealt with by a future **explicit** bounded deferral if lawful and compatible with D-0004/D-0005; a no-AI or no-policy-gated-Dataset Day-one cannot be presented as compliant with those accepted requirements.

## 5. Fast execution sequence without serial micro-questions

**Wave 1 — CURRENTLY ADMISSIBLE (Business documentation only):** preserve D-0135…D-0146 and map them to A–F; prepare the inventory and eligibility evidence worksheets above; consolidate open dependencies into B1–B5; draft traceable negative-path scenarios; coordinate with PR #8's pre-Stage plan and PR #9's independent Provider decisions **without merging their separate branches by implication**.

**Wave 2 — EVIDENCE-TRIGGERED:** when authentic content, organization authority evidence and applicable legal/consent rules become available, resolve only the blockers actually necessary for a **bounded** first AI slice. Record actual decisions in `docs/DECISIONS.md` with source/scope. Do not pretend candidate controls or generic "safe" options are Accepted Business policy.

**Wave 3 — FUTURE GATED DELIVERY:** only after Business Slice Gate passes, author Technical → Product Backlog → Sprint → Code → Code Review → exact-head CI. Handle AI Runtime, Dataset and human handoff as independently gated capabilities. Tests and local/disposable container smoke may precede Hosted Stage but cannot replace it.

**Current result: INTEGRATED BUSINESS READINESS PACKAGE PREPARED; AI TECHNICAL ENTRY NOT YET AUTHORIZED.** No model selected, API/schema/workflow deployed, source file imported, dataset generated, user permission granted, Stage Admission or Production action performed by this document. Further user questions should be reserved for genuine **material** scope, legal, organizational authority or eligibility choices, not routine document-field micro-decisions.
