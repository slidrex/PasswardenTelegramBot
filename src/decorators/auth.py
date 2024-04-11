from aiogram.types import Message
from aiogram.types import CallbackQuery
from keyboards.pin_board import get_pin_markup

def auth_required(func):
    async def inner1(message: Message,*args, **kwargs):
        is_authenticated = False

        if not is_authenticated:
            await message.answer(text="Введите PIN:", reply_markup=get_pin_markup())
            return

        return await func(*args, **kwargs)
    return inner1
