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
        
        self.current_game = "say \"!?\" for help" #the current game message
        
        self.pairs = [
            ['georgie', 'pennywise']
            ]
            
        self.pair_health = [
            [100, 100]
            ]
        
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
        print('----------------') #prints '------' at end of startup squence
    
    async def print_message(self, message, raw_message): #prints the name of author and stuff
        """prints the name of author, commaand used, channel, and server that it was called in"""
        print(message, end=' ') #prints command on console
        print(raw_message.author, end=' @') #prints message author
        print(raw_message.server, end=':') #prints in console the server that the message was in with a ':' at the end
        print(raw_message.channel) #prints the server's channel
        
    async def private_message_recieved(self, raw_message, client): #when tapir-bot recieves a private message
        """sends me a private message of the channel ID and the author name and content"""
        await client.send_message(client.get_channel('173957638302728192'), '{} : {} \n {}'.format(raw_message.channel.id, raw_message.author.name, raw_message.content))
    
    async def send_message(self, raw_message, client):
        """I send a message, through tapir-bot"""
        message = raw_message.content.split(' ') #makes the message a list of the words
        receiver = message[1] #the channel is the ID I send
        receiver = client.get_channel(receiver) #it makes that into a channel class
        del message[0:2] #in message it deletes thee first two indexes
        message = ' '.join(message) #joins the list back together with a space inbeetween the indexes
        print(str(receiver) + ' : ' + message) #on consol it prints the channel and the message
        await client.send_message(receiver, message) #send the message
        
    
    async def tapir(self, message, client): #when someone calls the !tapir command
        """the tapir command function"""
        taper = self.tapirs[random.randrange(self.images)] #generates the tapir
        await client.send_message(message.channel, taper) #sends the tapir
        
    async def define(self, pair, raw_message, client):
        """will define a new pair for attack"""
        if pair not in self.pairs and pair[::-1] not in self.pairs: #if it's not defined
            self.pairs.append(pair) #puts the pair in
            self.pair_health.append([100, 100]) #appends the health to the health list
            await client.send_message(raw_message.channel, '{} vs. {} is ready!'.format(pair[0], pair[1])) #confirms they are added
        else: #if it's already defined
            await client.send_message(raw_message.channel, '{} vs. {} is already defined.'.format(pair[0], pair[1])) #says they are already defined
    
    async def reset(self, raw_message, client):
        """resets all of the healths to 100"""
        for pair in range(len(self.pair_health)): #for the pair in the health list
            for character in range(len(self.pair_health[pair])): #for every character in the pair
                self.pair_health[pair][character] = 100 #their health is 100
        await client.send_message(raw_message.channel, 'All healths reset!')
                
    async def attack(self, pair, raw_message, client):
        """attack command, with unlimited pairs"""
        if pair in self.pairs or pair[::-1] in self.pairs: #if they are in the list
            attacker = pair[0] #makes sure to define which is the attacker
            defender = pair[1] #and the defender
            if pair not in self.pairs: #if the base isn't in, it reverse the two
                pair = pair[::-1]
            pair_index = self.pairs.index(pair) #finds the index of the pair in the pairs list
            attacker_index = self.pairs[pair_index].index(attacker) #finds the index of the attacker
            defender_index = self.pairs[pair_index].index(defender) #and the defender
            if self.pair_health[pair_index][attacker_index] > 0: #if the attacker is still alive
                damage = random.randrange(10, 21) #he damages the defender
                self.pair_health[pair_index][defender_index] -= damage #applies the damage
                if self.pair_health[pair_index][defender_index] > 0: #if the defender is still alive
                    await client.send_message(raw_message.channel, '{} did {} damage to {}, who has {} health left'.format(attacker, damage, defender, self.pair_health[pair_index][defender_index])) #says how much health is left of defender and such
                else: #if the defender has 0 or less health after being damaged
                    await client.send_message(raw_message.channel, '{} is dead!'.format(defender)) #if the defender dies it says so
            else: #if the attacker is dead
                await client.send_message(raw_message.channel, '{} is dead, they can\'t attack!'.format(attacker)) #says so
                