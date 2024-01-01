import os
import logging
import traceback
from typing import final
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters , Application , ContextTypes

username:final = os.getenv('@tableMusic_bot')
token:final = '6768326497:AAFzUJWdGpzs08502OprpIuRmEymhni_zDE'

# Commands
async def start_command(update: Update, context: ContextTypes):
    await update.message.reply_text("hello")

def message_handler(update: Update, context: ContextTypes):
   message = update.message # Get the message from the Update
   message_data = message.to_dict() # Convert the Message object into a dictionary
   print(message_data)

# Error Handler
async def error_handler(update: Update, context: ContextTypes):
   # Log the error before we do anything else, so we can see it even if something breaks.
   logging.error("Exception while handling an update:", exc_info=context.error)

   # traceback.format_exception returns the usual python message about an exception, but as a
   # list of strings rather than a single string, so we have to join them together.
   tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
   tb_string = "".join(tb_list)

   # Print the error details
   print(f"An error occurred: {tb_string}")

if __name__ == "__main__":
   print("Bot is running")
   app = Application.builder().token(token).build()

   app.add_handler(CommandHandler("start", start_command))
   app.add_handler(MessageHandler(filters.ALL,message_handler))

   # Add the error handler
   app.add_error_handler(error_handler)

   print("bot is polling")
   app.run_polling(poll_interval=4)
