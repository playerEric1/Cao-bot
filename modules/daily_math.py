import asyncio
import discord
from discord.ext import commands

class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def math(self, ctx):
        print("!!!!!!!!!!")
        first_run = True
        while True:
            if first_run:
                page1 = discord.Embed(title='Page 1/3', description='Description1', colour=discord.Colour.orange())
                first_run = False
                msg = await ctx.send(embed=page1)

                reactmoji = ["1️⃣", "2️⃣", "3️⃣"]

                for react in reactmoji:
                    await msg.add_reaction(react)

            def check_react(reaction, user):
                if reaction.message.id != msg.id:
                    return False
                if user != ctx.message.author:
                    return False
                if str(reaction.emoji) not in reactmoji:
                    return False
                return True

            try:
                res, user = await self.client.wait_for('reaction_add', check=check_react)
            except asyncio.TimeoutError:
                return await msg.clear_reactions()

            if user != ctx.message.author:
                pass
            elif '1️⃣' in str(res.emoji):
                print('<<1️⃣>>')
                await msg.remove_reaction("1️⃣", user)
                await msg.edit(embed=page1)
            elif '2️⃣' in str(res.emoji):
                print('<<2️⃣>>')
                page2 = discord.Embed(title='Page 2/3', description='Description2', colour=discord.Colour.orange())
                await msg.remove_reaction("2️⃣", user)
                await msg.edit(embed=page2)
            elif '3️⃣' in str(res.emoji):
                print('<<3️⃣>>')
                page3 = discord.Embed(title='Page 3/3', description='Description3', colour=discord.Colour.orange())
                await msg.remove_reaction("3️⃣", user)
                await msg.edit(embed=page3)


async def setup(client):
    await client.add_cog(Math(client))
