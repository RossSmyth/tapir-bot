from discord.ext import commands
from .utils import checks, formats
import discord
from collections import OrderedDict, deque, Counter
import datetime
import re, asyncio
import copy


            
class Meta:
    """Commands for utilities related to Discord or the Bot itself."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self):
        """Displays my hello message."""
        await self.bot.say('Hello! I\'m a bot made by <@149281074437029890>')
        
    @commands.command()
    async def source(self):
        """displays link to github"""
        await self.bot.say('Github: https://github.com/treefroog/tapir-bot')
        
    @commands.command(hidden=True, aliases=['say'])
    @checks.is_owner()
    async def echo(self, *, content):
        """says stuff that I tell it to"""
        await self.bot.say(content)
        
    @commands.command(name='quit', hidden=True, aliases=['close'])
    @checks.is_owner()
    async def _quit(self):
        """quits tapir-bot"""
        await self.bot.logout()
    	
    @commands.command(aliases=['rip'], hidden=True)
    @checks.is_owner()
    async def kill(self):
        """Kills tapir-bot violently"""
        await self.bot.say("See you in hell <@149281074437029890> :middle_finger:")
        await asyncio.sleep(3)
        await self.bot.logout()

    async def say_permissions(self, member, channel):
        permissions = channel.permissions_for(member)
        entries = [(attr.replace('_', ' ').title(), val) for attr, val in permissions]
        await formats.entry_to_code(self.bot, entries)

    @commands.command(pass_context=True, no_pm=True)
    async def permissions(self, ctx, *, member : discord.Member = None):
        """Shows a member's permissions.
        You cannot use this in private messages. If no member is given then
        the info returned will be yours.
        """
        channel = ctx.message.channel
        if member is None:
            member = ctx.message.author

        await self.say_permissions(member, channel)

    @commands.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_roles=True)
    async def botpermissions(self, ctx):
        """Shows the bot's permissions.
        This is a good way of checking if the bot has the permissions needed
        to execute the commands it wants to execute.
        To execute this command you must have Manage Roles permissions or
        have the Bot Admin role. You cannot use this in private messages.
        """
        channel = ctx.message.channel
        member = ctx.message.server.me
        await self.say_permissions(member, channel)

    @commands.command(hidden=True)
    @checks.is_owner()
    async def commandstats(self):
        """gives me command stats"""
        msg = 'Since startup, {} commands have been used.\n{}'
        counter = self.bot.commands_used
        await self.bot.say(msg.format(sum(counter.values()), counter))


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
    async def uptime(self):
        """Tells you how long the bot has been up for."""
        await self.bot.say('Uptime: **{}**'.format(self.get_bot_uptime()))
    
    @commands.command()
    async def oauth(self):
        """Gives a link to invite to a server
        
        Gives it all permissions as well if you don't uncheck them"""
        oauth_url = discord.utils.oauth_url(self.bot.client_id, discord.Permissions.all())
        await self.bot.say(oauth_url, delete_after = 120)

def setup(bot):
    bot.add_cog(Meta(bot))