from pydantic import Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="NASIM_", extra="ignore")
    database_url: PostgresDsn = Field(...)

    @property
    def async_url(self) -> str:
        return str(self.database_url).replace("postgresql://", "postgresql+asyncpg://", 1)


def load_settings() -> Settings:
    # BaseSettings custom initialization resolves NASIM_* variables during validation.
    # model_validate also avoids a false static required-field error for environment loading.
    return Settings.model_validate({})
