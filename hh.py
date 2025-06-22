import requests
import json
from loader import BOT_TOKEN

  # замени на свой реальный токен
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open("updates.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✅ Апдейты сохранены в updates.json")
else:
    print(f"❌ Ошибка запроса: {response.status_code}")
    print(response.text)