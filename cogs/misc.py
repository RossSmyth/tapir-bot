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
		
	@commands.command()
	async def bartti(self):
		"""Description of Bartti"""
		self.bot.say('Bartti: http://i.imgur.com/kw5is3L.png')
        
def setup(bot):
    bot.add_cog(Misc(bot))