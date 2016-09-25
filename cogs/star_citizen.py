from discord.ext import commands
from .utils import checks
import discord
import asyncio
from bs4 import BeautifulSoup
import urllib.request

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
        url = 'http://www.timeanddate.com/countdown/launch?iso=20161009T00&p0=835&msg=Citizen+Con&ud=1&font=cursive&csz=1'
        with urllib.request.urlopen(url) as doc:
            soup = BeautifulSoup(doc, 'html.parser')
        digit_divs = soup.find_all(class_="csvg-digit-number")
        weeks = digit_divs[0].text
        days = int(digit_divs[1].text) - 7
        hours = digit_divs[2].text
        minutes = digit_divs[3].text
        seconds = digit_divs[4].text
        countdown = 'Citizencon is in:\n`{} Weeks, {} Days, {} Hours, {} Minutes, {} Seconds`'
        countdown = countdown.format(weeks, days, hours, minutes, seconds)
        await self.bot.say(countdown)
        
def setup(bot):
    bot.add_cog(Star_Citizen(bot))