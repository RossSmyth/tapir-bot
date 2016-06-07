#https://discordapp.com/oauth2/authorize?&client_id=173642301921296385&scope=bot&permissions=0
#random tapir bot
#http://imgur.com/a/Nwp6c/
#http://imgur.com/a/QAr54

import random #imports the random module
import discord #imports the discord api module thing
import asyncio #imports asyncio
import tapir_module

client = discord.Client() #easier coding!

tapir = tapir_module.tapirbot() #initializes the tapir

@client.event
async def on_ready(): #same here, maybe when bot is ready it does the thing
    """the client starting up, once up, what it doess"""
    await client.change_status(game=discord.Game(name=tapir.current_game)) #puts a help command in the game played
    await tapir.startup(client)
    
@client.event
async def on_message(message): #when someone sends a message
    """the stuff that happens when a message is sent"""
    channel = message.channel #defines the channel the messages is sent to as a variable
    raw_message = message #the message content is ssaved
    message = message.content.lower() #the message is put into a lower case format
    if len(message) >= 1: #must have atleast one character in the message
        message = message.split(' ') #message is made into a list split at every ' '
        if message[0].startswith('!'): #prefix is defined as '!'
            if message[0] in tapir.commands: #if not tapir checks if command in the the command dictionary
                await tapir.print_message(message[0], raw_message) #gets the console stuff
                await client.send_message(raw_message.channel, tapir.commands[message[0]]) #says the commands text
            elif message[0] == '!tapir' or message[0] == '!taper': #the tapir command!
                await tapir.print_message(message[0], raw_message) #gets the console stuff
                await tapir.tapir(raw_message, client) #gets the tapir image
            elif message[0] == '!attack':
                await tapir.print_message(message[0], raw_message) #gets the console stuff
                try:
                    await tapir.attack(message[1], raw_message, client)
                    await tapir.print_message(message[0], raw_message) #gets the console stuff
                except IndexError:
                    await client.send_message(raw_message.channel, "Whoops, you forgot to specify a character!")
                    await tapir.print_message("Attack_list_error", raw_message)
            elif message[0] == '!add_tapir' and raw_message.author.id == '149281074437029890': #add tapirs to the text if you are me :)
                tapir.tapirs_text.write(message[1] + "\n") #adds the link and a line ender thing (can't remember name)
                tapir.tapirs.append(message[1]) #also puts the link in the list for immediate usage
                tapir.images = len(tapir.tapirs) #allows to use instantly
                await tapir.print_message(message[0], raw_message) #prints on console
                await client.send_message(raw_message.channel, "Got it!") #confirms the tapir
            elif message[0] == '!close' and raw_message.author.id == '149281074437029890': #if you're me you can close tapir-bot
                tapir.tapirs_text.close() #closes the tapir.txt
                await client.logout() #logs tapir-bot out
            


    
client.run('bot_token') #bot token