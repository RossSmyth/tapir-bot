from discord.ext import commands
from .utils import config, checks
from urllib.request import urlopen
from datetime import datetime
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
        
        embed = discord.Embed(title="xkcd {}: {}".format(data['num'], data['title']), 
                              colour=discord.Colour(0x96a8c8), 
                              url="https://xkcd.com/{}/".format(data['num']), 
                              timestamp=datetime(int(data['year']), int(data['month']), int(data['day'])))

        embed.set_image(url="{}".format(data['img']))
        embed.set_thumbnail(url="https://xkcd.com/s/0b7742.png")
        embed.set_footer(text="{}".format(data['alt']))
        
        return embed
        
    @commands.command()
    async def xkcd(self, number=None):
        """Get your favorite XKCD comics and their attributes!"""
        
        if number == None:
            with urlopen('http://xkcd.com/info.0.json') as comic:
                comic = comic.read().decode('utf8')
                comic = json.loads(comic)
                await self.bot.say(embed=await self.formatter(comic))
        else:
            try:
                with urlopen('http://xkcd.com/{}/info.0.json'.format(number)) as comic:
                    comic = comic.read().decode('utf8')
                    comic = json.loads(comic)
                    await self.bot.say(embed=await self.formatter(comic))
            except:
                await self.bot.say('Not a valid comic number')
                
def setup(bot):
    bot.add_cog(XKCD(bot))