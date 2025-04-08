from settings import settings
from src.db.helpers import BaseModel


def create_tables() -> None:
    with settings.DB_OBJECT as db:
        db.create_tables(BaseModel._sub_classes)
