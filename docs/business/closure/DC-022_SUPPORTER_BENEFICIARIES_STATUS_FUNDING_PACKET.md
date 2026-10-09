# DC-022 — Supporter Beneficiaries, Status Visibility and Money Injection: Open Decision Contract

- **Status:** Direction ACCEPTED under D-0174; individual workflows, permissions and financial contracts **NOT YET APPROVED**
- **Date:** 2026-10-09
- **Owner:** Business/Product Owner (financial and privacy contracts need separate explicit human approvals)
- **Inputs:** BC-003, BC-005, BC-009, BC-013, BC-014, BC-020, BC-022, D-0170, D-0171, D-0173, D-0174, UX-006 and UX-007.

## Approved capability requirements

1. A support organization must be able to **define/register people for its support scope**. This is an organizational relationship/enrollment **proposal** distinct from canonical Nasim Elder identity or an elder Case.
2. It must be able to **review per-person support status**, within separately authorized and privacy-minimized permission bounds. What a support status is and who may see it are open.
3. It must be able to **provide / inject money or resources** through a governed financial process that will be defined and integrated later.
4. It must be able to see **authorized funding and support activity/history** once authoritative read-models and policy exist.
5. This makes the supporter panel an **operational workspace**, not just an aggregate dashboard.

## Critical distinctions

`Organization person/beneficiary relationship != Nasim Elder != Nasim Case != family representative != payer account`.

`Support funding != personal elder wallet != child self-funded order != service payment` unless future accepted contracts explicitly connect them.

`Status seen by a supporter != complete healthcare/case records`.

## Open decisions before coding

| Area | Owner must specify |
|---|---|
| Actor class | Which entities count as supporter organizations, and whether they also act as employers, donors, or operators |
| Person registration | Person type, required minimal identifiers, evidence/consent, verification, duplicates, amendments, revocation and canonical Nasim identity/case linking |
| Support relationship | Who approves or rejects organization-person linkage; who may deactivate/reassign it; access after support ends |
| Status visibility | Exact categories and durable status vocabulary, authoritative status producer, fields, snapshot date, individual vs aggregate, purpose limitations and opt-out |
| Money destination | Fund to organizational support pool, individual-earmarked allocation, service-only budget, or another path; **NONE selected** |
| Financial authority | Funding principal/beneficiary, payer identity, currency, account ownership, ledger, PSP/bank, human authorization, maker-checker, idempotency, refunds/reversal, reconciliation, audit |
| Support spending | If and how support becomes a spendable amount; service eligibility, separate authorization, expiration, refunds and whether any elder-facing balance exists |
| Reporting & access | Reporting scope, supporter tenancy isolation, financial statement, per-person details, export/disclosure rules and retention |
| Exceptional cases | Wrong person, duplicate deposit, reversal, lost consent, interrupted provider, fraud prevention, dispute, inactive organization |

## Gate / non-implementation

No creation of an operative Case by sponsor, no exposing a sensitive Case read model, no new beneficiary lifecycle enum, no payment/credit/wallet schema or financial integration is authorized by this decision. No real-money feature must be simulated as successful in demo.

Business requirements → Technical contract → Product Backlog → Sprint → Code → Review → Stage/QA (when D-0130 permits) → release. Current Figma work remains non-operational.
