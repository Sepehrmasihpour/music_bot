from typing import final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters , Application , ContextTypes

username:final = '@tableMusic_bot'
token:final = '6768326497:AAFzUJWdGpzs08502OprpIuRmEymhni_zDE'

# Commands

async def start_command(update: Update, context: ContextTypes):
    await update.message.reply_text("hello")

# message handlers

async def is_music(update: Update, context: ContextTypes):
    if update.message.audio:
        if update.message.audio.duration > 90:
            await update.message.reply_text("music detected")
    else:
        await update.message.reply_text("not a music")
        
    message = update.message # Get the message from the Update
    message_data = message.to_dict() # Convert the Message object into a dictionary
    print(message_data)
# errror handler
    
async def error(update: Update, context: ContextTypes):
        print(f"Update {update} caused error {context.error}")
    

# Commands
async def start_command(update: Update, context: ContextTypes):
    await update.message.reply_text("hello")



if __name__ == "__main__":
    print ("bot is running")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))

    # messagr handler
    app.add_handler(MessageHandler(filters.ALL, is_music))

    # error handler
    app.add_error_handler(error)    

    print("bot is polling")
    app.run_polling(poll_interval=4)
