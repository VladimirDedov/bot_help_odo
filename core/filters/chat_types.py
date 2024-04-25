import os
from aiogram.filters import Filter
from aiogram import types


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: []) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types

class IsAdmin(Filter):
    def __init__(self):
        pass

    async def __call__(self, message: types.Message) -> bool:
        lst_of_admin = set(map(int, os.getenv("ADMIN_ID").split(',')))
        return message.from_user.id in lst_of_admin