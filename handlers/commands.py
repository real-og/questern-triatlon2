from loader import dp
from states import State
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import aiotable
from datetime import datetime, timedelta, timezone



@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help)

@dp.message_handler(commands=['terms'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('terms.pdf', 'rb') as f:
        await message.answer_document(f)


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('images/Max.jpeg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.t1)
    await message.answer(texts.t2)
    await State.enter_name.set()

    username = str(message.from_user.username)
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")

    await aiotable.append_user_strict_short(str(message.from_user.id), str(username), str(datetime_str))
    # await State.finish_velo.set()