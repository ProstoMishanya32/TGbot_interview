# - *- coding: utf- 8 - *-
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ChatPhoto
from aiogram.utils.exceptions import MessageCantBeDeleted
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.markdown import hlink

from modules.utils import main_config
from modules.utils.check_func import CheckAdmin

from contextlib import suppress
from datetime import datetime, date

from bot_telegram import dp
import os


@dp.message_handler(CheckAdmin(), commands = ['admin'], state = "*")
async def start(message: Message, state: FSMContext):
    await state.finish()

    files = os.listdir("./data/txt_dialogs/")

    await message.answer(f"<b>Всего опрос прошло <code>{len(files)}</code> ч.</b>")
    message_text = ''
    for i, name_files in enumerate(files, 1):
        user_id = name_files.replace(".txt", "")

        with open(f"./data/txt_dialogs/{name_files}", 'r', encoding="utf-8") as file:
            data = file.read()
            data = data.split(" ")
            user_username = [row for row in data if row.startswith("@")][0]

        message_text += f"{i}. {user_username} - <code>{user_id}</code>\n"

    await message.answer(f"<i>Для открытия диалога с пользоваталем, введите его ID.</i>\n\n{message_text}")
    await state.set_state("waiting_id")




@dp.message_handler(CheckAdmin(), state = "waiting_id")
async def get_dialogs(message: Message, state: FSMContext):
    await state.finish()
    try:
        user_id = int(message.text)
    except ValueError:
        await message.answer("<b>ID должен быть числом</b>")

    files = os.listdir("./data/txt_dialogs/")
    if f"{message.text}.txt" in files:
        with open(f"./data/txt_dialogs/{message.text}.txt", 'r', encoding="utf-8") as file:
            data = file.read()
            await message.answer(data)

    else:
        await message.answer("<b> ID не найден </b>")



