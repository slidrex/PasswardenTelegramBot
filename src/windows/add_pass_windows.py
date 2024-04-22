
from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Format, Const
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo, Next, Cancel, Button, Row, Back, Checkbox
from dialog_states.pass_add_dialog_state import PasswordDialog
from windows_services.add_pass_callbacks import (
    on_pass_gen_clicked, 
    on_pass_login_edited, 
    on_pass_login_enterred, 
    on_pass_manual_clicked, 
    on_pass_manual_password_enterred, 
    on_pass_name_edited, 
    on_pass_name_enterred,
    pass_get_data,
    save_pass_click,
    get_password_security_report,
    check_changed, choose_16_passlen, choose_32_passlen, choose_64_passlen, choose_8_passlen
)


def get_pass_data_confirm_window():
    
    return Window(
        Format('''
Your enterred data:
               
Name: `{dialog_data[entered_pass_name]}`
Login: `{dialog_data[entered_pass_login]}`
Password: `{dialog_data[entered_pass_password]}`

Entropy: {entropy} bits
Leak Status: {leak}

Status: {leak_status}
               
Is it correct?
'''
    ),
    Next(Const("Продолжить ✅"), id="pass_confirmation_continue", on_click=save_pass_click),
    Cancel(Const("<-- Закрыть -->"), id="pass_confirmation_btn"),
    SwitchTo(Const("⚙️ Изменить имя"), id="pass_confirmation_change_name", state=PasswordDialog.edit_name),
    SwitchTo(Const("⚙️ Изменить логин"), id="pass_confirmation_change_login", state=PasswordDialog.edit_login),
    SwitchTo(Const("⚙️ Изменить пароль"), id="pass_confirmation_change_pass", state=PasswordDialog.ask_pass_gen_way),
    state=PasswordDialog.confirm_pass_data,
    getter=get_password_security_report,
    parse_mode="MarkdownV2"
    )
def edit_name_window():
    return Window(
        Const("Введите имя пароля: "),
        TextInput(id="edit_name_win", on_success=on_pass_name_edited),
        state=PasswordDialog.edit_name
    )
def edit_login_window():
    return Window(
        Const("Введите имя пароля: "),
        TextInput(id="edit_login_win", on_success=on_pass_login_edited),
        state=PasswordDialog.edit_login
    )

def input_pass_login_window():
    return Window(
        Const('Введите логин:'),
        TextInput(id='login', on_success=on_pass_login_enterred),
        Cancel(Const("Отменить")),
        state=PasswordDialog.ask_pass_login
    )
def input_pass_password_window():
    return Window(
        Const('Введите пароль:'),
        TextInput(id='pass_pwd', on_success=on_pass_manual_password_enterred),
        Cancel(Const("Отменить")),
        state=PasswordDialog.ask_pass_password
    )
def pass_data_confirmed_win():
    return Window(
        Const("Новый пароль добавлен!"),
        state=PasswordDialog.pass_data_confirmed
    )

def input_pass_choose_window():
    return Window(
        Const('Введите способ создания пароля:'),
        Button(Const("Ввести вручную"), id="manual_pass_enter", on_click=on_pass_manual_clicked),
        Button(Const("Сгенерировать"), id="get_pass_enter", on_click=on_pass_gen_clicked),
        state=PasswordDialog.ask_pass_gen_way
    )
def get_change_pass_len_window():
    return Window(
        Const("Выберите длину пароля"),
        Row(
            Button(Const("8"), id="choose_8_passlen", on_click=choose_8_passlen),
            Button(Const("16"), id="choose_16_passlen", on_click=choose_16_passlen),
            Button(Const("32"), id="choose_32_passlen", on_click=choose_32_passlen),
            Button(Const("64"), id="choose_64_passlen", on_click=choose_64_passlen)
        ),
        Back(Const("<< Назад")),
        Cancel(Const("<-- Закрыть -->")),

        state=PasswordDialog.choose_passlen_win
    )

def input_pass_gen_window():
    return Window(
        Format('''`{pwd}`'''),
        SwitchTo(Const("Взять пароль"), id="take_pass", state=PasswordDialog.confirm_pass_data),
        Row(
            Checkbox(default=False, on_state_changed=check_changed, checked_text=Const("Символы ✅"), unchecked_text=Const("Символы ❌"), id="include_symbols"),
                    SwitchTo(Const("Изменить длину"), id="change_len", state=PasswordDialog.choose_passlen_win),
        ),
        
        SwitchTo(Const("Сгенерировать новый"), id="genn_new", state=PasswordDialog.pass_gen_menu),
        state=PasswordDialog.pass_gen_menu,
        parse_mode="MarkdownV2",
        getter=pass_get_data
    )
def input_pass_name_window():
    return Window(
        Const('Введите название пароля: (чтобы знать от чего пароль)'),
        TextInput(id='name', on_success=on_pass_name_enterred),
        Cancel(Const("Отменить")),
        state=PasswordDialog.ask_pass_name
    )