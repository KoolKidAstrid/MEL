import discord
import random
import asyncio


tokenfile = 'C:\\Users\\Astrid\\code\\MEL token\\meltoken.txt'
t = open(tokenfile, 'r')
print(t.readline())

client = discord.Client()
token = t.readline()

classes = ['nothing', 'fighter', ]

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='AAAAAAAAAAAAAAAAAAAAAAA'))
    print('Ready!')

@client.event
async def on_message(message):
    if message.author.bot == False:
        tempmsg = message.content
        first = tempmsg[:1]
        if first == '!':
            s = tempmsg[1:]
            args = s.split()
            if str(args[0]).lower() == 'screm':
                if len(args) > 1:
                    screm = ' '.join(args[1:])
                    await message.channel.send(screm.upper())
                else:
                    await message.channel.send("AAAAAAAAAAAAAAAA")
            elif str(args[0]).lower() == 'rpg':
                f = open('users.txt', 'r+')
                textOutput = f.read().splitlines()
                f.close
                startnum = textOutput.index(str(message.author.id))
                level = int(textOutput[startnum + 4])
                xp = int(textOutput[startnum + 6])
                name = textOutput[startnum + 2]
                money = int(textOutput[startnum + 8])
                charclass = int(textOutput[startnum + 10])
                hp = int(textOutput[startnum + 12])
                maxhp = int(textOutput[startnum + 14])
                items = []
                if len(args) == 1:
                    await message.channel.send('Try "!rpg help"')
                if str(args[1]).lower() == 'help':
                    await message.channel.send('--RPG COMMANDS--\n!rpg begin - setup stuff\n!rpg status - status of your character\n!rpg travel - change location')
                if str(args[1]).lower() == 'begin':
                    await message.author.send('tbd')
            elif str(args[0]).lower() == 'ask':
                if str(args[1]).lower() == 'emotion':
                    temp = random.randint(0,3)
                    possibleResponses = ['ANGRY', 'am good borb', 'SCREEEE', 'WATERBOARDING BELLLLLLLL']
                    await message.channel.send(possibleResponses[temp])
                if str(args[1]).lower() == 'name':
                    await message.channel.send('Mechanical Erratic Liberal (M.E.L.)')
#        await message.channel.send(first)

async def my_background_task():
    await client.wait_until_ready()
    while True:
        f = open('users.txt', 'r+')
        textOutput = f.read().splitlines()
        f.close
#        print(textOutput)
        for member in client.get_all_members():
            if member.id != 643635275230216212:
                if str(member.id) in textOutput:
                    startnum = textOutput.index(str(member.id))
                    level = int(textOutput[startnum+4])
                    xp = int(textOutput[startnum+6])
                    name = textOutput[startnum+2]
                    money = int(textOutput[startnum+8])
                    charclass = int(textOutput[startnum+10])
                    hp = int(textOutput[startnum + 12])
                    maxhp = int(textOutput[startnum + 14])
                    items = []

                    if xp >= (level^2 * 100):
                        xp -= (level^2 * 100)
                        level += 1
                        user = client.get_user(member.id)
                        await user.send(':confetti_ball: Congrats!  You leveled up! :confetti_ball:')

#                     print (name, str(level), str(xp), charclass, str(money), str(hp)+'/'+str(maxhp))
                else:
                    textOutput.extend(('id', (str(member.id)), 'name', member.name, 'level', '1', 'xp', '0', 'money', '500', 'class', '0', 'hp', '10', 'maxhp', '10', 'items', ''))
#        print(textOutput)
        f = open('users.txt', 'w+')
        f.truncate()
        for line in textOutput:
            f.write(line + '\n')
        f.close()
        await asyncio.sleep(1)

client.loop.create_task(my_background_task())
client.run(token)
