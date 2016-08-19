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
		
	@ship.command(pass_context=True)
	async def avenger(self):
		"""The Avenger law enforcement ship"""
		await self.bot.say('Here ya go: http://imgur.com/a/ipNE1')

	@ship.command(pass_context=True)
	async def endeavor(self):
		"""The Endeavor science vessel"""
		await self.boy.say('Here ya go: http://imgur.com/a/iYzOu')
		
	@ship.command(pass_context=True)
	async def blade(self):
		"""The Vanduul Blade fighter"""
		await self.boy.say('Here ya go: http://imgur.com/a/UviA5')
		
	@ship.command(pass_context=True)
	async def gladius(self):
		"""The Gladius light fighter"""
		await self.boy.say('Here ya go: http://imgur.com/a/Xinmf')
		
	@ship.command(pass_context=True)
	async def herald(self):
		"""The Herald info runner"""
		await self.boy.say('Here ya go: http://imgur.com/a/iqtmw')
		
	@ship.command(pass_context=True)
	async def redeemer(self):
		"""The Redeemer dropship"""
		await self.boy.say('Here ya go: http://imgur.com/a/kzzni')
		
	@ship.command(pass_context=True)
	async def sabre(self):
		"""The Stealthy Sabre fighter"""
		await self.boy.say('Here ya go: http://imgur.com/a/jEiYX')
		
	@ship.command(pass_context=True)
	async def 85X(self):
		"""The 890's snub, the 85X"""
		await self.boy.say('Here ya go: http://imgur.com/a/cOzff')

def setup(bot):
	bot.add_cog(Ships(bot))