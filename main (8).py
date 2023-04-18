import logging
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters

BOT_TOKEN = "TOKEN"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    await update.message.reply_text(
        "Привет. Я бот-психолог! Я не храню данные о нашем разговоре, поэтому ты можешь мне выговориться)) \n"
        "Хоть я и идеальный слушатель, но ты можешь прервать наш с тобой разговор, отправив: /stop.\n"
        "Рассказывай, что у тебя случилось?")

    return 1


async def first_response(update, context):
    await update.message.reply_text(
        f"Что ты планируешь делать с этой проблемой?")
    return 2


async def second_response(update, context):
    weather = update.message.text
    logger.info(weather)
    await update.message.reply_text("Я вижу твои усилия и старания."
                                    "Они не преподадут даром, а уже скоро у тебя все наладится."
                                    "Мир будет полон радостей и счастья, как только ты сможешь пройти через все это.")
    return ConversationHandler.END


async def skip(update, context):
    await update.message.reply_text("Хочешь рассказать еще о чем то?")
    return 2


async def stop(update, context):
    await update.message.reply_text("Я не могу оставить тебя в таком состоянии, поэтому позвони на телефон доверия: 8-800-2000-122 "
                                    "Я переживаю и желаю тебе всего самого лучшего. До новых встреч!")

    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response), CommandHandler('skip', skip)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_response)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
