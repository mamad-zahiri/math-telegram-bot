from telebot.states.sync.context import StateContext
from telebot.types import Message

from src import states
from src.handlers.commons import bot


@bot.message_handler(commands=["newcompetition"])
def new_competition__begin(message: Message, state: StateContext) -> None:
    bot.send_message(message.chat.id, "شروع مسابفه جدید")
    msg = """سال ماه روز و ساعت شروع مسابقه کی باشه؟
فرمت ورودی به صورت سال ماه روز ساعت میباشد.
مثال:
1404 10 29 18
    """
    bot.send_message(message.chat.id, msg)

    state.set(states.NewCompetitionState.start_time_year_month_day_hour)


@bot.message_handler(state=[states.NewCompetitionState.start_time_year_month_day_hour])
def new_competition__start_ymdh(message: Message, state: StateContext) -> None:
    start_ymdh = list(map(int, message.text.split()))

    state.add_data(start=start_ymdh)
    msg = """سال ماه روز و ساعت پایان مسابقه کی باشه؟
فرمت ورودی به صورت سال ماه روز ساعت میباشد.
مثال:
1404 10 29 18
    """
    bot.send_message(message.chat.id, msg)

    state.set(states.NewCompetitionState.end_time_year_month_day_hour)


@bot.message_handler(state=[states.NewCompetitionState.end_time_year_month_day_hour])
def new_competition__end_ymdh(message: Message, state: StateContext) -> None:
    end_ymdh = list(map(int, message.text.split()))

    state.add_data(end=end_ymdh)
    msg = """حد امتیاز مسابقه چقدره؟
فرمت وروری به صورت عدد صحیح و لاتین میباشد.
مثال:
18
"""
    bot.send_message(message.chat.id, msg)

    state.set(states.NewCompetitionState.score_threshold)


@bot.message_handler(state=[states.NewCompetitionState.score_threshold])
def new_competition__score_threshold(message: Message, state: StateContext) -> None:
    with state.data() as data:
        start_ymdh = data["start"]
        end_ymdh = data["end"]
        score_threshold = int(message.text)

    msg = f"{start_ymdh} {end_ymdh} {score_threshold}"
    bot.send_message(message.chat.id, msg)

    state.delete()
