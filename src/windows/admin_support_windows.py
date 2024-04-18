from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Cancel, Button
from aiogram_dialog import Window
from dialog_states.admin_panel_state import AdminState
from windows_services.admin_support_service import on_support_response_enterred, send_support_response

def get_support_message_window():
    return Window(
        Const("Enter response text: "),
        TextInput(id="support_response_text_input", on_success=on_support_response_enterred),

        state=AdminState.SUPPORT_RESPONSE_DIALOG
    )

def get_support_text_window():
    return Window(
            Const("Enter chat id and response message: (  3482937 Hello! It's PasswardenSupport... )"),
            TextInput(id="answer_support_input", on_success=on_support_response_enterred),
            Cancel(Const("<< Back")),

            state = AdminState.ADMIN_DIALOG_RESPONSE
    )

def get_response_confirm_window():

    return Window(Format('''
           <b>Support Response</b>

ChatID: {dialog_data[support_chat_id]}
Message: {dialog_data[support_message]}
    '''
    ),
    Button(Const("Confirm"), id="confirm_support_response", on_click=send_support_response),
    Cancel(Const("Reject")),
    state=AdminState.RESPONSE_CONFIRM_INFO
    )