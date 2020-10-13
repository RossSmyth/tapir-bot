from discord.ext import commands
from .utils import checks, formats
import discord
from collections import OrderedDict, deque, Counter
import datetime
import re, asyncio
import copy



class Meta(commands.Cog):
    """Commands for utilities related to Discord or the Bot itself."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Displays my hello message."""
        await ctx.send('Hello! I\'m a bot made by <@149281074437029890>')

    @commands.command()
    async def source(self, ctx):
        """displays link to github"""
        await ctx.send('Github: https://github.com/treefroog/tapir-bot')

    @commands.command()
    async def invite(self, ctx):
        """Invite to tapir-bot's official server.
        Coulld be for suggestions or help. Whatever you want.
		"""
        await ctx.author.send('Here ya go: \ndiscord.gg/JzzSxb5')

    @commands.command(hidden=True, aliases=['say'])
    @commands.check(commands.is_owner())
    async def echo(self, ctx, *, content):
        """says stuff that I tell it to"""
        await ctx.send(content)

    @commands.command(name='quit', hidden=True, aliases=['close'])
    @commands.check(commands.is_owner())
    async def _quit(self, ctx):
        """quits tapir-bot"""
        await self.bot.logout()

    @commands.command(aliases=['rip'], hidden=True)
    @commands.check(commands.is_owner())
    async def kill(self, ctx):
        """Kills tapir-bot violently"""
        await ctx.send("See you in hell <@149281074437029890> :middle_finger:")
        await asyncio.sleep(3)
        await self.bot.logout()

    async def say_permissions(self, ctx, member, channel):
        permissions = channel.permissions_for(member)
        entries = [(attr.replace('_', ' ').title(), val) for attr, val in permissions]
        await ctx.send(formats.entry_to_code(entries))

    @commands.command(no_pm=True)
    async def permissions(self, ctx, *, member : discord.Member = None):
        """Shows a member's permissions.
        You cannot use this in private messages. If no member is given then
        the info returned will be yours.
        """
        channel = ctx.message.channel
        if member is None:
            member = ctx.message.author

        await self.say_permissions(ctx, member, channel)

    @commands.command(no_pm=True)
    @checks.admin_or_permissions(manage_roles=True)
    async def botpermissions(self, ctx):
        """Shows the bot's permissions.
        This is a good way of checking if the bot has the permissions needed
        to execute the commands it wants to execute.
        To execute this command you must have Manage Roles permissions or
        have the Bot Admin role. You cannot use this in private messages.
        """
        channel = ctx.message.channel
        member = ctx.message.guild.me
        await self.say_permissions(ctx, member, channel)

    @commands.command(hidden=True)
    @commands.check(commands.is_owner())
    async def commandstats(self, ctx):
        """gives me command stats"""
        msg = 'Since startup, {} commands have been used.\n{}'
        counter = self.bot.commands_used
        await ctx.send(msg.format(sum(counter.values()), counter))


    def get_bot_uptime(self):
        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days:
            fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h} hours, {m} minutes, and {s} seconds'

        return fmt.format(d=days, h=hours, m=minutes, s=seconds)

    @commands.command()
    async def uptime(self, ctx):
        """Tells you how long the bot has been up for."""
        await ctx.send('Uptime: **{}**'.format(self.get_bot_uptime()))

    @commands.command()
    async def oauth(self, ctx):
        """Gives a link to invite to a server

        Gives it all permissions as well if you don't uncheck them"""
        oauth_url = discord.utils.oauth_url(self.bot.client_id, discord.Permissions.all())
        await ctx.send(oauth_url, delete_after = 120)

def setup(bot):
    bot.add_cog(Meta(bot))
