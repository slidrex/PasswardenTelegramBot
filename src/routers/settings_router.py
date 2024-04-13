from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from typing import Any, Dict
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Cancel, Row
from logging_master.api.base_inputs import log_support_response
from aiogram_dialog.widgets.common import Whenable
from logging_master.logging_manager import LOG_CHANNEL, ADMIN_ID, log_to_user
from aiogram.filters.callback_data import CallbackData
from .support_router import rt as sport_router
from .support_router import on_support_write_click
rt = Router(name=__name__)




class SettingsState(StatesGroup):
    INPUT_SUPPORT = State()
    SEETINGS_DIALOG = State()

def is_has_pin(data: Dict, widget: Whenable, manager: DialogManager):
    return False
def has_no_pin(data: Dict, widget: Whenable, manager: DialogManager):
    return not is_has_pin(data, widget, manager)

def get_settings_layout():
    
    return Window(
        Const("Настройки"),
        Button(Const('Написать в поддержку'), id="write_support", on_click=on_support_write_click),
        Button(Const('Удалить данные'), id="write_support"),

        Button(Const('Удалить PIN'), id="write_support", when=is_has_pin),
        Button(Const('Изменить PIN'), id="write_support", when=is_has_pin),

        Button(Const('Добавить PIN'), id="write_support", when=has_no_pin),
        state=SettingsState.SEETINGS_DIALOG
    )
rt.include_router(sport_router)
rt.include_router(Dialog(get_settings_layout()))