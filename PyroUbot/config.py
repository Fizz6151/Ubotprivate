import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "6139972751").split()))

API_ID = int(os.getenv("API_ID", "20607074"))

API_HASH = os.getenv("API_HASH", "f5639cb2a94b785afc60800f351ec802")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7600571701:AAGNyYxTB5yTaGo1bfEkTc7CtatqHUOxCPk")

OWNER_ID = int(os.getenv("OWNER_ID", "6139972751"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "MA2sUZ4HdAfBegL36HiG4BUG")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://fizzpamell:fizzpamell@cluster0.9nmhi5m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4628173231"))
