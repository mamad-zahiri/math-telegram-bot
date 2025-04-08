from peewee import DoesNotExist

from src.db.models import User
from src.error_codes.db import UserErrCode


def get_user(student_id: int) -> User | UserErrCode:
    try:
        return User.get(student_id=student_id)
    except DoesNotExist:
        return UserErrCode.USER_DOES_NOT_EXIST


def register_student(user: User) -> User | UserErrCode:
    user.type = User.Type.STUDENT
    try:
        User.get(phone=user.phone)
        return UserErrCode.USER_EXIST
    except DoesNotExist:
        user.save()
        return user


def downgrade_to_student(student_id: int) -> User | UserErrCode:
    try:
        user = User.get(student_id=student_id)
        user.type = User.Type.STUDENT
        user.save()
        return user
    except DoesNotExist:
        return UserErrCode.USER_EXIST


def upgrade_to_admin(student_id: int) -> User | UserErrCode:
    try:
        user = User.get(student_id=student_id)
        user.type = User.Type.ADMIN
        user.save()
        return user
    except DoesNotExist:
        return UserErrCode.USER_EXIST
