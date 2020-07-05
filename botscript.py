import re
import asyncio

from discord.ext import commands
from googletrans import Translator

import config
import utils

TOKEN = config.TOKEN
HELP_TEXT = utils.HELP_TEXT

client = commands.Bot(command_prefix='!')

@client.event
async def on_error(event, *args, **kwargs):
    print("Error?")

async def background_translate(text, langs, times):
    translator = Translator()
    translation = text
    count = 0
    for i in range(times):
        for lang in langs:
            count += 1
            translation = translator.translate(translation, dest=lang).text
        translation = translator.translate(translation, dest='en').text
    
    print("Count: {}".format(count))
    
    endtext = '[*] "{}" but translated {} times!'.format(text.strip(), times*len(langs)) + "\n\n" + translation
    print("Output ready: {}".format(endtext))
    
    return endtext

@client.command()
async def translate(ctx):
    message = ctx.message
    
    # do not want the bot to reply to itself so
    if message.author == client.user:
        return
    
    message.content = '{}'.format(message.content)
    
    args = message.content.split('-')[1:]
    args = [arg.strip() for arg in args]
    
    langs = []
    n = -1
    text = ""
    
    print("=" * 50)
    print("New request received")
    
    for arg in args:
        if arg.startswith('h'):
            print("Help information requested")
            return await ctx.send(HELP_TEXT)
        
        if arg.startswith('l'):
            langs = arg.split(' ')[1:]
            if len(langs) == 0:
                return await ctx.send("Invalid language codes (-l): {}".format(message.content))
            
            print("Languages: {}".format(langs))
        if arg.startswith('n'):
            try:
                n = int(arg.split(' ')[1])
            except ValueError:
                return await ctx.send("Invalid no. of translations (-n): {}".format(message.content))
            
            print("No. of translations: {}".format(n))
        if arg.startswith('t'):
            try:
                text = re.findall(r'"([^"]*)"', arg)[0] # regex for life
            except:
                return await ctx.send("Error in the text (-t): {}".format(message.content))
            
            print("Translation text: {}".format(text))
            
    if n == -1:
        n = 10   
    if len(langs) == 0:
        langs = ['de', 'ko', 'la', 'ja', 'eo'] # default
    if len(text) == 0:
        return await ctx.send("No text provided (-t): {}".format(message.content))
    
    print(text, langs, n)
    
    translated = await background_translate(text, langs, n)
    
    await ctx.send(translated)
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)