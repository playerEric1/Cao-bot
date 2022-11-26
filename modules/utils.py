import discord
import random
from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pnm! {round(self.client.latency * 1000)}ms")
        return


async def setup(client):
    await client.add_cog(Utils(client))
