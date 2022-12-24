from discord.ext import commands
import discord
import json
import requests
from random import randint


async def _find(message, animal):
    response = requests.get('https://some-random-api.ml/img/' + animal)
    json_data = json.loads(response.text)
    print(json_data)
    embed = discord.Embed(color=0xff9900)
    embed.set_image(url=json_data['link'])
    embed.set_footer(text="requested by:" + message.author.name + '#' + message.author.discriminator)
    await message.channel.send(embed=embed)


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_comtext=True)
    async def cat(self, ctx):
        await ctx.message.delete()
        await _find(ctx.message, 'cat')

    @commands.command(pass_comtext=True)
    async def panda(self, ctx):
        if (randint(1, 3) == 1):
            await _find(ctx.message, 'red_panda')
        else:
            await _find(ctx.message, 'panda')

    @commands.command(pass_context=True)
    async def duck(self, message):
        await message.message.delete()
        response = requests.get('https://random-d.uk/api/random')
        json_data = json.loads(response.text)
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=json_data['url'])
        embed.set_footer(text="requested by:" + message.author.name + '#' + message.author.discriminator)
        await message.channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def slap(self, ctx):
        await ctx.send(f'拍了拍 {ctx.author.mention}')

    @commands.command(pass_context=True)
    async def eva(self, ctx, *args):
        """use '.eval' (or any customized command prefix) + math equation you would like to calculate"""
        arg_str = '_'.join(args)
        await ctx.send(eval(arg_str))

    @commands.command(pass_context=True)
    async def mc(self, ctx, *args):
        arg_str = '_'.join(args)
        await ctx.send("https://minecraft.gamepedia.com/" + arg_str)

    @commands.command()
    async def random(self, ctx, arg1=1, arg2=6):
        # num = random.randint(arg1, arg2) # randint not working?
        await ctx.send(114514)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello {ctx.author.display_name}.')

    @commands.command()
    async def image(self, ctx):
        embed = discord.Embed()
        embed.set_image(url="https://picsum.photos/536/354")
        await ctx.send(embed=embed)

    @commands.command()
    async def embed(self, ctx):
        embed = discord.Embed(title='Example Embed',
                              description='Showcasing the use of Embeds...\nSee the visualizer for more info.',
                              colour=0x98FB98)
        embed.set_author(name='MysterialPy',
                         url='https://gist.github.com/MysterialPy/public',
                         icon_url='http://i.imgur.com/ko5A30P.png')
        embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')

        embed.add_field(name='Embed Visualizer', value='[Click Here!](https://leovoel.github.io/embed-visualizer/)')
        embed.add_field(name='Command Invoker', value=ctx.author.mention)
        embed.set_footer(text='Made in Python with discord.py@rewrite', icon_url='http://i.imgur.com/5BFecvA.png')

        await ctx.send(content='**A simple Embed for discord.py@rewrite in cogs.**', embed=embed)


async def setup(client):
    await client.add_cog(Misc(client))
