# BX-015 — Technical Entry Slice Candidate Map & Minimal Decision Sets

- **Status:** ACTIVE TECHNICAL-ENTRY PREPARATION
- **Stage:** Business — Technical Entry Preparation
- **Date:** 2026-10-07
- **Source basis:** BX-014 + BC-025 + BR-004 + D-0118 + BX-002…BX-013
- **Purpose:** تعریف Candidate Technical Sliceهای محدود، نگاشت کوچک‌ترین مجموعه تصمیم‌های Business لازم برای هر Slice، تفکیک Blockerهای مشترک و اختصاصی، و مقایسه Relative Closure Burden؛ بدون انتخاب Slice، بدون Accept کردن D-0006…D-0117 و بدون Architecture Freeze.

> اصل حاکم: Select a bounded slice first; trigger only the decisions that slice truly needs.

## 1. Gate operating rule

مسیر مجاز برای ورود فنی محدود:

`Candidate Slice → Explicit Slice Selection → Minimal Business Decision Closure → Slice Gate Record → Technical Design for that Slice`

و همچنان:

`OPEN ≠ DEFERRED ≠ ACCEPTED`

هیچ Slice در BX-015 انتخاب نشده است.

## 2. Shared blocker classes

این Blockerها ممکن است در بیش از یک Slice ظاهر شوند، ولی فقط زمانی Context Triggered می‌شوند که Slice انتخاب‌شده واقعاً به آنها نیاز داشته باشد.

### SB-1 — Scope
- target population / enrollment boundary
- applicable geography/organization/pilot scope

### SB-2 — Human authority
- owner/reviewer/approver for consequential action
- separation between responsibility and permission

### SB-3 — Data governance
- purpose
- allowed data class
- consent/legal-basis direction
- access/sharing boundary
- provenance

### SB-4 — Versioned policy
- policy owner
- version/effective-date
- activation boundary
- runtime traceability

### SB-5 — Safety / failure behavior
- fail-safe
- exception ownership
- incident/escalation boundary when consequential

### SB-6 — Audit / lineage
- actor/process attribution
- source/version context
- correction/history preservation

## 3. TS-01 — Policy / Configuration Foundation

### Technical intent
Design a generic technical foundation for versioned business policy/configuration without implementing domain-specific rules.

### Minimal Business decisions triggered
- policy lifecycle vocabulary sufficient for Technical contract
- Policy Owner / Approver boundary
- Activation Authority
- minimum Scope model needed by the first implementation
- runtime must use only active/effective policy
- historical policy-version trace requirement

### Candidate decision references
D-0105…D-0110 are directly relevant candidates; D-0113…D-0116 may become relevant depending activation/rollback scope.

### Can remain OPEN
- full precedence model not used by first scope
- broad override matrix
- emergency-change path if not implemented
- all domain-specific policy contents

### Shared blockers
SB-2, SB-4, SB-6.

### Relative closure burden
**LOW–MEDIUM** if first slice supports one bounded policy scope with no overrides.

### Main risk
Creating an abstract Policy Engine before business lifecycle/authority is sufficiently clear.

## 4. TS-02 — Data / Provenance Foundation

### Technical intent
Design the shared representation of source, provenance, correction history and purpose linkage for records.

### Minimal Business decisions triggered
- which first Data Classes enter the slice
- purpose of processing for those classes
- source/provenance requirements
- correction/supersession semantics
- minimum access boundary for those classes
- whether AI runtime or Training can access any of them

### Candidate decision references
D-0021…D-0028 are the primary candidate decision group.

### Can remain OPEN
- unrelated Data Classes
- final retention period if storage lifecycle is not frozen yet
- external-data rules if no external source is in slice
- Training Eligibility for classes excluded from initial learning scope

### Shared blockers
SB-3, SB-4, SB-6; possibly SB-2.

### Relative closure burden
**MEDIUM** because legal/access boundaries become real as soon as personal data is represented.

### Main risk
Turning conceptual data availability into assumed access or training permission.

## 5. TS-03 — Core Case / Journey Foundation

