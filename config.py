import os

from dotenv import load_dotenv

load_dotenv()


def _required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable {name} is required")
    return value


def _optional(name: str, default: str = "") -> str:
    return os.getenv(name, default)


BOT_TOKEN = _required("BOT_TOKEN")
ADMIN_GROUP_ID = int(_required("ADMIN_GROUP_ID"))
MINI_APP_BASE_URL = _required("MINI_APP_BASE_URL").rstrip("/")
NEW_CAR_CHANNEL_ID = _optional("NEW_CAR_CHANNEL_ID")
BOT_NOTIFY_SECRET = _optional("BOT_NOTIFY_SECRET")
BOT_NOTIFY_HOST = _optional("BOT_NOTIFY_HOST", "0.0.0.0")
BOT_NOTIFY_PORT = int(_optional("BOT_NOTIFY_PORT", "8080"))
