import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "Type /calc to open the calculator."
    )


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton("7", callback_data="7"),
            InlineKeyboardButton("8", callback_data="8"),
            InlineKeyboardButton("9", callback_data="9"),
            InlineKeyboardButton("÷", callback_data="/"),
        ],
        [
            InlineKeyboardButton("4", callback_data="4"),
            InlineKeyboardButton("5", callback_data="5"),
            InlineKeyboardButton("6", callback_data="6"),
            InlineKeyboardButton("×", callback_data="*"),
        ],
        [
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("−", callback_data="-"),
        ],
        [
            InlineKeyboardButton("C", callback_data="clear"),
            InlineKeyboardButton("0", callback_data="0"),
            InlineKeyboardButton("=", callback_data="equals"),
            InlineKeyboardButton("+", callback_data="+"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🧮 Calculator\n\n"
        "0",
        reply_markup=reply_markup,
    )


def main():

    if BOT_TOKEN is None:
        print("BOT_TOKEN not found!")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("calc", calc))

    print("Calculator Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
