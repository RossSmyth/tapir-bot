from discord.ext import commands


class Misc:
    """miscellaneous commands"""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def azwe(self, ctx):
        """Azwe's dancing animation"""
        await ctx.send('<@118907180761088006> '
                       'https://giphy.com/gifs/IEceC9q1MgWrK')
        
    @commands.command()
    async def bartti(self, ctx):
        """Hacked picture of Bartti"""
        await ctx.send('Bartti: http://i.imgur.com/kw5is3L.png')
        
    @commands.command()
    async def waffle(self, ctx):
        """Azwe's idea"""
        await ctx.send('Waffles are for tapirs')


def setup(bot):
    bot.add_cog(Misc(bot))