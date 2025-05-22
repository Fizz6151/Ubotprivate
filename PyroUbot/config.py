import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "6609037353").split()))

API_ID = int(os.getenv("API_ID", "14933784"))

API_HASH = os.getenv("API_HASH", "b5bfa597497fdae2a3d97f2640d63fa3")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7773256927:AAEH1Hl58yHB_g29E_D_-nBurgN9UDLSVrQ")

OWNER_ID = int(os.getenv("OWNER_ID", "6609037353"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "ZZRtUKLd6M4GoDSPAdzVVZz8")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Userbot:xZgNn17M2ya4ivjZ@userbotkyz.si2ilrj.mongodb.net/?retryWrites=true&w=majority&appName=UserbotKyz")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4778429932"))
