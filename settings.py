from pathlib import Path
from typing import Annotated

from peewee import Database, SqliteDatabase
from pydantic import PlainValidator
from pydantic_settings import BaseSettings, SettingsConfigDict
from telebot.util import validate_token

BASE_DIR = Path(__name__).resolve().absolute()

DB_CLASS = SqliteDatabase


def _validate_token(token: str) -> str:
    validate_token(token)
    return token


class Settings(BaseSettings, case_sensitive=False):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
    )

    BOT_TOKEN: Annotated[str | None, PlainValidator(_validate_token)] = None
    ENCRYPTION_KEY: str
    DB_CLASS: type[Database] = DB_CLASS
    DB_NAME: str
    __DB_OBJECT: Database | None = None

    @property
    def DB_OBJECT(self) -> Database:  # noqa: N802
        if self.__DB_OBJECT is None:
            self.__DB_OBJECT = self.DB_CLASS(self.DB_NAME)

        return self.__DB_OBJECT


settings = Settings()  # type: ignore [call-arg]
