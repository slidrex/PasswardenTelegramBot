from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram_dialog.widgets.kbd import Url
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import Window
from aiogram_dialog.widgets.media import StaticMedia
from html_messages.about import MESSAGE
from dialog_states.main_menu_states import MenuState
SOURCE_CODE_BOT_URI = "https://github.com/slidrex/passwarden"
def get_info_window():
    
    return Window(
        Const(MESSAGE),
        Url(text=Const("Github (Bot)"), url=Const(SOURCE_CODE_BOT_URI)),
        
        state=MenuState.INFO
    )

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