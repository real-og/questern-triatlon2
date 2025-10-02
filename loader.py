from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import logging
import os


logging.basicConfig(level=logging.WARNING)
ADMIN_ID = str(os.environ.get('ADMIN_ID'))
BOT_TOKEN = str(os.environ.get('BOT_TOKEN'))
SHEET_LINK = str(os.environ.get('SHEET_LINK'))
GROUP_CHAT_ID_PHOTO = '-4983295124'
GROUP_CHAT_ID_FEED = '-4977101733'

storage = RedisStorage2(db=2)


bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)