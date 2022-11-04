from dotenv import load_dotenv
from os import getenv

load_dotenv()

s = getenv('DB_NAME')
print(s)
