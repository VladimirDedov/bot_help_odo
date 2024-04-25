from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, or_f, StateFilter, Command
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from core.filters.chat_types import ChatTypeFilter, IsAdmin
from core.keyboards.kbd import ADMIN_KBD, get_keybord_btns, keyboard_remove
from core.keyboards.inline import START_INLINE_KBD
from core.fsm.fsm import Add_Instr_Problem as state_fsm
from core.fsm.fsm import FSM_LIST
from core.database.orm_query import orm_add_problem
from core.database.models import Instructions, Problems

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())


@admin_router.message(or_f(CommandStart(), F.text.lower().in_({"menu", "заново"})))
async def start_cmd(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.clear()
    await message.answer(f'<u><b>Выбирай кнопочки</b></u>', reply_markup=START_INLINE_KBD)
    await message.answer(f'<u><b>Ты бог, делай что хочешь...</b></u>', reply_markup=ADMIN_KBD)


"""Машина состояний для добавления записей в БД"""


@admin_router.message(StateFilter(None), F.text.in_({'Добавить инструкцию', 'Добавить вопрос'}))
async def fsm_add_name(message: Message, state: FSMContext):
    if message.text in ('Добавить вопрос',):
        state_fsm.model_name_is_Problems = True
    await message.answer('Введите название:', reply_markup=get_keybord_btns("Заново", "Отмена"))
    await state.set_state(state_fsm.name)


@admin_router.message(StateFilter('*'), F.text.casefold() == 'отмена')  # casefold - переводит в нижний регистр
async def cansel_handler(message: Message, state: FSMContext) -> None:
    """Команда отмена"""
    current_state = await state.get_state()
    if current_state is not None:
        await state.clear()
        await message.answer('Действия отменены', reply_markup=ADMIN_KBD)


@admin_router.message(StateFilter('*'), F.text.casefold() == 'end')
async def cmd_end(message: Message, session: AsyncSession, state: FSMContext):
    """Завершение FSM и запись в бд"""
    data = await state.get_data()
    current_state = await state.get_state()
    count = int(current_state.split('_')[-1])
    model_name = Instructions
    if 'decision' in data.keys():
        model_name = Problems
    try:
        await orm_add_problem(data=data,
                              session=session,
                              model_name=model_name,
                              count=count)
        await message.answer('Данные успешно записаны', reply_markup=ADMIN_KBD)
        await state.clear()
    except Exception as e:
        print(str(e))
        await message.answer("Нихрена не записалось. Ахтунг! Коллапсинг!")


@admin_router.message(StateFilter(state_fsm.name), F.text)
async def fsm_add_description(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите описание проблемы. Разделитель _photo_",
                         reply_markup=get_keybord_btns("Заново", "Отмена"))
    await state.set_state(state_fsm.description)


@admin_router.message(StateFilter(state_fsm.description, state_fsm.decision), F.text)
async def fsm_add_decision(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state.split(':')[-1] == 'description':
        await state.update_data(description=message.text)
    else:
        await state.update_data(decision=message.text)

    if state_fsm.model_name_is_Problems:
        await message.answer("Введите решение проблемы. Разделитель _photo_")
        await state.set_state(state_fsm.decision)
        state_fsm.model_name_is_Problems = False
    else:
        await message.answer("Отправьте скриншот. Либо напишите \'end\'")
        await state.set_state(state_fsm.photo_1)


@admin_router.message(StateFilter(*FSM_LIST))
async def fsm_add_photo(message: Message, state: FSMContext, session: AsyncSession):
    """Add photos"""
    current_state = await state.get_state()
    tmp_name_row = current_state.split(':')[-1]

    match tmp_name_row:
        case 'photo_1':
            await state.update_data(photo_1=message.photo[-1].file_id)
            await state.set_state(state_fsm.photo_2)
        case 'photo_2':
            await state.update_data(photo_2=message.photo[-1].file_id)
            await state.set_state(state_fsm.photo_3)
        case 'photo_3':
            await state.update_data(photo_3=message.photo[-1].file_id)
            await state.set_state(state_fsm.photo_4)
        case 'photo_4':
            await state.update_data(photo_4=message.photo[-1].file_id)
            await state.set_state(state_fsm.photo_5)
        case 'photo_5':
            await state.update_data(photo_5=message.photo[-1].file_id)
            await state.set_state(state_fsm.photo_6)
        case 'photo_6':
            await state.update_data(photo_6=message.photo[-1].file_id)
            await state.set_state(state_fsm.photo_7)
        case 'photo_7':
            await state.update_data(photo_7=message.photo[-1].file_id)
            await state.set_state(state_fsm.photo_8)
        case 'photo_8':
            await state.update_data(photo_8=message.photo[-1].file_id)
            await state.set_state(state_fsm.photo_9)
        case 'photo_9':
            await state.update_data(photo_9=message.photo[-1].file_id)
            await state.set_state(state_fsm.photo_10)
        case 'photo_10':
            await state.update_data(photo_10=message.photo[-1].file_id)
            await cmd_end()
    if tmp_name_row != 'photo_10':
        await message.answer("Отправьте следующее фото, либо напишите \'end\'")
