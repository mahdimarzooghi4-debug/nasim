# T-015 — HTTP Browser Identity Admission Boundary (deny-only)

Status: **no-provider, no-authentication technical protection**. This is NOT a usable browser login integration.

## Boundaries and error behavior

- `create_app()` gains a thin FastAPI middleware that screens **only** URLs under `/api/v1/`.
- If any of the request headers `Cookie`, `Origin`, `Referer`, `Sec-Fetch-Site`, `Sec-Fetch-Mode`, `Sec-Fetch-Dest`, `Sec-Fetch-User` is present, the request is denied before request authentication / Domain writes.
- Respond `401`, existing compatible `{"error":{"code":"BROWSER_SESSION_NOT_CONFIGURED","message":"A trusted browser identity session is not configured"}}`, `Cache-Control: no-store`, no `Set-Cookie`.
- Header *values* are never trusted. Presence tests do not authorize, infer identity, accept a particular origin, make a grant or process a mutation.
- `GET /openapi.json` and health stay outside the admission boundary. No DB writes/migrations or external network calls.
- Server-to-server/internal requests lacking those browser markers continue to **require** the existing trusted in-process Principal/ActorContext from the server, not caller-controlled HTTP headers. Backend permission checks and request-time Resolver remain the final authority.

## No unapproved browser security implementation

Do not implement JWT validation, OIDC discovery, fake BFF, generated cookie/token, CSRF double-submit secret, static admin, whitelisted origin/issuer, hardcoded credentials or bearer token adapter before contracts are accepted. Detecting browser request metadata is only **an additional refusal**, not a security guarantee if a malicious HTTP client forges/omits headers.

Future gate needs actual issuer/enterprise IdP and actor mapping, session storage/revocation, CSRF+Origin verification bound to session, safe cookie/HTTPS and audit policy, independent real browser E2E, hosted Stage and operations acceptance. Do not open a runtime bypass option.

## Verification

Real PostgreSQL+HTTP test matrix:
- Cookie, Origin, Referer and all Fetch Metadata markers, including same-origin values, on GET `authorization/self` and POST `cases`, even with a **test-only trusted in-process actor**.
- Non-cacheable 401 and no session cookie issuance.
- Rejected browser POST touches neither Cases, Audit, Outbox nor Idempotency DB tables.
- Plain anonymous forged `Authorization`, `X-Role`, `X-Actor-ID`, proxy identity headers remain 401, no actor.
- Trusted in-process test actor with non-browser request works to prove no regression to existing platform contract.
- OpenAPI remains available with browser headers.
- Full CI quality, PostgreSQL, migrations, disposable container smoke. All modifications Draft/unmerged. No hosted Stage.
