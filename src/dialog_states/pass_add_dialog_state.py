from aiogram.filters.state import StatesGroup, State

class PasswordDialog(StatesGroup):
    ask_pass_name = State()
    ask_pass_login = State()
    ask_pass_gen_way = State()
    ask_pass_password = State()
    pass_gen_menu = State()
    choose_passlen_win = State()
    confirm_pass_data = State()
    pass_data_confirmed = State()

    edit_name = State()
    edit_login = State()