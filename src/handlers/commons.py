from telebot import TeleBot
from telebot.storage import StatePickleStorage

from settings import settings

state_storage = StatePickleStorage(file_path="./state.pkl")

bot = TeleBot(
    settings.BOT_TOKEN,
    state_storage=state_storage,
    use_class_middlewares=True,
)
