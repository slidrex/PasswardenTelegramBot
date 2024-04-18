from dialog_states.admin_panel_state import AdminState
from aiogram_dialog.widgets.kbd import Button
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager


async def on_admin_panel_close(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.start(AdminState.ADMIN_DIALOG_RESPONSE)