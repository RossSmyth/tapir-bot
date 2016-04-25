#https://discordapp.com/oauth2/authorize?&client_id=173642301921296385&scope=bot&permissions=0
#random tapir bot
#http://imgur.com/a/Nwp6c/
#http://imgur.com/a/QAr54

import random #imports the random module
import discord #imports the discord api module thing
import asyncio #imports asyncio

#giant list of tapir picture links
tapirs = ["http://i.imgur.com/tgPoQ9S.jpg", "http://i.imgur.com/n2BjyFA.png", "http://i.imgur.com/e18ZHri.png", "http://i.imgur.com/VJDf9s1.png", "http://i.imgur.com/dRAiEe4.png", "http://i.imgur.com/wdova3J.png", "http://i.imgur.com/tJjx4qK.png", "http://i.imgur.com/qeN3TjM.png", "http://i.imgur.com/tHPhFMa.gif", "http://i.imgur.com/WKQiNFw.jpg", "http://i.imgur.com/x4j0d90.jpg", "http://i.imgur.com/Rla6CxQ.jpg", "http://i.imgur.com/TvbXgVi.jpg", "http://i.imgur.com/14P5ikM.jpg", "http://i.imgur.com/ktviJuC.png", "http://i.imgur.com/6994eHI.png", "http://i.imgur.com/5NwpK4M.jpg", "http://i.imgur.com/tpcRmnE.jpg", "http://i.imgur.com/Q3fk7iI.png", "http://i.imgur.com/OXLj8ev.png", "http://i.imgur.com/OYTzAWh.jpg", "http://i.imgur.com/UkBNbfh.png", "http://i.imgur.com/oC8wpfE.png", "http://i.imgur.com/ysuEpzp.png", "http://i.imgur.com/H2LU6Yv.png", "http://i.imgur.com/B2MSSDU.png", "http://i.imgur.com/a6ULF53.png", "http://i.imgur.com/PwodKBZ.png", "http://i.imgur.com/8kzzOoV.png", "http://i.imgur.com/Qurbk2d.png", "http://i.imgur.com/EV4Xr1D.png", "http://i.imgur.com/g2gxNsq.jpg", "http://i.imgur.com/3TTRki4.jpg", "http://i.imgur.com/9MTpv1c.png", "http://i.imgur.com/7zVbBDQ.jpg", "http://i.imgur.com/xncjSd7.png", "http://i.imgur.com/4SiThqS.png", "http://i.imgur.com/A0kOELj.png", "http://i.imgur.com/6BgR8WB.png", "http://i.imgur.com/96Ue3sg.png", "http://i.imgur.com/oFrncNz.png", "http://i.imgur.com/q9KKE6D.png", "http://i.imgur.com/FhXFun1.png", "http://i.imgur.com/mxZtX8j.png", "http://i.imgur.com/BKUUzmO.png", "http://i.imgur.com/S1vKjhl.jpg", "http://i.imgur.com/MWuXrUO.png", "http://i.imgur.com/uzYhQ9W.png", "http://i.imgur.com/HM7oIKc.png", "http://i.imgur.com/ONGCZhO.gif", "http://i.imgur.com/MwgplL8.png", "http://i.imgur.com/R8y3v49.jpg", "http://i.imgur.com/QSC0cSu.png", "http://i.imgur.com/11ZBtG7.png", "http://i.imgur.com/XfyT4H5.gif", "http://i.imgur.com/oLC9AyL.jpg", "http://i.imgur.com/0KVeMLf.jpg", "http://i.imgur.com/MPBZafq.png", "http://i.imgur.com/7g7LHjf.png", "http://i.imgur.com/oxgAUQA.png", "http://i.imgur.com/2W42kNe.jpg", "http://i.imgur.com/KmuiOzA.jpg", "http://i.imgur.com/lGofpCK.jpg", "http://i.imgur.com/pllUFWw.jpg", "http://i.imgur.com/kr2w5TZ.png", "http://i.imgur.com/1nmhYLT.png", "http://i.imgur.com/NfWZFze.png", "http://i.imgur.com/l91ZWw1.png", "http://i.imgur.com/ss1jKr8.png", "http://i.imgur.com/EiYlaVb.png", "http://i.imgur.com/f3jl9Qi.png", "http://i.imgur.com/1jOb6Hb.png", "http://i.imgur.com/dyfC203.png", "http://i.imgur.com/MW4JNJt.png", "http://i.imgur.com/i4lt0Cg.png", "http://i.imgur.com/38qGdwX.png", "http://i.imgur.com/XebMxP5.png", "http://i.imgur.com/qZx3d3D.png", "http://i.imgur.com/vCy8rFr.png" ]

images = len(tapirs) #so I don't have to manually count it, and able to add pictures easily

current_game = "\"!help-tapir\" for help" #string for the game being played. Don't forget escape characters!

client = discord.Client() #easier coding!

@client.event #haha I don't know what this means
async def on_ready(): #same here, maybe when bot is ready it does the thing
    await client.change_status(game=discord.Game(name=current_game)) #puts a help command in the game played
    print('Logged in as') #I know this one
    print(client.user.name) #prints the bots user name
    print("\nServers:") #puts "Servers" and a new line
    for s in client.servers: #lists the servers. Broken for the Discord API server. idk why
        print(s.name)
    print('------') #prints '------' at end of startup squence

#command dictionary
commands = {
    '!help-tapir' : 'Hello! I am a bot made by <@149281074437029890> . Type `|tapir` to get a random tapir image!',
    '!carrack' : 'Carrack pls http://i.imgur.com/BA3F1OI.png',
    '!jumby' : 'http://i.imgur.com/IGsmL62.png',
    '!jumbify': 'http://i.imgur.com/IGsmL62.png'
}

@client.event #still don't know what this means
async def on_message(message): #probably means when someone sends a message
    channel = message.channel #defines the channel the messages is sent to as a variable
    raw_message = message #the raw message is saved
    message = message.content.lower() #the message is put into a lower case format
    if len(message) >= 1: #must have atleast one character in the message
        message = message.split(' ') #message is made into a list split at every ' '
        if message[0].startswith('!'): #prefix is defined as '|'
            if message[0] == '!tapir': #the tapir command since it's speical and can't be string sadly
                print(message[0], end=' ') #prints command on console
                print(raw_message.author) #print who sent the command
                await client.send_message(raw_message.channel, tapirs[random.randrange(images)]) #send random link from image list
            elif message[0] in commands: #if not tapir checks if command in the the command dictionary
                print(message[0], end=' ') #prints command on console
                print(raw_message.author) #prints message author
                await client.send_message(raw_message.channel, commands[message[0]]) #says the commands text
            
    
    

client.run('bot_token') #bot token here