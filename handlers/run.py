from loader import dp, GROUP_CHAT_ID_PHOTO, GROUP_CHAT_ID_FEED, bot
from aiogram import types
import time
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
from aiogram import types
import random
from math import radians, sin, cos, sqrt, atan2
def is_within_500m(lat_str: str, lon_str: str) -> bool:
    # фиксированная точка
    lat0, lon0 = 43.400374, 39.948611  
    R = 6371000  # радиус Земли в метрах

    # преобразуем строки в float
    lat, lon = float(lat_str), float(lon_str)

    # переводим градусы в радианы
    phi1, phi2 = radians(lat0), radians(lat)
    dphi = radians(lat - lat0)
    dlambda = radians(lon - lon0)

    # формула гаверсинуса
    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    dist = R * c

    return dist <= 500



# @dp.message_handler(state=State.finish_velo)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text != buttons.end_velo:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.finish_velo)
#         return

#     await message.answer(texts.t65, reply_markup=kb.zero_km)
#     await State.st1.set()



@dp.message_handler(state=State.st1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.came:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.came)
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
    await message.answer(texts.t69, reply_markup=kb.terms_run)
    await State.wait_terms_run.set()


@dp.message_handler(state=State.wait_terms_run)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.terms_run:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.terms_run)
        return
    await message.answer(texts.dop_rule)
    await message.answer(texts.t71, reply_markup=kb.start_run)
    await State.wait_start_run.set()


@dp.message_handler(state=State.wait_start_run)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.start_run:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.start_run)
        return
    
    with open('images_sochi/run1_big.jpeg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.caption_run)
    voice = InputFile("audio_sochi/run1_1.ogg")  
    await message.answer_voice(voice=voice, reply_markup=kb.donthear)
    await State.run1.set()
    await state.update_data(start_run_time=int(time.time()))
    utc_plus_3 = timezone(timedelta(hours=3))
    now_utc3 = datetime.now(utc_plus_3)
    datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
    await aiotable.update_cell(message.from_user.id, 19, datetime_str)



@dp.callback_query_handler(state=State.run1)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    file = InputFile("audio_sochi/run1.mp3", 'Voice message')
    await callback.message.answer_audio(file, caption='Надеюсь, так лучше', performer='Max')

@dp.callback_query_handler(state=State.run2)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    file = InputFile("audio_sochi/run2.mp3", 'Voice message')
    await callback.message.answer_audio(file, caption='Надеюсь, так лучше', performer='Max')

@dp.callback_query_handler(state=State.run3)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    file = InputFile("audio_sochi/run3.mp3", 'Voice message')
    await callback.message.answer_audio(file, caption='Надеюсь, так лучше', performer='Max')

@dp.callback_query_handler(state=State.run4)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    file = InputFile("audio_sochi/run4.mp3", 'Voice message')
    await callback.message.answer_audio(file, caption='Надеюсь, так лучше', performer='Max')

@dp.callback_query_handler(state=State.run5)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    file = InputFile("audio_sochi/run5.mp3", 'Voice message')
    await callback.message.answer_audio(file, caption='Надеюсь, так лучше', performer='Max')

@dp.callback_query_handler(state=State.run6)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback.id)
    file = InputFile("audio_sochi/run6.mp3", 'Voice message')
    await callback.message.answer_audio(file, caption='Надеюсь, так лучше', performer='Max')


