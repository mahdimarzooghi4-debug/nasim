# Sprint 012 — Governed Caregiver Recording (Draft only)

Date: 2026-10-09. Base: unmerged PR #23 HEAD `69867fe4760ef561bb17dcfd7b1b0cdc0a43af62`. Status: **Code and tests on isolated Draft PR**.

Parent lifecycle: Business SG-012 → Technical T-012 → Product Backlog PB-012 → Sprint → Web source/test → Code Review → Stage (unavailable).

Implementation: reuse existing backend commands via typed same-origin browser POST, forms for Need/Observation, CONTACT/MONITORING, Referral and human Follow-up; secure per-intent idempotency; current-assignment and capability presentation checks; authoritative server refresh, no invented outcomes or provider authority. Preserve all backend contracts and previous PRs #14–#23 as-is.

Gate: exact final SHA Web CI and full Backend CI then AI-assisted non-approving Code Review; no merge, Ready for Review, hosted Stage, QA/Release/Production without explicit product owner instruction. Lack of real IdP, CSRF/session policy, accepted consent and external integrations is an explicit blocker to real-data deployment.
