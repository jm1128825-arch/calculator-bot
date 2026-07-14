from telegram import Update
from telegram.ext import ContextTypes

from keyboards import calculator_keyboard
from calculator import solve


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\nType /calc to open the calculator."
    )


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧮 Calculator\n\n0",
        reply_markup=calculator_keyboard(),
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    display = query.message.text.split("\n\n")[1]
    data = query.data

    if data == "clear":
        display = "0"

    elif data == "equals":
        try:
            display = solve(display)
        except Exception:
            display = "Error"

    else:
        if display == "0":
            display = data
        else:
            display += data

    await query.edit_message_text(
        text=f"🧮 Calculator\n\n{display}",
        reply_markup=calculator_keyboard(),
    )
