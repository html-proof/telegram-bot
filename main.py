import constant as ct

from telegram.ext import*

import Responses as R

print("Chat bot")

def start_command(update,context):
    update.message.reply_text('Type Something You want to Known')


def help_command(update, context):
    update.message.reply_text('Hi how can i help you!You want more ask google')


def handle_message(update, context):
    text =str(update.message.text).lower()
    responses =R.sample_response(text)
    update.message.reply_text(responses)


def error(update, context):
    print(f"update{update}causes error{context.error}")


def main():


    updater =Updater(ct.API_KEY,use_context=True)
    dp =updater.dispatcher
    dp.add_handler(CommandHandler("Start",start_command))
    dp.add_handler(CommandHandler("Start", help_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_error_handler(error)
    updater.start_polling(2)
    updater.idle()

if  __name__ =='__main__':
    main()


