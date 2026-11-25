# Telegram Bridge Security & Environment

## 1. Stack Confirmation
* **Framework:** Python CLI + Python platform plugin.
* **Library:** `python-telegram-bot`.
* **Execution:** Long-polling by default (ideal for local Mac/server setups), switching to webhooks if `TELEGRAM_WEBHOOK_URL` is set.

## 2. Security Guardrails
Because this bridge exposes your personal diary and brand accounts to the internet via Telegram, security is paramount.
* **Hardcoded ID Lock:** The bridge must verify `update.message.from_user.id` against your personal Telegram ID before passing anything to Hermes. If someone else messages the bot, it should silently ignore them or drop the payload.
* **Environment Variables:** Never hardcode the Telegram Token or your User ID in the script. Use a `.env` file in `~/life-agent/`:
  ```bash
  TELEGRAM_BOT_TOKEN="your_botfather_token"
  AUTHORIZED_USER_ID="123456789"
  ```

## 3. Execution State
Run the bridge in a multiplexer like `tmux` or `screen` if deploying to a remote server, or as a background process (`&` or launchd daemon) on macOS. This ensures the long-polling loop survives terminal closures and Mirror is always ready to receive your diary entries.
