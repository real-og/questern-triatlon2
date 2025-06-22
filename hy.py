import json

with open("updates.json", "r", encoding="utf-8") as f:
    data = json.load(f)

user_ids = set()

for update in data.get("result", []):
    msg = update.get("message")
    if msg and msg.get("text") == "/start":
        user_ids.add(msg["from"]["id"])

print(f"Уникальных пользователей с командой /start: {len(user_ids)}")