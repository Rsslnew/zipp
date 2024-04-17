# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("APP_ID", 20247370))
    API_HASH = os.environ.get("API_HASH", "813309fab8cd9fce260ce7269e543bdb")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7153848219:AAF1nL2W3tTuFDKHjGU3N7rUE7NDOOJBO8Y")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1001881201311"))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1748872441))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://Set:12345@cluster0.ebhgmux.mongodb.net/?retryWrites=true&w=majority")
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN" "False")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6