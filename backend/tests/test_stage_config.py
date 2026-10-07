import pytest
from pydantic import ValidationError

from nasim.api.stage import create_stage_app
from nasim.infrastructure.stage_config import (
    StageConfigurationError,
    StageMigrationSettings,
    load_stage_settings,
)

RUNTIME = (
    "postgresql+asyncpg://stage_app:VALIDATION_ONLY_NOT_A_SECRET@postgres:5432/stage_validation"
)
OWNER = (
    "postgresql+asyncpg://stage_owner:VALIDATION_ONLY_NOT_A_SECRET@postgres:5432/stage_validation"
)


@pytest.fixture
def stage_environment(monkeypatch):
    monkeypatch.setenv("NASIM_ENVIRONMENT", "stage")
    monkeypatch.setenv("NASIM_DATABASE_URL", RUNTIME)
    monkeypatch.delenv("NASIM_MIGRATION_DATABASE_URL", raising=False)


def test_stage_configuration_is_explicit(stage_environment):
    settings = load_stage_settings()
    assert settings.environment == "stage"
    assert settings.async_url == RUNTIME


@pytest.mark.parametrize("missing", ["NASIM_ENVIRONMENT", "NASIM_DATABASE_URL"])
def test_stage_requires_environment_and_database(stage_environment, monkeypatch, missing):
    monkeypatch.delenv(missing)
    with pytest.raises(StageConfigurationError):
        create_stage_app()


@pytest.mark.parametrize("value", ["", "development", "production"])
def test_stage_environment_cannot_fall_back(stage_environment, monkeypatch, value):
    monkeypatch.setenv("NASIM_ENVIRONMENT", value)
    with pytest.raises(StageConfigurationError):
        load_stage_settings()


@pytest.mark.parametrize(
    "url",
    [
        "",
        "sqlite:///fallback.db",
        "postgresql://role:password@localhost/stage_validation",
        "postgresql://role:password@127.0.0.1/stage_validation",
        "postgresql://role:password@[::1]/stage_validation",
        "postgresql://role:password@host.docker.internal/stage_validation",
        "postgresql://role@postgres/stage_validation",
        "postgresql://role:password@postgres",
        "postgresql://nasim:nasim_dev_only@postgres/nasim_dev",
        "postgresql://nasim_app:nasim_app_dev_only@postgres/stage_validation",
        "postgresql://role:REPLACE_WITH_PASSWORD@postgres/stage_validation",
        "postgresql+psycopg://role:password@postgres/stage_validation",
    ],
)
def test_stage_rejects_incomplete_dev_or_placeholder_configuration(
    stage_environment, monkeypatch, url
):
    monkeypatch.setenv("NASIM_DATABASE_URL", url)
    with pytest.raises(StageConfigurationError):
        create_stage_app()


def test_stage_does_not_read_dotenv(stage_environment, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".env").write_text(f"NASIM_DATABASE_URL={RUNTIME}\nNASIM_ENVIRONMENT=stage\n")
    monkeypatch.delenv("NASIM_DATABASE_URL")
    with pytest.raises(StageConfigurationError):
        load_stage_settings()


def test_stage_configuration_error_does_not_disclose_credentials(stage_environment, monkeypatch):
    monkeypatch.setenv("NASIM_DATABASE_URL", "postgresql://role:SENSITIVE_TEST_VALUE@localhost/db")
    with pytest.raises(StageConfigurationError) as result:
        load_stage_settings()
    assert "SENSITIVE_TEST_VALUE" not in str(result.value)
    assert result.value.__suppress_context__


def test_stage_migration_roles_are_separate_and_same_database():
    settings = StageMigrationSettings.model_validate(
        {"environment": "stage", "database_url": RUNTIME, "migration_database_url": OWNER}
    )
    assert settings.database_url != settings.migration_database_url


@pytest.mark.parametrize(
    "owner",
    [
        RUNTIME,
        OWNER.replace("/stage_validation", "/different_database"),
        OWNER.replace("@postgres:", "@different-service:"),
    ],
)
def test_stage_migration_rejects_wrong_target_or_shared_role(owner):
    with pytest.raises(ValidationError):
        StageMigrationSettings.model_validate(
            {"environment": "stage", "database_url": RUNTIME, "migration_database_url": owner}
        )
