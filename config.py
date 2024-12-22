import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25751497"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c18db31105b92bba3cfa1ab685c4787f")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5548923721"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://xeroxbayzid12:xeroxbayzid12@cluster0.dcapc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
