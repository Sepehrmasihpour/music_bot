import os
from dotenv import load_dotenv
from typing import final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters , Application , ContextTypes

load_dotenv()

username:final = os.getenv('USERNAME')
token:final = os.getenv('TOKEN')

# Commands

async def start_command(update: Update, context: ContextTypes):
    await update.message.reply_text("hello")

if __name__ == "__main__":
    print("Bot is running")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))

    print("bot is polling")
    app.run_polling(poll_interval=4)