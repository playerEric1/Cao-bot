import settings
import message_handler
import func

import sys
import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands

CLIENT_PUBLIC_KEY = os.getenv('CLIENT_PUBLIC_KEY')

this = sys.modules[__name__]
this.running = False

# Initialize the client
print("Starting up...")

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)

global mute
mute = False


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

    global guild
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
    await default_channel.send(f'粪男bot上线啦')


@client.event
async def on_voice_state_update(member, before, after):
    if mute:
        return

    print(member.name + " has joined a voice channel")
    default_channel = client.get_channel(settings.DEFAULT_CHANNEL)  # channel id should be an int

    # process mute status
    if not before.afk and after.afk:  # enter afk channel from another channel
        await default_channel.send(member.name + " 失踪了")
    elif not before.self_mute and after.self_mute:
        await default_channel.send(member.name + " 怎麽不叫了")
    elif not before.mute and after.mute:
        await default_channel.send(member.name + " 還能説話嗎")
    elif before.self_mute and after.mute:
        await default_channel.send(member.name + " 都已经自我禁评了啊")
    elif not before.self_stream and after.self_stream:
        await default_channel.send(member.name + " 开播了")

    elif before.channel is None and after.channel is not None:
        if member.name == "_Ikuta":
            await default_channel.send("主要人員來啦")
        else:
            await default_channel.send("次要人員" + member.name + "來啦")
    elif before.channel is not None and after.channel is None:
        if member.name == "_Ikuta":
            await default_channel.send("主要人員睡觉去啦")
        else:
            await default_channel.send("次要人員" + member.name + "睡觉去啦")
    print("voice_state_update sent")


@client.event
async def on_message(message):
    if mute or message.author == client.user:
        return

    reply = message_handler.process_message(message.content)
    if reply is not None:  # do not send empty messages
        # await asyncio.sleep(len(reply) / 10 + 0.3) # add some delay before sending
        await message.channel.send(reply)
    await client.process_commands(message)  # always process the commands


@client.event
async def on_message_delete(message):
    if mute or message.author == client.user:
        return

    msg = f'{message.author} 刚说了: {message.content}'
    await message.channel.send(msg)


@client.command()
async def sleep(ctx, arg):
    global mute
    await ctx.send(f'粪男bot不能说话啦')
    mute = True
    if settings.NOW_PLAYING:
        print("Setting now playing game", flush=True)
        await client.change_presence(
            activity=discord.Game(name="禁言中"))
    await asyncio.sleep(int(arg))

    # awake
    mute = False
    await ctx.send(f'我活啦')
    if settings.NOW_PLAYING:
        print("Setting now playing game", flush=True)
        await client.change_presence(
            activity=discord.Game(name=settings.NOW_PLAYING))


@client.command(name='close')
@func.owner()
async def close(ctx):  # Close the bot
    await ctx.send(f'粪男bot睡觉去啦')
    print("Bot Closed")
    await client.close()


@client.event
async def on_command_error(message, error):
    if isinstance(error, commands.errors.CommandNotFound):
        print(error)
        return await message.channel.send("Command not found!")
    if isinstance(error, commands.errors.MissingRequiredArgument):
        print(error)
        return await message.channel.send('Not enough arguments!')
    if isinstance(error, commands.errors.MissingPermissions):
        print(error)
        return await message.channel.send('You do not have permissions!')
    raise error


async def main():
    # start the client
    async with client:
        if __name__ == "__main__":
            # await client.load_extension('modules.daily_math')
            await client.load_extension('modules.wfalpha')
            await client.load_extension('modules.simple_cog')
            await client.load_extension('modules.cat')
            print("load cogs!")
            await client.start(TOKEN)


asyncio.run(main())
