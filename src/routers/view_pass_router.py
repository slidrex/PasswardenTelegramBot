from aiogram_dialog import Dialog
from aiogram import Router
from windows.view_pass_windows import get_pass_info_window, get_passwords_window

rt = Router()

rt.include_router(Dialog(get_passwords_window(), 
                         get_pass_info_window()))
