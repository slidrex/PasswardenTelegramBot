from aiogram import Router
from aiogram_dialog import Dialog
from .support_router import rt as sport_router
from .user_data_router import get_delete_data_window
from windows.settings_main_window import get_settings_layout
from windows.user_support_window import get_support_layout

rt = Router(name=__name__)



rt.include_router(sport_router)
rt.include_router(Dialog(get_settings_layout(), 
                         get_support_layout(),
                         get_delete_data_window()))