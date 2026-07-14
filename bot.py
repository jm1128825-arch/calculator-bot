import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)


BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Calculator Bot!\n\n"
        "✅ Your bot is working!"
    )


def main():

    if BOT_TOKEN is None:
        print("BOT_TOKEN was not found.")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Calculator Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
