from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

admin_router = Router()

# @admin_router.message(Command("start"))
# @admin_router.message(F.text.lower() == "start")
# async def start(message: Message):
#     await message.answer('Команда старт')
