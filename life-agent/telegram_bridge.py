import os
import subprocess
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
AUTHORIZED_USER_ID = os.getenv("AUTHORIZED_USER_ID")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in the environment or .env file.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Guardrail: Check authorization
    if not update.effective_user or str(update.effective_user.id) != str(AUTHORIZED_USER_ID):
        logging.warning("Unauthorized access attempt from user ID: %s", update.effective_user.id if update.effective_user else "unknown")
        return

    user_text = update.message.text.strip() if (update.message and update.message.text) else ""
    if not user_text:
        return

    # 1. Route to Forge (The Architect)
    if user_text.lower().startswith("/forge") or user_text.lower().startswith("@forge"):
        prompt = user_text.split(maxsplit=1)[1] if len(user_text.split(maxsplit=1)) > 1 else ""
        command = f'hermes run forge -p "{prompt or user_text}"'
        await update.message.reply_text("⚙️ Forge is analyzing...")

    # 2. Route to Pulse (The Social Creator)
    elif user_text.lower().startswith("/pulse") or user_text.lower().startswith("@pulse"):
        prompt = user_text.split(maxsplit=1)[1] if len(user_text.split(maxsplit=1)) > 1 else ""
        command = f'hermes run pulse -p "{prompt or user_text}"'
        await update.message.reply_text("📱 Pulse is drafting...")

    # 3. Default to Mirror (The Companion)
    else:
        command = f'hermes run mirror -p "{user_text}"'

    # Execute Hermes CLI command
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            await update.message.reply_text(result.stdout)
        if result.stderr:
            await update.message.reply_text(f"Notice: {result.stderr}")
    except Exception as e:
        await update.message.reply_text(f"System failure: {str(e)}")

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.add_handler(MessageHandler(filters.COMMAND, handle_message))
    print("Telegram bridge running (long-polling)...")
    app.run_polling()

if __name__ == "__main__":
    main()
