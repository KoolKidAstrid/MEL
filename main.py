import discord
import random

client = discord.Client()

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
                    max = len(args) - 1
                    screm = ' '.join(args[1:])
                    await message.channel.send(screm.upper())
                else:
                    await message.channel.send("AAAAAAAAAAAAAAAA")
            elif str(args[0]).lower() == 'ask':
                if str(args[1]).lower() == 'emotion':
                    await message.channel.send('TBD')
                if str(args[1]).lower() == 'name':
                    await message.channel.send('Mechanical Erratic Liberal (M.E.L.)')
        #await message.channel.send(first)

client.run("NjQzNjM1Mjc1MjMwMjE2MjEy.Xcopug.nefc0c9Pe-iuwZX0d3kvL8KbvYU")
