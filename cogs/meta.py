import asyncio

import discord
from discord.ext import commands

from .utils import checks


class Meta:
    """Commands for utilities related to Discord or the Bot itself."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Displays my the hello message."""
        await ctx.send('Hello! I\'m a bot made by <@149281074437029890>')

    @commands.command()
    async def source(self, ctx):
        """displays link to github"""
        await ctx.send('Github: https://github.com/treefroog/tapir-bot')

    @commands.command(hidden=True, aliases=['say'])
    @commands.is_owner()
    async def echo(self, ctx, *, content: str):
        """says stuff that I tell it to"""
        await ctx.send(content)

    @commands.command(name='quit', hidden=True, aliases=['close'])
    @commands.is_owner()
    async def _quit(self, ctx):
        """quits tapir-bot"""
        await self.bot.logout()

    @commands.command(aliases=['rip'], hidden=True)
    @commands.is_owner()
    async def kill(self, ctx):
        """Kills tapir-bot violently"""
        await ctx.send("See you in hell <@149281074437029890> :middle_finger:")
        await asyncio.sleep(3)
        await self.bot.logout()

    async def say_permissions(self, ctx, member, channel):
        permissions = channel.permissions_for(member)
        e = discord.Embed(colour=member.colour)
        allowed, denied = [], []
        for name, value in permissions:
            name = name.replace('_', ' ').replace('guild', 'server').title()
            if value:
                allowed.append(name)
            else:
                denied.append(name)

        e.add_field(name='Allowed', value='\n'.join(allowed))
        e.add_field(name='Denied', value='\n'.join(denied))
        await ctx.send(embed=e)

    @commands.command(pass_context=True, no_pm=True)
    @commands.guild_only()
    async def permissions(self, ctx, member: discord.Member = None,
                          channel: discord.TextChannel = None):
        """Shows a member's permissions in a specific channel.
        If no channel is given then it uses the current one.
        You cannot use this in private messages. If no member is given then
        the info returned will be yours.
        """
        channel = channel or ctx.channel
        if member is None:
            member = ctx.author

        await self.say_permissions(ctx, member, channel)

    @commands.command()
    @commands.guild_only()
    @checks.admin_or_permissions(manage_roles=True)
    async def botpermissions(self, ctx, *, channel: discord.TextChannel = None):
        """Shows the bot's permissions in a specific channel.
        If no channel is given then it uses the current one.
        This is a good way of checking if the bot has the permissions needed
        to execute the commands it wants to execute.
        To execute this command you must have Manage Roles permission.
        You cannot use this in private messages.
        """
        channel = channel or ctx.channel
        member = ctx.guild.me
        await self.say_permissions(ctx, member, channel)

    @commands.command()
    async def oauth(self, ctx):
        """Gives a link to invite to a server
        Gives it all permissions as well if you don't uncheck them"""
        oauth_url = discord.utils.oauth_url(self.bot.client_id,
                                            permissions=discord.Permissions.all())
        await ctx.send(oauth_url, delete_after=120)


def setup(bot):
    bot.add_cog(Meta(bot))
