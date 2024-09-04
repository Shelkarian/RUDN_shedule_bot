from services import get_schedule_for_next_week
from telegram import Update
from telegram.ext import ContextTypes

async def next_week(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = get_schedule_for_next_week()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=res
    )