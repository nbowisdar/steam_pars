from dotenv import load_dotenv
from os import getenv

load_dotenv()

DB_NAME = getenv('DB_NAME')
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST')
DB_PORT = int(getenv('DB_PORT'))

# Mongo db
MONGO_HOST = getenv('MONGO_HOST')
MONGO_PORT = int(getenv('MONGO_PORT'))

#Telegram
TOKEN_BOT = getenv('TOKEN_BOT')
CHAT_ID = int(getenv('CHAT_ID'))