### Technical intent
Design the bounded technical representation of elder Case/Profile, contact, monitoring and basic handoff before full referral/service automation.

### Minimal Business decisions triggered
- Phase-1 enrollment boundary for the selected slice
- minimum Case/Profile information
- case ownership / assignment
- correction/history rule
- minimum journey interactions included
- handling of unreachable elder if represented
- audit/provenance for case actions

### Candidate decision references
D-0006/D-0007 for Phase/Pilot context, D-0011…D-0015 for role/authority, and selected D-0016…D-0020 journey candidates.

### Can remain OPEN
- detailed Referral state machine
- Provider selection
- Service pricing
- Outcome taxonomy
- full Emergency workflow if safety-critical behavior is excluded from this slice

### Shared blockers
SB-1, SB-2, SB-3, SB-6.

### Relative closure burden
**MEDIUM–HIGH**.

### Main risk
Case ownership or entry rules being silently encoded as technical defaults.

## 6. TS-04 — Service Catalog / Need / Referral Foundation

### Technical intent
Design versioned Need, Service Catalog and Referral concepts for the selected service scope.

### Minimal Business decisions triggered
- active Service Catalog subset for the slice
- Need taxonomy subset or minimum vocabulary
- Need-to-Service mapping boundary
- direct vs referral-only boundary
- Referral authorization
- minimum Referral behavior
- Service Completion Evidence direction

### Candidate decision references
D-0008…D-0010 plus relevant D-0016…D-0020.

### Can remain OPEN
- full Pilot catalog
- SLA numbers
- provider ranking
- pricing/settlement
- outcome scoring

### Shared blockers
SB-1, SB-2, SB-3, SB-4, SB-6.

### Relative closure burden
**HIGH**.

### Main risk
Service/Referral workflow forcing premature authority, eligibility and provider decisions.

## 7. TS-05 — Identity / Role / Authorization Foundation

### Technical intent
Design actor identities, organization boundaries and authorization structure for a bounded set of actions.

### Minimal Business decisions triggered
- role inventory for the slice
- actor/organization boundaries
- authority for each consequential action in scope
- family vs authorized-representative boundary if included
- employer/provider access boundary if included
- privileged/audit-required action classes

### Candidate decision references
D-0011…D-0015 plus selected data/access candidates D-0021…D-0028.

### Can remain OPEN
- roles not participating in the selected slice
- future geographic hierarchy permissions
- emergency access if excluded
- permissions for deferred capabilities

### Shared blockers
SB-2, SB-3, SB-6.

### Relative closure burden
**HIGH** because Role ≠ Permission and authority cannot be inferred.

### Main risk
Encoding organization/job titles as permissions before Business authority is explicit.

## 8. TS-06 — Provider Network Foundation

### Technical intent
Design Provider Registry/lifecycle and referral-response boundary without ranking or settlement.

### Minimal Business decisions triggered
- Provider Types used by the selected service slice
- qualification boundary
- activation authority
- Service-to-Provider mapping
- Provider data-access boundary
- response semantics
- Completion Evidence direction
- failure/re-route ownership

### Candidate decision references
D-0036…D-0042.

### Can remain OPEN
- ranking algorithm
- SLA numbers
- financial settlement
- provider types outside the slice
- integration with external provider systems if not required

### Shared blockers
SB-2, SB-3, SB-4, SB-5, SB-6.

### Relative closure burden
**MEDIUM–HIGH**.

### Main risk
Conflating qualification, activation, eligibility and final selection.

## 9. TS-07 — Outcome / Reassessment Foundation

### Technical intent
Design longitudinal Observation, Reassessment and Outcome lineage for a bounded domain.

### Minimal Business decisions triggered
- Observation review/acceptance boundary
- Accepted State authority
- baseline definition for the slice
- Reassessment definition and trigger
- Outcome evidence validity
- Need Resolution boundary if included
- correction/restatement behavior

### Candidate decision references
D-0094…D-0104.

### Can remain OPEN
- broad Outcome taxonomy
- causal impact methodology
- unrelated reassessment instruments
- training-label validation if learning is excluded from first slice

