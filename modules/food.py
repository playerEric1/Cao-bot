from discord.ext import commands
import discord


# Defines a custom Select containing colour options
# that the user can choose. The callback function
# of this class is called when the user changes their choice
class Select(discord.ui.Select):
    def __init__(self):
        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label="่็้ฃฏ", emoji="๐", description="12ๅ"),
            discord.SelectOption(label="่พฃ่้บต", emoji="๐", description="15ๅ"),
            discord.SelectOption(label="็ด็ๆ้ชจ", emoji="๐", description="22ๅ")
        ]
        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder="่ซ้ธๆไธ็จฎzc!", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"ไปๅคฉๅ {self.values[0]}!", ephemeral=False)


class SelectView(discord.ui.View):
    def __init__(self, *, timeout=1800):
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
        await ctx.send("่ซ็่ๅฎ!", view=view)


async def setup(client):
    await client.add_cog(Zc(client))
