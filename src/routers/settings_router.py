from aiogram import Router
from aiogram.types import Message
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

rt = Router(name=__name__)

def get_settings_layout(has_pin: bool):
    builder = InlineKeyboardBuilder()
    builder.button(text="Язык: Русский 🇺🇦", callback_data="s")
    builder.button(text="Удалить данные", callback_data="s")
    if has_pin:
        builder.button(text="Удалить PIN", callback_data="s")
        builder.button(text="Изменить PIN", callback_data="s")
    else:
        builder.button(text="Добавить PIN", callback_data="s")
    builder.adjust(1, 1)
    return builder
