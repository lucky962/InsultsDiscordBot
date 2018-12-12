# Work with Python 3.6
import discord
import random
import json
import re
import os
import time
import requests
from PyDictionary import PyDictionary
from yandex_translate import YandexTranslate
from nested_lookup import nested_lookup
from bs4 import BeautifulSoup

os.chdir('CMDDependencies')

if not os.path.isfile('lastmessage.py'):
    with open('lastmessage.py','w') as f:
        f.writelines('lastmessage = {\n    \'<@244596682531143680>\':\'' + str(time.time()) + '\',\n}')

from CMDDependencies.ServerPrefixes import *
from CMDDependencies.lastmessage import *

djenable = []
spamdetect = {}

with open('translaterkey.txt') as g:
    f = g.read()
    translate = YandexTranslate(f)

with open('BotToken.txt') as f:
    TOKEN = f.read()

with open('insults.txt') as f:
    insults = f.readlines()
insults = [x.strip() for x in insults]

with open('hb.txt') as f:
    hb = f.read()
    print(hb)

with open('dictionarykeys.txt') as f:
    contents = [x.strip() for x in f]
    app_id = contents[0]
    app_key = contents[1]

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
    global hb
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
    try:
        if (time.time() - 2 < float(lastmessage.get('{0.author.mention}'.format(message)))):
            spamdetect.update({'{0.author.mention}'.format(message):(spamdetect.get('{0.author.mention}'.format(message))) + 1})
            print (spamdetect.get('{0.author.mention}'.format(message)))
            if spamdetect.get('{0.author.mention}'.format(message)) > 2:
                await client.send_message(message.channel, "Hello, it seems that you might be spamming, please don't spam or you may be banned.")
        else:
            spamdetect.update({'{0.author.mention}'.format(message):0})
    except:
        lastmessage.update({'{0.author.mention}'.format(message):time.time()})
    if (message.content.startswith('pcatch ')) and (time.time() - 60 > float(lastmessage.get('{0.author.mention}'.format(message)))):
        await client.send_message(message.channel, 'Hello, it seems you haven\'t said anything since ' + str(time.time() - float(lastmessage.get('{0.author.mention}'.format(message)))) + ' seconds ago, but seem to have tried to catch a pokemon, you have been suspected of lurking.')
    lastmessage.update({'{0.author.mention}'.format(message):time.time()})
    with open('lastmessage.py','w') as f:
        f.write("lastmessage = {\n")
        for key,val in lastmessage.items():
            f.write('    \'' + key + '\':\'' + str(val) + '\',\n')
        f.write('}\n')
    if (('{0.author.mention}'.format(message) == '<@!256334462697078784>') or ('{0.author.mention}'.format(message) == '<@256334462697078784>')) and (hb == '0') and (time.time() > 1543755600):
        await client.send_message(message.channel, 'Happy Birthday <@256334462697078784>!!!')
        hb = 1
        with open('hb.txt','w') as f:
            f.write('1')
    if message.content.startswith(CMDPrefix.get(message.server.id) if message.server.id in CMDPrefix else 'i!'):
        messege = message.content[len(CMDPrefix.get(message.server.id)):]
        print(message)
        if messege.startswith('loop') and OtherVars['Loop'] == 'True':
            await client.send_message(message.channel, 'loop')
            # await client.send_message(message.channel, 'loop has been disabled for now.\nIt will be back soon though! With an added stop function!')
        elif messege.startswith('loop') and OtherVars['Loop'] == 'False':
            await client.send_message(message.channel, 'The loop function has been disabled until further notice.')
            # to re-enable it, please type enaloop.')
        elif message.author == client.user:
            return
        elif messege.startswith('disloop'):
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
        elif messege.startswith('enaloop'):
            await client.send_message(message.channel, 'Sorry, Loop has been temporarily disabled, we apologise for the inconveniences')
            # with open('OtherVars.txt', 'r') as document:
            #     data = document.readlines()
            # data[0] = 'Loop True\n'
            # with open('OtherVars.txt', 'w') as document:
            #     document.writelines(data)
            # with open('OtherVars.txt', 'r') as document:
            #     OtherVars = {}
            #     for line in document:
            #         line = line.split()
            #         OtherVars[line[0]] = line[1]
            # await client.send_message(message.channel, 'Loop Enabled')
        elif messege.startswith('insult'):
            if len(messege) > 9:
                try:
                    await client.send_message(message.channel, insults[int(message[9:]) - 1])
                except IndexError:
                    await client.send_message(message.channel, 'Sorry, I don\'t have that many/few insults, I only have ' + str(len(insults)) + ' insults, but here\'s another random insult.')
                    await client.send_message(message.channel, insults[random.randint(0,(len(insults) - 1))])
                except:
                    await client.send_message(message.channel, insults[random.randint(0,(len(insults) - 1))])
            else:
                await client.send_message(message.channel, insults[random.randint(0,(len(insults) - 1))])
        elif messege.lower().startswith('define'):
            if len(messege) > 7:
                r = requests.get('https://od-api.oxforddictionaries.com:443/api/v1/entries/' + 'en' + '/' + messege[7:].lower(), headers = {'app_id': app_id, 'app_key': app_key})
                data = json.loads(r.text)
                definitions = nested_lookup('definitions', data)
                # definitions = "\n".join(definitions)
                await client.send_message(message.channel, "Definitions: \n" + str(definitions))
                # definition = PyDictionary().meaning(messege[7:])
                # definitionmsg = discord.Embed(
                #     title=messege[7:].capitalize(),
                #     color=3447003
                # )
                # if definition == None:
                #     await client.send_message(message.channel, 'Sorry, word not found.')
                #     return
                # if 'Noun' in definition:
                #     finaldef = ''
                #     for x in definition.get('Noun'):
                #         finaldef = finaldef + str(definition.get('Noun').index(x) + 1) + '. ' + x + '\n'
                #     definitionmsg.add_field(
                #         name='Noun',
                #         value=finaldef
                #     )
                # if 'Verb' in definition:
                #     finaldef = ''
                #     for x in definition.get('Verb'):
                #         finaldef = finaldef + str(definition.get('Verb').index(x) + 1) + '. ' + x + '\n'
                #     definitionmsg.add_field(
                #         name='Verb',
                #         value=finaldef
                #     )
                # if 'Adjective' in definition:
                #     finaldef = ''
                #     for x in definition.get('Adjective'):
                #         finaldef = finaldef + str(definition.get('Adjective').index(x) + 1) + '. ' + x + '\n'
                #     definitionmsg.add_field(
                #         name='Adjective',
                #         value=finaldef
                #     )
                # if 'Adverb' in definition:
                #     finaldef = ''
                #     for x in definition.get('Adverb'):
                #         finaldef = finaldef + str(definition.get('Adverb').index(x) + 1) + '. ' + x + '\n'
                #     definitionmsg.add_field(
                #         name='Adverb',
                #         value=finaldef
                #     )
                # await client.send_message(message.channel, embed=definitionmsg)
            else:
                await client.send_message(message.channel, 'Error: No word specified')
        elif messege.startswith('synonyms'):
            r = requests.get('https://od-api.oxforddictionaries.com:443/api/v1/entries/' + 'en' + '/' + messege[9:].lower() + '/synonyms', headers = {'app_id': app_id, 'app_key': app_key})
            data = json.loads(r.text)
            synonymes = nested_lookup('text', data)
            print(len(str(synonymes)))
            await client.send_message(message.channel, "synonyms \n" + str(synonymes))
        elif messege.startswith('translate'):
            if len(messege) > 10:
                await client.send_message(message.channel, 'Translation: ' + translate.translate(messege[13:],messege[10:12]).get('text')[0])
            else:
                await client.send_message(message.channel, 'No word specified.')
        elif messege.startswith('patch'):
            page = requests.get('https://playoverwatch.com/en-us/news/patch-notes/pc').text
            pagelist = page.split('\n')
            soup = BeautifulSoup(page, 'html.parser')
            price_box = soup.find('span', attrs={'class':'IconHeading-text'})
            price = price_box.text
            for i, elem in enumerate(pagelist):
                if price in elem:
                    index = i
                    break
            for i, elem in enumerate(pagelist):
                if 'Learn more about' in elem:
                    indices = i
                    break
            pagelist = pagelist[index + 1:indices + 1]
            pageliste = '\n'.join(pagelist)
            pageliste = BeautifulSoup(pageliste, 'html.parser')
            price_box = soup.find('span', attrs={'class':'IconHeading-text'})
            price_boxe = soup.find('a', attrs={'class':'u-float-left'})
            price = pageliste.text
            PatchNotes = discord.Embed(
                title=price_boxe.get('href'),
                url='https://playoverwatch.com/en-us/news/patch-notes/pc' + price_boxe.get('href'),
                color=0xFFFFFF,
            )
            PatchNotes.set_thumbnail(
                url='http://www.stickpng.com/assets/images/586273b931349e0568ad89df.png'
            )
            PatchNotes.add_field(
                name=price_box.text,
                value=price
            )
            PatchNotes.set_footer(
                icon_url=message.server.get_member("244596682531143680").avatar_url,
                text="© 2018 Lucky's Creations"
            )   
            await client.send_message(message.channel, embed=PatchNotes)
        elif messege.startswith('suggestion'):
            file = open("insults.txt","a")
            file.write(message[13:] + '\n')
            file.close()
            with open('insults.txt') as f:
                insults = f.readlines()
            insults = [x.strip() for x in insults]
            await client.send_message(message.channel, 'Thank you for the insult suggestion, it has been added to the list of insults!')
        elif messege.startswith('help'):
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
                name=(CMDPrefix.get(message.server.id) if message.server.id in CMDPrefix else 'i!') + "help",
                value="Displays this help page."
            )
            HelpMsg.add_field(
                name=(CMDPrefix.get(message.server.id) if message.server.id in CMDPrefix else 'i!') + "version",
                value="This will show the current version of Insults Bot."
            )
            HelpMsg.add_field(
                name=(CMDPrefix.get(message.server.id) if message.server.id in CMDPrefix else 'i!') + "insult <number(optional)>",
                value="Displays a randomly selected Insult. If a number is present, show the insult at that position."
            )
            HelpMsg.add_field(
                name=(CMDPrefix.get(message.server.id) if message.server.id in CMDPrefix else 'i!') + "suggestion <suggestion>",
                value="This adds an insult to the list of insults that this bot chooses from."
            )
            HelpMsg.add_field(
                name=(CMDPrefix.get(message.server.id) if message.server.id in CMDPrefix else 'i!') + "prefix <prefix>",
                value=("This changes the prefix for commandsv")
            )            
            HelpMsg.add_field(
                name=(CMDPrefix.get(message.server.id) if message.server.id in CMDPrefix else 'i!') + "loop",
                value=("This makes the bot say this command on repeat. Loop is currently ") + ('enabled.' if OtherVars['Loop'] == 'True' else 'disabled until further notice.')
            )
            HelpMsg.add_field(
                name=(CMDPrefix.get(message.server.id) if message.server.id in CMDPrefix else 'i!') + "updatelog",
                value="This shows the improvements from the last update and upcoming updates."
            )
            HelpMsg.add_field(
                name="@Insults, stop/start dad jokes",
                value="This stops/allows the insult bot from making any more dad jokes. DadJokes are disabled at default."
            )
            HelpMsg.add_field(
                name="@Insults, please leave",
                value="This will force the bot to leave the server, please don\'t do this."
            )
            HelpMsg.set_footer(
                icon_url=message.server.get_member("244596682531143680").avatar_url,
                text="© 2018 Lucky's Creations"
            )   
            await client.send_message(message.channel, embed=HelpMsg)
        elif messege.startswith('updatelog'):
            # doc = open('updatelog.txt','r')
            # updatelog = doc.read()
            # await client.send_message(message.channel, updatelog)
            # doc.close()
            await client.send_message(message.channel, "To view the update log, please visit http://discordbotupdates.luckysweb.net/")
        elif messege.startswith('version'):
            await client.send_message(message.channel, "You are using Insults Bot TEST VERSION v1.5.0")
        elif messege.startswith('test'):
            await client.send_message(message.channel, 'Debug comments ' + '{0.author.mention}'.format(message) + ' ' + message.content +  ' ' + message.server.id +  ' ' + str(djenable) + str(CMDPrefix))
            await client.send_message(message.channel, "<@244596682531143680>")
        elif messege.startswith('prefix'):
            if len(messege) < 8:
                await client.send_message(message.channel, 'Your prefix has been set to the default(i!) from ' + CMDPrefix.get(message.server.id))
                CMDPrefix.update({message.server.id:'i!'})
                with open('ServerPrefixes.py','w') as f:
                    f.write("CMDPrefix = {\n")
                    for key,val in CMDPrefix.items():
                        f.write('    \'' + key + '\':\'' + val + '\',\n')
                    f.write('}\n')
            elif len(messege) > 7:
                await client.send_message(message.channel, 'You have changed your prefix from ' + CMDPrefix.get(message.server.id) + ' to ' + messege[7:])
                CMDPrefix.update({message.server.id:messege[7:]})
                with open('ServerPrefixes.py','w') as f:
                    f.write("CMDPrefix = {\n")
                    for key,val in CMDPrefix.items():
                        f.write('    \'' + key + '\':\'' + val + '\',\n')
                    f.write('}\n')
        else:
            await client.send_message(message.channel, 'Sorry I don\'t know about that command yet, to see all available commands, please type ' + (CMDPrefix.get(message.server.id) if message.server.id in CMDPrefix else 'i!') + 'help')
    elif ((message.author == client.user)) and ((message.content in insults) or ('I\'m Insults Bot' in message.content)):
        await client.add_reaction(message, '😂')
    elif message.author == client.user:
        return
    elif message.content.startswith('Hello <@503096810961764364>') or message.content.startswith('Hello <@!503096810961764364>'):
        await client.send_message(message.channel, 'Hello {0.author.mention}'.format(message))
    elif ('<@503096810961764364>' in message.content.lower() or '<@!503096810961764364>' in message.content.lower()) and 'start' in message.content.lower() and 'dad joke' in message.content.lower():
        with open('DJENABLED.txt','r') as document:
            djenable = document.readlines()
            djenable[:] = [x.rstrip('\n') for x in djenable]
            if not message.server.id in djenable:
                await client.send_message(message.channel, 'Sure!')
                djenable.append(message.server.id)
            else:
                await client.send_message(message.channel, 'Dad jokes are already enabled.')
            djenabledit[:] = [x + '\n' for x in djenable]
        with open('DJENABLED.txt','w') as document:
            document.writelines(djenabledit)
        print(OtherVars['DADJOKE'])
    elif ('<@503096810961764364>' in message.content.lower() or '<@!503096810961764364>' in message.content.lower()) and 'stop' in message.content.lower() and 'dad joke' in message.content.lower():
        with open('DJENABLED.txt','r') as document:
            djenable = document.readlines()
            djenable[:] = [x.rstrip('\n') for x in djenable]
            if message.server.id in djenable:
                await client.send_message(message.channel, 'Fine...')
                djenable.remove(message.server.id)
            else:
                await client.send_message(message.channel, 'Dad jokes are already disabled.')
            djenabledit[:] = [x + '\n' for x in djenable]
        with open('DJENABLED.txt','w') as document:
            document.writelines(djenabledit)
    elif (message.content.startswith('<@503096810961764364>') or message.content.startswith('<@!503096810961764364>')) and ("shut" in message.content.lower()) and ("up" in message.content.lower()):
        with open('DJENABLED.txt','r') as document:
            djenable = document.readlines()
            djenable[:] = [x.rstrip('\n') for x in djenable]
            if message.server.id in djenable:
                await client.send_message(message.channel, 'No need to be so rude, but fine I\'ll stop')
                djenable.remove(message.server.id)
            else:
                await client.send_message(message.channel, 'Dad jokes are already disabled.')
            djenabledit[:] = [x + '\n' for x in djenable]
        with open('DJENABLED.txt','w') as document:
            document.writelines(djenabledit)
    elif 'i am' in message.content.lower() and (message.server.id in djenable):
        dadname = re.split("I am ", message.content, flags=re.IGNORECASE)
        if 'insult bot' in message.content.lower() or 'insult bots' in message.content.lower():
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
        else:
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif 'i\'m' in message.content.lower() and (message.server.id in djenable):
        dadname = re.split("I\'m ", message.content, flags=re.IGNORECASE)
        if 'insult bot' in message.content.lower() or 'insult bots' in message.content.lower():
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
        else:
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif 'i’m' in message.content.lower() and (message.server.id in djenable):
        dadname = re.split("I’m ", message.content, flags=re.IGNORECASE)
        if 'insult bot' in message.content.lower() or 'insult bots' in message.content.lower():
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
        else:
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif ' im ' in message.content.lower() and (message.server.id in djenable):
        dadname = re.split("Im ", message.content, flags=re.IGNORECASE)
        if 'insult bot' in message.content.lower() or 'insult bots' in message.content.lower():
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
        else:
            await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif 'im ' in message.content.lower() and (message.server.id in djenable):
        print('dadjoke')
        dadname = re.split("Im ", message.content, flags=re.IGNORECASE)
        if len(dadname[0]) == 0:
            if 'insult bot' in message.content.lower() or 'insult bots' in message.content.lower():
                await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m... wait... That\'s me!!!')
            else:
                await client.send_message(message.channel, 'Hello ' + dadname[1] + ', I\'m Insults Bot!')
    elif ('5 year old' in message.content.lower()) or ('you are 5' in message.content.lower()):
        await client.send_message(message.channel, 'Do you mean 15 year old?')
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
