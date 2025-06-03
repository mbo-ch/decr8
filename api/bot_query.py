from api.imports import *
from api.variables import *

# Globals for paging
search_results = []
page_number = 1
page_size = 10

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Simple search: returns 'active' if a filename matches, else 'not found'. Stores results for paging."""
    global search_results, page_number, page_size

    query_text = update.message.text
    search_results = [v.get('filename') for v in data.values() if re.search(query_text, v.get('filename', ''), re.IGNORECASE)]

    page_number = 1  # Reset to first page

    if search_results:
        await send_page(update)
    else:
        await update.message.reply_text("Status: not found")

async def send_page(update_or_query):
    """Helper to send current page of results."""
    global search_results, page_number, page_size

    start = (page_number - 1) * page_size
    end = start + page_size
    current_page = search_results[start:end]

    if not current_page:
        text = "No results."
    else:
        text = "Status: active\n" + "\n".join(f"{i+1}. {name}" for i, name in enumerate(current_page, start=start))

    keyboard = [
        [
            InlineKeyboardButton("<", callback_data="prev"),
            InlineKeyboardButton(">", callback_data="next"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Support both message and callback_query objects
    if hasattr(update_or_query, "edit_message_text"):
        await update_or_query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await update_or_query.message.reply_text(text, reply_markup=reply_markup)

async def search_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles pagination for search results."""
    global page_number

    query = update.callback_query
    await query.answer(text="🤖")    

    if query.data == "prev" and page_number > 1:
        page_number -= 1
    elif query.data == "next":
        page_number += 1

    await send_page(query)
    
async def inlinequery(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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

