# PB-015 — Unbound Browser Identity Safety

Status: **Limited security hardening backlog**, not a general login product backlog.

- BI-015-01 P0: deny every `/api/v1/*` request that advertises an unverified browser Cookie/Origin/Referer/Fetch Metadata context, irrespective of spoofed principal or origin string.
- BI-015-02 P0: 401 stable typed error, no caching or Set-Cookie; do not add a token, login, Role grant or data mutation.
- BI-015-03 P0: preserve existing internal `TrustedPrincipal` + request-time resolver and anonymous 401; false HTTP identity headers cannot authenticate.
- BI-015-04 P0: real PostgreSQL HTTP matrix, cross-domain write non-effect assertion, stable public OpenAPI/health, full CI/exact-head review.
- BI-015-05 P0: document external issuer/browser session/CSRF/real E2E blockers; no vendor or secret guesses and no reversible env bypass.

Out of scope: issuer/OIDC provider choice, token parsing, cookie issuance, identity ownership, session expiry, production proxy, CSRF validation, authorization admin/grant provisioning, OAuth redirect or end-user login, AI, Provider authority, Outcome, Stage/QA/Release/Production.
