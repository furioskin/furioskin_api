import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = f"sqlite+aiosqlite:////:memory"
    READER_DB_URL: str = f"mysql+aiomysql://root:password@localhost:3306/dongwon"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SDN: str = None
    CELERY_BROKER_URL: str = "amqp://user:bitnami@localhost:5672/"
    CELERY_BACKEND_URL: str = "redis://:password123@localhost:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


class DevelopmentConfig(Config):
    WRITER_DB_URL: str = f"sqlite+aiosqlite:///.dongwonfile"
    READER_DB_URL: str = f"sqlite+aiosqlite:///.dongwonfile"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379


class LocalConfig(Config):
    WRITER_DB_URL: str = f"sqlite+aiosqlite:///.dongwonfile"
    READER_DB_URL: str = f"sqlite+aiosqlite:///.dongwonfile"


class ProductionConfig(Config):
    DEBUG: str = False
    WRITER_DB_URL: str = f"sqlite+aiosqlite:///.dongwonfile"
    READER_DB_URL: str = f"sqlite+aiosqlite:///.dongwonfile"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
