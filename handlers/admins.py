
from loader import dp, GROUP_CHAT_ID_PHOTO, bot
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
import logic

@dp.message_handler(lambda message: str(message.chat.id) == str(GROUP_CHAT_ID_PHOTO), state='*')
async def handle_admin_reply_ok(message: types.Message):
    try:
        if message.text not in [ '1','2','3','4', '5']:
            return
        if message.reply_to_message:
            target_id = message.reply_to_message.message_id
            user_id = logic.cache[target_id]
            name = logic.photo_names[int(message.text) - 1]
            with open(name, 'rb') as photo:
                await bot.send_photo(user_id, photo)
    except:
        pass

