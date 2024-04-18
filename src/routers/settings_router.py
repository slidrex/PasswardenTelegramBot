from aiogram import Router
from aiogram_dialog import Dialog
from windows.settings_main_window import get_settings_layout
from windows.user_support_window import get_support_layout
from windows.user_data_windows import get_delete_data_window

rt = Router(name=__name__)


rt.include_router(Dialog(get_settings_layout(), 
                         get_support_layout(),
                         get_delete_data_window()))