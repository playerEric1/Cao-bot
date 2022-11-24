from mimetypes import common_types
import discord
from discord.ext import commands
import json
import requests
from datetime import datetime, timedelta
from random import randint, seed, random


@commands.command(pass_comtext=True)
async def cat(ctx):
    await ctx.message.delete()
    await _find(ctx.message, 'cat')


@commands.command(pass_comtext=True)
async def dog(ctx):
    await _find(ctx.message, 'dog')


@commands.command(pass_comtext=True)
async def fox(ctx):
    await _find(ctx.message, 'fox')


@commands.command(pass_comtext=True)
async def koala(ctx):
    await _find(ctx.message, 'koala')


@commands.command(pass_comtext=True)
async def panda(ctx):
    if (randint(1, 3) == 1):
        await _find(ctx.message, 'red_panda')
    else:
        await _find(ctx.message, 'panda')


@commands.command(pass_context=True)
async def duck(message):
    await message.message.delete()
    response = requests.get('https://random-d.uk/api/random')
    json_data = json.loads(response.text)
    embed = discord.Embed(color=0xff9900)
    embed.set_image(url=json_data['url'])
    embed.set_footer(text="requested by:" + message.author.name + '#' + message.author.discriminator)
    await message.channel.send(embed=embed)


@commands.command(pass_context=True)
async def slap(ctx, user: discord.User):
    await ctx.message.delete()
    await ctx.message.channel.send(f'{ctx.message.author.mention} slaps {user.mention} with a large trout')


async def _find(message, animal):
    response = requests.get('https://some-random-api.ml/img/' + animal)
    json_data = json.loads(response.text)
    print(json_data)
    embed = discord.Embed(color=0xff9900)
    embed.set_image(url=json_data['link'])
    embed.set_footer(text="requested by:" + message.author.name + '#' + message.author.discriminator)
    await message.channel.send(embed=embed)


async def setup(bot):
    bot.add_command(cat)
    bot.add_command(duck)
