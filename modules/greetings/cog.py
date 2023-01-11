from discord.ext import commands
import discord

class Greetings(commands.Cog, name="Greetings Cof"):
    """Say hello for new members"""

    def __init__(self, bot):
        print('Greetings commands initiated')
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.')

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Say hello for members
        Usage: ?hello
        """

        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member


async def setup(bot:commands.Bot):
    await bot.add_cog(Greetings(bot))
