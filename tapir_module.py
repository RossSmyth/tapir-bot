#tapir-bot other file

import asyncio
import discord
import random

class tapirbot():
    """the tapirbot master"""
    def __init__(self):
        """all the startup junk"""
        self.tapirs_text = open('tapirs.txt', 'r+') #tapir .txt file is opened
        self.tapirs = [x.strip() for x in self.tapirs_text.readlines()] #makes a list out of the file and removes the '\n'
        
        self.images = len(self.tapirs) #sets the length to the length of the list
        
        self.current_game = "say \"!?\" for help" #the current game messsage
        
        self.georgie = 100 #health of georgie
        self.pennywise = 100 #health of pennywise
        
        self.commands = { #command dictioinary
    '!?' : 'Hello! I am a bot made by <@149281074437029890> . \n say `!tapir` to get a random tapir image! \n say `!carrack` for a Carrack picture. \n say `!azwe` for @Azwethinkweiz\'s beautiful mocap animation. \n say `!ben` to get Ben\'s beautiful dancing. \n say `!2.4` to get an update on the new 2.4 update. \n say `!scam` to know the truth of Star Citizen. \n say `!attack <pennywise or georgie>` to play the attacking minigame. say `!attack help` for more information. \n say `!source` for my Github!',
    '!carrack' : 'Carrack pls http://i.imgur.com/BA3F1OI.png',
    '!azwe': '<@118907180761088006> https://giphy.com/gifs/IEceC9q1MgWrK',
    '!ben' : 'http://i.imgur.com/OLKOQ6H.gif',
    '!2.4' : 'It\'s not just a meme! http://i.imgur.com/umBUjqW.gif',
    '!scam' : 'Star Citizen is a scam, confirmed by Chris Roberts himself: http://i.imgur.com/UK3D1c0.gifv',
    '!source' : 'My Github is here: https://github.com/treefroog/tapir-bot'
}
    
    async def startup(self, client): #when the client starts it prints all this junk
        """prints the startup stuff like the name of the bot, and the name of the server the bot is in"""
        print('Logged in as') #I know this one
        print(client.user.name) #prints the bots user name
        print("\nServers:") #puts "Servers" and a new line
        for s in client.servers: #lists the servers. Broken for all except TAPIR BOT server. Sometimes works. IDK why
            print(s.name)
        print('----------') #prints '------' at end of startup squence
    
    async def print_message(self, message, raw_message): #prints the name of author and stuff
        """prints the name of author, commaand used, channel, and server that it was called in"""
        print(message, end=' ') #prints command on console
        print(raw_message.author, end=' @') #prints message author
        print(raw_message.server, end=':') #prints in console the server that the message was in with a ':' at the end
        print(raw_message.channel) #prints the server's channel
    
    async def tapir(self, message, client): #when someone calls the !tapir command
        """the tapir command function"""
        taper = self.tapirs[random.randrange(self.images)] #generates the tapir
        await client.send_message(message.channel, taper) #sends the tapir
    
    async def attack(self, character, message, client):
        """does the pennywise vs. georgie attack minigame, for now at least"""
        if character == "pennywise": #if you play ass pennywise
            if self.pennywise > 0: #and he isn't dead
                damage = random.randrange(10, 21) #you get a damage value
                self.georgie -= damage #and damage the other charcter with it
                if self.georgie <= 0: #if georgie gets dead
                    await client.send_message(message.channel, "Georgie is dead!") #he is rekt
                else: #if georgie is still alive after being beat down
                    await client.send_message(message.channel, "Pennywise did {} points of damage to Georgie, he only has {} left!".format(damage, self.georgie)) #you get told
            else: #if pennywise was dead
                await client.send_message(message.channel, "Pennywise is dead dummy!") #your dumb, reset
        elif character == "georgie": #if you want to play as georgie
            if self.georgie > 0: #and he's not dead
                damage = random.randrange(10, 21) #he gets a damage value
                self.pennywise -= damage #applies it to pennywise
                if self.pennywise <= 0: #if he gets rekt
                    await client.send_message(message.channel, "Pennywise is dead!") #then he is dead, and you are told
                else: #if he is still alive
                    await client.send_message(message.channel, "Georgie did {} points of damage to Pennywise, he only has {} left!".format(damage, self.pennywise)) #you are told his health
            else: #if georgie is dead
                await client.send_message(message.channel, "Georgie is dead dummy!") #ur dumb reset
        elif character == "reset": #resets the game
            self.georgie = 100 #health back to 100
            self.pennywise = 100
            await client.send_message(message.channel, "Healths have been reset") #notified that it is reset
        elif character == "health": #if you want to know the health of the characters
            await client.send_message(message.channel, "Pennywise has: {} \n Georgie has {}".format(self.pennywise, self.georgie)) #it tells you the health!
        elif character == "help":
            await client.send_message(message.channel, "This is the Pennywise vs. Georgie game. It can be used to settle conflicts if needed. \n say `!attack pennywise` to play as pennywise, and say `!attack georgie` to play as georgie. \n say `!attack health` to get an update on the character's health. \n say `attack reset` to reset everything")
        else:
            await client.send_message(message.channel, "That isn't a recognized attacking character, say `!attack help` for help")