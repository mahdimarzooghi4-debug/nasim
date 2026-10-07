"""Explicit, environment-only Stage configuration. No development fallbacks."""

import ipaddress
from urllib.parse import unquote

from pydantic import PostgresDsn, ValidationError, field_validator, model_validator
from pydantic_settings import SettingsConfigDict

from nasim.infrastructure.config import Settings


def validate_stage_database(url: PostgresDsn) -> PostgresDsn:
    hosts = url.hosts()
    if url.scheme not in {"postgresql", "postgresql+asyncpg"} or len(hosts) != 1:
        raise ValueError("A single PostgreSQL asyncpg destination is required")
    host = hosts[0]
    hostname = host["host"]
    if not hostname:
        raise ValueError("Stage database hostname is required")
    hostname = hostname.strip("[]")
    if hostname.lower() in {"localhost", "host.docker.internal"}:
        raise ValueError("Stage database must be explicitly addressed outside loopback")
    try:
        loopback = ipaddress.ip_address(hostname).is_loopback
    except ValueError:
        loopback = False
    if loopback:
        raise ValueError("Stage database must be explicitly addressed outside loopback")
    values = [host.get("username"), host.get("password"), url.path]
    if any(not value or not value.strip("/") for value in values):
        raise ValueError("Database identity, password and database name are required")
    for value in values:
        decoded = unquote(str(value))
        if "REPLACE_" in decoded.upper() or "CHANGE_ME" in decoded.upper() or "<" in decoded:
            raise ValueError("Example placeholders must be replaced by external inputs")
        if decoded in {"nasim_dev_only", "nasim_app_dev_only", "/nasim_dev", "/nasim_test"}:
            raise ValueError("Development configuration is not a Stage configuration")
    return url


class StageSettings(Settings):
    model_config = SettingsConfigDict(
        env_prefix="NASIM_", extra="ignore", env_file=None, hide_input_in_errors=True
    )
    # Required explicitly even though the Stage factory itself is an explicit entry point.
    environment: str

    @field_validator("environment")
    @classmethod
    def stage_only(cls, value: str) -> str:
        if value != "stage":
            raise ValueError("NASIM_ENVIRONMENT must explicitly select stage")
        return value

    @field_validator("database_url")
    @classmethod
    def stage_database(cls, value: PostgresDsn) -> PostgresDsn:
        return validate_stage_database(value)


class StageMigrationSettings(StageSettings):
    migration_database_url: PostgresDsn

    @field_validator("migration_database_url")
    @classmethod
    def migration_database(cls, value: PostgresDsn) -> PostgresDsn:
        return validate_stage_database(value)

    @model_validator(mode="after")
    def distinct_roles_same_database(self) -> "StageMigrationSettings":
        app_host = self.database_url.hosts()[0]
        migration_host = self.migration_database_url.hosts()[0]
        if (
            app_host["host"] != migration_host["host"]
            or (app_host.get("port") or 5432) != (migration_host.get("port") or 5432)
            or self.database_url.path != self.migration_database_url.path
            or app_host.get("username") == migration_host.get("username")
        ):
            raise ValueError("Migration and runtime require distinct roles in the same database")
        return self


class StageConfigurationError(RuntimeError):
    pass


def load_stage_settings() -> StageSettings:
    try:
        return StageSettings.model_validate({})
    except ValidationError:
        raise StageConfigurationError(
            "Incomplete or invalid Stage environment configuration"
        ) from None


def load_stage_migration_settings() -> StageMigrationSettings:
    try:
        return StageMigrationSettings.model_validate({})
    except ValidationError:
        raise StageConfigurationError(
            "Incomplete or invalid Stage migration configuration"
        ) from None
