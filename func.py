from discord.ext import commands


def owner():
    async def predicate(ctx):
        return ctx.author.id == 765212693795307520

    return commands.check(predicate)
