from api.imports import *
from api.variables import *
from api.utils import *

# Globals for paging
search_results = []
page_number = 1
page_size = 10

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Simple search: returns 'active' if a filename matches, else 'not found'. Stores results for paging."""
    global search_results, page_number, page_size

    query_text = update.message.text
    search_results = search_filenames(query_text)

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
        
async def inlinequery(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    results = []
    channel = context.user_data.get("channel")  # Optional: filter per channel

    # Reuse your existing search helper
    for msg_id, filename, title, *_ in search_filenames(update.message.text):
        results.append(
            InlineQueryResultAudio(
                id=str(uuid4()),
                audio_url=f"{dcr8_url}{msg_id}",
                title=title or filename
            )
        )
        await update.inline_query.answer(results, auto_pagination=True)
        
