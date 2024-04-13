from logging_master.logging_manager import log_to_channel, log_to_user
from aiogram.types import Message

'''
Application Logging for security audit.
'''

class LogType:
    SUPPORT_REQUEST="#SupportRequest"

class RequestType:
    SUPPORT="Support"

#пидораспедик123

async def log_support_response(user_id:int, username:str, chat_id:int, message:str):
    await log_to_channel(f'''
{LogType.SUPPORT_REQUEST}

User: {user_id} (@{username})
Chat-ID: {chat_id}
Message: {message}
    ''')

async def write_support_message(chat_id: int, message:str):
    await log_to_user(chat_id=chat_id, message=
                      f'''
<b>Сообщение от поддержки:</b>

{message}
                      ''')