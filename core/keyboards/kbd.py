from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard = ReplyKeyboardBuilder()

def get_keybord_btns(
        *btns: str,
        placeholder: str = None,
        request_contact: int = None,
        request_location: int = None,
        size: tuple = (2,)
):
    for text, index in enumerate(btns):
        keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*size).as_markup(resize_keyboard = True)