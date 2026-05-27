import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from access import is_admin
from config import ADMIN_GROUP_ID, BOT_TOKEN, MINI_APP_BASE_URL
from keyboards import admin_keyboard

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def send_admin_menu(message: Message) -> None:
    if not message.from_user:
        await message.answer("У вас нет доступа к админке.")
        return

    allowed = await is_admin(bot, ADMIN_GROUP_ID, message.from_user.id)

    if not allowed:
        await message.answer("У вас нет доступа к админке.")
        return

    await message.answer(
        "AutoHub KG Admin\nВыберите действие:",
        reply_markup=admin_keyboard(MINI_APP_BASE_URL),
    )


@dp.message(F.text == "/start")
async def start(message: Message) -> None:
    await send_admin_menu(message)


@dp.message(F.text == "/admin")
async def admin(message: Message) -> None:
    await send_admin_menu(message)


@dp.message()
async def fallback(message: Message) -> None:
    await send_admin_menu(message)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
