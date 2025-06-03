from api.imports import *
from api.variables import *
from api.bot_command import *
from api.bot_query import *

# on different commands - answer in Telegram
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("queue", queue))
application.add_handler(CommandHandler("queue_v2", queue_v2))
application.add_handler(CommandHandler("queue_mix", queue_mix))
application.add_handler(CommandHandler("add", add))
application.add_handler(CommandHandler("sub", sub))
application.add_handler(CommandHandler("help", help_info))

# on query i.e message - echo the message on Telegram
application.add_handler(InlineQueryHandler(inlinequery))
application.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        search,
    )
)

# application.add_handler(CallbackQueryHandler(search_buttons))
