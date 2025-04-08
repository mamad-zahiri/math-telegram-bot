from telebot import custom_filters
from telebot.states.sync.middleware import StateMiddleware

from src.db.utils import create_tables
from src.handlers.commons import bot
from src.handlers.login_handlers import *

if __name__ == "__main__":
    create_tables()

    # Add custom filters
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(custom_filters.IsDigitFilter())
    bot.add_custom_filter(custom_filters.TextMatchFilter())

    bot.setup_middleware(StateMiddleware(bot))

    bot.infinity_polling()
