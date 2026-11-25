# Telegram Bridge Routing Logic

## 1. The Routing Concept
The bridge script parses incoming Telegram messages and routes them to the correct Hermes agent:
- `/forge` or `@forge` -> Routes to **Forge** (`hermes run forge -p "<prompt>"`)
- `/pulse` or `@pulse` -> Routes to **Pulse** (`hermes run pulse -p "<prompt>"`)
- Everything else -> Defaults to **Mirror** (`hermes run mirror -p "<prompt>"`)

## 2. Python Routing Implementation
```python
import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()

AUTHORIZED_USER_ID = os.getenv("AUTHORIZED_USER_ID")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Guardrail: Only respond to the authorized user
    if str(update.effective_user.id) != str(AUTHORIZED_USER_ID):
        return

    user_text = update.message.text.strip() if update.message.text else ""
    if not user_text:
        return

    # 1. Route to Forge (The Architect)
    if user_text.lower().startswith("/forge") or user_text.lower().startswith("@forge"):
        command = f'hermes run forge -p "{user_text}"'
        await update.message.reply_text("⚙️ Forge is analyzing...")

    # 2. Route to Pulse (The Social Creator)
    elif user_text.lower().startswith("/pulse") or user_text.lower().startswith("@pulse"):
        command = f'hermes run pulse -p "{user_text}"'
        await update.message.reply_text("📱 Pulse is drafting...")

    # 3. Default to Mirror (The Companion)
    else:
        command = f'hermes run mirror -p "{user_text}"'

    # Execute the Hermes CLI command
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            await update.message.reply_text(result.stdout)
        if result.stderr:
            await update.message.reply_text(f"Notice: {result.stderr}")
    except Exception as e:
        await update.message.reply_text(f"System failure: {str(e)}")
```

## 3. How to Use in Telegram
* **Standard Diary Entry:** Type naturally or send a thought. It routes automatically to Mirror.
  * *Example:* "I'm feeling burnt out from the Shopify redesign today."
* **Triggering Forge:** Use `@Forge` or `/forge` to force analysis.
  * *Example:* "@Forge analyze my last 3 days of diary entries and update my sleep patterns."
* **Triggering Pulse:** Use `/pulse` to command content generation.
  * *Example:* "/pulse generate 3 Twitter hooks based on my latest BLESSET TURMOIL beat."