### Shared blockers
SB-2, SB-3, SB-4, SB-6.

### Relative closure burden
**MEDIUM–HIGH**.

### Main risk
Treating service completion, provider result or satisfaction as Outcome.

## 10. TS-08 — Measurement / KPI Foundation

### Technical intent
Design versioned Metric Definition, evidence capture and reporting provenance for a bounded set of measures.

### Minimal Business decisions triggered
- initial KPI/metric catalog for the selected scope
- definition of each captured metric
- evidence sources
- metric owner
- reporting audience/boundary
- versioning/restatement requirement

### Candidate decision references
D-0043…D-0050.

### Can remain OPEN
- numeric targets if not needed for collection
- overall Pilot score
- GO/NO-GO formula
- incentive/ranking formulas

### Shared blockers
SB-3, SB-4, SB-6.

### Relative closure burden
**LOW–MEDIUM** if the slice is limited to evidence capture and versioned metric definitions.

### Main risk
Building dashboards before the metric meaning and evidence contract are defined.

## 11. TS-09 — AI Day-one Foundation

### Technical intent
Design the minimum internal-AI product boundary required by D-0004/D-0005 for a selected Day-one use case.

### Minimal Business decisions triggered
- one or more explicitly active Day-one use cases
- allowed and forbidden actions for those use cases
- Human Owner / Review requirement
- official-record boundary
- AI transparency boundary
- Runtime Data Classes
- fail-safe behavior
- AI incident boundary
- Training Eligibility for any data entering automatic Dataset lifecycle
- minimum evaluation governance before model use

### Candidate decision references
D-0029…D-0035 plus relevant D-0021…D-0028.

### Can remain OPEN
- model family
- algorithm
- training implementation
- unrelated AI use cases
- production promotion details if first Technical slice is pre-production design only, but they must close before Production model lifecycle

### Shared blockers
SB-2, SB-3, SB-4, SB-5, SB-6.

### Relative closure burden
**VERY HIGH** despite being mandatory Day-one product scope.

### Main risk
Using D-0004/D-0005 to infer permissions, data eligibility or autonomous authority that were never accepted.

## 12. TS-10 — Integration Foundation

### Technical intent
Design one explicit external integration contract after the external dependency is selected.

### Minimal Business decisions triggered
- exact partner/system
- business purpose
- mandatory/optional/deferred status for current scope
- direction
- Data Classes
- Source of Truth
- reconciliation
- organization/data-sharing boundary
- failure/fallback business behavior

### Candidate decision references
D-0061…D-0070.

### Can remain OPEN
- unrelated integrations
- Tarannom if not the selected integration
- protocol/API technology
- retry count/timeouts
- external-data training use if explicitly excluded from learning

### Shared blockers
SB-1, SB-3, SB-4, SB-5, SB-6.

### Relative closure burden
**HIGH** because a real external system and contract evidence are required.

### Main risk
Designing an interface before Source of Truth and failure behavior are known.

## 13. Cross-slice dependencies

Key dependency relationships:

- TS-03 Case/Journey commonly depends on TS-02 Data/Provenance and TS-05 Authority.
- TS-04 Service/Referral commonly depends on TS-03, TS-05 and later TS-06.
- TS-06 Provider commonly depends on TS-04 and TS-02.
- TS-07 Outcome commonly depends on TS-03/04 plus TS-02.
- TS-08 Measurement consumes evidence from TS-03/04/06/07 but can build a generic versioned metric foundation independently after metric definitions are chosen.
- TS-09 AI consumes TS-02 data boundaries, TS-05 authority boundaries and TS-13-like policy concepts represented by TS-01.
- TS-10 Integration depends strongly on TS-02 provenance/data governance and TS-01 versioned contract concepts.
- TS-01 Policy/Configuration is cross-cutting and can support all other slices once its own minimum governance decisions are closed.

## 14. Comparative closure-burden view

