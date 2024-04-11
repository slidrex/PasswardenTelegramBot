import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from routers import router as main_router
from aiogram.client.default import DefaultBotProperties

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
from middleware.auth_middleware import AuthorizationMiddleware

async def main() -> None:
    dp = Dispatcher()
    dp.include_router(main_router)
    bot = Bot(
            token=TOKEN,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML)
        )
    logging.basicConfig(level=logging.INFO)
    dp.message.middleware(AuthorizationMiddleware())

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())