# DC-017 — Internal AI Day-one Bounded Use Case & Data Governance Decision Packet

- **Status:** DRAFT / DECISION INPUT — ALL NEW USE-CASE AND POLICY QUESTIONS OPEN
- **Project:** نسیم — نظام سالمند‌یاری محله‌محور
- **Stage:** Business / context-triggered decision preparation
- **Prepared:** 2026-10-08
- **Official context:** `docs/DECISIONS.md` D-0004 (Nasim-owned internal AI assistant for elder and caregiver), D-0005 (Day-one AI and automatic versioned dataset lifecycle from **eligible** operational data), D-0014/D-0015 (system not an independent human decision-maker; actor provenance), D-0021/D-0028 (purpose-limited data, provenance), D-0118 (just-in-time closure), D-0124 (bounded acceleration with no invented institutional/technical facts), D-0130 (Hosted Stage UNAVAILABLE).
- **Existing source packets:** `DC-005_LEGAL_CONSENT_DATA_ACCESS_TRAINING_ELIGIBILITY_PACKET.md`, `DC-006_AI_DAY1_HUMAN_OVERSIGHT_MODEL_GOVERNANCE_PACKET.md`, `BC-004_INTERNAL_AI_ASSISTANT.md`, `BC-006_AI_USE_CASES_HUMAN_OVERSIGHT_LEARNING.md`, `BR-004_CONTEXTUAL_OPEN_DECISION_REGISTER.md`.
- **Purpose:** Choose the smallest **real**, non-consequential first AI interaction and make its necessary business/data prerequisites explicit. This **does not** authorize an AI runtime, select any model, or satisfy the full D-0005 Day-one dataset obligation by itself.

> This is a **new draft decision input** under the existing DC-006 intent, not an Accepted Decision and not a replacement for DC-006. `OPEN ≠ DEFERRED ≠ ACCEPTED`. No SG/T/PB/Sprint/Code is authorized.

## 1. Accepted direction versus decisions still missing

**Accepted:** Nasim must have an internal AI assistant for both elders and caregivers from the first operational day. The dataset lifecycle must automatically create/update *versioned datasets* from eligible new operational data. Training success does **not** automatically promote a model to Production. AI/System authority is not inferred from execution or actor type.

**Not yet Accepted:** specific elder/caregiver use cases, content sources, permitted runtime data classes, consent/legal-basis paths, Training Eligibility rules/owners, reviewer/approver authority, output constraints, evaluation standards, failure handling, model family, training method, deployment topology, hardware, retention periods or thresholds.

A **successful AI demo is not an operational Day-one capability**. A Dataset Builder with no approved eligible data rule is not evidence of authorized training data. Full Day-one readiness needs independently justified runtime, governance and learning capabilities.

## 2. Recommended minimal candidate use case — NOT APPROVED

**Candidate AI-U01 — Read-only guidance on approved Nasim services and operating processes.**

The **same bounded informational capability** could be exposed to the two D-0004 target audiences without granting access to elder case data by default:

| Audience | Candidate assistance | Required authoritative source | Explicit exclusions |
|---|---|---|---|
| Elder | Explain **already approved** Nasim services, basic process steps and where/how to request human help, in clear language | Explicitly published and versioned approved service/process guidance, with actual owner and publication approval | No medical/clinical instruction, elder-specific case status, automatic referral, eligibility, Provider recommendation/selection, or official record change |
| Caregiver | Find/explain **approved** operational guidance and service descriptions to support human work | Approved and versioned staff-facing procedure/catalog material permitted for that caregiver | No access to case/protected records by default; no assignment/qualification/provider decision; no write-back, autonomous case update or service commitment |

The candidate is intentionally smaller than the DC-006 proposals involving real case summaries, personal reminder schedules, Need interpretation or Referral suggestions. Those depend on decisions not currently closed. **Nothing here assumes that approved catalog content, a real UI, a retrieval design, or an AI runtime currently exists.** If approved source content is missing or unavailable, an AI answer may not fabricate it.

**Candidate rejection alternative:** choose a different first use case from DC-006, but document its exact user, purpose, allowed data, human owner, risk and evidence requirements before opening its Technical Gate.

