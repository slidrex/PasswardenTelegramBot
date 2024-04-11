'''
from aiogram.types import Message
from keyboards.pin_board import markup
from keyboards.pin_board import rt as pin_router
from aiogram.types import CallbackQuery
from aiogram import Router
from aiogram import F

is_authenticated = False


rt = Router()
rt.include_router(pin_router)

def auth_required(func):
    async def inner1(*args, **kwargs):
        message = None
        for arg in args:
            if isinstance(arg, Message):
                message = arg
                break
        
        if message is None:
            raise ValueError("Message argument not found in function call")
        
        if not is_authenticated:
            await message.answer(text="Введите PIN:", reply_markup=markup)
            return

        return await func(*args, **kwargs)
    
    return inner1

@rt.callback_query(F.data == "enter_pin")
async def validate_pin(callback: CallbackQuery):
    global is_authenticated
    pin = callback.message.text

    if pin == '123456':
        await callback.message.answer(text="Authenticated.")
        is_authenticated = True
    else:
        await callback.message.edit_text(text="Incorrect pin!", reply_markup=markup)
        
'''