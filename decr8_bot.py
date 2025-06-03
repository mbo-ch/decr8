# -*- coding: utf-8 -*-

import os, sys, json

from uuid import uuid4

from api.variables import *
from api.bot_command import *
from api.bot_query import *

#from telegram.utils import (
#    helpers
#    )

def main():
    
    from api import bot_handler
    
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    # Start the Bot
    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # run_polling() is non-blocking and will stop the bot gracefully.
    application.run_polling()
       
        
if __name__ == "__main__":
    sys.path.append("/home/decr8/decr8/api")
    main()
    
