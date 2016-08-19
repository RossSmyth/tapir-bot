from discord.ext import commands
from .utils import checks
import discord
import asyncio

class Ships:
	"""all of the Star Citizen ship commands"""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True)
	async def ship(self, ctx):
		"""Posts a link to an album of the specified ship (no where near done)"""
		if ctx.invoked_subcommand is None:
			await self.bot.say('Invalid ship: {0.subcommand_passed}'.format(ctx))

	@ship.command(pass_context=True)
	async def carrack(self):
		"""The majestic Carrack"""
		await self.bot.say('Carrack pls http://i.imgur.com/BA3F1OI.png \n Rest of album: http://imgur.com/a/8cPzB')

	@ship.command(pass_context=True)
	async def dragonfly(self):
		"""The nimble Dragonfly"""
		await self.bot.say('Here ya go: http://imgur.com/a/msSaN')
	
	@ship.command(pass_context=True)
	async def javelin(self):
		"""The Javelin Destroyer Capital ship"""
		await self.bot.say('Here ya go: http://imgur.com/a/LWViV')
		
	@ship.command(pass_context=True)
	async def merlin(self):
		"""The Merlin snub"""
		await self.bot.say('Here ya go: http://imgur.com/a/5Tsrd')

def setup(bot):
	bot.add_cog(Ships(bot))