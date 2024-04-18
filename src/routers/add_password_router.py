from aiogram.types import Message
from aiogram import F
from aiogram.types import CallbackQuery

from aiogram_dialog.widgets.kbd import Checkbox, ManagedCheckbox
from aiogram_dialog.widgets.text import Const

from aiogram_dialog import DialogManager, ChatEvent

import random


from typing import Any


from aiogram_dialog.widgets.input import TextInput


from aiogram_dialog.widgets.kbd import Button, SwitchTo

from aiogram_dialog.widgets.text import Const, Format
from dialog_states.pass_add_dialog_state import PasswordDialog
from aiogram_dialog.widgets.kbd import Cancel, Row, Back, Next
from aiogram import Router

from aiogram_dialog import (
    Dialog, DialogManager, StartMode, Window,
)

rt = Router(name=__name__)




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

def input_pass_name_window():
    return Window(
        Const('Введите название пароля: (чтобы знать от чего пароль)'),
        TextInput(id='name', on_success=on_pass_name_enterred),
        Cancel(Const("Отменить")),
        state=PasswordDialog.ask_pass_name
    )

async def check_changed(event: ChatEvent, checkbox: ManagedCheckbox,
                        manager: DialogManager):
    ctx = manager.current_context()

    ctx.dialog_data.update( include_symbols=checkbox.is_checked() )


def input_pass_gen_window():
    return Window(
        Format('{pwd}'),
        SwitchTo(Const("Взять пароль"), id="take_pass", state=PasswordDialog.confirm_pass_data),
        Row(
            Checkbox(default=False, on_state_changed=check_changed, checked_text=Const("Символы ✅"), unchecked_text=Const("Символы ❌"), id="include_symbols"),
                    SwitchTo(Const("Изменить длину"), id="change_len", state=PasswordDialog.choose_passlen_win),
        ),
        
        Button(Const("Сгенерировать новый"), id="gen_new"),
        state=PasswordDialog.pass_gen_menu,
        getter=pass_get_data
    )


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

def get_change_pass_len_window():
    return Window(
        Const("Выберите длину пароля"),
        Row(
            Button(Const("8"), id="choose_8_passlen", on_click=choose_8_passlen),
            Button(Const("16"), id="choose_16_passlen", on_click=choose_16_passlen),
            Button(Const("32"), id="choose_32_passlen", on_click=choose_32_passlen),
            Button(Const("64"), id="choose_64_passlen", on_click=choose_64_passlen)
        ),
        Back(Const("<< Назад")),
        Cancel(Const("<-- Закрыть -->")),

        state=PasswordDialog.choose_passlen_win
    )



async def on_pass_name_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    
    manager.dialog_data.update(entered_pass_name= data)
    
    await manager.switch_to(PasswordDialog.ask_pass_login)



def input_pass_login_window():
    return Window(
        Const('Введите логин:'),
        TextInput(id='login', on_success=on_pass_login_enterred),
        Cancel(Const("Отменить")),
        state=PasswordDialog.ask_pass_login
    )
def input_pass_password_window():
    return Window(
        Const('Введите пароль:'),
        TextInput(id='pass_pwd', on_success=on_pass_manual_password_enterred),
        Cancel(Const("Отменить")),
        state=PasswordDialog.ask_pass_password
    )
def pass_data_confirmed_win():
    return Window(
        Const("Новый пароль добавлен!"),
        state=PasswordDialog.pass_data_confirmed
    )

def input_pass_choose_window():
    return Window(
        Const('Введите способ создания пароля:'),
        Button(Const("Ввести вручную"), id="manual_pass_enter", on_click=on_pass_manual_clicked),
        Button(Const("Сгенерировать"), id="get_pass_enter", on_click=on_pass_gen_clicked),
        state=PasswordDialog.ask_pass_gen_way
    )



async def on_pass_gen_clicked(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.switch_to(PasswordDialog.pass_gen_menu)

async def on_pass_manual_clicked(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await manager.switch_to(PasswordDialog.ask_pass_password)


def get_pass_data_confirm_window():
    
    return Window(
        Format('''
Your enterred data:
               
Name: {dialog_data[entered_pass_name]}
Login: {dialog_data[entered_pass_login]}
Password: {dialog_data[entered_pass_password]}
               
Is it correct?
'''
    ),
    Next(Const("Продолжить ✅"), id="pass_confirmation_continue"),
    Cancel(Const("<-- Закрыть -->"), id="pass_confirmation_btn"),
    SwitchTo(Const("⚙️ Изменить имя"), id="pass_confirmation_change_name", state=PasswordDialog.edit_name),
    SwitchTo(Const("⚙️ Изменить логин"), id="pass_confirmation_change_login", state=PasswordDialog.edit_login),
    SwitchTo(Const("⚙️ Изменить пароль"), id="pass_confirmation_change_pass", state=PasswordDialog.ask_pass_gen_way),
    state=PasswordDialog.confirm_pass_data
    )
def edit_name_window():
    return Window(
        Const("Введите имя пароля: "),
        TextInput(id="edit_name_win", on_success=on_pass_name_edited),
        state=PasswordDialog.edit_name
    )
def edit_login_window():
    return Window(
        Const("Введите имя пароля: "),
        TextInput(id="edit_login_win", on_success=on_pass_login_edited),
        state=PasswordDialog.edit_login
    )
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


rt.include_router(Dialog(input_pass_name_window(), 
                         input_pass_gen_window(), 
                         input_pass_choose_window(), 
                         input_pass_login_window(),
                         get_change_pass_len_window(),
                         input_pass_password_window(),
                         get_pass_data_confirm_window(),
                         pass_data_confirmed_win(),
                         edit_name_window(),
                         edit_login_window()
                         ))