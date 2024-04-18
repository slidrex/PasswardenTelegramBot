
def get_pass_data_confirm_window():
    
    return Window(
        Format('''
Your enterred data:
               
Name: {dialog_data[entered_pass_name]}
Login: {dialog_data[entered_pass_login]}
Password: {dialog_data[entered_pass_password]}
               
Is it correct?
'''
    ),
    Next(Const("Продолжить ✅"), id="pass_confirmation_continue"),
    Cancel(Const("<-- Закрыть -->"), id="pass_confirmation_btn"),
    SwitchTo(Const("⚙️ Изменить имя"), id="pass_confirmation_change_name", state=PasswordDialog.edit_name),
    SwitchTo(Const("⚙️ Изменить логин"), id="pass_confirmation_change_login", state=PasswordDialog.edit_login),
    SwitchTo(Const("⚙️ Изменить пароль"), id="pass_confirmation_change_pass", state=PasswordDialog.ask_pass_gen_way),
    state=PasswordDialog.confirm_pass_data
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