from discord.ext import commands
from .utils import checks
import discord
import asyncio

class Star_Citizen:
    """All of the Star Citizen related commands"""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ben(self):
        """Dancing Ben"""
        await self.bot.say('http://i.imgur.com/OLKOQ6H.gif')
        
    @commands.command()
    async def scam(self):
        """Shows that Star Citizen is a scam"""
        await self.bot.say('Star Citizen is a scam, confirmed by Chris Roberts himself: http://i.imgur.com/UK3D1c0.gifv')
    
    @commands.command(name='2.4')
    async def two_four(self):
        """Shows the progress of 2.4"""
        await self.bot.say('It\'s not just a meme! http://i.imgur.com/umBUjqW.gif')
        
def setup(bot):
    bot.add_cog(Star_Citizen(bot))