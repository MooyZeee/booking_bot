from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command, StateFilter

router = Router()


@router.message(StateFilter(None), Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Добро пожаловать в наш бот! Чего вы желаете? - \n'
                         '/book (бронь) - Забронировать столик\n'
                         '/reservation (все брони) - С помощью этой функции вы сможете просмотреть все активные брони')