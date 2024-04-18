from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, Cancel
from dialog_states.admin_panel_state import AdminState
from windows_services.admin_support_service import on_support_response_click
from windows_services.admin_panel_service import on_admin_panel_close

def get_admin_dialog_window():
    return Window(
        Const("Admin panel"),
        Button(Const("Answer question"), id="answer_support", on_click=on_support_response_click),
        Cancel(Const("<-- Close -->"), on_click=on_admin_panel_close),
        state = AdminState.ADMIN_DIALOG
)