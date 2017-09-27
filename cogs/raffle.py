from discord.ext import commands
from .utils import config, checks
import discord
import asyncio
import random

class Raffle:

    def __init__(self, bot):
        self.bot = bot
        self.config = config.Config('raffle.json', loop=bot.loop)
    
    @commands.group(pass_context=True, no_pm=True)
    @checks.is_in_servers('120318148095246336')
    async def raffle(self, ctx):
        """Can create raffles within a specific channel"""
        
        if ctx.invoked_subcommand is None:
            return
            
    @raffle.command(pass_context=True)
    async def start(self, ctx):
        """Starts a raffle in a channel"""
        raffles = self.config.get('raffles', {})
        
        if ctx.message.channel.id in raffles:
            await self.bot.say('Yo dawg, there is already a raffle in this channel')
        else:
            raffles[ctx.message.channel.id] = [ctx.message.author.id, []]
            await self.config.put('raffles', raffles)
            await self.bot.say('Raffle you nerds!')
            
    @raffle.enter(pass_context=True)
    async def enter(self, ctx):
        """Enters a raffle in the channel"""
        raffles = self.config.get('raffles', {})
        
        if ctx.message.channel.id in raffles:
            raffle = raffles[ctx.message.channel.id][1]
            if ctx.author.id in raffle:
                await self.bot.say('<@{}> You are already entered dummy'.format(ctx.message.author.id))
            else:
                raffle.append(ctx.message.author.id)
                raffles[ctx.message.channel.id][1] = raffle
                await self.config.put('raffles', raffles)
                await self.bot.say("<@{}> You're entered!".format(ctx.message.author.id))
                return
        else:
            return
    
    @raffle.draw(pass_context=True)
    async def draw(self, ctx):
        """Draws a raffle in a channel"""
        raffles = self.config.get('raffles', {})
        
        if ctx.message.channel.id in raffles:
            raffle = raffles[ctx.message.channel.id]
            if ctx.author.id == raffle[0]:
                winner = raffle[1][random.randrange(len(raffle))]
                await self.bot.say('Congratulations <@{}>, You won!'.format(winner))
                raffles.pop(ctx.message.channel.id)
                await self.config.put('raffles', raffles)
            else:
                return
        else:
            return
    
    @raffle.count(name='count', pass_context=True)
    async def _count(self, ctx):
        """Counts the people in a channel's raffle"""
        raffles = self.config.get('raffles', {})
        
        if ctx.message.channel.id in raffles:
            raffle = raffles[ctx.message.channel.id][1]
            await self.bot.say('{} people are entered'.format(len(raffle)))
        else:
            return
            
def setup(bot):
    bot.add_cog(Raffle(bot))
