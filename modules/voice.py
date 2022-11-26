import asyncio
import settings
import random
import requests
from gtts import gTTS
import discord
from discord.ext import commands
import io
import base64


# import audio_api


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def lai(self, ctx):
        channel = ctx.author.voice.channel
        print('Bot joined the channel.')
        await channel.connect()

    @commands.command(pass_context=True)
    async def bjl(self, ctx):
        await ctx.voice_client.disconnect()

    # @commands.command(pass_context=True)
    # async def tts(self, ctx, arg):
    #     channel = ctx.author.voice.channel
    #     await channel.send(arg, tts=True)

    @commands.command(pass_context=True)
    async def jiao(self, ctx, *args):
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            await ctx.send('User is not in accessible voice channel!')

        # play audio via GTTS of the user's message
        # tts = gTTS(" ".join(args), 'com.au')
        # tts.save('tts.mp3')
        # audio_source = await discord.FFmpegOpusAudio.from_probe('tts.mp3')
        # discord.voice_client.play(audio_source)
        # raw = audio_api.on_message(raw_class)
        f = open('b64.txt', 'r')
        raw = f.read()

        f.close()
        file = discord.File(io.BytesIO(base64.b64decode(raw)))
        await ctx.send(file=file)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def play(self, ctx, *, url):
        return

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        self.voices[ctx.guild.id].songs = asyncio.Queue()
        self.voices[ctx.guild.id].now_playing = ""
        self.voices[ctx.guild.id].queue = []
        await ctx.voice_client.disconnect()

    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def pause(self, ctx):
        if ctx.voice_client.is_paused():
            await ctx.send('I have already paused the audio.')
        else:
            ctx.voice_client.pause()
            await ctx.send('I have paused the audio.')

    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def resume(self, ctx):
        if ctx.voice_client.is_playing():
            await ctx.send('I am already playing audio. Is your head alright?')
        else:
            ctx.voice_client.resume()
            await ctx.send('I have resumed the audio.')

    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def queue(self, ctx):
        embed = discord.Embed(Title='Music Queue for ' + ctx.guild.name + ' in ' + ctx.channel.name,
                              description="Music Queue for " + ctx.guild.name + ' through #' + ctx.channel.name)
        embed.add_field(name="**[Now Playing]**", value="" + self.voices[ctx.guild.id].now_playing)
        titles = []
        if len(self.voices[ctx.guild.id].queue) > 10:
            titles = self.voices[ctx.guild.id].queue[:10]
        else:
            titles = self.voices[ctx.guild.id].queue

        i = 1

        for title in titles:
            embed.add_field(name="[" + str(i) + "]", value=title)
            i += 1

        await ctx.send(embed=embed)

    @play.before_invoke
    @pause.before_invoke
    @resume.before_invoke
    @stop.before_invoke
    @queue.before_invoke
    async def not_in_voice(self, ctx):
        if ctx.voice_client is None:
            await ctx.send(
                "I am not connected to a voice channel. Use -connect when in a voice channel to instruct me to join.")


async def setup(client):
    await client.add_cog(Voice(client))
