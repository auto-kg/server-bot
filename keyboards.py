from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


def admin_keyboard(base_url: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Добавить авто",
                    web_app=WebAppInfo(url=f"{base_url}/admin/cars/new"),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Популярные категории",
                    web_app=WebAppInfo(url=f"{base_url}/admin/categories"),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Настройки сайта",
                    web_app=WebAppInfo(url=f"{base_url}/admin/settings"),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Открыть админку",
                    web_app=WebAppInfo(url=f"{base_url}/admin"),
                )
            ],
        ]
    )
