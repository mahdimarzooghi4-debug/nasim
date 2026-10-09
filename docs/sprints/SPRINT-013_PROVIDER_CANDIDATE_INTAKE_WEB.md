# Sprint 013 — Provider Human Intake

Date: 2026-10-09. Source SG-013→T-013→PB-013 (existing approved Provider Registry records). Draft branch `sprint-013-provider-candidate-human-intake-web` based on still-unmerged Sprint 012 PR #24 HEAD `eb214058e24c30e1e1f4034c5647b79adbb3e2fc`.

Implement three immutable Provider Candidate/Evidence/Review Request POST calls with exact Backend contracts, typed forms, explicit human capability checks, safe same-origin idempotency and 201-authoritative refresh. Test in Web CI and inherited Backend CI, record review after full green. No backend DB/code modification, invented qualification decision or model activation.

Keep all PRs Draft/Open, no Merge/Ready/Hosted Stage/QA/Release/Production without explicit product owner approval. D-0130 remains active. Figma follows substantive code as instructed.
