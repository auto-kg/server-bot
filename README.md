# AutoHub Bot

Telegram bot that sends Mini App admin buttons.

Create env:

```bash
cp .env.example .env
nano .env
```

Required:

```env
BOT_TOKEN=123456789:telegram-bot-token
ADMIN_GROUP_ID=-1001234567890
MINI_APP_BASE_URL=https://autohub-63-180-133-249.sslip.io
NEW_CAR_CHANNEL_ID=@your_channel
BOT_NOTIFY_SECRET=change_me_same_as_nuxt
BOT_NOTIFY_HOST_PORT=8091
```

Add the bot to `NEW_CAR_CHANNEL_ID` as an admin with post permission.
Nuxt should call `http://host.docker.internal:8091/notify/new-car` with the same `BOT_NOTIFY_SECRET`.

Start:

```bash
docker compose up -d --build
```

Check:

```bash
docker compose ps
docker compose logs -f bot
```
