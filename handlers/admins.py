
from loader import dp, GROUP_CHAT_ID_PHOTO
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import re
from datetime import datetime, timedelta, timezone
import buttons
import answers
import random
from aiogram.types import InputFile

@dp.message_handler(lambda message: str(message.chat.id) == str(GROUP_CHAT_ID_PHOTO), state='*')
async def handle_admin_reply_ok(message: types.Message):
    # replied_id = message.reply_to_message.message_id

    # if replied_id in message_links:
    #     user_id = message_links.pop(replied_id)
    #     await bot.send_message(user_id, "✅ ваше фото одобрено!")
    #     await message.reply("Ответ отправлен пользователю.")
    # else:
    #     await message.reply("неизвестное сообщение, не найдено в базе.")
    print(message)