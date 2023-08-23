# Load environment variable from .env
from decouple import config

# ---------------------
# environment Variables
# ---------------------
TOKEN = config("TOKEN", cast=str)
NGROK_TOKEN = config("NGROK_TOKEN", cast=str)
