import sys

from loguru import logger
from pydantic import BaseSettings, ValidationError


class Settings(BaseSettings):
    """Model for service settings."""

    ml_service_url: str

    class Config:  # NOQA
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    """Envs validation.
    @return [Settings]: Settings model
    """
    try:
        Settings()
    except ValidationError:
        logger.critical("Envs were set incorrectly !")
        sys.exit(0)
    logger.info("Envs are correct !")
    logger.info(f"Received envs {Settings()}")
    return Settings()
