from aiogram import Router
from aiogram.types import Message, InputFile, BufferedInputFile
from aiogram.filters import Command
from database.db import activeBronSelect

router = Router()


@router.message(Command('reservation'))
async def reservation_cmd(message: Message):
    # Получаем данные о бронированиях
    reservation = activeBronSelect()

    # Форматируем данные для отправки
    if reservation.empty:
        await message.reply("Нет активных броней.")
        return

    # Заголовок таблицы
    response_message = "📅 Список активных броней\n\n"
    response_message += "👤 Имя человека | 🏷️ Дата | 🕒 Время | 👥 Количество людей | 📝 Пожелания | Идентификатор пользователя (ID)\n"
    response_message += "-------------------------------------\n"

    # Добавляем каждую бронь в сообщение
    for index, row in reservation.iterrows():
        response_message += f"{row['People Name']} | {row['Day']} | {row['Time']} | {row['People']} | {row['Wishes']} | {row['Player ID']}\n"

    # Отправляем сообщение пользователю
    await message.reply(response_message)

# @router.message(Command('reservation'))
# async def reservation_cmd(message: Message):
#     # Получаем данные о бронированиях
#     reservation = activeBronSelect()
#
#     # Сохраняем данные в Excel файл
#     file_path = 'bookings.xlsx'
#     reservation.to_excel(file_path, index=False)
#
#     # Отправляем файл пользователю
#     with open(file_path, 'rb') as file:
#         await message.bot.send_document(chat_id=message.chat.id,
#                                         document=BufferedInputFile(file.read(), filename=f'{file_path}'),
#                                          caption='Держите документ со всеми бронями на ближайшие сроки')
