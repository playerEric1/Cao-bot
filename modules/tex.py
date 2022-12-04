from discord.ext import commands
from sympy import preview, symbols
import discord
from io import BytesIO


class Latex(commands.Cog):
    """use '.tex' (or any customized command prefix) + latex expression"""

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def tex(self, ctx, arg):
        x, y = symbols("x,y")
        buf = BytesIO()
        print("received!")
        try:
            preview(
                x + y,
                outputTexFile="sample.tex")
        except RuntimeError:
            await ctx.send("Invalid syntax")
            return

        buf.seek(0)
        files = discord.File(filename="sample.tex")

        if files:
            print("success!")
            await ctx.send(files=files)


async def setup(client):
    await client.add_cog(Latex(client))
