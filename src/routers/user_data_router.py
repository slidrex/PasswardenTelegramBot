from aiogram.types import Message, CallbackQuery
from aiogram import F
from typing import Any, Dict
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram.filters.state import StatesGroup, State
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram import Router
from dialog_states.settings_states import SettingsState

def get_delete_data_window():
    return Window(
        Const("Вы собираетесь удалить свои данные. Продолжить?"),
        Button(Const("Да"), id="delete_account_continue", on_click=delete_account_async),
        SwitchTo(Const("Нет"), id="delete_account_abort", state=SettingsState.SEETINGS_DIALOG),
        state=SettingsState.DeleteData
    )
async def delete_account_async(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await callback.message.delete()
    await manager.done()
    await callback.message.answer("Ваши данные были удалены из бота.")

    #Delete data API call