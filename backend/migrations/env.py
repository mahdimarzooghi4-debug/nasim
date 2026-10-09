import asyncio

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine

from nasim.authorization import models as authorization_models  # noqa: F401
from nasim.infrastructure.config import load_settings
from nasim.learning import models as learning_models  # noqa: F401
from nasim.infrastructure.models import Base
from nasim.provider_registry import models as provider_registry_models  # noqa: F401
from nasim.referral import models as referral_models  # noqa: F401

target_metadata = Base.metadata


def run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()


async def run_online():
    engine = create_async_engine(load_settings().async_url, poolclass=pool.NullPool)
    async with engine.connect() as connection:
        await connection.run_sync(run_migrations)
    await engine.dispose()


if context.is_offline_mode():
    context.configure(
        url=load_settings().async_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()
else:
    asyncio.run(run_online())
