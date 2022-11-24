import os

import wolframalpha
from dotenv import load_dotenv

load_dotenv()

# Wolfram Alpha credentials and client session Discord_py
app_id = os.getenv('WFA_APPID')
waclient = wolframalpha.Client(app_id)

messageHistory = set()
computemessageHistory = set()
previousQuery = ''

# Fun strings for invalid queries
invalidQueryStrings = ["Nobody knows.", "It's a mystery.", "I have no idea.", "No clue, sorry!",
                       "I'm afraid I can't let you do that.", "Maybe another time.", "Ask someone else.",
                       "That is anybody's guess.", "Beats me.", "I haven't the faintest idea."]

def inquery(arg):
    res = waclient.query(arg)
    return res