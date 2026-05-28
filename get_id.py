import asyncio
import os

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("Environment variable BOT_TOKEN is required")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# 1. Хэндлер для ГРУПП и ЛИЧНЫХ СООБЩЕНИЙ
@dp.message()
async def handle_message(message: types.Message):
    if message.chat.type in ['group', 'supergroup']:
        print("\n" + "=" * 40)
        print(f"👥 ГРУППА: {message.chat.title}")
        print(f"ID группы: {message.chat.id}")
        print(f"Текст:     {message.text or '[Медиа]'}")
        print("=" * 40)
    else:
        print(f"[Инфо] Сообщение из ЛС ({message.chat.type}). ID пользователя: {message.chat.id}")


# 2. Хэндлер для КАНАЛОВ (Новый)
@dp.channel_post()
async def handle_channel_post(channel_post: types.Message):
    print("\n" + "=" * 40)
    print(f"📢 КАНАЛ:   {channel_post.chat.title}")
    print(f"ID канала: {channel_post.chat.id}")
    print(f"Пост:      {channel_post.text or '[Медиа]'}")
    print("=" * 40)


async def main():
    print("Бот успешно запущен!")
    print("Можете писать в группу или публиковать пост в канале.")
    print("Для остановки нажмите Ctrl + C")
    print("-" * 50)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\nБот остановлен пользователем.")
