from aiogram import Router
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from html_messages import start, about
from aiogram import F
from keyboards.main_keyboard import (
    get_main_markup,
    ButtonText
)

rt = Router(name=__name__)


@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    
    
    await message.answer(text= start.START_MESSAGE, reply_markup=get_main_markup())

@rt.message(F.text == ButtonText.INFO)
async def about_handler(message: Message) -> None:

    await message.answer(text= about.MESSAGE)

@rt.message(F.text == ButtonText.CREATE_PASS)
async def create_pass_handler(message: Message) -> None:
    await message.answer(text= about.MESSAGE)

@rt.message(F.text == ButtonText.VIEW_PASS)
async def view_pass_handler(message: Message) -> None:
    await message.answer(text= about.MESSAGE)

@rt.message(F.text == ButtonText.SETTINGS)
async def settings_handler(message: Message) -> None:
    await message.answer(text= about.MESSAGE)