from aiogram_dialog import DialogManager
from aiogram.types import CallbackQuery
from typing import Any
from dialog_states.view_pass_state import ViewPassStates

async def get_passwords(dialog_manager: DialogManager, **middleware_data):

    data = {
        'passwords': [
            ('GitHub', 'pidoras@gmail.com', 'asfsaf', 10),
            ('Gmail' , 'guesos@gmail.com','xzasfasfx' , 20)
        ]
    }
    return data
async def get_pass_info(dialog_manager: DialogManager, **middleware_data):
    #session = middleware_data.get('session')
    context = dialog_manager.current_context()
    pass_id = int(context.dialog_data['pass_id'])

    data = {
        'pass_id': pass_id,
    }
    return data

async def on_chosen_pass(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(pass_id=item_id)
    
    await manager.switch_to(ViewPassStates.view_pass_info)