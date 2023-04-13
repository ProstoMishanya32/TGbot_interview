from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton as ikb

from modules.utils import main_config



def sussecfully_opros(id_txt):
    keyboard = InlineKeyboardMarkup(
    ).add(
        ikb("❌", callback_data=f"opros:❌:{id_txt}")
    ).insert(
        ikb("✅", callback_data=f"opros:✅:{id_txt}")

    )
    return keyboard