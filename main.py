import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import config
from handlers import start, tomorrow, today, week, next_week

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    today_handler = CommandHandler('today', today)
    tomorrow_handler = CommandHandler('tomorrow', tomorrow)
    week_handler = CommandHandler('week', week)
    next_week_handler = CommandHandler('next_week', next_week)

    application.add_handler(start_handler)
    application.add_handler(today_handler)
    application.add_handler(tomorrow_handler)
    application.add_handler(week_handler)
    application.add_handler(next_week_handler)

    application.run_polling()  

