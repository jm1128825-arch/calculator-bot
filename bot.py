from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello!\n\n"
        "Welcome to Calculator Bot.\n\n"
        "We're building this bot step by step! 🚀"
    )


def main():
    print("Calculator Bot is starting...")


if __name__ == "__main__":
    main()
