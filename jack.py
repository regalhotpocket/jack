import os, discord, urllib.request, json, QuestionMarkovChain, sched, time, asyncio, random, re, io

questions = json.loads(urllib.request.urlopen('https://raw.githubusercontent.com/regalhotpocket/questions/master/questions.json').read().decode())
markov = QuestionMarkovChain.QMC(questions)
jack = discord.Client()

async def spam(msg):
    for server in jack.servers:
        for channel in server.channels:
            if channel.name == '🤖bot_spam':
                return await jack.send_message(channel, msg)

@jack.event
async def on_message(message):
    if message.author == jack.user:
        pass
    elif message.content.startswith('!topic'):
        await jack.send_message(message.channel, random.choice(questions))
    elif message.content.startswith('!thonk'):
        await jack.send_message(message.channel, markov.generate())
    elif message.content.startswith('!data'):
        m = re.match("^!data ([0-9]+)", message.content)
        limit = 1000 if not m else int(m.group(1))
        for channel in message.server.channels:
            if channel.name == '🤖bot_spam':
                result = [['m' if log.content == '🌙' else 's', str(log.timestamp)] async for log in jack.logs_from(channel, limit) if log.content in ('🌙', '🌞')]
                await jack.send_file(destination=message.channel, fp=io.StringIO(json.dumps(result)), filename='data.json')

@jack.event
async def on_member_update(before, after):
    if str(after) == 'dark yaoi#9458':
        if after.status == discord.Status.offline: await spam('🌙')
        elif before.status == discord.Status.offline: await spam('🌞')

@jack.event
async def on_ready():
    await spam('🍇')

jack.run(os.environ['token'])
