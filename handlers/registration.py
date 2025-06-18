from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import re
from datetime import datetime, timedelta, timezone
from aiogram.types import ReplyKeyboardRemove


def is_email(string):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, string) is not None


@dp.message_handler(state=State.enter_name)
async def send_welcome(message: types.Message, state: FSMContext):
    name = message.text
    await message.answer(texts.t3_1, reply_markup=kb.number_kb)
    await State.waiting_for_number.set()
    await state.update_data(name=name)
    await aiotable.update_cell(message.from_user.id, 4, name)


@dp.message_handler(state=State.waiting_for_number, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    if not message.contact:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.number_kb)
        return

    phone_number = 'Не указал'
    if message.contact:
        phone_number = message.contact.phone_number

    await message.answer(texts.t4, reply_markup=ReplyKeyboardRemove())
    await State.enter_email.set()
    await state.update_data(phone_number=phone_number)
    await aiotable.update_cell(message.from_user.id, 3, phone_number)



#ekb
@dp.message_handler(state=State.enter_email)
async def send_welcome(message: types.Message, state: FSMContext):
    email = message.text.strip()
    if not is_email(email):
        await message.answer(texts.email_wrong)
        return
    

    await message.answer(texts.t3_2)
    await aiotable.update_cell(message.from_user.id, 5, email)
    await State.choose_town.set()


@dp.message_handler(state=State.choose_town)
async def send_welcome(message: types.Message, state: FSMContext):
    town = message.text.strip()
    await message.answer(texts.t3_3)
    await State.gg.set()
    await aiotable.update_cell(message.from_user.id, 6, town)
    # await aiotable.update_cell(message.from_user.id, 11, datetime_str)



@dp.message_handler(state=State.gg)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer("Наберись терпения и готовься! Триатлон-квест стартует 27 июня в 10:00 🔥")

# @dp.message_handler(state=State.enter_email)
# async def send_welcome(message: types.Message, state: FSMContext):
#     email = message.text.strip()
#     if not is_email(email):
#         await message.answer(texts.email_wrong)
#         return
    
#     await message.answer(texts.t5 + '\n' + texts.t8)
#     # await message.answer(texts.t6)
#     # await message.answer(texts.t7)
#     # await message.answer(texts.t8)
#     await message.answer(texts.t9, reply_markup=kb.get_game_kb([]))
#     await State.playing_game.set()
#     data = await state.get_data()
#     await state.update_data(selected_butts=[])
#     name = data.get('name')
#     phone_number = data.get('phone_number')
#     id = str(message.from_id)
#     username = str(message.from_user.username)

#     utc_plus_3 = timezone(timedelta(hours=3))
#     now_utc3 = datetime.now(utc_plus_3)
#     datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")

#     # await aiotable.append_user(id, str(username), str(phone_number), str(name), str(email), str(datetime_str))
#     await aiotable.append_user_strict(id, str(username), str(phone_number), str(name), str(email), str(datetime_str))






