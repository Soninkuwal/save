# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20945078"))
API_HASH = getenv("API_HASH", "93f6b8ce4bb0ab61b4c7e42187f2aa64")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1664376941").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://meenakanhaiyalal638:files@files.8ko8k.mongodb.net/?retryWrites=true&w=majority&appName=files")
LOG_GROUP = getenv("LOG_GROUP", "-1002319987698")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001821282319"))
