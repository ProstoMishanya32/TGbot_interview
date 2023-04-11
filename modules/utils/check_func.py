# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from modules.utils import main_config

class CheckAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if message.from_user.id == main_config.bot.main_admin:
            return True
        else:
            return False