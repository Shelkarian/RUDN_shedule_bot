from services import get_schedule_for_today
from telegram import Update
from telegram.ext import ContextTypes

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    res = get_schedule_for_today()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=res
    )