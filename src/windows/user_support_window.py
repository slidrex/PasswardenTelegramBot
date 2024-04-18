from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Cancel
from dialog_states.settings_states import SettingsState
from windows_services.user_support_getter import on_support_written

def get_support_layout():

    return Window(
        Const('Напишите текст обращения к президенту: '),
        TextInput(id="support_write", on_success=on_support_written),
        Cancel(Const('Назад')),
        

        state=SettingsState.SUPPORT_DIALOG
    )