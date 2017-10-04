from datetime import datetime
import sqlite3

import discord


class Database:
    """This is an attempt at a database object
    Abstracts most stuff away from me so that I don't have to type stuff every
    time
    """
    def __init__(self, file):
        self.db = sqlite3.connect(file)
        self.db.row_factory = lambda cursor, row: row[0]
        self.cursor = self.db.cursor()

        # A bunch of pre-defined statements
        self._create_table = "CREATE TABLE '{}' (ignores TEXT)"

        self._get_plonks = 'SELECT plonks FROM bot'
        self._add_plonk = 'INSERT INTO bot (plonks) VALUES (?)'

        self._get_tapirs = 'SELECT tapirs FROM bot'
        self._add_tapir = 'INSERT INTO bot (tapirs) VALUES (?)'

        self._get_ignores = "SELECT ignores FROM '{}'"
        self._add_ignore = "INSERT INTO '{}' (ignores) VALUES (?)"

        self._get_raffle = "SELECT ? FROM raffles"
        self._add_raffle = "INSERT INTO raffles (?) VALUES (?)"

    async def setup_table(self, ctx):
        """Sets up a table for a guild"""
        statement = self._create_table.format(ctx.guild.id)
        self.cursor.execute(statement)
        self.db.commit()
        return True

    async def query(self, statement, *args):
        """Just runs a SQL statement like normal"""
        try:
            results = self.cursor.execute(statement, args).fetchall()
            self.db.commit()
            return results
        except Exception as e:
            return e

    async def get_plonks(self):
        """Gets the plonks for the bot"""
        return self.cursor.execute(self._get_plonks).fetchall()

    async def add_plonk(self, user_id):
        """Adds a user to the plonk list"""
        self.cursor.execute(self._add_plonk, (user_id,))
        self.db.commit()
        return True

    async def get_tapirs(self):
        """Gets the tapirs the bot has"""
        return self.cursor.execute(self._get_tapirs).fetchall()

    async def add_tapir(self, tapir):
        """Adds a tapir to the database"""
        self.cursor.execute(self._add_tapir, (tapir,))
        self.db.commit()
        return True

    async def get_ignores(self, ctx):
        """Gets the ignores for a guild"""
        ignores = self._get_ignores.format(ctx.guild.id)
        return self.cursor.execute(ignores).fetchall()

    async def add_ignore(self, ctx, channel_id):
        """Adds a channel to the ignore list"""
        statement = self._add_ignore.format(ctx.guild.id)
        self.cursor.execute(statement, (channel_id,))
        self.db.commit()
        return True

    async def get_raffle(self, channel_id):
        """Grabs a whole raffle from a channel's row"""
        return self.cursor.execute(self._get_raffle, (channel_id,))

    async def add_to_raffle(self, channel_id, user_id):
        """Adds a user to a channel's raffle"""
        self.cursor.execute(self._add_raffle, (channel_id, user_id))
        self.db.commit()
        return True

    async def close(self):
        """Closes the database"""
        self.db.close()

    async def get_ignore_embed(self, ctx):
        """Gets the ignores for a guild. Returns a discord.Embed object
        After thinking about it, this will not exist eventually, but I am going
        to keep it for now so I can just copy the code later
        """
        ignores = self._get_ignores.format(ctx.guild.id)
        ignores = self.cursor.execute(ignores).fetchall()

        # Creates the embed object
        kwargs = {'title': 'Ignored Channels',
                  'colour': 0xC4985E,
                  'description': 'List of all ignored channels in the '
                                 'guild by <@218751061446492160>',
                  'timestamp': datetime.utcnow()}

        ignore_embed = discord.Embed(**kwargs)
        ignore_embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon)

        channels = [f'<#{channel}>'+'\n' for channel in ignores]
        channels = ''.join(channels)
        ignore_embed.add_field(name='Ignored Channels:', value=channels)

        return ignore_embed
