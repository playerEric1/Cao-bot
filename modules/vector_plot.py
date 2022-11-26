import numpy as np
import matplotlib.pyplot as plt
import discord
from discord.ext import commands


@commands.command()
async def vec(ctx, arg1="-Y / (X ** 2 + Y ** 2)", arg2="X / (X ** 2 + Y ** 2)"):
    # 1D arrays
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)

    # Mesh grid
    X, Y = np.meshgrid(x, y)

    # Assign vector directions
    Ex = eval(arg1)
    Ey = eval(arg2)

    # Depict illustration
    plt.figure(figsize=(10, 10))
    plt.streamplot(X, Y, Ex, Ey, density=1.4, linewidth=None, color='#A23BEC')

    plt.savefig('vec.png')
    file = discord.File("vec.png")
    await ctx.send(file=file)


async def setup(bot):
    bot.add_command(vec)
