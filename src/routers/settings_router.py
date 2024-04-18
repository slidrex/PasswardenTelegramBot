from aiogram import Router
from aiogram import F
from aiogram.filters.state import StatesGroup, State
from typing import Any, Dict
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from logging_master.api.base_inputs import log_support_response
from aiogram_dialog.widgets.common import Whenable
from .support_router import rt as sport_router
from .support_router import on_support_write_click
from .settings_states import SettingsState
from aiogram_dialog.widgets.kbd import SwitchTo
from .user_data_router import rt as data_router
from .user_data_router import get_delete_data_window
rt = Router(name=__name__)






def is_has_pin(data: Dict, widget: Whenable, manager: DialogManager):
    return False
def has_no_pin(data: Dict, widget: Whenable, manager: DialogManager):
    return not is_has_pin(data, widget, manager)

def get_settings_layout():
    
    return Window(
        Const("Настройки"),
        Button(Const('Написать в поддержку'), id="write_support", on_click=on_support_write_click),
        SwitchTo(Const('Удалить данные'), id="delete_data", state=SettingsState.DeleteData),

        Button(Const('Удалить PIN'), id="write_support", when=is_has_pin),
        Button(Const('Изменить PIN'), id="write_support", when=is_has_pin),

        Button(Const('Добавить PIN'), id="write_support", when=has_no_pin),
        state=SettingsState.SEETINGS_DIALOG
    )
rt.include_router(sport_router)
rt.include_router(data_router)
rt.include_router(Dialog(get_settings_layout(), get_delete_data_window()))