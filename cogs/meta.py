from discord.ext import commands
from .utils import checks, formats
import discord
from collections import OrderedDict, deque, Counter
import os, datetime
import re, asyncio
import copy


            
class Meta:
    """Commands for utilities related to Discord or the Bot itself."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(hidden=True)
    async def hello(self):
        """Displays my hello message."""
        await self.bot.say('Hello! I\'m a bot made by <@149281074437029890>')
        
    @commands.command(hidden=True)
    async def source(self):
        """displays link to github"""
        await self.bot.say('Github: https://github.com/treefroog/tapir-bot')
        
    @commands.command(rest_is_raw=True, hidden=True, aliases=['say'])
    @checks.is_owner()
    async def echo(self, *, content):
        """says stuff that I tell it to"""
        await self.bot.say(content)
        
    @commands.command(name='quit', hidden=True, aliases=['close'])
    @checks.is_owner()
    async def _quit(self):
        """quits tapir-bot"""
        await self.bot.logout()
        
    @commands.command(hidden=True)
    @checks.is_owner()
    async def commandstats(self):
        """gives me command stats"""
        msg = 'Since startup, {} commands have been used.\n{}'
        counter = self.bot.commands_used
        await self.bot.say(msg.format(sum(counter.values()), counter))
        
def setup(bot):
    bot.add_cog(Meta(bot))