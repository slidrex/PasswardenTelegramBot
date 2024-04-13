import logging
from aiogram import Bot
from dotenv import load_dotenv
from os import getenv

load_dotenv()

LOG_CHANNEL = getenv("LOG_CHANNEL")

ADMIN_ID = getenv("ADMIN_ID")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot: Bot = None

def init_logging_bot(s_bot: Bot):
    global bot
    bot = s_bot

async def log_to_channel(message):
    try:
        await bot.send_message(chat_id=LOG_CHANNEL, text=f"{message}")
    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения в канал: {e}")
    
async def log_to_user(chat_id, message):
    try:
        await bot.send_message(chat_id=chat_id, text=f"{message}")
    except Exception as e:
        logger.error(f"Ошибка при отправке сообщения в канал: {e}")