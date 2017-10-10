import random

from discord.ext import commands


class Raffle:
    """Creates per channel raffles"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(pass_context=True, no_pm=True)
    @commands.guild_only()
    async def raffle(self, ctx):
        """Can create raffles within a specific channel"""
        
        if ctx.invoked_subcommand is None:
            return
            
    @raffle.command(pass_context=True)
    @commands.guild_only()
    async def start(self, ctx):
        """Starts a raffle in a channel"""
        
        if await self.bot.db.create_raffle(ctx.channel.id):
            await ctx.send('Raffle you nerds!')
        else:
            await ctx.send('There is probably another raffle in this channel')
            
    @raffle.command(pass_context=True)
    @commands.guild_only()
    async def enter(self, ctx):
        """Enters a raffle in the channel"""
        raffle = await self.bot.db.get_raffle(ctx.channel.id)

        if ctx.author.id in raffle:
            await ctx.send(f'<@{ctx.author.id}> you are already entered!')
        else:
            await self.bot.db.add_to_raffle(ctx.channel.id, ctx.author.id)
            await ctx.send(f'<@{ctx.author.id} you are entered!')

    @raffle.command(pass_context=True)
    @commands.guild_only()
    async def draw(self, ctx):
        """Draws a raffle in a channel"""
        raffle = await self.bot.db.get_raffle(ctx.channel.id)

        await ctx.send(f'Congratulations <@{random.choice(raffle)}>,'
                       f' you have won!')
    
    @raffle.command(name='count', pass_context=True)
    @commands.guild_only()
    async def _count(self, ctx):
        """Counts the people in a channel's raffle"""
        raffle = self.bot.db.get_raffle(ctx.channel.id)

        await ctx.send(f'There are {len(raffle)} people entered')


def setup(bot):
    bot.add_cog(Raffle(bot))
