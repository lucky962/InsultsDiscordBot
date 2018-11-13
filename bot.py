# Work with Python 3.6
import discord
import random
import json
import re
import os

os.chdir('CMDDependencies')
djenable = []

with open('BotToken.txt') as f:
    TOKEN = f.read()

with open('insults.txt') as f:
    insults = f.readlines()
insults = [x.strip() for x in insults]

with open('OtherVars.txt', 'r') as document:
    OtherVars = {}
    for line in document:
        line = line.split()
        OtherVars[line[0]] = line[1]

with open('DJENABLED.txt', 'r') as document:
    djenable = document.readlines()
    djenable[:] = [x.rstrip('\n') for x in djenable]
    print(djenable)

client = discord.Client()

@client.event
async def on_message(message):
    global insults
    global OtherVars
    global djenable
    djenabledit = []
    print('{0.author.mention}'.format(message))
    print(message.content)
    print(message.server.id)
    print(message.server.id in djenable)
    print(djenable)
    # IDEAS FOR NEW FUNCTIONS
    # if '{0.author.mention}'.format(message) == '<@256334462697078784>':
    #     await client.send_message(message.channel, '<@256334462697078784> ' + insults[random.randint(0,len(insults))])
    # if (sum(1 for c in message.content if c.isupper()) > (len(message.content) / 2)) and (len(message.content) > 1):
    #     await client.send_message(message.channel, 'No need to shout...')
    
    if message.content.startswith('i!disloop'):
        with open('OtherVars.txt', 'r') as document:
            data = document.readlines()
        data[0] = 'Loop False\n'
        with open('OtherVars.txt', 'w') as document:
            document.writelines(data)
        with open('OtherVars.txt', 'r') as document:
            OtherVars = {}
            for line in document:
                line = line.split()
                OtherVars[line[0]] = line[1]
        await client.send_message(message.channel, 'Loop Disabled')
    elif message.content.startswith('i!enaloop'):
        await client.send_message(message.channel, 'Sorry, Loop has been temporarily disabled, we apologise for the inconveniences')
    #     with open('OtherVars.txt', 'r') as document:
    #         data = document.readlines()
    #     data[0] = 'Loop True\n'
    #     with open('OtherVars.txt', 'w') as document:
    #         document.writelines(data)
    #     with open('OtherVars.txt', 'r') as document:
    #         OtherVars = {}
    #         for line in document:
    #             line = line.split()
    #             OtherVars[line[0]] = line[1]
    #     await client.send_message(message.channel, 'Loop Enabled')
    elif message.content.startswith('i!loop') and OtherVars['Loop'] == 'True':
        await client.send_message(message.channel, 'i!loop')
        # await client.send_message(message.channel, 'i!loop has been disabled for now.\nIt will be back soon though! With an added stop function!')
    elif message.content.startswith('i!loop') and OtherVars['Loop'] == 'False':
        await client.send_message(message.channel, 'The i!loop function has been disabled until further notice.')
        # to re-enable it, please type i!enaloop.')
    elif ((message.content in insults) and (message.author == client.user)) or ('I\'m Insults Bot' in message.content):
        await client.add_reaction(message, '😂')
    elif message.author == client.user:
        return
    elif message.content.startswith('i!insult'):
        if len(message.content) > 9:
            try:
                await client.send_message(message.channel, insults[int(message.content[9:]) - 1])
            except IndexError:
                await client.send_message(message.channel, 'Sorry, I don\'t have that many/few insults, I only have ' + str(len(insults)) + ' insults, but here\'s another random insult.')
                await client.send_message(message.channel, insults[random.randint(0,(len(insults) - 1))])
            except:
                await client.send_message(message.channel, insults[random.randint(0,(len(insults) - 1))])
        else:
            await client.send_message(message.channel, insults[random.randint(0,(len(insults) - 1))])
    elif message.content.startswith('Hello <@503096810961764364>') or message.content.startswith('Hello <@!503096810961764364>'):
        await client.send_message(message.channel, 'Hello {0.author.mention}'.format(message))
    elif message.content.startswith('<@503096810961764364>, start the dad jokes') or message.content.startswith('<@!503096810961764364>, start the dad jokes'):
        with open('DJENABLED.txt','r') as document:
            djenable = document.readlines()
            djenable[:] = [x.rstrip('\n') for x in djenable]
            if not message.server.id in djenable:
                djenable.append(message.server.id)
            djenabledit[:] = [x + '\n' for x in djenable]
        with open('DJENABLED.txt','w') as document:
            document.writelines(djenabledit)
        await client.send_message(message.channel, 'Sure!')
        print(OtherVars['DADJOKE'])
    elif message.content.startswith('<@503096810961764364>, stop the dad jokes') or message.content.startswith('<@!503096810961764364>, stop the dad jokes'):
        with open('DJENABLED.txt','r') as document:
            djenable = document.readlines()
            djenable[:] = [x.rstrip('\n') for x in djenable]
            if message.server.id in djenable:
                djenable.remove(message.server.id)
            djenabledit[:] = [x + '\n' for x in djenable]
        with open('DJENABLED.txt','w') as document:
            document.writelines(djenabledit)
        await client.send_message(message.channel, 'Fine...')
    elif 'i am' in message.content.lower() and (message.server.id in djenable):
        dadname = re.split("I am ", message.content, flags=re.IGNORECASE)
        if 'insult' in message.content.lower():
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
        else:
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif 'i\'m' in message.content.lower() and (message.server.id in djenable):
        dadname = re.split("I\'m ", message.content, flags=re.IGNORECASE)
        if 'insult' in message.content.lower():
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
        else:
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif 'i’m' in message.content.lower() and (message.server.id in djenable):
        dadname = re.split("I’m ", message.content, flags=re.IGNORECASE)
        if 'insult' in message.content.lower():
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
        else:
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif ' im ' in message.content.lower() and (message.server.id in djenable):
        dadname = re.split("Im ", message.content, flags=re.IGNORECASE)
        if 'insult' in message.content.lower():
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
        else:
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif 'im ' in message.content.lower() and (message.server.id in djenable):
        print('dadjoke')
        dadname = re.split("Im ", message.content, flags=re.IGNORECASE)
        if len(dadname[0]) == 0:
            if 'insult' in message.content.lower():
                await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
            else:
                await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif message.content.startswith('i!suggestion'):
        file = open("insults.txt","a")
        file.write(message.content[13:] + '\n')
        file.close()
        with open('insults.txt') as f:
            insults = f.readlines()
        insults = [x.strip() for x in insults]
        await client.send_message(message.channel, 'Thank you for the insult suggestion, it has been added to the list of insults!')
    elif message.content.startswith('i!help'):
        HelpMsg = discord.Embed(
            title="Help Page",
            description="This is a page full of commands you can use with Insults Bot",
            color=3447003
        )
        HelpMsg.set_author(
            name='Insults Bot', 
            icon_url=client.user.avatar_url
            )
        HelpMsg.add_field(
            name="i!help",
            value="Displays this help page."
        )
        HelpMsg.add_field(
            name="i!insult <number(optional)>",
            value="Displays a randomly selected Insult. If a number is present, show the insult at that position."
        )
        HelpMsg.add_field(
            name="i!suggestion <suggestion>",
            value="This adds an insult to the list of insults that this bot chooses from."
        )
        HelpMsg.add_field(
            name="i!updatelog",
            value="This shows the improvements from the last update and upcoming updates."
        )
        HelpMsg.add_field(
            name="@Insults, stop the dad jokes",
            value="This stops insults bot from making any more dad jokes or until reenabled. DadJokes are disabled at default."
        )
        HelpMsg.add_field(
            name="@Insults, start the dad jokes",
            value="This allows insults bot to make dad jokes. Example of dad joke that this bot makes: Someone: I'm happy. Bot: Hi happy!"
        )
        HelpMsg.add_field(
            name="@Insults, please leave",
            value="This will force the bot to leave the server, please don\'t do this."
        )
        HelpMsg.add_field(
            name="i!loop",
            value=("This makes the bot say i!loop on repeat. Type i!disloop to disable loop and i!enaloop to enable loop. Loop is currently ") + ('enabled.' if OtherVars['Loop'] == 'True' else 'disabled until further notice.')
        )
        HelpMsg.set_footer(
            icon_url=client.user.avatar_url,
            text="© 2018 Lucky's Creations"
        )   
        await client.send_message(message.channel, embed=HelpMsg)
    elif message.content.startswith('i!updatelog'):
        # doc = open('updatelog.txt','r')
        # updatelog = doc.read()
        # await client.send_message(message.channel, updatelog)
        # doc.close()
        await client.send_message(message.channel, "To view the update log, please visit http://discordbotupdates.luckysweb.net/")
    elif message.content.startswith('i!'):
        await client.send_message(message.channel, 'Sorry I don\'t know about that command yet, to see all available commands, please type i!help!')
    elif message.content.startswith('<@503096810961764364>, please leave') or message.content.startswith('<@!503096810961764364>, please leave'):
        await client.send_message(message.channel, 'I am sorry to have failed you, I will now leave.')
        await client.leave_server(client.get_server(message.server.id))
        # print(client.get_guild(id))

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Type i!help for help!'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
