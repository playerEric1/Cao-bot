import os

# https://discord.com/api/oauth2/authorize?client_id=1038261014409519155&permissions=8&scope=bot

# The prefix that will be used to parse commands.
# It doesn't have to be a single character
COMMAND_PREFIX = "."

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = "小便"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Copy the ID of the channel where you want the bot to send messages
DEFAULT_CHANNEL = 925476993158508607  # It should be an int!
