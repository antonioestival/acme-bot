import os, discord, asyncio
from discord.ext import commands
from infrastructure.config import Environments

async def main():
    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(command_prefix = Environments.DISCORD_PREFIX, intents = intents)

    @bot.event
    async def on_ready():
        print(f"We have logged in as {bot.user}")
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}"))
        print(discord.__version__)

    @bot.event
    async def on_error(error):
        print(f"Error: {error}")

    for _ in os.listdir("modules"):
        if os.path.exists( os.path.join("modules", _ , "cog.py") ):
            await bot.load_extension(f"modules.{_}.cog")
            

    await bot.start(Environments.DISCORD_TOKEN)


if __name__ == '__main__':
    asyncio.run(main())

