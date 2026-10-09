# T-024 — Keycloak OIDC and Hosted Stage target architecture

**Architecture selected by Product Owner (D-0169).** **No environment, realm, IdP client, production or hosted Stage actually provisioned. D-0130 still applies.** Date 2026-10-09.

## Recommended trust architecture
Browser → HTTPS reverse proxy → same-origin Nasim Web/BFF → Nasim Backend. Authentication authority: dedicated Keycloak realm OIDC; preferred confidential server-side Authorization Code + PKCE S256 + state/nonce, exact allowlisted redirect URI; no browser-available client secret or access tokens stored in LocalStorage. Backend/BFF validates issuer, audience, JWKS-signature, expiry, nonce/session binding, session rotation, strict SameSite/Secure/HttpOnly cookie and CSRF/Origin for mutations before building a server-trusted ActorContext. Subject/tenant/role/capabilities **must be mapped from vetted provisioning**, not arbitrary browser headers/role claims; Operations Manager privilege granted only to an actually identified and authorized human. AI/System remain separate principals and cannot impersonate a human.

Current `browser_session_unavailable()` and the 401 guard remain mandatory until actual live Keycloak + authorization tests exist. This design does not create working login.

## Stage target dependencies
| External source | Status/required proof |
|---|---|
| Hosting and VPC/network/routing | OPEN — actual provider/region/server tenancy needed; do not invent host or size |
| HTTPS DNS/TLS for Web/API and IdP | OPEN — owned domain, cert lifecycle and allowed origins/redirect URIs needed |
| Keycloak realm, confidential client, exact issuer, public keys, service account/user provisioning | OPEN — no fake secret, realm or grant |
| PostgreSQL persistent managed Stage instance + migrations/backups | OPEN — ephemeral CI PostgreSQL is NOT Stage |
| Secrets manager + restricted network & egress | OPEN |
| Observability/alerts and incident contact | OPEN |
| Staging data and privacy/test identities | OPEN — no real elder data without authorization |
| Independent QA & Stage acceptance tests | OPEN — not attempted |
| Production promotion/recovery | OUT OF SCOPE |

## Security admission
- Hard-coded or dynamic issuer from browser headers: prohibited.
- Confirm Keycloak published realm metadata through **HTTPS** and compare issuer exactly; verify discovery/JWKS and key rotation under trusted server config.
- Require registered redirect URI, OAuth state, nonce and PKCE S256. Scope/audience mapping and logout/session revocation contracts require Technical tests before live login.
- Keep Keycloak admin endpoints separated/restricted; restrict metrics/health management from public access; use fixed public hostname and correctly configured reverse-proxy forwarded headers. No anonymous access to Case/Provider.
- No default/fallback password, demo token, test principal, synthetic user or implicit Operations Manager grant.

Official reference: https://www.keycloak.org/server/configuration-production ; https://www.keycloak.org/server/reverseproxy ; https://www.keycloak.org/server/hostname .

## Stage Gate
Architecture documentation and disposable CI container smoke are **not** real Stage. Before any Hosted Stage approval obtain the concrete hosting provider/target, realm/issuer/client, server-issued TLS/DNS, Postgres/backup, secure secrets, operational owner, and authorize Stage deployment separately. Never treat D-0169 as permission to deploy or bypass Stage.
