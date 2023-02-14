"""
This is a test bot for the telegram bot api.
"""
from tools.telegram_bot import TelegramBot

bot = TelegramBot()
bot.async_look_for_updates()
