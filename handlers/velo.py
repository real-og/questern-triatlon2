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
from aiogram.types import ReplyKeyboardRemove
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
        # video = InputFile("ekb.mp4")
        # await message.answer_video(
        #     video=video,
        #     supports_streaming=True,
        #     caption='🔗 https://vk.com/video-70227637_456240754'
        # )
        await message.answer(texts.t95, disable_web_page_preview=True)
        await message.answer(texts.t97, reply_markup=ReplyKeyboardRemove())
        await State.feed.set() 
        utc_plus_3 = timezone(timedelta(hours=3))
        now_utc3 = datetime.now(utc_plus_3)
        datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
        await aiotable.update_cell(message.from_user.id, 21, datetime_str)
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
    await message.answer(texts.t53, reply_markup=kb.start_velo)
    await State.wait_start_velo.set()





@dp.message_handler(state=State.wait_start_velo)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.start_velo:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.start_velo)
        return
    await message.answer(texts.t544)
    await message.answer(texts.t5444, reply_markup=ReplyKeyboardRemove())
    await State.wait_velo_ans1.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 14, datetime_str)


@dp.message_handler(state=State.wait_velo_ans1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() == 'тридцать три':
        await message.answer('На буквах ты далеко не уедешь. Напиши ответ числом.')
    elif message.text == '33':
        with open('images/rule.png', 'rb') as photo:
            await message.answer_photo(photo, caption='Идеальный старт! Держи руль — теперь каждый твой поворот будет чётким. Вперёд, к следующему муралу!')
        await message.answer('Нажми на кнопку, чтобы продолжить ⤵️', reply_markup=kb.drive_next)
        await State.before_velo_2.set()
    else:
        await message.answer('Неверно')


@dp.message_handler(state=State.before_velo_2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.drive_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.drive_next)
        return
    await message.answer(texts.tvelo2)
    await State.wait_velo_ans2.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 15, datetime_str)
    


@dp.message_handler(state=State.wait_velo_ans2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() == 'двадцать семь':
        await message.answer('На буквах ты далеко не уедешь. Напиши ответ числом.')
    elif message.text == '27':
        with open('images/rama.png', 'rb') as photo:
            await message.answer_photo(photo, caption='А ты уловил суть! 👏  Держи раму — основу твоего будущего болида.')
        await message.answer('Нажми на кнопку, чтобы продолжить ⤵️', reply_markup=kb.drive_next)
        await State.before_velo_3.set()
    else:
        await message.answer('Неверно')


@dp.message_handler(state=State.before_velo_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.drive_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.drive_next)
        return
    await message.answer(texts.tvelo3)
    await State.wait_velo_ans3.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 16, datetime_str)


@dp.message_handler(state=State.wait_velo_ans3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() == 'двадцать три':
        await message.answer('На буквах ты далеко не уедешь. Напиши ответ числом.')
    elif message.text == '23':
        with open('images/trans.png', 'rb') as photo:
            await message.answer_photo(photo, caption='У тебя звериная скорость! А твоя добыча — трансмиссия ⚙️ Так держать! 👏')
        await message.answer('Нажми на кнопку, чтобы продолжить ⤵️', reply_markup=kb.drive_next)
        await State.before_velo_4.set()
    else:
        await message.answer('Неверно')


@dp.message_handler(state=State.before_velo_4)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.drive_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.drive_next)
        return
    await message.answer(texts.tvelo4)
    await State.wait_velo_ans4.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 17, datetime_str)
    

@dp.message_handler(state=State.wait_velo_ans4)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() == 'девятнадцать':
        await message.answer('На буквах ты далеко не уедешь. Напиши ответ числом.')
    elif message.text == '19':
        with open('images/sedlo.png', 'rb') as photo:
            await message.answer_photo(photo, caption='Дух дракона и сила скакуна на твоей стороне! Держи седло — теперь ты и твой велосипед едины. Остался последний рывок! 👍')
        await message.answer('Нажми на кнопку, чтобы продолжить ⤵️', reply_markup=kb.drive_next)
        await State.before_velo_5.set()
    else:
        await message.answer('Неверно')


