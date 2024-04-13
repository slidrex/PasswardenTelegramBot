from aiogram import Router , flags
from aiogram.types import Message
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram_dialog.widgets.kbd import Checkbox, ManagedCheckbox
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import DialogManager, ChatEvent
from aiogram.filters.callback_data import CallbackData
import random
from typing import Any

from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Cancel, Row

from aiogram_dialog import (
    Dialog, DialogManager, StartMode, Window,
)

rt = Router(name=__name__)

INCLUDE_SYMBOLS = True

class PasswordDialog(StatesGroup):
    ask_pass_name = State()
    ask_pass_login = State()
    ask_pass_gen_way = State()
    ask_pass_password = State()
    pass_gen_menu = State()

    include_symbols = State()

def get_pass(include_symbols: bool, length: int) -> str:
    return "`password`" + str(random.randint(1, 9)) + ("###" if include_symbols else "")

async def pass_get_data(state: FSMContext, **kwargs):
    return {
        "pwd": get_pass(INCLUDE_SYMBOLS, 16),
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
    global INCLUDE_SYMBOLS

    INCLUDE_SYMBOLS = checkbox.is_checked()




def input_pass_gen_window():
    return Window(
        Format('{pwd}'),
        Button(Const("Взять пароль"), id="take_pass"),
        Row(
            Checkbox(default=INCLUDE_SYMBOLS, on_state_changed=check_changed, checked_text=Const("Символы ✅"), unchecked_text=Const("Символы ❌"), id="include_symbols"),
                    Button(Const("Изменить длину"), id="change_len"),
        ),
        
        Button(Const("Сгенерировать новый"), id="gen_new"),
        state=PasswordDialog.pass_gen_menu,
        getter=pass_get_data
    )

async def on_pass_name_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    await message.answer(text=data)
    await manager.start(PasswordDialog.ask_pass_login, mode=StartMode.RESET_STACK)



def input_pass_login_window():
    return Window(
        Const('Введите логин:'),
        TextInput(id='login', on_success=on_pass_login_enterred),
        Cancel(Const("Отменить")),
        state=PasswordDialog.ask_pass_login
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
    await callback.message.answer("Going on!")

async def on_pass_manual_clicked(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await callback.message.answer("Going on!")


async def on_pass_login_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    await manager.start(PasswordDialog.ask_pass_gen_way, mode=StartMode.RESET_STACK)

async def on_pass_way_enterred(message: Message, widget: Any, manager: DialogManager, data: str):
    await message.answer(data)
    await manager.start(PasswordDialog.ask_pass_login, mode=StartMode.RESET_STACK)


rt.include_router(Dialog(input_pass_name_window(), 
                         input_pass_gen_window(), 
                         input_pass_choose_window(), 
                         input_pass_login_window()))