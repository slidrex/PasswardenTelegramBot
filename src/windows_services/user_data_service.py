from aiogram.types import CallbackQuery
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import DialogManager
from core.repositories.user_data_repository import DeleteUser, UserDataRepository
from core.services.user_data_service import delete_user_data

async def delete_account_async(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    
    await delete_user_data(callback.from_user.id)
    await callback.message.delete()
    await manager.done()
    await callback.message.answer("Ваши данные были удалены из бота.")