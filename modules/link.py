from discord.ext import commands
import discord
from urllib.parse import quote_plus


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
        await interaction.response.send_message(content=f"今天吃 {self.values[0]}!", ephemeral=False)


# Define a simple View that gives us a google link button.
# We take in `query` as the query that the command author requests for
class Google(discord.ui.View):
    def __init__(self, query: str):
        super().__init__()
        # we need to quote the query string to make a valid url. Discord will raise an error if it isn't valid.
        query = quote_plus(query)
        url = f'https://www.google.com/search?q={query}'

        # Link buttons cannot be made with the decorator
        # Therefore we have to manually create one.
        # We add the quoted url to the button, and add the button to the view.
        self.add_item(discord.ui.Button(label='Click Here', url=url))


class Gg(commands.Cog):
    """ Generate a dropdown menu where you can select your dish for today! """

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def google(self, ctx: commands.Context, *, query: str):
        """Returns a google link for a query"""
        await ctx.send(f'Google Result for: `{query}`', view=Google(query))


async def setup(client):
    await client.add_cog(Gg(client))
