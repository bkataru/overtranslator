import os, re, shlex

from discord.ext import commands
from googletrans import Translator, LANGCODES

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
    print("Internal Error :(")

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
    print("S - Output ready: {}".format(endtext))
    
    await ctx.send(endtext)

@client.command()
async def translate(ctx):
    message = ctx.message
    # do not want the bot to reply to itself so
    if message.author == client.user:
        return
    
    request = '{}'.format(message.content)
    
    print("=" * 50)
    print("S - New request received")
    
    args = shlex.split(request)
    
    l_ind = find_in_list(args, "-l")
    n_ind = find_in_list(args, "-n")
    t_ind = find_in_list(args, "-t")
    h_ind = find_in_list(args, "-h")
    
    if h_ind != -1:
        print("S - Help information requested")
        return await ctx.send(HELP_TEXT)
    
    await ctx.send("Translation request received (⌐■_■)")
    
    if t_ind == -1 or len(args[t_ind+1:]) == 0:
        print("E - No text provided (-t): {}".format(request))
        return await ctx.send("Error - No text provided (-t): {}".format(request))
    
    text = " ".join(args[t_ind+1:])
    
    if max(l_ind, n_ind, t_ind) != t_ind:
        print("E - Optional arguments (-l,-n) should be positioned before the text argument (-t): {}".format(request))
        return await ctx.send("Error - Optional arguments (-l,-n) should be positioned before the text argument (-t): {}".format(request))
    
    if n_ind == -1:
        n = 10
    else:
        try:
            n = int(args[n_ind+1])
        except ValueError:
            print("E - Invalid no. of translations (-n): {}".format(request))
            return await ctx.send("Error - Invalid no. of translations (-n): {}".format(request))
    
    if l_ind == -1:
        langs = ['de', 'ko', 'la', 'ja', 'eo'] # default
    else:
        ind = l_ind
        while not ind in (n_ind, t_ind, h_ind):
            ind += 1
        
        langs = args[l_ind+1:ind]
        
        if len(langs) == 0:
            print("E - No language codes provided (-l), please refer to the help command (-h) for valid codes : {}".format(request))
            return await ctx.send("Error - No language codes provided (-l), please refer to the help command (-h) for valid codes : {}".format(request))
        
        invalid = [lang for lang in langs if not lang in list(LANGCODES.values())]
        
        if len(invalid) != 0:
            print("E - Invalid language code(s) provided (-l): {}. Please refer to the help command (-h) for valid codes: {}".format(" ".join(invalid), request))
            return await ctx.send("Error - Invalid language code(s) provided (-l): {}. Please refer to the help command (-h) for valid codes: {}".format(" ".join(invalid), request))
        
        
    print("S - Languages: {}".format(langs))
    print("S - No. of iterations: {}".format(n))
    print("S - Text to be translated: {}".format(text))

    await background_translate(ctx, text, langs, n)
    
@client.event
async def on_ready():
    print('S - Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

if __name__ == "__main__":
    client.run(TOKEN)