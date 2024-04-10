from aiogram import Router
from aiogram.types import Message
from aiogram import F
rt = Router(name=__name__)

SECURITY_GUIDE_PREFIX= "securityg"

class SecurityOptions:
    CLOUD_MANAGER="cloud_manager" 
    FILE_MANAGER="file_manager" 
    MANUAL_PASS="manual_pass"
    GEN_PASS="gen_pass"
    GENERAL_INFO="additional"


@rt.callback_query(F.data.startswith(SECURITY_GUIDE_PREFIX))
async def security_guide_handler(message: Message):
    message.text = "справ ка))"
    print("HI")


