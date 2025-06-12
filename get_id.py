from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

API_TOKEN = str(os.environ.get('BOT_TOKEN'))

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message):
    await message.answer("""Привет! 👋 
‼️ Триатлон-квест стартует завтра 13 июня в 11:00. 
‼️ Ждём тебя на площади Конторы пароходства около сцены.
Будет интересно, динамично и по-спортивному 💪""")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)