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
```

Start:

```bash
docker compose up -d --build
```

Check:

```bash
docker compose ps
docker compose logs -f bot
```
