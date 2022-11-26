import discord
import random
from discord.ext import commands


@commands.command()  # incomplete
async def slap(ctx):
    user = random.choice(ctx.message.channel.guild.members)
    # slapper = ctx.author.mention
    await ctx.send(f"粪男bot 拍了拍 {user.mention()}")


@commands.command()
@commands.is_owner()
async def only_me(ctx):
    """A simple command which only responds to the owner of the bot."""

    await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you!!')


@commands.command()
async def ping(ctx):
    await ctx.send(f"pnm! {round(commands.latency * 1000)}ms")
    return


async def setup(bot):
    bot.add_command(only_me)
    bot.add_command(ping)
