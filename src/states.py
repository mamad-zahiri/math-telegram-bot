from telebot.states import State, StatesGroup


class AdminLoginState(StatesGroup):
    begin = State()
    enter_student_id = State()
    enter_password = State()
