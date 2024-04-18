from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram import F
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from typing import Any, Dict
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Cancel
from logging_master.api.base_inputs import log_support_response, write_support_message
from logging_master.logging_manager import ADMIN_ID

rt = Router()

class SupportState(StatesGroup):
    ADMIN_DIALOG = State()
    
    ENTER_SUPPORT_ANSWER = State()
    SUPPORT_RESPONSE_DIALOG = State()
    
    ADMIN_DIALOG_RESPONSE = State()
    RESPONSE_CONFIRM_INFO = State()
    


async def on_support_write_click(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.start(SupportState.SUPPORT_DIALOG)


def get_support_message_window():
    return Window(
        Const("Enter response text: "),
        TextInput(id="support_response_text_input", on_success=on_support_response_enterred),

        state=SupportState.SUPPORT_RESPONSE_DIALOG
    )
def get_admin_dialog_window():
    return Window(
        Const("Admin panel"),
        Button(Const("Answer question"), id="answer_support", on_click=on_support_response_click),
        Cancel(Const("<-- Close -->"), on_click=on_admin_panel_close),
        state = SupportState.ADMIN_DIALOG
)

def get_support_text_window():
    return Window(
            Const("Enter chat id and response message: (  3482937 Hello! It's PasswardenSupport... )"),
            TextInput(id="answer_support_input", on_success=on_support_response_enterred),
            Cancel(Const("<< Back")),

            state = SupportState.ADMIN_DIALOG_RESPONSE
    )

async def on_admin_panel_close(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await callback.message.delete()

def get_response_confirm_window():

    return Window(Format('''
           <b>Support Response</b>

ChatID: {dialog_data[support_chat_id]}
Message: {dialog_data[support_message]}
    '''
    ),
    Button(Const("Confirm"), id="confirm_support_response", on_click=send_support_response),
    Cancel(Const("Reject")),
    state=SupportState.RESPONSE_CONFIRM_INFO
    )

async def send_support_response(callback: CallbackQuery, button: Button, manager: DialogManager):
    

    await callback.message.delete()
    await callback.message.answer(text="Response sent.")
    await write_support_message(int(manager.dialog_data["support_chat_id"]), manager.dialog_data["support_message"])
    await manager.done()

@rt.message(F.text == "adminpanel")
async def answer_handler(message: Message, dialog_manager: DialogManager, state: FSMContext):
    
    if message.from_user.id == int(ADMIN_ID):
        await dialog_manager.start(SupportState.ADMIN_DIALOG)
    
        
async def on_support_response_click(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.start(SupportState.ADMIN_DIALOG_RESPONSE)


async def on_support_response_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
        
    ops = data.split(' ')
    chat_id = ops[0]
    del ops[0]
    if str(chat_id).isdigit() and len(ops) > 0:
        
        msg = ' '.join(ops)
        manager.dialog_data["support_chat_id"] = chat_id
        manager.dialog_data["support_message"] = msg
        await manager.next()



rt.include_router(Dialog(get_admin_dialog_window(), get_support_message_window(), get_support_text_window(), get_response_confirm_window()))