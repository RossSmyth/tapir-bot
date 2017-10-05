import datetime

import aiohttp

import discord
from discord.ext import commands


class XKCD:
    
    def __init__(self, bot):
        self.bot = bot
        
    def formatter(self, data: dict):
        """Formats the XKCD json data into an embed"""

        # Getting the data from the JSON
        day = data['day']
        month = data['month']
        year = data['year']
        number = data['num']
        title = data['title']
        alt = data['alt']
        image = data['img']

        # Formatting the data
        embed_date = datetime.date(year=int(year),
                                   month=int(month),
                                   day=int(day)).strftime("%a %b %dth, %Y")

        embed_description = f'xkcd #{number}'
        embed_title = f'{title}'
        embed_colour = 0x96a8c8
        embed_url = f'https://xkcd.com/{number}/'

        # instances the embed object
        complete = discord.Embed(title=embed_title, url=embed_url,
                                 description=embed_description,
                                 colour=embed_colour)

        # sets some of the attributes
        complete.set_thumbnail(url='https://xkcd.com/s/0b7742.png')
        complete.set_image(url=image)
        complete.add_field(name='alt-text', value=alt)
        complete.set_footer(text=embed_date)

        return complete
        
    @commands.command()
    async def xkcd(self, ctx, number: int = None):
        """Get your favorite XKCD comics and their attributes!

        If there are not any arguments, it returns the most currecnt xkcd. If
        there are arguments, it will try and find that xkcd.
        """

        async with aiohttp.ClientSession() as session:

            if number is None:
                async with session.get('http://xkcd.com/info.0.json') as comic:
                    comic = await comic.json()
                    await ctx.send(embed=self.formatter(comic))

            else:
                try:
                    async with session.get(
                            f'http://xkcd.com/{number}/info.0.json') as comic:

                        comic = await comic.json()
                        await ctx.send(embed=self.formatter(comic))
                except:
                    await ctx.send('Not a valid comic number')


def setup(bot):
    bot.add_cog(XKCD(bot))
