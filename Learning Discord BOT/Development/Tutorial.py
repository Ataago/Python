import discord
from discord.ext import commands

class Tutorial:
    def __init__(self, GoBot):
        self.GoBot = GoBot

    async def on_message_delete(self, message):
        await self.GoBot.send_message(message.channel, 'Message Deleted Nana')

    @commands.command()
    async def allo(self):
        await self.GoBot.say('Allooo There!')

def setup(GoBot):
    GoBot.add_cog(Tutorial(GoBot))