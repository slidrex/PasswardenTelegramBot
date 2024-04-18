from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram_dialog import Dialog, DialogManager
from logging_master.logging_manager import ADMIN_ID
from dialog_states.admin_panel_state import AdminState
from aiogram.types import Message
from windows.admin_panel_windows import get_admin_dialog_window
from windows.admin_support_windows import get_response_confirm_window, get_support_message_window, get_support_text_window


rt = Router()
    

@rt.message(F.text == "adminpanel")
async def answer_handler(message: Message, dialog_manager: DialogManager, state: FSMContext):
    
    if message.from_user.id == int(ADMIN_ID):
        await dialog_manager.start(AdminState.ADMIN_DIALOG)
    


rt.include_router(Dialog(
                        get_admin_dialog_window(), 
                        get_support_message_window(), 
                        get_support_text_window(), 
                        get_response_confirm_window()))