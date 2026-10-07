from fastapi import FastAPI

from nasim.api.app import create_app
from nasim.infrastructure.stage_config import load_stage_settings


def create_stage_app() -> FastAPI:
    return create_app(load_stage_settings())
