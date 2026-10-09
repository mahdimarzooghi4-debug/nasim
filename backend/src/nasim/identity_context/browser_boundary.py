"""Fail-closed boundary for *unimplemented* browser identity sessions.

Nasim has an internal, trusted-principal authorization resolver, but NO
approved external IdP, browser session issuer, Origin/CSRF verifier or browser
principal adapter. Browser request metadata must never be promoted to identity.
"""

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.responses import Response

BROWSER_REQUEST_HEADERS = frozenset(
    {
        "cookie",
        "origin",
        "referer",
        "sec-fetch-site",
        "sec-fetch-mode",
        "sec-fetch-dest",
        "sec-fetch-user",
    }
)


def browser_session_is_unbound(request: Request) -> bool:
    """Detect evidence of browser context; do not treat its value as trusted."""

    if not request.url.path.startswith("/api/v1/"):
        return False
    return any(header in request.headers for header in BROWSER_REQUEST_HEADERS)


def browser_session_unavailable() -> Response:
    """Deny a browser context until an approved trusted session exists.

    This is NOT a CSRF verifier or login endpoint. No header, cookie, URL,
    configuration variable or supposed principal can enable this path.
    """

    return JSONResponse(
        status_code=401,
        content={
            "error": {
                "code": "BROWSER_SESSION_NOT_CONFIGURED",
                "message": "A trusted browser identity session is not configured",
            }
        },
        headers={"Cache-Control": "no-store"},
    )
