from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton

class ButtonText:
    CREATE_PASS = "➕Создать пароль"
    VIEW_PASS = "🔐Посмотреть пароли"
    INFO = "📄Информация"
    SETTINGS = "⚙️Настройки"


def get_main_markup() -> ReplyKeyboardMarkup:
    kb = [
        [
            KeyboardButton(text=ButtonText.CREATE_PASS), KeyboardButton(text=ButtonText.VIEW_PASS),   
        ],
        [
            KeyboardButton(text=ButtonText.INFO), KeyboardButton(text=ButtonText.SETTINGS)
        ]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        is_persistent=True,
        resize_keyboard=True,
    )
    return keyboard