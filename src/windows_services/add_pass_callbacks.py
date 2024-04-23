from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram_dialog.widgets.kbd import ManagedCheckbox
from aiogram_dialog import DialogManager, ChatEvent
from aiogram_dialog.widgets.kbd import Button
import random
from typing import Any
from dialog_states.pass_add_dialog_state import PasswordDialog
from core.services.pass_generate_service import generate_pass
from core.services.pass_security_check_service import get_security_report
from core.repositories.password_repository import PasswordRepository, AddPassword
from core.repositories.user_data_repository import UserDataRepository, GetUser


def get_pass(include_symbols: bool, length: int) -> str:
    return generate_pass(length, include_symbols)

async def save_pass_click(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    ctx = manager.current_context()

    user_id = ctx.dialog_data.get("user_id")
    pass_name = ctx.dialog_data.get("entered_pass_name")
    pass_login = ctx.dialog_data.get("entered_pass_login")
    pass_pass = ctx.dialog_data.get("entered_pass_password")

    user = await UserDataRepository.get_user(GetUser(user_id=user_id))

    await PasswordRepository.add_pass(data=AddPassword(user_id=user.id, name=pass_name, login=pass_login, password=pass_pass))

async def pass_get_data(dialog_manager: DialogManager,  **kwargs):
    ctx = dialog_manager.current_context()
    
    include_symbols = ctx.dialog_data.get("include_symbols")
    data = ctx.dialog_data.get("password_length")
    if data == None:
        ctx.dialog_data.update(password_length=16)
        data = 16
    passw = get_pass(include_symbols, data).replace('`', '\\`').replace('}', '\\}')
    
    
    ctx.dialog_data.update(entered_pass_password=passw)
    
    return {
        "pwd": passw,
    }

async def get_password_security_report(dialog_manager: DialogManager,  **kwargs):
    ctx = dialog_manager.current_context()

    pwd = ctx.dialog_data.get("entered_pass_password")
    report = get_security_report(pwd)

    leak_message = f"Ваш пароль был найден в {report.leaked_count} утечках баз данных" if report.leaked_count > 0 else f"Пароль не был найден в утечках"

    return {"entropy": int(report.entropy), "leak" : leak_message, "leak_status" : report.status}


async def check_changed(event: ChatEvent, checkbox: ManagedCheckbox,
                        manager: DialogManager):
    ctx = manager.current_context()

    ctx.dialog_data.update( include_symbols=checkbox.is_checked() )





async def choose_8_passlen(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await change_pass_len(length=8, manager=manager)

async def choose_16_passlen(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await change_pass_len(length=16, manager=manager)

async def choose_32_passlen(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await change_pass_len(length=32, manager=manager)

async def choose_64_passlen(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await change_pass_len(length=64, manager=manager)

async def change_pass_len(length: int, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(password_length=length)
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
async def on_pass_manual_password_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    manager.dialog_data.update(entered_pass_password= data)
    await manager.switch_to(PasswordDialog.confirm_pass_data)
######
async def on_pass_login_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(user_id=message.from_user.id)
    ctx.dialog_data.update(entered_pass_login= data)
    await manager.switch_to(PasswordDialog.ask_pass_gen_way)


async def on_pass_way_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    await message.answer(data)
    await manager.switch_to(PasswordDialog.ask_pass_login)

