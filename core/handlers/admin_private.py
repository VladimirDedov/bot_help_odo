from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, or_f, StateFilter
from aiogram.fsm.context import FSMContext

from core.filters.chat_types import ChatTypeFilter, IsAdmin
from core.keyboards.kbd import ADMIN_KBD, get_keybord_btns
from core.keyboards.inline import START_INLINE_KBD
from core.fsm.fsm import Add_Instr_Problem as state_fsm
from core.fsm.fsm import FSM_LIST



admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())


@admin_router.message(or_f(CommandStart(), F.text.lower() == "menu"))
async def start_cmd(message: Message):
    await message.answer('Выбирай кнопочки', reply_markup=START_INLINE_KBD)
    await message.answer('Ты бог, делай что хочешь...', reply_markup=ADMIN_KBD)

"""Машина состояний для добавления записей в БД"""
@admin_router.message(StateFilter(None), F.text.in_({'Добавить инструкцию','Добавить вопрос'}))
async def fsm_add_name(message: Message, state: FSMContext):
    if message.text in ('Добавить вопрос',):
        state_fsm.model_name_is_Problems = True
    await message.answer('Введите название:', reply_markup=get_keybord_btns("Заново", "Отмена"))
    await state.set_state(state_fsm.name)

"""Команда отмена"""
@admin_router.message(StateFilter('*'), F.text.casefold() == 'отмена')  # casefold - переводит в нижний регистр
async def cansel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await message.answer('Действия отменены', reply_markup=ADMIN_KBD)
    await state.clear()

@admin_router.message(StateFilter(state_fsm.name), F.text)
async def fsm_add_description(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer("Введите описание проблемы. Разделитель _photo_")
    await state.set_state(state_fsm.description)

@admin_router.message(StateFilter(state_fsm.description, state_fsm.decision), F.text)
async def fsm_add_desicion(message: Message, state: FSMContext):
    if await state.get_state().split(':')[-1] == 'description':
        await state.update_data(description=message.text)
    else:
        await state.update_data(desicion=message.text)

    if state_fsm.model_name_is_Problems:
        await message.answer("Введите решение проблемы. Разделитель _photo_")
        await state.set_state(state_fsm.decision)
        state_fsm.model_name_is_Problems = False
    else:
        await message.answer("Отправьте скриншот. Либо напишите \'end\'")
        await state.set_state(state_fsm.photo_1)
        state_fsm.model_name_is_Problems = True

@admin_router.message(StateFilter(*FSM_LIST))
async def fsm_add_photo(message: Message, state: FSMContext):
    tmp_name_row = state.get_state().split(':')[-1]
    if await  tmp_name_row != 'photo_10':
        await state.update_data(temp_name_row = message.text)