from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_all_messages(message: types.Message):
    print(f"[{message.chat.id}] {message.from_user.full_name}: {message.text}")
    await message.reply("я получил сообщение!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)