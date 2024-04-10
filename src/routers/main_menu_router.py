from aiogram import Router
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from html_messages import start, about
from aiogram import F

from aiogram.utils.keyboard import InlineKeyboardBuilder

from .security_guide_router import rt as security_router
from .security_guide_router import (
    SECURITY_GUIDE_PREFIX,
    SecurityOptions
)
SOURCE_CODE_BOT_URI = "https://github.com/slidrex/passwarden-bot" 

from keyboards.main_keyboard import (
    get_main_markup,
    ButtonText
)

rt = Router(name=__name__)
rt.include_router(security_router)

@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    
    
    await message.answer(text= start.START_MESSAGE, reply_markup=get_main_markup())

@rt.message(F.text == ButtonText.INFO)
async def about_handler(message: Message) -> None:

    builder = InlineKeyboardBuilder()
    builder.button(text="Github (Bot)", url=SOURCE_CODE_BOT_URI)
    builder.button(text="Справка по безопасности", callback_data="security_info")

    await message.answer(text= about.MESSAGE, reply_markup=builder.as_markup())

@rt.callback_query(F.data == "security_info")
async def security_info_handler(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.button(text="Ручная установка пароля", callback_data=f"{SECURITY_GUIDE_PREFIX}{SecurityOptions.MANUAL_PASS}")
    builder.button(text="Генерация пароля", callback_data=f"{SECURITY_GUIDE_PREFIX}{SecurityOptions.GEN_PASS}")
    builder.button(text="Файловые менеджеры паролей", callback_data=f"{SECURITY_GUIDE_PREFIX}{SecurityOptions.FILE_MANAGER}")
    builder.button(text="Облачные менеджеры паролей", callback_data=f"{SECURITY_GUIDE_PREFIX}{SecurityOptions.CLOUD_MANAGER}")
    builder.button(text="Дополнительные средства защиты (Обновления паролей, 2FA)", callback_data=f"{SECURITY_GUIDE_PREFIX}{SecurityOptions.GENERAL_INFO}")

    await message.answer(text="Справка по безопасности:\n", reply_markup=builder.as_markup())

@rt.message(F.text == ButtonText.CREATE_PASS)
async def create_pass_handler(message: Message) -> None:
    await message.answer(text= about.MESSAGE)

@rt.message(F.text == ButtonText.VIEW_PASS)
async def view_pass_handler(message: Message) -> None:
    await message.answer(text= about.MESSAGE)

@rt.message(F.text == ButtonText.SETTINGS)
async def settings_handler(message: Message) -> None:
    await message.answer(text= about.MESSAGE)