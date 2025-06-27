from loader import dp
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


@dp.message_handler(state=State.wait_for_start)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.start:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.start)
        return

    await message.answer(texts.t13_1)
    # await message.answer(texts.t14)
    # await message.answer(texts.t15)
    await message.answer(texts.t14, reply_markup=kb.start_swim_terms)
    await State.wait_start_swim_terms.set()



@dp.message_handler(state=State.wait_start_swim_terms)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.terms_swim:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.start_swim_terms)
        return

    # await message.answer(texts.t17)
    await message.answer(texts.t17, reply_markup=kb.start_swim)
    await State.wait_start_swim.set()


@dp.message_handler(state=State.wait_start_swim)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.start_swim:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.start_swim)
        return

    await message.answer(texts.t19, reply_markup=kb.found_qr)
    await State.state1.set()

@dp.message_handler(state=State.state1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.found:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.found_qr)
        return

    await message.answer(texts.t21)
    await State.ans1.set()

@dp.message_handler(state=State.ans1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() != answers.answer1.lower():
        random_answer = random.choice(texts.wrong_ans)
        await message.answer(random_answer)
        return 
    await message.answer(texts.t22)
    with open('images/Часы.png', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.t23)
    await message.answer(texts.t24, reply_markup=kb.swim_next)
    await State.state2.set()

    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 9, datetime_str)



@dp.message_handler(state=State.state2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.swim_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.swim_next)
        return

    await message.answer(texts.t25, reply_markup=kb.found_qr)
    await State.state3.set()

@dp.message_handler(state=State.state3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.found:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.found_qr)
        return

    await message.answer(texts.t27)
    await State.ans2.set()

@dp.message_handler(state=State.ans2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() != answers.answer2.lower():
        random_answer = random.choice(texts.wrong_ans)
        await message.answer(random_answer)
        return 
    await message.answer(texts.t28)
    with open('images/Гидрокостюм.png', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.t29)
    await message.answer(texts.t30, reply_markup=kb.swim_next)
    await State.state4.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 10, datetime_str)



@dp.message_handler(state=State.state4)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.swim_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.swim_next)
        return

    await message.answer(texts.t31, reply_markup=kb.found_qr)
    await State.state5.set()

@dp.message_handler(state=State.state5)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.found:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.found_qr)
        return

    await message.answer(texts.t33)
    await State.ans3.set()

@dp.message_handler(state=State.ans3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() != answers.answer3.lower():
        random_answer = random.choice(texts.wrong_ans)
        await message.answer(random_answer)
        return 
    await message.answer(texts.t34)
    with open('images/Очки.png', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.t35)
    await message.answer(texts.t36, reply_markup=kb.swim_next)
    await State.state6.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 11, datetime_str)



@dp.message_handler(state=State.state6)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.swim_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.swim_next)
        return

    await message.answer(texts.t37, reply_markup=kb.found_qr)
    await State.state7.set()

@dp.message_handler(state=State.state7)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.found:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.found_qr)
        return

    await message.answer(texts.t38)
    await State.ans4.set()

@dp.message_handler(state=State.ans4)
async def send_welcome(message: types.Message, state: FSMContext):
    if not (message.text.lower() in answers.answer4):
        random_answer = random.choice(texts.wrong_ans)
        await message.answer(random_answer)
        return 
    await message.answer(texts.t39)
    with open('images/Буй.png', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.t40)
    await message.answer(texts.t41, reply_markup=kb.swim_next)
    await State.state8.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 12, datetime_str)



@dp.message_handler(state=State.state8)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.swim_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.swim_next)
        return

    # await message.answer(texts.t42)
    await message.answer(texts.t42, reply_markup=kb.found_qr)
    await State.state9.set()

@dp.message_handler(state=State.state9)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.found:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.found_qr)
        return
    # voice = InputFile('audio/Плавание_Памятник студентам.mp3')
    # await message.answer_voice(voice, caption=texts.t43)
    await message.answer(texts.t44)
    await State.ans5.set()

@dp.message_handler(state=State.ans5)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() != answers.answer5.lower():
        random_answer = random.choice(texts.wrong_ans)
        await message.answer(random_answer)
        return 
    await message.answer(texts.t45)
    with open('images/Шапочка.png', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.t46)
    await message.answer(texts.t47, reply_markup=kb.yn)
    await State.state111.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 13, datetime_str)


@dp.message_handler(state=State.state111)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == buttons.y:
        await message.answer(texts.t100, reply_markup=kb.trans)
        await State.state10.set()
    elif message.text == buttons.n:
        # await message.answer(texts.t101)
        await message.answer(texts.t102, reply_markup=kb.trans)
        await State.state10.set()
    else:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.yn)

    

    