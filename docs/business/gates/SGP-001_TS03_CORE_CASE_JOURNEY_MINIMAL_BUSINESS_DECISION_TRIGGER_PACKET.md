# SGP-001 — TS-03 Core Case / Journey Minimal Business Decision Trigger Packet

- **Status:** ACTIVE — CONTEXT TRIGGERED
- **Stage:** Business — TS-03 Slice Gate Preparation
- **Date:** 2026-10-07
- **Selected Slice:** TS-03 — Core Case / Journey Foundation
- **Selection authority:** Product Owner
- **Source basis:** D-0001…D-0005 + D-0118 + BX-003 + BX-004 + BX-005 + BX-015 + BX-018 + BX-019 + DC-001 + DC-003 + DC-004 + DC-005 + BR-003 + BR-004
- **Purpose:** بستن فقط کوچک‌ترین Business Decision Set لازم برای Technical Design محدود TS-03، بدون ورود به Referral/Provider/Outcome/AI implementation.

> Selection of TS-03 is explicit. No Candidate Decision below is accepted merely by appearing in this packet.

## 1. Selected technical intent

TS-03 is selected to establish the bounded product/technical foundation around:
- Elder
- Case / Profile
- contact
- monitoring
- basic observation/history
- case responsibility / handoff boundary
- audit / provenance

before full Referral/Service automation.

## 2. Explicitly outside this Slice

These remain outside TS-03 unless Product Owner later expands the slice:
- detailed Referral state machine
- Provider selection / matching
- Provider lifecycle
- Service pricing / billing / settlement
- Outcome taxonomy
- Reassessment workflow
- KPI automation
- external integrations
- AI runtime / Dataset Builder implementation
- full Emergency workflow

These are not rejected or deferred globally; they remain OPEN for their own context.

## 3. Context-triggered Candidate Decisions

Only the following existing Candidate Decisions are now relevant enough to review for TS-03:

### CT-D-0006 — Phase-1 Target Population
Candidate text: Phase-1 target population is elderly people under support of Imam Khomeini Relief Foundation.

Initial trigger reason: TS-03 needed to know whether Case creation was scoped directly to Phase-1 eligibility or began after an upstream enrollment decision.

**Q1 resolution:** D-0119 selected the post-enrollment boundary. Therefore D-0006 is **NO LONGER REQUIRED FOR TS-03 GATE** and returns to the unrelated OPEN/not-accepted candidate pool. It is neither Accepted nor Deferred by TS-03.

### CT-D-0012 — Caregiver base responsibility boundary
Candidate direction: caregiver base responsibility includes contact, monitoring, recording, coordination, Referral and Follow-up; specialist medical/financial/provider-activation/final-eligibility authority is not inferred.

Reason triggered: TS-03 needs a safe operational boundary for who may act around Case/Monitoring.

Status: **CONTEXT TRIGGERED — NOT ACCEPTED**

### CT-D-0013 — Role is not Permission
Candidate direction: job title/career level does not itself create Permission or Approval Right.

Reason triggered: Case ownership must not silently become authorization.

Status: **CONTEXT TRIGGERED — NOT ACCEPTED**

### CT-D-0014 — System is not independent Business Authority
Candidate direction: the NASIM system executes/records approved rules; automation does not create independent Business Decision Right.

Reason triggered: TS-03 will represent Case actions and must not infer authority from system execution.

Status: **CONTEXT TRIGGERED — NOT ACCEPTED**

### CT-D-0015 — Actor provenance
Candidate direction: important actions must distinguish Human / System / AI / Automation origin for audit.

Reason triggered: TS-03 requires action provenance/history.

Status: **CONTEXT TRIGGERED — NOT ACCEPTED**

### CT-D-0016 — Single Point of Contact
Candidate direction: elder should have a close, traceable contact point and caregiver is the primary coordination interface; substitution/change of Case Owner remains separate.

Initial trigger reason: TS-03 includes Case responsibility/handoff.

**Q3 resolution:** D-0121 establishes the caregiver as Primary Operational Case Owner / Contact for TS-03 and requires authorized assignment/reassignment with reason + audit. D-0016 remains **NOT ACCEPTED AS A WHOLE**; its broader journey meaning remains reference material.

### CT-D-0017 — High-level Elder Journey
Candidate direction: Contact → Case/Profile → Monitoring → Need → Initial Assessment → Referral if needed → Service → Follow-up → Satisfaction → Continued Monitoring.

Initial trigger reason: TS-03 needed to define which early interactions belong to this bounded slice.

**Q2 resolution:** D-0120 fixes the TS-03 boundary at `Contact → Case/Profile → Monitoring → Observation / Need capture`. Therefore D-0017 remains **NOT ACCEPTED AS A WHOLE** and is no longer a blocker for the remaining later Journey stages in TS-03.

### CT-D-0021 — Purpose-limited data use
Candidate direction: each Data Class is used only for an approved Purpose; Service Delivery, Reporting, AI Runtime and AI Training are separate purposes.

Reason triggered: Case/Profile data needs a declared operational purpose.

Status: **CONTEXT TRIGGERED — NOT ACCEPTED**

### CT-D-0028 — Provenance must be preserved
Candidate direction: source of data must remain distinguishable across Elder, Family, Caregiver, Provider, System, AI and human-reviewed AI.

