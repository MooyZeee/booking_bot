from aiogram import Router
from aiogram.types import Message, PreCheckoutQuery
from utils.constans import PRICE
from config.config import PAYMENT_TOKEN, PHOTO_URL, DESCRIPTION_FOR_DEPOSIT

router = Router()


async def send_invoice_deposit(message: Message):
    # Отправка фото перед инвойсом (это необязательно)
    await message.bot.send_photo(chat_id=message.chat.id,
                                 photo=PHOTO_URL)

    # Отправка инвойса с фото
    await message.bot.send_invoice(
        chat_id=message.chat.id,
        title='Deposit for the table',
        description=DESCRIPTION_FOR_DEPOSIT,
        payload='deposit',
        provider_token=PAYMENT_TOKEN,
        currency='RUB',
        prices=PRICE,
        photo_url=PHOTO_URL
    )


@router.pre_checkout_query()
async def checkout_handler(query: PreCheckoutQuery):
    await query.bot.send_message(query.from_user.id, 'Ожидайте, оплата проверяется..')
    await query.answer(ok=True)


@router.message(lambda message: message.successful_payment is not None)
async def successful_payment_handler(message: Message):
    await message.answer('Оплата прошла успешно!')


@router.message(lambda message: message.successful_payment is False)
async def dont_successful_payment_handler(message: Message):
    await message.answer('Оплата не прошла! Попробуйте пожалуйста снова.')

#
# from aiogram import Router
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message, PreCheckoutQuery
#
# from utils.constans import PRICE
# from config.config import PAYMENT_TOKEN
# from database.db import insertIntoToTable
#
# router = Router()
#
#
# async def some_functions(message: Message, state: FSMContext):
#     from handlers.bron_handler import window_func
#     a = await window_func(message, state)
#     insertIntoToTable(a.get('day_data'), a.get('time_data'), a.get('people_data'), a.get('window'))
#
#
# async def send_invoice_deposit(message: Message):
#     await message.bot.send_photo(chat_id=message.chat.id,
#                                  photo='https://avatars.dzeninfra.ru/get-zen_doc/1863556/pub_6069c99f741adc251d992f62_6069d81e608d5c20734c33a5/scale_1200',
#                                  caption='Хорошо! Мы учли все ваши пожелания и бронь почти заполнена. '
#                                          'Для полной у достоверности вашего прихода, сделайте депозит в размере 50% от суммы!')
#     await message.bot.send_invoice(
#         chat_id=message.chat.id,
#         title='Deposit for the table',
#         description='Обязательный депозит в размере 50% от суммы для бронирования столика. (Сумма будет возвращена в полном размере перед выходом.)',
#         payload='deposit',
#         provider_token=PAYMENT_TOKEN,
#         currency='RUB',
#         prices=PRICE,
#         photo_url='https://avatars.dzeninfra.ru/get-zen_doc/1863556/pub_6069c99f741adc251d992f62_6069d81e608d5c20734c33a5/scale_1200'
#     )
#
#
# @router.pre_checkout_query()
# async def checkout_handler(query: PreCheckoutQuery):
#     await query.bot.send_message(query.from_user.id, 'Ожидайте, оплата проверяется..')
#     await query.answer(ok=True)
#
#
# @router.message(lambda message: message.successful_payment is not None)
# async def successful_payment_handler(message: Message, state: FSMContext):
#     await message.answer('Оплата прошла успешно!')
#     await some_functions(message, state)
#
#
# @router.message(lambda message: message.successful_payment is False)
# async def dont_successful_payment_handler(message: Message):
#     await message.answer('Оплата не прошла! Попробуйте пожалуйста снова.')
