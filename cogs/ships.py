from discord.ext import commands
from .utils import checks
import discord
import asyncio

class Ships:
    """all of the Star Citizen ship commands"""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.group(pass_context=True)
    async def ship(self, ctx):
        """Posts a link to an album of the specified ship"""
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid ship: {0.subcommand_passed}'.format(ctx))
        
    @ship.command(pass_context=True, hidden=True)
    async def carrack(self):
        await self.bot.say('Carrack pls http://i.imgur.com/BA3F1OI.png')