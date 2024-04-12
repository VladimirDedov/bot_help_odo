"""Данные Машины состояний """

from aiogram.fsm.state import StatesGroup, State


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


FSM_LIST = [
    Add_Instr_Problem.photo_1,
    Add_Instr_Problem.photo_2,
    Add_Instr_Problem.photo_3,
    Add_Instr_Problem.photo_4,
    Add_Instr_Problem.photo_5,
    Add_Instr_Problem.photo_6,
    Add_Instr_Problem.photo_7,
    Add_Instr_Problem.photo_8,
    Add_Instr_Problem.photo_9,
    Add_Instr_Problem.photo_10
]

