from api.imports import *
from api.variables import *
from api.deep_link import *
from api.bot_commands import *
from api.bot_non_commands import *
from api.bot_error import *

# Register a deep-linking handler
application.add_handler(
    CommandHandler(
        "start",
        deep_linked_level_1,
        filters.Regex(DECR8)
    )
)

# This one works with a textual link instead of an URL
application.add_handler(
    CommandHandler(
        "start",
        deep_linked_level_2,
        filters.Regex(SO_COOL)
    )
)

# We can also pass on the deep-linking payload
application.add_handler(
    CommandHandler(
        "start",
        deep_linked_level_3,
        filters.Regex(USING_ENTITIES)
    )
)

# Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        STAGE1: [MessageHandler(filters.Regex('^(/start|/queue|/cancel)$'), STAGE1)],
        STAGE3: [
            MessageHandler(filters._Location, STAGE3),
            CommandHandler('skip', STAGE3),
        ],
        STAGE4: [MessageHandler(filters.Text, STAGE4)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

# on different commands - answer in Telegram
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("queue", queue))
application.add_handler(CommandHandler("queue_v2", queue_v2))
application.add_handler(CommandHandler("queue_mix", queue_mix))
application.add_handler(CommandHandler("add", add))
application.add_handler(CommandHandler("sub", sub))
application.add_handler(CommandHandler("slow", slow))
application.add_handler(CommandHandler("fast", fast))
application.add_handler(CommandHandler("tempo", tempo))
application.add_handler(CommandHandler("bad_command", bad_command))

# on noncommand i.e message - echo the message on Telegram
application.add_handler(InlineQueryHandler(inlinequery))
application.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        search,
    )
)

application.add_handler(CallbackQueryHandler(search_buttons))
application.add_handler(conv_handler)
application.add_error_handler(error_handler)
