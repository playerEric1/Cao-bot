import wolframalpha

# Wolfram Alpha credentials and client session Discord_py
app_id = '44GJT6-5KULL99HGG'
waclient = wolframalpha.Client(app_id)

# Globals for message removal
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