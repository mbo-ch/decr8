from api.imports import *
from api.variables import *
from api.bot_command import *
from api.bot_query import *

# on command - answer in Telegram
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("queue", queue))
application.add_handler(CommandHandler("queue_mix", queue_mix))
application.add_handler(CommandHandler("pick_channel", pick_channel))
# on query i.e message - echo the message on Telegram
application.add_handler(InlineQueryHandler(inlinequery))
application.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        search,
    )
)

application.add_handler(CallbackQueryHandler(button_handler))
