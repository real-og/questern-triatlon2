import json
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import BotBlocked, ChatNotFound
from loader import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def main():
    # Загрузка updates.json
    with open("updates.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    user_ids = set()
    for update in data.get("result", []):
        msg = update.get("message")
        if msg and msg.get("text") == "/start":
            user_id = msg["from"]["id"]
            user_ids.add(user_id)

    print(f"Найдено {len(user_ids)} уникальных пользователей.")

    text = """Готов к приключениям? 🚀 Регистрация на квест открыта! Жми /start и погнали! 💪"""

    for user_id in user_ids:
        try:
            await bot.send_message(user_id, text)
            print(f"✅ Сообщение отправлено {user_id}")
            await asyncio.sleep(0.5)  # минимальная задержка, чтобы избежать спама
        except BotBlocked:
            print(f"⛔ Бот заблокирован пользователем {user_id}")
        except ChatNotFound:
            print(f"❌ Чат не найден для {user_id}")
        except Exception as e:
            print(f"⚠️ Ошибка при отправке {user_id}: {e}")

    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())