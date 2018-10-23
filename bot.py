# Work with Python 3.6
import discord
import random

TOKEN = 'NTAzMDk2ODEwOTYxNzY0MzY0.Dq7sxQ.-YBSGfKLjxE6CrA8t5GhLys_fMk'

client = discord.Client()

insults = [ 'Do you practice being dumb or something?',
            'Your family tree must be a cactus because everybody on it is a prick.',
            'No I\'m not insulting you, I\'m describing you.',
            'It\'s better to let someone think you are an Idiot than to open your mouth and prove it.',
            'If I had a face like yours, I\'d sue my parents.',
            'Your birth certificate is an apology letter from the condom factory.',
            'I guess you prove that even god makes mistakes sometimes.',
            'If I wanted to kill myself I\'d climb your ego and jump to your IQ.',
            'You must have been born on a highway because that\'s where most accidents happen.',
            'I don\'t know what makes you so stupid, but it really works.',
            'Roses are red violets are blue, God made me pretty, what happened to you?',
            'Calling you an idiot would be an insult to all the stupid people.',
            'Some babies were dropped on their heads but you were clearly thrown at a wall.',
            'I\'d slap you, but that would be animal abuse.',
            'Please shut your mouth when you\'re talking to me.',
            'Why don\'t you go play in traffic.',
            'Stop trying to be a smart ass, you\'re just an ass.',
            'The last time I saw something like you, I flushed it.',
            'Your mind is on vacation but your mouth is working overtime.',
            'Why don\'t you slip into something more comfortable... like a coma.',
            'If you\'re gonna be two faced, honey at least make one of them pretty.',
            'Keep rolling your eyes, perhaps you\'ll find a brain back there.',
            'You are not as bad as people say, you are much, much worse.',
            'Sadly, there is no vaccine against stupidity.',
            'You\'re the reason the gene pool needs a lifeguard.',
            'How old are you? - Wait I shouldn\'t ask, you can\'t count that high.',
            'Have you been shopping lately? They\'re selling lives, you should go get one.',
            'You\'re like Monday mornings, nobody likes you.',
            'Of course I talk like an idiot, how else would you understand me?',
            'All day I thought of you... I was at the zoo.',
            'You\'re so fat, you could sell shade.',
            'I\'d like to see things from your point of view but I can\'t seem to get my head that far up my ass.',
            'Don\'t you need a license to be that ugly?',
            'If you really spoke your mind, you\'d be speechless.',
            'Stupidity is not a crime so you are free to go.',
            'If I told you that I have a piece of dirt in my eye, would you move?',
            'You so dumb, you think Cheerios are doughnut seeds.',
            'So, a thought crossed your mind? Must have been a long and lonely journey.',
            'You are so old, your birth-certificate expired.',
            'Every time I\'m next to you, I get a fierce desire to be alone.',
            'You\'re so dumb that you got hit by a parked car.',
            'Keep talking, someday you\'ll say something intelligent!',
            'You\'re so fat, you leave footprints in concrete.',
            'How did you get here? Did someone leave your cage open?',
            'Pardon me, but you\'ve obviously mistaken me for someone who gives a damn.',
            'Wipe your mouth, there\'s still a tiny bit of bullshit around your lips.',
            'Don\'t you have a terribly empty feeling - in your skull?',
            'As an outsider, what do you think of the human race?',
            'Just because you have one doesn\'t mean you have to act like one.',
            'We can always tell when you are lying. Your lips move.',
            'Are you always this stupid or is today a special occasion?'
]

@client.event
async def on_message(message):
    print('{0.author.mention}'.format(message))
    print(message.content)
    # we do not want the bot to reply to itself
    # if '{0.author.mention}'.format(message) == '<@256334462697078784>':
    #     await client.send_message(message.channel, '<@256334462697078784> ' + insults[random.randint(0,len(insults))])

    if message.author == client.user:
        return
    if (sum(1 for c in message.content if c.isupper()) > (len(message.content) / 2)) and (len(message.content) > 1):
        await client.send_message(message.channel, 'No need to shout...')
    if message.content.startswith('i!insult'):
        await client.send_message(message.channel, insults[random.randint(0,len(insults))])
    elif message.content.startswith('Hello <@503096810961764364>'):
        await client.send_message(message.channel, 'Hello {0.author.mention}'.format(message))
    elif message.content.startswith('i!loop'):
        await client.send_message(message.channel, 'i!loop has been disabled for now.\nIt will be back soon though! With an added stop function!')
    # elif message.content.startswith('Who sux?'):
    #     await client.send_message(message.channel, '<@256334462697078784> sux!')
    # elif message.content.startswith('i!loop'):
    #     client.send_message(message.channel, 'i!loop')
    elif message.content.startswith('i!help'):
        await client.send_message(message.channel, 'Commands:\ni!help: Displays this help page\ni!insult: Displays a randomly selected Insult.\ni!suggestion <suggestion> This adds an insult to the list of insults that this bot chooses from.')
    elif message.content.startswith('p!'):
        await client.send_message(message.channel, 'The new prefix for pokecord is \'P\'')
    elif message.content.startswith('i!'):
        await client.send_message(message.channel, 'Sorry I don\'t know about that command yet, to see all available commands, please type i!help!')

    # if message.content.startswith('!hello'):
    #     msg = 'Hello {0.author.mention}'.format(message)
    #     await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)