Reason triggered: TS-03 requires record/history provenance.

Status: **CONTEXT TRIGGERED — NOT ACCEPTED**

## 4. Candidate Decisions deliberately NOT triggered

These remain not accepted and are not required for TS-03 gate preparation at this time:
- D-0007 — Pilot purpose
- D-0011 — full Employer / NASIM Operator / Provider separation
- D-0018 — Follow-up/Satisfaction as core caregiver duty
- D-0019 — Service Completion / Need Resolution separation
- D-0020 — Emergency boundary
- D-0022…D-0027 — training/runtime/family/provider/employer/dataset governance candidates

Reason: their detailed behavior is outside the current bounded TS-03 design unless scope is later expanded.

## 5. Context-triggered unresolved choices

These are the actual Product Owner choices needed before TS-03 can be gate-checked.

### Q1 — Case entry boundary — RESOLVED
**Accepted: Option A.** TS-03 starts after enrollment. Case/Profile assumes the elder has already been admitted by an upstream Business process; enrollment eligibility enforcement is outside this Slice.

Decision Record: **D-0119**.

### Q2 — Early journey scope — RESOLVED
**Accepted:** `Contact → Case/Profile → Monitoring → Observation / Need capture`.

Referral، Service Delivery، Follow-up، Satisfaction، Reassessment، Need Resolution و Outcome خارج از TS-03 باقی می‌مانند.

Decision Record: **D-0120**.

### Q3 — Case operational owner — RESOLVED
**Accepted:**
- سالمندیار is the Primary Operational Case Owner / Contact.
- initial assignment and reassignment/substitution are performed by an authorized supervisory/operations function.
- every reassignment/substitution requires reason + actor + time + audit trail.
- exact mapping of the authorized function to a named Role/Permission remains OPEN for Identity/Authorization.

Decision Record: **D-0121**.

### Q4 — Minimum Case/Profile information
Before Data Model design, Business must identify only the minimum Data Classes needed by this Slice.

Source-supported categories may include:
- elder identity/reference
- contact information
- Case administrative context
- interaction/monitoring record
- observation / Need capture
- caregiver assignment/history

Exact fields are not defined in this packet.

### Q5 — Correction / history
Need explicit rule for whether Case/Profile/Observation corrections:
- preserve prior value/history
- record actor/time/reason
- distinguish correction from silent overwrite

Exact technical event/version mechanism remains Technical.

### Q6 — Access boundary for TS-03 data
Need only the minimum access direction for actors actually participating in TS-03.

Provider, Employer, Family/Representative and AI access can remain out of Slice unless Product Owner includes them.

## 6. Decisions allowed to remain OPEN

For TS-03 Gate, these can remain OPEN if kept outside the Slice:
- Pilot geography
- Pilot population count
- Pilot duration
- Active Service Catalog
- Referral authorization/lifecycle
- Provider selection
- Provider response/completion
- Emergency workflow
- Outcome/Reassessment
- KPI targets
- Billing/Settlement
- Integration inventory
- AI runtime use cases
- Training Eligibility / Dataset Builder

## 7. Slice Gate must-not-assume constraints

Technical must not assume:
- exact enrollment eligibility unless Q1 chooses B and it is closed;
- caregiver job title equals permission;
- system action equals Business approval;
- family contact equals authorized representative;
- Provider/employer access to Case data;
- AI access to Case data;
- Case/Need closure behavior;
- Referral behavior;
- Emergency behavior;
- silent overwrite for corrected records.

## 8. Closure sequence for SGP-001

Close in this order:
1. Q1 — Case entry boundary — **RESOLVED by D-0119**
2. Q2 — early journey scope — **RESOLVED by D-0120**
3. Q3 — Case operational owner / assignment — **RESOLVED by D-0121**
4. Q4 — minimum Case/Profile Data Classes
5. Q5 — correction/history
6. Q6 — minimum access boundary
7. review Context-Triggered Candidate Decisions for explicit acceptance/modification
8. create SG-001 for TS-03

Only one small decision set should be discussed at a time.

## 9. Current state

- Selected Technical Slice: **TS-03**
- TS-03 status: **SELECTED FOR GATE PREPARATION**
- SGP-001: **ACTIVE**
- Context-triggered Candidate Decisions still active for TS-03: D-0012, D-0013, D-0014, D-0015, D-0021, D-0028
- Resolved boundary references: D-0006 released by D-0119; D-0017 bounded by D-0120; D-0016 no longer blocks TS-03 case ownership because D-0121 establishes the slice-specific owner/assignment rule.
- Accepted decisions created from this packet: **D-0119, D-0120, D-0121**
- Explicitly Deferred from this packet: **0**
- Unrelated decisions: **OPEN / unchanged**
- TS-03 Slice Gate: **NOT YET READY**
- Global Business → Technical Gate: **NOT PASSED**
- Technical: **NOT STARTED**
- Code: **NOT STARTED**

## 10. Next Product Owner question

**Q4 — Minimum Case/Profile Data Classes**

Proposed minimum for TS-03:
- Elder identity/reference
- contact information
- Case administrative context
- interaction/monitoring record
- Observation / Need capture
- caregiver assignment/history

No detailed fields, medical dataset, Provider data, Outcome data or AI-training fields are included yet.

**Confirm this minimum set or modify it.**