@dp.message_handler(content_types=['any'], state=State.run1)
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(random.choice(texts.run_answers))
        with open('images/r.png', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer('Готов двигаться дальше? Жми на кнопку ⤵️', reply_markup=kb.go_next)
        await State.run_before2.set()
    else:
        await message.answer(texts.need_photo)

@dp.message_handler(state=State.run_before2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.go_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.go_next)
        return
    with open('images_sochi/run2.jpeg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.caption_run)
    voice = InputFile("audio_sochi/run2_1.ogg")  
    await message.answer_voice(voice=voice, reply_markup=kb.donthear)
    await State.run2.set()



@dp.message_handler(content_types=['any'], state=State.run2)
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(random.choice(texts.run_answers))
        with open('images/n.png', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer('Готов двигаться дальше? Жми на кнопку ⤵️', reply_markup=kb.go_next)
        await State.run_before3.set()
    else:
        await message.answer(texts.need_photo)

@dp.message_handler(state=State.run_before3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.go_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.go_next)
        return
    with open('images_sochi/run3.jpeg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.caption_run)
    voice = InputFile("audio_sochi/run3_1.ogg")  
    await message.answer_voice(voice=voice, reply_markup=kb.donthear)
    await State.run3.set()



@dp.message_handler(content_types=['any'], state=State.run3)
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(random.choice(texts.run_answers))
        with open('images/i.png', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer('Готов двигаться дальше? Жми на кнопку ⤵️', reply_markup=kb.go_next)
        await State.run_before4.set()
    else:
        await message.answer(texts.need_photo)

@dp.message_handler(state=State.run_before4)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.go_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.go_next)
        return
    with open('images_sochi/run4.jpeg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.caption_run)
    voice = InputFile("audio_sochi/run4_1.ogg")  
    await message.answer_voice(voice=voice, reply_markup=kb.donthear)
    await State.run4.set()




@dp.message_handler(content_types=['any'], state=State.run4)
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(random.choice(texts.run_answers))
        with open('images/t.png', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer('Готов двигаться дальше? Жми на кнопку ⤵️', reply_markup=kb.go_next)
        await State.run_before5.set()
    else:
        await message.answer(texts.need_photo)

@dp.message_handler(state=State.run_before5)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.go_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.go_next)
        return
    with open('images_sochi/run5.jpeg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.caption_run)
    voice = InputFile("audio_sochi/run5_1.ogg")  
    await message.answer_voice(voice=voice, reply_markup=kb.donthear)
    await State.run5.set()



@dp.message_handler(content_types=['any'], state=State.run5)
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(random.choice(texts.run_answers))
        with open('images/p.png', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer('Готов двигаться дальше? Жми на кнопку ⤵️', reply_markup=kb.go_next)
        await State.run_before6.set()
    else:
        await message.answer(texts.need_photo)

@dp.message_handler(state=State.run_before6)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.go_next:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.go_next)
        return
    with open('images_sochi/run6.jpeg', 'rb') as photo:
        await message.answer_photo(photo, caption=texts.caption_run)
    voice = InputFile("audio_sochi/run6_1.ogg")  
    await message.answer_voice(voice=voice, reply_markup=kb.donthear)
    await State.run6.set()


@dp.message_handler(content_types=['any'], state=State.run6)
async def handle_photo(message: types.Message):
    if message.photo and (not message.media_group_id):
        f = await message.forward(chat_id=GROUP_CHAT_ID_PHOTO)
        await message.answer(random.choice(texts.run_answers))
        with open('images/s.png', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer(texts.t88)
        await State.answ7.set()
        
    else:
        await message.answer(texts.need_photo)

# @dp.message_handler(state=State.wait_start_run)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text != buttons.start_run:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.start_run)
#         return
    
#     voice = InputFile("audio_ekb/voice1.ogg")  
#     await message.answer_voice(voice=voice)
#     await message.answer(texts.t73, reply_markup=kb.run)
#     await State.run1.set()
#     await state.update_data(start_run_time=int(time.time()))
#     utc_plus_3 = timezone(timedelta(hours=3))
#     now_utc3 = datetime.now(utc_plus_3)
#     datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#     await aiotable.update_cell(message.from_user.id, 19, datetime_str)


# @dp.message_handler(state=State.run1)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.need_hint:
#         await message.answer(texts.t74, reply_markup=kb.run)
#         return
#     if message.text == buttons.came:
#         await message.answer(texts.t75)
#         await State.answ1.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.run)



# @dp.message_handler(state=State.answ1)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text.lower() == answers.answer6.lower():
#         with open('images/Буква1.png', 'rb') as photo:
#             await message.answer_photo(photo, caption='Верно 👍 ')
#         # voice = InputFile("audio_ekb/voice2.ogg")
#         # await message.answer_voice(voice=voice)
#         await message.answer(texts.t78, reply_markup=kb.go_next)
#         await State.run22.set()
#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 20, datetime_str)
#     else:
#         texts.wrong_run
#         await message.answer(texts.wrong_run)


# @dp.message_handler(state=State.run22)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.go_next:
#         voice = InputFile("audio_ekb/voice2.ogg")
#         await message.answer_voice(voice=voice)
#         await message.answer(texts.t73, reply_markup=kb.run)
#         await State.run2.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.go_next)



# @dp.message_handler(state=State.run2)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.need_hint:
#         await message.answer(texts.t76, reply_markup=kb.run)
#         return
#     if message.text == buttons.came:
#         await message.answer(texts.t77)
#         await State.answ2.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.run)

# @dp.message_handler(state=State.answ2)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text.lower() == answers.answer7.lower():
#         with open('images/Буква Н.png', 'rb') as photo:
#             await message.answer_photo(photo, caption='Верно 👍 ')
#         await message.answer(texts.t107, parse_mode=types.ParseMode.MARKDOWN_V2)
#         await State.answ3.set()
#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 21, datetime_str)
#     else:
#         await message.answer(texts.wrong_run)







# @dp.message_handler(state=State.answ3)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text.upper() in answers.answer9:
#         with open('images/Буква И.png', 'rb') as photo:
#             await message.answer_photo(photo, caption='Верно 👍 ')
#         await message.answer(texts.t78, reply_markup=kb.go_next)
#         await State.run3.set()
#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 22, datetime_str)
        
#     else:
#         await message.answer(texts.wrong_run)



# @dp.message_handler(state=State.run3)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.go_next:
#         voice = InputFile("audio_ekb/voice3.ogg")
#         await message.answer_voice(voice=voice)
#         await message.answer(texts.t73, reply_markup=kb.run)
#         await State.run4.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.go_next)



# @dp.message_handler(state=State.run4)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.need_hint:
#         await message.answer(texts.t79, reply_markup=kb.run)
#         return
#     if message.text == buttons.came:
#         await message.answer(texts.t80)
#         await State.answ4.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.run)


# @dp.message_handler(state=State.answ4)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text.lower() in answers.answer13:
#         with open('images/Буква Т.png', 'rb') as photo:
#             await message.answer_photo(photo, caption='Верно 👍 ')
#         await message.answer(texts.t78, reply_markup=kb.go_next)
#         await State.run5.set()
#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 23, datetime_str)

#     else:
#         await message.answer(texts.wrong_run)


# @dp.message_handler(state=State.run5)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.go_next:
#         voice = InputFile("audio_ekb/voice4.ogg")
#         await message.answer_voice(voice=voice)
#         await message.answer(texts.t73, reply_markup=kb.run)
#         await State.run6.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.go_next)


# @dp.message_handler(state=State.run6)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.need_hint:
#         await message.answer(texts.t83, reply_markup=kb.run)
#         return
#     if message.text == buttons.came:
#         await message.answer(texts.t84)
#         await State.answ5.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.run)


# @dp.message_handler(state=State.answ5)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text.lower() == answers.answer10.lower():
#         with open('images/Буква П.png', 'rb') as photo:
#             await message.answer_photo(photo, caption='Верно 👍 ')
#         await message.answer(texts.t78, reply_markup=kb.go_next)
#         await State.run7.set()
#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 24, datetime_str)
#     else:
#         await message.answer(texts.wrong_run)


# @dp.message_handler(state=State.run7)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.go_next:
#         voice = InputFile("audio_ekb/voice5_1.ogg")
#         await message.answer_voice(voice=voice)
#         await message.answer(texts.t73, reply_markup=kb.run)
#         await State.run8.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.go_next)



# @dp.message_handler(state=State.run8)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.need_hint:
#         await message.answer(texts.t86, reply_markup=kb.run)
#         return
#     if message.text == buttons.came:
#         await message.answer(texts.t87)
#         await State.answ6.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.run)


# @dp.message_handler(state=State.answ6)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text.lower() == answers.answer14.lower():
#         with open('images/Буква С.png', 'rb') as photo:
#             await message.answer_photo(photo, caption='Верно 👍 ')
#         await message.answer(texts.t88, reply_markup=ReplyKeyboardRemove())
#         await State.answ7.set()
#         utc_plus_3 = timezone(timedelta(hours=3))
#         now_utc3 = datetime.now(utc_plus_3)
#         datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
#         await aiotable.update_cell(message.from_user.id, 25, datetime_str)
#     else:
#         await message.answer(texts.wrong_run)


@dp.message_handler(state=State.answ7)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.lower() == 'спринт':
        await message.answer(texts.t90)
        await message.answer(texts.t92, reply_markup=kb.place)
        await State.before_geo.set()
    else:
        await message.answer(texts.t89)


@dp.message_handler(state=State.before_geo)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text != buttons.place:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.place)
        return
    await message.answer(texts.ask_geo, reply_markup=kb.geo)
    await State.enter_geo.set()


@dp.message_handler(state=State.enter_geo, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    if not message.location:
        await message.answer('Поделитесь геолокацией', reply_markup=kb.geo)
        return
    lat = message.location.latitude
    lon = message.location.longitude
    if is_within_500m(str(lat), str(lon)):
        with open('images/kross.png', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.caption_kross, reply_markup=kb.endend)
            await State.finish.set()
    else:
        await message.answer(random.choice(texts.wrong_geo), reply_markup=kb.geo)
        await State.bad_geo.set()


@dp.message_handler(state=State.bad_geo, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    if not message.location:
        await message.answer('Поделитесь геолокацией', reply_markup=kb.geo)
        return
    lat = message.location.latitude
    lon = message.location.longitude
    if is_within_500m(str(lat), str(lon)):
        with open('images/kross.png', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.caption_kross, reply_markup=kb.endend)
            await State.finish.set()
    else:
        await message.answer("Возможно, это сбой GPS. Будем считать, что ты на месте! 👌")
        with open('images/kross.png', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.caption_kross, reply_markup=kb.endend)
            await State.finish.set()

    



@dp.message_handler(state=State.finish)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == buttons.finish:
        now = int(time.time())
        data = await state.get_data()
        start_time = int(data.get('start_run_time'))
        await message.answer(texts.generate_run_reult(now - start_time))
        await message.answer(texts.t93, reply_markup=kb.see_ammo)
        await State.ammo.set()
        utc_plus_3 = timezone(timedelta(hours=3))
        now_utc3 = datetime.now(utc_plus_3)
        datetime_str = now_utc3.strftime("%Y-%m-%d %H:%M:%S")
        await aiotable.update_cell(message.from_user.id, 20, datetime_str)
    else:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.endend)


@dp.message_handler(state=State.ammo)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == buttons.see_ammo:
        with open('images/Экипировка.png', 'rb') as photo:
            await message.answer_photo(photo, caption=texts.t94)
        # with open('ekb.mp4', 'rb') as video:
        #     await message.answer_video(video, caption='🔗 https://vk.com/video-70227637_456240754')
        # await message.answer('https://youtu.be/tPNoe27_GKg?feature=shared')
        await message.answer(texts.t95, disable_web_page_preview=True)
        await message.answer(texts.t97, reply_markup=ReplyKeyboardRemove())
        # await message.answer(texts.t96, reply_markup=kb.gift)
        await State.feed.set() 
    else:
        await message.answer(texts.wrong_btn_input, reply_markup=kb.see_ammo)


# @dp.message_handler(state=State.gift)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == buttons.get_present:
#         await message.answer(texts.t97, reply_markup=ReplyKeyboardRemove())
#         await State.feed.set()
#     else:
#         await message.answer(texts.wrong_btn_input, reply_markup=kb.gift)


@dp.message_handler(state=State.feed)
async def send_welcome(message: types.Message, state: FSMContext):
    try:
        await message.forward(GROUP_CHAT_ID_FEED)
    except:
        pass
    await message.answer(texts.t98)
    await State.after_end.set()


@dp.message_handler(state=State.after_end)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.after_end, disable_web_page_preview=True)

    

    


