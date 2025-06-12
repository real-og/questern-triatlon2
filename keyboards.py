from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import buttons

number_btn = KeyboardButton(buttons.number, request_contact=True)
number_kb = ReplyKeyboardMarkup([[number_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)


def get_game_kb(selected: list):
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='✅' if buttons.run in selected else buttons.run, callback_data=buttons.run)
    button_2 = InlineKeyboardButton(text='✅' if buttons.velo in selected else buttons.velo, callback_data=buttons.velo)
    button_3 = InlineKeyboardButton(text='✅' if buttons.swim in selected else buttons.swim, callback_data=buttons.swim)


    kb.row(button_1, button_2, button_3)
    return kb

start = ReplyKeyboardMarkup([[buttons.start]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

start_swim_terms = ReplyKeyboardMarkup([[buttons.terms_swim]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

start_swim = ReplyKeyboardMarkup([[buttons.start_swim]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

found_qr = ReplyKeyboardMarkup([[buttons.found]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

swim_next = ReplyKeyboardMarkup([[buttons.swim_next]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

trans = ReplyKeyboardMarkup([[buttons.transit]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

start_velo_terms = ReplyKeyboardMarkup([[buttons.terms_velo]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

start_velo = ReplyKeyboardMarkup([[buttons.start_velo]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

finish_velo = ReplyKeyboardMarkup([[buttons.end_velo]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

zero_km = ReplyKeyboardMarkup([[buttons.zero_km]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

make_velo = ReplyKeyboardMarkup([[buttons.make_velo]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

terms_run = ReplyKeyboardMarkup([[buttons.terms_run]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

start_run = ReplyKeyboardMarkup([[buttons.start_run]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

run = ReplyKeyboardMarkup([[buttons.came, buttons.need_hint]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

yn = ReplyKeyboardMarkup([[buttons.y, buttons.n]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

go_next = ReplyKeyboardMarkup([[buttons.go_next]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

