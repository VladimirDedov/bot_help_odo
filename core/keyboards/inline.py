from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_callback_btns(
        *,
        btns: dict,
        sizes: tuple = (2,),
):
    keyboard = InlineKeyboardBuilder()

    for text, data in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))
    return keyboard.adjust(*sizes).as_markup()


START_INLINE_KBD = get_callback_btns(
    btns={
        "Инструкции": "instructions",
        "Частые вопросы": "problems"
    }
)
