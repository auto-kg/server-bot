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


@dp.message()
async def handle_message(message: types.Message):
    if message.chat.type in ['group', 'supergroup']:
        print("\n" + "=" * 40)
        print(f"Группа:  {message.chat.title}")
        print(f"ID чата: {message.chat.id}")
        print(f"От кого: @{message.from_user.username or message.from_user.first_name}")
        print(f"Текст:   {message.text or '[Медиа/Служебное]'}")
        print("=" * 40)
    else:
        print(f"[Инфо] Сообщение из ЛС ({message.chat.type}). Отправьте в группу.")


async def main():
    print("Бот успешно запущен!")
    print("Можете писать в группу. Для остановки нажмите Ctrl + C")
    print("-" * 50)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\nБот остановлен пользователем.")
