import constants as keys
from telegram.ext import *
from lottery import get_lottery_numbers


print("bot started. . .")

def start_command(update, context):
    update.message.reply_text("Type /hello to get started")

def lottery_command(update, context):
    update.message.reply_text(get_lottery_numbers())

def generic_response(update, context):
    text = str(update.message.text)
    res = f"Sorry, I don't know what to do with {text}\nType /help"

def hello(update, context):
    update.message.reply_text("Hi Dad! Type /lottery to get your numbers!")

def main():
    updater = Updater(keys.API_KEY, use_context=True)

    bot = updater.dispatcher

    bot.add_handler(CommandHandler("start", start_command))
    bot.add_handler(CommandHandler("help", start_command))
    bot.add_handler(CommandHandler("lottery", lottery_command))
    bot.add_handler(CommandHandler("hello", hello))
    bot.add_handler(MessageHandler(Filters.text, generic_response))

    updater.start_polling(5)
    updater.idle()


if __name__ == "__main__":
    main()