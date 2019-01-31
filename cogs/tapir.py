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
    @commands.cooldown(1, 10, commands.BucketType.channel)
    async def tapir(self):
        """The wonderful tapir command that outputs a random tapir"""
        tapir_list = self.config.get('tapirs', [])
        tapir = tapir_list[random.randrange(len(tapir_list))]
        try:
            await self.bot.say(tapir)
        except:
            await self.bot.whisper(tapir)

    @commands.command(hidden=True)
    @checks.is_owner()
    async def save_tapir(self, *, tapir_link):
        """allows the saving of a tapirs"""
        tapir_list = self.config.get('tapirs', [])
        tapir_list.append(tapir_link)
        await self.config.put('tapirs', tapir_list)
        await self.bot.say('\N{OK HAND SIGN}')
        
def setup(bot):
    bot.add_cog(Tapir(bot))