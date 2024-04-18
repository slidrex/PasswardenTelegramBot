from typing import Dict
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import Whenable

def is_has_pin(data: Dict, widget: Whenable, manager: DialogManager):
    return False
def has_no_pin(data: Dict, widget: Whenable, manager: DialogManager):
    return not is_has_pin(data, widget, manager)