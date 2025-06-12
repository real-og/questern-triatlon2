from loader import dp
from states import State
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts


@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help)


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    with open('images/Max.jpeg', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.t1)
    await message.answer(texts.t2)
    await State.enter_name.set()
    await State.wait_start_run.set()