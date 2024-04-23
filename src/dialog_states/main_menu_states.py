from aiogram.filters.state import StatesGroup, State

class MenuState(StatesGroup):
    INFO = State()
    ADMINPANEL = State()