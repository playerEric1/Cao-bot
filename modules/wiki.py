import discord
from discord.ext import commands
import wikipedia

# Parse wikipedia pages into summary contained in Discord embed
class Wiki(commands.Cog):
    """use '.' (or any customized command prefix) + wiki + the wikipedia page you would like to search"""

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def wiki(self, ctx, *args):
        """use '.' (or any customized command prefix) + wiki + language (default: English; cn: Chinese; ja: Japanese + the
        wikipedia page you would like to search """

        # return wikipedia pages of other languages if received such command
        if args[0] == 'cn':
            await ctx.send("https://zh.wikipedia.org/wiki/" + '_'.join(args)[1:])
        elif args[0] == 'jp' or args[0] == 'ja':
            await ctx.send("https://ja.wikipedia.org/wiki/" + '_'.join(args)[1:])
        else:
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
