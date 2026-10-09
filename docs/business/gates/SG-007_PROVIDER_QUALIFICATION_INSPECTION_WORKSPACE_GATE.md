# SG-007 — Provider Qualification Inspection Workspace Business Gate

- Date: 2026-10-08
- Result: **FOUNDATION ONLY / eligible for Technical design**
- Basis: D-0124, D-0036, D-0037, D-0038, D-0131, D-0132, D-0133; existing SG-004, SG-005, SG-006 and BC-008
- Purpose: make *already authorized* descriptive Candidate, Qualification Evidence and Qualification Review Request records jointly inspectable without making a qualification judgement.

## Approved bounded behavior

One read-only Provider Candidate workspace returns three existing record views: one Candidate, independently paginated immutable Qualification Evidence and independently paginated immutable Qualification Review Requests. No new fields asserting business status, sufficiency, assigned reviewer, decision, activation, provider capacity or referral eligibility.

Authorization is strictly **all three existing read capabilities** on the same trusted ActorContext: `provider_candidate.read`, `provider_qualification_evidence.read`, `provider_qualification_review.read`. No composite grant, job-title inheritance, actor-role seed, special reviewer or system/AI business authority. AI fails closed even if erroneously granted capabilities. The existence of one permission cannot disclose another record class.

## Non-decisions

The workspace is **not** an immutable evidence bundle or a qualification snapshot. Later evidence may be appended; the view has no review-time pinning, complete evidence claim, decision, score, queue, reviewer assignment, activation or effect on existing records. Evidence pinning policy, qualification criteria, sufficiency, reviewer/approver identity and authority, status vocabulary, Provider Type, service/capacity/geography mapping, dispatch and Service Delivery remain **OPEN** (not deferred/accepted). No cross-context Case/Referral read.

## Gate

This narrowly derived informational composition adds no business authority and is allowed under D-0124. Larger Provider Decision / Activation work is **not** admitted. Continue with T-007 → PB-007 → Sprint-007 → Code → Code Review. D-0130 Hosted Stage remains unavailable; no merge, Release or Production approval is implied.
