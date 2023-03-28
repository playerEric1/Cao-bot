import settings
import func

import sys
import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands

this = sys.modules[__name__]
this.running = False

# Initialize the client
print("Starting up...")
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = commands.Bot(command_prefix=settings.COMMAND_PREFIX, intents=intents)


@client.event
async def on_ready():
    if this.running:
        return

    this.running = True

    # Set the playing status
    if settings.NOW_PLAYING:
        print("Setting now playing game", flush=True)
        await client.change_presence(
            activity=discord.Game(name=settings.NOW_PLAYING))

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')  # print all members
    default_channel = client.get_channel(settings.DEFAULT_CHANNEL)  # channel id should be an int
    await default_channel.send(f'我上线啦')


@client.command()
async def sleep(ctx, arg):
    await ctx.send('我不能说话啦')
    await client.unload_extension('modules.events')
    await client.change_presence(activity=discord.Game(name="禁言中"))
    await asyncio.sleep(int(arg))

    # awake
    await client.load_extension('modules.events')
    await ctx.send('我活啦')
    await client.change_presence(activity=discord.Game(name=settings.NOW_PLAYING))


@client.command(name='close')
@func.owner()  # Only authorized member can do this command
async def close(ctx):  # Close the bot
    await ctx.send('我睡觉去啦')
    print("Bot Closed")
    await client.close()


async def main():
    async with client:
        if __name__ == "__main__":
            await client.load_extension('modules.events')
            await client.load_extension('modules.daily_math')
            await client.load_extension('modules.wfalpha')
            await client.load_extension('modules.simple_cog')
            await client.load_extension('modules.help')
            await client.load_extension('modules.voice')
            await client.load_extension('modules.wiki')
            await client.load_extension('modules.tex')
            await client.load_extension('modules.food')
            await client.load_extension('modules.utils')
            await client.load_extension('modules.confirm')
            await client.load_extension('modules.counter')
            # await client.load_extension('modules.ai')
            await client.load_extension('modules.vector_plot')
            print("load cogs!")
            await client.start(TOKEN)


asyncio.run(main())
