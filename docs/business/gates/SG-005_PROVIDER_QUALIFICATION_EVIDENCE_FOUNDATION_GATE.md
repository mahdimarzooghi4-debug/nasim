# SG-005 — Provider Qualification Evidence Foundation Gate

- **Date:** 2026-10-07
- **Result:** READY FOR FOUNDATION ONLY
- **Authority:** D-0124, D-0037, D-0131, D-0132
- **Source basis:** BC-008 + DC-007 + BX-007

## Purpose

Allow Nasim to record traceable qualification evidence against an existing Provider Candidate
without making any qualification, approval, activation, service-eligibility or provider-selection decision.

## Core invariant

`Qualification Evidence ≠ Qualification Decision ≠ Activation`

The existence, count or contents of evidence records MUST NOT imply that a Provider Candidate:

- is qualified;
- is approved;
- is active;
- is contracted;
- is eligible for any Service;
- is selectable for Referral;
- has any Case/Elder data-access right.

## Included

This Gate permits only:

- immutable Qualification Evidence records linked to an existing Provider Candidate;
- an opaque/descriptive evidence reference and descriptive label;
- Actor / ActorType / Time / Reason / Correlation provenance;
- explicit technical permission vocabulary for record/read;
- audit, outbox and idempotency for evidence registration;
- list/detail read contracts.

The evidence reference is an opaque business reference only. This Slice does not define file storage,
document transport, credential verification or external evidence retrieval.

## OPEN — not ACCEPTED or DEFERRED

The following remain OPEN:

- qualification criteria;
- mandatory documents;
- credential/licence requirements;
- evidence validity and expiry;
- reviewer;
- approver;
- review cadence;
- qualification result vocabulary/state machine;
- evidence correction/replacement rules;
- deduplication rules;
- contract prerequisite;
- activation authority/workflow/scope/effective date;
- Provider Type;
- Service-to-Provider mapping;
- geography eligibility;
- Capacity;
- Provider Selection;
- Referral acceptance/rejection;
- Provider data-sharing/access;
- suspension/termination;
- external Provider integration.

## Governance

- AI cannot make a qualification decision or activate a Provider.
- AI must not record Qualification Evidence in this Slice, even with an erroneous explicit capability.
- ActorType alone does not create authority.
- Role Title does not create permission.
- No Role → Permission mapping is accepted by this Gate.
- Evidence records are append-only; silent overwrite/delete is not allowed.
- Duplicate evidence references must not be prevented unless a later Business rule explicitly defines deduplication.

## Explicit exclusions

No qualification review result, approval, activation, contract, Service mapping, Provider selection,
capacity, Referral handoff/response, Service Delivery, Provider Case/Elder access, ranking/score,
finance, external integration, UI, Hosted Stage, Release or Production behavior.

Gate chain:

`SG-005 → T-005 → PB-005 → Sprint 005 → Code → Code Review`

D-0130 remains in force.
