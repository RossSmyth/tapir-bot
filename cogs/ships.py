from discord.ext import commands
from .utils import config, checks
import discord
import asyncio

class Ships(commands.Cog):
    """all of the Star Citizen ship commands"""

    def __init__(self, bot):
        self.bot = bot
        self.config = config.Config('ships.json', loop=bot.loop)

    @commands.command()
    async def ship(self, ctx, *, ship_name):
        """Say ship and a ship's name to see an album of that ship!"""
        ship_name = ship_name.lower()
        try:
            ship_album = self.config.get(ship_name, "")
            await ctx.send(ship_album)
        except:
            pass
def setup(bot):
    bot.add_cog(Ships(bot))
