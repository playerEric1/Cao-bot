from discord.ext import commands

import ai
import settings
from modules import message_handler


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        print(member.name + " has joined a voice channel")
        default_channel = self.client.get_channel(settings.DEFAULT_CHANNEL)  # channel id should be an int

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
                await default_channel.send("群主來啦")
            else:
                await default_channel.send("" + member.name + "來啦")
            channel = member.voice.channel
            if self.client.user is not member:
                await default_channel.send("我也來叫")
                await channel.connect()

        elif before.channel is not None and after.channel is None:
            if member.name == "_Ikuta":
                await default_channel.send("群主睡觉去啦")
            else:
                await default_channel.send("" + member.name + "睡觉去啦")
        print("voice_state_update sent")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        reply = ai.get_gpt3(message.content)
        # if reply is not None:  # do not send empty messages
        # await asyncio.sleep(len(reply) / 10 + 0.3) # add some delay before sending
        await message.channel.send(reply)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author == self.client.user:
            return

        msg = f'{message.author} 刚说了: {message.content}'
        await message.channel.send(msg)

    @commands.Cog.listener()
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


async def setup(client):
    await client.add_cog(Events(client))
