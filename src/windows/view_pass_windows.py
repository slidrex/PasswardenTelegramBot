from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.kbd import Cancel, Back, Select, ScrollingGroup
from dialog_states.view_pass_state import ViewPassStates
from windows_services.view_pass_service import on_chosen_pass, get_passwords, get_pass_info
import operator


SCROLLING_HEIGHT = 6

def get_scrolling_group(on_click):
    return ScrollingGroup(
        Select(
            Format("{item[0]}" + ":" + "{item[1]}"),
            id="s_scroll_pass",
            item_id_getter=operator.itemgetter(3),
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
Name: {pass_id}
Login:
Password: 

Entropy: ... bits
Leak Status: ...

Status: ...
'''
        ),
        Button(Const("⚙️ Изменить имя"), id="change_name"),
        Button(Const("⚙️ Изменить логин"), id="change_login"),
        Button(Const("⚙️ Изменить пароль"), id="change_pass"),
        Back(Const('<< Назад')),
        Cancel(Const("<-- Закрыть -->")),
        getter=get_pass_info,
        state=ViewPassStates.view_pass_info
    )