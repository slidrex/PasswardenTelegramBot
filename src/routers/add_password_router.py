from aiogram import Router
from windows.add_pass_windows import input_pass_choose_window, input_pass_gen_window, edit_login_window, edit_name_window, input_pass_login_window, input_pass_name_window, input_pass_password_window, get_change_pass_len_window, pass_data_confirmed_win, get_pass_data_confirm_window

from aiogram_dialog import (
    Dialog
)

rt = Router(name=__name__)

rt.include_router(Dialog(input_pass_name_window(), 
                         input_pass_gen_window(), 
                         input_pass_choose_window(), 
                         input_pass_login_window(),
                         get_change_pass_len_window(),
                         input_pass_password_window(),
                         get_pass_data_confirm_window(),
                         pass_data_confirmed_win(),
                         edit_name_window(),
                         edit_login_window()
                         ))