import asyncio
import os

from aiogram import Dispatcher, Bot, types
from aiogram.enums import ParseMode
from core.handlers.admin_private import admin_router
from core.handlers.user_private import user_private_router
from core import config
from core.database.engine import create_db, session_maker
from core.middlewares.db import DataBaseSession


bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
dp=Dispatcher()
dp.include_routers(admin_router, user_private_router)


async def main():
    await create_db()
    dp.update.middleware(DataBaseSession(session_pool=session_maker))#сессия для работы с бд
    await bot.delete_webhook(drop_pending_updates=True)
    #await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats) удаляет все команды
    await dp.start_polling(bot, allowed_updates=config.ALLOWED_UPDATES)

if __name__ == "__main__":
    asyncio.run(main())