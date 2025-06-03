from api.imports import *
from api.variables import *

COUNT = 0
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start bot"""

    global COUNT
    
    COUNT = +1
    
    reply_keyboard = [
        ["/start"],
        ["/queue", "/queue_mix", "/queue_v2"],
        ["/help"]
    ]
    
    bot = context.bot
    user = update.effective_user        
    text = ("👺" "{} items found".format(len(data)))

    await update.message.reply_html(
        rf"ִֶָ𓂃 ࣪˖ ִֶָ🐇་༘࿐ {user.mention_html()}! {text}.",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="ﮩـﮩﮩ٨ـ❤️ﮩ٨ـﮩﮩ٨ـ"
        ),
    )
    
    keyboard = [
        [
            InlineKeyboardButton(
                "<",
                callback_data="1"
            ),
            
            InlineKeyboardButton(
                ">",
                callback_data="2"
            ),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    link = re.search(r"(t\.me\/[a-zA-Z0-9_]{5,32})", update.message.text)

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    global COUNT
    
    reply_keyboard = [
        ["/sub", "/add"],
        ["/queue", "/queue_mix", "/queue_v2"],
        ["/help"]
    ]

    COUNT += 1

    await update.message.reply_text(
        "queue {} song(s)".format(COUNT),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard),
        parse_mode=ParseMode.MARKDOWN
    )

async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    global COUNT

    reply_keyboard = [
        ["/sub", "/add"],
        ["/queue", "/queue_mix", "/queue_v2"],
        ["/help"]
    ]
    if COUNT < 1:
        await update.message.reply_text(
            "queue cant be < {}. /add instead".format(COUNT),
            reply_markup=ReplyKeyboardMarkup(help_keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    else:
        COUNT -= 1
        await update.message.reply_text(
            "queue {} song(s)\nuse /add for more".format(COUNT),
            reply_markup=ReplyKeyboardMarkup(reply_keyboard),
            parse_mode=ParseMode.MARKDOWN
        )

async def queue(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /next is issued."""

    global COUNT

    # Get all available message IDs, excluding known bad IDs
    msg_id = [k for k in data.keys()]

    # Shuffle the list of message IDs
    random.shuffle(msg_id)

    # Iterate over the shuffled list
    for i in range(min(COUNT, len(msg_id))):
        url = f"https://t.me/crateofnotsodasbutmusic/{msg_id[i]}"
        
        reply_keyboard = [
            ["/sub", "/add"],
            ["/queue", "/queue_mix", "/queue_v2"],
            ["/start"]
        ]
        try:
            await update.message.reply_audio(
                "{}".format(url),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=ReplyKeyboardMarkup(
                    reply_keyboard,
                    one_time_keyboard=True,
                    input_field_placeholder="▄︻デ══━一💥"
                )
            )
        except (AttributeError, BadRequest) as e:
            await update.message.reply_text(
                "[{}]({})".format("  🃜🃚🃖🃁🂭🂺  ", url),
                parse_mode=ParseMode.MARKDOWN,
            )

async def queue_v2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /next is issued."""

    global COUNT
         
    # Get all available message IDs, excluding known bad IDs
    msg_id = [k for k in data_v2.keys()]

    # Shuffle the list of message IDs
    random.shuffle(msg_id)

    # Iterate over the shuffled list
    for i in range(min(COUNT, len(msg_id))):
        url = f"https://t.me/thecrate/{msg_id[i]}"
        print(url)
        reply_keyboard = [
            ["/sub", "/add"],
            ["/queue", "/queue_mix", "/queue_v2"],
            ["/start"]
        ]
        try:
            await update.message.reply_audio(
                "{}".format(url),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=ReplyKeyboardMarkup(
                    reply_keyboard,
                    one_time_keyboard=True
                )
            )
            print(url)
        except (AttributeError, BadRequest) as e:
            await update.message.reply_text(
                "[{}]({})".format("  🃜🃚🃖🃁🂭🂺  ", url),
                parse_mode=ParseMode.MARKDOWN,
            )

async def queue_mix(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /next is issued."""
    
    global COUNT
        
    msg_id = []

    for k, v in data.items():
        if v.get("duration") > 600 and v.get("duration") < 18000:
            msg_id.append(k)

    # Shuffle the list of message IDs
    random.shuffle(msg_id)
    reply_keyboard = [
        ["/sub", "/add"],
        ["/queue", "/queue_mix", "/queue_v2"],
        ["/start"]
    ]
    
    # Define your URLs
    urls = [
        f"https://t.me/crateofnotsodasbutmusic/{msg_id[i]}" for i in range(min(COUNT, len(msg_id)))
    ] + ["https://t.me/thecrate"]
    
    # Iterate over the URLs and send an audio message for each one
    for url in urls:
        try:
            await update.message.reply_audio(
                "{}".format(url),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=ReplyKeyboardMarkup(
                    reply_keyboard,
                    one_time_keyboard=True,
                    input_field_placeholder="▀▄▀▄▀▄"
                )
            )
        except (AttributeError, BadRequest) as e:
            continue
        
async def help_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """usaindizi"""
    await update.message.reply_text(
        "/start",
        parse_mode=ParseMode.MARKDOWN
    )
