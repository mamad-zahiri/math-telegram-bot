from choice_enum import ChoiceEnumeration, Option


class UserErrCode(ChoiceEnumeration):
    USER_EXIST = Option("User already exists")
    USER_DOES_NOT_EXIST = Option("User does not exit")

    ONLY_ADMINS = Option("You don't have permission to do this")
    ONLY_OWNERS = Option("You don't have permission to do this")
