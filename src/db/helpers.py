from peewee import Model, PrimaryKeyField

from settings import settings


class BaseModel(Model):
    """Base Model all database models"""

    _create_table = False
    _sub_classes: list[type[Model]] = []

    id = PrimaryKeyField()

    def __init_subclass__(cls) -> None:
        if cls._create_table:
            cls._sub_classes.append(cls)

    class Meta:
        database = settings.DB_OBJECT


class BaseIdModel(BaseModel):
    """The Base Model with id field"""

    _create_table = False

    id = PrimaryKeyField()
