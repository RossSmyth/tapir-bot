from discord.ext import commands
from .utils import checks
import discord
import asyncio

class Misc:
    """miscellaneous commands"""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def azwe(self):
		"""Azwe's dancing animation"""
        self.bot.say('<@118907180761088006> https://giphy.com/gifs/IEceC9q1MgWrK')
        
def setup(bot):
    bot.add_cog(Misc(bot))