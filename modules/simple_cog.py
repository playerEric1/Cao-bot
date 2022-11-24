import discord
import random
from discord.ext import commands


@commands.command()
async def test(ctx, arg="我还活着"):
    await ctx.send(arg)


@commands.command()
async def random(ctx, arg1=1, arg2=6):
    num = random.randint(arg1, arg2)
    await ctx.send(num)


@commands.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.display_name}.')


@commands.command()
async def wiki(ctx, arg="Minecraft"):
    arg = arg.replace(" ", "_")
    await ctx.send("https://en.wikipedia.org/wiki/" + arg)


@commands.command()  # incomplete
async def slap(ctx):
    user = random.choice(ctx.message.channel.guild.members)
    # slapper = ctx.author.mention
    await ctx.send(f"粪男bot 拍了拍 {user.mention()}")


@commands.command()
async def image(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://picsum.photos/536/354")
    await ctx.send(embed=embed)


@commands.command()
@commands.is_owner()
async def only_me(ctx):
    """A simple command which only responds to the owner of the bot."""

    await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you!!')


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
    bot.add_command(hello)
    bot.add_command(random)
    bot.add_command(wiki)
    bot.add_command(only_me)
    bot.add_command(embed)