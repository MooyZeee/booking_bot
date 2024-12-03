import asyncio
import logging

from aiogram import Bot, Dispatcher
from config.config import BOT_TOKEN
from handlers.start_handler import router as start_router
from handlers.bron_handler import router as bron_router
from handlers.reservation_handler import router as reservation_router
from payment.payment import router as payment_router
from database.db import createTable


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    logging.basicConfig(level=logging.INFO)
    dp.include_router(start_router)
    dp.include_router(bron_router)
    dp.include_router(reservation_router)
    dp.include_router(payment_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        createTable()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
