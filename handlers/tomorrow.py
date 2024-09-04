from services import get_schedule_for_tomorrow
from telegram import Update
from telegram.ext import ContextTypes

async def tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = get_schedule_for_tomorrow()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=res
    )