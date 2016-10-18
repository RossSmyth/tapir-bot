from discord.ext import commands
from .utils import config, checks
from urllib.request import urlopen
import json
import discord
import asyncio

class XKCD:
    
    def __init__(self, bot):
        self.bot = bot
        
    async def formatter(self, data):
        """Formats the XKCD json data"""
        day = 'day'
        month = 'month'
        year = 'year'
        number = 'num'
        title = 'title'
        hidden = 'alt'
        image = 'img'
        
        template = '```Date: {} \nNumber: {} \nTitle: {} \nTooltip Text: {} \n```{}'
        
        day = data[day]
        month = data[month]
        year = data[year]
        number = data[number]
        title = data[title]
        hidden = data[hidden]
        image = data[image]
        
        date = '{}-{}-{}'.format(month, day, year)
        
        complete = template.format(date, number, title, hidden, image)
        
        return complete
        
    @commands.command()
    async def xkcd(self, number=None):
        """Get your favorite XKCD comics and their attributes!"""
        
        if number == None:
            with urlopen('http://xkcd.com/info.0.json') as comic:
                comic = comic.read().decode('utf8')
                comic = json.loads(comic)
                await self.bot.say(await self.formatter(comic))
        else:
            try:
                with urlopen('http://xkcd.com/{}/info.0.json'.format(number)) as comic:
                    comic = comic.read().decode('utf8')
                    comic = json.loads(comic)
                    await self.bot.say(await self.formatter(comic))
            except:
                await self.bot.say('Not a valid comic number')
                
def setup(bot):
    bot.add_cog(XKCD(bot))