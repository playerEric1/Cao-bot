from discord.ext import commands
import discord


# Define a simple View that gives us a confirmation menu
class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Confirming', ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Cancelling', ephemeral=True)
        self.value = False
        self.stop()


class Cf(commands.Cog):
    """ Generate a dropdown menu where you can select your dish for today! """

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ask(self, ctx: commands.Context):
        """Asks the user a question to confirm something."""
        # We create the view and assign it to a variable so we can wait for it later.
        view = Confirm()
        await ctx.send('Do you want to continue?', view=view)
        # Wait for the View to stop listening for input...
        await view.wait()
        if view.value is None:
            print('Timed out...')
        elif view.value:
            print('Confirmed...')
        else:
            print('Cancelled...')


async def setup(client):
    await client.add_cog(Cf(client))
