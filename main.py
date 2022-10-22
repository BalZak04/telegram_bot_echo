from telegram.ext import MessageHandler, Filters, Updater
from telegram.ext import CommandHandler


token = 'toke'


def echo(update, conext):
    txt = update.message.text

    if txt.lower() in ['привет', 'как дела', 'txt']:
        txt = 'И тебе привет ххх'

    update.message.reply_text(txt)


def start(update, conext):
    update.message.reply_text('Я устал\nДа-да-да')


def help(update, conext):
    update.message.reply_text('А Я устал\nНет-Нет-Нет')


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    print('Бот запущен...')

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))

    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
