import os
from dotenv import load_dotenv
from typing import final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters , Application , ContextTypes

load_dotenv()

username:final = "@tableMusic_bot"
token:final = '6768326497:AAFzUJWdGpzs08502OprpIuRmEymhni_zDE'

# Commands



async def start_command(update: Update, context: ContextTypes):
    await update.message.reply_text("hello")

# add messsage handler that will determine if a message is a music or not and if it is respond with a message saying "music detected"

async def is_music(update: Update, context: ContextTypes):
    if update.message.audio:
        if update.message.duration > 90:
            await update.message.reply_text("music detected")
    else:
        await update.message.reply_text("not a music")


# errror handler
    
async def error(update: Update, context: ContextTypes):
        print(f"Update {update} caused error {context.error}")
    
if __name__ == "__main__":
    print("Bot is running")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))

    # messagr handler
    app.add_handler(MessageHandler(filters.ALL, is_music))

    print("bot is polling")
    app.run_polling(poll_interval=4)
    
    # error handler
    app.add_error_handler(error)    