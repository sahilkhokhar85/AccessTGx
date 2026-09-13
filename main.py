import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_string = os.environ.get("SESSION_STRING")

client = TelegramClient(StringSession(session_string), api_id, api_hash)
client.connect()

if client.is_user_authorized():
    me = client.get_me()
    print(f"🟢 Logged in as: {me.first_name} (@{me.username})")
else:
    print("🔴 Session invalid or expired — login failed.")

client.disconnect()
