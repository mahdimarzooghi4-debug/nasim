# DC-017 — Internal AI Day-one Bounded Use Case & Data Governance Decision Packet

- **Status:** DRAFT / PARTIAL BUSINESS CLOSURE — D-0135 THROUGH D-0146 CONDITIONAL CEO AUTHORITY SOURCE ACCEPTED; actual delegation, operational role, source evidence and learning policies OPEN
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

## 2.7 Accepted bounded source-failure response — D-0142

The Product Owner expressly accepted the **entire four-part informational-assistant fail-safe policy**: when content required to answer lacks a valid, current, published and audience-permitted official source, or relevant sources are expired, invalid or conflicting, the assistant must (1) avoid definitive, speculative or fabricated official answers; (2) clearly explain lack of verified content or a conflict, without disclosing inaccessible internal source details; (3) direct the user toward appropriate human follow-up; and (4) withhold the invalid/stale/conflicting information as an official answer until duly resolved.

The actual human destination/channel, publication-version validation method, exact response text, human escalation ownership/recording, source conflict resolution, and incident handling remain **OPEN**. This is a Business policy for D-0135, elaborating D-0034; it is not a technical implementation, does not seed permissions and does not grant access to protected personal or internal content.

## 2.8 Elder's first human follow-up contact — D-0143 Accepted

The Product Owner explicitly approved **the assigned caregiver for the same elder (سالمندیار مسئول همان سالمند)** as the **first human follow-up function** when the elder-facing informational assistant cannot provide a safe answer under D-0142. This is an **elder-only** Business responsibility boundary.

This does **not** establish that an assigned caregiver actually exists for a given elder, nor authorize the AI to access case assignment data or personal contact details. Case assignment provenance, consent/legal basis, verification of the actual responsible caregiver, and the eventual user-facing communication channel remain independently gated. In the absence/unavailability of a verifiably assigned caregiver, no fallback owner, message route, default Operations Manager or next authority is inferred.

**Still OPEN:** the actual elder-to-caregiver contact/queue/notification and audit contract, response deadline, who handles unanswered follow-up or tasks beyond caregiver authority, urgency/emergency escalation, and the **first human destination for caregiver-facing AI users**. D-0143 does not authorize caregiver decisions beyond established scope and cannot affect official records, referrals, clinical care or AI training.

## 2.9 Conditional fallback when the elder's assigned caregiver is absent/unavailable — D-0144

The Product Owner explicitly selected the **Nasim response/support function (مسئول پاسخ‌گویی یا پشتیبانی نسیم)** as the first fallback **only after this organizational function has been formally defined and its authority validly assigned**. This applies when an elder-facing AI user needs human follow-up under D-0142 but no assigned caregiver exists or that caregiver cannot be reached (D-0143).

**This support role is a future Business function, not an existing verified operational role or technical permission.** Its responsibility limits, appointing authority, accountable individual/unit, training, actual communication channel and access rights remain OPEN. Until the function is formally defined, assigned and reachable, the fallback cannot be represented as operationally available; any further interim/manual fallback remains OPEN. AI cannot invent a support person, number, contact mechanism, SLA, handoff receipt or case access.

Caregiver-side AI human follow-up, more senior/urgent escalation, actual source validity, privacy/consent, incident ownership and Training Eligibility are independent unresolved decisions. No clinical/emergency/Provider/financial decision rights are created.

## 2.10 Conditional support-role definition/approval owner — D-0145

The Product Owner **conditionally accepted** **مدیر عملیات نسیم (Nasim Operations Manager)** as the Business authority intended to **define and approve the future Nasim response/support officer function** named in D-0144, **only insofar as the Operations Manager possesses valid organizational authorization to do so**.

**The organizational authorization has NOT been established.** This decision neither certifies that an appointing authority exists nor identifies its issuer, instrument, delegation boundary, accountable human occupant or effective period. The exact formal authority source and proof are still OPEN. Until confirmed, the designation must not be converted into an established approval right.

**Separation:** selecting an intended Business approval owner ≠ ratifying legal/organizational competence ≠ adopting a role contract ≠ appointing support staff ≠ granting technical permissions ≠ operating the elder fallback service. The support function, any interim fallback when no caregiver is available, channels and SLAs remain OPEN. No role, backend permission, deployment or AI case access arises from this document.

**Next narrowly triggered question:** which real organizational person/body grants the Operations Manager authority to define and approve this support function, and what actual source of authority is applicable? Do not assume executive/board approval without Product Owner evidence.

