from api.imports import *
from api.variables import *
from api.utils import *

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Start bot"""
    
    reply_keyboard = [
        ["/start"],
        ["/queue", "/queue_mix"],
        ["/pick_channel"]
    ]

    bot = context.bot
    user = update.effective_user
    channel = context.user_data.get("channel")
    count = get_song_count(channel)
    channels = get_available_channels()
    if count == 0 and channel is None:
        text = f"👺 No channel selected. Please /pick_channel"
    else:
        text = f"👺 {count} items found in {channel}"        

    await update.message.reply_html(
        rf"ִֶָ𓂃 ࣪˖ ִֶָ🐇་༘࿐ {user.mention_html()}! {text}.",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="ﮩـﮩﮩ٨ـ❤️ﮩ٨ـﮩﮩ٨ـ"
        ),
    )
    
async def pick_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    channels = get_available_channels()
    keyboard = [
        [InlineKeyboardButton(channel, callback_data=f"set_channel:{channel}")]
        for channel in channels
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Pick a channel:",
        reply_markup=reply_markup
    )
    
async def queue(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /next is issued."""
    channel = context.user_data.get("channel")
    songs = get_random_song_list(channel=channel, count=10)
    if not songs:
        await update.message.reply_text("No songs found.")
        return

    keyboard = []
    for song in songs:
        channel, msg_id, performer, filename, duration, date, title, is_album, media_group_id = song
        if not title:
            title = filename
        mins, secs = divmod(duration, 60)
        time_str = f"{mins}:{secs:02d}"
        album_marker = "📀 " if is_album else ""
        # Add duration at the end of the label
        if performer:
            label = f"{album_marker}{title} - {performer} — {time_str}"
        else:
            label = f"{album_marker}{title} — {time_str}"
        callback_data = f"send_song_{channel}_{msg_id}"
        keyboard.append([InlineKeyboardButton(label, callback_data=callback_data)])
    keyboard.append([InlineKeyboardButton("🔄 Refresh", callback_data="refresh_queue")])

    reply_markup = InlineKeyboardMarkup(keyboard)

    if context.user_data.get("START_OVER"):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            text="Random Songs from {}:".format(channel),
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "Random Songs from {}:".format(channel),
            reply_markup=reply_markup
        )

    context.user_data["START_OVER"] = False
    
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    data = query.data

    if data == "refresh_queue":
        context.user_data["START_OVER"] = True
        await queue(update, context)
        return
    
    if data == "refresh_queue_mix":
        context.user_data["START_OVER"] = True
        await queue(update, context)
        return

    if data.startswith("send_song_"):
        _, _, channel, msg_id = data.split("_", 3)
        msg_id = int(msg_id)
        song = get_song_by_channel_and_msg_id(channel, msg_id)
        if song:
            channel, msg_id, performer, filename, duration, date, title, is_album, media_group_id = song
            url = (
                f"https://t.me/thecrate/{msg_id}"
                if channel == "main"
                else f"https://t.me/crateofnotsodasbutmusic/{msg_id}"
            )
            try:
                await query.message.reply_audio(url)
            except (AttributeError, BadRequest):
                await query.message.reply_text(
                    f"[  🃜🃚🃖🃁🂭🂺  ]({url})",
                    parse_mode=ParseMode.MARKDOWN,
                )
        await query.answer()
    elif data.startswith("set_channel:"):
        channel = data.split(":", 1)[1]
        context.user_data["channel"] = channel
        await query.answer(f"Channel set to {channel}!")
        await query.edit_message_text(
            f"✅ Channel switched to: <b>{channel}</b>", parse_mode="HTML"
        )
    else:
        await query.answer()
        
async def queue_mix(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /next is issued."""
    channel = context.user_data.get("channel")  
    songs = get_long_songs(channel, count=10)
    if not songs:
        await update.message.reply_text("No songs 10 minutes or longer found! in {}".format(channel))
        return

    keyboard = []
    for s in songs:
        mins, secs = divmod(s[4], 60)
        time_str = f"{mins}:{secs:02d}"
        album_icon = "💿 " if s[7] else ""
        title = s[6]
        if not title:
            title = s[3]
        button_text = f"{album_icon}{title} — {time_str}"
        callback_data = f"send_song_{s[0]}_{s[1]}"
        keyboard.append([InlineKeyboardButton(button_text, callback_data=callback_data)])
    keyboard.append([InlineKeyboardButton("🔄 Refresh", callback_data="refresh_queue_mix")])

    reply_markup = InlineKeyboardMarkup(keyboard)

    if context.user_data.get("START_OVER"):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            "Select a song from {}:".format(channel),
            reply_markup=reply_markup
        )

        await update.callback_query.edit_message_text(
            text="Random Songs from {}:".format(channel),
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "Random Songs from {}:".format(channel),
            reply_markup=reply_markup
        )

    context.user_data["START_OVER"] = False
    
