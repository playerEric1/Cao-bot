import asyncio
import discord
from discord.ext import commands
import youtube_dl
import io
from scipy.io import wavfile
import base64
import numpy as np

import settings

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.players = {}

    @commands.command(pass_context=True)
    async def lai(self, ctx):
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            await ctx.send('User is not in a voice channel!')
        await channel.connect()

    @commands.command(pass_context=True)
    async def bjl(self, ctx):
        """Stops and disconnects the bot from voice"""
        await ctx.voice_client.disconnect()

    @commands.command(pass_context=True)
    async def tts(self, ctx, arg):
        channel = ctx.author.voice.channel
        await channel.send(arg, tts=True)

    @commands.command(pass_context=True)
    async def jiao(self, ctx, *args):
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            await ctx.send('User is not in accessible voice channel!')

        # Handle the exceptions that can occur
        except discord.ClientException as e:
            await ctx.send(f"A client exception occurred:\n`{e}`")

        except discord.TypeError as e:
            await ctx.send(f"TypeError exception:\n`{e}`")

        except discord.OpusNotLoaded as e:
            await ctx.send(f"OpusNotLoaded exception: \n`{e}`")

    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {query}')

    @commands.command()
    async def j(self, ctx):
        """Plays a file from the local filesystem"""
        # source = discord.FFmpegPCMAudio(source=io.BufferedIOBase(b'RIFF$\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x00\x04\x00\x00'
        #                b'\x00\x04\x00\x00\x01\x00\x08\x00data\x00\x00\x00\x00'), format="wav").read()
        bio = io.BytesIO(b'RIFF$\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x00\x04\x00\x00'
                         b'\x00\x04\x00\x00\x01\x00\x08\x00data\x00\x00\x00\x00')
        samplerate = 44100
        fs = 100
        # t = np.linspace(0., 1., samplerate)
        # amplitude = np.iinfo(np.int16).max
        # data = amplitude * np.sin(2. * np.pi * fs * t)
        data = np.frombuffer(b'\x10\x00\x00\x00\x01\x00\x01\x00\x00\x04\x00\x00\x00\x04\x00\x00\x01\x00\x08\x00',
                             dtype=np.int16, count=10)
        print(data)
        wavfile.write('t.wav', samplerate, data)
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('t.wav'))
        ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

    @commands.command()
    async def yt(self, ctx, *, url):
        """Plays from an url (almost anything youtube_dl supports)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url)
            print(1)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
            print(2)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def stream(self, ctx, *, url):
        """Streams from an url (same as yt, but doesn't predownload)"""

        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            print(1)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send(f"Changed volume to {volume}%")

    @play.before_invoke
    @yt.before_invoke
    @stream.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


async def setup(client):
    await client.add_cog(Voice(client))
