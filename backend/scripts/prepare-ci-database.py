"""Prepare a dedicated externally configured PostgreSQL CI test database and runtime role."""

import asyncio
import os
import subprocess
from urllib.parse import unquote

from pydantic import PostgresDsn
from sqlalchemy import literal, text
from sqlalchemy.ext.asyncio import create_async_engine

from nasim.infrastructure.stage_migrate import grant_runtime_access


async def prepare(owner: PostgresDsn, runtime: PostgresDsn) -> None:
    owner_host = owner.hosts()[0]
    runtime_host = runtime.hosts()[0]
    if (
        not owner.path
        or not owner.path.endswith("_test")
        or owner.path != runtime.path
        or owner_host["host"] != runtime_host["host"]
        or owner_host.get("port") != runtime_host.get("port")
        or owner_host.get("username") == runtime_host.get("username")
    ):
        raise RuntimeError("CI requires separate roles in the same dedicated *_test database")
    role = unquote(runtime_host.get("username") or "")
    password = unquote(runtime_host.get("password") or "")
    if not role or not password:
        raise RuntimeError("CI runtime login must be supplied externally")
    owner_url = str(owner).replace("postgresql://", "postgresql+asyncpg://", 1)
    environment = os.environ.copy()
    environment["NASIM_DATABASE_URL"] = owner_url
    subprocess.run(["alembic", "upgrade", "head"], check=True, env=environment)
    engine = create_async_engine(owner_url, hide_parameters=True)
    try:
        async with engine.begin() as connection:
            existing = await connection.scalar(
                text("SELECT 1 FROM pg_roles WHERE rolname=:role"), {"role": role}
            )
            if not existing:
                identifier = connection.dialect.identifier_preparer.quote(role)
                password_literal = literal(password).compile(
                    dialect=connection.dialect, compile_kwargs={"literal_binds": True}
                )
                await connection.execute(
                    text(
                        f"CREATE ROLE {identifier} LOGIN PASSWORD {password_literal} "
                        "NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS"
                    )
                )
    except Exception:
        # Utility-statement errors can include SQL literals; never reflect a password.
        raise RuntimeError("CI runtime-role provisioning failed") from None
    finally:
        await engine.dispose()
    await grant_runtime_access(owner_url, role)


if __name__ == "__main__":
    asyncio.run(
        prepare(
            PostgresDsn(os.environ["NASIM_TEST_DATABASE_URL"]),
            PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"]),
        )
    )
