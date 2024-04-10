"""Данные Машины состояний """

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

FSM_LIST = [
    'photo_1' ,
    'photo_2' ,
    'photo_3' ,
    'photo_4' ,
    'photo_5' ,
    'photo_6' ,
    'photo_7' ,
    'photo_8' ,
    'photo_9' ,
    'photo_10'
]

class Add_Instr_Problem(StatesGroup):
    model_name_is_Problems = False
    is_published = State()
    name = State()
    description = State()
    decision = State()
    photo_1 = State()
    photo_2 = State()
    photo_3 = State()
    photo_4 = State()
    photo_5 = State()
    photo_6 = State()
    photo_7 = State()
    photo_8 = State()
    photo_9 = State()
    photo_10 = State()

