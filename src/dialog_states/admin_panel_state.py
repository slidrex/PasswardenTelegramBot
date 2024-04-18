from aiogram.filters.state import StatesGroup, State

class AdminState(StatesGroup):
    ADMIN_DIALOG = State()
    
    ENTER_SUPPORT_ANSWER = State()
    SUPPORT_RESPONSE_DIALOG = State()
    
    ADMIN_DIALOG_RESPONSE = State()
    RESPONSE_CONFIRM_INFO = State()