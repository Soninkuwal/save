# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20945078"))
API_HASH = getenv("API_HASH", "93f6b8ce4bb0ab61b4c7e42187f2aa64")
BOT_TOKEN = getenv("BOT_TOKEN", "7928313510:AAGZGr6uhlWc4vQZiwieXB2klOfd0NIPii4")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7378826796").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://meenakanhaiyalal638:files@files.8ko8k.mongodb.net/?retryWrites=true&w=majority&appName=files")
LOG_GROUP = getenv("LOG_GROUP", "-1002352077049")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001910904349"))
