"""
This example should work with Discord.py and most of it's forks, including Pycord. This cog is loaded in dpy.py.
"""
import discord
from discord.ext import commands
from dpy import (
    client,
)  # import the client variable from dpy.py - the file, not the module


class Events(commands.Cog):  # subclass discord.ext.commands.Cog
    def __init__(self, bot):
        self.bot = bot
        self.client = client  # this is the client variable we imported from dpy.py

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in as")
        print(self.bot.user.name)
        print(self.bot.user.id)
        print("------")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if isinstance(
            message.channel, discord.channel.DMChannel
        ):  # if message is in DM
            res = await self.client.get_ai_response(
                message.content, bot_name="yarsaw", uid=message.author.id
            )  # generate different responses for different users
            await message.channel.send(res.response)  # send response


def setup(bot):
    bot.add_cog(Events(bot))
