from discord.ext import commands
from .utils import config, checks
import discord
import asyncio
import random

class Raffle:
    """Zephyr Raffle"""
    def __init__(self, bot):
        self.bot = bot
        self.config = config.Config('raffle.json', loop=bot.loop)
    
    @commands.command(pass_context=True, no_pm=True)
    async def raffle(self, ctx):
        raffle = self.config.get('raffle', [])
        person = ctx.message.author.id
        if person in raffle:
            await self.bot.say("<@{}> You're already entered!".format(person))
            return

        raffle.append(person)
        await self.config.put('raffle', raffle)
        await self.bot.say("<@{}> You're entered!".format(person))
    
    @commands.command(no_pm=True)
    @checks.is_user('118907180761088006')
    async def draw(self):
        raffle = self.config.get('raffle', [])
        winner = raffle.pop(random.randrange(len(raffle)))
        raffle = []
        await self.config.put('raffle', raffle)
        await self.bot.say("Congratulatons <@{}>! You've won!".format(winner))
        self.bot.unload_extension('cogs.raffle')
        
    @commands.command(no_pm=True)
    async def count(self):
        raffle = self.config.get('raffle', [])
        length = len(raffle)
        await self.bot.say('{} People are entered'.format(length))

        
def setup(bot):
    bot.add_cog(Raffle(bot))
