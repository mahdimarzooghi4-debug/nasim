# SG-006 — Provider Qualification Review Request Foundation Gate

- **Date:** 2026-10-07
- **Result:** READY FOR FOUNDATION ONLY
- **Authority:** D-0124, D-0037, D-0132, D-0133
- **Source basis:** BC-008 + DC-007 + BX-007

## Purpose

Allow Nasim to record that a human-controlled qualification review has been requested for an
existing Provider Candidate without assigning a reviewer and without making any qualification,
approval, activation, service-eligibility or provider-selection decision.

## Core invariant

`Review Request ≠ Review Decision ≠ Activation`

A Review Request MUST NOT imply that a Provider Candidate:

- has been reviewed;
- is qualified;
- is approved;
- is active;
- is contracted;
- is eligible for any Service;
- is selectable for Referral.

## Included

This Gate permits only:

- immutable Qualification Review Request records linked to an existing Provider Candidate;
- human-readable request reason;
- Actor / ActorType / Time / Correlation provenance;
- explicit technical permission vocabulary for request/read;
- audit, outbox and idempotency for request creation;
- list/detail read contracts.

## Evidence boundary

Existing Qualification Evidence remains independently append-only and queryable.

This Slice does NOT define:

- a required evidence set;
- evidence sufficiency;
- evidence completeness;
- evidence pinning/bundle policy;
- mandatory document rules;
- credential validity;
- evidence expiry.

A Review Request therefore does not certify that sufficient evidence exists.

## OPEN — not ACCEPTED or DEFERRED

The following remain OPEN:

- reviewer identity and reviewer authority;
- approver identity and approval authority;
- review assignment;
- review queue ownership;
- review SLA/cadence;
- qualification criteria;
- evidence sufficiency;
- evidence pinning/bundle policy;
- decision vocabulary/state machine;
- rejection/rework semantics;
- approval/activation authority;
- activation scope/effective date;
- Provider Type;
- Service-to-Provider mapping;
- geography eligibility;
- Capacity;
- Provider Selection;
- Referral acceptance/rejection;
- Provider data-sharing/access;
- suspension/termination.

## Governance

- AI cannot request qualification review in this Slice.
- System/Automation ActorType alone does not create authority.
- Role Title does not create permission.
- No Role → Permission mapping is accepted by this Gate.
- Review Request is append-only and immutable.
- Repeated requests are allowed; no one-active-request rule is invented.
- No status/state field is introduced.

## Explicit exclusions

No reviewer assignment, review result, qualification decision, approval, activation, Provider Type,
Service mapping, Provider selection, Capacity, Referral response, Service Delivery, Provider
Case/Elder access, ranking/score, finance, external integration, UI, Hosted Stage, Release or
Production behavior.

Gate chain:

`SG-006 → T-006 → PB-006 → Sprint 006 → Code → Code Review`

D-0130 remains in force.
