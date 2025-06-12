from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
from states import State
import keyboards as kb
import aiotable
import buttons
CODE = [buttons.swim, buttons.velo, buttons.run]


@dp.callback_query_handler(state=State.playing_game)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    tapped_butt = callback.data
    data = await state.get_data()
    selected_butts = data.get('selected_butts')

    position = len(selected_butts)


    if CODE[position] == str(tapped_butt):
        selected_butts.append(tapped_butt)
    else:
        selected_butts = []

    try:
        await bot.edit_message_reply_markup(callback.message.chat.id,
                            callback.message.message_id,
                            reply_markup=kb.get_game_kb(selected_butts))
    except:
        pass
    if len(selected_butts) == 3:
        selected_butts = []
        await callback.message.answer(texts.t10)
        await callback.message.answer(texts.t11)
        await callback.message.answer(texts.t12)
        await callback.message.answer(texts.t13, reply_markup=kb.start)
        await State.wait_for_start.set()

    await state.update_data(selected_butts=selected_butts) 
    await bot.answer_callback_query(callback.id)