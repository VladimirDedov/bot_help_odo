from sqlalchemy import select, update, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Bundle
from aiogram import types

from core.database.models import Instructions, Problems, User

async def orm_get_all_list(table_name: str, session: AsyncSession):
    if table_name == 'instructions':
        model_class_name = Instructions
    elif table_name == 'problems':
        model_class_name = Problems
    query=select(Bundle("lst",model_class_name.name, model_class_name.id, model_class_name.is_published))
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_row(session: AsyncSession, id: int):
    query = select(Instructions).where(Instructions.id == id)
    result = await session.execute(query)
    return result.scalar()


async def add_user(message: types.Message, session: AsyncSession):
    obj = User(
        user_id=message.from_user.id,
        name=message.from_user.first_name
    )
    session.add(obj)
    await session.commit()