from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]
    
if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"not compatible with your current PTB version {TG_VER}."
    )
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultArticle,
    helpers
    )

from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    PicklePersistence,
    InlineQueryHandler,
    ConversationHandler,
    CallbackQueryHandler,
    filters
    )

from telegram.helpers import escape_markdown

from telegram.error import (
    TelegramError,
    BadRequest
    )

from uuid import uuid4
from html import escape
from io import BytesIO

import random, os, re, json, traceback, logging, librosa, time
