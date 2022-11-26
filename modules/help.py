import discord
from discord.ext import commands
from discord.errors import Forbidden


async def send_embed(ctx, embed):
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


class Helper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def h(self, ctx, *args):
        """Shows all modules of that bot"""

        # !SET THOSE VARIABLES TO MAKE THE COG FUNCTIONAL!
        prefix = "."  # ENTER YOUR PREFIX - loaded from config, as string or how ever you want!
        owner = 765212693795307520  # ENTER YOU DISCORD-ID
        owner_name = "_Ikuta#7350"  # ENTER YOUR USERNAME#1234

        # checks if cog parameter was given
        # if not: sending all modules and commands not associated with a cog
        if not args:
            # checks if owner is on this server - used to 'tag' owner
            try:
                owner = ctx.guild.get_member(owner).mention

            except AttributeError as e:
                owner = owner

            # starting to build embed
            emb = discord.Embed(title='Commands and modules', color=discord.Color.blue(),
                                description=f'Use `{prefix}help <module>` to gain more information about that module '
                                            f':smiley:\n')

            # iterating trough cogs, gathering descriptions
            cogs_desc = ''
            for cog in self.bot.cogs:
                cogs_desc += f'`{cog}` {self.bot.cogs[cog].__doc__}\n'

            # adding 'list' of cogs to embed
            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            # integrating trough uncategorized commands
            commands_desc = ''
            for command in self.bot.walk_commands():
                # if cog not in a cog
                # listing command if cog name is None and command isn't hidden
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            # adding those commands to embed
            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            # setting information about author
            emb.add_field(name="About", value=f"The Bots is developed by {owner_name}, based on discord.py.\n\
                                    This version of it is maintained by {owner}\n\
                                    Please visit https://github.com/playerEric1/Cao-bot to submit ideas or bugs.")

        # block called when one cog-name is given
        # trying to find matching cog and it's commands
        else:
            # iterating trough cogs
            for cog in self.bot.cogs:
                # check if cog is the matching one
                if cog.lower() == args[0].lower():

                    # making title - getting description from doc-string below class
                    emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
                                        color=discord.Color.green())

                    # getting commands from cog
                    for command in self.bot.get_cog(cog).get_commands():
                        # if cog is not hidden
                        if not command.hidden:
                            emb.add_field(name=f"`{prefix}{command.name}`", value=command.help, inline=False)
                    # found cog - breaking loop
                    break

            # if input not found
            # yes, for-loops have an else statement, it's called when no 'break' was issued
            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{args[0]}` before :scream:",
                                    color=discord.Color.orange())

        # sending reply embed using our own function defined above
        await send_embed(ctx, emb)


async def setup(client):
    await client.add_cog(Helper(client))
