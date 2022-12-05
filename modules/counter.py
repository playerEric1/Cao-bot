from discord.ext import commands
import discord


# Define a simple View that gives us a counter button
class Counter(discord.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @discord.ui.button(label='0', style=discord.ButtonStyle.red)
    async def count(self, button: discord.ui.Button, interaction: discord.Interaction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = discord.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)
        await interaction.response.send_message("別按了")
        try:
            interaction.respond()
        except:
            pass


# Define a simple View that gives us a counter button
class Ctr(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def counter(self, ctx: commands.Context):
        """Starts a counter for pressing."""
        await ctx.send('Press!', view=Counter())


async def setup(client):
    await client.add_cog(Ctr(client))
