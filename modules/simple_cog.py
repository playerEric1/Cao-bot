import discord
import random
from discord.ext import commands


@commands.command()
async def random(ctx, arg1=1, arg2=6):
    # num = random.randint(arg1, arg2) # randint not working?
    await ctx.send(114514)


@commands.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.display_name}.')


@commands.command()
async def image(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://picsum.photos/536/354")
    await ctx.send(embed=embed)


@commands.command()
async def embed(ctx):
    embed = discord.Embed(title='Example Embed',
                          description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
                          colour=0x98FB98)
    embed.set_author(name='MysterialPy',
                     url='https://gist.github.com/MysterialPy/public',
                     icon_url='http://i.imgur.com/ko5A30P.png')
    embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

    embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
    embed.add_field(name='Command Invoker', value=ctx.author.mention)
    embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

    await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)


async def setup(bot):
    bot.add_command(random)
    bot.add_command(hello)
    bot.add_command(image)
    bot.add_command(embed)
