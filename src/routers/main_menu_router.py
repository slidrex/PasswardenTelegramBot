from aiogram import Router , flags
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F
from .settings_router import rt as settings_rt
from dialog_states.settings_states import (
SettingsState
)
from html_messages import about
from aiogram.fsm.context import FSMContext

from aiogram.utils.keyboard import InlineKeyboardBuilder
from .add_password_router import rt as add_pass_router
from .view_pass_router import rt as view_pass_router


from middleware.auth_middleware import rt as auth_rt
from dialog_states.pass_add_dialog_state import PasswordDialog
from dialog_states.view_pass_state import ViewPassStates
from routers.admin_panel_router import rt as admin_router

from aiogram_dialog import (
    DialogManager, StartMode
)



SOURCE_CODE_API_URI = "https://github.com/slidrex/passwarden-server"
SOURCE_CODE_BOT_URI = "https://github.com/slidrex/passwarden-bot"


from windows.main_menu_window import (
    get_main_markup,
    ButtonText
)


rt = Router(name=__name__)

rt.include_router(view_pass_router)
rt.include_router(settings_rt)
rt.include_router(add_pass_router)
rt.include_router(auth_rt)
rt.include_router(admin_router)

@rt.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    
    await message.answer(text= about.MESSAGE, reply_markup=get_main_markup())

@rt.message(F.text == ButtonText.INFO)
async def about_handler(message: Message) -> None:

    builder = InlineKeyboardBuilder()
    builder.button(text="Github (API)", url=SOURCE_CODE_API_URI)
    builder.button(text="Github (Bot)", url=SOURCE_CODE_BOT_URI)
    
    await message.answer(text= about.MESSAGE, reply_markup=builder.as_markup())

@rt.message(F.text == ButtonText.CREATE_PASS)
@flags.authorization()
async def create_pass_handler(message: Message, state: FSMContext, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(PasswordDialog.ask_pass_name, mode=StartMode.RESET_STACK,
                               data={"password_length":16,
                                     "include_symbols": False})


@rt.message(F.text == ButtonText.VIEW_PASS)
async def view_pass_handler(message: Message, state: FSMContext, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(ViewPassStates.select_pass, mode=StartMode.RESET_STACK)


@rt.message(F.text == ButtonText.SETTINGS)
async def settings_handler(message: Message, state: FSMContext, dialog_manager: DialogManager) -> None:

    await dialog_manager.start(SettingsState.SEETINGS_DIALOG)

