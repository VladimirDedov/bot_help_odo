from sqlalchemy import select, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Bundle
from aiogram import types

from core.database.models import Instructions, Problems, User


def __get_model_class_name(table_name: str):
    if table_name == 'instructions':
        return Instructions
    return Problems


async def orm_get_all_list(table_name: str, session: AsyncSession):
    model_class_name = __get_model_class_name(table_name)
    query = select(Bundle("lst", model_class_name.name, model_class_name.id, model_class_name.is_published))
    result = await session.execute(query)
    return result.scalars().all()


# get one record
async def orm_get_row(session: AsyncSession, table_name: str, id: int):
    model_class_name = __get_model_class_name(table_name)
    query = select(model_class_name).where(model_class_name.id == id)
    result = await session.execute(query)
    return result.scalar()


async def orm_add_user(message: types.Message, session: AsyncSession):
    query = select(User.user_id)
    result = await session.execute(query)
    lst_users = result.scalars().all()
    if message.from_user.id not in lst_users:
        obj = User(
            user_id=message.from_user.id,
            name=message.from_user.first_name
        )
        session.add(obj)
        await session.commit()


async def orm_add_problem(data: dict,
                          session: AsyncSession,
                          model_name: Instructions or Problems,
                          count: int = 1):
    for i in range(count, 11):
        data[f'photo_{i}'] = None

    obj = model_name(
        name=data['name'],
        description=data['description'],
        photo_1=data['photo_1'],
        photo_2=data['photo_2'],
        photo_3=data['photo_3'],
        photo_4=data['photo_4'],
        photo_5=data['photo_5'],
        photo_6=data['photo_6'],
        photo_7=data['photo_7'],
        photo_8=data['photo_8'],
        photo_9=data['photo_9'],
        photo_10=data['photo_10'])

    if model_name == Problems:
        obj.decision=data['decision']

    session.add(obj)
    await session.commit()
