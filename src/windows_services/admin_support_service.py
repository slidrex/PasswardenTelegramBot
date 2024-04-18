from dialog_states.admin_panel_state import AdminState
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from typing import Any
from aiogram.types import CallbackQuery, Message
from logging_master.api.base_inputs import write_support_message


async def on_support_write_click(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.start(AdminState.SUPPORT_DIALOG)

async def on_support_response_click(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.start(AdminState.ADMIN_DIALOG_RESPONSE)


async def on_support_response_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
        
    ops = data.split(' ')
    chat_id = ops[0]
    del ops[0]
    if str(chat_id).isdigit() and len(ops) > 0:
        
        msg = ' '.join(ops)
        manager.dialog_data["support_chat_id"] = chat_id
        manager.dialog_data["support_message"] = msg
        await manager.next()

async def send_support_response(callback: CallbackQuery, button: Button, manager: DialogManager):
    

    await callback.message.delete()
    await callback.message.answer(text="Response sent.")
    await write_support_message(int(manager.dialog_data["support_chat_id"]), manager.dialog_data["support_message"])
    await manager.done()