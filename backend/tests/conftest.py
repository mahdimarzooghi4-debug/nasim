import os
from collections.abc import AsyncIterator

import pytest
from pydantic import PostgresDsn
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine

from nasim.application.casework import Casework
from nasim.identity_context.contracts import ActorContext, ActorType
from nasim.infrastructure.config import Settings
from nasim.infrastructure.database import make_engine, make_sessions

ALL_CAPABILITIES = frozenset(
    {
        "case.create",
        "case.read.assigned",
        "case.monitor.assigned",
        "case.observe.assigned",
        "case.contact.manage.assigned",
        "case.assignment.manage",
        "case.read.oversight",
    }
)


@pytest.fixture
def manager() -> ActorContext:
    return ActorContext(
        actor_id="operations-actor",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset({"case.assignment.manage", "case.read.oversight"}),
        correlation_id="test-manager",
    )


@pytest.fixture
def caregiver() -> ActorContext:
    return ActorContext(
        actor_id="caregiver-a",
        actor_type=ActorType.HUMAN,
        capabilities=frozenset(
            {
                "case.read.assigned",
                "case.monitor.assigned",
                "case.observe.assigned",
                "case.contact.manage.assigned",
            }
        ),
        correlation_id="test-caregiver",
    )


@pytest.fixture
async def admin_engine() -> AsyncIterator[AsyncEngine]:
    url = os.environ.get("NASIM_TEST_DATABASE_URL")
    if not url:
        pytest.skip("NASIM_TEST_DATABASE_URL absent: PostgreSQL integration was not executed")
    dsn = PostgresDsn(url)
    if not dsn.path or not dsn.path.endswith("_test"):
        pytest.fail("Destructive test setup requires a dedicated database ending in _test")
    engine = make_engine(Settings(database_url=dsn))
    async with engine.begin() as connection:
        version = await connection.scalar(text("SELECT version_num FROM alembic_version"))
        assert version == "0008_learning_manifest", (
            "Run scripts/setup-dev.sh or migrate test database first"
        )
        await connection.execute(
            text(
                "TRUNCATE elder_case, case_profile_revision, contact_point_revision, "
                "case_assignment, "
                "case_interaction, case_observation, audit_entry, outbox_event, "
                "idempotency_record, referral_follow_up_record, "
                "learning_proposed_source, learning_proposed_manifest, "
                "provider_qualification_review_request_record, "
                "provider_qualification_evidence_record, provider_candidate_record CASCADE"
            )
        )
    yield engine
    await engine.dispose()


@pytest.fixture
async def service(admin_engine: AsyncEngine) -> AsyncIterator[Casework]:
    url = os.environ.get("NASIM_TEST_APP_DATABASE_URL") or os.environ["NASIM_TEST_DATABASE_URL"]
    engine = make_engine(Settings(database_url=PostgresDsn(url)))
    yield Casework(make_sessions(engine))
    await engine.dispose()
