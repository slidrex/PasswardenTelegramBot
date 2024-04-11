from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram import F
from aiogram import MagicFilter

rt = Router()

PIN_BOARD_PREFIX = "pinboard_"
PIN_BOARD_BACK = "back"
PIN_BOARD_ENTER = "enter"
PIN_BOARD_DELETE = "delete"

ENTER_PIN_MESSAGE = "Введите PIN:"


def get_pin_markup():
    builder = InlineKeyboardBuilder()
    for i in range(1, 10):

        builder.button(text=str(i), callback_data=PIN_BOARD_PREFIX+str(i))
    builder.button(text="Сброс", callback_data=PIN_BOARD_PREFIX + PIN_BOARD_DELETE)
    builder.button(text="0", callback_data=PIN_BOARD_PREFIX+"0")
    builder.button(text="Ввод", callback_data=PIN_BOARD_PREFIX + PIN_BOARD_ENTER)

    builder.button(text="Назад", callback_data=PIN_BOARD_PREFIX + PIN_BOARD_BACK)
    

    builder.adjust(3, 3, 3, 3, 2)
    return builder.as_markup()
markup = get_pin_markup()
async def send_auth_message(message: Message):
    await message.answer(text= ENTER_PIN_MESSAGE, reply_markup=get_pin_markup())

@rt.callback_query(F.data.startswith(PIN_BOARD_PREFIX))
async def view_pass_handler(callback: CallbackQuery) -> None:
    postfix_message = callback.data[callback.data.index("_") + 1:]
    field_text = str(callback.message.text)
    len_of_field_text = len(field_text)
    
    if postfix_message == PIN_BOARD_DELETE and field_text != ENTER_PIN_MESSAGE:
        await callback.message.edit_text(text=ENTER_PIN_MESSAGE,reply_markup=markup)
    
    if field_text[0].isdigit():
        if len_of_field_text < 6:
            await callback.message.edit_text(text=field_text + postfix_message, reply_markup=markup)
    else:
        await callback.message.edit_text(text=postfix_message, reply_markup=markup)
    
        