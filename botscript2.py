import os, re, shlex

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

def find_in_list(lis, char):
    try:
        char_ind = lis.index(char)
        return char_ind
    except ValueError:
        return -1

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
    
    request = '{}'.format(message.content)
    
    print("=" * 50)
    print("New request received")
    
    args = shlex.split(request)
    
    l_ind = find_in_list(args, "-l")
    n_ind = find_in_list(args, "-n")
    t_ind = find_in_list(args, "-t")
    h_ind = find_in_list(args, "-h")
    
    if h_ind != -1:
        print("Help information requested")
        return await ctx.send(HELP_TEXT)
    
    if t_ind == -1 or len(args[t_ind+1:]) == 0:
        return await ctx.send("No text provided (-t): {}".format(request))
    
    text = " ".join(args[t_ind+1:])
    
    if max(l_ind, n_ind, t_ind) != t_ind:
        return await ctx.send("Optional arguments (-l,-n) should be positioned before the text argument (-t): {}".format(request))
    
    if n_ind != -1:
        n = 10
    else:
        try:
            n = int(args[n_ind+1])
        except ValueError:
            return await ctx.send("Invalid no. of translations (-n): {}".format(request))
    
    if l_ind != -1:
        langs = ['de', 'ko', 'la', 'ja', 'eo'] # default
    else:
        ind = l_ind
        while not ind in (n_ind, t_ind, h_ind):
            ind += 1
            
        langs = args[l_ind:ind]
        
        if len(langs) == 0: # also do check if codes are part of ISO standard
            return await ctx.send("Invalid language codes (-l): {}".format(request))
    
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