import discord
from discord.ext import commands
import wikipedia


class Wiki(commands.Cog):
    """wwwwwwwwwwwwww"""
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def wiki(self, ctx, *args):
        """wwwwwwwwwwwwww"""
        args_str = '_'.join(args)
        try:
            wiki = wikipedia.page(args_str)
        except:
            await ctx.send("https://en.wikipedia.org/wiki/" + args_str)
        summary = wikipedia.summary(args_str, sentences=3)
        embed = discord.Embed(title=wiki.title, description=summary, url=wiki.url, color=0xffffff)
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Wiki(client))
