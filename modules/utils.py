import time
import discord
import random
from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        start_time = time.time()
        msg = await ctx.send(f"My ping is {round(self.client.latency * 1000)}ms")
        send_time = (time.time() - start_time) * 1000
        await msg.edit(
            content=f"{msg.content} but it took {send_time:.2f}ms to send this message"
        )


async def setup(client):
    await client.add_cog(Utils(client))
