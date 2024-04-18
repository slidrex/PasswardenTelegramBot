from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram_dialog.widgets.kbd import ManagedCheckbox
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.kbd import Button
import random
from typing import Any
from dialog_states.pass_add_dialog_state import PasswordDialog

def get_pass(include_symbols: bool, length: int) -> str:
    return "`password `" + str(length) + " " + str(random.randint(1, 9)) + ("###" if include_symbols else "")

async def pass_get_data(dialog_manager: DialogManager,  **kwargs):
    ctx = dialog_manager.current_context()
    
    include_symbols = ctx.dialog_data.get("include_symbols")
    passw = get_pass(include_symbols, ctx.dialog_data.get("password_length"))
    
    ctx.dialog_data.update(entered_pass_password=passw)

    return {
        "pwd": passw,
    }



async def check_changed(event: ChatEvent, checkbox: ManagedCheckbox,
                        manager: DialogManager):
    ctx = manager.current_context()

    ctx.dialog_data.update( include_symbols=checkbox.is_checked() )





async def choose_8_passlen(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await change_pass_len(8, manager)

async def choose_16_passlen(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await change_pass_len(16, manager)

async def choose_32_passlen(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await change_pass_len(32, manager)

async def choose_64_passlen(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await change_pass_len(length=64, manager=manager)

async def change_pass_len(length: int, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(password_length= length)
    await manager.switch_to(PasswordDialog.pass_gen_menu)




async def on_pass_name_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    
    manager.dialog_data.update(entered_pass_name= data)
    
    await manager.switch_to(PasswordDialog.ask_pass_login)






async def on_pass_gen_clicked(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.switch_to(PasswordDialog.pass_gen_menu)

async def on_pass_manual_clicked(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.switch_to(PasswordDialog.ask_pass_password)



####
async def on_pass_name_edited(message: Message, widget: Any, manager: DialogManager, data: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(entered_pass_name=data)
    await manager.switch_to(PasswordDialog.confirm_pass_data)

async def on_pass_login_edited(message: Message, widget: Any, manager: DialogManager, data: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(entered_pass_login=data)
    await manager.switch_to(PasswordDialog.confirm_pass_data)
######
async def on_pass_login_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(entered_pass_login= data)
    await manager.switch_to(PasswordDialog.ask_pass_gen_way)

async def on_pass_manual_password_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    manager.dialog_data.update(entered_pass_password= data)
    await manager.switch_to(PasswordDialog.confirm_pass_data)

async def on_pass_way_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    await message.answer(data)
    await manager.switch_to(PasswordDialog.ask_pass_login)