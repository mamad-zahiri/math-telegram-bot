from hashlib import sha256

from settings import settings
from src.db.models import User


def set_password(user: User, password: str) -> None:
    salted_password = settings.ENCRYPTION_KEY + password
    user.password = sha256(salted_password.encode()).hexdigest()  # type: ignore
    user.save()


def authenticate(user: User, password: str) -> bool:
    salted_password = settings.ENCRYPTION_KEY + password
    hashed_password = sha256(salted_password.encode()).hexdigest()

    is_authenticated = user.password == hashed_password
    is_admin = user.type == User.Type.ADMIN
    is_owner = user.type == User.Type.OWNER

    return is_authenticated and (is_admin or is_owner)  # type: ignore
