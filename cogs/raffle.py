from discord.ext import commands
from .utils import config, checks
import discord
import asyncio
import random

class Raffle(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = config.Config('raffle.json', loop=bot.loop)

    @commands.group(pass_context=True, no_pm=True)
    async def raffle(self, ctx):
        """Can create raffles within a specific channel"""

        if ctx.invoked_subcommand is None:
            raffles = self.config.get('raffles', {})

            if ctx.message.channel.id in raffles:
                await ctx.send('You probably meant to say ```!raffle enter``` instead')
        else:
            return

    @raffle.command(pass_context=True)
    async def start(self, ctx):
        """Starts a raffle in a channel"""
        raffles = self.config.get('raffles', {})

        if ctx.message.channel.id in raffles:
            await ctx.send('Yo dawg, there is already a raffle in this channel')
        else:
            raffles[ctx.message.channel.id] = [ctx.message.author.id, []]
            await self.config.put('raffles', raffles)
            await ctx.send('Raffle you nerds!')

    @raffle.command(pass_context=True)
    async def enter(self, ctx):
        """Enters a raffle in the channel"""
        raffles = self.config.get('raffles', {})

        if ctx.message.channel.id in raffles:
            raffle = raffles[ctx.message.channel.id][1]

            if ctx.message.author.id in raffle:
                await ctx.send('<@{}> You are already entered dummy'.format(ctx.message.author.id))
            else:
                raffle.append(ctx.message.author.id)
                raffles[ctx.message.channel.id][1] = raffle
                await self.config.put('raffles', raffles)
                await ctx.send("<@{}> You're entered!".format(ctx.message.author.id))
        else:
            return

    @raffle.command(pass_context=True)
    async def draw(self, ctx):
        """Draws a raffle in a channel"""
        raffles = self.config.get('raffles', {})

        if ctx.message.channel.id in raffles:
            raffle = raffles[ctx.message.channel.id]

            if ctx.message.author.id == raffle[0]:
                winner = raffle[1][random.randrange(len(raffle))]
                await ctx.send('Congratulations <@{}>, You won!'.format(winner))
                raffles.pop(ctx.message.channel.id)
                await self.config.put('raffles', raffles)
            else:
                return
        else:
            return

    @raffle.command(name='count', pass_context=True)
    async def _count(self, ctx):
        """Counts the people in a channel's raffle"""
        raffles = self.config.get('raffles', {})

        if ctx.message.channel.id in raffles:
            raffle = raffles[ctx.message.channel.id][1]
            await ctx.send('{} people are entered'.format(len(raffle)))
        else:
            return

def setup(bot):
    bot.add_cog(Raffle(bot))
