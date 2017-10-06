from discord.ext import commands


class Ships:
    """all of the Star Citizen ship commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ship(self, ctx, *, ship_name):
        """Say a ship's name to see an album of that ship!
        pls no SQL inject thx
        """
        ship_name = ship_name.lower()
        try:
            ship_album = await self.bot.db.get_ship(ship_name)
            await ctx.send(ship_album)
        except:
            pass


def setup(bot):
    bot.add_cog(Ships(bot))
