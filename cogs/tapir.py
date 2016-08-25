from discord.ext import commands
from .utils import config, checks
import random
import discord
import asyncio

class Tapir:
    """the tapir command(s)"""
    
    def __init__(self, bot):
        self.bot = bot
		self.config = config.Config('tapirs.json', loop=bot.loop)
        
    @commands.command()
    async def tapir(self):
        """The wonderful tapir command that outputs a random tapir"""
        tapirs = self.config.get('tapirs', [])
        tapir = tapirs[random.randrange(len(tapirs))]
        await self.bot.say(tapir)

    @commands.command(hidden=True)
    @checks.is_owner()
    async def save_tapir(self, *, tapir):
        """allows the saving of a tapirs"""
        tapirs = self.config.get('tapirs', [])
        tapirs.append(tapir)
        tapir_file.put('tapirs', tapirs)
        self.bot.say('\N{OK HAND SIGN}')
        
def setup(bot):
    bot.add_cog(Tapir(bot))