## 2.11 Conditional authority source for establishing the future support function — D-0146

The Product Owner named the **Nasim CEO (مدیرعامل نسیم)** as the intended organizational issuer of authority for the **Nasim Operations Manager** to formally define and approve the future Nasim support/response function. This is **conditional on the CEO actually possessing such authority under Nasim's real organizational/legal framework**.

**Not proven or activated:** CEO identity/appointment, governing charter/resolution, authority to delegate, actual documented delegation to Operations Manager, role establishment, staffing, technical grants or contact availability. Until separately evidenced, the D-0144 support function remains a **future fallback, not an available service**.

**Important scope isolation:** this CEO authority direction is for the future **support function only**; it must **not** be generalized to Provider Qualification, provider Approval/Activation, medical review or any other appointment power. In particular, PR #9's QD-02 issuer remains independent and OPEN.

### Decision-efficiency guidance accepted with this user feedback

The Product Owner requested an end to low-value serial micro-questions. Proceed with **bounded evidence-based decision packages** from existing Accepted rules under D-0118/D-0124, maintain an OPEN/DEFERRED/ACCEPTED register and bring questions back only where actual material Business alternatives or real legal/institutional/external facts cannot be inferred. This is delivery interaction guidance, **not authorization to invent an authority, technical contract, personal-data use, Provider policy or runtime capability**.

## 3. Smallest context-triggered Product Owner decisions

| Ref | OPEN decision | Minimum decision evidence | Why it blocks implementation |
|---|---|---|---|
| AI-D1 | **PARTIALLY RESOLVED** — first informational use case for **elder and caregiver** (D-0135) | Selection and read-only boundaries accepted; additional use cases, actual publication sources and operational support remain OPEN | D-0004/D-0005 mandate both audiences; D-0135 selects only the first bounded use case, not the full eventual scope |
| AI-D2 | Official **content** source — **PARTIALLY RESOLVED (D-0136…D-0141)** | **مدیر عملیات نسیم** owns collection/import (D-0139), audience-level classification and reclassification (D-0141), and independently approval/publication (D-0136); two levels accepted under D-0140. Still OPEN: actual source documents/issuers/versions and validity, independent legal/specialist checks where needed, actor grants, specific audience access controls, audit/revocation and stale/withdrawn behavior. | The Business classifier does not gain authority to disclose legally restricted content, and the labels do not constitute technical access grants or Training Eligibility. |
| AI-D3 | Human Follow-up / Review — **PARTIALLY RESOLVED (D-0143…D-0146)** | Assigned caregiver first for elder (D-0143); future support fallback once real role/authority exists (D-0144). Operations Manager is intended role-definition approver (D-0145), with CEO as intended authority issuer (D-0146), **both conditioned on actual lawful/institutional appointment and delegation evidence**. OPEN: actual proof/grant, supported role and person, interim path, contacts/SLA, caregiver-facing route and all per-actor access permissions. | Naming CEO as a source is not proof of charter authority or a completed delegation, nor actual support staffing, Case access or operational handoff. |
| AI-D4 | Runtime data-access + legal purpose | Allowed and prohibited data classes for each audience, identity/consent/legal basis, minimal context, audit and retention basis | Operational access ≠ AI Runtime Access ≠ Training Eligibility |
| AI-D5 | Fail-safe / disclosure / incident ownership — **PARTIALLY RESOLVED (D-0142…D-0144)** | D-0142 prohibits unsupported official answers; D-0143 selects the elder's assigned caregiver as first follow-up; D-0144 selects **future formally defined and authorized Nasim support** as fallback if caregiver absent/unavailable. OPEN: actual contact and interim handling before that role exists, no-answer processing, caregiver-side escalation, human routing, incident/privacy/urgency and real source validation. | A conditional future Business role is NOT a deployable or currently reachable escalation destination. |
| AI-D6 | Day-one automatic **Dataset** source policy | Exact eligible source data/event classes, exclusions, source-of-truth, de-identification/purpose/consent, verification, revision/withdrawal effect, eligible-signal owner and versioning | D-0005 does not permit arbitrary new Production data to become training data |
| AI-D7 | Training, evaluation and release governance | Training/validation/evaluation dataset isolation, evaluation evidence, approver authority, rollback, versions and production promotion process (no thresholds invented) | Model readiness and governed release cannot be assumed from technical completion |
| AI-D8 | Operational quality and user safety | Applicable linguistic/accessibility requirements for elderly users, user-facing transparency, human handoff, specific prohibited advice and risk ownership | Needs real user-specific and human/organizational decisions, not guessed UI or clinical policies |

