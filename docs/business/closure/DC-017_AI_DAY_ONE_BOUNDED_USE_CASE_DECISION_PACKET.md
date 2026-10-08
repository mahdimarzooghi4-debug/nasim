# DC-017 — Internal AI Day-one Bounded Use Case & Data Governance Decision Packet

- **Status:** DRAFT / PARTIAL BUSINESS CLOSURE — D-0135 FIRST USE CASE AND D-0136 CONTENT PUBLISHER ACCEPTED; actual content, access and learning policies OPEN
- **Project:** نسیم — نظام سالمند‌یاری محله‌محور
- **Stage:** Business / context-triggered decision preparation
- **Prepared:** 2026-10-08
- **Official context:** `docs/DECISIONS.md` D-0004 (Nasim-owned internal AI assistant for elder and caregiver), D-0005 (Day-one AI and automatic versioned dataset lifecycle from **eligible** operational data), D-0014/D-0015 (system not an independent human decision-maker; actor provenance), D-0021/D-0028 (purpose-limited data, provenance), D-0118 (just-in-time closure), D-0124 (bounded acceleration with no invented institutional/technical facts), D-0130 (Hosted Stage UNAVAILABLE).
- **Existing source packets:** `DC-005_LEGAL_CONSENT_DATA_ACCESS_TRAINING_ELIGIBILITY_PACKET.md`, `DC-006_AI_DAY1_HUMAN_OVERSIGHT_MODEL_GOVERNANCE_PACKET.md`, `BC-004_INTERNAL_AI_ASSISTANT.md`, `BC-006_AI_USE_CASES_HUMAN_OVERSIGHT_LEARNING.md`, `BR-004_CONTEXTUAL_OPEN_DECISION_REGISTER.md`.
- **Purpose:** Choose the smallest **real**, non-consequential first AI interaction and make its necessary business/data prerequisites explicit. This **does not** authorize an AI runtime, select any model, or satisfy the full D-0005 Day-one dataset obligation by itself.

> This is a **partially resolved Business packet** under DC-006. The bounded first informational use case has been **ACCEPTED as D-0135**, and AI safety/review/governance principles D-0031…D-0035 were accepted under D-0124 on this branch. Other source, human authority, data, training and evaluation policies remain **OPEN**. This packet itself is not an implementation authorization. `OPEN ≠ DEFERRED ≠ ACCEPTED`.

## 1. Accepted direction versus decisions still missing

**Accepted:** Nasim must have an internal AI assistant for both elders and caregivers from the first operational day. The dataset lifecycle must automatically create/update *versioned datasets* from eligible new operational data. Training success does **not** automatically promote a model to Production. AI/System authority is not inferred from execution or actor type.

**Partially Accepted:** only information-only guidance over actually approved/published Nasim content for elders and caregivers (D-0135), and high-level prohibitions, consequential Human Review, non-automatic model promotion, fail-safe and traceability (D-0031…D-0035). **Still OPEN:** actual content sources, published versions and named/authorized publisher account (Business content approval/publication owner is now مدیر عملیات نسیم under D-0136), any other use cases, permitted runtime/training data classes, consent/legal basis, specific human owner/permission mapping, detailed error handling, evaluation, deployment/model/algorithm/hosting, retention and thresholds.

A **successful AI demo is not an operational Day-one capability**. A Dataset Builder with no approved eligible data rule is not evidence of authorized training data. Full Day-one readiness needs independently justified runtime, governance and learning capabilities.

## 2. Accepted first informational use case — D-0135; actual launch blockers OPEN

**AI-U01 — First bounded approved Business use-case direction: read-only guidance on approved Nasim services and operating processes.** Selection accepted through D-0135; no content dataset or operational permission was approved.

The **same bounded informational capability** is the first selected use case for both D-0004 target audiences; case/Elder data access is not granted by default:

