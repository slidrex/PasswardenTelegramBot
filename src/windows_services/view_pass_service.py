from aiogram_dialog import DialogManager
from aiogram.types import CallbackQuery
from typing import Any
from dialog_states.view_pass_state import ViewPassStates
from core.repositories.password_repository import PasswordRepository, GetPasses, GetPassInfo, ChangePwdLogin, ChangePwdName, ChangePwdPassword, DeletePassword
from core.services.pass_security_check_service import get_security_report
from aiogram.types import Message
from aiogram_dialog.widgets.kbd import Button
from dialog_states.view_pass_state import ViewPassStates

async def get_passwords(dialog_manager: DialogManager,  **middleware_data):
    passes = await PasswordRepository.get_passes(data=GetPasses(user_id=int(dialog_manager.current_context().start_data.get("user_id"))))
    #print(passes, dialog_manager.current_context().start_data.get("user_id"))
    
    data = {
        'passwords': [
        
           (ps.name, ps.login, ps.id)
           for ps in passes
           ]
    }
    return data

async def get_pass_info(dialog_manager: DialogManager, **middleware_data):
    
    context = dialog_manager.current_context()
    pass_id = int(context.dialog_data['pass_id'])
    

    pwd = await PasswordRepository.get_pass_info(GetPassInfo(pass_id=pass_id))
    


    report = get_security_report(pwd.password)

    
    data = {
        'pass_id': pass_id,
        "pass_name" : pwd.name,
        'pass_login' : pwd.login,
        "pass_pass" : pwd.password,
        "pass_entropy" : int(report.entropy),
        "pass_leak": f"Ваш пароль был найден в {report.leaked_count} утечках баз данных" if report.leaked_count > 0 else f"Пароль не был найден в утечках",
        "pass_status" : report.status
    }
    return data

async def on_chosen_pass(c: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(pass_id=item_id)
    
    await manager.switch_to(ViewPassStates.view_pass_info)

async def change_name(message: Message, widget: Any, manager: DialogManager, data: str):
    pass_id = manager.current_context().dialog_data.get("pass_id")
    await PasswordRepository.change_pwd_name(ChangePwdName(pass_id=pass_id, name=data))
    await manager.switch_to(ViewPassStates.view_pass_info)

async def change_login(message: Message, widget: Any, manager: DialogManager, data: str):
    pass_id = manager.current_context().dialog_data.get("pass_id")
    await PasswordRepository.change_pwd_login(ChangePwdLogin(pass_id=pass_id, login=data))
    await manager.switch_to(ViewPassStates.view_pass_info)

async def change_pwd(message: Message, widget: Any, manager: DialogManager, data: str):
    pass_id = manager.current_context().dialog_data.get("pass_id")
    await PasswordRepository.change_pwd_pass(ChangePwdPassword(pass_id=pass_id, password=data))
    await manager.switch_to(ViewPassStates.view_pass_info)

async def del_pass(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await PasswordRepository.delete_pass(DeletePassword(id=manager.current_context().dialog_data.get("pass_id")))
    await manager.switch_to(ViewPassStates.view_pass_info)