@dp.message_handler(state=State.before_velo_5)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.drive_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.drive_next)
        return
    await message.answer(texts.tvelo5)
    await State.wait_velo_ans5.set()
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 18, datetime_str)


@dp.message_handler(state=State.wait_velo_ans5)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() == 'семь':
        await message.answer('На буквах ты далеко не уедешь. Напиши ответ числом.')
    elif message.text == '7':
        with open('images/koles.png', 'rb') as photo:
            await message.answer_photo(photo, caption='Фантастика! 🤩 Ты справился и почувствовал ритм гонки. Держи колесо! Точнее, вот тебе оба колеса. Ты их заслужил! 😄')
        await message.answer(texts.t67, reply_markup=kb.make_velo)
        await State.st2.set()


    else:
        await message.answer('Неверно')






# @dp.message_handler(content_types=['any'], state=State.wait_photo1)
# async def handle_photo(message: types.Message):
#     if message.photo and (not message.media_group_id):
#         f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
#         cache[f.message_id] = message.from_user.id
#         await message.answer(texts.t104)
#         with open('images_ekb/tower.JPG', 'rb') as photo:
#             await message.answer_photo(photo)
#         await message.answer(texts.t55, parse_mode=types.ParseMode.MARKDOWN_V2)
#         await State.wait_photo4.set()

#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 17, datetime_str)
#     else:
#         await message.answer(texts.photo_need)


# @dp.message_handler(content_types=['any'], state=State.wait_photo2)
# # @dp.message_handler(content_types=['photo'], state='*')
# async def handle_photo(message: types.Message):
#     if message.photo and (not message.media_group_id):
#         f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
#         cache[f.message_id] = message.from_user.id
#         await message.answer(texts.t105)
#         with open('images_ekb/hole.PNG', 'rb') as photo:
#             await message.answer_photo(photo)
#         await message.answer(texts.t59, parse_mode=types.ParseMode.MARKDOWN_V2)
#         await State.wait_photo3.set()
#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 15, datetime_str)
#     else:
#         await message.answer(texts.photo_need)


# @dp.message_handler(content_types=['any'], state=State.wait_photo3)
# # @dp.message_handler(content_types=['photo'], state='*')
# async def handle_photo(message: types.Message):
#     if message.photo and (not message.media_group_id):
#         f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
#         cache[f.message_id] = message.from_user.id
#         await message.answer(texts.t104)
#         with open('images_ekb/sevastian.JPG', 'rb') as photo:
#             await message.answer_photo(photo)
#         await message.answer(texts.t61, parse_mode=types.ParseMode.MARKDOWN_V2)
#         await State.wait_photo1.set()
#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 16, datetime_str)
#     else:
#         await message.answer(texts.photo_need)


# @dp.message_handler(content_types=['any'], state=State.wait_photo4)
# # @dp.message_handler(content_types=['photo'], state='*')
# async def handle_photo(message: types.Message):
#     if message.photo and (not message.media_group_id):
#         f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
#         cache[f.message_id] = message.from_user.id
#         await message.answer(texts.t104)
#         with open('images_ekb/house.png', 'rb') as photo:
#             await message.answer_photo(photo)
#         await message.answer(texts.t63, parse_mode=types.ParseMode.MARKDOWN_V2)
#         await State.wait_photo5.set()
#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 18, datetime_str)
#     else:
#         await message.answer(texts.photo_need)


# @dp.message_handler(content_types=['any'], state=State.wait_photo5)
# # @dp.message_handler(content_types=['photo'], state='*')
# async def handle_photo(message: types.Message):
#     if message.photo and (not message.media_group_id):
#         f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
#         cache[f.message_id] = message.from_user.id
#         # await message.answer(texts.t105)
#         await message.answer(texts.t65, reply_markup=kb.came)
#         await State.st1.set()
#     else:
#         await message.answer(texts.photo_need)

    