| Audience | Candidate assistance | Required authoritative source | Explicit exclusions |
|---|---|---|---|
| Elder | Explain **already approved** Nasim services, basic process steps and where/how to request human help, in clear language | Explicitly published and versioned approved service/process guidance, with actual owner and publication approval | No medical/clinical instruction, elder-specific case status, automatic referral, eligibility, Provider recommendation/selection, or official record change |
| Caregiver | Find/explain **approved** operational guidance and service descriptions to support human work | Approved and versioned staff-facing procedure/catalog material permitted for that caregiver | No access to case/protected records by default; no assignment/qualification/provider decision; no write-back, autonomous case update or service commitment |

This selected first use case is intentionally smaller than the DC-006 proposals involving real case summaries, personal reminder schedules, Need interpretation or Referral suggestions. Those depend on decisions not currently closed. **Nothing here assumes that approved catalog content, a real UI, a retrieval design, or an AI runtime currently exists.** If approved source content is missing or unavailable, an AI answer may not fabricate it.

**Change control:** a later replacement/extension of the selected first use case requires a separate recorded Business decision; D-0135 does not accept the broader list of candidate abilities in D-0029/D-0030.

## 2.1 Accepted content publication responsibility — D-0136

The Product Owner expressly designated **مدیر عملیات نسیم (Nasim Operations Manager)** as the Business owner responsible for **approval and publication of official Nasim information** used by the D-0135 first AI guidance use case. This resolves the Business **publication responsibility** portion of AI-D2 only. Content must be actually approved/published and permitted for the specific audience before AI can present it as official.

**Unresolved:** whether a real authoritative published corpus exists; location/system/source-of-truth, versioned publication evidence, owner/account appointment and grant mapping, changes/withdrawal, per-audience access, and any independently required legal/clinical/specialist verification. The Operations Manager's content-publishing responsibility neither supplies medical competence nor authorizes AI to give clinical instructions. Publication is not AI Runtime personal-data access or Training Eligibility.

## 3. Smallest context-triggered Product Owner decisions

| Ref | OPEN decision | Minimum decision evidence | Why it blocks implementation |
|---|---|---|---|
| AI-D1 | **PARTIALLY RESOLVED** — first informational use case for **elder and caregiver** (D-0135) | Selection and read-only boundaries accepted; additional use cases, actual publication sources and operational support remain OPEN | D-0004/D-0005 mandate both audiences; D-0135 selects only the first bounded use case, not the full eventual scope |
| AI-D2 | Authoritative **content** source — **PARTIALLY RESOLVED (D-0136)** | Publication approval owner: **مدیر عملیات نسیم** (ACCEPTED). Still OPEN: real approved/published corpus, exact document/system source and version, named/authorized account, audience-specific permissions, required specialist/legal review, and missing/stale/withdrawn content procedure. | Business publishing responsibility is not a technical permission, proof content exists, a specialist license, or Data/Training access. AI may not invent official service rules or instructions. |
| AI-D3 | Accountable Human Owner / review boundary | Who owns each use case, how users reach a human, which AI outputs (if any) require explicit review; escalation when unsuitable/incomplete | A job title or ActorType cannot grant authority; AI Output ≠ Official Record |
| AI-D4 | Runtime data-access + legal purpose | Allowed and prohibited data classes for each audience, identity/consent/legal basis, minimal context, audit and retention basis | Operational access ≠ AI Runtime Access ≠ Training Eligibility |
| AI-D5 | Fail-safe / disclosure / incident ownership | Exact safe responses when source unavailable/contradictory, model absent, privacy authorization denied, or user requests consequential action | No plausible fabricated answer, implicit clinical guidance or business action |
| AI-D6 | Day-one automatic **Dataset** source policy | Exact eligible source data/event classes, exclusions, source-of-truth, de-identification/purpose/consent, verification, revision/withdrawal effect, eligible-signal owner and versioning | D-0005 does not permit arbitrary new Production data to become training data |
| AI-D7 | Training, evaluation and release governance | Training/validation/evaluation dataset isolation, evaluation evidence, approver authority, rollback, versions and production promotion process (no thresholds invented) | Model readiness and governed release cannot be assumed from technical completion |
| AI-D8 | Operational quality and user safety | Applicable linguistic/accessibility requirements for elderly users, user-facing transparency, human handoff, specific prohibited advice and risk ownership | Needs real user-specific and human/organizational decisions, not guessed UI or clinical policies |

