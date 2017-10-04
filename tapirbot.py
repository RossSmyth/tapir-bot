import datetime
import logging
import sys
import traceback

import aiohttp
from discord.ext import commands
from cogs.utils.database import Database

import config

description = """
I am a bot written by treefroog to provide tapirs!
"""

initial_extensions = [
    'cogs.admin',
    'cogs.meta',
    'cogs.mod',
    'cogs.tapir',
    'cogs.ships',
    'cogs.star_citizen',
    'cogs.xkcd',
    'cogs.repl',
    'cogs.misc'
    ]

discord_logger = logging.getLogger(__name__)


class TapirBot(commands.Bot):
    def __init__(self, sql_file: str):
        super().__init__(command_prefix=['!'],
                         description=description,
                         pm_help=None,
                         help_attrs=dict(hidden=True, name='halp'))

        self.client_id = config.client_id
        self.session = aiohttp.ClientSession(loop=self.loop)

        self.db = Database(sql_file)

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()

    async def on_command_error(self, ctx, error):
        """Some miscellaneous command handlers"""
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send('This command cannot be used in private '
                                  'messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.author.send(
                'Sorry. This command is disabled and cannot be used.')
        elif isinstance(error, commands.CommandInvokeError):
            print(f'In {ctx.command.qualified_name}:', file=sys.stderr)
            traceback.print_tb(error.original.__traceback__)
            print(f'{error.original.__class__.__name__}: {error.original}',
                  file=sys.stderr)

    async def on_ready(self):
        """Makes sure there is an uptime attribute"""
        if not hasattr(self, 'uptime'):
            self.uptime = datetime.datetime.utcnow()

        print(f'Ready: {self.user} (ID: {self.user.id}')

    async def on_message(self, message):
        """Some message checking stuff"""

        # Lowers the command for insensitive case
        content_list = message.content.split(" ")
        content_list[0] = content_list[0].lower()
        message.content = " ".join(content_list)

        if message.author.bot:
            return

        await self.process_commands(message)

    async def close(self):
        """Closes all connections cleanly"""
        await super().close()
        await self.session.close()
        await self.db.close()

    def run(self):
        """Passes the secret token to the run method"""
        super().run(config.token, reconnect=True)
