# SG-011 — Live Operational Web Read Foundation

Date: 2026-10-09. Status **FOUNDATION ONLY**. This is a display/interaction layer for existing allowed Case, Referral, Follow-up and Provider Registry *reads*. Not acceptance of any new Business Domain capability.

Sources: SG-001/T-001, SG-002/T-002, SG-007/T-007, SG-008/T-008, SG-009/T-009, SG-010/T-010 and the existing versioned TS-05 permission model. The preceding features are **Draft PRs**, not merged into main.

Product owner order: complete product code/real tests before Figma. Frontend uses a provisional accessible responsive Persian RTL design. Figma reconciliation follows implementation, never defines runtime data.

## Narrow admitted UI behavior

A genuinely authenticated human can *read* a list of currently assigned Cases (or cases under explicitly granted oversight), inspect existing Case Profile, Need/Observation, descriptive Referral, and human Follow-up records; independently a user with the required Provider Registry read permissions can inspect Provider Candidates, submitted Qualification Evidence and Qualification Review Requests. Every listed record comes from the real Backend, never from a hard-coded sample/mock/default Case. No workflow action is invented.

Authentication is not yet externally integrated and TS-05 explicitly supplies no public login, headers, token or actor provisioning. The frontend must **not** fabricate a login, actor, token or permission. It renders a blocked/unavailable view when `GET /api/v1/authorization/self` fails. After a valid future same-origin trusted identity adapter, the server supplies exact capability context. The UI may hide links based on that context but **backend remains authoritative for every request**.

## Non-decisions

No new RBAC, IdP provider, authentication bypass, Provider qualification/approval, service selection, referral dispatch/status, outcome, training eligibility, AI model, payment, consent-sharing or medical authority. Backend Contract owners determine responses. Figma status does not become a Business Contract.

Gate: SG-011 → T-011 → PB-011 → Sprint 011 → Code/tests → full exact-head Backend+Web CI → technical Code Review. D-0130 hosted Stage unavailable; Draft only, no Release/Production.
