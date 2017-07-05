#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from subprocess import call

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text("""/help - show current help
/server - get server info
/browse - get surveilance url""")

def help(bot, update):
    update.message.reply_text("""/help - show current help
/server - get server info
/browse - get surveilance url""")

def echo(bot, update):
   update.message.reply_text(update.message.text)

def server(bot, update):
    try:
        # Script to collect info
        call(["/root/status.sh"])
        # Script results
        status = open("/root/status.txt", "rb").read()
        update.message.reply_text(status)
    except Exception as e:
        logger.exception(str(e))
        update.message.reply_text('Ошибка при получении статуса сервера. Подробности в журнале.')

def browse(bot, update):
    #call([])
    #chat_id = bot.get_updates()[-1].message.chat_id
    chat_id = 285743410
    update.message.reply_text('Here is a link to surveilance monitor: http://megaurl.com/')
    bot.send_photo(chat_id=chat_id, photo='http://www.andiar.com/1281-large_default/vinilo-bart-simpson-asomandose.jpg')

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
