"""One-shot migration command, separate from runtime serving and credentials."""

import asyncio
import os
import subprocess

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from nasim.infrastructure.stage_config import load_stage_migration_settings


async def grant_runtime_access(migration_url: str, app_role: str) -> None:
    engine = create_async_engine(migration_url, hide_parameters=True)
    try:
        async with engine.begin() as connection:
            # Privileged provisioning must supply a pre-existing, restricted runtime login.
            role = (
                await connection.execute(
                    text(
                        "SELECT rolsuper, rolcreatedb, rolcreaterole, rolreplication, rolbypassrls "
                        "FROM pg_roles WHERE rolname=:name"
                    ),
                    {"name": app_role},
                )
            ).first()
            if role is None or any(role):
                raise RuntimeError("Runtime role must exist and have no administrative privileges")
            quoted_role = connection.dialect.identifier_preparer.quote(app_role)
            await connection.execute(text(f"GRANT USAGE ON SCHEMA public TO {quoted_role}"))
            tables = (
                "elder_case",
                "case_profile_revision",
                "contact_point_revision",
                "case_assignment",
                "case_interaction",
                "case_observation",
                "audit_entry",
                "outbox_event",
                "idempotency_record",
            )
            for table in tables:
                unsafe = await connection.scalar(
                    text("SELECT has_table_privilege(:role, :table, 'DELETE,TRUNCATE')"),
                    {"role": app_role, "table": table},
                )
                if unsafe:
                    raise RuntimeError("Runtime role has destructive privileges or owns schema")
            audit_update = await connection.scalar(
                text("SELECT has_table_privilege(:role, 'audit_entry', 'UPDATE')"),
                {"role": app_role},
            )
            if audit_update:
                raise RuntimeError("Runtime role must not update audit history")
            for table in (*tables, "alembic_version"):
                await connection.execute(text(f"GRANT SELECT ON {table} TO {quoted_role}"))
            for table in tables:
                await connection.execute(text(f"GRANT INSERT ON {table} TO {quoted_role}"))
            await connection.execute(
                text(f"GRANT UPDATE (ended_at) ON case_assignment TO {quoted_role}")
            )
            # SELECT FOR UPDATE needs column UPDATE; immutable trigger blocks actual changes.
            await connection.execute(text(f"GRANT UPDATE (id) ON elder_case TO {quoted_role}"))
    finally:
        await engine.dispose()


def main() -> None:
    settings = load_stage_migration_settings()
    migration_url = str(settings.migration_database_url).replace(
        "postgresql://", "postgresql+asyncpg://", 1
    )
    environment = os.environ.copy()
    environment["NASIM_DATABASE_URL"] = migration_url
    subprocess.run(["alembic", "upgrade", "head"], check=True, env=environment)
    subprocess.run(["alembic", "check"], check=True, env=environment)
    app_role = settings.database_url.hosts()[0]["username"]
    assert app_role is not None
    asyncio.run(grant_runtime_access(migration_url, unquote_role(app_role)))


def unquote_role(value: str) -> str:
    from urllib.parse import unquote

    return unquote(value)


if __name__ == "__main__":
    main()
