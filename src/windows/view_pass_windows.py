from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, SwitchTo
from aiogram_dialog.widgets.kbd import Cancel, Back, Select, ScrollingGroup, Start
from dialog_states.view_pass_state import ViewPassStates
from windows_services.view_pass_service import (on_chosen_pass, 
 get_passwords, get_pass_info, change_login, change_name, change_pwd, del_pass)
import operator
from dialog_states.pass_add_dialog_state import PasswordDialog


SCROLLING_HEIGHT = 6

def get_scrolling_group(on_click):
    return ScrollingGroup(
        Select(
            Format("{item[0]}" + ":" + "{item[1]}"),
            id="s_scroll_pass",
            item_id_getter=operator.itemgetter(2),
            items="passwords",
            on_click=on_click,
        ),
        id="pass_ids",
        width=1, height=SCROLLING_HEIGHT,
    )
def get_passwords_window():
    return Window(
        Const('Choose pass:'),
        get_scrolling_group(on_chosen_pass),
        Cancel(Const('<-- Close -->')),
        state=ViewPassStates.select_pass,
        getter=get_passwords
    )
def get_pass_info_window():
    return Window(
        Format(
'''
Name: `{pass_name}`
Login: `{pass_login}`
Password: `{pass_pass}`

Entropy: {pass_entropy} bits
Leak Status: {pass_leak}

Status: {pass_status}
'''
        ),
        SwitchTo(Const("⚙️ Изменить имя"), state=ViewPassStates.change_name, id="pv_change_name"),
        SwitchTo(Const("⚙️ Изменить логин"),state=ViewPassStates.change_login, id="pv_change_login"),
        SwitchTo(Const("⚙️ Изменить пароль"),state=ViewPassStates.change_pwd, id="pv_change_pwd"),
        Button(Const("❌ Удалить"), id="pv_del_pass", on_click=del_pass),
        Back(Const('<< Назад')),
        Cancel(Const("<-- Закрыть -->")),
        getter=get_pass_info,
        parse_mode="MarkdownV2",
        state=ViewPassStates.view_pass_info
    )
def change_pass_login_window():
    return Window(
        Const('Введите логин:'),
        TextInput(id='pv_login', on_success=change_login),
        Cancel(Const("Отменить")),
        state=ViewPassStates.change_login
    )
def change_pass_name_window():
    return Window(
        Const('Введите имя:'),
        TextInput(id='pv_name', on_success=change_name),
        Cancel(Const("Отменить")),
        state=ViewPassStates.change_name
    )
def change_pass_pass_window():
    return Window(
        Const('Введите пароль:'),
        TextInput(id='pv_pwd', on_success=change_pwd),
        Cancel(Const("Отменить")),
        state=ViewPassStates.change_pwd
    )