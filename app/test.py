from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_URL = getenv("DB_URL")
DB_POOL = getenv("DB_POOL")
DB_MAX_OVERFLOW = getenv("DB_MAX_OVERFLOW")

print(DB_URL, DB_POOL, DB_MAX_OVERFLOW)