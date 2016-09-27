from discord.ext import commands
from .utils import checks
import discord
import asyncio
from bs4 import BeautifulSoup
import urllib.request
import datetime

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

    @commands.command()
    async def countdown(self):
        """Countdown to Citizencon \N{SMILE}"""
        utc_now = datetime.datetime.utcnow()
        citizencon_utc = datetime.datetime.utcfromtimestamp(1476050400)
        time_delta = citizencon_utc - utc_now
        hours = time_delta.seconds // 3600
        minutes = (time_delta.seconds % 3600) // 60
        seconds = time_delta.seconds % 60
        citizencon_countdown = 'Citizencon is in:\n`{} Days, {} Hours, {} Minutes, {} Seconds`'
        citizencon_countdown = citizencon_countdown.format(time_delta.days, hours, minutes, seconds)
        await self.bot.say(citizencon_countdown)
        
def setup(bot):
    bot.add_cog(Star_Citizen(bot))