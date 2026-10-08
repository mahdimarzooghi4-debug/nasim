# DC-017 — Internal AI Day-one Bounded Use Case & Data Governance Decision Packet

- **Status:** DRAFT / PARTIAL BUSINESS CLOSURE — D-0135 USE CASE THROUGH D-0141 CLASSIFICATION OWNER PARTIALLY ACCEPTED; actual document evidence, role grants and learning policies OPEN
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

## 2.2 Accepted official content source categories — D-0137

The Product Owner accepted exactly **two potential source categories** for the D-0135 informational AI assistant: **(1) existing official documents**, and **(2) new content explicitly approved and published inside Nasim**. Per D-0136, the Nasim Operations Manager is the accountable Business approver and publisher of official content used by this AI use case.

**This is a category choice, not evidence of actual source material.** None of the actual documents, locations, versions, publication records, approval evidence, status, or audience-specific access grants have been provided or authenticated. No existing document or internal draft becomes AI-authoritative merely because it belongs to one of the categories; its approval/publication, current validity and allowed audience must be verified. Specialist/legal subject-matter validity is not replaced by the Operations Manager's Business publication responsibility.

**Minimum remaining source facts to obtain:** provide the location/list of existing official source documents, clarify their issuing authorities and proof of validity, and identify how approved newly created content is actually published and versioned within Nasim. If these sources do not yet exist, retain the missing-source blocker rather than fabricating publications or service policies. This does not give training rights to documents, AI conversations, or personal/operational data.

## 2.3 Existing official documents currently outside Nasim — D-0138

The Product Owner confirmed that **the current holding location of existing official source documents is outside Nasim** and those materials are **intended to be imported into Nasim later**. This is a Business fact and future intention, not a completed import, verified document list, selected storage service, publication record or an approved intake mechanism.

**Current content-source disposition:** existing documents are **not yet in Nasim**. No assumption is made about their precise external location, issuing authority, completeness, validity, current publication status, or ingestion date. No new Nasim-native content repository/import pipeline was authorized by D-0138.

**Must stay separate:** `external document → controlled intake / provenance and authenticity checks → appropriate subject-matter validity verification where required → approval/publication by Operations Manager under D-0136 → permitted audience-specific official source`. This sequence is a *candidate business analysis*, **not** an approved exact state machine, implementation workflow or set of authorized actors. Import alone never confers authority to serve the text as official AI guidance or use it for Training.

**Remaining decisions:** who is accountable for obtaining/importing the external documents, their issuing organizations/sources of truth, acceptance/review evidence, version/change and withdrawal semantics, the audience authorization matrix and handling when content is stale, unavailable or conflicting.

## 2.4 Accepted document-collection/import Business owner — D-0139

The Product Owner explicitly assigned **مدیر عملیات نسیم** (Nasim Operations Manager) as the responsible Business owner for **collecting external official documents and importing them into Nasim**. The same Operations Manager separately owns **approval/publication** of official AI content under D-0136.

**Import is not publication or validation.** An imported document still needs source/validity evidence, applicable specialist/legal review, explicit publication for a permitted audience and appropriate controls before it can be used as official AI guidance. Naming a Business owner does not appoint a technical Actor or grant Role/Permission access.

**OPEN:** actual documents and issuing organizations, source location and authentication, intake and versioning mechanism, actual published versions, named accountable user and permission grants, audience classification, withdrawal/stale-material rules and all Training Eligibility questions.

## 2.5 Accepted two-level content audience boundary — D-0140

The Product Owner explicitly approved **two Business audience levels** for official informational content in the D-0135 Day-one AI use case:

- **عمومی (elder + caregiver audience):** verified, approved and published guidance that may be presented to elders and caregivers.
- **داخلی (authorized staff audience):** verified, approved and published operating procedures to be disclosed **only to an authorized caregiver or other staff actor within their granted scope**. Elder-facing AI may not view or repeat these documents.

The word **public/عمومی** means **permitted for both elder and caregiver audiences within Nasim**. It does **not** itself mean anonymous Internet publication, third-party access or that all users can view all documents. Similarly, staff classification does not grant blanket access to all caregivers/staff. No RBAC permission, authentication method, access-policy implementation, actual content classification or document list is approved by this Business-level distinction.

**Still OPEN:** who classifies/changes the audience level on each document, actual access and identity checks per role/scope, version and publication validity, specialist/legal review where applicable, revocation and stale-source rules, and the AI Runtime/Training eligibility boundaries. Import, publication approval, audience classification and data-purpose permissions are separate governance operations.

## 2.6 Audience-classification owner — D-0141 Accepted

The Product Owner explicitly designated **مدیر عملیات نسیم** as the Business owner for **initial and changed classification** of each approved official content item into the two D-0140 audience levels, **عمومی** (elder/caregiver-permitted in Nasim, not anonymous Internet) and **داخلی** (only caregiver/other staff with separate authorized scope).

This responsibility **does not** waive legal/confidentiality constraints, actual specialist verification, publication approval, actor-level permissions, or source validity. Broadening access to an item with protected content requires its actual legal/professional disclosure conditions to be met; those specifics are **OPEN** and cannot be inferred from the Operations Manager's title or classification label.

Import (D-0139), evidence/validation, audience classification (D-0141), approval/publication (D-0136), and runtime access/training permission remain separate governance steps. No real document has yet been assigned a level, no authorization is seeded, and no publication or AI Runtime is activated by this decision.

