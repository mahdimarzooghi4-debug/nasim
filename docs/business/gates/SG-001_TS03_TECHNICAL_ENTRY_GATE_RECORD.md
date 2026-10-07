# SG-001 — TS-03 Core Case / Journey Technical Entry Gate Record

- **Status:** PASSED WITH EXPLICIT DEFERRAL
- **Stage:** Business → Technical (TS-03 only)
- **Date:** 2026-10-07
- **Slice:** TS-03 — Core Case / Journey Foundation
- **Source basis:** D-0003 + D-0012 + D-0013 + D-0014 + D-0015 + D-0021 + D-0028 + D-0118 + D-0119…D-0126 + SGP-001 + BC-025
- **Gate result:** READY FOR THIS SLICE WITH EXPLICIT DEFERRAL

> This Gate passes only TS-03. It does not pass the global Business → Technical Gate for unrelated slices.

## 1. Included business scope

`Post-Enrollment → Contact → Case/Profile → Monitoring → Observation / Need capture`

Included capabilities:
- create/represent a Case/Profile after upstream Enrollment
- assigned caregiver as primary operational Case owner/contact
- Contact and Monitoring records
- Observation / Need capture
- caregiver assignment/reassignment history
- bounded TS-03 access
- append-only/auditable correction history
- actor and data provenance

## 2. Explicit exclusions

Out of TS-03:
- Enrollment rules/eligibility
- Referral lifecycle and authorization
- Service Delivery
- Provider selection/lifecycle
- Follow-up/Satisfaction
- Reassessment / Outcome / Need Resolution
- Emergency workflow
- KPI automation
- Billing/Settlement
- external integrations
- AI runtime
- Dataset Builder / Training Eligibility

## 3. Accepted decisions relied upon

- D-0003 — parent delivery process
- D-0012 — caregiver responsibility boundary
- D-0013 — Role Title ≠ Permission
- D-0014 — System ≠ independent Business Authority
- D-0015 — Human/System/AI/Automation traceability
- D-0021 — purpose-limited data use
- D-0028 — provenance preservation
- D-0118 — contextual decision closure
- D-0119 — TS-03 begins after Enrollment
- D-0120 — bounded early Journey
- D-0121 — caregiver Case owner + assignment/reassignment rule
- D-0122 — six minimum Case/Profile Data Classes
- D-0123 — minimum access boundary
- D-0124 — accelerated decision authority to Code boundary
- D-0125 — correction/history integrity
- D-0126 — exact named supervisory Role/Permission mapping deferred to TS-05

## 4. Explicit deferral

**Deferred item:** exact mapping of the authorized supervisory/operations function to a named Role/Permission.

- Future slice: TS-05 — Identity / Role / Authorization Foundation
- Owner: Product Owner
- Constraint: TS-03 may use only an abstract authorization capability/predicate; it must not hard-code a job title as final permission.

## 5. Data boundary

Allowed TS-03 Data Classes:
- Elder identity/reference
- Contact information
- Case administrative context
- Interaction / Monitoring record
- Observation / Need capture
- Caregiver assignment / history

Explicitly not included:
- Medical dataset
- Provider data
- Outcome data
- AI-training fields

## 6. Access boundary

- assigned caregiver: only data needed for Contact, Monitoring and Observation/Need capture
- authorized supervisory/operations function: only assignment/reassignment + operational oversight needs
- Elder self-access: not defined in TS-03
- Family/Representative: outside TS-03
- Provider: outside TS-03
- Employer: outside TS-03
- AI: outside TS-03

Default principle:
`Data Existence ≠ Access Permission`

## 7. Record integrity boundary

- no silent overwrite
- prior value/history preserved
- every correction records Actor + Time + Reason
- provenance/evidence link preserved where applicable
- exact technical versioning mechanism remains Technical

## 8. Authority boundaries

- Case Ownership ≠ Authorization
- Role Title ≠ Permission
- System execution ≠ Business approval
- AI has no role in TS-03 runtime scope

## 9. Safety / failure boundaries

TS-03 does not implement Emergency, Referral or Provider behavior.

If a Technical path would require any of those behaviors, it must fail closed / stop at the TS-03 boundary rather than invent a workflow.

## 10. Remaining Technical-only questions

Technical may decide, within accepted Business boundaries:
- domain aggregate boundaries
- identifiers
- field-level schema for the six Data Classes
- revision/history storage mechanism
- API/resource shape
- transaction boundaries
- abstract authorization interface/capabilities
- audit persistence
- event/outbox shape
- database constraints/indexing
- test architecture
- implementation stack

## 11. Gate evidence

- SGP-001: all required TS-03 Business choices resolved
- D-0126: one explicit bounded deferral
- no unrelated OPEN decision forced closed
- no Provider/AI/Outcome/Referral assumption introduced

## 12. Gate result

**READY FOR THIS SLICE WITH EXPLICIT DEFERRAL**

TS-03 is authorized to enter **Technical**.

Global Business → Technical remains **NOT PASSED** for unrelated slices.

## 13. Next stage

Create the TS-03 Technical Baseline and complete Technical Design before Product Backlog.

Code remains prohibited until Technical → Backlog → Sprint gates are complete and the Codex handoff is explicitly announced.