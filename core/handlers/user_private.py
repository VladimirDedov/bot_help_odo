from aiogram import Router, F
from aiogram import types
from aiogram.filters import CommandStart, Command, or_f

from core.keyboards.inline import START_INLINE_KBD


user_private_router = Router()

@user_private_router.message(or_f(CommandStart, F.text.lower().in_({'start', 'начать', 'cтарт'})))
async def send_main_menu(message: types.Message):
    await message.answer('Выберите из списка ниже, что вы хотите изучить: \n', reply_markup=START_INLINE_KBD)

@user_private_router.callback_query(F.data=='instructions')
async def get_instructions(callback: types.CallbackQuery):
    await callback.message.answer("Это список инструкций")
    await callback.message.answer("spisok 2")
