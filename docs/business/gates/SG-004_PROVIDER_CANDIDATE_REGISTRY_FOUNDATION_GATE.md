# SG-004 — Provider Candidate Registry Foundation Gate

Date: 2026-10-07. Result: **READY FOR FOUNDATION ONLY**.

Authority: D-0124, D-0036…D-0042 and D-0131. Source references: BC-008 and DC-007.

## Purpose

Create only a pre-operational Provider Candidate Registry so Nasim can hold a traceable
identity/provenance record for a potential specialist Provider without treating that
record as an approved, active, eligible or selectable Provider.

## Included

- immutable Provider Candidate registration;
- internal canonical candidate ID;
- nonblank descriptive display name;
- Actor / ActorType / Time / Reason / Correlation provenance;
- explicit technical authorization capability for registration/read;
- audit, outbox and idempotency for registration;
- safe list/detail read contracts.

## Business boundary

`Registry Entry ≠ Operational Activation`.

A Provider Candidate record MUST NOT imply:

- Provider Type;
- qualification/credential approval;
- activation;
- Service eligibility or Service mapping;
- Referral destination or Provider selection;
- geographic coverage;
- capacity;
- contract status;
- Provider access to Elder/Case data;
- quality approval;
- financial/settlement authority.

No Role → Permission mapping is accepted by this Gate. Role Title does not create authority.

## OPEN, not ACCEPTED or DEFERRED

Provider Types for Pilot; onboarding/qualification; activation authority; service mapping;
Provider selection; Referral acceptance/rejection; capacity; completion evidence; data-sharing;
suspension/termination; rerouting; financial model; external Provider integration; correction
semantics and deduplication policy.

## Safety / governance

- AI may not register Provider Candidates.
- System/Automation do not receive authority from ActorType; any future use still requires an
  explicit capability and approved trusted-principal path.
- Candidate registration cannot mutate Referral or Case.
- No Provider candidate becomes operational through this slice.

Gate chain: SG-004 → T-004 → PB-004 → Sprint 004 → Code → Code Review.

D-0130 remains in force. No Hosted Stage/QA/Release/Production admission.
