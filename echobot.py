#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from subprocess import call
from functools import wraps
import logging
import telegram

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.

LIST_OF_ADMINS = [285743410]

def restricted(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(bot, update, *args, **kwargs)
    return wrapped

@restricted
def start(bot, update):
    update.message.reply_text("""/help - show current help
/server - get server info
/browse - get surveilance url
/balance - get balance info
""")

@restricted
def help(bot, update):
    update.message.reply_text("""/help - show current help
/server - get server info
/browse - get surveilance url
/balance - get balance info
""")

@restricted
def echo(bot, update):
   update.message.reply_text(update.message.text)

@restricted
def server(bot, update):
    chat_id = update.message.chat_id
    try:
        # Script to collect info
        bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
        call(["/root/dev/bot/status.sh"])
        # Script results
        status = open("/root/status.txt", "rb").read()
        #update.message.reply_text(status)
        bot.send_message(chat_id=chat_id, text=status, parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        logger.exception(str(e))
        update.message.reply_text('Ошибка при получении статуса сервера. Подробности в журнале.')

@restricted
def balance(bot, update):
    chat_id = update.message.chat_id
    try:
        # Script to collect info
        bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
        call(["/root/dev/bot/balance.sh"])
        # Script results
        balance = open("/root/balance.txt", "rb").read()
        bot.send_message(chat_id=chat_id, text=balance, parse_mode=telegram.ParseMode.MARKDOWN)
    except Exception as e:
        logger.exception(str(e))
        update.message.reply_text('Ошибка при получении баланса. Подробности в журнале.')

@restricted
def browse(bot, update):
    #call([])
    chat_id = update.message.chat_id
    update.message.reply_text('Here is a link to surveilance monitor: https://silitus.ru:8443/')
    bot.send_photo(chat_id=chat_id, photo='http://www.andiar.com/1281-large_default/vinilo-bart-simpson-asomandose.jpg')

@restricted
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("425144783:AAFipL2EsnBn0kpgLZbtXV1LaZIQPuAeouw")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("server", server))
    dp.add_handler(CommandHandler("browse", browse))
    dp.add_handler(CommandHandler("balance", balance))
    

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
