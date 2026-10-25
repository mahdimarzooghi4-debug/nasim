# SG-014 — Case Creation / Assignment / Contact Web Gate

Date: 2026-10-09. **FOUNDATION ONLY / already accepted TS-03 Case commands**. Sources: SG-001/T-001/PB-001 TS-03, SG-002/T-002 existing capability-first identity, SG-010/T-010 Case index, SG-011/T-011 secure web, SG-012/T-012 human recording. Built on unmerged Draft PR #25 HEAD `ae715e3335a9af626ccab99f18a990aee3ad63fb`.

Admitted narrow UI scope:
- a HUMAN explicitly granted `case.assignment.manage` may create a Case **after supplying an existing upstream Enrollment reference**, an opaque elder reference, and initial caregiver actor ID, and may reassign a currently visible Case by an explicit reason plus exact expected current assignment;
- a HUMAN explicitly granted `case.contact.manage.assigned` who is the current Case caregiver may add an append-only Contact reference with operator-entered kind/value;
- a human who has existing Case read but no Referral/Follow-up read grant may access a narrow Case Profile and Contact workspace without obtaining inferred access to Referrals;
- a human with assignment-management but without `case.read.*` may create a Case without automatically being entitled to enumerate or read it. These are existing backend invariants, not newly granted roles.

Case creation records the **supplied** external Enrollment reference; it does not verify Enrollment completion, elder eligibility, identity legal basis or contacts. Reassignment records a new authoritative assignment, never edits historical rows. Contact reference is not proof of contact delivery or validation of ownership. No new lifecycle/status, triage, medical decision, Provider, external communication, AI, Outcome or data Training permission.

Delivery route: SG-014 → T-014 → PB-014 → Sprint-014 → Web code/test → exact-head full Web + Backend CI → technical nonapproving review. Stage remains unavailable D-0130. All PRs Draft/Open until explicit human instruction; no implicit merge, Release or Production.
