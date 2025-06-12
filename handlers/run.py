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


@dp.message_handler(state=State.finish_velo)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.end_velo:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.finish_velo)
        return

    await message.answer(texts.t65)
    await message.answer(texts.t66, reply_markup=kb.zero_km)
    await State.st1.set()


@dp.message_handler(state=State.st1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.zero_km:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.zero_km)
        return

    await message.answer(texts.t67, reply_markup=kb.make_velo)
    await State.st2.set()


@dp.message_handler(state=State.st2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.make_velo:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.make_velo)
        return
    video = InputFile("images/Велик со звуком.mov")
    await message.answer_video(video)
    await message.answer(texts.t68)
    await message.answer(texts.t69)
    await message.answer(texts.t70, reply_markup=kb.terms_run)
    await State.wait_terms_run.set()


@dp.message_handler(state=State.wait_terms_run)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.terms_run:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.terms_run)
        return
    await message.answer(texts.t71)
    await message.answer(texts.t72, reply_markup=kb.start_run)
    await State.wait_start_run.set()





@dp.message_handler(state=State.wait_start_run)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.start_run:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.start_run)
        return
    
    voice = InputFile("compressed/Бег_1.ogg")  
    await message.answer_voice(chat_id=message.chat.id, voice=voice)
    await message.answer(texts.t73, reply_markup=kb.run)
    await State.run1.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await state.update_data(start_run_time=datetime_str)


@dp.message_handler(state=State.run1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == buttons.need_hint:
        await message.answer(texts.t74, reply_markup=kb.run)
        return
    if message.text == buttons.came:
        await message.answer(texts.t75, reply_markup=kb.start_run)
        await State.answ1.set()
    else:
        message.answer(texts.wrong_btn_input, reply_markup=kb.run)

@dp.message_handler(state=State.answ1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() == answers.answer6.lower():
        with open('images/Буква Р.png', 'rb') as photo:
            await message.answer_photo(photo, caption='Верно 👍 ')
        voice = InputFile("compressed/Бег_3.ogg")
        await message.answer_voice(chat_id=message.chat.id, voice=voice)
        message.answer(texts.t73, reply_markup=kb.run)
        await State.run2.set()
    else:
        message.answer("Неверно(")



@dp.message_handler(state=State.run2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == buttons.need_hint:
        await message.answer(texts.t76, reply_markup=kb.run)
        return
    if message.text == buttons.came:
        await message.answer(texts.t77)
        await State.answ2.set()
    else:
        message.answer(texts.wrong_btn_input, reply_markup=kb.run)

@dp.message_handler(state=State.answ2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() == answers.answer7.lower():
        with open('images/Буква Н.png', 'rb') as photo:
            await message.answer_photo(photo, caption='Верно 👍 ')
        voice = InputFile("compressed/Бег_3.ogg")
        await message.answer_voice(chat_id=message.chat.id, voice=voice)
        message.answer(texts.t73, reply_markup=kb.run)
        await State.run2.set()
    else:
        message.answer("Неверно(")


    


