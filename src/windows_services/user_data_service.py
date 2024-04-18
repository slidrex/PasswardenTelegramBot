from aiogram.types import CallbackQuery
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import DialogManager


async def delete_account_async(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    
    await callback.message.delete()
    await manager.done()
    await callback.message.answer("Ваши данные были удалены из бота.")