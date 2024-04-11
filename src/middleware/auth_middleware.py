import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message, TelegramObject
from aiogram.types import Message
from keyboards.pin_board import markup
from keyboards.pin_board import rt as pin_router
from aiogram.types import CallbackQuery
from aiogram import Router
from aiogram import F

logger = logging.getLogger(__name__)

rt = Router()
rt.include_router(pin_router)

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
        if not isinstance(event, Message):
            return await handler(event, data)

        authorization = get_flag(data, "authorization")
        print("Authorization: ", authorization)
        if authorization is not None:
            if authorization["is_authorized"] == False:
                    return await event.answer(text="Not authenticated", reply_markup=markup)
            else:
                return await handler(event, data)
        else:
            return await handler(event, data)





@rt.callback_query(F.data == "enter_pin")
async def validate_pin(callback: CallbackQuery):
    global is_authenticated
    pin = callback.message.text

    if pin == '123456':
        await callback.message.answer(text="Authenticated.")
        is_authenticated = True
    else:
        await callback.message.edit_text(text="Incorrect pin!", reply_markup=markup)
        