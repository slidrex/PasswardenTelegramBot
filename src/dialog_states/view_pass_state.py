from aiogram.filters.state import State, StatesGroup

class ViewPassStates(StatesGroup):
    select_pass = State()
    view_pass_info = State()