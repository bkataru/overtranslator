# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import subprocess
import re
import os

TOKEN = "NDQ1NTcyOTc4NzcyNTQxNDYx.DdsesQ.ZeWakXHGSPG8QX0Md_327kdA7V8"

client = discord.Client()

def indexFind(checklist, element):
    try:
        index_element = checklist.index(element)
        return index_element
    except ValueError:
        return -1
        
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!translate'):
        arr = ['python3.4', 'rgt.py']
        args = message.content.split(' ')
        if message.content.find('-h') != -1 or message.content.find('--help') != -1:
            arr.append('-h')
        else:
            text = re.findall(r'"([^"]*)"', message.content)[0]
            if len(text) > 0:
                arr.append('-t')
                arr.append('"{}"'.format(text))
            if indexFind(args, '-n') != -1:
                arr.append('-n')
                arr.append(indexFind(args, '-n') + 1)
            elif indexFind(args, '--num') != -1:
                arr.append('-n')
                arr.append(indexFind(args, '--num') + 1)
                
            if indexFind(args, '-l') != -1:
                langs = args[indexFind(args, '-l'):]
                arr.append('-l')
                for elem in langs:
                    arr.append(elem)
            print(arr)
        result = subprocess.check_output(" ".join(arr), shell=True)
        
        await client.send_message(message.channel, result.decode())

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)