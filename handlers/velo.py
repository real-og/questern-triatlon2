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


@dp.message_handler(state=State.state10)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.transit:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.trans)
        return

    await message.answer(texts.t49)
    with open('images/Велосипедист.jpeg', 'rb') as photo:
        await message.answer_photo(photo)

    await message.answer(texts.t50, reply_markup=kb.start_velo_terms)
    await State.wait_start_velo_terms.set()


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
    with open('images/кошки.png', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.t54)
    await message.answer(texts.t55, parse_mode=types.ParseMode.MARKDOWN_V2)
    await State.wait_photo1.set()

@dp.message_handler(content_types=['any'], state=State.wait_photo1)
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(texts.t104)
        with open('images/мотоцикл.png', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.t56)
        await message.answer(texts.t57, parse_mode=types.ParseMode.MARKDOWN_V2)
        await State.wait_photo2.set()
    else:
        await message.answer(texts.photo_need)


@dp.message_handler(content_types=['any'], state=State.wait_photo2)
# @dp.message_handler(content_types=['photo'], state='*')
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(texts.t105)
        with open('images/дом Буркова.png', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.t58)
        await message.answer(texts.t59, parse_mode=types.ParseMode.MARKDOWN_V2)
        await State.wait_photo3.set()
    else:
        await message.answer(texts.photo_need)


@dp.message_handler(content_types=['any'], state=State.wait_photo3)
# @dp.message_handler(content_types=['photo'], state='*')
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(texts.t106)
        with open('images/сквер виолончель.png', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.t60)
        await message.answer(texts.t61, parse_mode=types.ParseMode.MARKDOWN_V2)
        await State.wait_photo4.set()
    else:
        await message.answer(texts.photo_need)


@dp.message_handler(content_types=['any'], state=State.wait_photo4)
# @dp.message_handler(content_types=['photo'], state='*')
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(texts.t104)
        with open('images/фонтан.png', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.t62)
        await message.answer(texts.t63, parse_mode=types.ParseMode.MARKDOWN_V2)
        await State.wait_photo5.set()
    else:
        await message.answer(texts.photo_need)


@dp.message_handler(content_types=['any'], state=State.wait_photo5)
# @dp.message_handler(content_types=['photo'], state='*')
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(texts.t105)
        await message.answer(texts.t64, reply_markup=kb.finish_velo)
        await State.finish_velo.set()
    else:
        await message.answer(texts.photo_need)

    