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
from logic import cache



@dp.message_handler(state=State.state10)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.transit:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.trans)
        return

    await message.answer(texts.t49, reply_markup=kb.early_finish)
    await State.choose_option.set()


@dp.message_handler(state=State.choose_option)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == buttons.end_early:
        await message.answer(texts.t49_1)
        video = InputFile("ekb.mp4")
        await message.answer_video(
            video=video,
            supports_streaming=True,
            caption='🔗 https://vk.com/video-70227637_456240754'
        )
        await message.answer(texts.t49_2, reply_markup=kb.gift)
        await State.gift.set()
        utc_plus_3 = timezone(timedelta(hours=3))
        now_utc3 = datetime.now(utc_plus_3)
        datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
        await aiotable.update_cell(message.from_user.id, 26, datetime_str)
    elif message.text == buttons.continue_quest:
        await message.answer(texts.t49_3)
        with open('images_ekb/velosipedist.JPG', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.t50, reply_markup=kb.start_velo_terms)
        await State.wait_start_velo_terms.set()
    else:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.early_finish)



@dp.message_handler(state=State.wait_start_velo_terms)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.terms_velo:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.start_velo_terms)
        return
    await message.answer(texts.t51)
    await message.answer(texts.t52)
    await message.answer(texts.t53, reply_markup=kb.start_velo)
    await State.wait_start_velo.set()





@dp.message_handler(state=State.wait_start_velo)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.start_velo:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.start_velo)
        return
    with open('images_ekb/pole.PNG', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.t544)
    await message.answer(texts.t5444, parse_mode=types.ParseMode.MARKDOWN_V2)
    await State.wait_photo2.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 14, datetime_str)


@dp.message_handler(content_types=['any'], state=State.wait_photo1)
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        cache[f.message_id] = message.from_user.id
        await message.answer(texts.t104)
        with open('images_ekb/tower.JPG', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.t55, parse_mode=types.ParseMode.MARKDOWN_V2)
        await State.wait_photo4.set()

        utc_plus_3 = timezone(timedelta(hours=3))
        now_utc3 = datetime.now(utc_plus_3)
        datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
        await aiotable.update_cell(message.from_user.id, 17, datetime_str)
    else:
        await message.answer(texts.photo_need)


@dp.message_handler(content_types=['any'], state=State.wait_photo2)
# @dp.message_handler(content_types=['photo'], state='*')
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        cache[f.message_id] = message.from_user.id
        await message.answer(texts.t105)
        with open('images_ekb/hole.PNG', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.t59, parse_mode=types.ParseMode.MARKDOWN_V2)
        await State.wait_photo3.set()
        utc_plus_3 = timezone(timedelta(hours=3))
        now_utc3 = datetime.now(utc_plus_3)
        datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
        await aiotable.update_cell(message.from_user.id, 15, datetime_str)
    else:
        await message.answer(texts.photo_need)


@dp.message_handler(content_types=['any'], state=State.wait_photo3)
# @dp.message_handler(content_types=['photo'], state='*')
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        cache[f.message_id] = message.from_user.id
        await message.answer(texts.t104)
        with open('images_ekb/sevastian.JPG', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.t61, parse_mode=types.ParseMode.MARKDOWN_V2)
        await State.wait_photo1.set()
        utc_plus_3 = timezone(timedelta(hours=3))
        now_utc3 = datetime.now(utc_plus_3)
        datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
        await aiotable.update_cell(message.from_user.id, 16, datetime_str)
    else:
        await message.answer(texts.photo_need)


@dp.message_handler(content_types=['any'], state=State.wait_photo4)
# @dp.message_handler(content_types=['photo'], state='*')
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        cache[f.message_id] = message.from_user.id
        await message.answer(texts.t104)
        with open('images_ekb/house.png', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.t63, parse_mode=types.ParseMode.MARKDOWN_V2)
        await State.wait_photo5.set()
        utc_plus_3 = timezone(timedelta(hours=3))
        now_utc3 = datetime.now(utc_plus_3)
        datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
        await aiotable.update_cell(message.from_user.id, 18, datetime_str)
    else:
        await message.answer(texts.photo_need)


@dp.message_handler(content_types=['any'], state=State.wait_photo5)
# @dp.message_handler(content_types=['photo'], state='*')
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        cache[f.message_id] = message.from_user.id
        # await message.answer(texts.t105)
        await message.answer(texts.t65, reply_markup=kb.came)
        await State.st1.set()
    else:
        await message.answer(texts.photo_need)

    