| Slice | Relative closure burden | Coupling | Earliest-safe-entry potential |
|---|---|---|---|
| TS-01 Policy/Configuration | Low–Medium | Cross-cutting but abstract | High if bounded to one scope/no override |
| TS-08 Measurement/KPI | Low–Medium | Evidence-oriented | High if limited to versioned metric definitions/capture |
| TS-02 Data/Provenance | Medium | Cross-cutting | Medium–High, but legal/access becomes real quickly |
| TS-03 Case/Journey | Medium–High | Foundational domain | Medium |
| TS-06 Provider | Medium–High | Service-dependent | Medium |
| TS-07 Outcome/Reassessment | Medium–High | Journey/data-dependent | Medium |
| TS-04 Service/Need/Referral | High | Authority/provider-heavy | Lower |
| TS-05 Identity/Authorization | High | Authority-heavy | Lower until role/action scope is chosen |
| TS-10 Integration | High | External-evidence dependent | Lower until real dependency selected |
| TS-09 AI Day-one | Very High | Data/authority/governance-heavy | Mandatory eventually, but not lowest closure surface |

این جدول Recommendation برای انتخاب Slice نیست؛ فقط Decision Surface را مقایسه می‌کند.

## 15. Earliest-safe-entry candidates

از نظر **کمترین سطح تصمیم‌گیری لازم**، سه Candidate قابل بررسی برای اولین bounded Technical entry عبارت‌اند از:

1. **TS-01 Policy/Configuration Foundation** — اگر فقط lifecycle/version/effective scope محدود طراحی شود.
2. **TS-08 Measurement/KPI Foundation** — اگر فقط Metric Definition + Evidence Capture بدون target/gate automation طراحی شود.
3. **TS-02 Data/Provenance Foundation** — اگر Data Classes محدود انتخاب و access/legal boundary همان محدوده بسته شود.

این ترتیب Selection نیست و هیچ‌کدام خودکار وارد Technical نمی‌شوند.

## 16. Slices unsuitable for implicit entry

این Sliceها نباید فقط به دلیل اهمیت محصول بدون Decision Closure وارد Technical شوند:
- AI Day-one
- Identity/Authorization
- Service/Referral
- External Integration

زیرا Guessing در آنها مستقیماً به Authority، Data Access، Safety یا external contract behavior تبدیل می‌شود.

## 17. Minimal slice-gate record

پس از انتخاب هر Slice، قبل از ورود رسمی به Technical باید یک Gate Record محدود حداقل شامل این موارد ساخته شود:
- slice ID/name
- Business purpose
- included capabilities
- explicitly excluded capabilities
- Accepted Decisions relied upon
- Context-Triggered Decisions resolved
- Explicit Deferrals, if any
- constraints
- safety/data/security boundaries
- remaining Technical-only questions
- gate result
- gate approver/owner once defined

## 18. No automatic status change

BX-015:
- هیچ Slice را انتخاب نمی‌کند.
- هیچ Open Decision را Context Triggered نمی‌کند.
- هیچ Candidate Decision را Accepted نمی‌کند.
- Business → Technical Gate را Pass نمی‌کند.
- هیچ Backlog item را implementation-ready نمی‌کند.

## 19. Next context

پس از این Map، اولین حرکت واقعی به سمت Technical نیازمند **انتخاب صریح یک Slice** است.

تا قبل از آن می‌توان فقط Documentation/Gate Preparation غیرالزام‌آور انجام داد.

## 20. Next artifact

**BX-016 — Technical Entry Gate Preparation & Documentation Consistency Cleanup Plan**

Scope:
- reconcile BC-025 with D-0118
- update stale accepted-decision summaries
- align BR-003 / BR-004 status wording
- create a slice-gate evidence template
- preserve all OPEN decisions unchanged
- no Technical entry and no slice selection

## 21. Current stage

- Stage: **Business — Technical Entry Preparation**
- Candidate Technical slices: **MAPPED**
- Selected Technical slice: **NONE**
- Business → Technical Gate: **NOT PASSED**
- D-0006…D-0117: **NOT ACCEPTED**
- Code: **NOT STARTED**
- Codex handoff: **NOT YET TRIGGERED**