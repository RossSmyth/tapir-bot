from discord.ext import commands
from .utils import config, checks
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import URLError
from datetime import datetime
from utils.credentials import load_credentials
import json
import discord
import asyncio

class Weather(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        credentials = load_credentials()
        self.synoptic_token = credentials["synoptic"]

    async def _formatter(self, current_data, forecast_data):
        """Puts data into embed"""

        # This chucks all the forecast data from the json data received to a dictionary that can be unpacked as kwargs
        forecast = [
                        {
                            "name"   : forecast_data[i]["name"],
                            "value"  : forecast_data[i]["detailedForecast"],
                            "inline" : True
                        }
                        for i in range(0, 3)
                    ]

        # grabs each item, puts it into string, and rounds towards 0. Also converts to metric
        air_temp = current_data["air_temp_value_1"]["value"]
        air_temp = "{} F ({} C)".format(int(air_temp), int((air_temp - 32) * 5 / 9))

        try:
            wind_chill = current_data["wind_chill_value_1d"]["value"]
        except KeyError:
            wind_chill = "not cold"
        else:
            wind_chill = "{} F ({} C)".format(int(wind_chill), int((wind_chill - 32) * 5 / 9))

        wind_speed = current_data["wind_speed_value_1"]["value"]
        wind_speed = "{} mph ({} km/h)".format(int(wind_speed), int(wind_speed * 1.609))

        wind_gust = current_data["wind_gust_value_1"]["value"]
        wind_gust = "{} mph ({} km/h)".format(int(wind_gust), int(wind_gust * 1.609))

        conditions = current_data["weather_condition_value_1d"]["value"]

        visibility = current_data["visibility_value_1"]["value"]
        visibility = "{:.2g} mi ({:.2g} km)".format(visibility, visibility * 1.609)

        obsevation_time = current_data["air_temp_value_1"]["date_time"]
        obsevation_time = datetime.strptime(obsevation_time, "%Y-%m-%dT%H:%M:%S%z")

        embed = discord.Embed(title="Houghton, MI Weather",
                              colour=discord.Colour(0xffcd00),
                              url="https://mesowest.utah.edu/cgi-bin/droman/meso_base_dyn.cgi?stn=KCMX&unit=0&timetype=LOCAL",
                              timestamp=obsevation_time)

        embed.set_thumbnail(url=forecast_data[0]["icon"].replace("medium", "large"))

        embed.set_author(name="National Weather Service",
                         url="https://forecast.weather.gov/MapClick.php?lat=47.11797510000008&lon=-88.56920929999995",
                         icon_url="https://pbs.twimg.com/profile_images/842835019613831170/vvWHIDxE_400x400.jpg")

        embed.add_field(name="Current Air Temperature", value=air_temp,    inline=True)
        embed.add_field(name="Current Wind Chill",      value=wind_chill,  inline=True)
        embed.add_field(name="Current Wind Speed",      value=wind_speed,  inline=True)
        embed.add_field(name="Current Peak Wind Speed", value=wind_gust,   inline=True)
        embed.add_field(name="Current Conditions",      value=conditions, inline=True)
        embed.add_field(name="Current Visibility",      value=visibility, inline=True)

        for kwargs in forecast:
            embed.add_field(**kwargs)

        return embed

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.guild)
    async def weather(self, ctx):
        """Shows the weather of the 49931 area"""

        # mesowest http query parameters
        mesowest_parameters = urlencode( {
                                            "stids" : "KCMX",
                                            "output" : "json",
                                            "units" : "english,speed|mph",
                                            "obtimezone" : "local",
                                            "token" : self.synoptic_token
                                         } )

        with urlopen("https://api.synopticdata.com/v2/stations/latest?{}".format(mesowest_parameters)) as current_data:
            current_data = current_data.read().decode("utf-8")
            current_data = json.loads(current_data)
            current_data = current_data["STATION"][0]["OBSERVATIONS"]

        with urlopen("https://api.weather.gov/gridpoints/MQT/114,95/forecast") as forecast_data:
            forecast_data = forecast_data.read().decode("utf-8")
            forecast_data = json.loads(forecast_data)
            forecast_data = forecast_data["properties"]["periods"]

        embed = await self._formatter(current_data, forecast_data)
        await ctx.send(embed=embed)

    @weather.error
    async def weather_error(self, ctx, error):
        if isinstance(error, KeyError):
            return await ctx.send("Something on the API side is broken")
        elif isinstance(error, URLError):
            return await ctx.send("Something is broken, not sure what side")

def setup(bot):
    bot.add_cog(Weather(bot))
