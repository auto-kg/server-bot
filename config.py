import os

from dotenv import load_dotenv

load_dotenv()


def _required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Environment variable {name} is required")
    return value


BOT_TOKEN = _required("BOT_TOKEN")
ADMIN_GROUP_ID = int(_required("ADMIN_GROUP_ID"))
MINI_APP_BASE_URL = _required("MINI_APP_BASE_URL").rstrip("/")
