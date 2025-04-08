from telebot.states.sync.context import StateContext
from telebot.types import Message

from src import states
from src.auth.utils import authenticate
from src.db.models import User
from src.handlers.commons import bot


@bot.message_handler(commands=["login"])
def login__begin(message: Message, state: StateContext) -> None:
    state.set(states.AdminLoginState.enter_student_id)

    bot.send_message(message.chat.id, "ok, you wanna login")
    bot.send_message(message.chat.id, "enter student id:")


@bot.message_handler(state=states.AdminLoginState.enter_student_id)
def login__username(message: Message, state: StateContext) -> None:
    state.add_data(student_id=message.text)
    state.set(states.AdminLoginState.enter_password)

    bot.send_message(message.chat.id, "enter password:")


@bot.message_handler(state=states.AdminLoginState.enter_password)
def login__finish(message: Message, state: StateContext) -> None:
    with state.data() as data:
        student_id = data.get("student_id")
        password = message.text

    state.delete()
    user = User.get(student_id=student_id)
    isa = authenticate(user, password)
    bot.send_message(message.chat.id, f"{student_id} {password}")
    bot.send_message(message.chat.id, f"{isa}")
