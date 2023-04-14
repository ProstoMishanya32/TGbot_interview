# - *- coding: utf- 8 - *-
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, ChatPhoto
from aiogram.utils.exceptions import MessageCantBeDeleted
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from modules.utils import main_config, ded


from contextlib import suppress
from datetime import datetime, date

from bot_telegram import dp, bot
import pytz, os


@dp.message_handler(commands = ['start'], state = "*")
async def start(message: Message, state: FSMContext):


    files = os.listdir("./data/txt_dialogs/")
    for i in files:
        if f"{message.from_user.id}.txt" == i:
            with open(f"./data/txt_dialogs/{message.from_user.id}.txt", 'r', encoding="utf-8") as file:
                data = file.read()
                if "<✅>" == data[-3:]:
                    await message.answer(ded("""
                            Поздравляем! Ваша заявка одобрена! ✅

                            Вступайте в чат проекта ILLUMINATES Project:
                            https://t.me/+yfWbnLuL0r1jM2U0
                            
                            Перед началом работы обязательно ознакомьтесь с мануалом в закрепленном сообщение чата!
                            
                            Если у вас есть вопросы, вы можете задать их в чате, а так же в личном сообщение @illuminates_ts
                             
                            Для того, чтобы получить домен и админ панель, напишите администратору чата, он предоставит доступ.
                            
                            Желаем успехов!"""))

                elif "<❌>" == data[-3:]:
                    await message.answer(ded("""
                            Ваша заявка отклонена! ❌

                            Узнать причину отказа вы можете у @illuminates_ts
                            
                            Желаем успехов """))
                else:
                    await message.answer("Ваша заявка на рассмотрении ожидайте ответа!")
            return

    await state.finish()

    if message.from_user.username == None:
        await message.answer("Перед работой бота, укажите username в настройках. Это требуется для того, что с вами связались после опроса.")
    else:
        await message.answer("Здравствуйте, добро пожаловать в проект!")
        await message.answer("Есть ли ли у вас опыт работы?")
        await state.set_state("1_quest")

@dp.message_handler(state = "1_quest")
async def q_1(message: Message, state: FSMContext):
    now_time = datetime.now(pytz.timezone('Europe/Moscow')).time().replace(microsecond=0)
    async with state.proxy() as data:
        data['q_1'] = f"1) {now_time}: {message.text}"

    await message.answer("Откуда вы узнали о нас? Если нашли нас на форуме - предоставьте ссылку на форум.")
    await state.set_state("2_quest")

@dp.message_handler(state = "2_quest")
async def q_2(message: Message, state: FSMContext):
    now_time = datetime.now(pytz.timezone('Europe/Moscow')).time().replace(microsecond=0)
    async with state.proxy() as data:
        data['q_2'] = f"2) {now_time}: {message.text}"

    await message.answer("Сколько вам лет и какими языками вы владеете?")
    await state.set_state("3_quest")

@dp.message_handler(state = "3_quest")
async def q_3(message: Message, state: FSMContext):
    now_time = datetime.now(pytz.timezone('Europe/Moscow')).time().replace(microsecond=0)
    async with state.proxy() as data:
        data['q_3'] = f"3) {now_time}: {message.text}"
    write_text = f"--- Пользователь @{message.from_user.username} ---\n"
    for i in data:
        write_text += f"{data[i]}\n"

    user_file = open(f"./data/txt_dialogs/{message.from_user.id}.txt", "w", encoding = "utf-8")
    user_file.write(write_text)
    user_file.close()


    await message.answer("Ваша заявка отправлена на рассмотрение, пожалуйста ожидайте ответа в данном чате.")
    await bot.send_message(main_config.bot.main_admin, f"<b>Пользователь @{message.from_user.username} прошел опрос.</b> Его результаты\n\n{write_text}")
    await state.finish()


