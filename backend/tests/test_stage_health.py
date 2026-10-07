"""Stage uses the shared DB readiness handler; exercise real unavailable/migrated schema paths."""

import os

import httpx
import pytest
from pydantic import PostgresDsn
from sqlalchemy import text

from nasim.api.app import create_app
from nasim.infrastructure.config import Settings


async def test_health_fails_when_database_unreachable():
    app = create_app(
        Settings(database_url=PostgresDsn("postgresql://unused@127.0.0.1:1/unavailable"))
    )
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.get("/health")
        assert response.status_code == 503
        assert response.json() == {"status": "not_ready"}
    finally:
        await app.state.engine.dispose()


@pytest.mark.integration
async def test_stage_health_after_migration(admin_engine):
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
    finally:
        await app.state.engine.dispose()


@pytest.mark.integration
@pytest.mark.parametrize("failure", ["missing_revision_table", "incorrect_revision"])
async def test_stage_health_fails_closed_with_unavailable_schema(admin_engine, failure):
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    async with admin_engine.begin() as connection:
        if failure == "missing_revision_table":
            await connection.execute(
                text("ALTER TABLE alembic_version RENAME TO unavailable_revision")
            )
        else:
            await connection.execute(text("UPDATE alembic_version SET version_num='unreviewed'"))
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            response = await client.get("/health")
        assert response.status_code == 503
        assert response.json() == {"status": "not_ready"}
    finally:
        await app.state.engine.dispose()
        async with admin_engine.begin() as connection:
            if failure == "missing_revision_table":
                await connection.execute(
                    text("ALTER TABLE unavailable_revision RENAME TO alembic_version")
                )
            else:
                await connection.execute(
                    text("UPDATE alembic_version SET version_num='0006_provider_qreview'")
                )
