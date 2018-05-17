import discord
import subprocess
import re
import os
import asyncio
import argparse
from googletrans import Translator
from . import config

TOKEN = config.TOKEN

client = discord.Client()
        
def rgt(text, langs, times):
	translator = Translator()

	translation = text
	for i in range(times):
		for lang in langs:
			translation = translator.translate(translation, dest=lang).text
		translation = translator.translate(translation, dest='en').text

	return translation

@client.event
async def on_message(message):
    # do not want the bot to reply to itself so
    if message.author == client.user:
        return
    if message.content.startswith('!translate'):
        message.content = '{}'.format(message.content)
        args = message.content.split('-')
        args = args[1:]
        langs = []
        n = -1
        text = ""
        for elem in args:
            elem = '-' + elem.strip()
            if elem.find('-l') != -1:
                templangs = elem.split(' ')[1:]
                print(templangs)
            if elem.find('-n') != -1:
                n = int(elem.split(' ')[1])
                print(n)
            if elem.find('-t') != -1:
                try:
                    text = re.findall(r'"([^"]*)"', elem)[0] # regex for life
                except:
                    text = "error in the text"
                print(text)
                
        if n == -1:
            n = 10
        if len(langs) == 0:
            langs = default=['de', 'ko', 'la', 'ja', 'eo']
        if len(text) == 0:
            text = "no text"
        endtext = '[*] "{}" but translated {} times!'.format(text.strip(), n*len(langs)) + "\n\n"
        endtext += rgt(text, langs, n)
        print("output sent")
        
        await client.send_message(message.channel, endtext)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)