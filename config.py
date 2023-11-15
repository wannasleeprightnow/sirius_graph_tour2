from os import environ

from dotenv import load_dotenv

load_dotenv()
TOKEN = environ.get("TELEGRAM_TOKEN")