**AI-D1 selection is ACCEPTED under D-0135; AI-D2 source/publisher/audience responsibilities under D-0136…D-0141; fail-safe under D-0142; elder first contact under D-0143; conditional fallback under D-0144; conditional Operations Manager role-definition/approval responsibility under D-0145; and CEO as intended issuer of that authority under D-0146, without assuming actual delegation or charter power.** Real documents, confirmed staffing/authority, interim route, actual channels and grants, caregiver-side destination and Training Eligibility remain OPEN. Actual documents, classification authority, access grants, workflow and Training Eligibility remain OPEN. Actual content/versions and remaining AI-D1…AI-D8 requirements remain OPEN. D-0031…D-0035 accept safeguards without filling in owners, policies or criteria. AI-D labels are packet references, not implementation states.

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

1. The first informational AI-D1 use case for **both** audiences is already selected under D-0135. **D-0139 closes import-owner responsibility:** the Operations Manager owns collection/import and separately formal publication. D-0140 now defines two Business audience levels. D-0141 now designates the Operations Manager to classify/reclassify each document. D-0142 now defines the safe Business response when source content is missing/stale/conflicting. D-0143 identifies the elder's assigned caregiver as first human follow-up. D-0144 now chooses a **conditional future** Nasim response/support function as fallback if the assigned elder caregiver is absent/unavailable; and D-0145 conditionally designates the Operations Manager to define/approve that role **only after independently evidenced formal authority**. The support role itself, formal authority **proof/grant**, interim route and caregiver-facing AI human contact remain OPEN. Actual channels and issuer/version evidence also remain OPEN. Do not treat draft Business packets as published services.
2. Close AI-D3…AI-D5 for the selected use case before authorizing any user-facing AI contract or data access.
3. Independently determine AI-D6 (training-eligible data classes, purpose/consent, curation and versioning). Until then, do **not** implement a permissive Dataset Builder or pretend a no-data shell satisfies Day-one learning.
4. Design Training/Evaluation/Model Governance only after AI-D6 and relevant AI-D7 decisions, without picking metrics/thresholds by guess.
5. Only after the minimal required Business closure: `Slice Gate → Technical → Product Backlog → Sprint → Code → Code Review → exact-HEAD CI`.
6. Independently continue Provider DC-016; unresolved formal institutional authority does not give AI any additional authority.

## 6.1 Consolidated no-micro-question readiness package — DC-018

The documentation-only integrated preparation and blocker matrix now lives in [DC-018 — AI Day-one Integrated Pre-Technical Readiness](DC-018_AI_DAY_ONE_INTEGRATED_PRE_TECHNICAL_READINESS.md). It consolidates D-0135…D-0146 into implementation-neutral content evidence, publication/classification, human continuity, Runtime safety and automatic Dataset governance packages. It specifies **candidate** tests and grouped B1–B5 source/authority/legal/eligibility blockers, **not** new Accepted Business decisions or entry into Technical/Code.

Per the Product Owner's request, carry forward all independently justified preparation in larger work packages; do not ask repetitive micro-questions. Keep actual documents, proven organizational authority, legitimate access, training eligibility and model deployment decisions OPEN until real evidence is supplied. DC-018 does not bypass any process gate.

## 7. Stage boundary and exit

**Result now: PARTIAL BUSINESS DECISIONS ACCEPTED (D-0031…D-0035, D-0135); AI TECHNICAL ENTRY NOT AUTHORIZED.**

No code, model choice, dataset approval, runtime, role grant, SG/T/Backlog/Sprint, Stage Admission, Stage-based QA, Release or Production is authorized by this packet. D-0130 remains: Hosted Stage is **UNAVAILABLE**. CI's disposable container smoke is not Hosted Stage.

**Next work package (without another micro-question):** prepare a concise Business authority-evidence checklist for D-0145/D-0146, group the support-role contract and caregiver-side human fallback gaps, and separately prioritize real published source and data/AI governance prerequisites. CEO authority evidence and actual delegation remain OPEN until the relevant real organizational documentation exists. Do not ask repetitive micro-questions, and do not advance SG/Technical/Code on guessed authority, content or Training Eligibility.
