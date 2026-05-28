import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiohttp import web

from access import is_admin
from config import ADMIN_GROUP_ID, BOT_NOTIFY_HOST, BOT_NOTIFY_PORT, BOT_TOKEN, MINI_APP_BASE_URL
from keyboards import admin_keyboard
from notify import create_notify_app

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
    notify_runner = web.AppRunner(create_notify_app(bot))
    await notify_runner.setup()
    notify_site = web.TCPSite(notify_runner, BOT_NOTIFY_HOST, BOT_NOTIFY_PORT)
    await notify_site.start()

    try:
        await dp.start_polling(bot)
    finally:
        await notify_runner.cleanup()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
