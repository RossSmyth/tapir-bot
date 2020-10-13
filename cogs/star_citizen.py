from discord.ext import commands
from .utils import checks
import discord
import asyncio

class Star_Citizen(commands.Cog):
    """All of the Star Citizen related commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ben(self, ctx):
        """Dancing Ben"""
        await ctx.send('http://i.imgur.com/OLKOQ6H.gif')

    @commands.command()
    async def scam(self, ctx):
        """Shows that Star Citizen is a scam"""
        await ctx.send('Star Citizen is a scam, confirmed by Chris Roberts himself: http://i.imgur.com/UK3D1c0.gifv')

    @commands.command(name='2.4')
    async def two_four(self, ctx):
        """Shows the progress of 2.4"""
        await ctx.send('It\'s not just a meme! http://i.imgur.com/umBUjqW.gif')

def setup(bot):
    bot.add_cog(Star_Citizen(bot))
