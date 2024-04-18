from aiogram.filters.state import StatesGroup, State

class SettingsState(StatesGroup):
    INPUT_SUPPORT = State()
    SEETINGS_DIALOG = State()
    DeleteData = State()
    SUPPORT_DIALOG = State()