import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message, TelegramObject
from aiogram.types import Message
from keyboards.pin_board import markup
from keyboards.pin_board import rt as pin_router
from aiogram import flags
from aiogram.types import CallbackQuery
from aiogram import Router
from aiogram import F

logger = logging.getLogger(__name__)

rt = Router()
rt.include_router(pin_router)

is_authorized = True

class InstanceType():
    None_="none"
    Message="class"
    Callback="callback"



class AuthorizationMiddleware(BaseMiddleware):
    """
    Helps to check if user is authorized to use the bot
    """

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        instance_of = InstanceType.None_
        
        if isinstance(event, CallbackQuery):
            instance_of = InstanceType.Callback
        
        if isinstance(event, Message):
            instance_of = InstanceType.Message
        
        if instance_of == InstanceType.None_:
            return await handler(event, data)

        authorization = get_flag(data, "authorization")
        
        if is_authorized == False and not (authorization is not None and authorization.get("is_authorized") != None and authorization["is_authorized"] == True):
                
                if instance_of == InstanceType.Callback:

                    return await event.message.answer(text="Not authenticated", reply_markup=markup)
                else:
                    return await event.answer(text="Not authenticated", reply_markup=markup)
        else:
            return await handler(event, data)
        

@rt.message(F.text == "lock")
@flags.authorization(is_authorized=True)
async def lock_auth(callback: CallbackQuery):
    global is_authorized
    is_authorized = False

@rt.message(F.text == "unlock")
@flags.authorization(is_authorized=True)
async def unlock_auth(callback: CallbackQuery):
    global is_authorized
    is_authorized = True

@rt.callback_query(F.data == "enter_pin")
@flags.authorization(is_authorized=True)
async def validate_pin(callback: CallbackQuery):
    global is_authorized
    pin = callback.message.text

    if pin == '1234':
        await callback.message.answer(text="Authenticated.")
        is_authorized = True
    else:
        await callback.message.edit_text(text="Incorrect pin!", reply_markup=markup)
        