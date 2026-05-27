from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

ADMIN_STATUSES = {"creator", "administrator"}


async def is_admin(bot: Bot, group_id: int, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(group_id, user_id)
        return member.status in ADMIN_STATUSES
    except TelegramBadRequest:
        return False
