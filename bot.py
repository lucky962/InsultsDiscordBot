# Work with Python 3.6
import discord
import random
import json

with open('BotToken.txt') as f:
    TOKEN = f.read()

client = discord.Client()
commands = {}

with open('insults.txt') as f:
    insults = f.readlines()
insults = [x.strip() for x in insults]

with open('OtherVars.txt', 'r') as document:
    OtherVars = {}
    for line in document:
        line = line.split()
        OtherVars[line[0]] = line[1]

@client.event
async def on_message(message):
    global OtherVars
    print('{0.author.mention}'.format(message))
    print(message.content)
    print(message)
    # we do not want the bot to reply to itself
    # if '{0.author.mention}'.format(message) == '<@256334462697078784>':
    #     await client.send_message(message.channel, '<@256334462697078784> ' + insults[random.randint(0,len(insults))])

    if message.author == client.user:
        return
    # if (sum(1 for c in message.content if c.isupper()) > (len(message.content) / 2)) and (len(message.content) > 1):
    #     await client.send_message(message.channel, 'No need to shout...')
    if message.content.startswith('i!insult'):
        global insults
        await client.send_message(message.channel, insults[random.randint(0,len(insults))])
    elif message.content.startswith('Hello <@!503096810961764364>'):
        await client.send_message(message.channel, 'Hello {0.author.mention}'.format(message))
    elif message.content.startswith('<@!503096810961764364>, start the dad jokes'):
        file = open("OtherVars.txt","w")
        file.write('DADJOKE True')
        file.close()
        with open('OtherVars.txt', 'r') as document:
            OtherVars = {}
            for line in document:
                line = line.split()
                OtherVars[line[0]] = line[1]
        await client.send_message(message.channel, 'Sure!')
        print(OtherVars['DADJOKE'])
    elif message.content.startswith('<@!503096810961764364>, stop with the dad jokes'):
        file = open("OtherVars.txt","w")
        file.write('DADJOKE False')
        file.close()
        with open('OtherVars.txt', 'r') as document:
            OtherVars = {}
            for line in document:
                line = line.split()
                OtherVars[line[0]] = line[1]
        await client.send_message(message.channel, 'Fine...')
        print(OtherVars['DADJOKE'])
    elif message.content.startswith('I am ') and OtherVars['DADJOKE'] == 'True':
        await client.send_message(message.channel, 'Hello ' + message.content[5:] + ', I\'m Insults Bot!')
    elif (message.content.startswith('I\'m ') or message.content.startswith('I\'M ')) and OtherVars['DADJOKE'] == 'True':
        await client.send_message(message.channel, 'Hello ' + message.content[4:] + ', I\'m Insults Bot!')
    elif (message.content.startswith('Im ') or message.content.startswith('im ') or message.content.startswith('IM ')) and OtherVars['DADJOKE'] == 'True':
        await client.send_message(message.channel, 'Hello ' + message.content[3:] + ', I\'m Insults Bot!')
    elif message.content.startswith('i!loop'):
        await client.send_message(message.channel, 'i!loop has been disabled for now.\nIt will be back soon though! With an added stop function!')
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
            name="i!insults",
            value="Displays a randomly selected Insult."
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
            name="@Insults, stop with the dad jokes",
            value="This stops insults bot from making any more dad jokes or until reenabled"
        )
        HelpMsg.add_field(
            name="@Insults, start the dad jokes",
            value="This allows insults bot to make dad jokes"
        )
        HelpMsg.timestamp
            #timestamp=new Date(),
        HelpMsg.set_footer(
            icon_url=client.user.avatar_url,
            text="© 2018 Lucky's Creations"
        )   
        await client.send_message(message.channel, embed=HelpMsg)
    elif message.content.startswith('i!updatelog'):
        await client.send_message(message.channel, '**Current update:** \nAdded a Dad Joke replying to one saying I\'m... \nAdded DadJoke Enabler/Disabler \n Made Help Menu look a looot better \n**Things being worked on:** \nMaking update log look better. \nAdding @bot please leave function\nAdding bot\'s reactions to it\'s own insults\nAdding stop function to i!loop function.')
    elif message.content.startswith('p!'):
        await client.send_message(message.channel, 'The new prefix for pokecord is \'p\'')
    elif message.content.startswith('i!'):
        await client.send_message(message.channel, 'Sorry I don\'t know about that command yet, to see all available commands, please type i!help!')
    elif message.content.startswith('<@503096810961764364>, please leave') or message.content.startswith('Test'):
        # await client.send_message(message.channel, 'I am sorry to have failed you, I will now leave.')
        # await client.leave_server(client.get_server(id))
        print(client.get_guild(id))

    # if message.content.startswith('!hello'):
    #     msg = 'Hello {0.author.mention}'.format(message)
    #     await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Type i!help for help!'))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)