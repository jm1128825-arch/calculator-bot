from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from config import BOT_TOKEN
from handlers import (
    start,
    calc,
    button,
)


def main():
    if BOT_TOKEN is None:
        print("BOT_TOKEN not found!")
        return

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("calc", calc))
    app.add_handler(CallbackQueryHandler(button))

    print("✅ Calculator Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
