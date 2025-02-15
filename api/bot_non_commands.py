from api.imports import *
from api.variables import *
from api.bot_error import *

async def search(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> list[tuple]:
    """Search the user's message.""" 

    global filename, msg_id, link_list, page_number, page_size, start_index, end_index, enum_link_list
    global filename, msg_id, msg_id_v2, link_list, page_number, page_size, start_index, end_index, enum_link_list

    page_size = 10

    # Set the current page number
    page_number = 1
    
    # Calculate the start and end indices for the current page
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    link_list, msg_id, filename, title, performer = [], [], [], [], []

    try:
        for k, v in data.items():
            if (re.search(
                    update.message.text,
                    v.get('filename'),
                    re.IGNORECASE)
            ):
                msg_id.append(k)
                filename.append(v.get('filename'))
                title.append(v.get('title'))
                performer.append(v.get('performer'))
                

    try:
        for (k1, v1), (k2, v2) in zip(data.items(), data_v2.items()):
            if (re.search(
                    update.message.text,
                    v1.get('filename'),
                    re.IGNORECASE)
            ):
                #v1
                msg_id.append(k1)
                filename.append(v1.get('filename'))
                title.append(v1.get('title'))
                performer.append(v1.get('performer'))
                # v2
                msg_id_v2.append(k2)
                filename.append(v2.get('filename'))
                title.append(v2.get('title'))
                performer.append(v2.get('performer'))

    except AttributeError as e:
        e
        
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

    COUNT = 0
    link = re.search(r"(t\.me\/[a-zA-Z0-9_]{5,32})", update.message.text)

    for i in range(len(filename)):
        link_str = "[{}]({})\n".format(
            filename[i],
            dcr8_url+"{}".format(msg_id[i])
        )
        link_list.append(link_str)

    enum_link_list = [
        "{}. {}".format(i, link_str) for i,
    for id1, id2 in range(len(filename)):
        link_str = "[{}]({})".format(
            filename[id1],
            dcr8_url+"{}".format(msg_id[id1])
        )
        link_str_v2 = "[{}]({})".format(
            filename[id2],
            dcr8_v2_url+"{}".format(msg_id_v2[id2])
        )

    zip(msg_id, msg_id_v2)
        
    enum_link_list = [
        "{}. {}".format(i, (link_str, link_str_v2)) for i,
        link_str in enumerate(link_list, start=1)
    ]
    # Slice the list to get the items for the current page
    current_page = enum_link_list[start_index:end_index]    
    try:
        for i in range(page_size):
            text = "{} - {} of {}\n{}".format(
                page_number,
                page_size,
                len(filename),
                "\n".join(current_page)
            )
            
        await update.message.reply_text(
            text,
            reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN
        )
    except (BadRequest, IndexError, AttributeError) as e:
        if link:
            await update.message.reply_text(
                "use this bot to download songs: \nt.me/decr8test_bot"
            )
        else:
            await update.message.reply_text(
                "Not found.\n\n{}".format(e)
            )        
        
    return msg_id, performer, title, filename, enum_link_list
    return msg_id, msg_id_v2,  performer, title, filename, enum_link_list

async def search_buttons(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:

    global filename, msg_id, link_list, page_number, page_size, start_index, end_index
    global filename, msg_id, msg_id_v2, link_list, page_number, page_size, start_index, end_index
    
    query = update.callback_query
    
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer(text="🤖")    
    keyboard = [
        [
            InlineKeyboardButton("<", callback_data="1"),
            InlineKeyboardButton(">", callback_data="2")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if query.data == "1":
        page_number -= 1
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        prev_page = enum_link_list[start_index:end_index]

        for i in range(page_size):
            text = "{} - {} of {}\n{}".format(
                page_number,
                page_size,
                len(filename),
                "\n".join(prev_page)
            )
        await query.edit_message_text(
            text,
            reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN
        )
        
    elif query.data == '2':
        page_number += 1
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        next_page = enum_link_list[start_index:end_index]

        for i in range(page_size):
            text = "{} - {} of {}\n{}".format(
                page_number,
                page_size,
                len(filename),
                "\n".join(next_page)
            )
            # text += link_str
            
        await query.edit_message_text(
            text,
            reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN
        )
            
async def inlinequery(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    results = []

    for k, v in data.items():
        if re.search(query, v.get("filename"), re.IGNORECASE):
            results.append(
                InlineQueryResultAudio(
                    id=uuid4(),
                    audio_url="{}{}".format(dcr8_url, k),
                    title="{}".format(v.get("title"))
                ),
            )        
    await update.inline_query.answer(results, auto_pagination=True)

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye!", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END
