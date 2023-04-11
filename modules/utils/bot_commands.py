# - *- coding: utf- 8 - *-
from aiogram import Dispatcher
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault
from modules.utils import main_config


user_commands = [
    BotCommand("start", "♻ Перезапустить бота"),
]

admin_commands = [
    BotCommand("start", "♻ Перезапустить бота"),
    BotCommand("admin", "Админ меню")
]

# Установка команд
async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(user_commands, scope=BotCommandScopeDefault())
    await dp.bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=main_config.bot.main_admin))
