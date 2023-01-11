from discord.ext import commands
import discord

from modules.correios.gateways import CorreiosGateway

class Correios(commands.Cog, name="Correios Commands Group"):
    """Implementa consultas na base dos correios"""
    
    def __init__(self, bot:commands.Bot):
        print('Correios command initiated')
        self.bot = bot

    @commands.command()
    async def end(self, ctx:commands.Context, cep):
        """ Consulta o endereço de um determinado CEP """
        endereco = CorreiosGateway().endereco(cep=cep)
        if endereco:
            await ctx.send(f"{endereco}")
        else:
            await ctx.send(f"Endereço não encontrado para o cep {cep}")


async def setup(bot:commands.Bot):
    await bot.add_cog(Correios(bot))