**Remaining:** documented real content item list and versions, who verifies applicable legal/specialist access restrictions, authorization for the named manager account and staff users, how changes/reclassification are audited and revoked, safe behavior when a source is invalid, and independent Training Eligibility.

## 3. Smallest context-triggered Product Owner decisions

| Ref | OPEN decision | Minimum decision evidence | Why it blocks implementation |
|---|---|---|---|
| AI-D1 | **PARTIALLY RESOLVED** — first informational use case for **elder and caregiver** (D-0135) | Selection and read-only boundaries accepted; additional use cases, actual publication sources and operational support remain OPEN | D-0004/D-0005 mandate both audiences; D-0135 selects only the first bounded use case, not the full eventual scope |
| AI-D2 | Official **content** source — **PARTIALLY RESOLVED (D-0136…D-0141)** | **مدیر عملیات نسیم** owns collection/import (D-0139), audience-level classification and reclassification (D-0141), and independently approval/publication (D-0136); two levels accepted under D-0140. Still OPEN: actual source documents/issuers/versions and validity, independent legal/specialist checks where needed, actor grants, specific audience access controls, audit/revocation and stale/withdrawn behavior. | The Business classifier does not gain authority to disclose legally restricted content, and the labels do not constitute technical access grants or Training Eligibility. |
| AI-D3 | Accountable Human Owner / review boundary | Who owns each use case, how users reach a human, which AI outputs (if any) require explicit review; escalation when unsuitable/incomplete | A job title or ActorType cannot grant authority; AI Output ≠ Official Record |
| AI-D4 | Runtime data-access + legal purpose | Allowed and prohibited data classes for each audience, identity/consent/legal basis, minimal context, audit and retention basis | Operational access ≠ AI Runtime Access ≠ Training Eligibility |
| AI-D5 | Fail-safe / disclosure / incident ownership | Exact safe responses when source unavailable/contradictory, model absent, privacy authorization denied, or user requests consequential action | No plausible fabricated answer, implicit clinical guidance or business action |
| AI-D6 | Day-one automatic **Dataset** source policy | Exact eligible source data/event classes, exclusions, source-of-truth, de-identification/purpose/consent, verification, revision/withdrawal effect, eligible-signal owner and versioning | D-0005 does not permit arbitrary new Production data to become training data |
| AI-D7 | Training, evaluation and release governance | Training/validation/evaluation dataset isolation, evaluation evidence, approver authority, rollback, versions and production promotion process (no thresholds invented) | Model readiness and governed release cannot be assumed from technical completion |
| AI-D8 | Operational quality and user safety | Applicable linguistic/accessibility requirements for elderly users, user-facing transparency, human handoff, specific prohibited advice and risk ownership | Needs real user-specific and human/organizational decisions, not guessed UI or clinical policies |

**AI-D1 first-use-case selection is ACCEPTED under D-0135. AI-D2 publisher, sources, document import, two audience levels and their Business classification owner are ACCEPTED only to the extent of D-0136…D-0141.** Real content, legal checks, role grants, version/audit and Training Eligibility remain OPEN. Actual documents, classification authority, access grants, workflow and Training Eligibility remain OPEN. Actual content/versions and remaining AI-D1…AI-D8 requirements remain OPEN. D-0031…D-0035 accept safeguards without filling in owners, policies or criteria. AI-D labels are packet references, not implementation states.

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

1. The first informational AI-D1 use case for **both** audiences is already selected under D-0135. **D-0139 closes import-owner responsibility:** the Operations Manager owns collection/import and separately formal publication. D-0140 now defines two Business audience levels. D-0141 now designates the Operations Manager to classify/reclassify each document. Next define the safe response to missing, invalid, stale or contradictory approved source content, and gather issuer/version evidence. Missing/stale-source behavior remains OPEN. Do not treat draft Business packets as published services.
2. Close AI-D3…AI-D5 for the selected use case before authorizing any user-facing AI contract or data access.
3. Independently determine AI-D6 (training-eligible data classes, purpose/consent, curation and versioning). Until then, do **not** implement a permissive Dataset Builder or pretend a no-data shell satisfies Day-one learning.
4. Design Training/Evaluation/Model Governance only after AI-D6 and relevant AI-D7 decisions, without picking metrics/thresholds by guess.
5. Only after the minimal required Business closure: `Slice Gate → Technical → Product Backlog → Sprint → Code → Code Review → exact-HEAD CI`.
6. Independently continue Provider DC-016; unresolved formal institutional authority does not give AI any additional authority.

## 7. Stage boundary and exit

**Result now: PARTIAL BUSINESS DECISIONS ACCEPTED (D-0031…D-0035, D-0135); AI TECHNICAL ENTRY NOT AUTHORIZED.**

No code, model choice, dataset approval, runtime, role grant, SG/T/Backlog/Sprint, Stage Admission, Stage-based QA, Release or Production is authorized by this packet. D-0130 remains: Hosted Stage is **UNAVAILABLE**. CI's disposable container smoke is not Hosted Stage.

**Next Product Owner decision:** determine the safe informational-assistant response when no valid, current, audience-permitted official content exists or sources conflict. Actual documents, issuers, validity and permissions remain unverified; AI Runtime access and Training Eligibility remain separate blockers. Until then, no SG/Technical/Code or inferred Dataset authorization.
