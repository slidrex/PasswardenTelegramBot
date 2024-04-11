from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from html_messages import start, about
from aiogram import F
from .settings_router import rt as settings_rt
from .settings_router import (
    get_settings_layout
)
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from decorators.auth import auth_required
from aiogram.utils.keyboard import InlineKeyboardBuilder
from .add_password_router import rt as add_pass_router

from .add_password_router import (
    AddPassword
)
from keyboards.pin_board import rt as pin_router



SOURCE_CODE_BOT_URI = "https://github.com/slidrex/passwarden-bot" 

from keyboards.main_keyboard import (
    get_main_markup,
    ButtonText
)

rt = Router(name=__name__)
rt.include_router(settings_rt)
rt.include_router(add_pass_router)
rt.include_router(pin_router)

@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    await message.answer(text= about.MESSAGE, reply_markup=get_main_markup())

@rt.message(F.text == ButtonText.INFO)
async def about_handler(message: Message) -> None:

    builder = InlineKeyboardBuilder()
    builder.button(text="Github (Bot)", url=SOURCE_CODE_BOT_URI)
    
    await message.answer(text= about.MESSAGE, reply_markup=builder.as_markup())

@rt.message(F.text == ButtonText.CREATE_PASS)
@auth_required
async def create_pass_handler(message: Message, state: FSMContext) -> None:
    await message.answer(text="Введите название пароля (чтобы знать от чего пароль)")
    await state.set_state(AddPassword.input_name)



@rt.message(F.text == ButtonText.VIEW_PASS)
@auth_required
async def view_pass_handler(message: Message) -> None:
    await message.answer(text= about.MESSAGE)


@rt.message(F.text == ButtonText.SETTINGS)
@auth_required
async def settings_handler(message: Message) -> None:

    await message.answer(text= "Настройки:", reply_markup=get_settings_layout(has_pin=True).as_markup())