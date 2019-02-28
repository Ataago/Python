import discord
from discord.ext import commands

import asyncio
from itertools import cycle


TOKEN = 'NDg3NjMwNjU3MDI4MzU4MTQ1.DnQicw.vSnlKzYQFRcoZuP35ZnekFUQbqQ'

GoBot = commands.Bot(command_prefix = 'go ')
status = ['msg1', 'msg2', 'msg3']

async def change_status():
    await GoBot.wait_until_ready()
    msgs = cycle(status)

    while not GoBot.is_closed:
        current_status = next(msgs)
        await GoBot.change_presence(game=discord.Game(name = current_status))
        await asyncio.sleep(5)


@GoBot.event
async def on_ready():
   # await GoBot.change_presence(game = discord.Game(name = 'Under Development'))
    print('Ready to GO!')


#autoRole https://www.youtube.com/watch?v=75P878_aje4&index=6&list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9
#on joinning only
@GoBot.command
async def logout():
    await GoBot.logout()


GoBot.loop.create_task(change_status())
GoBot.run(TOKEN)