import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from routers import router as main_router
from aiogram.client.default import DefaultBotProperties
from aiogram_dialog import setup_dialogs
from logging_master.logging_manager import init_logging_bot
from aiogram import flags
from core.database.entities import create_tables

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

from middleware.auth_middleware import AuthorizationMiddleware

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(main_router)
    
    #dp.callback_query.middleware(AuthorizationMiddleware())
    
   # dp.message.middleware(AuthorizationMiddleware())
    
    setup_dialogs(dp)
    await create_tables()
    bot = Bot(
            token=TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    logging.basicConfig(level=logging.INFO)

    init_logging_bot(bot)
    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())