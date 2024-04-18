from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo
from dialog_states.settings_states import SettingsState
from windows_services.user_data_service import delete_account_async

def get_delete_data_window():
    return Window(
        Const("Вы собираетесь удалить свои данные. Продолжить?"),
        Button(Const("Да"), id="delete_account_continue", on_click=delete_account_async),
        SwitchTo(Const("Нет"), id="delete_account_abort", state=SettingsState.SEETINGS_DIALOG),
        state=SettingsState.DeleteData
    )