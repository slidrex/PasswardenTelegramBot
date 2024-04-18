from aiogram.types import Message
from logging_master.api.base_inputs import log_support_response
from dialog_states.settings_states import SettingsState
from aiogram_dialog import DialogManager
from typing import Any

async def on_support_written(message: Message, widget: Any, manager: DialogManager, data: str):
    await log_support_response(message.from_user.id, message.from_user.username, message.chat.id, message.text)
    await message.answer(text="Ваше обращение отправлено! Вам может быть ответят в течение этого года.")
    
    #send to president API call

    await manager.switch_to(state=SettingsState.SEETINGS_DIALOG)