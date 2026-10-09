# Sprint 015 — Unbound Browser Identity Boundary

Date 2026-10-09. Branch `sprint-015-browser-identity-boundary`; base still-unmerged Draft PR #26 HEAD `05b48fdd6f9e5c163e8e9373c4e7f21f8e6bc1d5`; common main `f4bb75f1416e6b2dd83af4a9f835b8f1076316b4`.

Sequence: SG-015 → T-015 → PB-015 → Sprint Code (deny-only HTTP middleware) → PostgreSQL/HTTP test matrix → exact-head full Backend CI + Web CI → technical nonapproving Code Review. No new endpoints, migrations or frontend permission assumptions. The UI continues to display its original fail-closed auth gate on 401. No external IdP, cookie, key, origin or accepted authentication policy is invented.

Keep PRs #14–#26 plus Sprint 015 Draft/Open. No Merge, Ready, Stage/QA, Release or Production without explicit user instruction; D-0130 remains.
