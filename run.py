from aiogram import Bot, Dispatcher
import asyncio

from aiogram.fsm.storage.redis import RedisStorage

from handlers import router
from commands import set_commands
from data_base.create_db import async_main

from config import redis_url_db

from dotenv import load_dotenv

import os, logging, sys

from registr import reg_router
from admin import add_category_router

redis_url = redis_url_db

load_dotenv()

storage = RedisStorage.from_url(redis_url)
dp = Dispatcher(storage=storage)



async def main():

    token = os.getenv('TOKEN')
    bot = Bot(token=token)
    dp.include_router(router)
    dp.include_router(reg_router)
    dp.include_router(add_category_router)

    await set_commands(bot)
    await dp.start_polling(bot)

async def start_bot(bot: Bot):

    admin_id = os.getenv('ADMIN_ID')
    await bot.send_message(admin_id, text="Бот запущен")

    dp.startup.register(start_bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')