**AI-D1 first-use-case selection is ACCEPTED only to the extent of D-0135, and AI-D2 official content approval/publication responsibility is ACCEPTED only to the extent of D-0136.** Actual content/versions and remaining AI-D1…AI-D8 requirements remain OPEN. D-0031…D-0035 accept safeguards without filling in owners, policies or criteria. AI-D labels are packet references, not implementation states.

## 4. Separation between data-to-dataset and model lifecycle

`Operational source data → explicit eligibility/purpose/consent & quality policy → verified/curated eligible data → automatic versioned Dataset`

is distinct from:

`Versioned Dataset → Training → independent Evaluation → Candidate → explicit authorized human promotion / rollback → Production Model`.

Governance boundaries include accepted D-0031…D-0035 and still-open implementation details; the following items remain design considerations unless expressly covered by those decisions:

- Preserve source, policy and dataset-version lineage, input provenance and correction/supersession history.
- Do not make labels from unverified AI suggestions or Provider free text by default.
- Do not reinterpret historical records silently after a rule/model change.
- Do not infer training permission from operational data visibility.
- Keep Human/System/AI/Automation provenance distinct.
- Do not self-promote or self-authorize a Production model.

**The initial information-only use case is not automatically a Training dataset source.** AI conversations, elder queries and caregiver actions are not eligible training data merely because they occurred.

## 5. Explicit technology non-decisions

This packet selects **no** model family, architecture, training/fine-tuning algorithm, retrieval method, RAG/vector database, model-serving mechanism, vendor, external/in-process inference boundary, embedding technology, hosting, GPU/CPU/RAM, checkpoint, artifact store, endpoint/token, dataset cadence, formula, score or evaluation threshold.

The term **internal AI** has an accepted product meaning; its exact technical deployment and dependency boundary remain unresolved in BC-004 and require a separately governed Technical decision. Choices or technical contracts from other products are not imported into Nasim.

## 6. Suggested parallel work, each still gated

1. The first informational AI-D1 use case for **both** audiences is already selected under D-0135. **Next verify the remaining AI-D2 evidence:** actual published, versioned authoritative content; who is appointed as Operations Manager and the actual publication record, and what happens when content is stale/missing. Do not treat draft Business packets as published services.
2. Close AI-D3…AI-D5 for the selected use case before authorizing any user-facing AI contract or data access.
3. Independently determine AI-D6 (training-eligible data classes, purpose/consent, curation and versioning). Until then, do **not** implement a permissive Dataset Builder or pretend a no-data shell satisfies Day-one learning.
4. Design Training/Evaluation/Model Governance only after AI-D6 and relevant AI-D7 decisions, without picking metrics/thresholds by guess.
5. Only after the minimal required Business closure: `Slice Gate → Technical → Product Backlog → Sprint → Code → Code Review → exact-HEAD CI`.
6. Independently continue Provider DC-016; unresolved formal institutional authority does not give AI any additional authority.

## 7. Stage boundary and exit

**Result now: PARTIAL BUSINESS DECISIONS ACCEPTED (D-0031…D-0035, D-0135); AI TECHNICAL ENTRY NOT AUTHORIZED.**

No code, model choice, dataset approval, runtime, role grant, SG/T/Backlog/Sprint, Stage Admission, Stage-based QA, Release or Production is authorized by this packet. D-0130 remains: Hosted Stage is **UNAVAILABLE**. CI's disposable container smoke is not Hosted Stage.

**Next concrete Product Owner/external evidence input:** identify where the real approved/published service/procedure guidance is stored and how to identify its valid published version (AI-D2); approval and publication responsibility has been accepted as the Operations Manager under D-0136. after that, establish runtime purpose/data access/legal basis and human owner (AI-D3/AI-D4) and separate Training Eligibility for D-0005 (AI-D6). Until then, no SG/Technical/Code or implied dataset authorization.
