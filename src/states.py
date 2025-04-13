from telebot.states import State, StatesGroup


class AdminLoginState(StatesGroup):
    begin = State()
    enter_student_id = State()
    enter_password = State()


class NewCompetitionState(StatesGroup):
    begin = State()
    start_time_year_month_day_hour = State()
    end_time_year_month_day_hour = State()
    score_threshold = State()
    done = State()
