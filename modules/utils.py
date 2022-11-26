import discord
import random
from discord.ext import commands


@commands.command()  # incomplete
async def slap(ctx):
    user = random.choice(ctx.message.channel.guild.members)
    # slapper = ctx.author.mention
    await ctx.send(f"粪男bot 拍了拍 {user.mention()}")


@commands.command()
async def ping(ctx):
    await ctx.send(f"pnm! {round(commands.latency * 1000)}ms")
    return


async def setup(bot):
    bot.add_command(ping)
