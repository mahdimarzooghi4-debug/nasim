# DC-019 — Nasim AI Source-Use & Training-Eligibility Evidence Matrix

- **Status:** DRAFT / BUSINESS EVIDENCE WORKSHEET — **NOT** an Accepted policy, permission matrix, training dataset, Technical specification or implementation authorization
- **Date:** 2026-10-08
- **Project:** نسیم — نظام سالمندیاری محله‌محور
- **Scope:** The *first* D-0135 read-only informational AI use case for both elders and caregivers, and the **independent** D-0005 continuously updated, versioned Dataset obligation
- **Decision basis:** `docs/DECISIONS.md` D-0004/D-0005, D-0021/D-0028, D-0031…D-0035, D-0121…D-0123, D-0135…D-0147 (D-0147 narrowly defers the **model selection only**)
- **Cross-references:** [BC-007](../contracts/BC-007_DATA_GOVERNANCE_CONSENT_TRAINING_ELIGIBILITY.md), [DC-005](DC-005_LEGAL_CONSENT_DATA_ACCESS_TRAINING_ELIGIBILITY_PACKET.md), [DC-017](DC-017_AI_DAY_ONE_BOUNDED_USE_CASE_DECISION_PACKET.md), [DC-018](DC-018_AI_DAY_ONE_INTEGRATED_PRE_TECHNICAL_READINESS.md)
- **Repository baseline:** `main` `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`; exact-main CI [#95 SUCCESS](https://github.com/mahdimarzooghi4-debug/nasim/actions/runs/37803350724). No implemented AI Runtime, data eligibility pipeline or real published source corpus is asserted by this worksheet.

> **Central distinction:** `source exists ≠ operational authority ≠ AI Runtime reading right ≠ evaluation consent/right ≠ Training Eligibility ≠ Dataset membership ≠ Production model approval`. A candidate source listed here is **not eligible by default**. No synthetic record, organization grant, document validation, person-level consent or Training decision is invented. `OPEN ≠ DEFERRED ≠ ACCEPTED`.

## 1. Concrete source-by-source readiness — not permissions

`NO ACCEPTED GRANT` means that no specific positive authorization has been established **for the queried AI purpose**, not that the user or entire organization is permanently banned from using that source. Permission for one purpose never implies another.

| Actual or candidate source family | Evidence basis / observed implementation scope | Day-one **informational runtime** access | **Training/Dataset** use | Next authoritative evidence |
|---|---|---|---|---|
| **Existing official documents outside Nasim** | Source class accepted D-0137/D-0138, but real documents and import have **not** been evidenced | **OPEN:** only after actual provenance/validity verification, formal publication and requester-specific audience permission | **NO ACCEPTED GRANT:** informational publication never implies training rights | Real file/source register, issuer/current version, rights, classification, Operations Manager's real signed publication record |
| **New official Nasim-published content** | Accepted **potential source class** D-0137; no actual publication evidenced | **OPEN:** only approved/current/audience-permitted published version | **NO ACCEPTED GRANT** | Real content record, creator/issuer, reviewer, version, publication and permitted audience |
| **Elder identity/contact** | Case/Profile foundation exists; data class in D-0122 | **OUT OF FIRST USE CASE** per D-0135; no AI Case/PII grant | **NO ACCEPTED GRANT** | Specific lawful purpose, scope, protections and explicit Training Eligibility decision at a later relevant gate |
| **Case administrative context and caregiver assignment/history** | Operational Case/assignment foundation and D-0121…D-0123 | **OUT OF FIRST USE CASE**; human handoff D-0143 does not authorize AI lookup of assignment | **NO ACCEPTED GRANT** | Distinct runtime/assignment authorization if later proposed; independent class-level eligibility/legal decision |
| **Contacts, monitoring/interaction records** | TS-03 foundation, D-0120/D-0122 | **OUT OF FIRST USE CASE**; no personal case summarization approved | **NO ACCEPTED GRANT** | Versioned source, provenance, lawful purpose, human review, approved per-class rule |
| **Observation / Need capture** | TS-03 foundation; no Outcome/reassessment decision implied | **OUT OF FIRST USE CASE** | **NO ACCEPTED GRANT** | Verified scope and data quality, treatment of corrections, protected attributes, legal purpose and eligibility policy |
| **Referral records** | Sprint 003 bounded referral recording foundation only; no Provider selection/service workflow | **OUT OF FIRST USE CASE** | **NO ACCEPTED GRANT** | Real purpose, referral authority/source, exclusions and eligibility |
| **Provider Candidate / Qualification Evidence / Review Request** | Sprint 004–006 *foundations*; not a Qualification Decision or activation | **OUT OF FIRST USE CASE** | **NO ACCEPTED GRANT** | Independent Provider-governance and legal rights; PR #9 remains Draft; no inference from Candidate, Evidence or Request |
| **Caregiver operational/free-text notes** | Candidate data domain in BC-007; no universal verified record or training label | **OUT OF FIRST USE CASE** | **NO ACCEPTED GRANT**, including any AI-generated or unreviewed free text | Source provenance, lawful basis, verified human correction/review, consent and explicit eligibility |
| **AI prompts, conversations, completions, corrections** | BC-007 draft AI-related domain; does **not** establish storage or consent | **Not a source of official policy**; AI output ≠ official source | **NO ACCEPTED GRANT**; engagement or user feedback does not auto-authorize learning | Actually approved collection/retention, disclosure, provenance, purpose and Data Governance rules |
| **Quality, outcome, service delivery, workforce or reporting data** | BC-007 draft/operational domain candidates; no blanket implementation or validity claim | **OUT OF FIRST USE CASE** | **NO ACCEPTED GRANT** | Actual implemented authoritative producer, versioned label/source, consent/legal basis, and explicit eligibility |
| **Security/access/consent/audit/governance records** | Protected governance data domains | **OUT OF FIRST USE CASE**; not an information guide source | **NO ACCEPTED GRANT** | Independently approved narrowly scoped research/training policy, if ever appropriate |

**Interpretation:** This table distinguishes existing backend **foundations** from an available authoritative dataset. It intentionally contains **zero training-eligible source classes**; D-0005 nonetheless mandates that, *after approval of real eligible data sources*, new policy-qualified operational data must automatically create/update **versioned** datasets. Neither skipping that requirement nor implementing a permissive builder is acceptable.

## 1.1 Code-grounded producer/outbox inventory — verified on `main`

**Purpose:** distinguish the **real backend source/event vocabulary** from candidate training examples. The following facts come from actual repository files at exact `main` SHA `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`, not a deployed environment or evidence that any particular real user record exists. GitHub source links below are SHA-pinned, so later code changes must trigger reinspection.

| Implemented source family | Emitted outbox event names visible in source | Precise audited code | Eligibility/AI implication |
|---|---|---|---|
| Case creation/profile/contact/interaction/observation/assignment | `case.created.v1`, `case.profile_corrected.v1`, `case.contact_recorded.v1`, `case.contact_corrected.v1`, `case.interaction_recorded.v1`, `case.interaction_corrected.v1`, `case.observation_recorded.v1`, `case.observation_corrected.v1`, `case.caregiver_reassigned.v1` | [casework.py, EVENTS lines 54–64](https://github.com/mahdimarzooghi4-debug/nasim/blob/f4bb75f1416e6b2dd83af4a9f835b8f1076316b4/backend/src/nasim/application/casework.py#L54-L64), [Outbox construction lines 170–218](https://github.com/mahdimarzooghi4-debug/nasim/blob/f4bb75f1416e6b2dd83af4a9f835b8f1076316b4/backend/src/nasim/application/casework.py#L170-L218) | These events describe operational mutations, **not** validated Need/Outcome labels, eligibility decisions or AI-ready text. Even `case.observation_recorded.v1` does not prove a reviewed/accepted label. |
| Referral record creation | `referral.recorded.v1` | [referral_effects.py, lines 48–87](https://github.com/mahdimarzooghi4-debug/nasim/blob/f4bb75f1416e6b2dd83af4a9f835b8f1076316b4/backend/src/nasim/infrastructure/referral_effects.py#L48-L87) | **Referral recording only**; not Provider selection, service acceptance/delivery or a positive outcome/training label. |
| Provider candidate registry | `provider.candidate_registered.v1` | [provider_candidate_effects.py, lines 48–85](https://github.com/mahdimarzooghi4-debug/nasim/blob/f4bb75f1416e6b2dd83af4a9f835b8f1076316b4/backend/src/nasim/infrastructure/provider_candidate_effects.py#L48-L85) | Registry **presence only**, not Provider Qualification, Approval or Activation. |
| Provider qualification evidence reference | `provider.qualification_evidence_recorded.v1` | [provider_qualification_evidence_effects.py, lines 47–85](https://github.com/mahdimarzooghi4-debug/nasim/blob/f4bb75f1416e6b2dd83af4a9f835b8f1076316b4/backend/src/nasim/infrastructure/provider_qualification_evidence_effects.py#L47-L85) | Existence of a descriptive evidence record, **not** verification/validity or an approved qualification label. |
| Provider qualification review request | `provider.qualification_review_requested.v1` | [provider_qualification_review_request_effects.py, lines 47–85](https://github.com/mahdimarzooghi4-debug/nasim/blob/f4bb75f1416e6b2dd83af4a9f835b8f1076316b4/backend/src/nasim/infrastructure/provider_qualification_review_request_effects.py#L47-L85) | A **request** for human review; **not** review completion or decision/activation. |

### 1.1.a Outbox shape and data minimization — verified, not a training contract

The Casework Outbox deliberately emits **identifier/provenance-only** payloads: case ID, resource ID, supersedes ID, actor ID/type, timestamp, correlation ID, and for Case creation the profile revision and assignment IDs. The code expressly comments that **contact values and content never leave in events** ([casework.py lines 198–217](https://github.com/mahdimarzooghi4-debug/nasim/blob/f4bb75f1416e6b2dd83af4a9f835b8f1076316b4/backend/src/nasim/application/casework.py#L198-L217)). Referral and Provider events likewise use record IDs, provenance/timing, and linkage rather than automatic AI training records (see exact files above).

The persisted generic Outbox contract has `event_type`, `occurred_at`, `case_id`, JSON `payload` ([models.py lines 230–245](https://github.com/mahdimarzooghi4-debug/nasim/blob/f4bb75f1416e6b2dd83af4a9f835b8f1076316b4/backend/src/nasim/infrastructure/models.py#L230-L245)). **Identifier-only does not mean anonymous or legal-to-train:** actor, case, referral and Provider IDs can still be protected linkage data. Reconstructing text from linked tables for training would require a **separately accepted Training Eligibility + lawful purpose + authorized access policy**, not an implicit Outbox join.

`ActorContext` has Human/System/AI/Automation provenance, but **the existing TS-03 capability guard explicitly rejects AI actors** even if a capability string were present ([identity_context/contracts.py lines 8–32](https://github.com/mahdimarzooghi4-debug/nasim/blob/f4bb75f1416e6b2dd83af4a9f835b8f1076316b4/backend/src/nasim/identity_context/contracts.py#L8-L32)). **Do not bypass this in a proposed assistant or dataset implementation.** D-0135's informational AI also has no default Case/PII access.

The inspected `main` source tree contains **no dedicated AI Runtime, Training Eligibility decision engine, automatic Dataset Builder, Training Run, Evaluation service or Model Registry implementation**. The presence of `outbox_event` and idempotency/audit foundations is a **potential integration foundation, not proof of a delivered learning system**; nor does this inspection prove a message broker/worker is running or has processed any events. Actual runtime, deployment and event-delivery evidence remain unavailable.

### 1.1.b Ordered future evidence steps, without authorizing code

1. Record an approved **purpose- and class-specific policy** naming actual operational source records/events and the required verified label/provenance (if any); do not treat raw `observation_recorded`, `referral.recorded` or Provider Review Request as reviewed Training signals.
2. Independently establish **legal/consent basis**, exclusions, sensitive-ID protection, retention and withdrawal effects; decide whether any data may cross from its operational domain into AI Runtime, Training or Evaluation.
3. Define a **verifiable authorization boundary** for enrichment of identifier-only event references, including source version, actor audit and fail-closed handling of missing or stale records. No direct use of Outbox IDs as AI user-context permissions.
4. Only after Business Slice Gate and its Technical/Backlog/Sprint gates are explicitly passed should implementation of automatic policy-gated **versioned Dataset creation** proceed. D-0005 requires it by first operational day, while no current event class is yet approved as Training-eligible.
5. Keep official-content informational answers, operational-learning datasets, and independent model Evaluation/Promotion as distinct pathways. D-0147 still defers **model choice only**.

**Inspection result:** backend *event producers exist*, but **zero verified training-eligible producer classes, Dataset Versions, actual approved documents, or runtime-model artifacts** have been established. This is a verified code-read and Business provenance review; **not** a CI test run, Stage admission, a code patch or a new Business decision.

## 2. Evidence required before admitting an actual source

The columns below constitute an **evidence collection template**, not a DB schema or permission enum. Record `UNKNOWN / NOT PRESENT` rather than guess.

| Evidence item | Official **answer source** (AI Runtime) | **Training / Evaluation** candidate (separate decision) |
|---|---|---|
| Identity and origin | Actual document/content ID; issuer; trusted source-of-truth location; version; provenance and authenticity evidence | Actual event/record class and producer; immutable source identity and lineage; accepted or reviewed observation where applicable |
| Legal purpose/rights | Authority to publish/serve this version to the specified recipient group; confidentiality restrictions | Separately established lawful purpose, applicable consent/legal basis for **Training** and/or **Evaluation**; training right is not inferred from publication |
| Eligibility and quality | Current valid source, authorized approval/publication, legal/specialist validation if applicable, withdrawn/conflicted/version status | Explicit per-class source and exclusion rules, quality/review requirements, eligibility authority, versioned governing policy |
| Audience and minimum exposure | `عمومی` for elder+caregiver **within permitted Nasim audience** or `داخلی` for individually authorized staff; real access scope | Minimum necessary fields, sensitive-data handling and independently authorized training-purpose scope |
| Revision and withdrawal | Exact applicable published version; reclassification/audit; revocation means no stale official answer | Legal retention/withdrawal/correction impact on future/current dataset versions and lineage, per accepted policy |
| Decision evidence | Responsible authorized Operations Manager plus any legally/specialist required review evidence | Separately approved eligibility policy and accountable legal/governance authority; explicit evaluation data authorization |
| What may run | Only after accepted Business/Technical gates and real subject authorization; informational read only | Only after approved eligible-data policy/technical gates; automatic versioned Dataset creation from eligible *new* operational data, **no auto-promotion** |

No real records are supplied in this packet. In particular, do not populate a fake approved document, invented human approver, source hash, consent timestamp, numerical validity period, model benchmark result or data-retention duration.

## 3. Exact evidence handoff and refusal cases — Business test-design inventory only

1. **Unknown official document:** if the issuer/current validity, publication decision or permitted audience cannot be confirmed, do not treat the document as an AI-usable official answer, even if uploaded.
2. **Reclassified internal item:** an elder (or unauthorized staff user) must not see `داخلی` content or protected internal metadata; no automatic declassification or Internet-public inference from `عمومی`.
3. **Retired/revoked version:** source existence in storage does not authorize continuing to answer from a superseded/withdrawn version. In unresolved cases, follow D-0142.
4. **Conflicting source versions:** no definitive official answer; truthful uncertainty and only an actually supported human follow-up path.
5. **Caregiver absent:** D-0143 cannot be used to expose unverified caregiver identity or create a Case relationship. D-0144 support is conditional, not a working channel.
6. **Operational field proposed for training:** reject automatic eligibility when no approved purpose, lawful basis, data-class rule or exclusions have been established; source existence is insufficient.
7. **AI chat proposed as training label:** a chat or model output, even if useful, is not automatically a verified observation or training-eligible label.
8. **Policy changed/withdrawal received:** preserve provenance; the effect on previous Dataset versions is **OPEN** until a real accepted rule exists. Do not silently rewrite history or claim automatic retroactive deletion.
9. **Evaluation says better:** the winning model and Production promotion are not automatically decided (D-0033/D-0147).
10. **No model has been selected:** do not claim model-based Day-one operational readiness or pretend a dummy/manual substitute satisfies D-0004/D-0005.

All ten scenarios are **suggested future acceptance checks, not executed tests**. Numeric metrics, technical state machines, data schemas, retrieval algorithms, model architecture and external integrations remain unselected.

## 4. Bundled real inputs — no low-value serial questions

| Gate group | One-shot evidence package to request when material | If not available |
|---|---|---|
| **Real published sources** | Verified actual source files/issuer, current versions and the Operations Manager's legitimate approval/publication/audience records, plus specialist/legal review where necessary | **OPEN**; continue template/scenario work; no AI answer-source activation |
| **Purpose, identity and permissions** | Actor authentication/Role grants; legally supportable runtime purpose for each audience; particular restricted-data handling | **OPEN**; no inferred access from title or operational presence |
| **Dataset governance** | Actual candidate source/event classes; lawful Training/Evaluation basis; exclusions; quality/curation and provenance; accountable policy owner; correction/withdrawal/retention treatment | **OPEN**; no real Training Eligibility, automatic builder or model training is admitted |
| **Human route and organization** | Verified assigned caregiver contact; actual support-office establishment/authority and channel; caregiver-facing human destination; urgent-case policy | **OPEN**; D-0142 safe disclosure, without fabricated handoff |
| **Model after evidence** | Comparable lawful/versioned benchmark dataset, human evaluation and real hosting benchmarks when available | **D-0147 narrowly DEFERRED** for exact model selection, not the Day-one AI obligation |

### Resume criteria for a future bounded AI technical slice

Only a **documented subset actually required by that slice** needs a Business decision first, not every future possible source class. However, no approved source or consent may be forged, and AI must not be scoped away from Day-one; the continuous eligible-data versioned Dataset requirement is independently mandatory. On a genuine Slice Gate acceptance: `Business → Technical → Product Backlog → Sprint → Code → Code Review → exact-HEAD CI → Hosted Stage (when provisioned)`.

**Current disposition:** **EVIDENCE MATRIX PREPARED; NO POSITIVE AI RUNTIME OR TRAINING ELIGIBILITY GRANTS; NO AI TECHNICAL ENTRY**. Current `main` green CI is not a model evaluation or Hosted Stage result (D-0130). The user has requested batched real decisions and no repeated micro-questions: ask next only when the relevant source/legal/institutional facts exist or an unavoidable material option changes the product.
