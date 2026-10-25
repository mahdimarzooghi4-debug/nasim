# Nasim — Pre-Stage Completion & Readiness Register

- **Project:** نسیم — نظام سالمند‌یاری محله‌محور
- **Status:** Current-state snapshot and execution plan; not a business acceptance or Stage certification
- **Updated:** 2026-10-25
- **Current main:** `52bf6ef15c701aa5ecec6a1a30635d83a2d0344b` (docs-only process update). Backend implementation through Sprint 024 is present in main; exact-head CI was previously verified on `25363a7d0c6d5fa129608dcff57de4d2af5610b5`. CI for the newer docs-only head is not asserted here.
- **Hosted Stage:** **UNAVAILABLE** under D-0130. No Stage admission, Stage QA, Release approval or Production deployment is claimed.

> This register records evidence and remaining gates. A merged technical foundation does not create business authority, operational permission, training eligibility or an external service. `OPEN ≠ ACCEPTED`; a closed issue is evidence only for the scope actually reviewed.

## 1. Current implementation baseline

| Area | Current state | Remaining boundary |
|---|---|---|
| Main branch | Backend work through Sprint 024 is integrated; current docs-only HEAD is `52bf6ef15c701aa5ecec6a1a30635d83a2d0344b` | Exact-head CI for the current docs-only SHA is not recorded; CI does not certify a deployed environment or user workflow |
| Backend | Case, Referral, Provider and learning-data foundations exist; migration head is `0009_learning_partition_claim` | Foundations do not by themselves complete operational Provider/service/Need/referral/outcome journeys |
| Web | React/TypeScript work is present for parts of Case and Provider operations | No complete supporter/admin product or Figma sign-off |
| Mobile | React Native/TypeScript is the accepted direction in D-0171 | No React Native app is implemented in this repository |
| Identity | Keycloak is the selected OIDC architecture (D-0169) | No real Keycloak realm/client, authentication integration or actor grants |
| AI | D-0135 selects read-only, source-grounded information for elder and caregiver; learning metadata foundations are present | No approved published corpus, operational AI runtime, Dataset Builder, Trainer, Evaluation or promotion pipeline |
| Stage/operations | Repository-side CI and container checks are available | Real Hosted Stage, secrets, identity, persistent DB, monitoring, backup and Stage QA are not supplied |

The 84 synthetic AI candidates have independent human review evidence recorded; issue #13 is closed. This does not establish a real official content corpus, lawful Training/Evaluation rights, an operational Dataset, or model evidence.

## 2. Remaining work, in dependency order

### A. Define the first operational Phase/Pilot

An initial participant target of **100 elders and 100 elder-care companions** is accepted in D-0176. Record the minimum capabilities that must be usable, and explicitly defer only out-of-scope capabilities with an owner, future gate and constraints. Geographic coverage, duration, entry criteria, whether these counts are targets or caps, and the complete accepted operational launch scope remain open.

### B. Close evidence-backed Business and authority inputs

| Work | Current status | Evidence or decision still needed |
|---|---|---|
| Provider qualification and activation | Open — issue [#38](https://github.com/mahdimarzooghi4-debug/nasim/issues/38) | Operations Manager review and actual decision on first service/provider scope, evidence criteria, activation, revocation, response and referral-selection rules |
| Official AI content | Open — issue [#11](https://github.com/mahdimarzooghi4-debug/nasim/issues/11) | Real source/version/authenticity, authorized publication, per-audience classification and correction/revocation route. Internet-source candidates and rights notes are tracked in `docs/ai/initial-content/INTERNET_SEED_SOURCE_INVENTORY.md`; none is approved yet. |
| Training/Evaluation eligibility | Open — issue [#12](https://github.com/mahdimarzooghi4-debug/nasim/issues/12) | D-0177 authorizes research/preparation of internet candidates for the initial seed; each exact source still requires rights and D-0161 approval. Operational Training/Evaluation eligibility, exclusions, curation and withdrawal/version lineage remain open. |
| Synthetic sample quality review | Closed — issue #13 | Review covers the 84 synthetic authoring candidates only; it is not permission to publish them as official policy or use them for training |
| First AI use case | Accepted direction — D-0135 | Read-only information for both audiences; actual source evidence, human follow-up and implementation gates remain |
| Supporter funding | D-0174/D-0175 accepted as high-level direction | Relationship, status data, funding/legal/accounting rules, permissions, payment integrations and actual transfer remain uncontracted |
| Family purchase | D-0170 accepted | Child pays using their own account; use of elder credit remains deferred |

Do not infer qualifications, Provider activation, financial authority, consent, personal-case access or training rights from titles, code, synthetic data or existing outbox events.

### C. Complete only the in-scope operational workflows

After the Phase/Pilot boundary and required Business decisions are recorded, define technical contracts and deliver bounded, reviewed slices for whichever workflows are in scope. Candidate gaps include Provider qualification/activation, service and Need catalogues, referral response and completion, Case outcomes/reassessment, and organization/supporter operations. Do not treat an existing record-creation API as a complete lifecycle.

### D. Deliver AI capabilities behind their separate gates

- Implement the D-0135 read-only experience only after authentic, approved content and audience permissions are available, with safe handling of missing, stale or conflicting sources and a real human follow-up route.
- Build automatic, continuously versioned Dataset production from newly observed **eligible-only** operational sources as required by D-0005. Existing outbox messages and the proposed manifest metadata are not an operational Dataset Builder or a Training grant.
- D-0177 now permits research and preparation of internet-source candidates for the initial seed. The reviewed source inventory contains no approved source; it does not authorize a Training Run. Keep Training, independent Evaluation, model selection, and human promotion as distinct decisions. D-0147 defers final model choice until comparable evidence exists; this does not remove the Day-one eligible-only operational Dataset requirement.

### E. Build the selected user experiences

D-0171 selects React/TypeScript for web and React Native/TypeScript for mobile. D-0172 and D-0173 record mobile UX and visual direction; these decisions are not completed applications or accessibility QA. Implement the elder/family and professional-caregiver experiences, plus in-scope supporter/admin workflows, only against accepted journeys, permissions and API contracts. No Figma sign-off or complete mobile project is recorded in this repository.

### F. Provision and verify real Stage

Issue [#37](https://github.com/mahdimarzooghi4-debug/nasim/issues/37) tracks actual infrastructure and Keycloak inputs. Provisioning still needs real hosting/network/DNS/TLS, Keycloak realm/client, persistent Stage database, secret storage, backup/restore, logs/metrics/alerts, operating owners, safe test data and explicit deploy authorization. After the environment exists, run independent Stage QA and obtain separate Release approval before Production.

## 3. Gate order

`Accepted Phase/Pilot scope → required Business decisions/evidence → Technical contracts → Product Backlog → authorized Sprint → Code → Code Review → exact-head CI → Hosted Stage admission → Stage QA → Release approval → Production → Monitoring`

For work outside the accepted initial scope, record an explicit deferral with owner, scope, future gate and constraints. Do not label an OPEN item as deferred.

## 4. Current readiness outcome

**NOT READY FOR HOSTED STAGE.** The initial cohort target is 100 elders and 100 elder-care companions, but the full operational pilot boundary is still open. Internet-source research for initial AI seed is authorized, but no source has cleared rights/content review or D-0161 approval. Hosted Stage is unavailable under D-0130; relevant Provider evidence, real identity/infrastructure and in-scope user workflows remain. Stage QA, Release and Production are separate later decisions.
