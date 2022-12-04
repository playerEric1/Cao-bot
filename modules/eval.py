from discord.ext import commands


class Eval(commands.Cog):
    """use '.eval' (or any customized command prefix) + math equation you would like to calculate"""

    def __init__(self, client):
        self.client = client

    # @commands.command(pass_context=True)
    # async def eval(self, ctx, *args):
    #     arg_str = '_'.join(args)
    #     await ctx.send(eval(arg_str))


async def setup(client):
    await client.add_cog(Eval(client))
