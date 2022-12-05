from discord.ext import commands
import discord
import json
import requests
from random import randint, seed, random


# Defines a custom Select containing colour options
# that the user can choose. The callback function
# of this class is called when the user changes their choice
class Select(discord.ui.Select):
    def __init__(self):
        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label="蛋炒飯", emoji="🍚", description="12元"),
            discord.SelectOption(label="辣肉麵", emoji="🍜", description="15元"),
            discord.SelectOption(label="紅燒排骨", emoji="🍖", description="22元")
        ]
        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder="請選擇一種zc!", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"今天吃 {self.values[0]}!", ephemeral=True)


class SelectView(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

        # Adds the dropdown to our view object.
        self.add_item(Select())


class Zc(commands.Cog):
    """ Generate a dropdown menu where you can select your dish for today! """

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def menu(self, ctx):
        # Create the view containing our dropdown
        view = SelectView()

        # Sending a message containing our view
        await ctx.send("請看菜單!", view=view)


async def setup(client):
    await client.add_cog(Zc(client))
