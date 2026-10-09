"""HTTP boundary contract: there is no browser IdP or session to authenticate yet."""

import os
from uuid import uuid4

import httpx
import pytest
from pydantic import PostgresDsn
from sqlalchemy import func, select

from nasim.api.app import create_app, get_actor
from nasim.infrastructure.config import Settings
from nasim.infrastructure.models import AuditEntry, ElderCase, IdempotencyRecord, OutboxEvent

pytestmark = pytest.mark.integration

BROWSER_CONTEXTS = [
    {"Cookie": "session=forged"},
    {"Origin": "https://untrusted.example"},
    {"Origin": "https://nasim.example"},
    {"Referer": "https://nasim.example/workspace"},
    {"Sec-Fetch-Site": "same-origin"},
    {"Sec-Fetch-Site": "cross-site"},
    {"Sec-Fetch-Mode": "cors"},
    {"Sec-Fetch-Dest": "empty"},
    {"Sec-Fetch-User": "?1"},
    {"Cookie": "session=forged", "Origin": "https://nasim.example"},
]


def app_for_test():
    return create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))


@pytest.mark.parametrize("headers", BROWSER_CONTEXTS)
@pytest.mark.parametrize("method", ["GET", "POST"])
async def test_protected_browser_http_context_denied_even_with_test_only_actor_override(
    admin_engine, manager, headers, method
):
    app = app_for_test()
    app.dependency_overrides[get_actor] = lambda: manager
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            if method == "GET":
                response = await client.get("/api/v1/authorization/self", headers=headers)
            else:
                response = await client.post(
                    "/api/v1/cases",
                    json={
                        "upstream_enrollment_ref": "test-upstream",
                        "elder_reference": "opaque-elder",
                        "initial_caregiver_actor_id": "caregiver",
                    },
                    headers={"Idempotency-Key": str(uuid4()), **headers},
                )
            assert response.status_code == 401
            assert response.json() == {
                "error": {
                    "code": "BROWSER_SESSION_NOT_CONFIGURED",
                    "message": "A trusted browser identity session is not configured",
                }
            }
            assert response.headers["cache-control"] == "no-store"
            assert "set-cookie" not in response.headers
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()


async def test_rejected_browser_mutations_do_not_touch_business_or_effect_tables(
    admin_engine, manager
):
    app = app_for_test()
    app.dependency_overrides[get_actor] = lambda: manager

    async def counts():
        async with admin_engine.connect() as conn:
            values = []
            for table in (ElderCase, AuditEntry, OutboxEvent, IdempotencyRecord):
                values.append(await conn.scalar(select(func.count()).select_from(table)))
            return tuple(values)

    before = await counts()
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            reply = await client.post(
                "/api/v1/cases",
                headers={
                    "Cookie": "opaque_session=forged",
                    "Idempotency-Key": str(uuid4()),
                    "X-Actor-ID": "operations-actor",
                    "Authorization": "Bearer untrusted",
                },
                json={
                    "upstream_enrollment_ref": "no-real-enrollment-verification",
                    "elder_reference": "opaque",
                    "initial_caregiver_actor_id": "a",
                },
            )
            assert reply.status_code == 401
            assert reply.json()["error"]["code"] == "BROWSER_SESSION_NOT_CONFIGURED"
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()
    assert await counts() == before


async def test_non_browser_in_process_actor_remains_supported_and_headers_cannot_authenticate(
    admin_engine, manager
):
    app = app_for_test()
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            anonymous = await client.get(
                "/api/v1/authorization/self",
                headers={
                    "Authorization": "Bearer forged",
                    "X-Actor-ID": manager.actor_id,
                    "X-Role": "supervisor",
                },
            )
            assert anonymous.status_code == 401
            assert anonymous.json()["error"]["code"] == "ACTOR_CONTEXT_REQUIRED"

            app.dependency_overrides[get_actor] = lambda: manager
            trusted = await client.get("/api/v1/authorization/self")
            assert trusted.status_code == 200
            assert trusted.json()["actor_id"] == manager.actor_id
            assert set(trusted.json()["capabilities"]) == set(manager.capabilities)
    finally:
        app.dependency_overrides.clear()
        await app.state.engine.dispose()


async def test_openapi_remains_public_for_contract_read_even_with_browser_metadata(admin_engine):
    app = app_for_test()
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.get(
                "/openapi.json",
                headers={"Sec-Fetch-Site": "same-origin", "Cookie": "opaque=anything"},
            )
            assert response.status_code == 200
            assert "/api/v1/authorization/self" in response.json()["paths"]
    finally:
        await app.state.engine.dispose()


async def test_real_api_ignores_trusted_principal_supplied_as_http_headers(admin_engine, manager):
    app = app_for_test()
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.get(
                "/api/v1/authorization/self",
                headers={
                    "X-Trusted-Principal": manager.actor_id,
                    "X-Forwarded-User": manager.actor_id,
                    "X-Authenticated-User": manager.actor_id,
                },
            )
            assert response.status_code == 401
            assert response.json()["error"]["code"] == "ACTOR_CONTEXT_REQUIRED"
    finally:
        await app.state.engine.dispose()
