from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard = ReplyKeyboardBuilder()
keyboard_remove = ReplyKeyboardRemove()

def get_keybord_btns(
        *btns: str,
        placeholder: str = None,
        request_contact: int = None,
        request_location: int = None,
        size: tuple = (2,)
):
    btns = btns
    for index, text in enumerate(btns, start=0):
        keyboard.add(KeyboardButton(text=text))
    return keyboard.adjust(*size).as_markup(resize_keyboard = True)

ADMIN_KBD = get_keybord_btns(
    'Добавить инструкцию',
    'Добавить вопрос',
    size=(2,)
)