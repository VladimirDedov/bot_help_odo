from aiogram import Router, F
from aiogram import types
from aiogram.filters import CommandStart, Command, or_f
from sqlalchemy.ext.asyncio import AsyncSession

from core.keyboards.inline import START_INLINE_KBD, get_callback_btns
from core.database.orm_query import orm_get_all_list, orm_add_user, orm_get_row

user_private_router = Router()


@user_private_router.message(or_f(CommandStart, F.text.lower().in_({'start', 'начать', 'cтарт'})))
async def send_main_menu(message: types.Message, session: AsyncSession):
    await message.answer('Выберите из списка ниже, что вы хотите изучить: \n', reply_markup=START_INLINE_KBD)
    await orm_add_user(message=message, session=session)


@user_private_router.callback_query(F.data.in_({'instructions', 'problems'}))
async def get_lst_instrustion_problem(callback: types.CallbackQuery, session: AsyncSession):
    answer = await orm_get_all_list(table_name=callback.data, session=session)
    print(answer)
    dict_btns = dict()
    count = 0
    flag = '_problems'
    if callback.data == 'instructions':
        flag = '_instructions'

    for ans in answer:
        if ans.is_published:
            dict_btns[ans.name] = str(ans.id) + flag
            count += 1
    sizes = tuple([1] * count)

    keyboard = get_callback_btns(btns=dict_btns, sizes=sizes)
    if callback.data == 'instructions':
        await callback.message.answer(text='Список инструкций:', reply_markup=keyboard)
    elif callback.data == 'problems':
        await callback.message.answer(text="Список часто задаваемых вопросов:", reply_markup=keyboard)



@user_private_router.callback_query(F.data.split('_')[-1].in_({'instructions', 'problems'}))
async def show_one_problem(callback: types.CallbackQuery, session: AsyncSession):
    table_name = callback.data.split('_')[-1]
    id = int(callback.data.split('_')[0])
    one_row = await orm_get_row(session, table_name, id)
    print(one_row.id)

    await callback.message.answer(text=callback.data.split('_')[0])
    await callback.message.answer('Инструкция!')