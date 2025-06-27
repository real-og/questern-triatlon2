import json
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import BotBlocked, ChatNotFound
from loader import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def main():
    user_ids = [520251635, 6150574145]
    text = """На старт, внимание... ! 🔥 Триатлон-квест по Екатеринбургу стартует прямо сейчас! 🚀  Впереди крутой маршрут, исторические загадки и море драйва!⚡️

Не забудь:  
✅ Удобная обувь  
✅ Заряженный телефон  
✅ Спортивное настроение  

Жду тебя на стадионе «Динамо» на ярмарке (ЭКСПО) IRONSTAR.
⚡️ 56.845516, 60.601278⚡️

Чтобы начать квест, жми 👉 /begin

☝️ Напомню, что пройти квест ты можешь в любой день с 27 по 29 июня 2025. Главное - финишируй не позднее 17:00 в воскресенье 29 июня. 
Увидимся на старте! 😎"""
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