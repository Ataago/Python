import discord
from discord.ext import commands
import asyncio
from itertools import cycle


import youtube_dl
import json
import os

extensions = ['Tutorial']


#TOKEN = input("Enter the TOKEN: ")
TOKEN ='NDg3NjMwNjU3MDI4MzU4MTQ1.DnYvcg.uePx3So8ltt7IBfF_pG2PLdun1o'

GoBot = commands.Bot(command_prefix = 'go ')
GoBot.remove_command('help')
status = ['Under Development', 'coming Soon!', 'type "go help"']
os.chdir(r'E:\Git\Python\Disocrd\Development')


async def change_status():
    await GoBot.wait_until_ready()
    msgs = cycle(status)

    while not GoBot.is_closed:
        current_status = next(msgs)
        await GoBot.change_presence(game=discord.Game(name = current_status))
        await asyncio.sleep(2)


@GoBot.event
async def on_ready():
    #await GoBot.change_presence(game = discord.Game(name = 'Under Development'))
    print('Ready to GO!')

@GoBot.event
async def on_member_join(member):
    with open('user.json','r') as f:
        users = json.load(f)

    await update_data(users,member)
    #code
    with open('user.json','w') as f:
        json.dump(users, f)


@GoBot.event
async def on_message(message):
    with open('user.json','r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_experience(users, message.author,5)
    await level_up(users,message.author,message.channel)

    #code
    with open('user.json','w') as f:
        json.dump(users, f)

    
    print('{} in {}-{}: {}'.format(message.author,message.channel,message.server, message.content))
    await GoBot.process_commands(message) #proccess the message as a command rather than an event.

async def update_data(users, user):
    if not user.name in users:
        users[user.name] = {}
        users[user.name]['experience'] = 0
        users[user.name]['level'] = 1

async def add_experience(users, user, exp):
    users[user.name]['experience'] += exp

async def level_up(users, user, channel):
    experience = users[user.name]['experience']
    lvl_start = users[user.name]['level']
    lvl_end = int(experience ** (1/4))
    
    if lvl_start < lvl_end:
        await GoBot.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[user.name]['level'] = lvl_end


#Simple command
@GoBot.command()
async def ping():
    await GoBot.say('Pong!')

#echo line.
@GoBot.command()
async def echo(*args):
    display = ''
    try:
        for word in args:
            display += word
            display += ' '
        await GoBot.say(display)
    
    except discord.errors.HTTPException:
        await GoBot.say('What to echo? For example- "go echo hi"') 

#Clear command https://www.youtube.com/watch?v=ZBVaH6nToyM&list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9&index=5
@GoBot.command(pass_context = True)
async def clear(ctx, amount = 2):
    channel = ctx.message.channel
    todelete = []
    try:
        async for message in GoBot.logs_from(channel, limit=int(amount)):
            todelete.append(message)
        await GoBot.delete_messages(todelete)

        await GoBot.say('Messages Deleted!')

    except Exception as e:
        await GoBot.say(e)
    #type conversion error is not beeing handled! go clear all
    except: 
        await GoBot.say('Please enter an integer')

#autoRole https://www.youtube.com/watch?v=75P878_aje4&index=6&list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9
#on joinning only

@GoBot.command
async def logout():
    await GoBot.logout()

#embed https://youtu.be/XKQWxAaRgG0?list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9
@GoBot.command()
async def about():
    embed = discord.Embed(
        title = 'GO BOT',
        description = 'Go is under Development. Stay tuned and give suggestions.',
        color = discord.Color.green()
    )

    #embed.set_image(url ='https://media.discordapp.net/attachments/487643988858372096/487963343676506132/unknown.png')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/487643988858372096/487968875242192898/GO2.png')
    embed.set_author(name='Ataago', icon_url ='https://cdn.discordapp.com/attachments/487643988858372096/487963343676506132/unknown.png')
    embed.add_field(name='How to use GO BOT?',value = 'Just type in "go help" to start using the BOT.',inline=False)
    #embed.add_field(name='Field Name',value = 'Field value',inline=True)
    #embed.add_field(name='Field Name',value = 'Field value',inline=True)
    embed.set_footer(text = 'DM me on Discord- Ataago#8094')

    await GoBot.say(embed=embed)

#reaction https://youtu.be/yISXyQea3uQ?list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9
@GoBot.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await GoBot.send_message(channel,'{} has added {} to the message: "{}"'.format(user.name, reaction.emoji, reaction.message.content))

@GoBot.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await GoBot.send_message(channel,'{} has removed {} to the message: "{}"'.format(user.name, reaction.emoji, reaction.message.content))
   
#Voice leave/ join https://youtu.be/hFVby_Vet7E?list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9
@GoBot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    try:
        await GoBot.join_voice_channel(channel)
    except:
        await GoBot.say('You must be in a Voice Channel.')


@GoBot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = GoBot.voice_client_in(server)
    try:
        await voice_client.disconnect()
    except:
        await GoBot.say('GO is not in any Voice Channel. Enter "go join".')


players = {}
queues = {}

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

#music https://youtu.be/MbhXIddT2YY?list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9
@GoBot.command(pass_context=True)
async def play(ctx,url):
    server = ctx.message.server
    voice_client = GoBot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()

#YT queue https://youtu.be/C9ZPFTzHg7g?list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9

@GoBot.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = GoBot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await GoBot.say('Queued: {}'.format(url))




#Help
@GoBot.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author #/channel/author

    embed = discord.Embed(
        title = 'HELP',
        description = 'Trigger a Command using "go "',
        colour = discord.Color.green()
    )

    #embed.set_author(name = 'Help')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/487643988858372096/487968875242192898/GO2.png')
    embed.add_field(name = 'go about', value = 'Know about the Developers',inline=True)
    embed.add_field(name = 'go ping', value = 'Returns Pong!', inline=True)
    embed.add_field(name = 'go echo <statement>', value = 'Echos the statment', inline=True)
    embed.add_field(name = 'go clear <integer>', value = 'Deletes previous messages', inline=True)
    embed.add_field(name = 'go join', value = 'Joins your Voice Channel', inline=True)
    embed.add_field(name = 'go leave', value = 'Leaves your Voice Channel', inline=True)
    
    

    await GoBot.send_message(author,embed=embed)
    await GoBot.say('I have sent you a Personal Message!')

@GoBot.command()
async def load(extension):
    try:
        GoBot.load_extension(extension)
        print('Loaded {}'.format(extension))

    except Exception as error:
        print(error)

@GoBot.command()
async def unload(extension):
    try:
        GoBot.unload_extension(extension)
        print('Loaded {}'.format(extension))
        
    except Exception as error:
        print(error)


if __name__ == '__main__':
    for extension in extensions:
        try:
            GoBot.load_extension(extension)
        except Exception as error:
            print(error)



    GoBot.loop.create_task(change_status())
    GoBot.run(TOKEN)