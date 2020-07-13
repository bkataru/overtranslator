import os, re

from discord.ext import commands
from googletrans import Translator

import utils

try:
    import config
    TOKEN = config.TOKEN
except:
    TOKEN = os.environ.get("TOKEN")

HELP_TEXT = utils.HELP_TEXT

client = commands.Bot(command_prefix='!')

translator = Translator()

@client.event
async def on_error(event, *args, **kwargs):
    print("Error?")

async def background_translate(ctx, text, langs, times):
    translation = text
    for i in range(times):
        for lang in langs:
            translation = translator.translate(translation, dest=lang).text
        translation = translator.translate(translation, dest='en').text

    endtext = '[*] "{}" but translated {} times!'.format(text.strip(), times*len(langs)) + "\n\n" + translation
    print("Output ready: {}".format(endtext))
    
    await ctx.send(endtext)

@client.command()
async def translate(ctx):
    message = ctx.message
    
    # do not want the bot to reply to itself so
    if message.author == client.user:
        return
    
    message.content = '{}'.format(message.content)
    
    request = message.content.split("!translate")[1].strip()
    
    t_ind = request.find("-t")
    text = request[t_ind+2:].strip()
    options_str = request[:t_ind].strip()
    
    print(text)
    
    args = options_str.split('-')[1:]
    args = [arg.strip() for arg in args]
    
    langs = []
    n = -1
    
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
            
        if arg.startswith('n'):
            try:
                n = int(arg.split(' ')[1])
            except ValueError:
                return await ctx.send("Invalid no. of translations (-n): {}".format(message.content))
        
    if n == -1:
        n = 10
    if len(langs) == 0:
        langs = ['de', 'ko', 'la', 'ja', 'eo'] # default
    if len(text) == 0:
        return await ctx.send("No text provided (-t): {}".format(message.content))
    
    print("Languages: {}".format(langs))
    print("No. of iterations: {}".format(n))
    print("Text to be translated: {}".format(text))

    await background_translate(ctx, text, langs, n)
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)