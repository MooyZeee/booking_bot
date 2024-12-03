from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from database.db import insertIntoToTable
from payment.payment import send_invoice_deposit

router = Router()


class Bron(StatesGroup):
    get_player_name = State()
    day = State()
    time = State()
    people = State()
    window_yes_or_no = State()


@router.message(F.text.startswith('бронь'))
@router.message(Command('book'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Введите имя человека на чье имя ставиться бронь столика')
    await state.set_state(Bron.get_player_name)

@router.message(Bron.get_player_name)
async def get_player_name_func(message: Message, state: FSMContext):
    await state.update_data(name_player=message.text)
    await message.answer('Отлично! Выберите день бронирования')
    await state.set_state(Bron.day)


@router.message(Bron.day)
async def day_func(message: Message, state: FSMContext):
    await state.update_data(day_data=message.text)
    await message.answer('Отлично! Введите теперь время в которое вы подойдете')
    await state.set_state(Bron.time)


@router.message(Bron.time)
async def time_func(message: Message, state: FSMContext):
    await state.update_data(time_data=message.text)
    await message.answer('Отлично! Выберите количество гостей?')
    await state.set_state(Bron.people)


@router.message(Bron.people)
async def people_func(message: Message, state: FSMContext):
    await state.update_data(people_data=message.text)
    await message.answer('Отлично! Выберите ваше пожелание по столу или меню;')
    await state.set_state(Bron.window_yes_or_no)


@router.message(Bron.window_yes_or_no)
async def window_func(message: Message, state: FSMContext):
    await state.update_data(window_data=message.text)
    await send_invoice_deposit(message)
    data = await state.get_data()
    await state.clear()

    a = { # Используем .get()
        'people_name': data.get("name_player"),
        'day_data': data.get("day_data"),
        'time_data': data.get("time_data"),
        'people_data': data.get("people_data"),
        'window': data.get("window_data")
    }
    insertIntoToTable(a.get('people_name'),
                      a.get('day_data'),
                      a.get('time_data'),
                      a.get('people_data'),
                      a.get('window'),
                      message.from_user.id)


# from aiogram import Router, F
# from aiogram.types import Message
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.context import FSMContext
# from aiogram.filters import Command, StateFilter
#
# from payment.payment import send_invoice_deposit
#
# router = Router()
#
#
# class Bron(StatesGroup):
#     day = State()
#     time = State()
#     people = State()
#     window_yes_or_no = State()
#
# @router.message(F.text.startswith('бронь'))
# @router.message(Command('book'))
# async def cmd_start(message: Message, state: FSMContext):
#     await message.answer('Выберите день бронирования')
#     await state.set_state(Bron.day)
#
#
# @router.message(Bron.day)
# async def day_func(message: Message, state: FSMContext):
#     await state.update_data(day_data=message.text)
#     await message.answer('Отлично! Введите теперь время в которое вы подойдете')
#     await state.set_state(Bron.time)
#
#
# @router.message(Bron.time)
# async def time_func(message: Message, state: FSMContext):
#     await state.update_data(time_data=message.text)
#     await message.answer('Отлично! Выберите количество гостей?')
#     await state.set_state(Bron.people)
#
#
# @router.message(Bron.people)
# async def people_func(message: Message, state: FSMContext):
#     await state.update_data(people_data=message.text)
#     await message.answer('Отлично! Выберите ваше пожелание по столу или меню;')
#     await state.set_state(Bron.window_yes_or_no)
#
#
# @router.message(Bron.window_yes_or_no)
# async def window_func(message: Message, state: FSMContext):
#     await state.update_data(window_data=message.text)
#     await send_invoice_deposit(message)
#     data = await state.get_data()
#     await state.clear()
#     return {
#         'day_data': data.get("day_data"),  # Используем .get()
#         'time_data': data.get("time_data"),
#         'people_data': data.get("people_data"),
#         'window': data.get("window_data")
#     }
#
