from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo
from dialog_states.settings_states import SettingsState
from windows_services.settings_getter import is_has_pin, has_no_pin

def get_settings_layout():
    
    return Window(
        Const("Настройки"),
        SwitchTo(Const('Написать в поддержку'), id="write_support", state=SettingsState.SUPPORT_DIALOG),
        SwitchTo(Const('Удалить данные'), id="delete_data", state=SettingsState.DeleteData),

        Button(Const('Удалить PIN'), id="write_support", when=is_has_pin),
        Button(Const('Изменить PIN'), id="write_support", when=is_has_pin),

        Button(Const('Добавить PIN'), id="write_support", when=has_no_pin),
        state=SettingsState.SEETINGS_DIALOG
    )