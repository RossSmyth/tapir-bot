from discord.ext import commands


class StarCitizen:
    """Most of the Star Citizen related commands"""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ben(self, ctx):
        """Dancing Ben"""
        await ctx.send('http://i.imgur.com/OLKOQ6H.gifv')
        
    @commands.command()
    async def scam(self, ctx):
        """Shows that Star Citizen is a scam"""
        await ctx.send('Star Citizen is a scam, confirmed by Chris Roberts '
                       'himself: http://i.imgur.com/UK3D1c0.gifv')
    
    @commands.command(name='3.0')
    async def three_point_o(self, ctx):
        """Shows the progress of 2.4"""
        await ctx.send('**__NEVER__** https://i.imgur.com/d5zY5tJ.jpg')


def setup(bot):
    bot.add_cog(StarCitizen(bot))
