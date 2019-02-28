# Discord BOT by Ataago

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='GO ')


class bot:


@bot.event
async def on_ready():
    await bot.change_presence(game = discord.Game(name = 'Nothing'))
    print ("\n\nGO GO GO GO!!!! Bot is online.\n")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("ALLOOoOoooOOooo!!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def hello(ctx, user: discord.Member):
    await bot.say("Allo there! @{}".format(user.name))
#@bot.event
#async def on_message(message):
#    if message.content.upper().startswith('HELLO'):
#        userID = message.author.id
#        await bot.send_message(message.channel, "Allo there! <@%s> " % (userID))
    
    

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("User name: {}".format(user.name))
    await bot.say("User ID: {}".format(user.id))
    await bot.say("User Status: {}".format(user.status))
    await bot.say("Users highest role: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say("SOTED {} ".format(user.name))
    await bot.kick(user)

bot.run("NDg2NzQ5Nzg5NjQ4NTg0NzA1.DnDp1Q.lOYPmoWlH3RqlYU4wOeE-h9BpLc")