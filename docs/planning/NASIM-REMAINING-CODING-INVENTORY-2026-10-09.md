# Nasim — Remaining Coding Inventory (as of 2026-10-09)

**Purpose:** grounded engineering scope, not a new Business Decision or estimated percent-complete claim. Read with current GitHub branches and `docs/business/blockers/BR-004_CONTEXTUAL_OPEN_DECISION_REGISTER.md`.

## Implemented foundation (not all merged)

Main (Sprint 001–006): Post-enrollment Case/Profile + Contact/Monitoring/Observation/Need, assignment and append-only corrections; versioned capability registry/authorization resolver with **no real external login**; descriptive Referral creation; Provider Candidate, qualification evidence and qualification review request foundations. Exact main HEAD at inventory: `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`.

Draft/Open PR #17: TS-03 pagination/cursor/idempotency hardening. #18: Provider Qualification inspection read. #19: immutable human Referral follow-up. #20: coherent cross-context integration; exact head `522c9498d58cb4e4debd0df7e3ea90305c27b1b3`, CI #37900908040 SUCCESS with 521 Pytests. **These commits are not in main**. None is approved to merge.

## Remaining coding workstreams / dependencies

| Workstream | Missing capability | Gate / boundary |
|---|---|---|
| Case operations | coherent case journey read, operational work management, future case lifecycle/close | present descriptive read is authorized; lifecycle/closure rules OPEN |
| Real identity | externally validated authentication, session lifecycle, real IdP identity binding and role/permission provisioning | trusted in-process identity exists; IdP/legal access/operational roles not frozen |
| Provider operations | qualification decision and human approval, activation, authorized service/capacity/location, suspension | qualification criteria/authority, Provider Types, service-to-provider mapping OPEN |
| Referral lifecycle | provider matching with human selection, dispatch/accept/reject, reroute/cancel/close, proof of service | provider selection and sharing/consent/evidence and response semantics OPEN |
| Outcome/Reassessment | versioned baseline, independently reviewed observed changes, reassessment cadence, Need Resolution | outcome definition/evidence validity/cadence/authority OPEN |
| Consent and privacy | purpose-specific consent/legal basis, withdrawal, representative access, retention, sharing/export/erasure control | data access matrix, legal owner and policy OPEN |
| Internal AI runtime | model/provider-independent internal execution, governed human assistance and provenance; no autonomous official decisions | real model choice, runtime policy, AI Use Cases/Human Owner OPEN |
| Automatic Dataset Builder | **mandatory** automatic eligibility-gated versioned dataset creation with lineage, exclusions, lawful real data, separated operational/training purpose | Training-eligible data classes, legal basis/consent, curation/owner OPEN; synthetic 84-sample independent review unresolved |
| AI training/evaluation | independent, controlled training, dataset evaluation, candidate lineage, human model approval/promotion/rollback | evaluation metrics, governance/authority/model algorithm/hardware OPEN |
| Real UI | authenticated operational caregiver/operations/provider/admin workspace, RTL and usability tests | Figma intentionally later; build follows compatible live API and real login |
| Integrations | real SMS/communications, enrollment source, provider dispatch, health/other external services where required | partner, protocol, credentials, data-sharing and inventory OPEN |
| Production operations | observability, privacy/security audit, backup/recovery, secrets, health checks, formal Stage/QA, deploy/verification | D-0130 Stage unavailable; no Hosting/integration evidence or release authorization |

## Priority without inventing policy

1. Finish descriptive authorized Backend integrations and regression coverage on Draft branches.
2. Continue independent safe operational read/record slices backed by accepted Business+Technical gates, not synthetic production behavior.
3. Activate context-triggered decisions only for the first truly blocked business capability: Provider qualification/activation, actual Referral dispatch, identity or AI Learning Eligibility as applicable.
4. With accepted rules, implement larger full end-to-end Backend capability packages, then real UI, external integrations and Stage operationalization.
5. Preserve **automatic versioned Dataset Builder from day one**, internal controlled AI, human-reviewed Production promotion, and no direct raw Production-to-Training ingestion.

## Explicit governance

`OPEN ≠ DEFERRED ≠ ACCEPTED`. Product owner said manager approved and manually delivered educational/AI materials — do not ask again. Versioned handoff, independent Training data authorization and review of 84 synthetic examples are not repository-proven (Issues #11–#13). No new credential, vendor, threshold, model, actor authority, Release criteria or provider approval may be fabricated. Stage remains unavailable under D-0130. All Draft PRs must remain unmerged until explicit permission.