## 3. Smallest context-triggered Product Owner decisions

| Ref | OPEN decision | Minimum decision evidence | Why it blocks implementation |
|---|---|---|---|
| AI-D1 | Initial **elder** and **caregiver** use cases | Explicit selection, user intent, allowed operations and excluded actions for each audience | D-0004/D-0005 mandate both audiences, not specific behaviors |
| AI-D2 | Authoritative **content** source | Which service/process publications are approved and versioned, who may authorize publication/change, what happens if a source is missing/stale | AI may not invent service rules, Provider eligibility or official operational instructions |
| AI-D3 | Accountable Human Owner / review boundary | Who owns each use case, how users reach a human, which AI outputs (if any) require explicit review; escalation when unsuitable/incomplete | A job title or ActorType cannot grant authority; AI Output ≠ Official Record |
| AI-D4 | Runtime data-access + legal purpose | Allowed and prohibited data classes for each audience, identity/consent/legal basis, minimal context, audit and retention basis | Operational access ≠ AI Runtime Access ≠ Training Eligibility |
| AI-D5 | Fail-safe / disclosure / incident ownership | Exact safe responses when source unavailable/contradictory, model absent, privacy authorization denied, or user requests consequential action | No plausible fabricated answer, implicit clinical guidance or business action |
| AI-D6 | Day-one automatic **Dataset** source policy | Exact eligible source data/event classes, exclusions, source-of-truth, de-identification/purpose/consent, verification, revision/withdrawal effect, eligible-signal owner and versioning | D-0005 does not permit arbitrary new Production data to become training data |
| AI-D7 | Training, evaluation and release governance | Training/validation/evaluation dataset isolation, evaluation evidence, approver authority, rollback, versions and production promotion process (no thresholds invented) | Model readiness and governed release cannot be assumed from technical completion |
| AI-D8 | Operational quality and user safety | Applicable linguistic/accessibility requirements for elderly users, user-facing transparency, human handoff, specific prohibited advice and risk ownership | Needs real user-specific and human/organizational decisions, not guessed UI or clinical policies |

**Every AI-D1…AI-D8 remains OPEN**. These are packet identifiers, not technical enums, permission names, official decision numbers or Accepted policy.

## 4. Separation between data-to-dataset and model lifecycle

`Operational source data → explicit eligibility/purpose/consent & quality policy → verified/curated eligible data → automatic versioned Dataset`

is distinct from:

`Versioned Dataset → Training → independent Evaluation → Candidate → explicit authorized human promotion / rollback → Production Model`.

Minimum governance proposals for evaluation (not yet accepted as implementation rules):

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

1. Product Owner first selects the minimum AI-D1 use cases for **both** audiences and approved information sources (AI-D2). If this informational candidate is not suitable, modify or reject it.
2. Close AI-D3…AI-D5 for the selected use case before authorizing any user-facing AI contract or data access.
3. Independently determine AI-D6 (training-eligible data classes, purpose/consent, curation and versioning). Until then, do **not** implement a permissive Dataset Builder or pretend a no-data shell satisfies Day-one learning.
4. Design Training/Evaluation/Model Governance only after AI-D6 and relevant AI-D7 decisions, without picking metrics/thresholds by guess.
5. Only after the minimal required Business closure: `Slice Gate → Technical → Product Backlog → Sprint → Code → Code Review → exact-HEAD CI`.
6. Independently continue Provider DC-016; unresolved formal institutional authority does not give AI any additional authority.

## 7. Stage boundary and exit

**Result now: BUSINESS DRAFT PREPARED; AI TECHNICAL ENTRY NOT AUTHORIZED.**

No code, model choice, dataset approval, runtime, role grant, SG/T/Backlog/Sprint, Stage Admission, Stage-based QA, Release or Production is authorized by this packet. D-0130 remains: Hosted Stage is **UNAVAILABLE**. CI's disposable container smoke is not Hosted Stage.

**Next concrete Product Owner input:** accept/modify/reject the **information-only approved-content guidance** candidate for both audiences, and identify the actual authorized content source/owner. If no source exists, that fact remains a blocker rather than an invitation to fabricate one.
