import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
PAYMENT_TOKEN = os.getenv("PAYMENT_TOKEN")
PHOTO_URL = 'https://avatars.dzeninfra.ru/get-zen_doc/1863556/pub_6069c99f741adc251d992f62_6069d81e608d5c20734c33a5/scale_1200'
DESCRIPTION_FOR_DEPOSIT = ('\nХорошо! Мы учли все ваши пожелания и бронь почти заполнена. '
                           'Для полной у достоверности вашего прихода, сделайте депозит в размере 50% от суммы. '
                           '(Сумма будет возвращена в полном размере перед выходом.)')


