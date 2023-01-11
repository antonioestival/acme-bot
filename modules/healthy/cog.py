from discord.ext import commands
import discord

class Healthy(commands.Cog, name="Bot Healthy Commands Group"):
    """Checking status off bot with ping request"""
    
    def __init__(self, bot:commands.Bot):
        print('Ping command initiated')
        self.bot = bot

    @commands.command()
    async def ping(self, ctx:commands.Context):
        """ Answer for ping request with pong """

        await ctx.send("pong")


    @commands.command()
    async def hc(self, ctx:commands.Context):
        """ Health Check (hc) answer with overall bot status dependencies """

        await ctx.send("Not implemented yet!")


async def setup(bot:commands.Bot):
    await bot.add_cog(Healthy(bot))