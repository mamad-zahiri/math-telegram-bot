from src.auth.utils import authenticate
from src.db.models import User


def login(student_id: int, password: str) -> bool:
    user = User.get(student_id=student_id)
    return authenticate(user, password)
