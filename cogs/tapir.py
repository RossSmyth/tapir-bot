import random

import discord
from discord.ext import commands


class Tapir:
    """the famous tapir commands"""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def tapir(self, ctx):
        """The wonderful tapir command that outputs a random tapir
        This has a cool down of 5 seconds to prevent spam"""
        tapir_list = await self.bot.db.get_tapirs()
        tapir = random.choice(tapir_list)
        try:
            await ctx.send(tapir)
        except:
            await ctx.author.send(
                embed=discord.Embed(colour=12884062).set_image(url=tapir))

    @commands.command(hidden=True)
    @commands.is_owner()
    async def save_tapir(self, ctx, *, tapir_link: str):
        """allows the saving of a tapirs by owner only"""
        success = await self.bot.db.add_tapir(tapir=tapir_link)

        if success:
            await ctx.send('\N{OK HAND SIGN}')
        else:
            await ctx.send('\N{PISTOL}')


def setup(bot):
    bot.add_cog(Tapir(bot))
