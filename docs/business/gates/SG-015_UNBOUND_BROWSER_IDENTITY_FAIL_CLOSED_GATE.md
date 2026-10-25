# SG-015 — Unbound Browser Identity Fail-Closed Gate

- Date: 2026-10-09.
- Result: **TECHNICAL SAFETY FOUNDATION ONLY**; **not** acceptance of an external identity provider, Browser Session or Role/Permission mapping.
- Sources: D-0013/14/15, D-0126, SG-002/T-002 (TS-05 trusted in-process identity + request-time resolver), SG-011/T-011 through SG-014/T-014 (protected browser UI as Draft only), active D-0130 Hosted Stage deferral.
- Base: unmerged Draft PR #26 HEAD `05b48fdd6f9e5c163e8e9373c4e7f21f8e6bc1d5`.

## Exact allowed security scope

A true browser session/identity **does not exist** in this repository. We admit a standalone, default-on HTTP admission boundary that refuses requests for `/api/v1/*` carrying Cookie, Origin, Referer or Fetch Metadata browser-context headers, with a non-cacheable `401 BROWSER_SESSION_NOT_CONFIGURED`, regardless of any claimed identity or server-side test actor. This is an explicit fail-closed policy for **unbound browser identity** until a future accepted browser session/CSRF adapter is installed by a separately approved Technical/Business gate.

The existing trusted **in-process** `TrustedPrincipal → AuthorizationResolver → ActorContext` and internal server-side API calls **without browser request markers** remain unchanged. Public documentation/health routing remains independent. HTTP identity headers, fake bearer tokens and role labels must never authorize a principal.

## Hard limitations

Header absence is **not** proof that a caller is non-browser or authenticated; all such requests still undergo existing resolver/ActorContext checks and capabilities. Browser marker detection is **not** a CSRF validator, secure cookie issuer or external IdP. There is deliberately **no feature flag, env toggle, hardcoded origin, issuer, tenant, audience, client ID, token, cookie name, signing key, Auth redirect, default Role, or Admin bootstrap** that bypasses the denial. No provider/vendor, identity/grant provisioning rule, CSRF token mechanism or expiry is guessed.

The future approved browser integration must pin authoritative issuer/claims/principal mapping and tenant context, server-owned session lifecycle/revocation, Origin/CSRF, HTTPS/cookie settings and tested authorization. It must remove/replace this deny-only boundary through explicit reviewed code, not disable it silently by configuration.

Business → Technical SG-015/T-015 → Backlog PB-015 → Sprint 015 → Code/tests → full exact-head CI → non-approving technical Code Review. No Stage/QA/Release/Production (D-0130) and all source PRs stay Draft/Open.
