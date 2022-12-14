import openai
import dotenv
import os
import requests
from discord.ext import commands

dotenv.load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


class OpenAI(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, " \
                      "clever, and very friendly. When generating code blocks, attach ``` and the name of the " \
                      "language at the beginning and ``` at the end of the code block "
        self.temper = 0.4
        self.m_token = 1000
        self.frequency_penalty = 0

    @commands.command(pass_context=True)
    async def a(self, ctx, *args):
        self.prompt += "\nHuman: " + ' '.join(args).replace('\"', ' ')
        print(self.prompt)
        try:
            completion = openai.Completion.create(
                model="text-davinci-003",
                prompt=self.prompt,
                temperature=self.temper,
                max_tokens=self.m_token,
                top_p=1,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=0
            )
        except requests.HTTPError:
            print("""Either the API is down or your values are too high."\nTry keeping max tokens, temperature, 
                and top_p to a reasonable value\nAlso don't add too many examples add enough but not an huge amount""")

        # print the completion
        print(completion)

        await ctx.send(
            completion["choices"][0]["text"].replace('AI Assistant: ', '').replace('AI ', '')
            .replace('Human ', '').replace('?\n\n', ''))

    # Reset the prompts
    @commands.command(pass_context=True)
    async def r(self, ctx):
        self.prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, " \
                      "clever, and very friendly."
        await ctx.send("Reset")

    @commands.command(pass_context=True)
    async def temper(self, ctx, arg):
        if int(arg) > 1 or int(arg) < 0:
            await ctx.send("?????????0???1???????????????")
        else:
            self.temper = int(arg)
            await ctx.send(f"??????????????????{self.temper}")

    @commands.command(pass_context=True)
    async def info(self, ctx):
        await ctx.send(self.prompt)
        await ctx.send(f"temperature: {self.temper}")
        await ctx.send(f"max_token: {self.m_token}")
        await ctx.send(f"frequency_penalty: {self.frequency_penalty}")

    @commands.command(pass_context=True)
    async def story(self, ctx):
        self.prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, " \
                      "clever, and very friendly.  "
        await ctx.send("???????????????+???+??????,???????????????!")


async def setup(client):
    await client.add_cog(OpenAI(client))
