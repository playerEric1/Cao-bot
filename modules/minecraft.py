from discord.ext import commands


class Minecraft(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def mc(self, ctx, *args):
        arg_str = '_'.join(args)
        await ctx.send("https://minecraft.gamepedia.com/" + arg_str)


async def setup(client):
    await client.add_cog(Minecraft(client))
