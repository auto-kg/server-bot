import html
from typing import Any

from aiogram import Bot
from aiohttp import web

from config import BOT_NOTIFY_SECRET, MINI_APP_BASE_URL, NEW_CAR_CHANNEL_ID


def _channel_id() -> str | int:
    if NEW_CAR_CHANNEL_ID.lstrip("-").isdigit():
        return int(NEW_CAR_CHANNEL_ID)

    return NEW_CAR_CHANNEL_ID


def _format_price(value: Any) -> str:
    try:
        return f"${int(value):,}".replace(",", " ")
    except (TypeError, ValueError):
        return str(value or "")


def _shorten(value: str, limit: int) -> str:
    value = " ".join(value.split())

    if len(value) <= limit:
        return value

    return f"{value[:limit - 1].rstrip()}..."


def _caption(car: dict[str, Any], car_url: str) -> str:
    title = html.escape(str(car.get("title") or "Новый автомобиль"))
    price = html.escape(_format_price(car.get("price")))
    city = html.escape(str(car.get("city") or ""))
    year = html.escape(str(car.get("year") or ""))
    mileage = html.escape(str(car.get("mileage") or "0"))
    fuel = html.escape(str(car.get("fuel") or ""))
    transmission = html.escape(str(car.get("transmission") or ""))
    description = html.escape(_shorten(str(car.get("description") or ""), 260))
    url = html.escape(car_url)

    parts = [
        f"<b>{title}</b>",
        "",
        f"Цена: <b>{price}</b>",
        f"Город: {city}",
        f"Год: {year}",
        f"Пробег: {mileage} км",
        f"Топливо: {fuel}",
        f"Коробка: {transmission}",
    ]

    if description:
        parts.extend(["", description])

    parts.extend(["", f'<a href="{url}">Открыть объявление</a>'])

    return _shorten("\n".join(parts), 1000)


def create_notify_app(bot: Bot) -> web.Application:
    app = web.Application()

    async def new_car(request: web.Request) -> web.Response:
        if not BOT_NOTIFY_SECRET:
            raise web.HTTPServiceUnavailable(reason="Notification secret is not configured")

        if request.headers.get("x-bot-notify-secret") != BOT_NOTIFY_SECRET:
            raise web.HTTPUnauthorized(reason="Invalid notification secret")

        if not NEW_CAR_CHANNEL_ID:
            raise web.HTTPServiceUnavailable(reason="New car channel is not configured")

        payload = await request.json()
        car = payload.get("car") or {}
        image_url = payload.get("imageUrl") or (car.get("images") or [""])[0]
        car_url = payload.get("carUrl") or f"{MINI_APP_BASE_URL}/cars/{car.get('id', '')}"
        caption = _caption(car, car_url)

        if image_url:
            await bot.send_photo(
                chat_id=_channel_id(),
                photo=image_url,
                caption=caption,
                parse_mode="HTML",
            )
        else:
            await bot.send_message(
                chat_id=_channel_id(),
                text=caption,
                parse_mode="HTML",
                disable_web_page_preview=False,
            )

        return web.json_response({"ok": True})

    app.router.add_post("/notify/new-car", new_car)
    return app
