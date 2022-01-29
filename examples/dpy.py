"""
This example should work with Discord.py and most of it's forks, including Pycord. Check dpy-cogs.py to understand how to use YARSAW in Cogs.
"""

import discord
from discord.ext import commands
import yarsaw

bot = commands.Bot(command_prefix="!")

# create yarsaw client
client = yarsaw.Client("Random Stuff API Key", "RapidAPI Application Key")


@bot.command()
async def joke(ctx):
    joke = await client.get_safe_joke()
    await ctx.send(yarsaw.format_joke(joke))


bot.load_extension("dpy-cogs")  # load the cog from dpy-cogs.py

bot.run("TOKEN")
