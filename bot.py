import settings
import message_handler
import wfalpha

import sys
import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands

CLIENT_PUBLIC_KEY = os.getenv('CLIENT_PUBLIC_KEY')

this = sys.modules[__name__]
this.running = False

if __name__ == '__main__':
    # Initialize the client
    print("Starting up...")

    load_dotenv()

    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')

    intents = discord.Intents.all()
    client = commands.Bot(command_prefix='.', intents=intents)


    @client.event
    async def on_ready():
        if this.running:
            return

        global mute
        mute = False

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
        global mute
        if mute:
            return
        print("Recognized that " + member.name + " has joined a voice channel")
        default_channel = client.get_channel(settings.DEFAULT_CHANNEL)  # channel id should be an int
        if after.self_mute:
            await default_channel.send(member.name + "怎麽不叫了")
        if after.mute:
            await default_channel.send(member.name + "還能説話嗎")
        if member.name == "_Ikuta":
            await default_channel.send("主要人員" + member.name + "來啦")
        else:
            await default_channel.send("次要人員 " + member.name + " 來啦")
        print("Sent message to " + member.name)
        # embed = discord.Embed(
        #     title="Welcome " + member.name + "!",
        #     description="We're so glad you're here!",
        #     color=discord.Color.green()
        # )

        # role = discord.utils.get(member.server.roles, name="name-of-your-role")  # Gets the member role as a `role` object
        # await client.add_roles(member, role)  # Gives the role to the user
        # print("Added role '" + role.name + "' to " + member.name)


    #
    # @client.event
    # async def on_member_leave(member):
    #     print("Recognised that a member called " + member.name + " left")
    #     embed = discord.Embed(
    #         title="😢 Goodbye " + member.name + "!",
    #         description="Until we meet again old friend.",  # A description isn't necessary, you can delete this line if
    #         # you don't want a description.
    #         color=discord.Color.red()  # There are lots of colors, you can check them here:
    #         # https://discordpy.readthedocs.io/en/latest/api.html?highlight=discord%20color#discord.Colour
    #     )

    @client.event
    async def on_message(message):
        global mute
        if mute or message.author == client.user:
            return

        reply = message_handler.process_message(message.content)
        if reply != None:  # will reply something
            # await asyncio.sleep(len(reply) / 10 + 0.3)
            await message.channel.send('@' + message.author.name + ' ' + reply)
        await client.process_commands(message)  # regardlessly process the commands


    @client.event
    async def on_message_delete(message):
        msg = f'{message.author} 從未説過: {message.content}'
        await message.channel.send('刪評')
        await message.channel.send(msg)


    @client.command()
    async def test(ctx, arg):
        await ctx.send(arg)


    @client.command()
    async def sleep(ctx, arg):
        global mute
        default_channel = client.get_channel(settings.DEFAULT_CHANNEL)  # channel id should be an int
        await default_channel.send(f'粪男bot不能说话啦')
        mute = True
        if settings.NOW_PLAYING:
            print("Setting now playing game", flush=True)
            await client.change_presence(
                activity=discord.Game(name="禁言中"))
        await asyncio.sleep(int(arg))
        mute = False
        await default_channel.send(f'我活啦')
        if settings.NOW_PLAYING:
            print("Setting now playing game", flush=True)
            await client.change_presence(
                activity=discord.Game(name=settings.NOW_PLAYING))


    @client.command()
    async def w(ctx, arg):
        print("received")
        default_channel = client.get_channel(settings.DEFAULT_CHANNEL)  # channel id should be an int
        text = wfalpha.inquery(arg)
        for pod in text.pods:
            for sub in pod.subpods:
                embed = discord.Embed()
                embed.set_image(url=sub.img.src)
                await default_channel.send(embed=embed)
                # await default_channel.send(sub.plaintext)


    # Close the bot
    @client.command()
    async def close(ctx):
        default_channel = client.get_channel(settings.DEFAULT_CHANNEL)  # channel id should be an int
        await default_channel.send(f'粪男bot睡觉去啦')
        await client.close()
        print("Bot Closed")


    @client.command()
    async def image(ctx):
        default_channel = client.get_channel(settings.DEFAULT_CHANNEL)  # channel id should be an int
        embed = discord.Embed()
        embed.set_image(
            url="https://picsum.photos/536/354")
        await default_channel.send(embed=embed)


    async def main():
        # do other async things

        # start the client
        async with client:
            await client.start(TOKEN)


    asyncio.run(main())
