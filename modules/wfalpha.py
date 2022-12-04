import os
import discord
import random
from discord.ext import commands

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


@commands.command()
async def w(ctx, *, arg):
    """use '.w' (or any customized command prefix) + any you would like to search on wolframalpha"""
    print("received")
    text = waclient.query(arg)
    for pod in text.pods:
        for sub in pod.subpods:
            embed = discord.Embed()
            embed.set_image(url=sub.img.src)
            await ctx.send(embed=embed)


async def setup(bot):
    bot.add_command(w)
